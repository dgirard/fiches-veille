---
themes: [transformation-adoption, agents-codage-ia-skills]
source: "McKinsey"
---
# moon-walsh-mckinsey-rewiring-software-delivery-agentic-era-2026-05-29

## Veille

Article court (**8 pages**, 4 exhibits) de **McKinsey Technology**, signé par **Jared Moon** (senior partner, Londres), **Rory Walsh** et **Vito Di Leo** (partners, Dublin et Zurich), avec **Adam Thelwall**, publié en **mai 2026**. Les auteurs rapportent des gains de productivité de **×3 à ×5** avec une **réduction de 60 %** de la taille des équipes chez plusieurs entreprises, et les attribuent à la refonte du modèle opératoire, non au seul déploiement d'agents. Quatre leviers : (1) le **sprint de 24 heures**, avec une équipe de nuit d'agents (16 h) et une équipe de jour humaine (8 h) ; (2) l'automatisation des **passages de relais** entre exigences, conception et code, qui pèsent selon eux **70 % de la dépense tech** contre 30 % pour le déploiement ; (3) une **infrastructure de connaissance** en graphes par domaine, interrogée par un agent « bibliothécaire » ; (4) le redimensionnement des équipes et du portefeuille. Sur le graphe : *« this should not begin with a grand, top-down ontology effort »*. Les chiffres d'équipe sont présentés comme illustratifs, tirés de l'« expérience et l'observation » du cabinet. Prolonge la présentation McKinsey de novembre 2025 sur la livraison logicielle par agents ([[harrison-maniar-mckinsey-reshaping-software-delivery-agents-2025-11-23]]).

## Titre Article

Rewiring software delivery for the agentic era

## Date

2026-05-29

## URL

https://www.mckinsey.com/capabilities/tech-and-ai/our-insights/rewiring-software-delivery-for-the-agentic-era

## Keywords

McKinsey, SDLC agentique, modèle opératoire, sprint de 24 heures, équipe de nuit, usine d'agents, agent squads, passages de relais, artefacts lisibles par machine, graphe de connaissance, agent bibliothécaire, mémoire organisationnelle, traçabilité, policy as code, outer loop, réduction des équipes, pods, reskilling, réallocation de capacité, productivité ×3-×5

## Authors

Jared Moon (senior partner), Rory Walsh, Vito Di Leo (partners), avec Adam Thelwall (associate partner) — McKinsey & Company

## Ton

**Profil** : note de cabinet de conseil destinée aux dirigeants technologiques (CIO, CTO, responsables de la livraison). Format court en quatre blocs parallèles, chacun clos par un « Main takeaway » en gras, et appuyé sur un exhibit illustratif.

**Style** : ouverture narrative (une product owner qui découvre à 9 h le travail fait la nuit par les agents : *« No one worked late. AI agents did. »*), puis registre prescriptif à l'impératif (« Treat your knowledge architecture as strategic infrastructure », « Resize teams »). Le vocabulaire est celui de l'industrialisation : *factory of agents*, *night shift / day shift*, *pipeline*, *review gates*. Les chiffres sont mis en exergue en marge (×3 à ×5, 60 %), et leur source est donnée en une ligne de note (« McKinsey experience and observation across multiple companies ») ; une seule source externe est citée (guide budgétaire Boundev AI pour la répartition 70/30).

**Autorité** : celle du cabinet et de sa pratique de transformation ; pas de cas client nommé, pas de méthodologie de mesure détaillée. **Public cible** : décideurs qui arbitrent la taille des équipes et l'allocation du portefeuille.

## Pense-betes

