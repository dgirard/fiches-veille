# zhutov-qmd-grep-dead-claude-code-memory-recall-2026-03-01
## Veille
QMD moteur de recherche local pour vault Obsidian, skill /recall pour mémoire persistante Claude Code, BM25 + sémantique + hybride vs grep

## Titre Article
Grep Is Dead: How I Made Claude Code Actually Remember Things

## Date
2026-03-01

## URL
https://github.com/tobi/qmd

## Keywords
QMD, moteur de recherche local, mémoire persistante, BM25, recherche sémantique, recherche hybride, Obsidian, Claude Code, skill recall, indexation vault, context engineering, grep, embeddings, knowledge base, sessions, reconstruction contexte, Tobias Lütke, Shopify

## Authors
Artem Zhutov (article/vidéo démonstration), Tobias Lütke (créateur QMD)

## Ton
**Profil** : Perspective de praticien-démonstrateur, registre accessible et enthousiaste, niveau intermédiaire à avancé

**Description** : Artem Zhutov adopte le ton d'un early adopter passionné qui partage ses découvertes en temps réel. Le style est celui d'un live coding commenté — exclamations spontanées ("That's so amazing!", "This is the one that surprised me"), comparaisons avant/après (grep 3 minutes vs QMD instantané), et métriques concrètes (700 sessions, 39 sessions en une journée). L'auteur oscille entre tutoriel technique (commandes CLI, architecture) et récit personnel (PhD, patterns de bonheur, idées oubliées). La démonstration de la recherche sémantique sur ses notes personnelles (sommeil, frustration, idées non réalisées) rend le propos viscéral et crédible. Le public cible est constitué d'utilisateurs intensifs de Claude Code et Obsidian qui ressentent le problème du "cold start" à chaque session.

## Pense-betes
- **Problème central** : chaque conversation avec Claude Code repart de zéro. 700 sessions en 3 semaines, impossibilité de retrouver le contexte, perte de décisions lors du compactage à 60% de contexte. Le grep natif de Claude Code (via Haiku sub-agent) prend 3 minutes, retourne 300 fichiers de bruit, et consomme beaucoup de tokens.
- **QMD** : moteur de recherche local créé par Tobias Lütke (CEO Shopify). Indexe des fichiers markdown en collections. 11 482 étoiles GitHub. Licence MIT. Trois modes de recherche :
  - **BM25** (`qmd search`) : recherche plein texte déterministe. Comme grep mais avec scoring TF-IDF — un court fichier mentionnant "sleep" 5 fois score plus haut qu'un fichier de 10 000 mots avec une seule mention. Pas d'IA, pas d'embeddings, juste des maths. Résultats en 2 secondes.
  - **Sémantique** (`qmd vsearch`) : utilise des embeddings pour trouver du sens même sans mots-clés exacts. "insomnia" ne retourne rien en BM25 mais "couldn't sleep, bad night" retrouve des notes sur la discipline du coucher. 4 résultats sur 5 ne contiennent pas les mots recherchés.
  - **Hybride** (`qmd query`) : combine BM25 + sémantique + expansion de requête + re-ranking LLM. Meilleur classement mais ~30 secondes. Utilise Reciprocal Rank Fusion.
- **Modèles locaux** : tout fonctionne sur la machine, pas d'API externe. Trois modèles GGUF : embedding Gemma 300M, reranker Qwen3 0.6B, query expansion 1.7B. ~2 Go au total.
- **Intégration agents** : serveur MCP intégré, plugin Claude Code marketplace (`claude marketplace add tobi/qmd`), sortie JSON/CSV/MD/XML optimisée pour LLM.
- **Skill /recall** : skill Claude Code qui se greffe sur QMD. Trois modes :
  - **Temporel** (`/recall yesterday`) : reconstruit la timeline des sessions par date. 39 sessions en une journée avec horaire, nombre de messages, résumé.
  - **Topic** (`/recall topic graph`) : recherche BM25 cross-collections, retrouve tous les fichiers liés à un sujet en moins d'une minute.
  - **Graph** (`/recall graph last week`) : visualisation HTML interactive — sessions comme blobs colorés, fichiers regroupés par type, connexions traçables.
- **Pipeline de sessions** : à la fermeture du terminal, un hook exporte et indexe automatiquement la session Claude Code dans QMD. Parse le markdown pur (messages utilisateur), filtre les tool uses et system prompts. L'index est toujours frais.
- **Benchmark grep vs QMD** : recherche "sleep" → grep retourne 200 fichiers dont `sleep()` (commande système), BM25 retourne des réflexions pertinentes sur la qualité du sommeil, sémantique retrouve des notes connexes sans les mots-clés, hybride produit le meilleur ranking.
- **Insight surprenant** : recherche "find the ideas I have never acted on" → Claude adapte la requête en multiples recherches sémantiques et retrouve des idées oubliées depuis des mois (dashboard PhD, screen recording Obsidian). Recherche "days when I was happy" → pattern : jours les plus heureux = shipping + bonne récupération (sauna, 9h de sommeil).
- **Recommandation pratique** : commencer par BM25 (80% des recherches, rapide, structuré). Ajouter sémantique pour transcripts et braindumps (texte libre, pas de mots-clés précis).
- **Philosophie** : "Tools change. Your context stays." — les outils évoluent (Claude Code, Codex, Gemini CLI) mais le contexte personnel persiste. Les notes cessent d'être passives — elles deviennent actionnables.
- **Lien fort avec la veille** : adresse directement le problème du "cold start" identifié par Debois ("chaque session est un nouvel employé") et Vasilopoulos (architecture 3 tiers). QMD est une implémentation concrète du Tier 3 (Cold Memory) avec le skill /recall comme mécanisme de chargement. Le pipeline de sessions automatique implémente le Context Flywheel de Debois.

