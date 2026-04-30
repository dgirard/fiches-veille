"""Tests de compatibilité YAML frontmatter optionnel pour les fiches veille.

Issue tracée par le plan ATransverse v3 (Unit 4) : `extract_fiche_veille()`
retourne historiquement la première ligne non-`#`. Avec un frontmatter YAML
en tête, cette ligne devient `---`, ce qui crée un alias incorrect pour
toutes les fiches portant un frontmatter.

Ces tests vérifient que le patch (skip du bloc YAML en tête) :
1. Préserve le comportement pour les fiches sans frontmatter (régression nulle).
2. Fonctionne correctement pour les fiches avec frontmatter.
3. Reste robuste face à des frontmatters mal formés.
"""

from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

# Permettre import depuis scripts/
sys.path.insert(0, str(Path(__file__).parent.parent))

from build_knowledge_base import extract_fiche_veille  # noqa: E402


SAMPLE_FICHE_NO_FRONTMATTER = """# osmani-agent-harness-engineering-2026-04-19

## Veille
Synthèse par Addy Osmani sur le harness engineering.

## Titre Article
Agent Harness Engineering

## GrapheDeConnaissance
### Triples
| Sujet | Type | … |
"""


SAMPLE_FICHE_WITH_FRONTMATTER = """---
cabinet_promotion_candidate: true
proposed_class: Concept
proposed_capability: capability/software-factory
notes: "Aligne avec ce qu'on observe chez 3 clients"
---
# osmani-agent-harness-engineering-2026-04-19

## Veille
Synthèse par Addy Osmani sur le harness engineering.

## Titre Article
Agent Harness Engineering

## GrapheDeConnaissance
### Triples
| Sujet | Type | … |
"""


SAMPLE_FICHE_WITH_PIPE_IN_FRONTMATTER = """---
notes: "value | with | pipes"
---
# fiche-test

## Veille
Le contenu attendu.

## Titre Article
Test
"""


SAMPLE_FICHE_MALFORMED_FRONTMATTER = """---
unclosed: "no closing fence

# fiche-test

## Veille
Le contenu attendu.
"""


SAMPLE_FICHE_EMPTY_FRONTMATTER = """---
---
# fiche-test

## Veille
Contenu sans champs frontmatter.
"""


def _write_temp_fiche(content: str) -> Path:
    f = tempfile.NamedTemporaryFile(
        mode="w", suffix=".md", delete=False, encoding="utf-8"
    )
    f.write(content)
    f.close()
    return Path(f.name)


class TestFrontmatterCompat(unittest.TestCase):

    def test_no_frontmatter_unchanged(self):
        """Comportement préservé pour les fiches existantes sans frontmatter."""
        path = _write_temp_fiche(SAMPLE_FICHE_NO_FRONTMATTER)
        result = extract_fiche_veille(str(path))
        self.assertEqual(result, "Synthèse par Addy Osmani sur le harness engineering.")
        path.unlink()

    def test_with_frontmatter_skipped(self):
        """Le frontmatter YAML est ignoré et l'alias correct est retourné."""
        path = _write_temp_fiche(SAMPLE_FICHE_WITH_FRONTMATTER)
        result = extract_fiche_veille(str(path))
        # Doit retourner la même chose que sans frontmatter,
        # PAS '---' (ce qui était la régression silencieuse).
        self.assertEqual(result, "Synthèse par Addy Osmani sur le harness engineering.")
        self.assertNotEqual(result, "---")
        path.unlink()

    def test_pipe_in_frontmatter_does_not_leak(self):
        """Un caractère `|` dans le frontmatter ne perturbe pas l'extraction."""
        path = _write_temp_fiche(SAMPLE_FICHE_WITH_PIPE_IN_FRONTMATTER)
        result = extract_fiche_veille(str(path))
        self.assertEqual(result, "Le contenu attendu.")
        path.unlink()

    def test_empty_frontmatter(self):
        """Un frontmatter vide (--- ---) ne fait pas crasher l'extraction."""
        path = _write_temp_fiche(SAMPLE_FICHE_EMPTY_FRONTMATTER)
        result = extract_fiche_veille(str(path))
        self.assertEqual(result, "Contenu sans champs frontmatter.")
        path.unlink()

    def test_malformed_frontmatter_does_not_crash(self):
        """Un frontmatter mal formé (pas de fence fermante) ne crashe pas.

        Comportement attendu : on ne trouve pas la fence fermante, donc
        start_idx reste 0 et on parcourt depuis le début. Le `---` initial
        sera la première ligne non-`#` rencontrée → on retombe sur l'ancien
        comportement qui retournerait `---` ; mais comme la fiche n'a pas
        de structure conforme attendue de toute façon, c'est un signal
        que le frontmatter est cassé. On vérifie juste que l'extraction
        ne crashe pas.
        """
        path = _write_temp_fiche(SAMPLE_FICHE_MALFORMED_FRONTMATTER)
        # Doit ne pas lever d'exception
        result = extract_fiche_veille(str(path))
        # Le résultat est probablement '---' (frontmatter mal formé non skip)
        # ou la ligne suivante. On ne vérifie pas la valeur exacte —
        # juste l'absence de crash.
        self.assertIsInstance(result, str)
        path.unlink()

    def test_file_not_found_returns_empty(self):
        """Comportement du chemin d'erreur : fichier absent → chaîne vide."""
        result = extract_fiche_veille("/path/that/does/not/exist.md")
        self.assertEqual(result, "")


class TestRegressionOnRealFiches(unittest.TestCase):
    """Test de régression sur un échantillon de fiches existantes."""

    def setUp(self):
        self.fiches_dir = Path(__file__).parent.parent.parent / "fiches"
        if not self.fiches_dir.exists():
            self.skipTest("fiches/ dir not present")

    def test_sample_existing_fiches_still_extract(self):
        """Vérifie que les fiches existantes (sans frontmatter) continuent
        de fonctionner identiquement.
        """
        # Prendre quelques fiches au hasard du dernier mois disponible
        recent_dirs = sorted(
            [d for d in self.fiches_dir.iterdir() if d.is_dir()],
            reverse=True,
        )[:1]
        for d in recent_dirs:
            fiche_files = list(d.glob("*.md"))[:3]
            for fiche in fiche_files:
                result = extract_fiche_veille(str(fiche))
                # Doit retourner une chaîne non vide qui n'est ni '---' ni
                # une ligne de séparation Markdown
                self.assertNotEqual(
                    result, "---",
                    f"{fiche.name}: returned '---', frontmatter handling bug",
                )
                self.assertNotEqual(result, "")


if __name__ == "__main__":
    unittest.main()
