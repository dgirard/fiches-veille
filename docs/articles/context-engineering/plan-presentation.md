# Plan de présentation — Context Engineering : nourrir les agents IA

> 15 slides — ~30 minutes + questions

## Vue d'ensemble

| # | Slide | Contenu clé | Durée |
|---|-------|-------------|-------|
| **1** | **Titre** | Context Engineering — L'art de nourrir les agents IA | — |
| **2** | **Le paradoxe** | "80 % des prompts < 100 mots" (Vasilopoulos, 283 sessions). Le travail est fait *avant* le prompt. | 2 min |
| **3** | **Le goulot a changé** | Ce n'est plus le code, c'est le contexte (Debois). "Chaque session est un nouvel employé." | 2 min |
| **4** | **Prompt Engineering vs Context Engineering** | Optimiser une interaction vs optimiser l'environnement. Artisanat vs ingénierie. Retour linéaire vs retour composé. | 2 min |
| | **— L'ARCHITECTURE (Vasilopoulos) —** | | |
| **5** | **Trois tiers de mémoire** | Schéma : Hot Memory (constitution, toujours chargé) → Warm Memory (experts de domaine, à la demande) → Cold Memory (savoir de référence, tiré quand nécessaire) | 3 min |
| **6** | **Ce que les données montrent** | 24,2 % de documentation = contexte. Contrôle qualité et correction domain-specific dominent les usages. Chaque sous-système documenté accélère les features adjacentes. | 2 min |
| | **— LE CYCLE DE VIE (Debois) —** | | |
| **7** | **Le CDLC en 4 phases** | Schéma circulaire : Générer → Évaluer → Distribuer → Observer | 2 min |
| **8** | **Générer + Évaluer** | 3 niveaux (technique, projet, business) — la plupart des équipes n'en fournissent qu'un. Le TDD du contexte : "un échec d'éval = une spec non écrite". Le contexte pourrit et entre en conflit. | 3 min |
| **9** | **Distribuer + Observer** | Le contexte comme package versionné et sécurisé. "For the first time, there's a selfish reason to share knowledge." Le contexte comme surface d'attaque. Fenêtres infinies ≠ solution — curation → gouvernance. | 3 min |
| | **— LA PRATIQUE (Shipper & Klaassen) —** | | |
| **10** | **Compound Engineering : l'inversion** | Ingénierie classique : chaque feature rend la suivante plus difficile. Compound : chaque feature rend la suivante plus facile. Boucle d'apprentissage documentée. | 2 min |
| **11** | **Plan-Work-Assess-Compound** | Barre de répartition : 40% Plan / 10% Work / 40% Assess / 10% Compound. "Le contexte mange le code." Documentation = carburant, plus coût. | 3 min |
| | **— SYNTHÈSE —** | | |
| **12** | **Trois visions, une convergence** | Tableau croisé sur 3 axes : le contexte compose (mesuré / théorisé / démontré), le problème est le contexte (3 formulations), le partage est incitatif (3 preuves) | 3 min |
| **13** | **Les 5 principes** | 1. Le goulot a changé. 2. Le contexte est un artefact d'ingénierie. 3. Le contexte compose. 4. Le problème est toujours le contexte. 5. Le partage est incitatif. | 2 min |
| **14** | **Le volant d'inertie** | Schéma Context Flywheel (Debois) : documenter → meilleur output → enrichir → composer → accélérer. Coût d'entrée : 1-2h/semaine. Valeur : composée. | 2 min |
| **15** | **Conclusion** | L'ingénieur de demain est un ingénieur du contexte. De la syntaxe → sémantique. Du prompt → système. De l'interaction → architecture. | 1 min |

## Arc narratif

Trois actes :
1. **Vasilopoulos** = l'architecture et la preuve empirique (slides 5-6)
2. **Debois** = le cycle de vie et les principes (slides 7-9)
3. **Shipper & Klaassen** = l'inversion de la complexité (slides 10-11)

Puis convergence et synthèse (slides 12-15).

## Schémas visuels clés

3 schémas indispensables :
- **Les 3 tiers de mémoire** (slide 5) — empilement hot/warm/cold
- **Le cycle CDLC** (slide 7) — boucle circulaire 4 phases
- **La barre de répartition 40/10/40/10** (slide 11) — visualisation du temps

## Sources principales

- Vasilopoulos — *Codified Context: Infrastructure for AI Agents in a Complex Codebase*, arXiv, février 2026
- Debois — *The Context Development Lifecycle*, Tessl, février 2026
- Shipper & Klaassen — *Compound Engineering: How Every Codes With Agents*, Every, décembre 2025
