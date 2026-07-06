#!/usr/bin/env python3
"""build_index.py — génère catalogue.tsv, index.md et le bloc stats de README.md.

Génération 100 % déterministe depuis les fiches (aucune prose produite). Deux
lancements sans changement d'entrée produisent des fichiers identiques octet pour
octet (manifest inclus).

    python3 scripts/build_index.py                 # écrit à la racine du dépôt
    python3 scripts/build_index.py --out-dir DIR   # écrit ailleurs (tests)
    python3 scripts/build_index.py --verify        # vérifie les liens, exit≠0 sinon

Contrats de format : voir docs/plans/…-scalabilite-1000-fiches (section
« Spécifications des formats »). Stdlib uniquement.
"""

from __future__ import annotations

import hashlib
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiche_lib import parse_fiche  # noqa: E402

CATALOGUE_COLS = ["id", "date", "titre", "auteurs", "source",
                  "themes", "keywords", "veille_courte", "flags"]
VEILLE_MAX = 200
ALIAS_STATS_TOP = 20


# ─── Helpers ─────────────────────────────────────────────────────────────────


def load_themes(scripts_dir: Path) -> dict[str, str]:
    """Charge scripts/themes.tsv → dict ordonné {slug: libellé} (ordre du fichier)."""
    themes: dict[str, str] = {}
    path = scripts_dir / "themes.tsv"
    if not path.exists():
        return themes
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        if i == 0 or not line.strip():
            continue
        parts = line.split("\t")
        if len(parts) >= 2:
            themes[parts[0].strip()] = parts[1].strip()
    return themes


def tsv_clean(value: str) -> str:
    """Neutralise tab/retour et réduit les espaces multiples (sûr en TSV)."""
    return re.sub(r"\s+", " ", value.replace("\t", " ")).strip()


def strip_markdown(text: str) -> str:
    """Retire l'emphase markdown la plus courante pour un résumé en clair."""
    text = re.sub(r"[*_`]+", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)  # [texte](url) → texte
    return text


def veille_courte(fiche) -> str:
    """Premiers VEILLE_MAX caractères du texte ## Veille, coupés sur un mot."""
    raw = fiche.sections.get("Veille", "")
    text = tsv_clean(strip_markdown(raw))
    if len(text) <= VEILLE_MAX:
        return text
    cut = text[:VEILLE_MAX].rsplit(" ", 1)[0]
    return cut + "…"


def keywords_list(fiche) -> list[str]:
    """Keywords de la fiche (ligne séparée par des virgules) → liste nettoyée."""
    return [k.strip() for k in fiche.keywords.split(",") if k.strip()]


def primary_author(auteurs: str) -> str:
    """Auteur principal (heuristique déterministe) pour l'agrégat statistique."""
    head = re.split(r"[(,&]|—|·|/", auteurs, 1)[0]
    return re.sub(r"[*_`]", "", head).strip()


def link_text(titre: str) -> str:
    """Texte de lien markdown sûr (crochets → parenthèses)."""
    return titre.replace("[", "(").replace("]", ")")


def flags_of(fiche) -> list[str]:
    f = []
    if not fiche.has_kg:
        f.append("sans-kg")
    if fiche.is_skill:
        f.append("skill")
    if fiche.is_promotion:
        f.append("promotion")
    return f


# ─── Collecte ────────────────────────────────────────────────────────────────


def collect(fiches_dir: Path) -> list[dict]:
    """Parse toutes les fiches → enregistrements normalisés, triés (date desc, id asc)."""
    records = []
    for path in sorted(fiches_dir.rglob("*.md")):
        fiche = parse_fiche(path)
        rel = path.relative_to(fiches_dir.parent).as_posix()
        records.append({
            "id": fiche.id,
            "date": fiche.date,
            "titre": tsv_clean(fiche.titre),
            "auteurs": tsv_clean(fiche.auteurs),
            "source": tsv_clean(fiche.source),
            "themes": fiche.themes,
            "keywords": keywords_list(fiche),
            "veille_courte": veille_courte(fiche),
            "flags": flags_of(fiche),
            "rel": rel,
            "veille_raw": fiche.sections.get("Veille", ""),
        })
    # Ordre total déterministe : date décroissante, puis id croissant.
    records.sort(key=lambda r: (_neg_date(r["date"]), r["id"]))
    return records


