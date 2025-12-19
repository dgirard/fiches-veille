# google-deepmind-interactions-api-gemini-agents-2025-12-11

## Veille
API Interactions Google DeepMind - interface unifiée modèles et agents Gemini

## Titre Article
Interactions API: A unified foundation for models and agents

## Date
2025-12-11

## URL
https://blog.google/technology/developers/interactions-api/

## Keywords
API, Gemini, agents IA, Google DeepMind, MCP, état serveur, outils distants, Deep Research, ADK, A2A

## Authors
Ali Çevik, Philipp Schmid

## Ton
Profil : Communication produit officielle, registre technique accessible, perspective annonce de lancement.
Style : Ton corporate enthousiaste mais mesuré, vocabulaire technique précis sans jargon excessif. L'article positionne le produit comme une évolution naturelle ("les modèles deviennent des systèmes") plutôt qu'une révolution. Autorité conférée par la signature Google DeepMind. Public cible : développeurs et architectes travaillant avec les APIs d'IA générative.

## Pense-betes
- Nouvelle API en bêta publique via Gemini API dans Google AI Studio
- Gestion d'état côté serveur (optionnelle) - réduit la complexité client
- Support natif du protocole MCP (Model Context Protocol) pour outils distants
- Exécution en arrière-plan sans connexion persistante requise
- Gemini Deep Research disponible comme agent intégré via l'API
- Complémentaire à generateContent (qui reste le chemin principal pour production standard)
- Intégration avec Agent Development Kit (ADK) et protocole Agent2Agent (A2A)
- Schéma propre supportant messages intercalés et appels d'outils

## RésuméDe400mots
Google DeepMind annonce le lancement en bêta publique de l'API Interactions, accessible via l'API Gemini dans Google AI Studio. Cette nouvelle interface propose un point d'entrée unifié pour interagir avec les modèles comme Gemini et les agents IA.

L'API répond aux limitations des approches existantes en offrant plusieurs fonctionnalités clés. Premièrement, la gestion d'état côté serveur devient optionnelle, permettant de réduire significativement la complexité du code client. Les développeurs n'ont plus besoin de maintenir l'historique complet des conversations localement.

Deuxièmement, l'API propose des structures de données interprétables pour gérer les historiques d'agents complexes. Le schéma supporte nativement les messages intercalés et les appels d'outils multiples, facilitant la construction de workflows sophistiqués.

Troisièmement, les capacités d'exécution en arrière-plan permettent des inférences longues sans maintenir de connexions persistantes. Cette architecture est particulièrement adaptée aux tâches de réflexion approfondie ("extended thinking") qui caractérisent les agents modernes.

Quatrièmement, le support natif du protocole MCP (Model Context Protocol) permet l'intégration d'outils distants de manière standardisée. Cette interopérabilité facilite la composition d'agents utilisant des services externes.

L'annonce inclut également la disponibilité de Gemini Deep Research en préversion, un agent de recherche intégré accessible directement via l'API. Cet agent illustre la direction prise par Google : les modèles évoluent vers des systèmes complets capables de raisonnement autonome.

Les développeurs soulignent que cette version n'est qu'un début, avec des plans d'expansion des agents intégrés et le support du développement d'agents personnalisés. L'API est positionnée comme complémentaire au endpoint generateContent existant, qui reste recommandé pour les charges de production standard nécessitant des réponses directes.

L'intégration est déjà disponible via l'Agent Development Kit (ADK) et le protocole Agent2Agent (A2A), avec une adoption plus large de l'écosystème attendue prochainement. Cette annonce s'inscrit dans la tendance plus large de l'industrie vers des interfaces standardisées pour agents, rejoignant les efforts d'autres acteurs autour du protocole MCP.
