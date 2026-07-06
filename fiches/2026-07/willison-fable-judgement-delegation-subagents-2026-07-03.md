# willison-fable-judgement-delegation-subagents-2026-07-03

## Veille

Note courte de Simon Willison (weblog) relayant deux conseils entendus lors d'un *Fireside Chat* à l'AIE avec Cat Wu et Thariq Shihipar (équipe Claude Code) : **laisser le modèle (Fable, et dans une certaine mesure Opus) exercer son propre jugement plutôt que de lui dicter des règles** — illustré sur la décision d'écrire ou non des tests. Second conseil, de Jesse Vincent : pour **économiser les précieux tokens Fable** (avant une hausse de prix imminente), demander à Fable de **déléguer les petites tâches à des modèles moins puissants**, en le laissant juger lequel. Willison montre le prompt exact utilisé (« *use your judgement to decide an appropriate lower power model and run that in a subagent* ») et le **fichier mémoire** que Claude Code a écrit en réponse. Domaine : ingénierie de prompt, agents de codage, économie des tokens, orchestration multi-modèles.

## Titre Article

Fable's judgement

## Date

2026-07-03

## URL

https://simonwillison.net/2026/Jul/3/judgement/

## Keywords

Jugement du modèle, délégation à des subagents, model override, économie de tokens, Fable, Opus, Sonnet, Haiku, Claude Code, mémoire d'agent, fichier memory, prompt engineering, Cat Wu, Thariq Shihipar, Jesse Vincent, ne pas sur-spécifier, hausse de prix des tokens

## Authors

Simon Willison

## Ton

**Profil** : note de blog très courte (« note »), première personne, registre praticien et conversationnel, faible densité mais forte valeur d'usage. Niveau technique moyen-élevé, adressé à des utilisateurs quotidiens d'agents de codage.

**Style** : anecdotique et immédiat — Willison rapporte des conseils reçus (« *the most interesting tips I got* »), les applique **en direct** (« *I prompted Claude Code just now* ») et livre le résultat brut (le prompt exact, le fichier mémoire généré) avec une conclusion empirique honnête (« *So far it seems to be working well* »). Autorité par la **démonstration reproductible** plutôt que par l'argumentation : il ne théorise pas, il montre l'artefact. Pas de métaphore ; ton utilitaire, presque un *lab notebook* public. La tension économique (« *the few days we have left before the prices go up* ») donne un caractère daté et périssable au conseil. **Public cible** : développeurs utilisant Claude Code / Fable, sensibles au coût et à l'efficacité.

## Pense-betes

