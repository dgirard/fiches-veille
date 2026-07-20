---
themes: [agents-codage-ia-skills, outils-plateformes]
source: GitHub (Udit Akhouri)
---
# akhouri-adhd-ideation-divergente-parallele-2026-07-20

## Veille

Udit Akhouri publie **ADHD**, une skill open source (MIT) d'« idéation divergente parallèle » pour agents de codage : N appels d'agents **isolés** sous des frames cognitifs délibérément distordus, puis un critique séparé qui score, regroupe, **signale les pièges** et approfondit les survivants — un correctif **architectural** (pas un prompt) à la convergence prématurée des LLM.

## Titre Article

ADHD — a skill for agents (Parallel Divergent Ideation for Coding Agents)

## Date

2026-07-20

## URL

https://github.com/UditAkhourii/adhd

## Keywords

ADHD, Udit Akhouri, idéation divergente parallèle, convergence prématurée, ancrage cognitif, Tree-of-Thought, Chain-of-Thought, frames cognitifs, générateur vs critique, détection de pièges, skills, agents parallèles, npx skills add, bouton rage-quit, Claude Agent SDK, éval juge LLM, brainstorming multi-agents, repowire

## Authors

Udit Akhouri (@akhouriudit)

## Ton

**Profil :** README de projet open source | Auteur-promoteur | Démonstratif et outillé (bench avant/après, transcripts committés) | ⚠️ évals self-reported : problèmes choisis par l'auteur, notation par juge LLM — à traiter comme des claims, pas des mesures indépendantes.

## Pense-betes

