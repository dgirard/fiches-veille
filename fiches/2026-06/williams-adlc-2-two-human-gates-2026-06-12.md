---
themes: [agents-codage-ia-skills]
source: "voodootikigod.com (Chris Williams)"
---
# williams-adlc-2-two-human-gates-2026-06-12

## Veille

Deuxième volet de la série ADLC de Chris Williams : il déroule le cycle qui découle de la « première loi » — huit phases (P0 Triage → P7 Distill), un gate déterministe entre chaque paire, et exactement deux moments humains obligatoires (approbation de la spec en P1, acceptation comportementale en P6). Principe clé : un handoff LLM→LLM sans checkpoint déterministe multiplie les taux d'erreur ; et une distribution des coûts « en haltère » (lourde aux deux bouts, légère au milieu) qui inverse l'économie agile.

## Titre Article

Two Human Gates and Everything Between Is Machine-Checked

## Date

2026-06-12

## URL

https://www.voodootikigod.com/adlc-2-two-human-gates

## Keywords

ADLC, cycle agentique en huit phases, gates déterministes, deux portes humaines, triage, interrogation, décomposition, rails, build, prosecution, integrate, distill, handoff LLM, compounding d'erreur, distribution en haltère, barbell spend, économie agile inversée, two-strike regeneration, tier de modèle, critères d'acceptation gelés, ingénierie de contexte, fenêtre de contexte utile

## Authors

Chris Williams (@voodootikigod)

## Ton

Profil : exposé d'architecture de processus (perspective praticien « nous/vous », registre méthodique en anglais), niveau technique élevé, public cible leads ingénierie déployant des agents à l'échelle. Le ton est celui de la spécification raisonnée : chaque phase est introduite avec ce qu'elle défend (rattachée aux modes F1-F8 du volet précédent), son gate de sortie déterministe et son éventuelle porte humaine. L'autorité tient à la cohérence systémique — le cycle « tombe » logiquement de la règle posée au volet 1 — et à la précision opérationnelle (gates nommés : Cold-Start Test, RED gate, Green gate, Zero-Findings gate). Style à forte densité structurelle, schéma de flux à l'appui (P0→P7 avec boucles Approved/Redo), métaphore économique de l'haltère (barbell) pour justifier où dépenser les tokens, et posture assumée de confiance déléguée à la machine entre les deux seules portes humaines.

## Pense-betes

- **Principe de compounding** : « an LLM→LLM handoff without a deterministic checkpoint multiplies error rates ». Entre deux phases doit exister un gate déterministe (compilateur, suite de tests, validateur) qui remet à zéro l'accumulation d'erreur probabiliste.
- **Huit phases** : P0 Triage (router par risque et blast radius, pas par complexité — le trivial court-circuite le cycle) ; P1 Interrogate (un agent interroge les parties prenantes *après* avoir lu le codebase ; sortie : spec dont les critères d'acceptation nomment leur méthode de vérification ; **Porte humaine 1 : approbation de la spec**) ; P2 Decompose (trancher en tickets atomiques exécutables par des agents frais, contrats explicites aux frontières ; gate : test Cold-Start par un modèle pas cher détecte les lacunes) ; P3 Rail (tests, stubs de types, contrats écrits depuis la spec en isolation puis **gelés** — le builder ne peut les modifier ; gate : tests échouent en RED pour les bonnes raisons, stubs typechecké) ; P4 Build (un agent par ticket, modèles mid-tier par défaut, two-strike regeneration, pas de personas) ; P5 Prosecute (agents frais chartés pour réfuter ; jusqu'à deux passes consécutives sans rien trouver) ; P6 Integrate (**Porte humaine 2 : acceptation comportementale**) ; P7 Distill (simplifier + miner les leçons).
- **Les deux portes humaines** : l'intention de spécification (P1) et la vérification comportementale (P6). Tout l'entre-deux est machine-gated. P6 : l'humain vérifie résumés de conformité, diffs de tests, comportement en exécution et hotspots — pas les diffs complets. La question : « Is this what I meant, *running*? »
- **Distribution en haltère (barbell)** : investir lourdement en tokens aux deux bouts (planification et revue), léger au milieu (exécution). Inverse l'économie agile où « misbuilding is what's expensive ».
- **Tier de modèle** : « model tier is a function of the cost of detecting an error, not of task prestige. »
- **Normes explicitement rejetées** : revue humaine de diff complet (théâtre au-delà de 500 lignes), planification « agile-light » pour du travail agentique, ingénierie de personas, construction multi-agents collaborative, DRY au moment de l'écriture, gates de pourcentage de couverture, quotas de tokens comme contrôle de coût, failover de modèle en cours de tâche.
- **Chaque rejet trace à un mode de défaillance** documenté au volet 1 : adopter un rituel exige de le justifier explicitement contre un défaut prouvé.

## RésuméDe400mots

