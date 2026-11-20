---
themes: [qualite-securite, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-agents-md-telechargements-codex-claude-code-2026-10-27

## Veille

Article **SFEIR AI** publié sur sfeir.com le **27 octobre 2026** (~14 000 signes, neuf sources notées : rapport Forever Security, BleepingComputer, CSO Online, Checkmarx, documentations Anthropic et OpenAI). Il restitue l'analyse publiée le **22 octobre 2026** par **Forever Security** d'un fichier **AGENTS.md** d'environ **13 Ko** trouvé dans le dossier Téléchargements d'un client, qui demandait à **OpenAI Codex** d'ajouter un serveur MCP à sa configuration globale pour installer `function-color`, paquet de la campagne npm **MALFEX**. Trois apports. **(A)** Les résultats : sur Codex, l'attaque aboutit dans plus de **90 %** des essais de laboratoire ; sur **Claude Code**, une variante écrite par les chercheurs (redirection via `ANTHROPIC_BASE_URL`, jeton OAuth rejoué) aboutit environ une fois sur deux. **(B)** Le mécanisme : deux comportements voulus combinés — l'agent suit le fichier d'instructions du dossier, le navigateur enregistre dans `~/Downloads` ; *« Markdown is the new executable »*. SFEIR classe AGENTS.md et CLAUDE.md dans la **supply chain logicielle**. **(C)** Les parades outil par outil (`trust_level`, `requirements.toml`, `managed-settings.json`, `allowedProviders`) et de gouvernance. Les réserves sont posées : un seul cas réel, vecteur inconnu, taux non validés indépendamment. Prolonge [[sfeir-agents-de-code-panorama-criteres-choix-2026-10-22]].

## Titre Article

AGENTS.md piégé dans Téléchargements : comment Codex et Claude Code ont été détournés, et les parades

## Date

2026-10-27

## URL

https://www.sfeir.com/articles/agents-md-telechargements-codex-claude-code/

## Keywords

AGENTS.md, CLAUDE.md, injection de prompt indirecte, fichier d'instructions, supply chain logicielle, dossier Téléchargements, Codex, Claude Code, Forever Security, MALFEX, function-color, npm, serveur MCP, config.toml, settings.json, ANTHROPIC_BASE_URL, jeton OAuth, trust_level, requirements.toml, managed settings, allowedProviders, disableBypassPermissionsMode, frontière de confiance, sécurité des agents de code, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Article d'alerte et de remédiation, registre technique et mesuré. Il distingue soigneusement le cas observé (Codex) de la variante construite par les chercheurs (Claude Code), signale les divergences entre le rapport et BleepingComputer, et précise ce qui relève du rapport plutôt que de la documentation des éditeurs. Une section « Gardons la mesure » rapporte le jugement d'IDC (avertissement crédible, pas preuve d'exploitation massive) et note que Forever vend la surveillance d'agents. La partie parades adopte le registre de la consigne, avec chemins de fichiers et clés de configuration exacts, et signale les points à tester avant généralisation. Public : RSSI, administrateurs de postes, responsables d'équipes de développement.

## Pense-betes

