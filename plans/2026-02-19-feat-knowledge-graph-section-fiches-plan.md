---
title: "feat: Ajouter une section Knowledge Graph aux fiches de veille"
type: feat
date: 2026-02-19
---

# feat: Ajouter une section GrapheDeConnaissance aux fiches de veille

## Overview

Ajouter une 10e section `## GrapheDeConnaissance` à chaque fiche de veille pour extraire et structurer les entités et relations clés de chaque article sous forme de triples (sujet, prédicat, objet). Cette section est générée par Claude Code lors de la création de la fiche, en même temps que les autres sections.

## Problem Statement / Motivation

Les 183 fiches de veille contiennent une richesse d'informations structurées (résumés, pense-bêtes, keywords) mais aucune représentation formelle des **entités** (personnes, organisations, technologies, concepts) ni des **relations** entre elles. Un knowledge graph par fiche permet :

- De capturer les relations implicites dans les articles (qui fait quoi, quelle techno impacte quel domaine)
- De préparer une future agrégation en graphe global inter-fiches
- D'enrichir la recherche thématique au-delà des keywords simples
- De formaliser les connaissances pour des analyses automatisées futures

## Proposed Solution

### Placement dans la fiche

La section `## GrapheDeConnaissance` est ajoutée **après `## RésuméDe400mots`** comme 10e et dernière section. Ce choix :
- Place les données dérivées/structurées après le contenu rédigé
- Ne perturbe pas l'ordre des 9 sections existantes
- Facilite l'ajout progressif (les fiches existantes restent valides sans cette section)

### Structure complète d'une fiche mise à jour

```markdown
# [identifiant-technique]
## Veille
## Titre Article
## Date
## URL
## Keywords
## Authors
## Ton
## Pense-betes
## RésuméDe400mots
## GrapheDeConnaissance        ← NOUVELLE SECTION
```

### Format de la section GrapheDeConnaissance

```markdown
## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Boris Cherny | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | prompt caching | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Boris Cherny | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |
| Demande latente | CONCEPT | guide | développement produit | CONCEPT | 0.90 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Boris Cherny | PERSONNE | rôle | Créateur Claude Code | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
```

### Adaptation de la spec au contexte "veille technique"

La spec originale est conçue pour des conversations évolutives. Pour des articles statiques, les adaptations suivantes sont appliquées :

#### Types d'entités (adaptés au domaine tech)

| Type | Description | Exemples |
|------|-------------|----------|
| `PERSONNE` | Individu nommé | Boris Cherny, Ethan Mollick, Marc Andreessen |
| `ORGANISATION` | Entreprise, labo, institution | Anthropic, Google, Y Combinator, Stanford |
| `TECHNOLOGIE` | Outil, framework, plateforme, langage | Claude Code, MCP, TypeScript, React |
| `CONCEPT` | Idée, principe, pattern | Demande latente, Bitter Lesson, prompt caching |
| `METHODOLOGIE` | Approche, workflow, pratique | Vibe coding, Plan mode, Compounding Engineering |
| `EVENEMENT` | Publication, annonce, incident | Opus 4.5 launch, 2026 Agentic Coding Report |
| `LIEU` | Localisation géographique | Silicon Valley, France, Japon |

> Note : `PREFERENCE` (de la spec originale) est supprimé car non applicable aux articles. `TECHNOLOGIE` et `METHODOLOGIE` sont ajoutés pour le domaine tech.

#### Types temporels

| Type | Quand l'utiliser | Exemple |
|------|-----------------|---------|
| `STATIQUE` | Fait ponctuel, ne change pas | "a publié en 2026", "a été fondé en 2021" |
| `DYNAMIQUE` | Fait qui peut évoluer | "travaille chez Anthropic", "utilise VS Code" |
| `ATEMPOREL` | Vérité générale, principe | "le modèle veut utiliser des outils", "le cache fonctionne par préfixe" |

#### Types de source (adaptés aux articles)

| Type | Description |
|------|-------------|
| `déclaré_article` | Fait explicitement énoncé dans l'article |
| `inféré` | Relation déduite du contexte de l'article |
| `généré_assistant` | Relation ajoutée par Claude pour enrichir le contexte |

> Note : Les types originaux `user_stated|inferred|assistant_generated` sont traduits en français et adaptés au contexte article.

#### Entity Updates (simplifié pour articles statiques)

