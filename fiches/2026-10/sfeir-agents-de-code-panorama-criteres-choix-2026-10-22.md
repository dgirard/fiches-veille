---
themes: [agents-codage-ia-skills, outils-plateformes, qualite-securite]
source: SFEIR
---
# sfeir-agents-de-code-panorama-criteres-choix-2026-10-22

## Veille

Panorama **SFEIR AI** publié sur sfeir.com le **22 octobre 2026** (~32 000 signes, quatre tableaux, 35 sources notées). Il relève **33 agents de code** dans leur documentation, leur fichier de licence et leur politique de confidentialité, sans classement. Point de départ : le modèle ne départage plus les outils — le même Claude passe par plus de vingt des 33 harnais ; à modèle identique, Composio mesure moins de **1 000** tokens de contexte fixe sous **Pi** contre ~**6 900** sous **OpenCode**. Quatre critères. **(1)** La **licence réelle** : quinze outils Apache 2.0/MIT, Crush en FSL-1.1-MIT, MiMo Code en MIT à restrictions, ZCode code ouvert / binaires sous conditions, trois cas limites (dont **OpenClaude**, dérivé sans autorisation du code de Claude Code publié par erreur le 30 mars 2026), douze propriétaires. **(2)** **Ce que l'agent fait sans demander** : cinq outils n'approuvent rien par défaut, **Claude Code** démarre en mode auto avec classifieur depuis la 2.1.283. **(3)** La **juridiction** se lit au point de connexion : Kimi Code CLI a trois politiques pour un seul outil ; trois incidents d'exfiltration ou d'intrusion en 2026. **(4)** Les **fichiers de contexte** : **27 sur 33** lisent AGENTS.md. Recommandation : *« deux harnais et un AGENTS.md »*. Recoupe [[janakiram-agent-platform-portability-contract-2026-07-20]] sur la portabilité.

## Titre Article

Agents de code : les critères qui comptent avant le benchmark

## Date

2026-10-22

## URL

https://www.sfeir.com/articles/agents-de-code-panorama-criteres-choix/

## Keywords

agents de code, harnais, harness engineering, panorama, Claude Code, Codex CLI, OpenCode, Pi, Goose, Crush, Kimi Code CLI, Qwen Code, ZCode, MiMo Code, OpenClaude, licence open source, FSL, source disponible, mode d'approbation, yolo, bac à sable, juridiction des données, entraînement par défaut, rétention zéro, AGENTS.md, CLAUDE.md, SKILL.md, réversibilité, multi-harnais, rachats, fin de vie, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Panorama documentaire, registre d'analyste. Le texte refuse explicitement le classement (« les comparatifs qui en publient se contredisent ») et s'en tient à ce que chaque éditeur écrit au **22 octobre 2026**, date répétée comme borne de validité. Les citations de licences et de documentations sont reproduites en anglais, entre guillemets, avec le fichier source ; « non documenté » est posé comme une information en soi. Les limites des mesures sont signalées (« un seul évaluateur, trente tâches : un indice »). L'article est organisé par critère puis par lecteur (DSI, CTO, RSSI, achats), avec une recommandation finale opérationnelle et un calendrier de révision trimestriel. SFEIR précise utiliser quotidiennement Claude Code et Codex. Public : DSI, CTO, RSSI, juristes, acheteurs.

## Pense-betes

