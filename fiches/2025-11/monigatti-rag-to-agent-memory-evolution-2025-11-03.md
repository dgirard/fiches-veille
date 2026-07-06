---
themes: [architecture-construction]
source: "Leonie Monigatti"
---
# monigatti-rag-to-agent-memory-evolution-2025-11-03

## Veille
Evolution RAG vers Agent Memory - Read-write operations - Gestion données inference - Vector databases - Mémoire persistante agents IA - Leonie Monigatti

## Titre Article
The Evolution from RAG to Agentic RAG to Agent Memory

## Date
2025-11-03

## URL
https://www.leoniemonigatti.com/blog/from-rag-to-agent-memory.html

## Keywords
Retrieval-Augmented Generation, RAG, Agentic RAG, Agent Memory, Vector Databases, Semantic Search, Tool Calls, Read-Write Operations, Memory Management, Procedural Memory, Episodic Memory, Semantic Memory, Context Window, Memory Corruption, Data Management, Persistent Learning, Personalization, Conversation History, LLM Agents

## Authors
Leonie Monigatti

## Ton
**Profil:** Technique-éducatif | Troisième personne explicative | Analytique-pédagogique | Intermédiaire

Monigatti adopte un style de blog technique didactique traçant une évolution technologique chronologique. Le ton pédagogique est structuré autour d'une progression conceptuelle claire : RAG → Agentic RAG → Agent Memory. L'utilisation de pseudo-code illustrant les transitions techniques rend les abstractions concrètes. Des questions rhétoriques structurent le raisonnement ("Comment récupérer ?" → "Dois-je récupérer ?" → "Comment l'information est-elle gérée ?"). Les admissions de nuances ("introduit de nouveaux défis comme la corruption de mémoire") établissent une perspective équilibrée. Contenu typique de praticienne ML expliquant des patterns architecturaux à un public technique familier des concepts fondamentaux mais explorant l'état de l'art.

## Pense-betes
- **RAG (2020)** : récupération en un coup depuis des sources de connaissances externes
  * Stockage hors ligne
  * Une seule récupération par requête
  * Question : "Comment récupérer ?"

- **Agentic RAG** : récupération dynamique via appels d'outils
  * L'agent détermine si une information supplémentaire est nécessaire
  * Plusieurs tours de récupération possibles
  * Question : "Dois-je récupérer ?"

- **Agent Memory** : opérations de lecture-écriture via des outils
  * WriteTool aux côtés de SearchTool
  * Apprentissage persistant pendant l'inférence
  * Question : "Comment l'information est-elle gérée ?"

**Évolution conceptuelle en 3 étapes**
1. **Stockage + récupération** (RAG vanilla)
2. **Récupération décidée par l'agent** (Agentic RAG)
3. **Gestion complète des données** (Agent Memory)

**Applications pratiques d'Agent Memory**
- Expériences utilisateur personnalisées via le stockage de l'historique de conversation
- Création automatique de souvenirs à partir des détails importants (préférences, dates, noms)
- Systèmes de mémoire multi-sources (procédurale, épisodique, sémantique)

**Types de mémoire**
- **Procédurale** : savoir-faire, workflows
- **Épisodique** : interactions passées, historique de contexte
- **Sémantique** : faits, connaissances du domaine

**Nouveaux défis**
- Corruption de mémoire nécessitant des stratégies de gestion dédiées
- Validation des opérations d'écriture
- Versionnage de la mémoire et résolution de conflits
- Confidentialité et politiques de rétention des données

**Changement de paradigme**
- Des systèmes centrés sur la récupération vers la gestion complète des données
- L'information circule de manière bidirectionnelle dans/hors des fenêtres de contexte
- Capacités de persistance et d'apprentissage fondamentalement modifiées

## RésuméDe400mots

Leonie Monigatti présente dans cet article technique l'évolution architecturale depuis le RAG vanilla (2020) vers l'Agent Memory, traçant la progression de la manière dont les systèmes IA accèdent aux connaissances externes et les gèrent, avec un focus sur le flux bidirectionnel d'information entrant et sortant des fenêtres de contexte des LLM.

**RAG vanilla (2020) : la couche fondation**

Le Retrieval-Augmented Generation a introduit la récupération en un coup depuis des sources de connaissances externes. Architecture simple : stockage hors ligne + une seule récupération par requête. Question centrale : "Comment récupérer ?" La recherche sémantique via bases de données vectorielles permet d'augmenter le LLM avec de l'information externe pertinente. Limite : récupération déterministe, en une seule passe, sans raffinement adaptatif de la requête.

**Agentic RAG : capacité de récupération dynamique**

L'évolution introduit les appels d'outils permettant à l'agent de déterminer si une information supplémentaire est nécessaire. Le pseudo-code illustre la transition :

