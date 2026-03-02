# vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24
## Veille
Infrastructure contexte codifié pour agents IA : architecture 3 tiers, mémoire persistante, 283 sessions, MCP, agents spécialisés, codebase complexe

## Titre Article
Codified Context: Infrastructure for AI Agents in a Complex Codebase

## Date
2026-02-24

## URL
https://arxiv.org/html/2602.20478v1

## Keywords
contexte codifié, infrastructure agents IA, mémoire persistante, architecture 3 tiers, constitution, agents spécialisés, knowledge base, MCP, Model Context Protocol, Claude Code, développement assisté IA, spécifications, maintenance documentation, routing expertise, sessions développement, C#, système distribué

## Authors
Aristidis Vasilopoulos (Chercheur indépendant, USA)

## Ton
**Profil** : Perspective de chercheur-praticien indépendant, registre académique rigoureux, niveau avancé

**Description** : Vasilopoulos adopte le ton d'un article de recherche empirique, avec abstract, méthodologie, résultats quantitatifs et limitations explicites. Le style est méthodique et honnête, reconnaissant les biais (single-developer, single-project, observational) tout en présentant des données concrètes impressionnantes (283 sessions, 2 801 prompts, 16 522 tours autonomes). L'auteur évite le ton évangéliste et préfère les études de cas observationnelles aux affirmations catégoriques. Le vocabulaire emprunte à l'architecture logicielle (tiers, hot/cold memory, routing) et à la recherche (confounding factors, quantitative metrics). Le public cible est constitué de développeurs utilisant des agents IA sur des projets complexes et de chercheurs en génie logiciel assisté par IA.

## Pense-betes
- **Problème fondamental** : Les agents LLM n'ont pas de mémoire persistante entre sessions. Ils perdent la cohérence du projet et répètent les mêmes erreurs. C'est le même problème qu'adressent CLAUDE.md, AGENTS.md, et le Context Development Lifecycle de Patrick Debois.
- **Architecture 3 tiers** :
  - **Tier 1 — Constitution (Hot Memory)** : Un seul fichier Markdown de 660 lignes, toujours chargé. Conventions de nommage, commandes build, patterns architecturaux, modes de défaillance connus, tables de routage vers agents spécialisés.
  - **Tier 2 — Agents spécialisés (Domain Experts)** : 19 spécifications d'agents (9 300 lignes). Plus de la moitié du contenu est constitué de faits codebase, formules, patterns et modes de défaillance — pas d'instructions comportementales.
  - **Tier 3 — Knowledge Base (Cold Memory)** : 34 documents de spécification à la demande (16 250 lignes) récupérés via un serveur MCP.
- **Métriques impressionnantes** : 283 sessions sur 70 jours, 2 801 prompts humains, 1 197 invocations d'agents, 16 522 tours autonomes. L'infrastructure contextuelle représente 24,2% de la documentation totale.
- **Pattern de sessions** : 87% ad-hoc avec agents spécialistes optionnels, 13% structurées (plan-execute-review). Plus de 80% des prompts font moins de 100 mots — le contexte pré-chargé réduit le besoin d'explication.
- **Agents les plus invoqués** : Code reviewer (154 invocations), network-protocol-designer (85). Montre que les use cases principaux sont le contrôle qualité et la correction domain-specific.
- **4 études de cas** :
  1. Système de sauvegarde : spec de 283 lignes référencée dans 74 sessions → zéro bug de corruption
  2. Synchronisation UI : documentation de patterns découverts manuellement → réussite au premier essai sur la feature suivante
  3. Système de drop : création de spec avant refactoring → accélération de dizaines d'interactions ultérieures
  4. RNG déterministe : agent de 915 lignes avec théorie du déterminisme → identification de 3 bugs subtils après 5 tentatives échouées
- **6 guidelines praticiens** :
  1. Une constitution basique apporte des améliorations substantielles dès le jour 1
  2. Les agents de planification doivent surfacer automatiquement les specs et spécialistes requis
  3. Les tables de déclenchement (trigger tables) encodent le routage d'expertise
  4. Les explications répétées signalent le besoin de créer une spec
  5. Créer des agents spécialisés débloque les sessions qui stagnent
  6. Les specs obsolètes induisent activement en erreur (failure mode principal)
- **Coût de maintenance** : ~5 min par session affectée + review bihebdomadaire de 30-45 min = 1-2h/semaine
- **Compounding knowledge** : Chaque sous-système documenté accélère non seulement ses propres modifications futures mais aussi chaque feature adjacente qui en dépend. Rejoint le concept de "Context Flywheel" de Patrick Debois.
- **Lien fort avec la veille** : Cet article est la version empirique et quantifiée de ce que décrivent Debois (CDLC, Context Flywheel), les skills d'Anthropic, CLAUDE.md, et l'approche spec-driven. C'est peut-être le papier le plus riche en données sur le sujet.