- **Périmètre** : 33 agents de code, quatre familles — éditeurs de modèles (Claude Code, Codex CLI, Antigravity, Grok Build, Meta Muse Code, Mistral Vibe), commerciaux multi-modèles (Cursor, Copilot, Devin, Factory, Amp, Kiro…), harnais open source (OpenCode, Pi, Goose, Cline, Crush…), laboratoires chinois (Qwen Code, Kimi Code CLI, ZCode, MiMo Code, DeepSeek Harness, CodeBuddy).
- **Le modèle ne départage plus** : Claude via plus de 20 harnais ; à modèle égal, Pi < **1 000** tokens de contexte fixe vs ~**6 900** pour OpenCode (Composio, 30 tâches).
- **Filiations** : Kilo et MiMo Code = forks d'OpenCode ; oh-my-pi = fork de Pi ; Qwen Code = fork de Gemini CLI v0.8.2 ; Crush continue l'opencode Go archivé.
- **Licences** : 15 libres ; Crush **FSL-1.1-MIT** (MIT deux ans après chaque version) ; MiMo Code MIT + interdiction militaire (hors définition OSI) ; ZCode code Apache / binaires réservés à la recherche personnelle ; **OpenClaude** dérivé de Claude Code 2.1.88 sans autorisation ; 12 propriétaires — Auggie : droit d'usage lié à l'abonnement.
- **Approbation par défaut** : rien demandé chez oh-my-pi (*yolo*), Pi, Amp, Cline CLI, OpenCode V2 ; Claude Code en **mode auto + classifieur** depuis la 2.1.283 (25 sept. 2026) ; Muse Code refuse de tourner sans sandbox. *« bash.patterns is an approval policy, not containment »*.
- **Juridiction** : se lit au point de connexion — Kimi Code CLI : Chine (kimi.com), pays non nommé (kimi.ai), Singapour (API). Mistral Vibe : UE par défaut mais entraînement par défaut hors Enterprise. Aucune qualification **SecNumCloud** relevée.
- **Incidents 2026** : Grok Build envoyait des dépôts entiers (juillet) ; ZCode 3.12.3 des instantanés `.git` (septembre) ; intrusion OpenCode Console, **1,4 %** des utilisateurs (17 octobre).
- **Marché** : Anysphere (Cursor) filiale de **SpaceX** (valeur implicite **60 Md$**) ; Continue racheté par Cursor ; Kilo par Anaconda ; Rovo Dev en fin de vie ; Gemini CLI fermé aux comptes individuels le 18 juin.
- **Contexte** : **27/33** lisent AGENTS.md ; Claude Code depuis la 2.1.277 (si pas de CLAUDE.md) ; huit outils écartent CLAUDE.md. SKILL.md (agentskills.io) largement implémenté.
- **Recommandation** : deux harnais par projet + AGENTS.md + skills dans `.agents/skills/` ; quatre lignes par candidat dans la politique d'outillage ; clé API, jamais un abonnement grand public ; révision trimestrielle.

## RésuméDe400mots

Ce panorama de SFEIR, publié le 22 octobre 2026, recense trente-trois agents de code à partir de leur documentation, de leur fichier de licence et de leur politique de confidentialité. Il ne propose aucun classement : le modèle appelé change tous les deux mois et le même Claude passe par plus de vingt de ces harnais. À modèle identique, c'est le harnais qui fait l'écart, comme le montre une mesure de Composio sur Pi et OpenCode. L'article retient donc quatre critères que les comparatifs ignorent.

Le premier est la licence réelle. Quinze outils relèvent d'Apache 2.0 ou MIT ; Crush est en source disponible (FSL-1.1-MIT) ; MiMo Code ajoute au MIT des restrictions d'usage, dont militaires ; ZCode ouvre son code mais réserve ses binaires ; OpenClaude déclare dériver, sans autorisation, du code de Claude Code publié par erreur en mars 2026. Douze outils sont propriétaires, et leur droit d'usage cesse avec l'abonnement. Le régime se lit dans le fichier de licence, pas dans le badge.

Le deuxième est ce que l'agent exécute sans demander. Cinq outils n'exigent aucune approbation par défaut, Claude Code confie depuis septembre 2026 l'arbitrage à un classifieur, d'autres demandent avant d'agir. Approbation, règles et confinement sont trois niveaux distincts, et un bac à sable système n'est présent par défaut que chez quelques éditeurs. Certains détails échappent à ces niveaux : fichier de configuration exécuté au lancement, hooks hors sandbox, orchestrateurs qui contournent les permissions.

Le troisième est la juridiction des données, qui se lit au point de connexion plutôt qu'au siège de l'éditeur. Un même outil chinois peut stocker en Chine ou à Singapour selon le compte ; un éditeur européen héberge dans l'Union par défaut mais entraîne sur les données hors offre Enterprise. Trois incidents de 2026 (Grok Build, ZCode, OpenCode Console) illustrent le risque, et aucune localisation ne vaut qualification.

Le quatrième est la réversibilité, dans un marché agité : rachat de Cursor par SpaceX, de Continue et de Kilo Code, fin de vie de Rovo Dev, fermeture de l'accès gratuit à Gemini CLI et Qwen Code. Ce qui reste quand l'outil part, c'est le contexte versionné : vingt-sept outils sur trente-trois lisent AGENTS.md, et le format SKILL.md est largement implémenté.

