"""Tests du générateur d'index et de catalogue (U3)."""

from __future__ import annotations

import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import build_index as bi  # noqa: E402


THEMES = {"agents-codage-ia-skills": "Agents de codage IA & Skills",
          "economie-marche": "Économie & Marché",
          "outils-plateformes": "Outils & Plateformes"}


def _fiche_md(*, titre="Un Titre", date="2026-06-15", auteurs="Jane Doe",
             frontmatter="", veille="Résumé de veille.", keywords="ia, agents",
             with_kg=True) -> str:
    fm = f"---\n{frontmatter}---\n" if frontmatter else ""
    kg = ("## GrapheDeConnaissance\n### Triples\n"
          "| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |\n"
          "|---|---|---|---|---|---|---|---|\n"
          "| A | ORGANISATION | a_créé | B | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |\n"
          "### Entités\n| Entité | Type | Attribut | Valeur | Action |\n"
          "|---|---|---|---|---|\n| A | ORGANISATION | x | y | AJOUT |\n") if with_kg else ""
    return (f"{fm}# fiche-id\n\n## Veille\n{veille}\n\n## Titre Article\n{titre}\n\n"
            f"## Date\n{date}\n\n## URL\nhttps://x\n\n## Keywords\n{keywords}\n\n"
            f"## Authors\n{auteurs}\n\n## Ton\nT\n\n## Pense-betes\n- n\n\n"
            f"## RésuméDe400mots\nR\n\n{kg}")


class _Tree:
    """Arborescence temporaire fiches/YYYY-MM/…"""
    def __init__(self):
        self.root = Path(tempfile.mkdtemp())
        (self.root / "fiches").mkdir()

    def add(self, name, month, content):
        d = self.root / "fiches" / month
        d.mkdir(exist_ok=True)
        (d / name).write_text(content, encoding="utf-8")

    def cleanup(self):
        shutil.rmtree(self.root, ignore_errors=True)


class TestCatalogue(unittest.TestCase):
    def setUp(self):
        self.t = _Tree()

    def tearDown(self):
        self.t.cleanup()

    def test_tsv_neuf_colonnes_et_flags(self):
        self.t.add("a-2026-06-15.md", "2026-06",
                   _fiche_md(frontmatter="themes: [economie-marche]\nsource: SFEIR\n"))
        self.t.add("b-2026-05-01.md", "2026-05",
                   _fiche_md(date="2026-05-01", with_kg=False))
        records = bi.collect(self.t.root / "fiches")
        tsv = bi.render_catalogue(records, "deadbeef", "2026-07-06")
        data_lines = tsv.splitlines()[2:]
        for ln in data_lines:
            self.assertEqual(len(ln.split("\t")), 9)
        # fiche sans KG → flag sans-kg
        b_line = [ln for ln in data_lines if ln.startswith("b-")][0]
        self.assertIn("sans-kg", b_line.split("\t")[8])

    def test_ordre_date_desc(self):
        self.t.add("a-2026-06-15.md", "2026-06", _fiche_md(date="2026-06-15"))
        self.t.add("b-2026-07-01.md", "2026-07", _fiche_md(date="2026-07-01"))
        records = bi.collect(self.t.root / "fiches")
        self.assertEqual(records[0]["date"], "2026-07-01")

    def test_flags_skill_et_promotion(self):
        self.t.add("s-2026-06-15.md", "2026-06",
                   _fiche_md(frontmatter="fiche_type: skill\nskill_source: x\nskill_author: y\n"))
        self.t.add("p-2026-06-16.md", "2026-06",
                   _fiche_md(date="2026-06-16",
                             frontmatter="cabinet_promotion_candidate: true\n"))
        records = {r["id"]: r for r in bi.collect(self.t.root / "fiches")}
        self.assertIn("skill", records["s-2026-06-15"]["flags"])
        self.assertIn("promotion", records["p-2026-06-16"]["flags"])

    def test_champ_avec_tab_nettoye(self):
        self.t.add("a-2026-06-15.md", "2026-06",
                   _fiche_md(titre="Titre\tavec\ttab", veille="Veille\navec retour"))
        records = bi.collect(self.t.root / "fiches")
        tsv = bi.render_catalogue(records, "x", "2026-07-06")
        for ln in tsv.splitlines()[2:]:
            self.assertEqual(len(ln.split("\t")), 9)

    def test_manifest_change_sur_edition_veille(self):
        self.t.add("a-2026-06-15.md", "2026-06", _fiche_md(veille="Version un."))
        m1 = bi.compute_manifest(bi.collect(self.t.root / "fiches"))
        (self.t.root / "fiches" / "2026-06" / "a-2026-06-15.md").write_text(
            _fiche_md(veille="Version deux modifiée."), encoding="utf-8")
        m2 = bi.compute_manifest(bi.collect(self.t.root / "fiches"))
        self.assertNotEqual(m1, m2)

    def test_manifest_stable_sans_changement(self):
        self.t.add("a-2026-06-15.md", "2026-06", _fiche_md())
        recs = bi.collect(self.t.root / "fiches")
        self.assertEqual(bi.compute_manifest(recs), bi.compute_manifest(recs))


