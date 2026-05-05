# habert-wenvision-proj-ai-repo-agent-ide-doctrine-2026-05-05

## Veille
Article méthode d'Antoine HABERT (WEnvision) qui formalise **PROJ-AI** : couche méthodologique légère pour que les projets collectifs deviennent transmissibles plutôt que de mourir avec leur livrable. Triade structurante : un **repo git versionné** (source unique), un **agent IA** (Claude Code, Cursor) qui lit la doctrine à chaque session, et une **doctrine en markdown** qui spécifie les protocoles de décision et les comportements d'agent. Six zones répertoires (DOCS/, IDEAS/, DR/, OUT/, DOCTRINE/, AGENT/), cycle opérationnel **DPEV** (Décider → Promettre → Exécuter → Vérifier), Decision Records scorés sur 7 dimensions, double interface (Studio métier + CLI/IDE tech), cinq directives agent, et bibliothèque partagée **proj-ai-commons** qui permet de bootstrap un projet en 30 minutes vs 1 semaine. Métriques sur 3 missions : onboarding **3 semaines → 2 jours**, décisions structurelles tracées **30% → 100%**, compilation archi **6 semaines → continu**. Aphorisme central : ***"Le projet n'est pas un sous-produit du livrable. Le projet EST le livrable."*** Posture explicite : technologie 20%, **discipline d'équipe 80%**.

## Titre Article
PROJ-AI — pour que vos projets ne s'arrêtent plus au livrable (Un repo, un agent, un IDE — pourquoi PROJ-AI ?)

## Date
2026-05-05

## URL
https://www.wenvision.com/fr/articles/un-repo-un-agent-un-ide-pourquoi-proj-ai/

## Keywords
Antoine HABERT, WEnvision, PROJ-AI, repo agent IDE doctrine, méthodologie agentique projet, mémoire projet transmissible, livrable comme projet, DPEV cycle, Décider Promettre Exécuter Vérifier, Decision Records, scoring 7 dimensions, six zones repo, DOCS IDEAS DR OUT DOCTRINE AGENT, slash-commands /dr-create /livrable-update, PROJ-AI Studio cockpit, dual interface métier tech, cinq directives agent, ingestion doctrine systématique, citation sources internes, end-of-session summaries, proj-ai-commons, bootstrap 30 minutes, onboarding 2 jours, décisions tracées 100%, archéologie PM négligeable, technology 20% team discipline 80%, agent-agnostic markdown, Claude Code Cursor, méthodologie accompagnée, missions 6-18 mois, mémoire organisationnelle, doctrine versionnée

## Authors
Antoine HABERT (WEnvision — cabinet français de conseil en stratégie et IA agentique).

## Ton
**Profil** : Article méthode signé par un consultant senior d'un cabinet français spécialisé IA agentique (WEnvision), publié en français sur le site corporate. Format hybride entre démonstration d'expertise et présentation produit/méthode (PROJ-AI étant une méthodologie packagée par le cabinet). Public cible : DSI, directeurs de projet, COMEX-IT, *project managers* d'entreprises engagées dans des missions de transformation IA, partenaires de mission ; secondairement, lecteurs francophones de la veille agentique cherchant des frameworks opérationnels.

**Style** : Voix méthodologique posée, registre conseil-stratégique francisé. HABERT alterne entre **constat-douleur** (les projets meurent quand le livrable part), **mécanique** (la triade repo+agent+doctrine, les six zones, le cycle DPEV) et **chiffrage prudent** (3 missions actives, 31 décisions enregistrées, métriques avant/après). Pas de hype, pas de promesse exorbitante : le ton est celui d'un cabinet qui a fait le travail et présente un cadre éprouvé en 3 missions. Métaphores ramassées (*"archéologie PM"*, *"bootstrap 30 min vs 1 semaine"*).

**Aphorisme central** : ***"Le projet n'est pas un sous-produit du livrable. Le projet EST le livrable."*** Cette phrase fait office de pivot rhétorique et inverse le rapport canonique entre projet et output — c'est la **mémoire et la transmissibilité** qui sont la valeur, pas l'artefact final.