Dans ce deuxième volet, Chris Williams matérialise la « première loi » de l'ADLC en un cycle concret : huit phases, un gate déterministe entre chaque paire, et exactement deux moments humains obligatoires. Le principe directeur est qu'un handoff direct de LLM à LLM, sans checkpoint déterministe, multiplie les taux d'erreur — chaque composant probabiliste branché sur un autre fait composer l'erreur. Les gates (compilateurs, suites de tests, validateurs) remettent cette accumulation à zéro.

Le cycle commence en P0 (Triage) : router le travail par risque et blast radius, pas par complexité ; le trivial court-circuite le cycle complet, le substantiel passe par les huit phases. P1 (Interrogate) est la phase à plus fort levier : un agent interroge les parties prenantes *après* avoir consulté le codebase, ce qui empêche des hypothèses génériques de combler les lacunes de la spec. Sa sortie est une spécification où chaque critère d'acceptation nomme sa méthode de vérification. C'est ici qu'intervient la Porte humaine 1, l'approbation de la spec — le moment de valeur humaine maximale.

P2 (Decompose) défend contre le context rot en découpant la spec en tickets atomiques exécutables par des agents frais, avec des contrats explicites aux frontières. P3 (Rail) écrit tests, stubs de types et contrats depuis la spec en isolation, puis les gèle : le builder ne peut pas les modifier. P4 (Build) lance un agent par ticket sur des modèles mid-tier par défaut, avec régénération à deux essais (tuer un agent qui patine et repartir à neuf) et sans personas — les capacités viennent du contexte, des outils et de la charte. P5 (Prosecute) déploie des agents frais chartés pour réfuter, la charge de la preuve portant sur la reproductibilité, jusqu'à deux passes consécutives sans rien trouver. P6 (Integrate) ouvre la Porte humaine 2, l'acceptation comportementale : l'humain vérifie la conformité à la spec, les diffs de tests, le comportement en exécution et les hotspots — pas les diffs complets. La question est « est-ce ce que je voulais dire, en train de tourner ? » Enfin P7 (Distill) simplifie et mine les leçons récurrentes en règles de lint, templates et skills.

Williams insiste sur une distribution des dépenses « en haltère » : lourde aux deux extrémités (planifier, prouver), légère au milieu (exécuter). Cela inverse l'économie agile classique où « mal construire est ce qui coûte cher ». Il rejette explicitement la revue de diff complet (théâtre au-delà de 500 lignes), les personas, le DRY à l'écriture ou les gates de couverture — chaque rejet étant tracé à un mode de défaillance précis.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Chris Williams | PERSONNE | publie | Two Human Gates and Everything Between Is Machine-Checked | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| ADLC | METHODOLOGIE | fait_partie_de | cycle agentique en huit phases | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | un handoff LLM→LLM sans checkpoint déterministe multiplie les taux d'erreur | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| gates déterministes | METHODOLOGIE | réduit | compounding d'erreur entre phases probabilistes | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| phase Interrogate | METHODOLOGIE | permet | specs dont les critères nomment leur méthode de vérification | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| phase Decompose | METHODOLOGIE | réduit | context rot | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| phase Rail | METHODOLOGIE | utilise | tests et stubs gelés que le builder ne peut modifier | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| phase Build | METHODOLOGIE | utilise | modèles mid-tier par défaut | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| deux portes humaines | CONCEPT | s_applique_à | intention de spec (P1) et vérification comportementale (P6) | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| distribution en haltère | CONCEPT | s_oppose_à | économie agile traditionnelle | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | le tier de modèle dépend du coût de détection d'une erreur, pas du prestige de la tâche | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| ADLC | METHODOLOGIE | s_oppose_à | revue humaine de diff complet au-delà de 500 lignes | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| chaque rejet de norme | CONCEPT | est_basé_sur | un mode de défaillance documenté des modèles | CONCEPT | 0.88 | ATEMPOREL | inféré |
| phase Build | METHODOLOGIE | utilise | two-strike regeneration | METHODOLOGIE | 0.87 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| cycle agentique en huit phases | METHODOLOGIE | phases | P0 Triage, P1 Interrogate, P2 Decompose, P3 Rail, P4 Build, P5 Prosecute, P6 Integrate, P7 Distill | AJOUT |
| deux portes humaines | CONCEPT | définition | P1 approbation de la spec (intention) et P6 acceptation comportementale (vérification) | AJOUT |
| gates déterministes | METHODOLOGIE | nature | Compilateurs, suites de tests, validateurs intercalés entre phases pour remettre l'erreur à zéro | AJOUT |
| distribution en haltère | CONCEPT | définition | Dépense de tokens lourde aux deux bouts (plan, revue), légère au milieu (exécution) | AJOUT |
| two-strike regeneration | METHODOLOGIE | règle | Tuer un agent qui échoue deux fois et repartir d'un contexte frais plutôt que le coacher | AJOUT |
| phase Interrogate | METHODOLOGIE | rôle | Phase à plus fort levier : interroger les parties prenantes après lecture du codebase | AJOUT |
| phase Rail | METHODOLOGIE | rôle | Geler tests/stubs/contrats depuis la spec avant le build | AJOUT |
| tier de modèle | CONCEPT | règle | Fonction du coût de détection d'une erreur, pas du prestige de la tâche | AJOUT |
