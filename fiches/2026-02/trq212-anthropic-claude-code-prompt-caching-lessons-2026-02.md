# trq212-anthropic-claude-code-prompt-caching-lessons-2026-02
## Veille
Leçons prompt caching Claude Code : architecture cache, plan mode, compaction, optimisation coûts et latence

## Titre Article
Lessons from Building Claude Code: Prompt Caching Is Everything

## Date
2026-02

## URL
https://x.com/trq212/status/2024574133011673516

## Keywords
prompt caching, Claude Code, cache prefix, latence, coûts API, plan mode, compaction, tool search, defer loading, system prompt, cache hit rate, context window, subagents, architecture agents, MCP tools, cache-safe forking

## Authors
@trq212 (Anthropic, équipe Claude Code)

## Ton
**Profil** : Perspective d'ingénieur interne (équipe Claude Code chez Anthropic), registre technique et pédagogique, niveau avancé

**Description** : L'auteur adopte un ton didactique structuré, partageant des leçons apprises "de l'intérieur" avec une transparence inhabituelle sur les choix d'architecture de Claude Code. Le style est direct et pragmatique, alternant explications théoriques ("le prompt caching fonctionne par correspondance de préfixe") et anecdotes de bugs rencontrés en production. L'approche est celle du post-mortem technique transformé en guide de bonnes pratiques. Chaque section suit un pattern problème/intuition naive/solution réelle qui rend les concepts contre-intuitifs accessibles. Le public cible est constitué de développeurs construisant des produits agentiques sur l'API Claude.

## Pense-betes
- **"Cache Rules Everything Around Me"** : Le prompt caching est LE facteur déterminant pour la faisabilité économique et la performance des agents long-running. Tout le harness de Claude Code est construit autour de cette contrainte.
- **Correspondance par préfixe** : Le cache fonctionne en matchant depuis le début de la requête jusqu'aux points de contrôle. Tout changement dans le préfixe invalide tout ce qui suit. Conséquence : l'ordre des éléments est critique.
- **Ordre optimal du system prompt** : Contenu statique en premier, dynamique en dernier. Pour Claude Code : (1) System prompt + Tools (cache global) → (2) CLAUDE.MD (cache par projet) → (3) Contexte session → (4) Messages conversation.
- **Fragilité surprenante** : Des erreurs subtiles cassent le cache : timestamp détaillé dans le system prompt, ordre des outils non-déterministe, mise à jour de paramètres d'outils.
- **System messages plutôt que modifications du prompt** : Pour les informations qui changent (date, fichiers modifiés), utiliser des `<system-reminder>` dans le message utilisateur suivant plutôt que de modifier le system prompt (qui casserait le cache).
- **Ne jamais changer de modèle en cours de session** : Le cache est unique par modèle. À 100k tokens dans une conversation Opus, switcher vers Haiku coûte plus cher que de rester sur Opus car il faut reconstruire le cache. Solution : utiliser des subagents (handoff message).
- **Ne jamais ajouter/retirer d'outils en cours de session** : Les outils font partie du préfixe caché. Toute modification invalide le cache de toute la conversation. C'est l'erreur la plus courante.
- **Plan mode = design autour du cache** : Au lieu de swapper les outils (lecture seule), Claude Code garde TOUS les outils et utilise EnterPlanMode/ExitPlanMode comme outils eux-mêmes + un system message. Bonus : le modèle peut entrer en plan mode de lui-même sans casser le cache.
- **Tool Search = defer au lieu de retirer** : Pour les dizaines d'outils MCP, au lieu de les retirer, envoyer des stubs légers (nom + `defer_loading: true`). Le modèle les "découvre" via ToolSearch. Le préfixe reste stable.
- **Compaction cache-safe** : Lors de la compaction (résumé quand la fenêtre de contexte est pleine), utiliser exactement le même system prompt, contexte et outils que la conversation parente. Seul le prompt de compaction est nouveau. Sinon = coût complet de tous les tokens d'entrée.
- **Buffer de compaction** : Il faut réserver de l'espace dans la fenêtre de contexte pour le message de compaction ET les tokens de sortie du résumé.
- **Monitoring du cache hit rate comme l'uptime** : Anthropic déclenche des alertes et déclare des SEVs quand le taux de cache hit est trop bas. Quelques points de pourcentage de cache miss impactent dramatiquement coûts et latence.
- **Compaction disponible dans l'API** : Basée sur les leçons de Claude Code, la compaction a été intégrée directement dans l'API Anthropic.