Pour les articles (snapshots statiques), seule l'action `AJOUT` est pertinente. Les actions `MISE_A_JOUR` et `INVALIDATION` sont conservées dans le schéma pour :
- Les articles qui contredisent des informations précédentes (rare mais utile si un graphe global est ajouté plus tard)
- La compatibilité future avec un système conversationnel

| Action | Quand l'utiliser |
|--------|-----------------|
| `AJOUT` | Nouvelle entité ou attribut identifié (cas standard) |
| `MISE_A_JOUR` | L'article corrige une information connue |
| `INVALIDATION` | L'article contredit une information connue |

#### Seuil de confiance

- **Seuil minimum : 0.70** — Les triples en dessous ne sont pas inclus
- **0.70–0.84** : Relations inférées, interprétations
- **0.85–0.94** : Relations fortement supportées par le texte
- **0.95–1.00** : Relations explicitement déclarées

#### Nombre cible de triples

- **5 à 15 triples** par fiche (ajuster selon la densité de l'article)
- Privilégier les relations **structurantes** (qui relient des entités majeures) aux relations **anecdotiques**
- Les articles longs/denses auront plus de triples, les courts/simples moins

#### Prédicats en français

Les prédicats doivent être en français, sous forme verbale courte (1-3 mots) :
- `a_créé`, `utilise`, `emploie`, `publie`, `critique`, `recommande`
- `transforme`, `remplace`, `améliore`, `réduit`, `augmente`
- `affirme_que`, `prédit`, `contredit`, `s_oppose_à`
- `fait_partie_de`, `est_basé_sur`, `collabore_avec`

Les prédicats épistémiques (`affirme_que`, `prédit`, `recommande`) distinguent les faits des opinions.

## Technical Considerations

### Extraction source

Lors de la création d'une fiche, Claude Code a accès au contenu complet de l'article (via transcript fourni par l'utilisateur, WebFetch, ou raw-data). L'extraction des triples se fait à partir de ce contenu complet, en même temps que la rédaction du résumé.

**Ordre d'extraction** :
1. Claude lit/reçoit le contenu de l'article
2. Claude génère les sections existantes (Veille → RésuméDe400mots)
3. Claude génère la section GrapheDeConnaissance en dernier (bénéficie de la compréhension accumulée)

### Impact sur les scripts existants

- `scripts/fetch_urls.py` : **Aucun changement** (extrait seulement ID et URL via regex sur `## URL`)
- `scripts/download_raw_data.py` : **Aucun changement** (télécharge contenu brut)
- `index.md` : **Aucun changement** (la section KG est interne aux fiches)

### Rétrocompatibilité

- Les fiches existantes sans section `## GrapheDeConnaissance` restent **parfaitement valides**
- La section est **optionnelle** pour les fiches existantes
- Elle devient **obligatoire** pour les nouvelles fiches (mise à jour de CLAUDE.md)

### Langue

Comme toutes les autres sections, le contenu de `## GrapheDeConnaissance` est **intégralement en français** :
- Types d'entités en majuscules françaises : `PERSONNE`, `ORGANISATION`, `TECHNOLOGIE`, etc.
- Prédicats en français : `a_créé`, `utilise`, `publie`
- Noms d'entités : restent dans leur langue d'origine (comme pour Authors)
- En-têtes de tableau en français

## Acceptance Criteria

### Fonctionnel

- [ ] La section `## GrapheDeConnaissance` est ajoutée comme 10e section après `## RésuméDe400mots`
- [ ] La section contient deux sous-sections : `### Triples` (tableau) et `### Entités` (tableau)
- [ ] Les triples incluent : Sujet, Type Sujet, Prédicat, Objet, Type Objet, Confiance, Temporalité, Source
- [ ] Les entités incluent : Entité, Type, Attribut, Valeur, Action
- [ ] Les types d'entités couvrent : PERSONNE, ORGANISATION, TECHNOLOGIE, CONCEPT, METHODOLOGIE, EVENEMENT, LIEU
- [ ] Les temporalités couvrent : STATIQUE, DYNAMIQUE, ATEMPOREL
- [ ] Les sources couvrent : déclaré_article, inféré, généré_assistant
- [ ] Les actions couvrent : AJOUT, MISE_A_JOUR, INVALIDATION
- [ ] Le seuil de confiance minimum est 0.70
- [ ] Chaque fiche contient entre 5 et 15 triples
- [ ] Tous les prédicats sont en français
- [ ] Les noms d'entités restent dans leur langue d'origine

### Documentation

- [ ] CLAUDE.md mis à jour : section `## GrapheDeConnaissance` ajoutée au format standardisé
- [ ] CLAUDE.md mis à jour : description de la section ajoutée dans "Description des sections"
- [ ] CLAUDE.md mis à jour : types d'entités, temporalités, sources, actions documentés
- [ ] CLAUDE.md mis à jour : seuil de confiance et nombre cible de triples documentés
- [ ] CLAUDE.md mis à jour : exemples de prédicats documentés

### Qualité

- [ ] Les triples extraits sont vérifiables dans le contenu source de l'article
- [ ] Les prédicats épistémiques (`affirme_que`, `prédit`) distinguent les faits des opinions
- [ ] Pas de triples en dessous du seuil de confiance 0.70
- [ ] Les types d'entités sont correctement assignés (TECHNOLOGIE vs CONCEPT vs METHODOLOGIE)

## Implementation Phases

### Phase 1 : Mise à jour de CLAUDE.md

**Fichiers modifiés** : `CLAUDE.md`

1. Ajouter `## GrapheDeConnaissance` dans le template de format standardisé (après `## RésuméDe400mots`)
2. Ajouter la description de la section dans "Description des sections"
3. Documenter le format complet : types d'entités, temporalités, sources, actions, prédicats
4. Documenter le seuil de confiance (0.70) et le nombre cible de triples (5-15)
5. Ajouter des exemples concrets

### Phase 2 : Validation sur 3 fiches existantes

**Fichiers modifiés** : 3 fiches de test dans `fiches/2026-02/`

Ajouter la section `## GrapheDeConnaissance` à 3 fiches récentes de types différents :
1. Une fiche **interview/podcast** (ex: `cherny-yc-lightcone-claude-code-origin-story-2026-02.md`)
2. Une fiche **article technique** (ex: `trq212-anthropic-claude-code-prompt-caching-lessons-2026-02.md`)
3. Une fiche **analyse/opinion** (ex: `andreessen-ai-coding-programmers-redefined-orchestrating-bots-2026-02.md`)

Vérifier que les triples extraits sont :
- Pertinents et vérifiables
- Correctement typés
- En français (sauf noms propres)
- Dans la fourchette 5-15 triples

### Phase 3 : Intégration au workflow

**Résultat** : Toutes les nouvelles fiches incluent automatiquement la section `## GrapheDeConnaissance` lors de leur création par Claude Code, conformément aux instructions mises à jour de CLAUDE.md.

## Alternatives Considered

### Format JSON au lieu de tableaux markdown

**Rejeté** : Moins lisible pour un humain parcourant les fiches. Les tableaux markdown sont natifs au format existant et rendus correctement par GitHub/Obsidian.

### Section après Keywords (position 7)

**Rejeté** : Perturbe l'ordre des sections existantes. Mieux de placer les données dérivées en fin de document.

### Graphe global séparé plutôt que par fiche

**Reporté** : Le graphe global est une évolution future naturelle. Commencer par les triples par fiche permet de valider la qualité de l'extraction avant d'agréger.

### Schéma simplifié (sans temporalité/confiance)

**Rejeté par l'utilisateur** : L'utilisateur a explicitement demandé le schéma complet.

## Future Considerations

- **Graphe global** : Agréger les triples de toutes les fiches dans un fichier centralisé (JSON/CSV) pour des requêtes cross-fiches
- **Entity resolution** : Quand le graphe global sera implémenté, utiliser la similarité cosinus pour fusionner les entités similaires (`Boris Cherny` = `Cherny` = `le créateur de Claude Code`)
- **Visualisation** : Générer des diagrammes Mermaid ou D3.js à partir des triples
- **Script batch** : Script Python pour ajouter la section KG aux 183 fiches existantes via API LLM

## References

### Spec fournie par l'utilisateur
- Extraction d'entités et relations par LLM (structured output)
- TextMine (2024) : +44.2% précision avec ontologie et exemples
- KGGen (Mo et al., 2025) : two-stage pattern avec DSPy
- iText2KG/ATOM : entity resolution par cosine similarity
- OpenAI Temporal Agents Cookbook (2025) : STATIC/DYNAMIC/ATEMPORAL

### Fichiers à modifier
- `CLAUDE.md` : Template et instructions (lignes 23-72 principalement)
- 3 fiches de test dans `fiches/2026-02/`
