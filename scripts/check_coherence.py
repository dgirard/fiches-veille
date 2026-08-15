#!/usr/bin/env python3
"""check_coherence.py — « doctor » : l'état du dépôt est-il cohérent ?

Sortie compacte (token-lean), une ligne par check. Code de retour ≠ 0 dès qu'un
check est STALE ou FAIL (WARN et SKIP n'échouent pas).

    python3 scripts/check_coherence.py                  # tous les checks
    python3 scripts/check_coherence.py --catalogue-only # (a) seul, avant lecture

Checks : (a) fraîcheur catalogue, (b) fraîcheur KB, (c) bijection
catalogue↔fiches, (d) retard des KB thématiques, (e) quasi-doublons d'entités,
(f) bloc stats README, (g) raw-data (best-effort), (h) dérive de nommage
Triples↔Entités. Stdlib uniquement.
"""

from __future__ import annotations

import difflib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_index as bi  # noqa: E402
import build_knowledge_base as bk  # noqa: E402

OK, STALE, FAIL, WARN, SKIP = "OK", "STALE", "FAIL", "WARN", "SKIP"
BLOCKING = {STALE, FAIL}

# Périmètres déclarés des KB thématiques (table interne — check (d)).
KB_THEMATIQUES = {
    "kb-context-engineering.md": {
        "themes": {"agents-codage-ia-skills"},
        "keywords": ["context engineering", "contexte", "mémoire", "memory"],
    },
    "kb-commerce-agentique.md": {
        "themes": {"economie-marche", "produits-services"},
        "keywords": ["commerce agentique", "agentic commerce", "mcp-ui"],
    },
    "kb-skills.md": {
        "themes": {"agents-codage-ia-skills"},
        "keywords": ["skill", "skill.md"],
    },
    "kb-souverainete.md": {
        "themes": set(),
        "keywords": ["souverain", "cloud act", "secnumcloud", "extraterritorial",
                     "cloud de confiance", "réversibilité", "scaleway"],
    },
}


def _stored_catalogue_manifest(catalogue: Path) -> str | None:
    if not catalogue.exists():
        return None
    first = catalogue.read_text(encoding="utf-8").splitlines()[:1]
    if not first:
        return None
    m = re.search(r"sha256:([0-9a-f]+)", first[0])
    return m.group(1) if m else None


def _stored_kb_manifest(kb_dashboard: Path) -> str | None:
    if not kb_dashboard.exists():
        return None
    m = re.search(r"manifest:\s*sha256=([0-9a-f]+)", kb_dashboard.read_text(encoding="utf-8"))
    return m.group(1) if m else None


def check_catalogue(root: Path) -> tuple[str, str, str]:
    catalogue = root / "catalogue.tsv"
    if not catalogue.exists():
        return "a. fraîcheur catalogue", SKIP, "catalogue.tsv absent (avant bascule)"
    stored = _stored_catalogue_manifest(catalogue)
    live = bi.compute_manifest(bi.collect(root / "fiches"))
    if stored == live:
        return "a. fraîcheur catalogue", OK, ""
    return ("a. fraîcheur catalogue", STALE,
            "catalogue périmé → python3 scripts/build_index.py")


def check_kb(root: Path) -> tuple[str, str, str]:
    dashboard = root / "knowledge-base.md"
    if not dashboard.exists():
        return "b. fraîcheur KB", SKIP, "knowledge-base.md absent"
    stored = _stored_kb_manifest(dashboard)
    live, _ = bk.compute_kb_manifest(root / "fiches")
    if stored == live:
        return "b. fraîcheur KB", OK, ""
    return ("b. fraîcheur KB", STALE,
            "kb/ périmé → python3 scripts/build_knowledge_base.py")


def check_bijection(root: Path) -> tuple[str, str, str]:
    catalogue = root / "catalogue.tsv"
    if not catalogue.exists():
        return "c. bijection catalogue↔fiches", SKIP, "catalogue.tsv absent"
    # Ids réellement listés dans le catalogue stocké (ligne manifest + en-tête sautées).
    lines = catalogue.read_text(encoding="utf-8").splitlines()
    catalogued = {ln.split("\t")[0] for ln in lines[2:] if ln.strip()}
    on_disk = {p.stem for p in (root / "fiches").rglob("*.md")}
    problems = ([f"catalogue → fiche absente : {i}" for i in sorted(catalogued - on_disk)]
                + [f"fiche non cataloguée : {i}" for i in sorted(on_disk - catalogued)])
    if not problems:
        return "c. bijection catalogue↔fiches", OK, ""
    return ("c. bijection catalogue↔fiches", FAIL,
            f"{len(problems)} écart(s) : " + " ; ".join(problems[:3]))