**Position épistémique** : équilibrée et honnête. Deux *caveats* explicites : (1) ***"technologie 20%, discipline d'équipe 80%"*** — refus du solutionnisme technique ; (2) ***"agent-agnostic"*** — pas de lock-in Claude exclusif, l'overlay markdown supporte plusieurs LLMs. Posture commerciale assumée : *méthodologie accompagnée, pas self-service software*. WEnvision se positionne explicitement comme cabinet d'accompagnement, pas comme éditeur de SaaS.

**Autorité** : construite par (a) la cohérence du cadre proposé (six zones / cycle DPEV / cinq directives), (b) les métriques chiffrées sur 3 missions clients actives, (c) la mention de *proj-ai-commons* qui suggère un capital méthodologique consolidé, (d) la précédente publication HABERT 2025-10-29 (*IA agentique en production : leçons de deux ans*) — déjà au dossier veille. Autorité francophone construite par la pratique consultante.

## Pense-betes
- **Date / source** : 5 mai 2026, WEnvision (cabinet FR conseil IA agentique). Auteur : **Antoine HABERT** — déjà au dossier veille avec sa fiche *"IA agentique en production"* (2025-10-29). Cet article est une formalisation d'une méthodologie maison.
- **URL slug** : *un-repo-un-agent-un-ide-pourquoi-proj-ai*. Titre éditorial : *"PROJ-AI — pour que vos projets ne s'arrêtent plus au livrable"*.
- **Problème adressé** : *"Les projets s'arrêtent à leur livrable, ne laissent aucune mémoire organisationnelle. Décisions critiques intraçables, onboarding nouveaux membres ~3 semaines, dirigeants incapables de reconstruire le rationale plusieurs mois après."* C'est le *project amnesia problem* classique du conseil et de l'IT projet.
- **Aphorisme central** : ***"Le projet n'est pas un sous-produit du livrable. Le projet EST le livrable."*** Inversion qui pose la mémoire/transmissibilité comme valeur centrale.
- **Triade PROJ-AI** :
  1. **Repository (git-versioned)** — source unique de vérité contenant raw materials, decisions, deliverables, doctrine.
  2. **Agent** — Claude Code, Cursor ou équivalent qui *lit la doctrine du repo à chaque session*.
  3. **Doctrine** — fichiers markdown de gouvernance spécifiant protocoles de décision, comportements agent, patterns appris.
- **Six zones répertoires** :
  | Zone | Rôle |
  |------|------|
  | `DOCS/` | Raw inputs (interviews, audits, données) |
  | `IDEAS/` | Hypothèses, draft thinking |
  | `DR/` | **Decision Records** scorés sur 7 dimensions |
  | `OUT/` | Livrables compilés |
  | `DOCTRINE/` | Gouvernance et pratiques |
  | `AGENT/` | Slash-commands et traces de session |
- **Cycle opérationnel DPEV** : ***Décider → Promettre → Exécuter → Vérifier***. Quatre étapes traçables qui transforment idées floues → livrables défendables.
- **Double interface** :
  - **Métier** : *PROJ-AI Studio* — application desktop avec vues Cockpit, Guide, Weekly, Monthly.
  - **Tech** : intégration CLI/IDE avec slash-commands : `/dr-create`, `/livrable-update`.
  - **Sous-jacent unique** : un seul repo, pas de fragmentation de données entre interfaces.
- **Cinq directives agent (PROJ-AI)** :
  1. **Ingest doctrine** avant de répondre.
  2. **Cite explicitly** les sources internes.
  3. **Propose Decision Records** pour les choix émergents.
  4. **Never override doctrine** unilatéralement.
  5. **Produce end-of-session summaries**.
- **Métriques observées sur 3 missions actives** :
  | Métrique | Avant | Après |
  |----------|-------|-------|
  | Onboarding nouveau membre | ~3 semaines | **~2 jours** |
  | Décisions structurelles tracées | ~30% | **100%** |
  | Compilation doc architecture | 6 semaines (sprint finale) | **Continu** |
  | Temps archéologie PM | ~30% | **Négligeable** |
- **proj-ai-commons** (bibliothèque partagée) : chaque projet contribue patterns anonymisés/aseptisés (slash-commands, templates Decision Records, fragments de doctrine) → **bootstrap nouveaux projets en 30 minutes vs 1 semaine**.
- **Status mai 2026** :
  - **3 missions clients actives**
  - **31 décisions enregistrées**
  - **Studio en preview interne**, pas encore public sur GitHub
  - **Positionné comme méthodologie accompagnée**, pas self-service software (modèle commercial WEnvision).