Les conséquences sont déclinées pour la DSI, le CTO, le RSSI et les achats. SFEIR recommande de garder deux harnais par projet, un outil principal et un harnais ouvert, de tenir les consignes dans AGENTS.md, d'inscrire les quatre critères dans la politique d'outillage, d'accéder aux modèles par clé API et de réviser le tableau chaque trimestre.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Agents de code : les critères qui comptent avant le benchmark | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le modèle ne départage plus les agents de code ; licence, approbation, juridiction et fichiers de contexte comptent davantage | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Composio | ORGANISATION | mesure | moins de 1 000 tokens de contexte fixe sous Pi contre ~6 900 sous OpenCode, à modèle identique | MESURE | 0.85 | STATIQUE | déclaré_article |
| Kilo Code | TECHNOLOGIE | est_variante_de | OpenCode | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| MiMo Code | TECHNOLOGIE | est_variante_de | OpenCode | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| oh-my-pi | TECHNOLOGIE | est_variante_de | Pi | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Qwen Code | TECHNOLOGIE | est_variante_de | Gemini CLI | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| OpenClaude | TECHNOLOGIE | est_basé_sur | Claude Code | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Crush | TECHNOLOGIE | utilise | Functional Source License | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | mode auto avec classifieur | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| oh-my-pi | TECHNOLOGIE | utilise | mode yolo par défaut | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| Kimi Code CLI | TECHNOLOGIE | affirme_que | le stockage dépend du compte : Chine (kimi.com), pays non nommé (kimi.ai), Singapour (API) | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| Grok Build | TECHNOLOGIE | observé_dans | envoi de dépôts entiers vers un bucket de l'éditeur (juillet 2026) | EVENEMENT | 0.86 | STATIQUE | déclaré_article |
| ZCode | TECHNOLOGIE | observé_dans | envoi d'instantanés de l'espace de travail, .git compris (septembre 2026) | EVENEMENT | 0.86 | STATIQUE | déclaré_article |
| Anysphere | ORGANISATION | fait_partie_de | SpaceX | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| Cursor | ORGANISATION | a_créé | Composer 2.5 | TECHNOLOGIE | 0.8 | STATIQUE | déclaré_article |
| AGENTS.md | TECHNOLOGIE | mesure | lu par 27 des 33 agents de code au 22 octobre 2026 | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | AGENTS.md | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| SKILL.md | DOCUMENT | permet | portabilité des skills entre harnais | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| AGENTS.md | TECHNOLOGIE | permet | réversibilité entre agents de code | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | stratégie multi-harnais | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | accéder aux modèles par clé API ou passerelle interne, jamais par abonnement grand public | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| harness engineering | METHODOLOGIE | s_applique_à | agents de code | TECHNOLOGIE | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| agents de code | TECHNOLOGIE | panorama | 33 outils relevés au 22 octobre 2026, quatre familles | AJOUT |
| OpenCode | TECHNOLOGIE | catégorie | Harnais open source (Anomaly), base de Kilo Code et MiMo Code | AJOUT |
| Pi | TECHNOLOGIE | catégorie | Harnais minimal MIT de Mario Zechner, entré chez Earendil en avril 2026 | AJOUT |
| OpenClaude | TECHNOLOGIE | licence | Déclare dériver du code de Claude Code 2.1.88 sans autorisation d'Anthropic | AJOUT |
| Crush | TECHNOLOGIE | licence | FSL-1.1-MIT : usage concurrent exclu, MIT deux ans après chaque version | AJOUT |
| Kimi Code CLI | TECHNOLOGIE | juridiction | Trois politiques selon le point de connexion | AJOUT |
| ZCode | TECHNOLOGIE | incident | Instantanés de l'espace de travail envoyés jusqu'à la 3.12.3 | AJOUT |
| AGENTS.md | TECHNOLOGIE | adoption | Lu par 27 des 33 agents ; par Claude Code depuis la 2.1.277 | AJOUT |
| stratégie multi-harnais | METHODOLOGIE | définition | Deux harnais par projet (un principal, un ouvert) partageant AGENTS.md et skills | AJOUT |