def _neg_date(d: str) -> str:
    """Clé de tri pour ordre date décroissant lexicographique."""
    # Inverse chaque caractère numérique pour trier desc via sort asc.
    return "".join(chr(255 - ord(c)) for c in d)


# ─── Manifest ────────────────────────────────────────────────────────────────


def compute_manifest(records: list[dict]) -> str:
    """sha256 des champs consommés par build_index (fiches triées par chemin)."""
    h = hashlib.sha256()
    for r in sorted(records, key=lambda r: r["rel"]):
        payload = "\x1f".join([
            r["rel"], r["date"], r["titre"], r["auteurs"],
            r["veille_raw"], ",".join(r["keywords"]),
            "1" if "sans-kg" not in r["flags"] else "0",
        ])
        h.update((payload + "\x1e").encode("utf-8"))
    return h.hexdigest()


# ─── Rendu catalogue.tsv ─────────────────────────────────────────────────────


def render_catalogue(records: list[dict], manifest: str, today: str) -> str:
    lines = [
        f"#manifest\tsha256:{manifest}\tfiches:{len(records)}\tgenere:{today}",
        "\t".join(CATALOGUE_COLS),
    ]
    for r in records:
        lines.append("\t".join([
            r["id"], r["date"], r["titre"], r["auteurs"], r["source"],
            ";".join(r["themes"]), ";".join(r["keywords"]),
            r["veille_courte"], ";".join(r["flags"]),
        ]))
    return "\n".join(lines) + "\n"


# ─── Rendu index.md ──────────────────────────────────────────────────────────


def render_stats_block(records: list[dict], themes: dict[str, str]) -> list[str]:
    """Bloc statistiques partagé (index.md et README.md)."""
    from collections import Counter
    lines = []
    total = len(records)
    lines.append(f"- **Total** : {total} fiches")

    by_year = Counter(r["date"][:4] for r in records if r["date"])
    lines.append("- **Par année** : " + " · ".join(
        f"{y} ({n})" for y, n in sorted(by_year.items(), reverse=True)))

    by_theme = Counter(t for r in records for t in r["themes"])
    if by_theme:
        lines.append("- **Par thème** :")
        for slug in themes:
            if by_theme.get(slug):
                lines.append(f"  - {themes[slug]} : {by_theme[slug]}")

    authors = Counter(primary_author(r["auteurs"]) for r in records if r["auteurs"])
    lines.append("- **Auteurs (top 20)** :")
    for name, n in authors.most_common(ALIAS_STATS_TOP):
        lines.append(f"  - {name} ({n})")

    sources = Counter(r["source"] for r in records if r["source"])
    if sources:
        lines.append("- **Sources (top 20)** :")
        for name, n in sources.most_common(ALIAS_STATS_TOP):
            lines.append(f"  - {name} ({n})")
    return lines


