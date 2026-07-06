#!/usr/bin/env python3
"""lint_fiches.py — gate Bronze : validation des fiches contre l'ontologie v2.

    python3 scripts/lint_fiches.py            # valide fiches/**/*.md
    python3 scripts/lint_fiches.py chemin.md  # valide une fiche précise

Règles (CLAUDE.md « Section GrapheDeConnaissance » + docs/specs/knowledge-base-construction.md) :
- les 10 sections présentes, dans l'ordre ;
- en-têtes de tableaux exacts, accents compris (`Prédicat`, `Entité`, `Temporalité`) —
  le padding d'alignement des cellules est toléré, pas les libellés approximatifs ;
- prédicats dans le registre fermé des 30 ;
- types sujet/objet dans les 8 types d'entités (+ 3 types épistémiques, objets seulement) ;
- objets épistémiques (AFFIRMATION/MESURE/CITATION) jamais sujets, jamais dans la table Entités ;
- confiance numérique ≥ 0.70 ; Temporalité et Source dans leurs vocabulaires fermés ;
- frontmatter YAML de promotion toléré (même skip que `extract_fiche_veille()`).

Sortie : rapport en français par fiche fautive + récapitulatif. Exit code 1 dès la
première violation (validation bloquante, pas indicative). Stdlib uniquement.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiche_lib import (  # noqa: E402
    FrontmatterError,
    load_themes as _load_themes_map,
    parse_frontmatter,
    skip_frontmatter,
    split_sections,
)

# ─── Ontologie v2 — vocabulaires fermés ──────────────────────────────────────

# Registre fermé des clés de frontmatter éditorial autorisées (U2).
CLES_FRONTMATTER = {
    # Éditorial
    "themes", "source",
    # Promotion cabinet (v3)
    "cabinet_promotion_candidate", "proposed_class", "proposed_capability", "notes",
    # Skill
    "fiche_type", "skill_source", "skill_author",
}

def load_themes() -> set | None:
    """Ensemble des slugs de thèmes valides (None si themes.tsv absent → check
    valeurs-de-thèmes désactivé plutôt que bloquant)."""
    themes = _load_themes_map(Path(__file__).resolve().parent)
    return set(themes) if themes else None

SECTIONS_ATTENDUES = [
    "Veille",
    "Titre Article",
    "Date",
    "URL",
    "Keywords",
    "Authors",
    "Ton",
    "Pense-betes",
    "RésuméDe400mots",
    "GrapheDeConnaissance",
]

PREDICATS = {
    # Structurels (5)
    "fait_partie_de", "est_instance_de", "est_variante_de", "remplace", "publie",
    # Épistémiques (9)
    "affirme_que", "soutient", "s_oppose_à", "affine", "prédit", "mesure",
    "est_basé_sur", "s_inspire_de", "référence",
    # Opérationnels (8)
    "utilise", "permet", "améliore", "réduit", "résout", "s_applique_à",
    "observé_dans", "recommande",
    # Marché (5)
    "concurrence", "surpasse", "converge_avec", "collabore_avec", "a_créé",
    # Personnes (3)
    "travaille_chez", "dirige", "emploie",
}

TYPES_ENTITES = {
    "PERSONNE", "ORGANISATION", "TECHNOLOGIE", "CONCEPT",
    "METHODOLOGIE", "EVENEMENT", "LIEU", "DOCUMENT",
}
TYPES_EPISTEMIQUES = {"AFFIRMATION", "MESURE", "CITATION"}

TEMPORALITES = {"STATIQUE", "DYNAMIQUE", "ATEMPOREL"}
SOURCES = {"déclaré_article", "inféré", "généré_assistant"}

SEUIL_CONFIANCE = 0.70

EN_TETE_TRIPLES = [
    "Sujet", "Type Sujet", "Prédicat", "Objet",
    "Type Objet", "Confiance", "Temporalité", "Source",
]
EN_TETE_ENTITES = ["Entité", "Type", "Attribut", "Valeur", "Action"]


# ─── Parsing ─────────────────────────────────────────────────────────────────

def _cells(row: str) -> list[str]:
    """Cellules d'une ligne de tableau markdown, nettoyées (padding toléré)."""
    return [c.strip() for c in row.strip().strip("|").split("|")]


def _is_separator(row: str) -> bool:
    return bool(re.match(r"^\s*\|[\s\-:|]+\|\s*$", row))


def _table_rows(lines: list[str], start: int) -> tuple[list[str] | None, list[list[str]]]:
    """À partir de `start`, trouve le premier tableau : (en-tête, lignes de données)."""
    header = None
    rows: list[list[str]] = []
    for line in lines[start:]:
        s = line.strip()
        if s.startswith("###") or (s.startswith("## ") and header):
            break
        if not s.startswith("|"):
            if header:
                break
            continue
        if _is_separator(s):
            continue
        if header is None:
            header = s
        else:
            rows.append(_cells(s))
    return header, rows


