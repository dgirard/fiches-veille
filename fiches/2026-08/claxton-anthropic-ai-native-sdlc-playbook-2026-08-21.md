---
themes: [agents-codage-ia-skills, strategie-frameworks, qualite-securite]
source: "Anthropic (blog claude.com)"
---
# claxton-anthropic-ai-native-sdlc-playbook-2026-08-21

## Veille

Guide long-form d'**Anthropic** signé **Louis Claxton** (équipe Applied AI), publié le **21 août 2026** sur le blog claude.com : **40 minutes** de lecture annoncées, environ **64 000 caractères**, présenté comme un recueil de *plays* tirés du travail de l'équipe avec ses clients. (A) Le diagnostic : le code n'étant plus le goulot, celui-ci se déplace vers les étapes situées à gauche et à droite du build (plan, revue/test, déploiement), les contrôles ligne-à-ligne cessent de tenir dès que l'agent écrit l'essentiel du diff, et le coût de gouvernance monte, les exceptions passant encore par des comités périodiques. (B) La réponse : six étapes (Plan, Design, Build, Test, Deploy, Maintain) organisées en **boucle** et non en chaîne, chacune se terminant par un **artefact committé** que la suivante lit — `intent.md`, `spec.md`, `plan.md`, le diff et ses tests, la PR et ses constats, l'enregistrement d'incident. (1) Le savoir institutionnel devient des fichiers versionnés : `CLAUDE.md`, skills, `REVIEW.md`, `bands.yaml`. (2) La gouvernance se scinde en deux couches, la skill posée comme contrôle consultatif et le hook comme couche déterministe derrière elle. La séparation des tâches est posée en invariant — l'agent qui écrit le code ne peut pas l'approuver — et le texte se clôt sur *« The loop keeps running. Human judgement stays above it. »* Le corpus tient déjà [[clinton-anthropic-secure-ai-native-sdlc-2026-07-21]] sur le versant sécurité du même cycle et [[hingel-augment-how-ai-changes-sdlc-six-stages-2026-06-08]] sur le même découpage en six étapes vu par un concurrent.

## Titre Article

The AI-Native SDLC playbook: How to transform your software development lifecycle with AI—stage by stage

## Date

2026-08-21

## URL

https://claude.com/blog/the-ai-native-sdlc-playbook

## Keywords

SDLC AI-native, cycle de vie logiciel, plays, intent.md, spec.md, plan.md, CLAUDE.md, REVIEW.md, bands.yaml, artefact committé, piste d'audit, plan mode, auto mode, hooks, skills, subagents, sessions parallèles, git worktrees, boucle de rétroaction, evals continues, revue de PR agentique, séparation des tâches, managed settings, sandbox, MCP, claude-code-action, Agent SDK, bandes de contrôle, règles Western Electric, OpenTelemetry, DORA, Claude Tag, indicateurs avancés, indicateurs retardés, gouvernance as code

## Authors

Louis Claxton (Anthropic, équipe Applied AI), sur le blog claude.com ; contributions créditées à Jim Blackhurst, Will Steuk et Jamal Arif.

## Ton

Profil : guide d'entreprise long-form à visée opérationnelle, voix « nous » de l'équipe Applied AI d'un éditeur qui décrit l'usage de ses propres produits, registre prescriptif et procédural, niveau technique élevé, public cible responsables plateforme, tech leads, équipes conformité et sécurité de grandes organisations, y compris régulées. La structure est celle d'un **manuel** plus que d'un essai : chaque *play* suit la même grille — ce qui change, prérequis, infrastructure, étapes d'exécution, considérations de gouvernance, indicateur avancé et indicateur retardé — et presque chacun s'accompagne d'un artefact montré tel quel (`intent.md`, `plan.md`, `CLAUDE.md`, `SKILL.md`, `settings.json`, `bands.yaml`, un workflow GitHub Actions). Le vocabulaire est emprunté au contrôle interne — *control objectives*, *separation of duties*, *approval gates*, *audit trail*, *blast radius* — et sert à traduire des pratiques d'agent dans les catégories d'un auditeur. La rhétorique procède par opposition binaire systématique, chaque play ouvrant sur un couple *Traditional* / *AI-native*. Le texte assume son rôle commercial sans le masquer : les produits nommés (Claude Code, Claude Design en bêta, Claude Tag en bêta publique, Code Review en *research preview*, Cowork) sont les siens, et la section finale renvoie à quinze pages de documentation. Il reste néanmoins qualifié sur ses propres limites — la skill est dite ne rien forcer, les managed settings sont donnés comme point de départ à ajuster et non comme recommandation à copier.