## RésuméDe400mots
Artem Zhutov présente une solution au problème fondamental du développement assisté par agents IA : **la perte de contexte entre sessions**. Avec 700 sessions Claude Code en 3 semaines, il constate que chaque conversation repart de zéro, que le compactage à 60 % de contexte perd des décisions, et que le grep natif (via Haiku sub-agent) prend 3 minutes pour retourner 300 fichiers de bruit.

La solution repose sur **QMD**, un moteur de recherche local créé par Tobias Lütke (CEO de Shopify), qui indexe des fichiers markdown en collections interrogeables. QMD propose trois modes de recherche. Le **BM25** effectue une recherche plein texte avec scoring de pertinence — contrairement à grep qui retourne toutes les correspondances de chaînes (y compris `sleep()` pour une recherche sur le sommeil), BM25 pondère par fréquence et rareté du terme, livrant des résultats pertinents en 2 secondes. La **recherche sémantique** utilise des embeddings locaux pour trouver du sens au-delà des mots-clés : une recherche "couldn't sleep, bad night" retrouve une note sur la discipline du coucher sans qu'aucun terme ne corresponde. La **recherche hybride** combine les deux avec expansion de requête et re-ranking par LLM pour le meilleur classement possible.

Tout fonctionne localement grâce à trois modèles GGUF (~2 Go) : embeddings Gemma 300M, reranker Qwen3 0.6B, et expansion de requête 1.7B. QMD s'intègre aux agents via un serveur MCP ou un plugin Claude Code.

Au-dessus de QMD, Zhutov a construit le **skill /recall**, une compétence Claude Code qui charge automatiquement le contexte pertinent avant chaque session. Trois modes d'accès : **temporel** (reconstruction de la timeline des sessions par date), **topic** (recherche BM25 cross-collections sur un sujet), et **graph** (visualisation HTML interactive des sessions et fichiers). Un hook de fermeture de terminal exporte et indexe automatiquement chaque session dans QMD, garantissant un index toujours frais.

Les démonstrations révèlent des usages inattendus. Une recherche sémantique "find the ideas I have never acted on" retrouve des projets oubliés depuis des mois. "Days when I was happy" fait émerger un pattern : les meilleurs jours corrèlent shipping et récupération physique. La recherche sémantique transforme un vault passif en **mémoire active** capable de surfacer des connexions invisibles aux mots-clés.

La philosophie sous-jacente résonne avec le context engineering : les outils changent, le contexte reste. Un vault bien indexé survit aux changements de modèle et d'outil. Zhutov démontre concrètement ce que Debois théorise avec le Context Flywheel : documenter le contexte → meilleur output → enrichir le contexte → accélérer.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Tobias Lütke | PERSONNE | a_créé | QMD | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Artem Zhutov | PERSONNE | a_créé | skill /recall | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| QMD | TECHNOLOGIE | utilise | BM25 | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| QMD | TECHNOLOGIE | utilise | recherche sémantique par embeddings | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| QMD | TECHNOLOGIE | utilise | Reciprocal Rank Fusion | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| QMD | TECHNOLOGIE | remplace | grep pour recherche vault | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| QMD | TECHNOLOGIE | s_intègre_à | Model Context Protocol | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| skill /recall | TECHNOLOGIE | est_basé_sur | QMD | TECHNOLOGIE | 0.98 | ATEMPOREL | déclaré_article |
| skill /recall | TECHNOLOGIE | améliore | reconstruction contexte Claude Code | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Artem Zhutov | PERSONNE | affirme_que | grep ne passe pas à l'échelle pour agents IA | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| recherche sémantique | CONCEPT | transforme | vault passif en mémoire active | CONCEPT | 0.90 | ATEMPOREL | inféré |
| Tobias Lütke | PERSONNE | dirige | Shopify | ORGANISATION | 0.99 | DYNAMIQUE | déclaré_article |
| QMD | TECHNOLOGIE | fait_partie_de | architecture mémoire agents IA | CONCEPT | 0.88 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| QMD | TECHNOLOGIE | catégorie | Moteur de recherche local pour documents markdown | AJOUT |
| QMD | TECHNOLOGIE | licence | MIT | AJOUT |
| QMD | TECHNOLOGIE | étoiles GitHub | 11 482 | AJOUT |
| QMD | TECHNOLOGIE | modes recherche | BM25, sémantique (vsearch), hybride (query) | AJOUT |
| QMD | TECHNOLOGIE | modèles locaux | Gemma 300M, Qwen3 0.6B, expansion 1.7B (~2 Go) | AJOUT |
| Tobias Lütke | PERSONNE | rôle | CEO Shopify, créateur QMD | AJOUT |
| Artem Zhutov | PERSONNE | rôle | Créateur skill /recall, animateur lab Claude Code × Obsidian | AJOUT |
| skill /recall | TECHNOLOGIE | catégorie | Skill Claude Code pour chargement contexte via QMD | AJOUT |
| skill /recall | TECHNOLOGIE | modes | temporel, topic (BM25), graph (visualisation HTML) | AJOUT |
| BM25 | CONCEPT | catégorie | Algorithme de scoring plein texte (TF-IDF pondéré) | AJOUT |