## RésuméDe400mots
Aristidis Vasilopoulos présente une infrastructure de **contexte codifié** développée pendant la construction d'un système distribué C# de 108 000 lignes, adressant un problème fondamental : les agents LLM n'ont pas de mémoire persistante entre sessions, perdant la cohérence du projet et répétant les erreurs.

L'architecture s'organise en **trois tiers**. Le Tier 1 (Constitution) est un fichier Markdown unique de 660 lignes, toujours chargé en mémoire, encodant conventions, patterns, modes de défaillance et tables de routage vers des agents spécialisés. Le Tier 2 comprend 19 agents spécialisés (9 300 lignes) fonctionnant comme mécanismes d'amorçage de domaine — plus de la moitié de leur contenu est constitué de faits codebase plutôt que d'instructions comportementales. Le Tier 3 est une knowledge base de 34 documents (16 250 lignes) récupérés à la demande via un serveur **MCP** (Model Context Protocol).

L'évaluation quantitative couvre **283 sessions** sur 70 jours, 2 801 prompts humains générant 1 197 invocations d'agents et 16 522 tours autonomes. L'infrastructure contextuelle représente 24,2% de la documentation totale. Les sessions sont à 87% ad-hoc et 13% structurées (plan-execute-review). Plus de 80% des prompts font moins de 100 mots, démontrant que le contexte pré-chargé réduit considérablement le besoin d'explication.

Quatre **études de cas observationnelles** illustrent la valeur du système. Une spécification de sauvegarde de 283 lignes, référencée dans 74 sessions, a produit zéro bug de corruption. La documentation de patterns de synchronisation UI a permis la réussite au premier essai de la feature suivante. La création d'une spec avant un refactoring du système de drop a accéléré des dizaines d'interactions ultérieures. Un agent réseau de 915 lignes a identifié trois bugs subtils de synchronisation qui avaient résisté à cinq tentatives précédentes.

L'auteur propose **six guidelines** : une constitution basique apporte des gains immédiats ; les agents de planification doivent surfacer automatiquement les specs requises ; les tables de routage remplacent la mémoire humaine ; les explications répétées signalent le besoin de créer une spec ; les agents spécialisés débloquent les sessions stagnantes ; et les specs obsolètes constituent le principal mode de défaillance.

Le coût de maintenance est estimé à 1-2 heures par semaine. L'article démontre que la connaissance documentée **compose** : chaque sous-système documenté accélère ses propres modifications et toutes les features adjacentes. L'auteur reconnaît les limites (single-developer, observational) mais fournit l'une des évaluations quantitatives les plus détaillées du développement assisté par agents IA sur un projet complexe réel.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Aristidis Vasilopoulos | PERSONNE | a_créé | infrastructure contexte codifié 3 tiers | METHODOLOGIE | 0.98 | STATIQUE | déclaré_article |
| infrastructure contexte codifié | METHODOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| infrastructure contexte codifié | METHODOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Tier 1 Constitution | CONCEPT | contient | conventions, patterns, tables routage | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Tier 2 Agents spécialisés | CONCEPT | contient | 19 spécifications domain experts | CONCEPT | 0.96 | STATIQUE | déclaré_article |
| Tier 3 Knowledge Base | CONCEPT | utilise | serveur MCP | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| contexte codifié | CONCEPT | améliore | cohérence agents IA entre sessions | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| specs obsolètes | CONCEPT | réduit | qualité output agents IA | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| connaissance documentée | CONCEPT | transforme | productivité développement agentique | CONCEPT | 0.92 | ATEMPOREL | inféré |
| infrastructure contexte codifié | METHODOLOGIE | est_basé_sur | architecture 3 tiers hot/warm/cold | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Aristidis Vasilopoulos | PERSONNE | affirme_que | constitution basique améliore output dès jour 1 | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| agents spécialisés | TECHNOLOGIE | fait_partie_de | infrastructure contexte codifié | METHODOLOGIE | 0.96 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Aristidis Vasilopoulos | PERSONNE | rôle | Chercheur indépendant, développeur C# | AJOUT |
| infrastructure contexte codifié | METHODOLOGIE | catégorie | Architecture 3 tiers pour mémoire persistante agents IA | AJOUT |
| infrastructure contexte codifié | METHODOLOGIE | métriques | 283 sessions, 2801 prompts, 16522 tours autonomes | AJOUT |
| Tier 1 Constitution | CONCEPT | catégorie | Hot memory — fichier Markdown 660 lignes toujours chargé | AJOUT |
| Tier 2 Agents spécialisés | CONCEPT | catégorie | Domain experts — 19 specs, 9300 lignes | AJOUT |
| Tier 3 Knowledge Base | CONCEPT | catégorie | Cold memory — 34 docs, 16250 lignes via MCP | AJOUT |