def check_kb_thematiques(root: Path) -> tuple[str, str, str]:
    records = bi.collect(root / "fiches")
    retards = []
    for fname, perim in KB_THEMATIQUES.items():
        path = root / fname
        if not path.exists():
            continue
        head = "\n".join(path.read_text(encoding="utf-8").splitlines()[:8])
        # Première date ISO de l'en-tête = date de génération/mise à jour.
        m = re.search(r"(\d{4}-\d{2}-\d{2})", head)
        if not m:
            continue
        since = m.group(1)
        kws = [k.lower() for k in perim["keywords"]]
        n = 0
        for r in records:
            if r["date"] <= since:
                continue
            hay = (r["titre"] + " " + r["veille_courte"] + " "
                   + " ".join(r["keywords"])).lower()
            if perim["themes"] & set(r["themes"]) or any(k in hay for k in kws):
                n += 1
        if n:
            retards.append(f"{fname}: {n} depuis {since}")
    if not retards:
        return "d. KB thématiques à jour", OK, ""
    return "d. KB thématiques à jour", WARN, " ; ".join(retards)


def check_quasi_doublons(root: Path) -> tuple[str, str, str]:
    all_e = []
    for p in sorted((root / "fiches").rglob("*.md")):
        _, ents, fid = bk.extract_graphe_connaissance(str(p))
        for e in ents:
            all_e.append((e, fid))
    # Mêmes fusions que le build, sinon le doctor réclame des arbitrages déjà
    # rendus dans entity_aliases.tsv.
    fusion_map, distinct_map = bk.load_entity_aliases(root / "scripts")
    for e, _fid in all_e:
        entry = fusion_map.get(bk.normalize_name(e.get("Entité", "")))
        if entry:
            e["Entité"], e["Type"] = entry
    unique = bk.deduplicate_entities(all_e)
    rep = bk.quasi_duplicate_report(unique, distinct_map)
    if not rep:
        return "e. quasi-doublons entités", OK, ""
    return ("e. quasi-doublons entités", WARN,
            f"{len(rep)} groupe(s) à arbitrer (entity_aliases.tsv) : "
            + " ; ".join(rep[:3]))


def check_readme(root: Path) -> tuple[str, str, str]:
    readme = root / "README.md"
    if not readme.exists():
        return "f. bloc stats README", SKIP, "README.md absent"
    text = readme.read_text(encoding="utf-8")
    if bi.README_BEGIN not in text or bi.README_END not in text:
        return "f. bloc stats README", SKIP, "marqueurs stats absents"
    records = bi.collect(root / "fiches")
    themes = bi.load_themes(root / "scripts")
    expected = "\n".join(bi.render_stats_block(records, themes))
    current = re.search(re.escape(bi.README_BEGIN) + r"(.*?)" + re.escape(bi.README_END),
                        text, re.DOTALL)
    if current and expected.strip() in current.group(1):
        return "f. bloc stats README", OK, ""
    return ("f. bloc stats README", WARN,
            "stats README périmées → python3 scripts/build_index.py")


def check_raw_data(root: Path) -> tuple[str, str, str]:
    raw = root / "raw-data"
    if not raw.exists():
        return "g. raw-data (local)", WARN, "raw-data/ absent (normal sur clone frais)"
    have = {p.stem for p in raw.glob("*.md")}
    fiches = {p.stem for p in (root / "fiches").rglob("*.md")}
    missing = fiches - have
    if not missing:
        return "g. raw-data (local)", OK, ""
    return "g. raw-data (local)", WARN, f"{len(missing)} fiche(s) sans raw archivé"


def _drift_key(name: str) -> str:
    """Clé de comparaison d'un nom d'entité : parenthèses et ponctuation retirées."""
    s = re.sub(r"\(.*?\)", " ", name)
    s = re.sub(r"[^\w\s]", " ", s, flags=re.UNICODE).lower()
    return re.sub(r"\s+", " ", s).strip()