# ─── Validation d'une fiche ──────────────────────────────────────────────────

def lint_text(text: str, nom: str) -> list[str]:
    """Valide le contenu d'une fiche ; retourne la liste des violations (en français)."""
    v: list[str] = []
    lines = skip_frontmatter(text.splitlines())

    # 1. Les 10 sections, présentes et dans l'ordre
    titres = [m.group(1).strip() for m in
              (re.match(r"^##\s+(.+?)\s*$", l) for l in lines) if m]
    manquantes = [s for s in SECTIONS_ATTENDUES if s not in titres]
    for s in manquantes:
        v.append(f"{nom} : section manquante « ## {s} »")
    presentes = [s for s in SECTIONS_ATTENDUES if s in titres]
    ordre_reel = [t for t in titres if t in SECTIONS_ATTENDUES]
    if not manquantes and ordre_reel != presentes:
        v.append(f"{nom} : sections présentes mais pas dans l'ordre attendu "
                 f"({' → '.join(ordre_reel)})")

    # 2. Tableaux du GrapheDeConnaissance
    idx_triples = idx_entites = None
    for i, l in enumerate(lines):
        if re.match(r"^###\s+Triples\s*$", l.strip()):
            idx_triples = i
        elif re.match(r"^###\s+Entités\s*$", l.strip()):
            idx_entites = i
    if "GrapheDeConnaissance" in titres and idx_triples is None:
        v.append(f"{nom} : sous-section « ### Triples » manquante")
    if "GrapheDeConnaissance" in titres and idx_entites is None:
        v.append(f"{nom} : sous-section « ### Entités » manquante")

    # 3. Table Triples
    if idx_triples is not None:
        header, rows = _table_rows(lines, idx_triples + 1)
        if header is None:
            v.append(f"{nom} : tableau Triples introuvable sous « ### Triples »")
        elif _cells(header) != EN_TETE_TRIPLES:
            v.append(f"{nom} : en-tête de tableau Triples non conforme "
                     f"(attendu accents compris : | {' | '.join(EN_TETE_TRIPLES)} | ; "
                     f"trouvé : {header.strip()})")
        else:
            for n, r in enumerate(rows, 1):
                if len(r) != 8:
                    v.append(f"{nom} : triple {n} — {len(r)} colonnes au lieu de 8")
                    continue
                sujet, t_sujet, predicat, objet, t_objet, confiance, tempo, source = r
                if t_sujet in TYPES_EPISTEMIQUES:
                    v.append(f"{nom} : triple {n} — un objet épistémique ({t_sujet}) "
                             f"ne peut pas être sujet (« {sujet} »)")
                elif t_sujet not in TYPES_ENTITES:
                    v.append(f"{nom} : triple {n} — type sujet invalide « {t_sujet} »")
                if t_objet not in TYPES_ENTITES | TYPES_EPISTEMIQUES:
                    v.append(f"{nom} : triple {n} — type objet invalide « {t_objet} »")
                if predicat not in PREDICATS:
                    v.append(f"{nom} : triple {n} — prédicat hors registre « {predicat} »")
                try:
                    c = float(confiance)
                    if c < SEUIL_CONFIANCE:
                        v.append(f"{nom} : triple {n} — confiance {confiance} "
                                 f"sous le seuil {SEUIL_CONFIANCE}")
                except ValueError:
                    v.append(f"{nom} : triple {n} — confiance non numérique « {confiance} »")
                if tempo not in TEMPORALITES:
                    v.append(f"{nom} : triple {n} — temporalité hors vocabulaire « {tempo} »")
                if source not in SOURCES:
                    v.append(f"{nom} : triple {n} — source hors vocabulaire « {source} »")

    # 4. Table Entités
    if idx_entites is not None:
        header, rows = _table_rows(lines, idx_entites + 1)
        if header is None:
            v.append(f"{nom} : tableau Entités introuvable sous « ### Entités »")
        elif _cells(header) != EN_TETE_ENTITES:
            v.append(f"{nom} : en-tête de tableau Entités non conforme "
                     f"(attendu accents compris : | {' | '.join(EN_TETE_ENTITES)} | ; "
                     f"trouvé : {header.strip()})")
        else:
            for n, r in enumerate(rows, 1):
                if len(r) != 5:
                    v.append(f"{nom} : entité {n} — {len(r)} colonnes au lieu de 5")
                    continue
                entite, type_, _attr, _val, action = r
                if type_ in TYPES_EPISTEMIQUES:
                    v.append(f"{nom} : entité {n} — type épistémique « {type_} » interdit "
                             f"dans la table Entités (« {entite} »)")
                elif type_ not in TYPES_ENTITES:
                    v.append(f"{nom} : entité {n} — type invalide « {type_} »")
                if action not in {"AJOUT", "MISE_A_JOUR", "INVALIDATION"}:
                    v.append(f"{nom} : entité {n} — action invalide « {action} »")

    return v


