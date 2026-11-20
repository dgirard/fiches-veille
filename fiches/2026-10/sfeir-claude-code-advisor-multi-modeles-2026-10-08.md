---
themes: [agents-codage-ia-skills, outils-plateformes, economie-marche]
source: SFEIR
---
# sfeir-claude-code-advisor-multi-modeles-2026-10-08

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **8 octobre 2026** (~3 900 mots, douze sources, majoritairement de la documentation Anthropic). Il part de **Claude Code v2.1.293** (7 octobre 2026), qui fait entrer **Claude Haiku 5.5** dans une session pouvant déjà combiner modèle principal, **advisor** et subagents épinglés. Trois apports. **(A)** Le mécanisme : l'advisor est un outil serveur consulté par le modèle principal avant de s'engager, quand une erreur revient et avant de conclure ; il lit tout le transcript, sans cache, et *« There is no setting to cap or force advisor calls »*. Une table d'appariements fixe qui peut conseiller qui. **(B)** Une configuration vérifiée : **Sonnet 5.5** en principal, **Opus 5.5** en advisor, un subagent Explore épinglé sur **Haiku 5.5** sans outils d'écriture, et une règle CLAUDE.md, justifiée par une mesure d'Anthropic : sans consigne, Haiku 5.5 et Sonnet 5.5 n'ont consulté sur **aucune des 198** questions GPQA, la définition de l'outil ajoutant **12 %** et **25 %** au coût. **(C)** Les échecs silencieux (appariement refusé sans erreur, télémétrie coupée, ticket **#100082** sur des subagents exécutés en Opus) et l'absence d'advisor sur Google Cloud, Bedrock et Foundry, avec deux replis : **opusplan** et un subagent reviewer Opus. Le texte se clôt sur un protocole de test de deux semaines.

## Titre Article

Advisor Claude Code : qui planifie, qui édite, qui lit entre Opus, Sonnet et Haiku 5.5

## Date

2026-10-08

## URL

https://www.sfeir.com/articles/claude-code-advisor-multi-modeles/

## Keywords

Claude Code, advisor, advisorModel, outil advisor, Claude Haiku 5.5, Claude Sonnet 5.5, Claude Opus 5.5, Fable, subagents, frontmatter, Explore, opusplan, plan mode, CLAUDE.md, routage multi-modèles, FinOps, coût par tâche, transcript, cache, max_uses, Terminal-Bench 4.0, GPQA Diamond, tokenizer, télémétrie, feature flags, Google Cloud, Amazon Bedrock, Microsoft Foundry, Agent SDK

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : guide de configuration publié sur le site d'un cabinet, à destination des équipes de développement et des responsables FinOps qui utilisent Claude Code. Français technique, extraits de configuration reproduits (settings JSON, frontmatter de subagent, règle CLAUDE.md, ligne de commande), citations de la documentation en anglais.

**Style** : objectif annoncé, prérequis, cinq étapes numérotées, deux variantes, puis coûts, pannes, cas Google Cloud, protocole de test et FAQ. Deux tables : les quatre mécanismes (advisor, opusplan, subagent, /model) et les appariements conseiller/conseillé avec versions minimales. Chaque recommandation est rattachée à une phrase de la documentation ou à une mesure chiffrée.

**Position épistémique** : l'article dit avoir relu la configuration *« ligne à ligne contre la documentation »* et signale ce qu'il n'a pas vérifié (ce que résout l'alias haiku hors API Anthropic). Les gains publiés par Anthropic sont datés de la génération 4.6 et présentés comme *« une direction, pas une garantie »*. Le ticket #100082 est qualifié de signalement d'utilisateur, non de bug confirmé. Le partenariat de SFEIR avec Anthropic et Google Cloud est déclaré.

## Pense-betes