- **Sprint quotidien** : la nuit (16 h), l'usine d'agents enrichit les exigences, vérifie l'architecture, conçoit, code, teste et rédige un rapport ; le jour (8 h), les humains font la revue de sprint, un *spec-and-code working session* en binôme sur les chemins critiques, la synchronisation transverse (juridique, conformité, design), le refactoring du code faible, l'affinage des garde-fous (contexte, skills, prompts, workflows) et la planification de la nuit suivante.
- **Quatre prérequis** du sprint de 24 h : une vision claire de ce qu'il faut construire (roadmap, standard) ; un environnement technique **standard et cohérent** (frameworks communs, architecture modulaire) ; un chemin **exigences → code** structuré de façon identique d'un projet à l'autre ; les **mêmes parties prenantes** sur toute la chaîne de valeur.
- **70 / 30** : exigences, conception, code et tests pèsent ~70 % de la dépense tech ; le déploiement ~30 %. Le CI/CD classique n'automatise que la seconde part.
- Exhibit 2 : un pipeline d'*agent squads* (flux de processus → exigences enrichies → conception haut et bas niveau → microservices de validation et de transformation → squad de tests unitaires), avec les humains **en revue à la fin**. Entrées codifiées : specs d'interface, garde-fous techniques, exigences non fonctionnelles, catalogue de règles, *YAML rules framework*.
- **Graphe de connaissance par domaine** : relie feedback client, décisions d'architecture, docs de conception, tickets, activité GitHub, incidents, règles de conformité résumées. Exemple d'onboarding : SharePoint (enquêtes), observabilité (points d'abandon), Jira (stories prévues), GitHub (services existants), savoir implicite des SME.
- Gains revendiqués du graphe : des questions qui demandaient **des semaines d'entretiens** avec des SME traitées **en minutes** ; toute décision traçable jusqu'à sa source (une dépriorisation reliée aux données d'usage) ; montée en compétence plus rapide.
- Démarche **organique**, autour des domaines prioritaires et des programmes en cours, pas une ontologie descendante. Rapprochement : [[talisman-modern-data-101-ontology-pipeline-refresh-2026-05-04]].
- Exhibit 4 (illustratif) : **~100 ETP, 200 années-personnes, 24 mois, 10 équipes de 8-12** (PO, BA, tech lead, devs, testeurs) → **~60 ETP, ~100 années-personnes, 18 mois, 16 équipes de 3-4** (PO, tech lead, *AI-enabled engineer*). Soit ~50 % d'effort en moins et ~60 % de taille d'équipe moyenne en moins.
- Trois priorités pour capter la valeur : **reskilling** (une équipe centrale maintient les usines d'agents ; les ingénieurs développent jugement, revue de code et supervision) ; intégrer les rôles de l'**outer loop** (risque, juridique, tests, achats), avec des contrôles *policy as code* intégrés dès la conception ; **réallouer la capacité** libérée (roadmaps, modernisation, nouveaux produits).
- Point de départ : les quelques **grands programmes** qui concentrent l'essentiel de la dépense (modernisation legacy, refontes brownfield, lancements).

## RésuméDe400mots

Jared Moon, Rory Walsh et Vito Di Leo, avec Adam Thelwall, tous associés de McKinsey, décrivent en mai 2026 la manière dont l'IA agentique transforme la livraison logicielle, qu'ils présentent comme l'avant-garde d'un changement plus large du modèle de delivery. L'article s'ouvre sur une scène : à 9 h, une product owner constate qu'une fonctionnalité est passée pendant la nuit d'exigences structurées à du code testé, avec cas limites signalés et dépendances d'architecture validées. Personne n'a travaillé tard ; les agents l'ont fait. Selon les auteurs, plusieurs entreprises obtiennent ainsi des gains de productivité de trois à cinq fois, avec des équipes réduites de 60 %, à condition de refondre le modèle opératoire pour une collaboration humains-agents vingt-quatre heures sur vingt-quatre.

Premier levier : le sprint quotidien. La nuit, une usine d'agents exécute le travail structuré ; le jour, les humains revoient les sorties, lèvent les ambiguïtés, renforcent les garde-fous et alignent les parties prenantes. Leur rôle devient la supervision du système qui produit les artefacts. Cela suppose une vision produit claire, un environnement technique standardisé, un chemin exigences-code uniforme et des parties prenantes stables.

Deuxième levier : supprimer les passages de relais humains. Le CI/CD automatise surtout tests et déploiement, environ 30 % de la dépense ; les 70 % restants, des exigences au code, restent manuels et interprétatifs. Codifier specs, exigences non fonctionnelles, garde-fous et diagrammes de séquence dans des formats lisibles par machine permet de faire tourner le pipeline de bout en bout en quelques heures, les humains n'intervenant qu'à des points de revue définis.

Troisième levier : une infrastructure de connaissance. Des graphes de connaissance par domaine servent de mémoire aux agents sur tout le cycle de vie logiciel, reliant feedback client, décisions d'architecture, tickets, activité GitHub et incidents. Un agent « bibliothécaire » répond en minutes à ce qui exigeait des semaines d'entretiens avec des experts, et rend chaque décision traçable. Les auteurs déconseillent une ontologie descendante : le graphe doit croître organiquement autour des domaines prioritaires.

Quatrième levier : redimensionner équipes et portefeuille. Des équipes de huit à douze personnes laissent place à des pods de trois ou quatre profils qualifiés supervisant les agents ; l'exemple illustratif passe de 200 à 100 années-personnes et de 24 à 18 mois. Cela exige du reskilling, l'intégration des fonctions de contrôle (risque, juridique, achats) via le policy as code, et une réallocation consciente de la capacité libérée. Les auteurs recommandent de commencer par les grands programmes qui concentrent la dépense, et prévoient que les rôles humains se concentreront sur l'architecture, le jugement produit et la conception des systèmes.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jared Moon | PERSONNE | travaille_chez | McKinsey | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Rory Walsh | PERSONNE | travaille_chez | McKinsey | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Vito Di Leo | PERSONNE | travaille_chez | McKinsey | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| McKinsey | ORGANISATION | publie | Rewiring software delivery for the agentic era | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Rewiring software delivery for the agentic era | DOCUMENT | mesure | "×3 à ×5 de productivité, -60 % de taille d'équipe" | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| Rewiring software delivery for the agentic era | DOCUMENT | affirme_que | "Les gains viennent de la refonte du modèle opératoire, pas du seul déploiement d'agents" | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Sprint de 24 heures | METHODOLOGIE | utilise | usine d'agents | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Sprint de 24 heures | METHODOLOGIE | remplace | sprint de deux semaines | METHODOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Sprint de 24 heures | METHODOLOGIE | est_basé_sur | architecture standardisée et modulaire | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Rewiring software delivery for the agentic era | DOCUMENT | mesure | "Exigences à tests : ~70 % de la dépense tech ; déploiement : ~30 %" | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| CI/CD | METHODOLOGIE | s_applique_à | tests et déploiement | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Artefacts lisibles par machine | CONCEPT | réduit | passages de relais humains | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Graphe de connaissance | TECHNOLOGIE | permet | autonomie des agents | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Graphe de connaissance | TECHNOLOGIE | fait_partie_de | SDLC | METHODOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Agent bibliothécaire | TECHNOLOGIE | utilise | Graphe de connaissance | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Agent bibliothécaire | TECHNOLOGIE | améliore | "Questions d'experts traitées en minutes au lieu de semaines" | MESURE | 0.82 | DYNAMIQUE | déclaré_article |
| McKinsey | ORGANISATION | s_oppose_à | ontologie descendante | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Rewiring software delivery for the agentic era | DOCUMENT | mesure | "~100 ETP / 200 années-personnes / 24 mois → ~60 ETP / ~100 années-personnes / 18 mois" | MESURE | 0.8 | STATIQUE | déclaré_article |
| Policy as code | METHODOLOGIE | s_applique_à | Outer loop | CONCEPT | 0.87 | ATEMPOREL | déclaré_article |
| McKinsey | ORGANISATION | recommande | "Commencer par les quelques grands programmes qui concentrent la dépense" | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| McKinsey | ORGANISATION | prédit | "Les rôles humains se concentreront sur l'architecture, le jugement produit et la conception des systèmes" | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Jared Moon | PERSONNE | rôle | Senior partner McKinsey, Londres | AJOUT |
| Rory Walsh | PERSONNE | rôle | Partner McKinsey, Dublin | AJOUT |
| Vito Di Leo | PERSONNE | rôle | Partner McKinsey, Zurich | AJOUT |
| McKinsey | ORGANISATION | secteur | Cabinet de conseil en stratégie | AJOUT |
| Rewiring software delivery for the agentic era | DOCUMENT | format | Article McKinsey Technology, 8 pages, 4 exhibits, mai 2026 | AJOUT |
| Sprint de 24 heures | METHODOLOGIE | définition | Équipe de nuit d'agents (16 h) + équipe de jour humaine (8 h) | AJOUT |
| Graphe de connaissance | TECHNOLOGIE | rôle | Mémoire des agents par domaine sur le cycle de vie logiciel | AJOUT |
| Agent bibliothécaire | TECHNOLOGIE | définition | Agent qui interroge le graphe de connaissance à la demande (questions multi-entités) | AJOUT |
| Policy as code | METHODOLOGIE | usage | Contrôles risque / juridique / conformité automatisés dans le SDLC | AJOUT |
| Outer loop | CONCEPT | définition | Fonctions support et contrôle : risque, juridique, tests, achats | AJOUT |