def _section_date(text: str) -> str:
    """Première ligne de contenu de la section ## Date (chaîne vide si absente)."""
    sections = split_sections(skip_frontmatter(text.splitlines()))
    for line in sections.get("Date", "").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            return s
    return ""


def lint_fiche(path: Path, warnings: list[str] | None = None,
               post_migration: bool = False) -> list[str]:
    """Valide une fiche sur disque ; retourne la liste des violations.

    Checks path-aware (U2) en plus des checks de contenu de `lint_text` :
    frontmatter (parse + registre fermé des clés), valeurs de thèmes contre
    `themes.tsv`, cohérence Date ↔ répertoire `fiches/YYYY-MM/`. Les avertissements
    non bloquants (ex. `themes` absent post-migration) sont ajoutés à `warnings`.
    """
    path = Path(path)
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as e:
        return [f"{path.name} : lecture impossible ({e})"]

    v = lint_text(text, path.name)

    # Frontmatter : parse + registre fermé des clés
    try:
        fm, _ = parse_frontmatter(text.splitlines())
    except FrontmatterError as e:
        v.append(f"{path.name} : frontmatter invalide — {e}")
        fm = {}
    for cle in fm:
        if cle not in CLES_FRONTMATTER:
            v.append(f"{path.name} : clé frontmatter hors registre « {cle} » "
                     f"(autorisées : {', '.join(sorted(CLES_FRONTMATTER))})")

    # Valeurs de thèmes contre le registre
    themes = fm.get("themes")
    themes_list = themes if isinstance(themes, list) else ([themes] if themes else [])
    slugs = load_themes()
    if themes_list and slugs is not None:
        for t in themes_list:
            if t not in slugs:
                v.append(f"{path.name} : thème inconnu « {t} » "
                         f"(voir scripts/themes.tsv)")
    elif not themes_list and post_migration and warnings is not None:
        warnings.append(f"{path.name} : frontmatter `themes:` absent (post-migration)")

    # Cohérence Date ↔ répertoire (seulement dans une arborescence fiches/YYYY-MM/)
    parent = path.parent.name
    if re.fullmatch(r"\d{4}-\d{2}", parent):
        date_val = _section_date(text)
        if re.match(r"\d{4}-\d{2}", date_val) and date_val[:7] != parent:
            v.append(f"{path.name} : Date {date_val} incohérente avec le "
                     f"répertoire {parent}/ (la section ## Date fait foi)")

    return v


# ─── I/O ─────────────────────────────────────────────────────────────────────

def main(argv: list[str]) -> int:
    racine = Path(__file__).resolve().parent.parent
    corpus_complet = len(argv) <= 1
    if not corpus_complet:
        cibles = [Path(a) for a in argv[1:]]
    else:
        cibles = sorted((racine / "fiches").rglob("*.md"))
    if not cibles:
        print("Aucune fiche à valider (répertoire fiches/ vide ou absent).")
        return 1

    # Post-migration = présence du catalogue généré (déclenche les WARN themes).
    post_migration = (racine / "catalogue.tsv").exists()

    violations: list[str] = []
    warnings: list[str] = []
    for fiche in cibles:
        violations.extend(lint_fiche(fiche, warnings=warnings,
                                     post_migration=post_migration))

    # Unicité globale des identifiants (stems) — seulement en mode corpus complet.
    if corpus_complet:
        par_stem: dict[str, list[str]] = {}
        for fiche in cibles:
            par_stem.setdefault(fiche.stem, []).append(str(fiche))
        for stem, chemins in sorted(par_stem.items()):
            if len(chemins) > 1:
                violations.append(f"identifiant en double « {stem} » : "
                                  + " ; ".join(chemins))

    if warnings:
        print(f"⚠ {len(warnings)} avertissement(s) :")
        for w in warnings:
            print(f"  - {w}")
        print()

    if violations:
        print(f"✗ {len(violations)} violation(s) sur {len(cibles)} fiche(s) :\n")
        for ligne in violations:
            print(f"  - {ligne}")
        print("\nGate Bronze : ÉCHEC — corriger les fiches (pas le lint).")
        return 1

    print(f"✓ {len(cibles)} fiche(s) validée(s), 0 violation. Gate Bronze : OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
