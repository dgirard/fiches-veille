---
themes: [architecture-construction, outils-plateformes, strategie-frameworks, economie-marche]
source: The New Stack
---
# janakiram-agent-platform-portability-contract-2026-07-20

## Veille

Analyse de Janakiram MSV (The New Stack, 20 juillet 2026) sur la **convergence architecturale** des plateformes d'agents d'entreprise des trois hyperscalers : en neuf mois, **Amazon Bedrock AgentCore**, **Microsoft Foundry** et **Gemini Enterprise Agent Platform** ont fait émerger les **mêmes six primitives** — runtime, mémoire, tool gateway, identité, observabilité, gouvernance — sous des noms de marque différents. Ce qui était il y a 18 mois une collection fragmentée de librairies devient une **couche plateforme** distincte. La thèse : cette convergence rejoue l'inflexion **PaaS de 2011-2016**, où **Cloud Foundry** et **Heroku** ont unifié VM, load balancers, files et secret stores autour d'un **contrat applicatif** portable — sauf qu'ici **aucun contrat équivalent n'existe encore**, et **aucun projet open source ne l'a revendiqué**. Conséquence : une entreprise ne peut pas **déplacer un agent d'un cloud à l'autre** (état de session, traces, identité terminent tous chez un seul fournisseur ; migrer = tout reconstruire). L'auteur propose un **mapping ligne à ligne** du contrat Cloud Foundry vers les agents, décline trois principes de conception (packager l'agent en **une unité déployable**, **attacher** les capacités plutôt qu'embarquer les fournisseurs, intégrer l'**opérationnel** à l'abstraction), pointe ce que les protocoles ouverts (MCP, A2A, OpenTelemetry) laissent hors champ — le **cycle de vie** —, et livre trois questions de due diligence : **gouvernance** (fondation neutre vs vendor), **packaging** (même artefact sur deux clouds sans réécriture), **état** (mémoire exportable). Verdict : celui qui possèdera le **control plane agent** définira *ce qu'est un agent*.

## Titre Article

Amazon, Microsoft, and Google are converging on the same enterprise agent architecture

## Date

2026-07-20

## URL

https://thenewstack.io/agent-platform-portability-contract/

## Keywords

Plateformes d'agents d'entreprise, convergence architecturale, portabilité, lock-in, réversibilité, contrat applicatif, Amazon Bedrock AgentCore, Microsoft Foundry, Azure AI Foundry, Foundry Agent Service, Entra Agent ID, Gemini Enterprise Agent Platform, Vertex AI, Agent Engine, Memory Bank, Agent Registry, Agent Substrate, runtime, mémoire, tool gateway, identité, observabilité, gouvernance, control plane agent, PaaS, Cloud Foundry, Heroku, buildpacks, Cloud Native Buildpacks, service broker, service binding, Korifi, Kubernetes, Twelve-Factor App, ressource attachée, MCP, Model Context Protocol, A2A, OpenTelemetry, conventions GenAI, OCI images, LangGraph, LangSmith, checkpointing, Agentic AI Foundation, Linux Foundation, goose, AGENTS.md, Strands, harness export, due diligence, gouvernance neutre, packaging, état exportable, hyperscalers, pouvoir de négociation, Janakiram MSV

## Authors

Janakiram MSV

## Ton

**Profil** : analyse d'architecte / analyste (thought leadership infrastructure) sous la plume de Janakiram MSV — praticien, analyste et conseil de startups de la Silicon Valley — pour The New Stack, adressée aux équipes plateforme et décideurs infra. Registre analytique et structuré (une thèse, une analogie historique filée, un tableau de mapping, trois principes, trois questions de diligence), technicité élevée mais didactique, longueur moyenne (~1600 mots).

**Style** : construit tout l'argument sur une **analogie historique** — la trajectoire PaaS 2011-2016 comme miroir de l'inflexion agent — et l'exploite jusqu'au bout (buildpacks qui survivent à Cloud Foundry via CNCF/Korifi ; Kubernetes qui gagne le marché mais hérite des principes). Posture d'analyste distancié : nomme la convergence « comportement rationnel plutôt que conspiration » (la marge est dans l'intégration verticale), refuse le prêchi-prêcha vendeur (« quel que soit ce qu'affirme la brochure de la plateforme »). Manie des **outils de décision réutilisables** : un tableau à trois colonnes (abstraction PaaS → équivalent agent → où la portabilité casse aujourd'hui), trois principes de conception nommés, trois questions de due diligence « en clair ». Sourçage factuel précis et daté (dates de GA, renommages, adhésions à la Linux Foundation). Renvoie à sa propre pièce antérieure sur l'Agent Substrate de Google. Chute prospective assumée (« Whoever ends up owning the agent control plane… defines what an agent is »). Note de transparence éditoriale TNS : l'actionnaire Insight Partners investit dans OpenAI, Anthropic, Real.

