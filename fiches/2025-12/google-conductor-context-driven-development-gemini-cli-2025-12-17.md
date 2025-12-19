# google-conductor-context-driven-development-gemini-cli-2025-12-17

## Veille
Conductor Google - extension Gemini CLI développement piloté par le contexte

## Titre Article
Conductor: Introducing context-driven development for Gemini CLI

## Date
2025-12-17

## URL
https://developers.googleblog.com/conductor-introducing-context-driven-development-for-gemini-cli/

## Keywords
Gemini CLI, développement contextualisé, spécifications, documentation persistante, brownfield, workflow IA, Markdown, planification

## Authors
Keith Ballinger, Jay Kornder, Sherzat Aitbayev

## Ton
Profil : Annonce produit officielle Google, registre technique accessible, perspective lancement d'outil développeur.
Style : Ton informatif et structuré, typique des communications Google Developer. Présentation méthodique en trois phases (setup, newTrack, implement). Emphase sur la résolution d'un problème identifié (gap entre chat éphémère et documentation persistante). Vocabulaire orienté productivité développeur. Public cible : développeurs utilisant Gemini CLI, équipes techniques cherchant à structurer leur usage de l'IA.

## Pense-betes
- Extension Gemini CLI pour le développement piloté par le contexte
- Philosophie : passer des logs de chat temporaires vers une documentation persistante
- Stockage des spécifications et plans en fichiers Markdown dans le codebase
- Trois commandes principales : /conductor:setup, /conductor:newTrack, /conductor:implement
- Phase setup : définition produit, stack technique, préférences workflow
- Phase newTrack : génération specs et plans de tâches détaillés pour nouvelles features
- Phase implement : exécution avec possibilité de pause, reprise et modification
- Support explicite des projets brownfield (codebases existants)
- Permet d'établir des standards techniques et guidelines partagés en équipe
- Disponible sur GitHub

## RésuméDe400mots
Google annonce Conductor, une nouvelle extension pour Gemini CLI conçue pour transformer les workflows de développement assisté par IA. L'outil propose une approche de "développement piloté par le contexte" qui abandonne les logs de chat éphémères au profit d'une documentation persistante et formelle.

Le principe fondamental de Conductor repose sur le stockage des spécifications et plans de projet sous forme de fichiers Markdown directement dans le codebase. Cette approche garantit que le contexte du projet reste accessible et cohérent pour tous les membres de l'équipe, contrairement aux conversations IA qui disparaissent après chaque session.

Le workflow s'articule autour de trois phases distinctes. La première phase utilise la commande `/conductor:setup` pour établir le contexte fondamental du projet. Cette étape couvre la définition du produit, la stack technologique choisie et les préférences de workflow de l'équipe. Ces informations deviennent la base de référence pour toutes les interactions ultérieures avec l'IA.

La deuxième phase, déclenchée par `/conductor:newTrack`, initie le travail sur une nouvelle fonctionnalité. L'outil génère alors des spécifications détaillées et des plans de tâches actionnables. Cette étape structure le travail avant toute implémentation, favorisant une réflexion préalable plutôt qu'un codage improvisé.

La troisième phase emploie `/conductor:implement` pour exécuter le plan établi. L'outil offre une flexibilité importante : les développeurs peuvent mettre en pause le travail, le reprendre ultérieurement ou modifier le plan en cours de route selon les découvertes faites pendant l'implémentation.

Conductor adresse un besoin spécifique souvent négligé : le support des projets brownfield, c'est-à-dire les codebases existants. Pour ces projets, la compréhension du contexte historique et de l'architecture en place s'avère cruciale. L'outil permet de documenter cette connaissance de manière structurée, facilitant l'onboarding de nouveaux développeurs et l'assistance IA pertinente.

L'extension permet également aux équipes d'établir des standards techniques et des guidelines de codage partagés. Ces conventions, une fois documentées, orientent les suggestions de l'IA vers des pratiques cohérentes avec les choix de l'équipe.

Cette annonce s'inscrit dans la tendance plus large de structuration des interactions IA en développement logiciel, rejoignant des approches similaires comme les fichiers AGENTS.md ou les systèmes de skills. L'extension est disponible en téléchargement sur GitHub.