## RésuméDe400mots
Cet article technique de l'équipe Claude Code chez Anthropic révèle comment le prompt caching constitue le fondement architectural de Claude Code, rendant économiquement viable un produit agentique à sessions longues. Le principe fondamental : le cache fonctionne par correspondance de préfixe, toute modification dans le préfixe invalidant tout ce qui suit. Cette contrainte unique dicte la conception de l'ensemble du système.

L'architecture du system prompt suit un ordre strict : contenu statique et outils en premier (cache global), puis CLAUDE.MD (cache par projet), contexte de session, et enfin les messages de conversation. Cette hiérarchie maximise le partage de cache entre sessions. L'équipe a découvert que cet ordre est étonnamment fragile : un simple timestamp, un ordre d'outils non-déterministe ou la mise à jour de paramètres d'outils suffit à casser le cache.

Plusieurs règles contre-intuitives émergent de leur expérience. Premièrement, ne jamais modifier le system prompt pour des informations changeantes (date, fichiers modifiés) mais utiliser des balises `<system-reminder>` dans les messages suivants. Deuxièmement, ne jamais changer de modèle en cours de session : à 100k tokens de conversation avec Opus, utiliser Haiku pour une question simple coûte plus cher car le cache doit être entièrement reconstruit. La solution : les subagents avec un message de handoff. Troisièmement, ne jamais ajouter ou retirer d'outils, car ils font partie du préfixe caché.

Le **plan mode** illustre parfaitement le design contraint par le cache. Au lieu de remplacer les outils par des versions lecture seule (ce qui casserait le cache), Claude Code conserve tous les outils et utilise EnterPlanMode/ExitPlanMode comme outils supplémentaires, avec un system message explicatif. Ce design permet au modèle d'entrer en plan mode de lui-même sans rupture de cache. Le **tool search** applique le même principe : au lieu de retirer les outils MCP inutilisés, des stubs légers avec `defer_loading: true` maintiennent le préfixe stable.

La **compaction** (résumé lors du dépassement de la fenêtre de contexte) présente des pièges majeurs. L'implémentation naïve avec un appel API séparé (system prompt différent, sans outils) fait payer le prix complet de tous les tokens. La solution : utiliser exactement les mêmes paramètres que la conversation parente pour réutiliser le préfixe caché, en ne payant que les tokens du prompt de compaction.

L'article conclut que le taux de cache hit doit être surveillé comme l'uptime, avec alertes et incidents déclarés en cas de baisse. Ces patterns sont désormais intégrés directement dans l'API Anthropic, permettant à tout développeur d'agents de bénéficier de ces optimisations.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Prompt caching | CONCEPT | est_le_fondement_de | architecture Claude Code | TECHNOLOGIE | 0.98 | ATEMPOREL | déclaré_article |
| Cache | CONCEPT | fonctionne_par | correspondance de préfixe | CONCEPT | 0.99 | ATEMPOREL | déclaré_article |
| System prompt | CONCEPT | doit_suivre | ordre statique puis dynamique | METHODOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| Modification du system prompt | CONCEPT | invalide | cache de la conversation | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| System-reminder | TECHNOLOGIE | remplace | modification du system prompt | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Plan mode | METHODOLOGIE | préserve | stabilité du cache | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Plan mode | METHODOLOGIE | utilise | EnterPlanMode/ExitPlanMode comme outils | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Tool search | METHODOLOGIE | utilise | stubs avec defer_loading | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| Changement de modèle | CONCEPT | détruit | cache de la session | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Compaction | METHODOLOGIE | doit_réutiliser | même system prompt et outils | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| @trq212 | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | surveille | cache hit rate comme l'uptime | METHODOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Compaction | METHODOLOGIE | a_été_intégrée_dans | API Anthropic | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Ajout/retrait d'outils | CONCEPT | invalide | cache de la conversation | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| @trq212 | PERSONNE | rôle | Ingénieur équipe Claude Code, Anthropic | AJOUT |
| Prompt caching | CONCEPT | description | Mécanisme de réutilisation du prefill par correspondance de préfixe | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| Plan mode | METHODOLOGIE | description | Conserve tous les outils + system message au lieu de swapper les outils | AJOUT |
| Tool search | METHODOLOGIE | description | Stubs légers avec defer_loading pour maintenir préfixe stable | AJOUT |
| Compaction | METHODOLOGIE | description | Résumé cache-safe réutilisant le même préfixe que la conversation parente | AJOUT |
| System-reminder | TECHNOLOGIE | description | Balise dans le message utilisateur pour infos dynamiques sans casser le cache | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| API Anthropic | TECHNOLOGIE | catégorie | API messages pour LLM Claude | AJOUT |