- **22 octobre 2026** : Forever Security (Gal Weizman, Omer Samet) bloque un agent qui installe `function-color` → téléchargeur `function-flag` (campagne **MALFEX**, Checkmarx, opérateur actif depuis 2023, 8 paquets malveillants sur 12).
- Vecteur : AGENTS.md « Engineering Work Guidelines » (~13 Ko) dans `~/Downloads` → ajoute `[mcp_servers.project-tools]` dans `~/.codex/config.toml` + `codex exec` avec `--dangerously-bypass-approvals-and-sandbox`. Persistance : la config machine charge le serveur à chaque session. **Arrivée du fichier inconnue**.
- **Codex** : > **90 %** de réussite en labo (charge inoffensive). **Claude Code** : variante des chercheurs via `ANTHROPIC_BASE_URL` → approbation humaine requise, ~1 fois sur 2 ; exécution de code ~1 sur 5 (BleepingComputer dit ~50 %).
- Claude Code lit AGENTS.md depuis la **2.1.277** en l'absence de CLAUDE.md.
- Pourquoi : agent qui suit le fichier d'instructions + navigateurs (Chrome, Edge, Firefox) qui enregistrent sans demander. *« Markdown is the new executable »*.
- Télémétrie Forever (non vérifiable) : ~**la moitié** des clients lancent un agent dans Téléchargements ; > **1 300** sessions Claude Code depuis ce dossier.
- Règle (Amit Kumar Jena) : *« An instruction file can change what the agent tries. It must never change what the agent is allowed to do »*.
- **Parades générales** : lancer l'agent depuis la racine d'un projet ; lire tout AGENTS.md non écrit par soi ; hostile toute demande de désactiver approbations/sandbox ou d'ajouter MCP/proxy/URL d'API.
- **Codex** : auditer `config.toml` ; `trust_level = "untrusted"` pour Downloads (n'ignore pas forcément AGENTS.md — à tester) ; `requirements.toml` avec liste `mcp_servers` approuvés.
- **Claude Code** : `managed-settings.json` avec `disableBypassPermissionsMode`, `allowManagedPermissionRulesOnly`, `allowManagedMcpServersOnly` ; `allowedProviders` (2.1.285+) ; réglage « Project instructions » ; attention au mode `-p`.

## RésuméDe400mots

Cet article de SFEIR, publié le 27 octobre 2026, analyse un incident documenté par Forever Security le 22 octobre. Un fichier AGENTS.md d'environ treize kilo-octets, d'apparence banale, a été trouvé dans le dossier Téléchargements d'un client. Il demandait à OpenAI Codex de modifier sa configuration globale pour y ajouter un serveur MCP chargé d'installer un paquet npm malveillant, issu de la campagne MALFEX, puis de lancer une session enfant sans approbation ni sandbox. Forever, qui surveille le comportement des agents sur les postes, a bloqué l'installation en pleine session. Personne ne sait comment le fichier est arrivé là ; les chercheurs ont seulement montré qu'une page web peut en déposer un.

En laboratoire, l'attaque a abouti sur Codex dans plus de 90 % des essais. Pour Claude Code, aucun fichier malveillant n'a été trouvé, mais les chercheurs ont construit une variante qui redirige le trafic API vers leur serveur ; elle exige une approbation humaine et n'a réussi qu'environ une fois sur deux, avec vol d'un jeton OAuth rejoué contre l'API réelle. Claude Code lit lui aussi les AGENTS.md depuis septembre 2026 quand aucun CLAUDE.md n'existe.

L'attaque combine deux comportements voulus : un agent suit le fichier d'instructions du dossier où on le lance, et les principaux navigateurs enregistrent les téléchargements sans demander. Aucun n'est une faille, et les protections des systèmes d'exploitation ne voient qu'un fichier texte. L'exposition est amplifiée par les habitudes : selon la télémétrie de Forever, environ la moitié de ses clients lancent un agent dans Téléchargements.

SFEIR range désormais AGENTS.md et CLAUDE.md dans la supply chain logicielle : la frontière de confiance passe par le dossier de travail, et tout ce qui y écrit devient fournisseur d'instructions. L'article garde la mesure : un seul cas réel, un vecteur inconnu, des taux non validés de façon indépendante et un éditeur qui vend la surveillance d'agents.

Les parades sont détaillées. Pour tous les agents : lancer depuis la racine d'un projet volontairement créé, lire tout fichier d'instructions non écrit par soi, traiter comme hostile toute demande de désactiver les protections ou d'ajouter un serveur ou une URL. Pour Codex : auditer la configuration, déclarer Téléchargements non fiable, déployer un fichier d'exigences qui restreint les serveurs MCP. Pour Claude Code : paramètres managés interdisant le contournement des permissions et limitant serveurs MCP et fournisseurs. Côté gouvernance : politique de dossiers de travail outillée, revue de code des fichiers d'instructions, registre de paquets filtrant et formation courte des équipes.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | AGENTS.md piégé dans Téléchargements : comment Codex et Claude Code ont été détournés, et les parades | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Forever Security | ORGANISATION | publie | Markdown Is the New Executable | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Markdown Is the New Executable | DOCUMENT | affirme_que | un AGENTS.md déposé dans Téléchargements a fait installer un paquet npm malveillant par Codex | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Codex | TECHNOLOGIE | utilise | AGENTS.md | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | AGENTS.md | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Forever Security | ORGANISATION | mesure | plus de 90 % de réussite de l'attaque sur Codex en laboratoire | MESURE | 0.85 | STATIQUE | déclaré_article |
| Forever Security | ORGANISATION | mesure | variante Claude Code : écriture de settings.json aboutie environ une fois sur deux | MESURE | 0.82 | STATIQUE | déclaré_article |
| function-color | TECHNOLOGIE | fait_partie_de | MALFEX | EVENEMENT | 0.88 | STATIQUE | déclaré_article |
| Checkmarx | ORGANISATION | publie | MALFEX npm malware campaign | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| injection de prompt indirecte | CONCEPT | s_applique_à | AGENTS.md | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | AGENTS.md et CLAUDE.md relèvent de la supply chain logicielle, au même titre qu'un package.json | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Amit Kumar Jena | PERSONNE | affirme_que | un fichier d'instructions peut changer ce que l'agent tente, jamais ce qu'il a le droit de faire | CITATION | 0.86 | ATEMPOREL | déclaré_article |
| Sakshi Grover | PERSONNE | affirme_que | avertissement crédible plutôt que preuve d'une exploitation massive ; taux non validés indépendamment | AFFIRMATION | 0.84 | STATIQUE | déclaré_article |
| managed settings | TECHNOLOGIE | réduit | détournement de Claude Code par fichier d'instructions piégé | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| requirements.toml | TECHNOLOGIE | réduit | ajout de serveurs MCP non approuvés dans Codex | CONCEPT | 0.84 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | lancer un agent depuis la racine d'un projet, jamais depuis Téléchargements, le dossier personnel ou le Bureau | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | placer fichiers d'instructions et dossiers .codex/ et .claude/ sous revue de code avec propriétaires désignés | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Forever Security | ORGANISATION | activité | Surveillance du comportement des agents sur les postes clients | AJOUT |
| Markdown Is the New Executable | DOCUMENT | date | Rapport Forever Security du 22 octobre 2026 (Gal Weizman, Omer Samet) | AJOUT |
| AGENTS.md | TECHNOLOGIE | risque | Fichier d'instructions devenu vecteur d'injection lorsqu'il est déposé dans le dossier de travail | AJOUT |
| MALFEX | EVENEMENT | description | Campagne npm analysée par Checkmarx (5 octobre 2026), opérateur actif depuis août 2023 | AJOUT |
| function-color | TECHNOLOGIE | rôle | Paquet npm installant le téléchargeur malveillant function-flag | AJOUT |
| injection de prompt indirecte | CONCEPT | définition | Instructions glissées à un agent via un contenu non fiable qu'il lit | AJOUT |
| managed settings | TECHNOLOGIE | rôle | Paramètres Claude Code verrouillés par l'administrateur (managed-settings.json, MDM) | AJOUT |