## Pense-betes

- **Trois conséquences quand le build cesse d'être la contrainte** : (1) le goulot se déplace vers les étapes qui tournent encore à vitesse humaine (plan, revue/test, déploiement) ; (2) les contrôles deviennent inapplicables — relire chaque ligne avait un sens quand un humain l'avait écrite ; (3) le coût de gouvernance monte, les exceptions passant par des comités périodiques. Exemple donné : une équipe sécurité dimensionnée pour du débit humain, face à quoi soit la file de revue s'allonge, soit le code part sous-revu.
- **Le fil conducteur est l'artefact committé**, pas l'outil : chaque étape se termine en écrivant dans le contrôle de version, la suivante commence en le lisant, et la chaîne de commits **est** la piste d'audit. Le `.md` domine en amont parce que le product owner et l'agent lisent le même fichier ; à partir du build, l'artefact est le code et ses traces.
- **Déclencheurs en cascade** : un `intent.md` accepté déclenche la passe exigences/design, un `spec.md` approuvé déclenche le plan mode, une PR mergée déclenche le pipeline, une bande franchie en production écrit l'`intent.md` suivant. On commence en promptant chaque étape à la main ; l'état cible est la boucle où chaque artefact accepté arme la barrière suivante.
- **Skill vs hook — la distinction porte l'édifice de contrôle** : la skill rend l'application de la politique probable sans obliger une session à s'y conformer ; le hook est déterministe et bloque l'action. Une politique qui doit toujours tenir a besoin d'un hook ou d'une passe de revue derrière la skill. Corollaire : un hook qui *demande* une approbation humaine appartient au déploiement, pas au build, où il remettrait une personne sur le chemin critique de toutes les sessions parallèles.
- **Systèmes légataires** : pour chaque artefact, nommer **un** système comme source de vérité (le dépôt, ou Jira/ServiceNow avec les `.md` en copies de travail), le reste ne détenant qu'un lien. Le simple **chaînage** — l'artefact porte l'ID de l'enregistrement, l'enregistrement porte le SHA du commit — est donné comme barre minimale de démarrage.
- **Test** : la boucle de rétroaction (tests, build, diff de capture d'écran) tourne pendant toute la tâche ; le sous-agent vérificateur est une passe finale à contexte neuf, pour que le verdict ne soit pas teinté par les hypothèses qui ont produit le code. Pour un correctif, écrire d'abord le test qui échoue, le committer, puis interdire à l'agent de le modifier via un hook. Les evals sont le pendant AI-native des portes QA : **20 à 50 tâches réelles** rejouées à chaque changement de `CLAUDE.md`, de skill ou de hook, chaque incident devenant un eval permanent.
- **Maintain, la fermeture de boucle** : la **détection reste déterministe** (moyenne et écart-type sur fenêtre glissante, règles Western Electric, script versionné et testé, aucun modèle impliqué) ; Claude n'est invoqué qu'une fois la bande franchie, et le palier fixe ce qu'il peut faire — 1σ journalise, 2σ diagnostique en lecture seule, 3σ propose (PR ou runbook pré-approuvé). Le rollback est désigné comme le chemin qui doit être le **plus répété** du pipeline.
- ⚠️ **Ce que le texte ne chiffre pas** : aucun résultat quantifié, ni gain de délai ni taux d'adoption. Les nombres du guide sont des **paramètres de mise en œuvre** (20-50 evals, deux ou trois sessions parallèles pour commencer) ; les résultats restent des indicateurs à mesurer soi-même, dont la source est nommée à chaque fois (git log, métadonnées de PR, export OpenTelemetry, DORA, outil de suivi d'incidents).
- **À relier** : [[sfeir-sdlc-ia-cycle-11-phases-2026-06-16]] (découpage concurrent, en onze phases) et [[sfeir-code-review-anneau-contraintes-2026-07-30]] (l'anneau de contraintes autour de l'agent, dont hooks et revue sont ici deux anneaux distincts).