- **Idée-force : le jugement bat la prescription.** Conseil de Cat Wu & Thariq Shihipar (équipe Claude Code, *Fireside Chat* à l'AIE) : laisser **Fable** (et dans une certaine mesure **Opus**) décider *comment* travailler, plutôt que de dicter des règles rigides. Le modèle a assez de discernement pour arbitrer lui-même.
- **Exemple canonique — les tests.** Au lieu de la règle explicite « *only use automated testing for larger features, don't update and run tests for small copy or design changes* », il vaut mieux dire simplement à Fable **d'utiliser son propre jugement** pour décider quand écrire des tests. La règle codée en dur est plus fragile que le jugement contextuel.
- **Second conseil (Jesse Vincent) — économiser les tokens Fable via la délégation.** Contexte daté : **hausse de prix imminente** (« *the few days we have left before the prices go up* »). Parade : demander à Fable de **confier les petites tâches à des modèles moins puissants**, en le laissant juger lequel — au lieu de tout traiter au modèle premium.
- **Le prompt exact utilisé** : « *For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent* ». Le pattern combine les deux conseils : jugement délégué **+** orchestration multi-modèles via **subagents** avec *model override*.
- **L'artefact généré — un fichier mémoire.** Claude Code a écrit tout seul `~/.claude/projects/<projet>/memory/delegate-coding-to-subagents.md` (frontmatter `type: feedback`, `node_type: memory`), qui **encode la règle et son mode d'application** : *sonnet* pour l'implémentation substantielle, *haiku* pour les éditions triviales/mécaniques ; **le jugement, la review et la synthèse restent au modèle principal** (design, audit, synthèse de données = jamais délégués).
- **Doctrine sous-jacente de la délégation** : « *implementation work rarely needs the top-tier model; judgment, review, and synthesis stay with the main loop* ». La boucle principale garde la tête ; les mains (écriture de code) descendent d'un cran de modèle.
- **Résultat empirique (non chiffré, honnête)** : « *I'm getting a ton of work done and my Fable allowance is shrinking less quickly than before.* » → productivité maintenue, consommation Fable ralentie.
- **Lien avec ce dépôt** : le mécanisme décrit (fichier mémoire `type: feedback` sous `~/.claude/projects/.../memory/`) est **exactement** le système de mémoire persistante utilisé ici. La note de Willison est une démonstration publique du même pattern « *delegate coding to subagents with model override* » — directement transposable à notre workflow.
- **À relier** : même famille que la fiche *Compounding Knowledge Lifecycle* (mémoire d'agent qui capture le *feedback* pour le rejouer) et que les conseils *loop engineering* / orchestration de subagents.

## RésuméDe400mots

Dans cette note brève publiée le 3 juillet 2026, Simon Willison relaie deux conseils convergents sur la façon d'exploiter les agents de codage, entendus lors d'un *Fireside Chat* qu'il a animé à l'AIE avec **Cat Wu** et **Thariq Shihipar**, de l'équipe Claude Code.

Le premier principe : **laisser le modèle exercer son propre jugement plutôt que de lui dicter comment travailler**. Cela vaut pour **Fable** et, dans une certaine mesure, pour **Opus**. L'exemple donné concerne les tests. On *peut* écrire une règle explicite — « n'utilise les tests automatisés que pour les fonctionnalités importantes, ne mets pas à jour ni ne lance de tests pour de petits changements de texte ou de design » — mais il est **préférable de demander simplement à Fable d'utiliser son jugement** pour décider quand écrire des tests. Le discernement contextuel du modèle se révèle plus robuste que la règle codée en dur.

Le second conseil, transmis par **Jesse Vincent**, applique la même philosophie à l'**économie des tokens**. Le contexte est daté : les prix des tokens Fable vont augmenter dans quelques jours. Pour ne pas brûler cette ressource précieuse, l'idée est de **demander à Fable de déléguer les tâches plus petites à des modèles moins puissants**, en le laissant juger lui-même lequel convient.

Willison applique aussitôt le conseil et documente l'expérience de bout en bout. Il fournit le **prompt exact** envoyé à Claude Code : « *For all coding tasks use your judgement to decide an appropriate lower power model and run that in a subagent* ». En réponse, Claude Code a **spontanément écrit un fichier mémoire** (`~/.claude/projects/<projet>/memory/delegate-coding-to-subagents.md`, `type: feedback`). Ce fichier ne se contente pas d'enregistrer la consigne : il en **codifie l'application** — *sonnet* pour l'implémentation substantielle, *haiku* pour les éditions triviales ou mécaniques — tout en réservant au **modèle principal** ce qui exige du jugement : design, audit, synthèse de données, review. La justification tient en une phrase : le travail d'implémentation a rarement besoin du modèle haut de gamme, tandis que jugement, review et synthèse restent dans la boucle principale.

Le verdict est empirique et mesuré : « *So far it seems to be working well. I'm getting a ton of work done and my Fable allowance is shrinking less quickly than before.* » La note illustre ainsi, sur un cas reproductible, une double bonne pratique : **ne pas sur-spécifier** les agents capables de jugement, et **orchestrer plusieurs niveaux de modèles** via des subagents pour préserver les tokens premium.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Cat Wu | PERSONNE | recommande | laisser Fable et Opus exercer leur propre jugement plutôt que dicter des règles | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Thariq Shihipar | PERSONNE | travaille_chez | équipe Claude Code | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Cat Wu | PERSONNE | travaille_chez | équipe Claude Code | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Jesse Vincent | PERSONNE | recommande | déléguer les petites tâches à des modèles moins puissants pour économiser les tokens Fable | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Fable | TECHNOLOGIE | permet | décision contextuelle sur l'écriture des tests (jugement du modèle) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Simon Willison | PERSONNE | utilise | délégation des tâches de code à des subagents à modèle moins puissant | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Délégation à des subagents | METHODOLOGIE | utilise | model override (Sonnet, Haiku) | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Délégation à des subagents | METHODOLOGIE | réduit | consommation de tokens Fable | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | a_créé | fichier mémoire delegate-coding-to-subagents.md | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Fichier mémoire | DOCUMENT | affirme_que | "implementation work rarely needs the top-tier model; judgment, review, and synthesis stay with the main loop" | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| Sonnet | TECHNOLOGIE | s_applique_à | implémentation substantielle de code | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Haiku | TECHNOLOGIE | s_applique_à | éditions triviales ou mécaniques | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Jugement du modèle | CONCEPT | s_oppose_à | règles explicites codées en dur | CONCEPT | 0.88 | ATEMPOREL | inféré |
| Simon Willison | PERSONNE | affirme_que | "I'm getting a ton of work done and my Fable allowance is shrinking less quickly than before" | CITATION | 0.9 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Fable | TECHNOLOGIE | catégorie | Modèle premium de codage (Claude Code) capable de jugement autonome | AJOUT |
| Opus | TECHNOLOGIE | catégorie | Modèle Claude apte, dans une certaine mesure, au jugement autonome | AJOUT |
| Délégation à des subagents | METHODOLOGIE | définition | Confier l'écriture de code à un subagent à modèle moins puissant, le modèle principal gardant jugement/review/synthèse | AJOUT |
| Fichier mémoire | DOCUMENT | chemin | ~/.claude/projects/<projet>/memory/delegate-coding-to-subagents.md (type: feedback) | AJOUT |
| Jugement du modèle | CONCEPT | principe | Laisser le modèle arbitrer le "comment" plutôt que lui dicter des règles rigides | AJOUT |
| Cat Wu | PERSONNE | rôle | Équipe Claude Code (intervenante Fireside Chat AIE) | AJOUT |
| Thariq Shihipar | PERSONNE | rôle | Équipe Claude Code (intervenant Fireside Chat AIE) | AJOUT |
| Jesse Vincent | PERSONNE | rôle | Praticien ayant transmis le conseil de délégation multi-modèles | AJOUT |
| Sonnet | TECHNOLOGIE | usage | Implémentation substantielle de code (model override) | AJOUT |
| Haiku | TECHNOLOGIE | usage | Éditions triviales/mécaniques (model override) | AJOUT |
| Hausse de prix des tokens Fable | EVENEMENT | temporalité | Annoncée imminente (« few days we have left before the prices go up ») au 2026-07-03 | AJOUT |
