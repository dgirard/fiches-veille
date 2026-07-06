#!/usr/bin/env python3
"""migrate_editorial_frontmatter.py — migration one-shot (U6a).

Extrait les métadonnées éditoriales (thèmes, source) de l'`index.md` ACTUEL
(rédigé à la main) et les écrit en frontmatter dans chaque fiche. Conservé pour
audit. Idempotent (re-run = 0 modification). Refuse de tourner après la bascule
(présence de catalogue.tsv) sauf --force.

    python3 scripts/migrate_editorial_frontmatter.py --dry-run   # mapping + orphelines
    python3 scripts/migrate_editorial_frontmatter.py --apply     # écrit le frontmatter

Les riches descriptions de l'ancien index.md ne sont PAS migrées (décision :
elles restent dans l'historique git). Stdlib uniquement.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fiche_lib import load_themes, parse_frontmatter  # noqa: E402

# Attribution explicite des fiches absentes de la section Thématiques (2 connues).
ORPHELINES = {
    "google-sans-flex-font-evolution-design-2025-12-18": ["outils-plateformes"],
    "rauch-coding-agents-cli-abstraction-2026-01-02": ["agents-codage-ia-skills"],
}


def load_libelle_to_slug(scripts_dir: Path) -> dict[str, str]:
    """Table inversée {libellé: slug} dérivée du registre des thèmes partagé."""
    return {libelle: slug for slug, libelle in load_themes(scripts_dir).items()}


def parse_index(index_path: Path, libelle_to_slug: dict) -> tuple[dict, dict, list]:
    """Parse l'index.md actuel.

    Returns (themes_by_id, source_by_id, broken_links) :
        themes_by_id[fiche_id] = [slug, …]
        source_by_id[fiche_id] = "Source"
        broken_links = [chemins d'index ne résolvant vers aucun fichier]
    """
    lines = index_path.read_text(encoding="utf-8").splitlines()
    themes_by_id: dict[str, list] = {}
    source_by_id: dict[str, str] = {}
    broken: list[str] = []

    root = index_path.parent
    link_re = re.compile(r"\[[^\]]*\]\((fiches/\d{4}-\d{2}/([^)]+?))\.md\)")

    section = None       # "date" | "theme" | None
    current_slug = None
    for line in lines:
        h2 = re.match(r"^##\s+(.+?)\s*$", line)
        if h2 and not line.startswith("###"):
            title = h2.group(1).strip()
            if title.startswith("Articles"):
                section = "date"
            elif title == "Thématiques":
                section = "theme"
            else:
                section = None
            current_slug = None
            continue
        h3 = re.match(r"^###\s+(.+?)\s*$", line)
        if h3 and section == "theme":
            current_slug = libelle_to_slug.get(h3.group(1).strip())
            continue

        for m in link_re.finditer(line):
            rel, fiche_id = m.group(1), m.group(2)
            if not (root / (rel + ".md")).exists():
                broken.append(rel + ".md")
                continue
            if section == "theme" and current_slug:
                themes_by_id.setdefault(fiche_id, [])
                if current_slug not in themes_by_id[fiche_id]:
                    themes_by_id[fiche_id].append(current_slug)
            elif section == "date":
                # Source = dernier segment « - … » de la ligne (best-effort).
                src = line.rsplit(" - ", 1)[-1].strip() if " - " in line else ""
                src = re.sub(r"\s+", " ", src)[:80]
                if src and fiche_id not in source_by_id:
                    source_by_id[fiche_id] = src
    return themes_by_id, source_by_id, sorted(set(broken))


def _fmt_source(src: str) -> str:
    return src.replace('"', "'")


def write_frontmatter(path: Path, themes: list[str], source: str) -> bool:
    """Écrit/fusionne themes+source dans le frontmatter. Retourne True si modifié."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    fm, _ = parse_frontmatter(lines)
    if "themes" in fm:
        return False  # déjà migrée (idempotence)

    new_keys = [f"themes: [{', '.join(themes)}]"]
    if source:
        new_keys.append(f'source: "{_fmt_source(source)}"')

    if lines and lines[0].strip() == "---":
        # Fusion : insérer avant le --- fermant.
        close = next(i for i in range(1, len(lines)) if lines[i].strip() == "---")
        merged = lines[:close] + new_keys + lines[close:]
        path.write_text("\n".join(merged) + "\n", encoding="utf-8")
    else:
        block = ["---"] + new_keys + ["---"]
        path.write_text("\n".join(block) + "\n" + text, encoding="utf-8")
    return True


def main(argv: list[str]) -> int:
    scripts_dir = Path(__file__).resolve().parent
    root = scripts_dir.parent
    apply = "--apply" in argv[1:]
    force = "--force" in argv[1:]

    if (root / "catalogue.tsv").exists() and not force:
        print("✗ catalogue.tsv présent (post-bascule) — migration déjà faite. "
              "Utiliser --force pour re-tourner.")
        return 1

    libelle_to_slug = load_libelle_to_slug(scripts_dir)
    themes_by_id, source_by_id, broken = parse_index(root / "index.md", libelle_to_slug)

    # Applique les orphelines.
    for fid, slugs in ORPHELINES.items():
        themes_by_id.setdefault(fid, list(slugs))

    all_fiches = {p.stem: p for p in (root / "fiches").rglob("*.md")}
    sans_theme = sorted(fid for fid in all_fiches if fid not in themes_by_id)

    print(f"Fiches totales          : {len(all_fiches)}")
    print(f"Fiches avec thème(s)    : {len(themes_by_id)}")
    print(f"Fiches avec source      : {len(source_by_id)}")
    print(f"Liens d'index cassés    : {len(broken)}")
    if broken:
        for b in broken[:10]:
            print(f"  - lien cassé : {b}")
    print(f"Fiches SANS thème ({len(sans_theme)}) — attribution requise avant bascule :")
    for fid in sans_theme:
        print(f"  - {fid}")

    if not apply:
        print("\n(dry-run — aucune écriture. Relancer avec --apply.)")
        return 0

    if sans_theme:
        print(f"\n✗ {len(sans_theme)} fiche(s) sans thème — compléter ORPHELINES avant --apply.")
        return 1

    modifiees = 0
    for fid, path in all_fiches.items():
        if write_frontmatter(path, themes_by_id[fid], source_by_id.get(fid, "")):
            modifiees += 1
    print(f"\n✓ {modifiees} fiche(s) enrichie(s) (idempotent : {len(all_fiches) - modifiees} déjà à jour).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
