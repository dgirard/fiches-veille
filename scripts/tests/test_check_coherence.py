"""Tests du gate de cohérence doctor (U5)."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import build_index as bi  # noqa: E402
import check_coherence as cc  # noqa: E402


FICHE = ("# a-2026-06-15\n\n## Veille\nRésumé.\n\n## Titre Article\nTitre\n\n"
         "## Date\n2026-06-15\n\n## URL\nx\n\n## Keywords\nia\n\n## Authors\nJane\n\n"
         "## Ton\nT\n\n## Pense-betes\n- n\n\n## RésuméDe400mots\nR\n\n"
         "## GrapheDeConnaissance\n### Triples\n"
         "| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |\n"
         "|---|---|---|---|---|---|---|---|\n"
         "| A | ORGANISATION | a_créé | B | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |\n"
         "### Entités\n| Entité | Type | Attribut | Valeur | Action |\n"
         "|---|---|---|---|---|\n| A | ORGANISATION | x | y | AJOUT |\n")


class _Repo:
    def __init__(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "fiches" / "2026-06").mkdir(parents=True)
        (self.root / "fiches" / "2026-06" / "a-2026-06-15.md").write_text(FICHE, encoding="utf-8")

    def write_catalogue(self, manifest="AUTO"):
        recs = bi.collect(self.root / "fiches")
        if manifest == "AUTO":
            manifest = bi.compute_manifest(recs)
        (self.root / "catalogue.tsv").write_text(
            bi.render_catalogue(recs, manifest, "2026-07-06"), encoding="utf-8")

    def cleanup(self):
        shutil.rmtree(self.root, ignore_errors=True)


class TestCatalogueFreshness(unittest.TestCase):
    def setUp(self):
        self.r = _Repo()

    def tearDown(self):
        self.r.cleanup()

    def test_absent_skip(self):
        _, status, _ = cc.check_catalogue(self.r.root)
        self.assertEqual(status, cc.SKIP)

    def test_frais_ok(self):
        self.r.write_catalogue()
        _, status, _ = cc.check_catalogue(self.r.root)
        self.assertEqual(status, cc.OK)

    def test_perime_stale(self):
        self.r.write_catalogue(manifest="0000deadbeef")
        _, status, _ = cc.check_catalogue(self.r.root)
        self.assertEqual(status, cc.STALE)

    def test_fiche_ajoutee_sans_regen_stale(self):
        self.r.write_catalogue()
        (self.r.root / "fiches" / "2026-07").mkdir()
        (self.r.root / "fiches" / "2026-07" / "b-2026-07-01.md").write_text(
            FICHE.replace("2026-06-15", "2026-07-01"), encoding="utf-8")
        _, status, _ = cc.check_catalogue(self.r.root)
        self.assertEqual(status, cc.STALE)


class TestBijection(unittest.TestCase):
    def setUp(self):
        self.r = _Repo()

    def tearDown(self):
        self.r.cleanup()

    def test_lien_pendant_fail(self):
        self.r.write_catalogue()
        # supprime la fiche mais garde le catalogue → lien pendant
        (self.r.root / "fiches" / "2026-06" / "a-2026-06-15.md").unlink()
        _, status, _ = cc.check_bijection(self.r.root)
        self.assertEqual(status, cc.FAIL)


class TestRawData(unittest.TestCase):
    def setUp(self):
        self.r = _Repo()

    def tearDown(self):
        self.r.cleanup()

    def test_absent_warn(self):
        _, status, _ = cc.check_raw_data(self.r.root)
        self.assertEqual(status, cc.WARN)


class TestRunExitCode(unittest.TestCase):
    def setUp(self):
        self.r = _Repo()

    def tearDown(self):
        self.r.cleanup()

    def test_stale_exit_1(self):
        self.r.write_catalogue(manifest="0000deadbeef")
        code = cc.run(self.r.root)
        self.assertEqual(code, 1)

    def test_catalogue_only_un_seul_check(self):
        # Sans catalogue → SKIP → exit 0
        code = cc.run(self.r.root, catalogue_only=True)
        self.assertEqual(code, 0)


if __name__ == "__main__":
    unittest.main()
