"""Tests du bornage et de l'assainissement du build KB (U4)."""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import build_knowledge_base as bk  # noqa: E402


class TestFicheAlias(unittest.TestCase):
    def test_sanitise_pipe_et_crochets(self):
        a = bk.fiche_alias("Voxtral | Mistral AI", "id")
        self.assertNotIn("|", a)
        self.assertEqual(a, "Voxtral - Mistral AI")

    def test_sanitise_crochets(self):
        self.assertEqual(bk.fiche_alias("Titre [x] fin", "id"), "Titre -x- fin")

    def test_troncature_120(self):
        long = "mot " * 60  # 240 chars
        a = bk.fiche_alias(long, "id")
        self.assertLessEqual(len(a), 121)
        self.assertTrue(a.endswith("…"))

    def test_fallback_id(self):
        self.assertEqual(bk.fiche_alias("", "mon-id"), "mon-id")


class TestEntityIndex(unittest.TestCase):
    def _majors(self, *pairs):
        return [{"name": n, "type": t, "fiches": ["f"], "attributes": {}} for n, t in pairs]

    def test_suffixe_type_sur_homonyme(self):
        majors = self._majors(("Cursor", "ORGANISATION"), ("Cursor", "TECHNOLOGIE"))
        pages, mt = bk.build_entity_index(majors, {})
        self.assertEqual(pages[("cursor", "organisation")], "Cursor-organisation")
        self.assertEqual(pages[("cursor", "technologie")], "Cursor-technologie")

    def test_nom_unique_pas_de_suffixe(self):
        majors = self._majors(("Claude Code", "TECHNOLOGIE"))
        pages, _ = bk.build_entity_index(majors, {})
        self.assertEqual(pages[("claude code", "technologie")], "Claude-Code")

    def test_nom_reserve_suffixe_entite(self):
        majors = self._majors(("Claude", "TECHNOLOGIE"))
        pages, _ = bk.build_entity_index(majors, {})
        self.assertEqual(pages[("claude", "technologie")], "Claude-entite")

    def test_distinct_override(self):
        majors = self._majors(("ARC", "ORGANISATION"), ("Arc", "TECHNOLOGIE"))
        distinct = {("arc", "organisation"): "org", ("arc", "technologie"): "tech"}
        pages, _ = bk.build_entity_index(majors, distinct)
        self.assertEqual(pages[("arc", "organisation")], "ARC-org")

    def test_collision_non_resolue_leve(self):
        # Deux noms distincts, même filename lower, même type → non résoluble.
        majors = self._majors(("A B", "CONCEPT"), ("A-B", "CONCEPT"))
        with self.assertRaises(RuntimeError):
            bk.build_entity_index(majors, {})


class TestEntityWikilink(unittest.TestCase):
    def test_lien_par_type(self):
        pages = {("cursor", "organisation"): "Cursor-organisation",
                 ("cursor", "technologie"): "Cursor-technologie"}
        mt = {"cursor": {"organisation", "technologie"}}
        link = bk.entity_wikilink("Cursor", "TECHNOLOGIE", pages, mt)
        self.assertIn("Cursor-technologie", link)
        self.assertIn("\\|Cursor]]", link)

    def test_fallback_type_absent(self):
        pages = {("cursor", "organisation"): "Cursor-organisation"}
        mt = {"cursor": {"organisation"}}
        # triple déclare TECHNOLOGIE mais seule la page ORG existe → fallback
        link = bk.entity_wikilink("Cursor", "TECHNOLOGIE", pages, mt)
        self.assertIn("Cursor-organisation", link)

    def test_entite_mineure_ancre(self):
        link = bk.entity_wikilink("Petite Entité", "CONCEPT", {}, {})
        self.assertIn("_entites-mineures#", link)


class TestAliasesTable(unittest.TestCase):
    def test_fusion_et_distinct(self):
        d = Path(tempfile.mkdtemp())
        (d / "entity_aliases.tsv").write_text(
            "# c\nvariante\tdirective\tcible\ttype\n"
            "Agentic AI\tFUSION\tIA agentique\tTECHNOLOGIE\n"
            "ARC\tDISTINCT\torg\tORGANISATION\n", encoding="utf-8")
        fusion, distinct = bk.load_entity_aliases(d)
        self.assertEqual(fusion["agentic ai"], ("IA agentique", "TECHNOLOGIE"))
        self.assertEqual(distinct[("arc", "organisation")], "org")


class TestQuasiDoublons(unittest.TestCase):
    def test_detecte_variantes(self):
        ents = [{"name": "vibe coding"}, {"name": "vibe-coding"}, {"name": "Autre"}]
        rep = bk.quasi_duplicate_report(ents)
        self.assertTrue(any("vibe coding" in r and "vibe-coding" in r for r in rep))


class TestManifest(unittest.TestCase):
    def _fiche(self, titre, kg="| A |"):
        return (f"# f\n\n## Veille\nv\n\n## Titre Article\n{titre}\n\n## Date\n2026-06-01\n\n"
                f"## GrapheDeConnaissance\n### Triples\n{kg}\n")

    def test_manifest_change_sur_titre(self):
        d = Path(tempfile.mkdtemp())
        (d / "fiches" / "2026-06").mkdir(parents=True)
        f = d / "fiches" / "2026-06" / "a-2026-06-01.md"
        f.write_text(self._fiche("Titre Un"), encoding="utf-8")
        m1, _ = bk.compute_kb_manifest(d / "fiches")
        f.write_text(self._fiche("Titre Deux"), encoding="utf-8")
        m2, _ = bk.compute_kb_manifest(d / "fiches")
        self.assertNotEqual(m1, m2)

    def test_manifest_change_sur_kg(self):
        d = Path(tempfile.mkdtemp())
        (d / "fiches" / "2026-06").mkdir(parents=True)
        f = d / "fiches" / "2026-06" / "a-2026-06-01.md"
        f.write_text(self._fiche("T", kg="| A |"), encoding="utf-8")
        m1, _ = bk.compute_kb_manifest(d / "fiches")
        f.write_text(self._fiche("T", kg="| B modifié |"), encoding="utf-8")
        m2, _ = bk.compute_kb_manifest(d / "fiches")
        self.assertNotEqual(m1, m2)


if __name__ == "__main__":
    unittest.main()