def render_index(records: list[dict], themes: dict[str, str], today: str) -> str:
    from itertools import groupby
    lines = ["# Veille Technologique", ""]
    total = len(records)
    dates = [r["date"] for r in records if r["date"]]
    periode = f"{min(dates)} → {max(dates)}" if dates else "—"
    lines.append(f"> {total} fiches | {periode} | généré le {today}")
    lines.append("")
    lines.append("_Index généré par `scripts/build_index.py` — ne pas éditer à la main._")
    lines.append("")

    # Articles par mois (antichronologique)
    lines.append("## Articles par mois")
    lines.append("")
    by_month = {}
    for r in records:
        by_month.setdefault(r["date"][:7], []).append(r)
    for month in sorted(by_month, reverse=True):
        lines.append(f"### {month}")
        lines.append("")
        for r in by_month[month]:  # déjà triés date desc, id asc
            jj = r["date"][8:10] if len(r["date"]) >= 10 else "??"
            kws = ", ".join(r["keywords"][:3])
            src = f" · {r['source']}" if r["source"] else ""
            suffix = f" — {kws}" if kws else ""
            lines.append(f"- **{jj}** [{link_text(r['titre'])}]({r['rel']}) "
                         f"— {r['auteurs']}{src}{suffix}")
        lines.append("")

    # Thématiques
    lines.append("## Thématiques")
    lines.append("")
    for slug, libelle in themes.items():
        matched = [r for r in records if slug in r["themes"]]
        if not matched:
            continue
        lines.append(f"### {libelle}")
        lines.append("")
        for r in matched:
            lines.append(f"- [{link_text(r['titre'])}]({r['rel']}) — {r['auteurs']}")
        lines.append("")

    # Statistiques
    lines.append("## Statistiques")
    lines.append("")
    lines.extend(render_stats_block(records, themes))
    lines.append("")
    return "\n".join(lines)


# ─── README stats block ──────────────────────────────────────────────────────

README_BEGIN = "<!-- stats:begin -->"
README_END = "<!-- stats:end -->"


def update_readme(readme_path: Path, records: list[dict], themes: dict[str, str]) -> str:
    """Remplace le contenu entre marqueurs. Retourne 'ok' | 'no-markers' | 'absent'."""
    if not readme_path.exists():
        return "absent"
    text = readme_path.read_text(encoding="utf-8")
    if README_BEGIN not in text or README_END not in text:
        return "no-markers"
    block = "\n".join([README_BEGIN, ""] + render_stats_block(records, themes)
                      + ["", README_END])
    new = re.sub(
        re.escape(README_BEGIN) + r".*?" + re.escape(README_END),
        block.replace("\\", "\\\\"), text, count=1, flags=re.DOTALL,
    )
    readme_path.write_text(new, encoding="utf-8")
    return "ok"


# ─── Vérification ────────────────────────────────────────────────────────────


def verify(records: list[dict], repo_root: Path) -> list[str]:
    """Chaque enregistrement pointe vers un fichier existant et réciproquement."""
    problems = []
    on_disk = {p.relative_to(repo_root).as_posix()
               for p in (repo_root / "fiches").rglob("*.md")}
    catalogued = {r["rel"] for r in records}
    for rel in sorted(catalogued - on_disk):
        problems.append(f"catalogue → fichier absent : {rel}")
    for rel in sorted(on_disk - catalogued):
        problems.append(f"fiche non cataloguée : {rel}")
    return problems


# ─── Main ────────────────────────────────────────────────────────────────────


def main(argv: list[str]) -> int:
    scripts_dir = Path(__file__).resolve().parent
    repo_root = scripts_dir.parent
    out_dir = repo_root
    do_verify = False
    args = argv[1:]
    i = 0
    while i < len(args):
        if args[i] == "--out-dir":
            out_dir = Path(args[i + 1]); i += 2
        elif args[i] == "--verify":
            do_verify = True; i += 1
        else:
            print(f"argument inconnu : {args[i]}"); return 2

    fiches_dir = repo_root / "fiches"
    records = collect(fiches_dir)
    themes = load_themes(scripts_dir)
    today = date.today().isoformat()

    if do_verify:
        problems = verify(records, repo_root)
        if problems:
            print(f"✗ {len(problems)} problème(s) de liens :")
            for p in problems:
                print(f"  - {p}")
            return 1
        print(f"✓ {len(records)} fiches — liens cohérents.")
        return 0

    manifest = compute_manifest(records)
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "catalogue.tsv").write_text(
        render_catalogue(records, manifest, today), encoding="utf-8")
    (out_dir / "index.md").write_text(
        render_index(records, themes, today), encoding="utf-8")
    readme_state = update_readme(out_dir / "README.md", records, themes)

    print(f"✓ catalogue.tsv + index.md générés ({len(records)} fiches). "
          f"README : {readme_state}. Manifest : {manifest[:12]}…")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