## RésuméDe400mots

Louis Claxton, de l'équipe Applied AI d'Anthropic, publie le 21 août 2026 un guide de mise en œuvre d'un cycle de vie logiciel « AI-native ». Le point de départ est un déséquilibre : les organisations écrivent désormais du code à une vitesse inconcevable un an plus tôt, mais les processus qui l'entourent — portes d'approbation, revues, passations, politiques — n'ont pas bougé. Le SDLC traditionnel a été conçu pour un monde où l'écriture du code était l'étape la plus longue et la plus coûteuse ; ses contrôles supposent en outre que chaque geste est posé par un humain.

Trois conséquences en découlent. Le goulot se déplace vers les étapes qui tournent encore à vitesse humaine, de part et d'autre du build. Les contrôles cessent d'être applicables : relire chaque ligne avait un sens quand une personne l'avait écrite. Et le coût de gouvernance augmente, les exceptions passant par des comités périodiques.

La réponse conserve les objectifs de contrôle et change le mode d'exécution. Le processus devient une boucle, avec l'IA embarquée en chaque point, organisée en six étapes — Plan, Design, Build, Test, Deploy, Maintain — décomposées en *plays* suivant tous la même grille, jusqu'à la mesure. Le fil conducteur est l'artefact committé. L'intention est captée par son auteur d'origine comme `intent.md` ; exigences et design fusionnent en une session produisant `spec.md`, contrainte par les skills de marque, sécurité, conformité et UX ; le build démarre en plan mode et fige `plan.md` avant toute écriture de code. La chaîne de commits tient lieu de piste d'audit.

Le savoir institutionnel devient des fichiers versionnés : `CLAUDE.md` pour le contexte du dépôt, les skills pour les politiques transverses, `REVIEW.md` pour la doctrine de revue, `bands.yaml` pour les seuils de production. La gouvernance se scinde en deux couches, la skill étant un contrôle consultatif et le hook la couche déterministe qui bloque ou demande une approbation. Un exemple de *managed settings* détaille clé par clé ce que chaque réglage achète en contrôle, du refus de lecture des secrets à la version plancher imposée.