- **Advisor** : outil serveur exécuté chez Anthropic ; le modèle principal consulte un modèle *« typically stronger »* avant une approche, quand une erreur revient, avant de déclarer la fin. Vous choisissez le modèle, Claude décide quand l'appeler. Fonction expérimentale.
- **Activation** : `/advisor opus`, réglage `advisorModel`, flag `--advisor` (absent de `claude --help` mais documenté). Notification au démarrage, états Reviewed / Declined / Unavailable.
- **Règle d'appariement** : le conseiller doit être classé au moins au niveau du principal. Haiku 5.5 peut être principal ou conseiller depuis v2.1.293, mais ne conseille ni Sonnet 5.5 ni Opus 5.5.
- **Configuration recommandée** : `model: claude-sonnet-5-5`, `advisorModel: claude-opus-5-5` ; subagent de projet nommé **Explore** (remplace l'intégré, qui tourne sur le modèle de session) avec `tools: Read, Grep, Glob`, `model: claude-haiku-5-5`, `effort: low`. Épingler par frontmatter plutôt que par `CLAUDE_CODE_SUBAGENT_MODEL`.
- **Pourquoi Haiku ne fait que lire** : Terminal-Bench 4.0, 39,2 % contre 70,6 % pour Sonnet 5.5.
- **Règle CLAUDE.md** : consulter avant un plan de plus de trois étapes, quand une erreur revient deux fois, avant de déclarer une tâche longue terminée.
- **Coûts** : chaque appel relit le transcript entier au tarif du conseiller, sans cache ; la dixième consultation coûte plus que la première. L'API expose `max_uses`, `max_tokens` et `caching`, Claude Code non. Avis typique : 400 à 700 tokens de texte.
- **Gains publiés (génération 4.6)** : Sonnet + Opus +2,7 points SWE-bench Multilingual, coût −11,9 % ; Haiku 4.5 + Opus 19,7 % → 41,2 % sur BrowseComp, coût −85 %. Base à battre : le modèle conseiller seul à effort low.
- **Prix Haiku 5.5** : 0,10 $ / 0,50 $ par million sous 100 000 tokens de prompt, ×5 au-delà ; tokenizer produisant ~30 % de tokens en plus que Haiku 4.5 (~1,25× selon Simon Willison).
- **Échecs silencieux** : appariement refusé = requête sans advisor, sans erreur ; `DISABLE_TELEMETRY` coupe l'advisor ; passerelles via `ANTHROPIC_BASE_URL` ; ticket #100082 (279 exécutions sur 301 en Opus). Contrôler `/usage` et les transcripts.
- **Google Cloud, Bedrock, Foundry** : pas d'advisor Claude Code ; la hiérarchie de subagents fonctionne ; replis opusplan et reviewer Opus explicite.
- **Pilote de deux semaines** : 10 à 20 tâches résolues, base actuelle, rejeu avec la configuration, contrôle des transcripts, adoption si succès au moins égal et coût par tâche réussie en baisse.

## RésuméDe400mots

Le 7 octobre 2026, la version 2.1.293 de Claude Code a ajouté Claude Haiku 5.5 aux modèles utilisables dans une même session. L'article de SFEIR décrit comment répartir le travail entre un modèle principal, un advisor et des subagents, à partir d'une relecture de la documentation d'Anthropic.

L'advisor est un outil exécuté côté serveur qui permet au modèle principal de consulter un modèle plus fort aux moments décisifs : avant de choisir une approche, quand une erreur se répète, avant de déclarer une tâche terminée. Le conseiller lit toute la conversation et rend une recommandation. L'utilisateur choisit le modèle conseiller, mais aucun réglage ne permet de plafonner ni de forcer les consultations. Une table fixe les appariements admis : le conseiller doit être au moins au niveau du modèle principal.

La configuration recommandée place Sonnet 5.5 en session principale et Opus 5.5 en advisor, et confie l'exploration du dépôt à un subagent nommé Explore, épinglé sur Haiku 5.5 et privé des outils d'écriture, parce que le subagent intégré tournerait au tarif de Sonnet. Haiku 5.5 obtient 39,2 % sur Terminal-Bench 4.0 contre 70,6 % pour Sonnet 5.5, d'où son rôle de lecteur. Une règle dans CLAUDE.md demande de consulter l'advisor aux trois moments clés : Anthropic a mesuré que, sans consigne, Haiku 5.5 et Sonnet 5.5 ne l'appelaient jamais, alors que la seule présence de l'outil augmentait le coût. Deux variantes sont proposées : Opus avec Fable pour les chantiers critiques, Haiku avec Opus pour des tâches étroites.

Côté coûts, chaque consultation relit le transcript entier au tarif du conseiller, sans cache, ce qui renchérit les sessions longues. L'API propose un plafond d'appels et un cache que Claude Code n'expose pas. Les gains publiés par Anthropic datent de la génération précédente. Haiku 5.5 est peu cher, mais son tokenizer produit davantage de tokens et son tarif quintuple au-delà de 100 000 tokens de prompt.

L'article recense les pannes silencieuses : appariement refusé sans erreur, advisor désactivé par la coupure de la télémétrie ou par une passerelle, subagents signalés comme exécutés sur Opus. Sur Google Cloud, Bedrock et Foundry, l'advisor n'existe pas ; la hiérarchie de subagents fonctionne, avec opusplan ou un reviewer Opus en repli. Un protocole de test sur dix à vingt tâches réelles, pendant deux semaines, permet de décider sur le coût par tâche réussie.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Advisor Claude Code : qui planifie, qui édite, qui lit | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Haiku 5.5 | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| advisor Claude Code | TECHNOLOGIE | fait_partie_de | Claude Code | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | Claude Haiku 5.5 | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| advisor Claude Code | TECHNOLOGIE | permet | consultation d'un modèle plus fort aux points de décision | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | Sonnet 5.5 en principal, Opus 5.5 en advisor, Haiku 5.5 en lecture seule | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | une règle CLAUDE.md qui demande de consulter l'advisor aux trois moments clés | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | mesure | 0 consultation sur 198 questions GPQA sans consigne ; +12 % (Haiku 5.5) et +25 % (Sonnet 5.5) de coût | MESURE | 0.88 | STATIQUE | déclaré_article |
| Claude Sonnet 5.5 | TECHNOLOGIE | surpasse | Terminal-Bench 4.0 : 70,6 % contre 39,2 % pour Haiku 5.5 | MESURE | 0.9 | STATIQUE | déclaré_article |
| advisor Claude Code | TECHNOLOGIE | réduit | coût par tâche de −11,9 % (Sonnet + Opus, génération 4.6) | MESURE | 0.8 | STATIQUE | déclaré_article |
| advisor Claude Code | TECHNOLOGIE | est_variante_de | outil advisor de l'API | TECHNOLOGIE | 0.82 | STATIQUE | inféré |
| SFEIR | ORGANISATION | recommande | opusplan ou un subagent reviewer Opus en repli sur Google Cloud | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un appariement refusé désactive l'advisor sans erreur visible | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Simon Willison | PERSONNE | affirme_que | le tokenizer de Haiku 5.5 est « a hidden price increase » (~1,25×) | CITATION | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | piloter deux semaines sur 10 à 20 tâches réelles et décider au coût par tâche réussie | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | collabore_avec | Anthropic | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, partenaire Anthropic Preferred et Google Cloud | AJOUT |
| advisor Claude Code | TECHNOLOGIE | définition | Outil serveur expérimental : le modèle principal consulte un modèle plus fort aux points de décision | AJOUT |
| Claude Haiku 5.5 | TECHNOLOGIE | catégorie | Modèle léger d'Anthropic (7 oct. 2026), Haiku par défaut de Claude Code v2.1.293 | AJOUT |
| Claude Sonnet 5.5 | TECHNOLOGIE | rôle | Modèle principal recommandé pour éditer et tester | AJOUT |
| Claude Opus 5.5 | TECHNOLOGIE | rôle | Conseiller recommandé, facturé aux points de décision | AJOUT |
| opusplan | METHODOLOGIE | définition | Opus planifie en plan mode, Sonnet exécute ; fonctionne hors API Anthropic | AJOUT |
| Claude Code | TECHNOLOGIE | version | v2.1.293 (7 oct. 2026) | AJOUT |