class TestIndex(unittest.TestCase):
    def setUp(self):
        self.t = _Tree()

    def tearDown(self):
        self.t.cleanup()

    def test_multi_themes_present_dans_chaque_vue(self):
        self.t.add("a-2026-06-15.md", "2026-06", _fiche_md(
            titre="Multi",
            frontmatter="themes: [agents-codage-ia-skills, economie-marche]\n"))
        records = bi.collect(self.t.root / "fiches")
        idx = bi.render_index(records, THEMES, "2026-07-06")
        self.assertEqual(idx.count("[Multi]"), 3)  # 1 mois + 2 thématiques

    def test_titre_avec_crochets_lien_valide(self):
        self.t.add("a-2026-06-15.md", "2026-06", _fiche_md(titre="Titre [x] fin"))
        records = bi.collect(self.t.root / "fiches")
        idx = bi.render_index(records, THEMES, "2026-07-06")
        self.assertIn("Titre (x) fin", idx)
        self.assertNotIn("[Titre [x]", idx)

    def test_stats_liste_pas_de_ligne_unique(self):
        for i in range(3):
            self.t.add(f"a{i}-2026-06-1{i}.md", "2026-06",
                       _fiche_md(date=f"2026-06-1{i}", auteurs="SFEIR"))
        records = bi.collect(self.t.root / "fiches")
        idx = bi.render_index(records, THEMES, "2026-07-06")
        self.assertIn("SFEIR (3)", idx)


class TestReadme(unittest.TestCase):
    def setUp(self):
        self.t = _Tree()
        self.t.add("a-2026-06-15.md", "2026-06", _fiche_md())
        self.records = bi.collect(self.t.root / "fiches")

    def tearDown(self):
        self.t.cleanup()

    def test_remplacement_entre_marqueurs(self):
        readme = self.t.root / "README.md"
        readme.write_text("# Titre\n\n<!-- stats:begin -->\nvieux\n<!-- stats:end -->\n\nfin\n",
                          encoding="utf-8")
        state = bi.update_readme(readme, self.records, THEMES)
        self.assertEqual(state, "ok")
        txt = readme.read_text(encoding="utf-8")
        self.assertIn("**Total** : 1 fiches", txt)
        self.assertNotIn("vieux", txt)
        self.assertIn("fin", txt)

    def test_sans_marqueurs_no_markers(self):
        readme = self.t.root / "README.md"
        readme.write_text("# Titre sans marqueurs\n", encoding="utf-8")
        self.assertEqual(bi.update_readme(readme, self.records, THEMES), "no-markers")
        self.assertEqual(readme.read_text(encoding="utf-8"), "# Titre sans marqueurs\n")


if __name__ == "__main__":
    unittest.main()