- **Thèse architecturale** : l'ancrage n'est pas un problème de prompting — CoT s'ancre sur sa première sortie, et même Tree-of-Thought « élargit la recherche mais parcourt un seul contexte partagé, donc l'ancrage persiste entre les branches ».
- **Mécanique en 2 phases étanches** : *Diverge* = N appels d'agents isolés (zéro contexte partagé), chacun sous un frame cognitif imposé + system prompt qui **interdit d'évaluer** ; *Focus* = un critique séparé (system prompt opposé) score originalité/viabilité/adéquation, clusterise, **flague les pièges avec raison**, approfondit le top-K.
- **15 frames cognitifs** livrés + logique de sélection + frames custom ; déclenchement sur « design decisions, fuzzy debugging, naming, API surface design, strategy » et tout prompt de forme « give me a few ways to… ».
- **Démo signature (CLI qui freeze 90 s)** : baseline = 4 patterns de manuel (timeouts progressifs, backoff, hedging, streaming) ; ADHD = 30+ idées en 6 clusters, 20 pièges nommés, et le pick non évident **« rage-quit »** — un bouton qui chauffe avec l'attente et rebascule la requête vers un modèle plus rapide/moins cher (« le modèle lent est peut-être juste le mauvais modèle »).
- **Évals auteur (6 problèmes ouverts, juge LLM)** : breadth 9,00 vs 4,83 ; novelty 7,83 vs 2,67 ; **trap detection 9,50 vs 1,83** ; actionability 9,50 vs 6,50 — ADHD gagne 5/6.
- **Distribution écosystème skills** : `npx skills add UditAkhourii/adhd` (~50 agents auto-détectés : Claude Code, Cursor, Codex, Cline, Gemini CLI, Windsurf…), `/adhd "…"`, CLI/lib npm `adhd-agent` ; bâti sur les Agent SDK Claude & Codex.
- **Traction réelle** : ~1 k stars, feature The New Stack, preprint ; adopté par repowire (PR #313, frames → « frame-shifted temp peers » du mesh-orchestrator), mstack (plugin `think`), zk-flow-oss, et une **revue de recherche indépendante** (testdouble/han, 11 sources, 8 rounds) dont les findings atterrissent en issues publiques #16-18.
- **Détail d'ingénierie révélateur** : la SKILL.md tient sa description sur une seule ligne ≤600 caractères parce que certains builds Codex tronquent ou rejettent le YAML multiligne.

## RésuméDe400mots

Udit Akhouri publie **ADHD** (« a skill for agents »), un projet open source (MIT, v0.1.4, ~1 000 stars) qui s'attaque à la **convergence prématurée** du raisonnement autorégressif : un LLM s'ancre sur sa première idée, et les méthodes en arbre n'y échappent pas vraiment — « Tree-of-Thought élargit la recherche mais parcourt un seul contexte partagé, donc l'ancrage persiste entre les branches ». La position du projet : c'est un **problème d'architecture, pas de prompting**.

La mécanique tient en deux phases **étanches**. *Diverge* : N appels d'agents parallèles et **isolés** — aucun contexte partagé — reçoivent chacun le problème à travers l'un des **15 frames cognitifs** délibérément distordus (avec logique de sélection et frames custom), sous un system prompt qui **interdit d'évaluer**. *Focus* : un critique **séparé**, au system prompt opposé, score les idées (originalité, viabilité, adéquation), les regroupe par angle sous-jacent, **signale les pièges avec leurs raisons** et approfondit les meilleurs survivants. La séparation générateur/critique est « mécanique » : des appels LLM distincts, pas des rôles simulés dans un même contexte — la même intuition que la revue adversariale en contexte séparé du chantier Bun ([[sumner-bun-rewrite-rust-claude-2026-07-08]]).

La démo signature compare, sur « un CLI qui appelle un LLM et freeze parfois 90 s », la baseline (4 patterns de manuel : timeouts progressifs, backoff exponentiel, requêtes hedgées, streaming — « la réponse qu'un senior donne en 30 secondes ») à ADHD : 30+ idées en 6 clusters, **20 pièges nommés**, et un pick non évident — le bouton **« rage-quit »** qui s'anime avec l'attente et rebascule instantanément la requête vers un modèle plus rapide et moins cher, car « le modèle lent est peut-être juste le mauvais modèle pour ce prompt ». Sur 6 problèmes ouverts, l'éval de l'auteur (juge LLM) donne breadth 9,00 vs 4,83, novelty 7,83 vs 2,67, **trap detection 9,50 vs 1,83**, actionability 9,50 vs 6,50 — des chiffres self-reported, à lire comme des claims.

La distribution passe par l'écosystème **skills** (même canal que [[skill-pocock-grill-with-docs-2026-06]]) : `npx skills add UditAkhourii/adhd` auto-détecte ~50 agents (Claude Code, Cursor, Codex, Cline, Gemini CLI, Windsurf…), invocation `/adhd` ou auto-déclenchement sur intentions d'idéation, CLI et librairie npm, le tout bâti sur les Agent SDK Claude et Codex. La traction est tangible : feature The New Stack, preprint, adoption par repowire (PR #313 mergée — les frames deviennent des « peers » du mesh-orchestrator), mstack (plugin `think`), zk-flow-oss, et une revue de recherche indépendante (testdouble/han) dont les conclusions vivent en issues publiques. À retenir : la divergence utile ne se prompt pas, elle **s'architecture** — par l'isolation des contextes et l'opposition mécanique générer/critiquer.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Udit Akhouri | PERSONNE | a_créé | ADHD | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| ADHD | TECHNOLOGIE | est_instance_de | skills | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| ADHD | TECHNOLOGIE | résout | convergence prématurée | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| ADHD | TECHNOLOGIE | utilise | idéation divergente parallèle | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| ADHD | TECHNOLOGIE | est_variante_de | Tree-of-Thought | METHODOLOGIE | 0.85 | STATIQUE | déclaré_article |
| ADHD | TECHNOLOGIE | utilise | séparation générateur-critique | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| ADHD | TECHNOLOGIE | utilise | Claude Agent SDK | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| ADHD | TECHNOLOGIE | s_applique_à | Claude Code | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| ADHD | TECHNOLOGIE | s_applique_à | Cursor | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| convergence prématurée | CONCEPT | observé_dans | Chain-of-Thought | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| convergence prématurée | CONCEPT | observé_dans | Tree-of-Thought | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| ADHD | TECHNOLOGIE | recommande | "isolation totale des contextes pendant la divergence — les branches ne se voient jamais, donc pas d'ancrage" | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| ADHD | TECHNOLOGIE | mesure | "breadth 9,00 vs 4,83 ; novelty 7,83 vs 2,67 ; trap detection 9,50 vs 1,83 ; actionability 9,50 vs 6,50 — 5 victoires sur 6 problèmes ouverts (juge LLM, éval de l'auteur)" | MESURE | 0.7 | STATIQUE | déclaré_article |
| repowire | TECHNOLOGIE | utilise | ADHD | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Udit Akhouri | PERSONNE | rôle | Créateur d'ADHD | AJOUT |
| ADHD | TECHNOLOGIE | catégorie | Skill d'idéation divergente pour agents de codage | AJOUT |
| ADHD | TECHNOLOGIE | licence | MIT, v0.1.4 (mai 2026), ~1 k stars | AJOUT |
| idéation divergente parallèle | METHODOLOGIE | définition | Diverger (N agents isolés sous frames cognitifs, interdiction d'évaluer) puis focaliser (critique séparé : score, clusters, pièges, approfondissement du top-K) | AJOUT |
| convergence prématurée | CONCEPT | définition | Ancrage d'un LLM sur sa première idée, persistant même en arbre quand les branches partagent un contexte | AJOUT |
| Tree-of-Thought | METHODOLOGIE | limite | Branches multiples mais contexte unique partagé — l'ancrage persiste | AJOUT |
| Chain-of-Thought | METHODOLOGIE | | | AJOUT |
| séparation générateur-critique | CONCEPT | définition | Appels LLM distincts aux system prompts opposés : générer sans évaluer, puis évaluer sans générer | AJOUT |
| Claude Agent SDK | TECHNOLOGIE | catégorie | SDK d'agents d'Anthropic | AJOUT |
| repowire | TECHNOLOGIE | catégorie | Mesh-orchestrator open source, premier adoptant officiel d'ADHD (PR #313) | AJOUT |
| Claude Code | TECHNOLOGIE | | | AJOUT |
| Cursor | TECHNOLOGIE | | | AJOUT |
| skills | TECHNOLOGIE | | | AJOUT |