```
SearchTool disponible → L'agent évalue la pertinence → Plusieurs tours de récupération possibles
```

La question se déplace : "Comment récupérer ?" devient "Dois-je récupérer ?" L'agent décide de manière autonome quand et où récupérer l'information. La récupération devient plus stratégique, contextuelle et itérative. Mais les opérations restent en lecture seule : l'information ne circule que vers la fenêtre de contexte.

**Agent Memory : gestion complète des données**

"L'étape logique suivante après l'évolution du RAG vanilla vers l'Agentic RAG." Introduit un WriteTool aux côtés du SearchTool. Changement de paradigme majeur : opérations de lecture-écriture. La question devient : "Comment l'information est-elle gérée ?"

Le pseudo-code montre la transformation :
```
SearchTool (lecture) + WriteTool (écriture) → Flux d'information bidirectionnel → Apprentissage persistant
```

L'information circule dans les deux sens : non seulement récupérer, mais aussi stocker et modifier pendant l'inférence. Les capacités d'apprentissage persistant des agents en sont fondamentalement modifiées.

**Applications pratiques démontrées**

**Expériences utilisateur personnalisées** : le stockage de l'historique de conversation assure la continuité entre sessions. Préférences utilisateur et patterns d'interaction sont persistés.

**Création automatique de souvenirs** : le système extrait et stocke les détails importants (préférences, dates, noms) sans commande explicite de l'utilisateur. Gestion proactive de la mémoire.

**Systèmes de mémoire multi-sources** : architecture supportant des types de mémoire distincts :
- **Mémoire procédurale** : workflows, savoir-faire
- **Mémoire épisodique** : interactions passées, historique de contexte
- **Mémoire sémantique** : faits, connaissances du domaine

La séparation permet des stratégies de récupération spécialisées par type de mémoire.

**Nouveaux défis introduits**

L'article, équilibré, souligne les défis :

**Corruption de mémoire** : les opérations d'écriture peuvent introduire des erreurs et des informations obsolètes. Des stratégies de validation sont nécessaires.

**Complexité de gestion** : versionnage, résolution de conflits et politiques de rétention deviennent nécessaires. Plus de puissance = gouvernance plus complexe.

**Confidentialité** : le stockage persistant soulève des questions de rétention des données, de consentement et de droit à l'oubli.

**Changement de paradigme résumé**

L'évolution représente un basculement fondamental des systèmes centrés sur la récupération vers la gestion complète des données. Le RAG récupérait la connaissance, l'Agentic RAG décidait quand récupérer, l'Agent Memory gère intégralement le cycle de vie de la connaissance.

Citation clé : "Agent memory represents paradigm shift from retrieval-focused systems to comprehensive data management."

Progression du framework : augmentation statique → récupération dynamique → apprentissage persistant. Chaque étape s'appuie sur les capacités précédentes en ajoutant une couche d'autonomie. L'Agent Memory permet aux agents d'apprendre des interactions, de construire des bases de connaissances et de personnaliser les réponses selon l'expérience accumulée. La transformation d'un outil de récupération en plateforme de gestion de données redéfinit fondamentalement l'architecture des agents LLM.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Leonie Monigatti | PERSONNE | publie | analyse de l'évolution RAG vers Agent Memory | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Agentic RAG | TECHNOLOGIE | est_basé_sur | RAG | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Agent Memory | TECHNOLOGIE | est_basé_sur | Agentic RAG | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Agent Memory | TECHNOLOGIE | utilise | opérations lecture-écriture | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| RAG | TECHNOLOGIE | utilise | vector databases | TECHNOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Agentic RAG | TECHNOLOGIE | utilise | tool calls dynamiques | CONCEPT | 0.94 | STATIQUE | déclaré_article |
| Agent Memory | TECHNOLOGIE | permet | apprentissage persistant | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Agent Memory | TECHNOLOGIE | utilise | mémoire procédurale | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Agent Memory | TECHNOLOGIE | utilise | mémoire épisodique | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Agent Memory | TECHNOLOGIE | utilise | mémoire sémantique | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Agent Memory | TECHNOLOGIE | permet | corruption mémoire | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| gestion complète des données | CONCEPT | remplace | systèmes centrés récupération | CONCEPT | 0.92 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Leonie Monigatti | PERSONNE | rôle | Praticienne ML, auteure technique | AJOUT |
| RAG | TECHNOLOGIE | catégorie | Architecture d'augmentation LLM (2020) | AJOUT |
| Agentic RAG | TECHNOLOGIE | catégorie | RAG avec récupération dynamique par agents | AJOUT |
| Agent Memory | TECHNOLOGIE | catégorie | Gestion bidirectionnelle de données pour agents | AJOUT |
| Vector Databases | TECHNOLOGIE | catégorie | Base de données vectorielle pour recherche sémantique | AJOUT |