## Pense-betes

- **Idée-force : trois hyperscalers, une seule architecture.** En 9 mois, Amazon, Microsoft et Google ont convergé sur les **mêmes six primitives** d'agent d'entreprise — runtime, mémoire, tool gateway, identité, observabilité, gouvernance — sous des marques différentes. Ce qui était une collection fragmentée de librairies il y a 18 mois devient une **couche plateforme** à part entière.
- **Le trou dans la raquette : pas de contrat, donc pas de portabilité.** La convergence des *composants* ne produit pas la portabilité. Il manque le **contrat** (au sens PaaS) qui rendrait un agent agnostique de son lieu d'exécution. Aujourd'hui état de session, traces et identité **terminent tous chez un seul fournisseur** ; déplacer l'agent un an plus tard = **tout reconstruire**.
- **L'analogie directrice : PaaS 2011-2016.** Avant Cloud Foundry / Heroku, on assemblait VM, load balancers, files, secret stores et agents de monitoring, chacun avec son API. Le PaaS a unifié tout ça autour d'un **contrat applicatif** : « l'appli déclare ce dont elle a besoin et reste agnostique de l'endroit où elle tourne ». **Ce qui comptait, c'était le contrat, pas l'implémentation.**
- **Leçon Cloud Foundry : le contrat survit à la plateforme.** Cloud Foundry n'a **pas** gagné le marché (Kubernetes l'a fait), mais ses principes ont voyagé : buildpacks nés chez Heroku (2011) → **Cloud Native Buildpacks** (Pivotal+Heroku, janv. 2018, acceptés CNCF en octobre) ; abstraction Cloud Foundry reconstruite sur K8s via **Korifi**. Les entreprises sur ce socle en 2016 avaient une portabilité que **la plupart des équipes agent ne peuvent pas acheter aujourd'hui**.
- **Les trois plateformes, marketing déshabillé.** (1) **AgentCore** (GA oct. 2025) : 7 services composables (runtime, gateway, memory, browser, code interpreter, identity, observability) ; runtime = fenêtres d'exécution de **8 h** isolées ; gateway branche des serveurs **MCP** existants ; observabilité exportée via **OpenTelemetry** vers CloudWatch. (2) **Microsoft Foundry** (renommage d'Azure AI Foundry au **1ᵉʳ janv. 2026**) : runtime managé isolé par session, identité **Entra Agent ID**, mémoire session/user/procédurale, tracing OpenTelemetry. (3) **Gemini Enterprise Agent Platform** (retrait du nom Vertex AI à Cloud Next 2026) : Agent Engine → **Deployments**, plus Memory Bank, Sessions, Agent Registry, Policies, Gateways.
- **La convergence n'est pas un complot, c'est la marge.** Les entreprises d'infra bâtissent des plateformes **verticalement intégrées** parce que « l'intégration, c'est là qu'est la marge ». La conséquence retombe sur le **client** : identité, télémétrie et déploiement terminent chez un seul fournisseur → **la couche opérationnelle sous l'agent est ce qui résiste à la migration**.
- **Le mapping du contrat (tableau, à réutiliser en due diligence).** 8 lignes « abstraction PaaS → équivalent agent → où la portabilité casse » : source appli → code+instructions+suite d'éval (chaque framework a sa forme de package) ; buildpack → détection framework+packaging (pas de build contract partagé entre SDK) ; backing service → modèle/mémoire/retrieval/tool (fournisseurs câblés dans la logique) ; service binding → attachement authentifié (credentials émis par le cloud hôte) ; router → endpoint MCP/A2A (les protocoles existent, pas le cycle de vie) ; logs → traces/tool calls/coût/qualité (conventions GenAI encore en dev) ; release promotion → évaluer/versionner/déployer progressivement (l'éval couple à un harness vendor) ; policy → identité/permissions/approbations (identité liée à l'annuaire du fournisseur).
- **Trois principes de conception.** (1) **Packager l'agent en une unité déployable** : code, instructions, dépendances outils, contrat mémoire, permissions, suite d'éval voyagent **ensemble ou pas du tout**. AWS s'en approche avec son *harness export* (une commande → code **Strands** préservant modèle, prompt, outils, mémoire, conteneur), « le bon instinct pointé vers un seul cloud ». (2) **Attacher plutôt qu'embarquer** (leçon **Twelve-Factor**) : modèles, mémoire, retrieval, browsers, gateways = ressources attachées par config. « Un agent qui nomme son fournisseur de modèle dans sa logique applicative a déjà renoncé à la portabilité. » (3) **Intégrer l'opérationnel à l'abstraction** : les bonnes questions agent = l'agent a-t-il accompli la tâche, choisi les bons outils, dépassé son autorité, à quel coût, la qualité a-t-elle régressé après un update modèle.
- **Un agent n'est pas une web app avec un modèle greffé.** Trois différences portent tout le poids : comportement **probabiliste** (mêmes entrées → tool calls différents) ; **autorité déléguée** de l'utilisateur (un bug de permissions devient un effet de bord réel, pas une page d'erreur) ; les **dépendances changent le comportement sans déploiement de code** (un update modèle ou une description d'outil révisée modifie ce que l'agent décide). La règle Twelve-Factor « processus stateless » n'y survit pas : il faut des **workers jetables** *plus* un **état durable, inspectable et portable**. **LangGraph** le démontre en open source (checkpointing à chaque étape, interruptions humaines, reprise après crash) — mais le control plane est dans le produit commercial **LangSmith** : la fragmentation apparaît **à l'intérieur d'un même projet**.
- **Ce que les protocoles ouverts laissent hors champ : le cycle de vie.** MCP (accès outils/données), A2A (découverte/communication inter-agents), OpenTelemetry (conventions GenAI, la plupart des attributs encore « in development »), images OCI (échappatoire de packaging) : **les primitives existent presque toutes**. Mais **une fondation qui régit comment les agents parlent aux outils ne dit rien sur comment versionner un agent**, le promouvoir entre environnements ou le rollback quand une éval régresse. **Protocoles ≠ plateforme de cycle de vie.**
- **Le signal de concession des vendors.** La **Linux Foundation** a annoncé l'**Agentic AI Foundation** (décembre 2025) ; projets fondateurs : **MCP** (Anthropic), **goose** (Block), **AGENTS.md** (OpenAI) ; **AWS, Google et Microsoft membres platine** ; Google a versé **A2A** à la Linux Foundation. Les hyperscalers **admettent** qu'une couche neutre compte.
- **Trois questions de due diligence (à garder en tête pour choisir une plateforme agent).** (1) **Gouvernance** : le projet est-il contrôlé par une **fondation neutre** ou par le vendor qui vend la version managée ? (2) **Packaging** : le même artefact tourne-t-il sur **deux clouds sans réécriture** ? (3) **État** : la mémoire vit-elle **quelque part d'exportable** par l'entreprise ? **Aucun projet ouvert ne répond aux trois aujourd'hui.**
- **Enjeu final : qui possède le control plane possède la définition.** Comme Kubernetes a défini pods/deployments/services et façonné la pensée de toute une industrie, l'équivalent agent n'est **pas encore figé**. Celui qui possèdera le **control plane agent** ne possèdera pas seulement le déploiement : il définira **ce qu'est un agent**, quels composants il contient, ce qu'une équipe plateforme a le droit de remplacer. Un projet neutre rendrait aux entreprises le **pouvoir de négociation** que buildpacks et service brokers leur avaient donné — au bénéfice des vendors autant que des acheteurs.
- **À relier** : « The Development Environment Is The Next Layer To Collapse » (Greyling) et « Building for trillions of agents » (Levie) sur les couches d'agents ; identité des agents (fiche Uber Engineering, zero-trust/SPIRE) — même problème d'identité déléguée traité côté infra ; famille souveraineté / réversibilité / **Design to Exit** (fiche ZML/LLMD) — même logique « payer d'avance la couche qui rend le fournisseur remplaçable », transposée du silicium au control plane agent.

## RésuméDe400mots

En neuf mois, Amazon, Microsoft et Google ont chacun lancé ou renommé une plateforme d'agents d'entreprise, et **tous trois ont convergé sur la même architecture** : runtime, mémoire, tool gateway, identité, observabilité et gouvernance apparaissent désormais dans **Bedrock AgentCore**, **Microsoft Foundry** et la **Gemini Enterprise Agent Platform**, sous des noms différents. Ce qui était il y a 18 mois une collection fragmentée de librairies devient une **couche plateforme** distincte.

Pour lire où cela mène, Janakiram MSV convoque l'**inflexion PaaS de 2011-2016**. Avant, on assemblait VM, load balancers, files, secret stores et agents de monitoring, chacun avec son API. **Cloud Foundry** et **Heroku** ont unifié ces pièces autour d'un **contrat applicatif** : l'application déclare ce dont elle a besoin et reste agnostique de son lieu d'exécution. Ce qui comptait, c'était le **contrat, pas l'implémentation**. Cloud Foundry n'a pas gagné le marché — Kubernetes l'a fait — mais ses principes ont survécu (buildpacks → Cloud Native Buildpacks/CNCF ; abstraction reconstruite sur K8s via Korifi). L'écosystème agent approche la même inflexion **sans contrat équivalent**, et aucun projet open source ne l'a revendiqué.

Le coût est concret : état de session, traces et identité **terminent tous chez un seul fournisseur** ; déplacer un agent un an plus tard oblige à **tout reconstruire**. La convergence n'est pas un complot mais un comportement rationnel — l'intégration verticale, « c'est là qu'est la marge » — dont la conséquence retombe sur le client.

L'auteur propose un **mapping** du contrat Cloud Foundry vers les agents (source appli → code+éval ; buildpack → packaging ; backing service → modèle/mémoire ; binding → attachement authentifié ; router → MCP/A2A ; logs → traces/coût/qualité ; promotion → éval/versioning ; policy → identité), puis trois principes : **packager l'agent en une unité déployable** (AWS s'en approche avec son *harness export* vers du code Strands, « bon instinct pointé vers un seul cloud »), **attacher les capacités plutôt qu'embarquer les fournisseurs** (leçon Twelve-Factor), **intégrer l'opérationnel à l'abstraction**. Un agent n'est pas une web app : comportement probabiliste, autorité déléguée, dépendances qui changent le comportement sans déploiement. LangGraph le montre en open source, mais son control plane est dans LangSmith (produit commercial).

Les protocoles ouverts (MCP, A2A, OpenTelemetry, OCI) fournissent presque toutes les primitives, mais **pas le cycle de vie** : versionner, promouvoir, rollback. La **Linux Foundation** a lancé l'**Agentic AI Foundation** (déc. 2025, projets MCP/goose/AGENTS.md, hyperscalers membres platine). Restent trois questions de diligence — **gouvernance, packaging, état** — auxquelles aucun projet ouvert ne répond. Celui qui possèdera le **control plane agent** définira *ce qu'est un agent*.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Amazon Bedrock AgentCore | TECHNOLOGIE | converge_avec | Microsoft Foundry | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Microsoft Foundry | TECHNOLOGIE | converge_avec | Gemini Enterprise Agent Platform | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Janakiram MSV | PERSONNE | affirme_que | les trois hyperscalers ont convergé sur les mêmes six primitives d'agent (runtime, mémoire, tool gateway, identité, observabilité, gouvernance) | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| Janakiram MSV | PERSONNE | affirme_que | l'écosystème agent manque du contrat de portabilité qu'aucun projet open source n'a revendiqué | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Cloud Foundry | TECHNOLOGIE | permet | portabilité applicative via un contrat agnostique du lieu d'exécution | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| plateforme d'agents d'entreprise | TECHNOLOGIE | s_inspire_de | PaaS (Cloud Foundry, Heroku) | TECHNOLOGIE | 0.88 | ATEMPOREL | inféré |
| contrat de portabilité agent | CONCEPT | réduit | lock-in vis-à-vis d'un hyperscaler | CONCEPT | 0.85 | ATEMPOREL | inféré |
| Amazon Bedrock AgentCore | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Amazon Bedrock AgentCore | TECHNOLOGIE | utilise | OpenTelemetry | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Microsoft Foundry | TECHNOLOGIE | utilise | Entra Agent ID | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Microsoft Foundry | TECHNOLOGIE | est_variante_de | Azure AI Foundry | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Gemini Enterprise Agent Platform | TECHNOLOGIE | remplace | Vertex AI | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| LangGraph | TECHNOLOGIE | permet | état d'agent durable, inspectable et portable (checkpointing, reprise après crash) | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| LangGraph | TECHNOLOGIE | fait_partie_de | LangSmith | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| Model Context Protocol | TECHNOLOGIE | fait_partie_de | Agentic AI Foundation | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Linux Foundation | ORGANISATION | publie | Agentic AI Foundation | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| protocoles ouverts (MCP, A2A, OpenTelemetry) | TECHNOLOGIE | s_oppose_à | plateforme de cycle de vie agent | CONCEPT | 0.8 | ATEMPOREL | inféré |
| harness export AWS | TECHNOLOGIE | permet | conversion d'un harness configuré en code Strands (modèle, prompt, outils, mémoire préservés) | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Twelve-Factor App | METHODOLOGIE | recommande | traiter les capacités (modèle, mémoire, outils) comme des ressources attachées par configuration | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Janakiram MSV | PERSONNE | recommande | évaluer une plateforme agent sur trois questions : gouvernance neutre, packaging portable, état exportable | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Janakiram MSV | PERSONNE | prédit | celui qui possèdera le control plane agent définira ce qu'est un agent | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Kubernetes | TECHNOLOGIE | a_créé | abstractions (pods, deployments, services) façonnant la pensée de l'industrie | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Janakiram MSV | PERSONNE | rôle | Architecte praticien, analyste et conseil de startups Silicon Valley ; auteur The New Stack | AJOUT |
| Amazon Bedrock AgentCore | TECHNOLOGIE | catégorie | Plateforme d'agents d'entreprise AWS ; GA oct. 2025 ; 7 services composables (runtime, gateway, memory, browser, code interpreter, identity, observability) ; runtime 8 h isolé par session | AJOUT |
| Microsoft Foundry | TECHNOLOGIE | catégorie | Plateforme d'agents d'entreprise Microsoft (renommage d'Azure AI Foundry au 1ᵉʳ janv. 2026) ; runtime managé isolé, identité Entra Agent ID, mémoire session/user/procédurale | AJOUT |
| Gemini Enterprise Agent Platform | TECHNOLOGIE | catégorie | Plateforme d'agents d'entreprise Google (retrait du nom Vertex AI à Cloud Next 2026) ; Agent Engine→Deployments, Memory Bank, Sessions, Agent Registry, Policies, Gateways | AJOUT |
| contrat de portabilité agent | CONCEPT | définition | Équivalent agent du contrat applicatif PaaS : packager code+instructions+outils+mémoire+permissions+éval en une unité déployable, portable entre clouds | AJOUT |
| Cloud Foundry | TECHNOLOGIE | rôle | PaaS de référence (2011-2016) ; contrat applicatif, buildpacks, service brokers ; battu par Kubernetes, reconstruit via Korifi | AJOUT |
| Cloud Native Buildpacks | TECHNOLOGIE | historique | Nés chez Heroku (2011) → projet Pivotal+Heroku (janv. 2018) → accepté CNCF (oct. 2018) ; « une idée PaaS a survécu à la plateforme qui l'a produite » | AJOUT |
| LangGraph | TECHNOLOGIE | rôle | Framework open source démontrant workers jetables + état durable/inspectable/portable (checkpointing, interruptions humaines, reprise après crash) | AJOUT |
| LangSmith | TECHNOLOGIE | rôle | Produit commercial (control plane) autour de LangGraph : déploiement, évaluation, observabilité | AJOUT |
| Agentic AI Foundation | TECHNOLOGIE | historique | Fondation Linux Foundation annoncée déc. 2025 ; projets fondateurs MCP (Anthropic), goose (Block), AGENTS.md (OpenAI) ; AWS/Google/Microsoft membres platine ; A2A versé par Google | AJOUT |
| Model Context Protocol | TECHNOLOGIE | rôle | Standardise l'accès des agents aux outils et données ; projet fondateur de l'Agentic AI Foundation | AJOUT |
| A2A | TECHNOLOGIE | rôle | Protocole de découverte et communication inter-agents ; versé à la Linux Foundation par Google | AJOUT |
| harness export AWS | TECHNOLOGIE | rôle | Chemin d'export AWS : une commande transforme un harness configuré en code Strands (modèle, prompt, outils, mémoire, conteneur préservés), pointé vers un seul cloud | AJOUT |
| control plane agent | CONCEPT | enjeu | Couche non encore figée qui définira ce qu'est un agent, ses composants et ce qu'une équipe plateforme peut remplacer | AJOUT |