def _is_sublist(petit: list[str], grand: list[str]) -> bool:
    """`petit` est-il une suite contiguë de mots de `grand` ?"""
    n = len(petit)
    return any(grand[i:i + n] == petit for i in range(len(grand) - n + 1))


def _is_drift(triple_key: str, declared_key: str) -> bool:
    """Le nom d'un triple est-il une variante d'une entité déclarée de la fiche ?

    Containment au **mot** près, jamais au caractère : « Uber » ⊂ « Uber
    Engineering » est une dérive, mais « B » ⊄ « Uber » (la sous-chaîne nue
    ferait matcher n'importe quel nom court dans n'importe quel nom long).
    """
    if not triple_key or not declared_key:
        return False
    if triple_key == declared_key:
        return True
    a, b = triple_key.split(), declared_key.split()
    if _is_sublist(a, b) or _is_sublist(b, a):
        return True
    # Typo / accent / séparateur : exiger une longueur minimale, sinon les noms
    # de 2-3 caractères (IA, ACP, 996…) se ressemblent tous.
    if min(len(triple_key), len(declared_key)) < 5:
        return False
    return difflib.SequenceMatcher(None, triple_key, declared_key).ratio() > 0.86


def check_derive_nommage(root: Path) -> tuple[str, str, str]:
    """(h) Entité d'un triple qui est une variante d'une entité déclarée voisine.

    Ex. les triples disent `Uber` là où la table `### Entités` déclare
    `Uber Engineering` : la dédup les traite comme deux entités distinctes et le
    savoir se scinde. Une entité de triple **absente** de la table n'est pas
    signalée — la table Entités n'est pas un miroir des triples (cf.
    `docs/reference/ontologie-kg.md`), seule la variante d'un nom déjà déclaré
    dans la MÊME fiche traduit une perte.
    """
    fusion_map, _ = bk.load_entity_aliases(root / "scripts")
    total = 0
    fiches_touchees = []
    for p in sorted((root / "fiches").rglob("*.md")):
        triples, ents, fiche_id = bk.extract_graphe_connaissance(str(p))
        declared = {bk.normalize_name(bk.apply_fusion_name(e.get("Entité", ""), fusion_map))
                    for e in ents if e.get("Entité", "").strip()}
        declared_keys = {_drift_key(d): d for d in declared}
        noms = set()
        for t in triples:
            for col, tcol in (("Sujet", "Type Sujet"), ("Objet", "Type Objet")):
                nom = t.get(col, "").strip()
                if nom and t.get(tcol, "").strip() not in bk.EPISTEMIC_TYPES:
                    noms.add(bk.apply_fusion_name(nom, fusion_map))
        n = sum(1 for nom in noms
                if bk.normalize_name(nom) not in declared
                and any(_is_drift(_drift_key(nom), dk) for dk in declared_keys))
        if n:
            total += n
            fiches_touchees.append((n, fiche_id))
    if not total:
        return "h. dérive nommage Triples↔Entités", OK, ""
    fiches_touchees.sort(reverse=True)
    tete = " ; ".join(f"{fid} ({n})" for n, fid in fiches_touchees[:3])
    return ("h. dérive nommage Triples↔Entités", WARN,
            f"{total} variante(s) dans {len(fiches_touchees)} fiche(s) : {tete}")


CHECKS_FULL = [check_catalogue, check_kb, check_bijection, check_kb_thematiques,
               check_quasi_doublons, check_readme, check_raw_data,
               check_derive_nommage]


def run(root: Path, catalogue_only: bool = False) -> int:
    checks = [check_catalogue] if catalogue_only else CHECKS_FULL
    results = [c(root) for c in checks]
    width = max(len(label) for label, _, _ in results)
    blocking = False
    for label, status, detail in results:
        tail = f"  {detail}" if detail else ""
        print(f"  {label.ljust(width)}  {status}{tail}")
        if status in BLOCKING:
            blocking = True
    if blocking:
        print("\n✗ doctor : incohérence(s) bloquante(s) — régénérer avant de committer/lire.")
        return 1
    print("\n✓ doctor : cohérent (WARN non bloquants).")
    return 0


def main(argv: list[str]) -> int:
    root = Path(__file__).resolve().parent.parent
    catalogue_only = "--catalogue-only" in argv[1:]
    return run(root, catalogue_only)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