L'étape Maintain ferme la boucle : un script déterministe surveille une métrique, et le franchissement d'une bande invoque Claude sans humain dans le chemin d'appel, à une autonomie fonction du palier. Ce que l'agent trouve est réécrit en `intent.md` et repart dans le cycle. Claude Tag, en bêta publique sur Slack, étend le schéma aux incidents arrivant par messagerie. Aucun résultat chiffré n'est avancé : le guide livre des indicateurs à mesurer et nomme leur source.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Anthropic | ORGANISATION | publie | The AI-Native SDLC playbook | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Louis Claxton | PERSONNE | a_créé | The AI-Native SDLC playbook | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| The AI-Native SDLC playbook | DOCUMENT | affirme_que | le goulot se déplace du build vers les étapes restées à vitesse humaine | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| SDLC AI-native | METHODOLOGIE | est_variante_de | SDLC | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| SDLC AI-native | METHODOLOGIE | utilise | artefact committé | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| artefact committé | CONCEPT | permet | piste d'audit | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| intent.md | DOCUMENT | fait_partie_de | SDLC AI-native | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| spec.md | DOCUMENT | est_basé_sur | intent.md | DOCUMENT | 0.91 | ATEMPOREL | déclaré_article |
| plan.md | DOCUMENT | est_basé_sur | spec.md | DOCUMENT | 0.90 | ATEMPOREL | déclaré_article |
| Plan mode | METHODOLOGIE | permet | plan accepté avant toute écriture de code | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| CLAUDE.md | DOCUMENT | s_applique_à | contexte du dépôt lu à chaque session | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Claude Skills | TECHNOLOGIE | s_applique_à | politique appliquée pendant l'écriture du code | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| hooks | TECHNOLOGIE | améliore | Claude Skills | TECHNOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| Louis Claxton | PERSONNE | affirme_que | une skill est un contrôle consultatif, rien n'oblige une session à la suivre | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| REVIEW.md | DOCUMENT | s_applique_à | passes de revue bugs, sécurité et conformité au spec et au plan | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| séparation des tâches | CONCEPT | s_applique_à | l'agent qui écrit le code ne peut pas l'approuver | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| evals continues | METHODOLOGIE | s_applique_à | configuration d'agent versionnée, testée comme du code | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Louis Claxton | PERSONNE | recommande | collecter 20 à 50 tâches réelles pour constituer la suite d'evals | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Louis Claxton | PERSONNE | recommande | démarrer à deux ou trois sessions parallèles par ingénieur | AFFIRMATION | 0.87 | ATEMPOREL | déclaré_article |
| git worktrees | TECHNOLOGIE | permet | sessions Claude Code parallèles isolées | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| bands.yaml | DOCUMENT | permet | paliers d'autonomie 1σ, 2σ, 3σ | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| détection de bande de contrôle | METHODOLOGIE | affirme_que | la détection reste entièrement déterministe, sans modèle impliqué | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| MCP | TECHNOLOGIE | permet | déploiement et rollback exposés comme outils cadrés par environnement | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| managed settings | TECHNOLOGIE | réduit | surface d'action de l'agent en environnement régulé | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| Claude Tag | TECHNOLOGIE | s_applique_à | réponse à incident depuis un canal Slack | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| DORA | DOCUMENT | mesure | performance de livraison, indicateur retardé du play CI/CD | MESURE | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Louis Claxton | PERSONNE | rôle | Auteur du guide, équipe Applied AI d'Anthropic | AJOUT |
| Anthropic | ORGANISATION | apport | Publie un playbook de SDLC AI-native tiré des déploiements de son équipe Applied AI | AJOUT |
| The AI-Native SDLC playbook | DOCUMENT | format | Guide de six étapes découpées en plays, ~40 min de lecture, publié le 21 août 2026 | AJOUT |
| SDLC | METHODOLOGIE | catégorie | Cycle classique en six étapes dont l'article dérive la variante AI-native | AJOUT |
| SDLC AI-native | METHODOLOGIE | structure | Boucle de six étapes (Plan, Design, Build, Test, Deploy, Maintain), chaque étape committant l'artefact que lit la suivante | AJOUT |
| intent.md | DOCUMENT | rôle | Proto-spec écrite par l'auteur de l'idée : problème, résultat attendu, contraintes, questions ouvertes | AJOUT |
| spec.md | DOCUMENT | rôle | Spécification exigences + design produite en une session, contrainte par les skills, points de friction signalés | AJOUT |
| plan.md | DOCUMENT | rôle | Plan d'implémentation accepté : fichiers touchés, ordre du travail, risques, preuves attendues | AJOUT |
| CLAUDE.md | DOCUMENT | rôle | Contexte de dépôt versionné : commandes, conventions, architecture, erreurs récurrentes de l'agent | AJOUT |
| REVIEW.md | DOCUMENT | rôle | Doctrine de revue : passes bugs/sécurité/conformité, définition de « Important », plafond de nits | AJOUT |
| bands.yaml | DOCUMENT | rôle | Config versionnée des bandes de contrôle production et des paliers d'autonomie associés | AJOUT |
| Plan mode | METHODOLOGIE | mécanisme | Claude lit le dépôt sans le modifier tant que le plan n'est pas accepté | AJOUT |
| hooks | TECHNOLOGIE | rôle | Couche déterministe : autoriser, demander une approbation, ou bloquer l'action de l'agent | AJOUT |
| Claude Skills | TECHNOLOGIE | rôle | Contrôle consultatif portant la politique de l'organisation au moment où le code est écrit | AJOUT |
| evals continues | METHODOLOGIE | déclenchement | Suite de 20 à 50 tâches réelles rejouée à chaque changement de configuration d'agent, plus incidents convertis en régressions | AJOUT |
| séparation des tâches | CONCEPT | invariant | L'agent qui produit le code n'a aucun chemin pour l'approuver ; la protection de branche exige un code owner humain | AJOUT |
| Claude Tag | TECHNOLOGIE | statut | Bêta publique sur Slack ; Claude membre du canal sous sa propre identité | AJOUT |
