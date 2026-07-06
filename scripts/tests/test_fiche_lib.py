"""Tests du module de parsing partagé fiche_lib (U1).

Couvre le parseur frontmatter minimal (grammaire fermée), le skip frontmatter,
l'extraction de sections, et la non-régression de `extract_veille` /
`parse_markdown_table` par rapport aux implémentations historiques.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from fiche_lib import (  # noqa: E402
    FrontmatterError,
    extract_veille,
    parse_fiche,
    parse_frontmatter,
    parse_markdown_table,
    skip_frontmatter,
    split_sections,
)


def _write(content: str) -> Path:
    f = tempfile.NamedTemporaryFile(mode="w", suffix=".md", delete=False, encoding="utf-8")
    f.write(content)
    f.close()
    return Path(f.name)


class TestParseFrontmatter(unittest.TestCase):

    def test_no_frontmatter(self):
        lines = ["# titre", "", "## Veille", "texte"]
        fm, rest = parse_frontmatter(lines)
        self.assertEqual(fm, {})
        self.assertEqual(rest, lines)

    def test_scalar_quotes_stripped(self):
        fm, _ = parse_frontmatter(['---', 'notes: "Aligne trois clients"', '---', '# t'])
        self.assertEqual(fm["notes"], "Aligne trois clients")

    def test_scalar_single_quotes_and_bool(self):
        fm, _ = parse_frontmatter(["---", "source: 'X'", "cabinet_promotion_candidate: true", "---"])
        self.assertEqual(fm["source"], "X")
        self.assertIs(fm["cabinet_promotion_candidate"], True)

    def test_flow_list(self):
        fm, _ = parse_frontmatter(["---", "themes: [agents-codage-ia-skills, economie-marche]", "---"])
        self.assertEqual(fm["themes"], ["agents-codage-ia-skills", "economie-marche"])

    def test_block_list(self):
        lines = ["---", "themes:", "  - agents-codage-ia-skills", "  - economie-marche", "---", "# t"]
        fm, rest = parse_frontmatter(lines)
        self.assertEqual(fm["themes"], ["agents-codage-ia-skills", "economie-marche"])
        self.assertEqual(rest, ["# t"])

    def test_empty_flow_list(self):
        fm, _ = parse_frontmatter(["---", "themes: []", "---"])
        self.assertEqual(fm["themes"], [])

    def test_promotion_frontmatter_real_shape(self):
        lines = [
            "---",
            "cabinet_promotion_candidate: true",
            "proposed_class: Concept",
            "proposed_capability: capability/software-factory",
            'notes: "Aligne avec ce qu\'on observe chez 3 clients"',
            "---",
            "# fiche",
        ]
        fm, rest = parse_frontmatter(lines)
        self.assertEqual(fm["proposed_class"], "Concept")
        self.assertEqual(rest, ["# fiche"])

    def test_unclosed_raises(self):
        with self.assertRaises(FrontmatterError):
            parse_frontmatter(["---", "notes: x", "# pas de fence"])

    def test_nested_map_raises(self):
        with self.assertRaises(FrontmatterError) as ctx:
            parse_frontmatter(["---", "meta:", "  child:", "    deep: 1", "---"])
        self.assertIn("ligne", str(ctx.exception))

    def test_multiline_scalar_raises(self):
        with self.assertRaises(FrontmatterError):
            parse_frontmatter(["---", "notes: |", "  multi", "---"])

    def test_bad_line_raises(self):
        with self.assertRaises(FrontmatterError):
            parse_frontmatter(["---", "ceci n'est pas une clé", "---"])


class TestSkipFrontmatter(unittest.TestCase):

    def test_skip(self):
        self.assertEqual(skip_frontmatter(["---", "a: 1", "---", "corps"]), ["corps"])

    def test_no_skip_when_absent(self):
        self.assertEqual(skip_frontmatter(["# t", "corps"]), ["# t", "corps"])

    def test_unclosed_not_skipped(self):
        lines = ["---", "a: 1", "corps"]
        self.assertEqual(skip_frontmatter(lines), lines)


class TestSplitSections(unittest.TestCase):

    def test_sections(self):
        body = ["# id", "", "## Veille", "résumé", "", "## Date", "2026-07-06", "",
                "## GrapheDeConnaissance", "### Triples", "| a |"]
        sec = split_sections(body)
        self.assertEqual(sec["Date"], "2026-07-06")
        self.assertIn("GrapheDeConnaissance", sec)
        self.assertNotIn("Triples", sec)  # ### ne crée pas de section de 1er niveau


class TestParseFiche(unittest.TestCase):

    def test_full_fiche(self):
        path = _write(
            "---\nthemes: [economie-marche]\nsource: SFEIR\n---\n"
            "# ma-fiche-2026-07-06\n\n## Veille\nRésumé de veille.\n\n"
            "## Titre Article\nMon Titre\n\n## Date\n2026-07-06\n\n"
            "## Authors\nJean Dupont\n\n## Keywords\nia, agents\n\n"
            "## GrapheDeConnaissance\n### Triples\n| x |\n"
        )
        f = parse_fiche(path)
        self.assertEqual(f.id, path.stem)
        self.assertEqual(f.themes, ["economie-marche"])
        self.assertEqual(f.source, "SFEIR")
        self.assertEqual(f.titre, "Mon Titre")
        self.assertEqual(f.date, "2026-07-06")
        self.assertEqual(f.auteurs, "Jean Dupont")
        self.assertEqual(f.veille, "Résumé de veille.")
        self.assertTrue(f.has_kg)
        self.assertFalse(f.is_skill)
        path.unlink()

    def test_fiche_sans_kg(self):
        path = _write("# f\n\n## Veille\nv\n\n## Titre Article\nT\n")
        f = parse_fiche(path)
        self.assertFalse(f.has_kg)
        self.assertEqual(f.themes, [])
        path.unlink()


class TestExtractVeilleParity(unittest.TestCase):
    """Non-régression : extract_veille reproduit l'ancien extract_fiche_veille."""

    def test_with_and_without_frontmatter(self):
        p1 = _write("# f\n\n## Veille\nLigne veille.\n\n## Titre Article\nT\n")
        self.assertEqual(extract_veille(str(p1)), "Ligne veille.")
        p2 = _write('---\nnotes: "x"\n---\n# f\n\n## Veille\nLigne veille.\n')
        self.assertEqual(extract_veille(str(p2)), "Ligne veille.")
        self.assertNotEqual(extract_veille(str(p2)), "---")
        p1.unlink(); p2.unlink()


class TestParseTableParity(unittest.TestCase):

    def test_basic_table(self):
        rows = parse_markdown_table(["| A | B |", "|---|---|", "| 1 | 2 |"])
        self.assertEqual(rows, [{"A": "1", "B": "2"}])


class TestCorpusParses(unittest.TestCase):
    """Toutes les fiches réelles se parsent sans FrontmatterError."""

    def test_all_fiches(self):
        fiches_dir = Path(__file__).parent.parent.parent / "fiches"
        if not fiches_dir.exists():
            self.skipTest("fiches/ absent")
        count = 0
        for p in fiches_dir.rglob("*.md"):
            f = parse_fiche(p)  # ne doit pas lever
            self.assertTrue(f.id)
            count += 1
        self.assertGreater(count, 300)


if __name__ == "__main__":
    unittest.main()