- **Public cible** : équipes mixtes tech/métier sur engagements de **6 à 18 mois** — projets internes, missions conseil, audits, builds nouveaux services.
- **Deux caveats critiques explicites** :
  1. ***"Technology is 20%, team discipline is 80%"*** — l'adoption nécessite shift culturel vers le decision-tracing explicite.
  2. ***"Not Claude-exclusive"*** — overlay agent-agnostic ; markdown + file conventions supportent multiples plateformes LLM.
- **Articulation dossier veille** :
  - **Suite logique** de la fiche HABERT 2025-10-29 *"IA agentique en production : leçons de deux ans"* — passage des principes (4 piliers) à une **méthodologie packagée** (PROJ-AI). Le cabinet WEnvision consolide son offre.
  - **Convergence française** avec **Wescale Usine Logicielle Augmentée** (2026-05-03) :
    - Wescale = chaîne de production logicielle, focus sur le **build**.
    - WEnvision PROJ-AI = méthodologie **projet/conseil**, focus sur la **gouvernance + mémoire**.
    - Les deux insistent sur la *gouvernance injectée* (Wescale) / *doctrine versionnée* (HABERT) comme barrière à l'entrée.
  - **Six zones repo + slash-commands + AGENT/** = transposition au domaine **conseil/projet** des patterns *AGENTS.md / SKILL.md / Skills* documentés par :
    - Vincent *Superpowers* (2026-04-02)
    - Anthropic *Skills* (2025-10-16, Willison 2025-10-16)
    - Karpathy *Skills pour Claude Code* (2026-01-27)
    - Gao *Vercel AGENTS.md* (2026-01-27)
    - Osmani *Agent Harness Engineering* (2026-04-19) — primitive *AGENTS.md "pilot's checklist, not style guide. Earn each line."*
    - Curran *Skills-Based Plugin Architecture* (2026-04-16) — marketplace 267 skills.
  - **Decision Records (DR/)** = transposition au pilotage de projet du pattern **ADR** (Architecture Decision Records) — déjà chez Wescale (2026-05-03 *"Intention : PRD & ADR"*).
  - **Cycle DPEV** = équivalent FR projet du **Plan-Work-Assess-Compound** (Shipper/Klaassen 2025-12-11), du **CDLC** (Debois/Tessl 2026-02-19/26), du *Ralph Loop* (Trivedy 2026-03-10), du *Plan-Execute-Test-Reflect* (Rohit 2026-04-29).
  - **proj-ai-commons** comme bibliothèque partagée = équivalent du *plugin marketplace privé* d'Intercom (Curran 2026-04-16, 153 contributeurs / 267 skills) à l'échelle d'un cabinet de conseil multi-clients.
  - **Métriques onboarding 3 sem → 2 jours** rejoint Stripe Minions (2026-02-09/19), Curran Intercom (2026-04-16), StrongDM Software Factory (2026-02-06) sur l'amplification de productivité par l'orchestration agentique.
  - **"Technology 20% team discipline 80%"** corrobore HBR Anand & Wu *Gen AI Playbook* (2025-11) *"70% people/processes"* + BCG *Brain Fry* (2026-03-05) *"70% people/processes"* — convergence des cabinets sur le ratio.
  - **Public cible francophone** complète le dossier français : **Caseau** (2025-11-05), **Ensarguet** (2025-11-04 et 2026-03-11), **Wescale** (2026-05-03), **Mornati** (2026-03-14), **ALMIA AG2R** (2026-03), **Habert WEnvision** (2025-10-29 + 2026-05-05), **Dèbes Les Echos** (2026-04-22), **Geudin** (2026-01-26).
- **À mobiliser pour** : design d'une méthodologie projet IA-native pour cabinet ou DSI ; *templates Decision Records* à standardiser ; argumentaire commercial sur la mémoire organisationnelle ; benchmark *bootstrap 30 min* à présenter en COMEX ; structuration d'un *proj-commons* interne pour entreprises multi-projets.
- **Limites à signaler** : (a) métriques sur 3 missions seulement — échantillon faible, biais cabinet ; (b) Studio en preview interne, donc pas vérifiable extérieurement ; (c) le ratio 20/80 est une affirmation prudente sans étude empirique propre ; (d) la *bibliothèque proj-ai-commons* n'est pas (encore) publique — pas de validation externe possible.

## RésuméDe400mots

Antoine HABERT (WEnvision, cabinet FR de conseil IA agentique) publie le 5 mai 2026 un article méthode qui formalise **PROJ-AI**, une couche méthodologique légère pour que les projets collectifs deviennent **transmissibles plutôt que de mourir avec leur livrable**. Le diagnostic : les projets s'arrêtent à leur livrable, ne laissent aucune mémoire organisationnelle, les décisions critiques deviennent intraçables, l'onboarding d'un nouveau membre prend trois semaines. Aphorisme central : *"Le projet n'est pas un sous-produit du livrable. Le projet EST le livrable."*

La méthodologie repose sur une **triade** : (1) un **repository git versionné** comme source unique de vérité ; (2) un **agent IA** (Claude Code, Cursor ou équivalent) qui lit la doctrine à chaque session ; (3) une **doctrine en markdown** spécifiant protocoles de décision et comportements d'agent. Le repo est organisé en **six zones** : `DOCS/` (raw inputs), `IDEAS/` (hypothèses), `DR/` (Decision Records scorés sur 7 dimensions), `OUT/` (livrables), `DOCTRINE/` (gouvernance), `AGENT/` (slash-commands et traces de session).

Le cycle opérationnel **DPEV** — *Décider → Promettre → Exécuter → Vérifier* — articule quatre étapes traçables qui transforment des idées floues en livrables défendables. Une **double interface** combine PROJ-AI Studio (vues Cockpit/Guide/Weekly/Monthly pour le métier) et CLI/IDE avec slash-commands `/dr-create`, `/livrable-update` (pour la tech), au-dessus du même repo unique. Cinq **directives agent** structurent le comportement : ingérer la doctrine avant de répondre, citer explicitement les sources internes, proposer des Decision Records pour les choix émergents, ne jamais outrepasser la doctrine, produire des résumés de fin de session.

Sur **trois missions actives** (31 décisions enregistrées), HABERT documente : onboarding nouveau membre **3 semaines → 2 jours**, décisions structurelles tracées **30% → 100%**, compilation doc architecture **6 semaines → continu**, temps d'archéologie du PM **30% → négligeable**. La bibliothèque partagée **proj-ai-commons** capitalise les patterns anonymisés (templates DR, slash-commands, fragments de doctrine) et permet de bootstrap un nouveau projet en **30 minutes au lieu d'une semaine**.

Deux *caveats* honnêtes : (1) ***"technologie 20%, discipline d'équipe 80%"*** — refus explicite du solutionnisme ; (2) ***"agent-agnostic"*** — markdown supporte plusieurs LLMs. Status : Studio en preview interne, méthodologie accompagnée par le cabinet (pas self-service).

Cette pièce convergente avec **Wescale Usine Logicielle Augmentée** (2026-05-03) et la précédente fiche HABERT (2025-10-29) consolide une doctrine française de l'industrialisation IA. PROJ-AI transpose au pilotage projet/conseil les patterns *Skills* (Vincent), *Plugin Marketplace* (Curran/Intercom), *AGENTS.md* (Anthropic, Vercel, Osmani) et *Decision Records* (Wescale). À mobiliser comme cadre opérationnel pour cabinets, DSI et équipes projet 6-18 mois.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Antoine HABERT | PERSONNE | a_créé | PROJ-AI | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Antoine HABERT | PERSONNE | travaille_chez | WEnvision | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| PROJ-AI | METHODOLOGIE | repose_sur | triade repo + agent + doctrine | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| PROJ-AI | METHODOLOGIE | organise_en | six zones répertoires | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Cycle DPEV | METHODOLOGIE | structure | Décider → Promettre → Exécuter → Vérifier | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Decision Records | METHODOLOGIE | sont_scorés_sur | 7 dimensions | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Agent IA | TECHNOLOGIE | doit_ingérer | doctrine avant chaque réponse | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| PROJ-AI | METHODOLOGIE | propose | double interface Studio + CLI/IDE | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| proj-ai-commons | TECHNOLOGIE | permet | bootstrap projet en 30 min vs 1 semaine | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| WEnvision | ORGANISATION | accompagne | 3 missions actives PROJ-AI | EVENEMENT | 0.96 | DYNAMIQUE | déclaré_article |
| PROJ-AI | METHODOLOGIE | réduit | onboarding de 3 semaines à 2 jours | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| PROJ-AI | METHODOLOGIE | augmente | traçabilité décisions de 30% à 100% | CONCEPT | 0.94 | STATIQUE | déclaré_article |
| Antoine HABERT | PERSONNE | affirme_que | "Le projet EST le livrable" | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Antoine HABERT | PERSONNE | affirme_que | technologie 20% / team discipline 80% | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| PROJ-AI | METHODOLOGIE | est | agent-agnostic (multi-LLM) | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| PROJ-AI | METHODOLOGIE | est_positionné_comme | méthodologie accompagnée pas self-service | CONCEPT | 0.94 | DYNAMIQUE | déclaré_article |
| PROJ-AI | METHODOLOGIE | cible | équipes mixtes tech/métier sur 6-18 mois | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Doctrine markdown | TECHNOLOGIE | est_versionnée_dans | repository git | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| PROJ-AI | METHODOLOGIE | est_construite_sur | doctrine versionnée + slash-commands | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Antoine HABERT | PERSONNE | rôle | Consultant senior WEnvision, créateur de PROJ-AI, déjà publié sur l'IA agentique en production (2025-10-29) | MISE_A_JOUR |
| WEnvision | ORGANISATION | secteur | Cabinet français de conseil en stratégie et IA agentique, méthodologie accompagnée | AJOUT |
| PROJ-AI | METHODOLOGIE | définition | Couche méthodologique légère pour rendre les projets collectifs transmissibles via repo+agent+doctrine ; transforme les projets en artefacts réutilisables | AJOUT |
| Triade PROJ-AI | CONCEPT | composants | (1) Repository git versionné, (2) Agent IA lisant doctrine à chaque session, (3) Doctrine markdown gouvernance | AJOUT |
| Six zones PROJ-AI | CONCEPT | détail | DOCS/ (raw inputs), IDEAS/ (hypothèses), DR/ (Decision Records 7 dim), OUT/ (livrables), DOCTRINE/ (gouvernance), AGENT/ (slash-commands + traces) | AJOUT |
| Cycle DPEV | METHODOLOGIE | définition | Décider → Promettre → Exécuter → Vérifier — quatre étapes traçables idée → livrable défendable | AJOUT |
| Decision Records 7 dimensions | METHODOLOGIE | description | Decision Records scorés sur 7 dimensions, traces tous choix structurants du projet | AJOUT |
| PROJ-AI Studio | TECHNOLOGIE | description | Application desktop avec vues Cockpit, Guide, Weekly, Monthly pour utilisateurs métier (preview interne mai 2026) | AJOUT |
| Slash-commands PROJ-AI | TECHNOLOGIE | exemples | /dr-create, /livrable-update — interface CLI/IDE pour utilisateurs tech | AJOUT |
| Cinq directives agent PROJ-AI | METHODOLOGIE | détail | (1) ingest doctrine, (2) cite sources, (3) propose DR, (4) never override doctrine, (5) end-of-session summaries | AJOUT |
| proj-ai-commons | TECHNOLOGIE | description | Bibliothèque partagée patterns anonymisés (templates DR, slash-commands, doctrine) — bootstrap 30 min vs 1 semaine | AJOUT |
| "Le projet EST le livrable" | CONCEPT | source | Aphorisme central HABERT — inverse rapport projet/output au profit de la mémoire et transmissibilité | AJOUT |
| Métriques PROJ-AI | EVENEMENT | description | Sur 3 missions actives : onboarding 3 sem → 2 jours, traçabilité 30% → 100%, doc archi 6 sem → continu, archéologie PM 30% → négligeable | AJOUT |
| Caveat 20/80 (HABERT) | CONCEPT | source | "Technology is 20%, team discipline is 80%" — refus explicite solutionnisme technique | AJOUT |
| Agent-agnostic (PROJ-AI) | CONCEPT | description | Markdown + file conventions supportent Claude, Cursor et autres LLMs — pas de lock-in | AJOUT |
