"""Tests de la migration éditoriale one-shot (U6a)."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import migrate_editorial_frontmatter as mig  # noqa: E402
from fiche_lib import parse_frontmatter  # noqa: E402


def _tmp(content: str) -> Path:
    p = Path(tempfile.mkdtemp()) / "f.md"
    p.write_text(content, encoding="utf-8")
    return p


class TestWriteFrontmatter(unittest.TestCase):
    def test_ajout_sur_fiche_sans_frontmatter(self):
        p = _tmp("# id\n\n## Veille\nv\n")
        self.assertTrue(mig.write_frontmatter(p, ["economie-marche"], "SFEIR"))
        fm, _ = parse_frontmatter(p.read_text().splitlines())
        self.assertEqual(fm["themes"], ["economie-marche"])
        self.assertEqual(fm["source"], "SFEIR")
        self.assertTrue(p.read_text().startswith("---\n"))

    def test_fusion_sur_frontmatter_existant(self):
        p = _tmp("---\ncabinet_promotion_candidate: true\nproposed_class: Concept\n"
                 "proposed_capability: capability/x\nnotes: \"n\"\n---\n# id\n\n## Veille\nv\n")
        self.assertTrue(mig.write_frontmatter(p, ["qualite-securite"], "X"))
        text = p.read_text()
        self.assertEqual(text.count("---"), 2)  # pas de double bloc
        fm, _ = parse_frontmatter(text.splitlines())
        self.assertEqual(fm["proposed_class"], "Concept")   # clé existante préservée
        self.assertEqual(fm["themes"], ["qualite-securite"])  # clé ajoutée

    def test_idempotent(self):
        p = _tmp("# id\n\n## Veille\nv\n")
        mig.write_frontmatter(p, ["economie-marche"], "SFEIR")
        # re-run : themes déjà présent → pas de modification
        self.assertFalse(mig.write_frontmatter(p, ["autre"], "Autre"))

    def test_source_avec_guillemets_echappee(self):
        p = _tmp("# id\n\n## Veille\nv\n")
        mig.write_frontmatter(p, ["economie-marche"], 'Le "Monde"')
        fm, _ = parse_frontmatter(p.read_text().splitlines())
        self.assertEqual(fm["source"], "Le 'Monde'")


class TestParseIndex(unittest.TestCase):
    def test_themes_et_source(self):
        d = Path(tempfile.mkdtemp())
        (d / "fiches" / "2026-06").mkdir(parents=True)
        (d / "fiches" / "2026-06" / "a-2026-06-15.md").write_text("# a", encoding="utf-8")
        (d / "index.md").write_text(
            "## Articles par date de publication\n"
            "### Juin 2026\n"
            "- **[2026-06-15]** [Titre](fiches/2026-06/a-2026-06-15.md) - Desc - SFEIR\n\n"
            "## Thématiques\n"
            "### Économie & Marché\n"
            "- [Titre](fiches/2026-06/a-2026-06-15.md) - Auteur\n",
            encoding="utf-8")
        l2s = {"Économie & Marché": "economie-marche"}
        themes, source, broken = mig.parse_index(d / "index.md", l2s)
        self.assertEqual(themes["a-2026-06-15"], ["economie-marche"])
        self.assertEqual(source["a-2026-06-15"], "SFEIR")
        self.assertEqual(broken, [])

    def test_lien_casse_detecte(self):
        d = Path(tempfile.mkdtemp())
        (d / "fiches").mkdir()
        (d / "index.md").write_text(
            "## Thématiques\n### Économie & Marché\n"
            "- [T](fiches/2026-06/absent-2026-06-15.md)\n", encoding="utf-8")
        _, _, broken = mig.parse_index(d / "index.md", {"Économie & Marché": "economie-marche"})
        self.assertIn("fiches/2026-06/absent-2026-06-15.md", broken)


if __name__ == "__main__":
    unittest.main()
