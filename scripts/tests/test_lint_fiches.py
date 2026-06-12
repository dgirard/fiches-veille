"""Tests du gate Bronze : scripts/lint_fiches.py.

Valide le lint ontologie v2 (plan 2026-06-11-001-feat-architecture-medaillon) :
structure 10 sections, en-têtes de tableaux exacts (accents compris), registre
fermé des 30 prédicats, types d'entités et types épistémiques, seuil de
confiance, vocabulaires fermés Temporalité/Source, tolérance au frontmatter
YAML de promotion.

Leçon du bug des 109 prédicats vides (docs/specs/knowledge-base-construction.md) :
tolérance zéro sur le parsing silencieux — un en-tête sans accent est une
violation, pas une bizarrerie ignorée.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# Permettre import depuis scripts/
sys.path.insert(0, str(Path(__file__).parent.parent))

from lint_fiches import lint_text, lint_fiche  # noqa: E402


def _fiche(
    *,
    frontmatter: str = "",
    sections: str | None = None,
    triples_header: str = "| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |",
    triples_rows: str = "| Anthropic | ORGANISATION | a_créé | Claude Code | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |",
    entites_rows: str = "| Anthropic | ORGANISATION | secteur | IA | AJOUT |",
) -> str:
    """Construit une fiche synthétique conforme par défaut."""
    if sections is None:
        sections = (
            "## Veille\nRésumé synthétique.\n\n"
            "## Titre Article\nSome Original Title\n\n"
            "## Date\n2026-06-01\n\n"
            "## URL\nhttps://example.com/article\n\n"
            "## Keywords\nagents, tests\n\n"
            "## Authors\nJane Doe\n\n"
            "## Ton\nAnalyse posée.\n\n"
            "## Pense-betes\n- note\n\n"
            "## RésuméDe400mots\nRésumé.\n\n"
        )
    sep = "|" + "---|" * 8
    return (
        f"{frontmatter}# fiche-test-2026-06-01\n\n"
        f"{sections}"
        "## GrapheDeConnaissance\n\n"
        "### Triples\n\n"
        f"{triples_header}\n{sep}\n{triples_rows}\n\n"
        "### Entités\n\n"
        "| Entité | Type | Attribut | Valeur | Action |\n"
        "|---|---|---|---|---|\n"
        f"{entites_rows}\n"
    )


class TestFicheValide(unittest.TestCase):

    def test_fiche_conforme_zero_violation(self):
        violations = lint_text(_fiche(), "fiche-test")
        self.assertEqual(violations, [])

    def test_frontmatter_de_promotion_tolere(self):
        fm = (
            "---\n"
            "cabinet_promotion_candidate: true\n"
            "proposed_class: Concept\n"
            "---\n"
        )
        violations = lint_text(_fiche(frontmatter=fm), "fiche-fm")
        self.assertEqual(violations, [])

    def test_en_tete_entites_avec_padding_tolere(self):
        """Le padding d'alignement des cellules n'est pas une violation
        (2 fiches réelles du corpus alignent les colonnes) — seuls les
        libellés exacts, accents compris, font foi."""
        fiche = _fiche().replace(
            "| Entité | Type | Attribut | Valeur | Action |",
            "| Entité   | Type   | Attribut  | Valeur   | Action |",
        )
        self.assertEqual(lint_text(fiche, "fiche-pad"), [])


class TestViolationsPredicats(unittest.TestCase):

    def test_predicat_hors_registre(self):
        fiche = _fiche(
            triples_rows="| A | CONCEPT | s_appuie_sur | B | CONCEPT | 0.9 | STATIQUE | inféré |"
        )
        violations = lint_text(fiche, "fiche-predicat")
        self.assertEqual(len(violations), 1)
        self.assertIn("s_appuie_sur", violations[0])
        self.assertIn("fiche-predicat", violations[0])


class TestViolationsEnTetes(unittest.TestCase):

    def test_en_tete_triples_sans_accent(self):
        fiche = _fiche(
            triples_header="| Sujet | Type Sujet | Predicat | Objet | Type Objet | Confiance | Temporalité | Source |"
        )
        violations = lint_text(fiche, "fiche-entete")
        self.assertTrue(any("en-tête" in v for v in violations))

    def test_en_tete_entites_sans_accent(self):
        fiche = _fiche().replace(
            "| Entité | Type | Attribut | Valeur | Action |",
            "| Entite | Type | Attribut | Valeur | Action |",
        )
        violations = lint_text(fiche, "fiche-entite")
        self.assertTrue(any("en-tête" in v for v in violations))


class TestViolationsEpistemiques(unittest.TestCase):

    def test_objet_epistemique_jamais_sujet(self):
        fiche = _fiche(
            triples_rows='| "727% ROI" | MESURE | soutient | X | CONCEPT | 0.9 | STATIQUE | inféré |'
        )
        violations = lint_text(fiche, "fiche-epi-sujet")
        self.assertTrue(any("sujet" in v.lower() for v in violations))

    def test_type_epistemique_interdit_table_entites(self):
        fiche = _fiche(
            entites_rows='| "Billable hours are dead" | CITATION | source | Article | AJOUT |'
        )
        violations = lint_text(fiche, "fiche-epi-entite")
        self.assertTrue(any("Entités" in v for v in violations))

    def test_objet_epistemique_valide_comme_objet(self):
        fiche = _fiche(
            triples_rows="| Jane Doe | PERSONNE | affirme_que | \"l'IA fait 30% du travail\" | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |"
        )
        self.assertEqual(lint_text(fiche, "fiche-epi-ok"), [])


class TestViolationsConfiance(unittest.TestCase):

    def test_confiance_sous_le_seuil(self):
        fiche = _fiche(
            triples_rows="| A | CONCEPT | soutient | B | CONCEPT | 0.65 | STATIQUE | inféré |"
        )
        violations = lint_text(fiche, "fiche-confiance")
        self.assertTrue(any("0.65" in v or "confiance" in v.lower() for v in violations))

    def test_confiance_non_numerique(self):
        fiche = _fiche(
            triples_rows="| A | CONCEPT | soutient | B | CONCEPT | haute | STATIQUE | inféré |"
        )
        violations = lint_text(fiche, "fiche-confiance-format")
        self.assertTrue(any("haute" in v or "numérique" in v for v in violations))


class TestViolationsStructure(unittest.TestCase):

    def test_section_graphe_manquante(self):
        fiche = _fiche().split("## GrapheDeConnaissance")[0]
        violations = lint_text(fiche, "fiche-sans-graphe")
        self.assertTrue(any("GrapheDeConnaissance" in v for v in violations))

    def test_section_ton_manquante(self):
        fiche = _fiche()
        fiche = fiche.replace("## Ton\nAnalyse posée.\n\n", "")
        violations = lint_text(fiche, "fiche-sans-ton")
        self.assertTrue(any("Ton" in v for v in violations))

    def test_sections_dans_le_desordre(self):
        fiche = _fiche()
        fiche = fiche.replace(
            "## Date\n2026-06-01\n\n## URL\nhttps://example.com/article\n\n",
            "## URL\nhttps://example.com/article\n\n## Date\n2026-06-01\n\n",
        )
        violations = lint_text(fiche, "fiche-desordre")
        self.assertTrue(any("ordre" in v.lower() for v in violations))


class TestViolationsVocabulaires(unittest.TestCase):

    def test_temporalite_hors_vocabulaire(self):
        fiche = _fiche(
            triples_rows="| A | CONCEPT | soutient | B | CONCEPT | 0.9 | PERMANENT | inféré |"
        )
        violations = lint_text(fiche, "fiche-temporalite")
        self.assertTrue(any("PERMANENT" in v for v in violations))

    def test_source_hors_vocabulaire(self):
        fiche = _fiche(
            triples_rows="| A | CONCEPT | soutient | B | CONCEPT | 0.9 | STATIQUE | wikipedia |"
        )
        violations = lint_text(fiche, "fiche-source")
        self.assertTrue(any("wikipedia" in v for v in violations))

    def test_type_entite_invalide(self):
        fiche = _fiche(
            triples_rows="| A | GADGET | soutient | B | CONCEPT | 0.9 | STATIQUE | inféré |"
        )
        violations = lint_text(fiche, "fiche-type")
        self.assertTrue(any("GADGET" in v for v in violations))


class TestLintFichePath(unittest.TestCase):

    def test_lint_fiche_sur_fichier(self):
        f = tempfile.NamedTemporaryFile(
            mode="w", suffix=".md", delete=False, encoding="utf-8"
        )
        f.write(_fiche())
        f.close()
        path = Path(f.name)
        self.assertEqual(lint_fiche(path), [])
        path.unlink()


class TestRegressionCorpusReel(unittest.TestCase):
    """Le corpus réel doit être vert : 0 violation sur l'ensemble des fiches
    (mises en conformité par l'ontologie v2 de juin 2026)."""

    def setUp(self):
        self.fiches_dir = Path(__file__).parent.parent.parent / "fiches"
        if not self.fiches_dir.exists():
            self.skipTest("fiches/ dir not present")

    def test_corpus_complet_zero_violation(self):
        violations = []
        for fiche in sorted(self.fiches_dir.rglob("*.md")):
            violations.extend(lint_fiche(fiche))
        self.assertEqual(
            violations, [],
            f"{len(violations)} violation(s) sur le corpus réel — "
            "le gate Bronze doit finir vert (corriger les fiches, pas le lint) :\n"
            + "\n".join(violations[:20]),
        )


if __name__ == "__main__":
    unittest.main()
