---
themes: [agents-codage-ia-skills, outils-plateformes, transformation-adoption]
source: SFEIR
---
# sfeir-sortir-de-jira-backlog-markdown-2026-11-13

## Veille

Article SFEIR AI publié sur sfeir.com le **13 novembre 2026** (~5 000 mots, 35 sources), qui répond à une question : où doit vivre le ticket quand des agents de code font le travail ? Point de départ : la fin de vie de **Jira Data Center** (lecture seule le **28 mars 2029**) et la hausse des prix de Jira Cloud (~**7 %** au 13 octobre 2026, plus la facturation à l'usage de Rovo). Trois apports : (A) un retour de praticien, **David Golverdingen** (Warmtebouw), dont l'équipe a remplacé Jira par des fichiers Markdown dans **10 repos** (165 tickets actifs, 12 personnes, ~1 h de maintenance par semaine) ; (B) une grille de **quinze solutions notées sur huit critères agent** (C1-C8), où **Backlog.md** (4,5) et **Beads** (4,4) devancent GitHub Issues (3,0) et **Jira Cloud + Rovo MCP** (2,6) ; (C) une échelle de maturité **N0-N4** synthétisant Dan Shapiro, Steve Yegge et le DORA AI Capabilities Model, avec un outil recommandé par niveau et une trajectoire de migration en cinq étapes. L'article borne lui-même ses notes : *« une évaluation argumentée, pas une mesure »*. Recommandation pour une instance GitLab privée : backlog Markdown dans le repo, OpenSpec ou Spec Kit, et le serveur MCP de GitLab pour la vue métier. Rejoint les fiches du corpus sur le [[context-engineering]] et le spec-driven development.

## Titre Article

Sortir de Jira en 2027 : mettez vos tickets là où travaillent vos agents

## Date

2026-11-13

## URL

https://www.sfeir.com/articles/sortir-de-jira-backlog-markdown-agents-ia/

## Keywords

Jira Data Center, fin de vie, Jira Cloud, Rovo MCP, backlog Markdown, ticket dans le repo, Backlog.md, Beads, Task Master, git-bug, Spec Kit, OpenSpec, Linear, GitLab, MCP, délégation d'agents, maturité N0-N4, context engineering, migration, software factory, SFEIR

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Article de conseil à visée décisionnelle, en français, adressé aux DSI, CTO, architectes, RSSI et acheteurs. Le registre est celui d'un comparatif documenté : chaque fait daté renvoie à une source numérotée (35 au total), les comptes d'étoiles GitHub sont relevés à une date précise, et les contradictions entre documentations sont signalées (Task Master, YouTrack) avec la règle « c'est le code qui fait foi ». La thèse est posée dès l'introduction (« dans le repo, à côté du code, modifié dans le même commit ») puis assortie de limites explicites : le modèle vise les équipes déjà outillées en agents, les notes sont une évaluation et non une mesure, l'échelle N0-N4 est une proposition SFEIR dont les correspondances avec Shapiro et Yegge sont présentées comme « notre lecture ». Une section entière recense les points où le tout-Markdown casse (portefeuille, multi-repo, permissions, conformité, non-développeurs, jeunesse des outils, échelle). La conclusion se décline par rôle (DSI, CTO, RSSI, achats) et se termine sur une recommandation concrète pour une instance GitLab privée.

## Pense-betes

- **Calendrier Atlassian** : fin de vente Data Center aux nouveaux clients le 30 mars 2026 ; extension possible jusqu'au 30 mars 2028 ; **lecture seule le 28 mars 2029**. Bitbucket et Bamboo Data Center échappent à la fin de vie (licence hybride).
- **Prix Cloud** au 13 octobre 2026 : Jira Standard 9,05 → 9,70 $, Premium 18,30 → 19,60 $ (tranche 1-100) ; facturation à l'usage Rovo à partir du 3 décembre 2026, dépassement activé par défaut.
- **Cas Warmtebouw** (David Golverdingen, *We Replaced Jira With Markdown Files*) : dossier `tickets/` par repo, frontmatter YAML validé par schéma, hook pre-commit et CI ; règle *« nobody edits these files by hand »* ; CLI typée ; board Kanban en projection ; serveur MCP maison **WBTickets** (20 outils). Bilan à 7 mois : 15 projets, 10 repos, 165 tickets, 12 personnes, licence Jira (~2 000 €/an) supprimée.
- **Outils dans le repo** : **Backlog.md** (MIT, 7 372 étoiles, CLI + MCP) ; **Beads** (Steve Yegge, 28 710 étoiles, backend Dolt, identifiants hachés, compaction) ; **Task Master** (36 outils ≈ 21 000 tokens, mode core 7 outils ≈ 5 000 ; MIT + Commons Clause) ; **git-bug** (issues comme objets git, pas de MCP officiel) ; **Spec Kit** / **OpenSpec** en complément.
- **Trackers classiques** : tous ont un MCP ; ils se départagent sur la délégation (Copilot sur GitHub, Linear vers Cursor/Codex/Devin, GitLab via compte de service en Premium/Ultimate). Huly gelé, à écarter.
- **Huit critères** C1-C8 : lecture dans le repo, écriture par l'agent, versionnement avec le code, CLI/MCP, hors ligne et worktrees, sobriété en tokens, délégation, audit. Accessibilité non-dev notée à part.
- **Échelle N0-N4** : du chat ponctuel à la software factory ; plus le niveau monte, plus le ticket doit être lisible par l'agent sans quitter son environnement.
- **Limites du tout-Markdown** : pas de reporting portefeuille natif, agrégateur multi-repo à construire, permissions = celles du repo, conformité mieux servie par un outil dédié, outils à mainteneur unique.
- **Migration** : auditer, pilote N2, hybride (repo maître → board en lecture), Jira en lecture seule, montée en maturité. Le sens inverse (board maître) recrée le problème.
- À relier : [[Model-Context-Protocol]], [[Steve-Yegge]].

## RésuméDe400mots

L'article part d'une contrainte de calendrier : Atlassian arrête Jira Data Center, qui passera en lecture seule le 28 mars 2029, tandis que Jira Cloud augmente ses prix catalogue d'environ 7 % et ajoute une facturation à l'usage des crédits Rovo. Pour SFEIR, cette migration forcée est le seul moment où une organisation peut changer de modèle sans payer la migration deux fois. La question posée est la suivante : quand des agents de code font le travail, où doit vivre le ticket ?

La réponse défendue est le repo. L'argument principal vient de David Golverdingen, de Warmtebouw : brancher Claude sur Jira par MCP fonctionnait, mais l'agent subissait un schéma étranger et ne voyait pas le ticket en lisant le code. Son équipe a créé un dossier de tickets Markdown dans chacun de ses dix repos, validés par schéma en pre-commit et en CI, écrits uniquement par une CLI typée, avec un board en projection et un serveur MCP de vingt outils pour les non-développeurs. Après sept mois, 165 tickets actifs, douze personnes et environ une heure de maintenance hebdomadaire. Le ticket devient le contexte de l'agent, consigné dans le même commit que le code.

L'article passe ensuite en revue les outils. Backlog.md, Beads, Task Master et git-bug placent le backlog près du code avec des compromis distincts (format Markdown, base Dolt versionnée, coût en tokens, absence de MCP). Spec Kit et OpenSpec remplacent le ticket détaillé mais pas le backlog. Les trackers classiques (GitHub, Linear, GitLab, Plane, YouTrack, OpenProject, ClickUp, Jira Cloud) exposent tous un serveur MCP et se distinguent par la délégation à des agents.

SFEIR propose une échelle de maturité en cinq niveaux, de N0 (pas d'IA) à N4 (software factory), construite à partir de Dan Shapiro, Steve Yegge et du DORA AI Capabilities Model. Quinze solutions sont notées sur huit critères agent : Backlog.md et Beads arrivent en tête, Jira Data Center en dernier. Une table associe à chaque niveau des outils recommandés, acceptables et à éviter.

L'article liste aussi les limites du tout-Markdown : reporting de portefeuille, agrégation multi-repo, permissions héritées du repo, conformité, interface pour non-développeurs, fragilité d'outils jeunes et absence de preuve à grande échelle. Il propose une migration en cinq étapes, du pilote sur une équipe N2 au modèle hybride où le repo fait foi. Pour une instance GitLab privée, la recommandation est un backlog Markdown dans chaque repo, OpenSpec ou Spec Kit, et le serveur MCP de GitLab pour la vue métier.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Sortir de Jira en 2027 | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Atlassian | ORGANISATION | publie | fin de vie de Jira Data Center | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Jira Data Center | TECHNOLOGIE | mesure | lecture seule le 28 mars 2029 | MESURE | 0.95 | STATIQUE | déclaré_article |
| backlog Markdown dans le repo | METHODOLOGIE | est_instance_de | context engineering | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| backlog Markdown dans le repo | METHODOLOGIE | remplace | Jira Data Center | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| David Golverdingen | PERSONNE | travaille_chez | Warmtebouw | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Warmtebouw | ORGANISATION | utilise | backlog Markdown dans le repo | METHODOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| backlog Markdown dans le repo | METHODOLOGIE | mesure | 165 tickets actifs, 10 repos, ~1 h de maintenance par semaine | MESURE | 0.9 | STATIQUE | déclaré_article |
| Steve Yegge | PERSONNE | a_créé | Beads | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Beads | TECHNOLOGIE | utilise | Dolt | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Alex Gavrilescu | PERSONNE | a_créé | Backlog.md | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Backlog.md | TECHNOLOGIE | surpasse | Jira Cloud | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| Jira Cloud | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| GitLab | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| échelle de maturité N0-N4 | METHODOLOGIE | s_inspire_de | DORA AI Capabilities Model | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| échelle de maturité N0-N4 | METHODOLOGIE | s_inspire_de | The Five Levels | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| OpenSpec | TECHNOLOGIE | converge_avec | Spec Kit | TECHNOLOGIE | 0.82 | ATEMPOREL | inféré |
| SFEIR | ORGANISATION | recommande | backlog d'ingénierie dans le repo, board synchronisé pour le métier, MCP GitLab pour la vue métier | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le tout-Markdown ne couvre ni le reporting de portefeuille ni les permissions fines | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Jira Data Center | TECHNOLOGIE | statut | Fin de vie, lecture seule le 28 mars 2029 | AJOUT |
| backlog Markdown dans le repo | METHODOLOGIE | définition | Tickets en fichiers Markdown versionnés, écrits par CLI ou MCP, modifiés dans le commit du code | AJOUT |
| Backlog.md | TECHNOLOGIE | catégorie | Tracker Markdown dans le repo (MIT), CLI + MCP, score agent 4,5/5 | AJOUT |
| Beads | TECHNOLOGIE | catégorie | Tracker natif agent en graphe de dépendances, backend Dolt, score agent 4,4/5 | AJOUT |
| David Golverdingen | PERSONNE | rôle | AI Engineering Lead chez Warmtebouw | AJOUT |
| échelle de maturité N0-N4 | METHODOLOGIE | définition | Échelle SFEIR de maturité agentique, du chat ponctuel à la software factory | AJOUT |
| Jira Cloud | TECHNOLOGIE | score | 2,6/5 sur les critères agent ; Rovo MCP Server GA depuis le 4 février 2026 | AJOUT |
