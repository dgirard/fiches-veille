# lancemartin-anthropic-prompt-auto-caching-claude-2026-02
## Veille
Auto-caching prompts Claude : mécanisme technique, API cache_control, économies 90% tokens, design cache-friendly

## Titre Article
Prompt auto-caching with Claude

## Date
2026-02

## URL
https://x.com/RLanceMartin/status/2024573404888911886

## Keywords
prompt caching, auto-caching, cache_control, ephemeral, tokens cachés, préfixe hash, cache hit, cache miss, inférence LLM, prefill, decode, vLLM, SGLang, API Claude messages, stateless, agents, coût tokens, latence, breakpoint

## Authors
Lance Martin (@RLanceMartin, Anthropic)

## Ton
**Profil** : Perspective de developer advocate chez Anthropic, registre technique et pédagogique, niveau intermédiaire à avancé

**Description** : Lance Martin adopte un ton explicatif et progressif, partant du "pourquoi" (les agents repaient tout le contexte à chaque tour) pour arriver au "comment" (mécanisme de hash cryptographique, prefill/decode). Le style est celui d'un tutoriel technique bien structuré avec des exemples de code JSON intercalés. L'auteur cite activement d'autres contributeurs (@trq212 pour Claude Code, @peakji de Manus, @sankalp, @kipply) créant un effet de communauté d'experts. Le public cible est constitué de développeurs utilisant l'API Claude qui veulent optimiser coûts et latence.

## Pense-betes
- **Économie massive** : Les tokens cachés coûtent 10% du prix des tokens non cachés. Sans caching, on paie la totalité de la fenêtre de contexte à chaque tour d'agent.
- **API stateless** : L'API messages de Claude ne mémorise pas les actions passées. Le harness agent doit repackager à chaque tour : nouveau contexte + actions passées + descriptions d'outils + instructions générales. La majorité du contexte est identique d'un tour à l'autre.
- **Mécanisme technique** : Le `cache_control` breakpoint est un "write point" qui crée un hash cryptographique de tous les blocs jusqu'à ce point, scopé au workspace. À la requête suivante, Claude cherche en arrière (max 20 blocs) pour trouver un match de hash. Un seul caractère de différence = cache miss.
- **Auto-caching (nouveau)** : Nouveau paramètre unique `cache_control: {"type": "ephemeral"}` au niveau de la requête (pas du bloc). Le breakpoint se déplace automatiquement au dernier bloc cachable. Plus besoin de déplacer manuellement le breakpoint.
- **Compatible avec cache au niveau bloc** : L'auto-caching fonctionne en complément du caching bloc par bloc (ex: breakpoint fixe sur le system prompt).
- **Citation @peakji (Manus)** : Le cache hit rate est "la métrique la plus importante" pour un agent IA en production.
- **Deux phases d'inférence LLM** : (1) Prefill = traitement du prompt, (2) Decode = génération des tokens de sortie. Le caching évite de refaire le prefill pour le contexte déjà vu.
- **Risque de casser le cache** : Modifier l'historique de conversation risque de casser le cache. Renvoie vers les leçons de @trq212 pour le design cache-friendly.
- **Complémentaire avec le post de @trq212** : Ce post explique le "quoi/pourquoi/comment technique" du caching, tandis que @trq212 détaille les leçons pratiques de Claude Code (plan mode, compaction, tool search).

## RésuméDe400mots
Lance Martin, developer advocate chez Anthropic, présente le mécanisme de prompt caching pour l'API Claude et annonce la nouvelle fonctionnalité d'auto-caching qui simplifie considérablement son utilisation. Les tokens utilisant le cache coûtent seulement 10% du prix normal, ce qui représente une économie critique pour les applications agentiques.

Le problème fondamental est que l'API messages de Claude est **stateless** : elle ne mémorise rien entre les appels. Un agent qui exécute des actions en boucle doit repackager à chaque tour le nouveau contexte avec l'historique des actions, les descriptions d'outils et les instructions générales. Sans caching, on paie le prix complet de toute la fenêtre de contexte à chaque tour, alors que la majorité du contenu est identique.

Le prompt caching résout ce problème en exploitant les deux phases de l'inférence LLM : le **prefill** (traitement du prompt) et le **decode** (génération). Le calcul du prefill peut être effectué une seule fois, sauvegardé, puis réutilisé si une partie du prompt futur est identique. C'est ce que font les frameworks comme vLLM et SGLang.

Techniquement, le caching utilise un paramètre `cache_control` qui sert de breakpoint. Ce breakpoint crée un **hash cryptographique** de tous les blocs de contenu jusqu'à ce point, scopé au workspace de l'utilisateur. Lors des requêtes suivantes, Claude cherche en arrière (maximum 20 blocs) pour trouver un match. La correspondance doit être exacte : un seul caractère de différence produit un hash différent et un cache miss.

La nouveauté majeure est l'**auto-caching** : un seul paramètre `cache_control: {"type": "ephemeral"}` placé au niveau de la requête (et non plus au niveau de chaque bloc) fait que le breakpoint se déplace automatiquement au dernier bloc cachable. À mesure que la conversation s'allonge, le breakpoint suit automatiquement. Cette fonctionnalité reste compatible avec le caching bloc par bloc pour les cas où l'on souhaite fixer des breakpoints spécifiques (par exemple sur le system prompt).

Martin cite @peakji de Manus qui considère le cache hit rate comme "la métrique la plus importante pour un agent IA en production", et renvoie vers le post complémentaire de @trq212 qui détaille les leçons pratiques tirées de Claude Code : comment structurer le prompt pour maximiser les hits, pourquoi ne jamais modifier les outils ou le modèle en cours de session, et comment concevoir des fonctionnalités (plan mode, compaction) en respectant les contraintes du cache. Les deux articles forment ensemble un guide complet pour construire des agents cache-optimisés sur l'API Claude.
