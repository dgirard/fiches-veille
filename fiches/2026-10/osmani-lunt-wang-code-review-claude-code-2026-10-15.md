---
themes: [agents-codage-ia-skills, qualite-securite]
source: "claude.dev Blog"
---
# osmani-lunt-wang-code-review-claude-code-2026-10-15

## Veille

Billet d'ingénierie d'**Addy Osmani**, **Morgan Westlee Lunt** et **Qing Wang** (équipe **Claude Code**, **Anthropic**) sur le blog *claude.dev*, publié le **15 octobre 2026** ; ~3 200 mots. Il décrit le flux de revue de code de l'équipe, où Claude écrit environ **90 %** du code de Claude Code. De juin à septembre, les PR fusionnées ont **plus que doublé** et la part revertée a baissé de **plus de 40 %** ; dans le monorepo d'Anthropic, les changements quotidiens sont passés de **~2 500** (mai) à **plus de 30 000** (septembre).

**(A)** Un objectif mesuré : *« the minimum amount of human review time that doesn't raise reverts or incidents »* — au plus un humain par PR, éventuellement l'auteur, avec le taux de revert et d'incident comme garde-fou. **(B)** Sept couches : vérification avant la PR, revue IA sur chaque PR (agents parallèles, vote de vérificateurs), revue de sécurité bloquante, CI bloquante, approbation humaine **graduée par le risque** (zéro, une ou deux personnes, palier fixé par un classifieur), merge queue et flags, rollback rapide. **(C)** Un relecteur amélioré en boucle : les incidents passés forment un **eval** rejoué chaque jour, le bruit se mesure à la réaction des auteurs, la convergence est imposée (plafond de trois rondes). **(D)** Les humains gardent cinq décisions, dont la direction et la propriété du résultat.

Prolonge [[osmani-agentic-verification-2026-10-14]] et [[laycock-thoughtworks-reviewing-all-this-code-2026-09-02]] sur le déplacement de la revue vers la preuve.

## Titre Article

How the Claude Code team does code review

## Date

2026-10-15

## URL

https://claude.dev/blog/solving-code-review-at-anthropic/

## Keywords

revue de code, code review, revue de code agentique, Claude Code, Code Review for Claude Code, REVIEW.md, CLAUDE.md, approbation graduée par le risque, classifieur de risque, revue de sécurité, merge queue, feature flags, déploiement progressif, rollback, eval d'incidents, bruit du relecteur, convergence de revue, plafond de rondes, temps humain, taux de revert, responsabilité de l'auteur, explicateur de code, vérification

## Authors

Addy Osmani, Morgan Westlee Lunt, Qing Wang — équipe Claude Code (Anthropic) ; blog *claude.dev*, catégorie Engineering.

## Ton

Retour d'expérience d'équipe, à la première personne du pluriel, sur un registre factuel et opérationnel. Le texte pose une question (comment relire au volume où les agents produisent), redéfinit le but de la revue, puis suit la vie d'un changement couche par couche, avant de décrire l'amélioration du relecteur, la place des humains et la diffusion du contexte. Il s'appuie sur des chiffres internes (volumes, taux de revert, part de PR commentées, rondes de revue) et sur cinq schémas. Il signale ses limites : pas encore de *circuit breakers* qui durcissent l'approbation quand les indicateurs bougent, pas de processus formel de partage du contexte, une PR passée par plus de cinquante rondes. Il se conclut par une liste d'adoption par étape et un appel aux retours d'équipes qui laissent des agents ouvrir des PR. Les produits Anthropic cités (Code Review, `/code-review`, `/security-review`, GitHub Action) sont présentés comme les briques disponibles.

## Pense-betes

- **But** : la question n'est plus *« un humain a-t-il lu le code ? »* mais *« qu'est-ce qui peut mal tourner, et quel contrôle doit l'attraper ? »*. La revue devient continue, comme un correcteur orthographique.
- **Métriques** : approbations humaines par PR (médiane, p95), commentaires humains, attente sur une personne ; garde-fou = taux de revert et d'incident.
- **Avant la PR** : Claude montre la sortie (tests, build, capture) ; un sous-agent relit le diff en contexte frais ; skills internes de chasse aux bugs, simplification, E2E. Boris Cherny estime que la vérification rend le résultat **2 à 3 fois** meilleur.
- **REVIEW.md** : écrit par les code owners ; court ; dit à quoi ressemble l'échec (docs : *« it lies »*, config : *« it misroutes »*), plafonne les nits, exige fichier et ligne comme preuve.
- **Revue IA** : PR avec commentaires substantiels **16 % → 54 %** ; niveaux Quick / Standard / Deep ; vote de vérificateurs ; tags Important / Nit / Pre-existing ; tout finding doit être traité.
- **Paliers** : bas (docs, flag) = zéro humain ; moyen = un ; haut = deux. Le changement fixe le palier, pas l'auteur ; une approbation d'agent ne remplace jamais un humain ; approbation liée à un commit.
- **Convergence** : 59 % des signalements répétés portaient sur du code présent dès la première passe. Après correctifs : passage en une ronde **65 % → 78 %**, cinq rondes ou plus **8,9 % → 1,5 %**, moyenne **2,08 → 1,32**.
- **« You land it, you own it »** : petits changements, tout réversible, la surface d'impact fixe l'exigence, sans blâme.
- **Contexte partagé** : un explicateur généré par Claude sur la tranche de code à modifier plutôt que la lecture de diffs triviaux.
- Voisin de [[houck-dx-what-are-code-reviews-for-2026-08-05]] et [[sfeir-code-review-anneau-contraintes-2026-07-30]].

## RésuméDe400mots

L'équipe Claude Code d'Anthropic décrit comment elle relit du code produit à environ 90 % par Claude. Le volume a explosé : dans le monorepo d'Anthropic, les changements quotidiens sont passés d'environ 2 500 en mai à plus de 30 000 en septembre, et la relecture manuelle ligne à ligne n'est plus tenable. De juin à septembre, les PR fusionnées sur Claude Code ont plus que doublé tandis que la part revertée baissait de plus de 40 %.

La revue a deux fonctions : trouver les défauts et diffuser la connaissance du code. Pour la première, l'équipe remplace la question « un humain a-t-il lu ? » par « quel contrôle doit attraper ce qui peut mal tourner ? ». L'objectif : la plupart des PR fusionnent avec au plus un humain, sans hausse des reverts ni des incidents, qui servent de garde-fou.

Un changement traverse plusieurs couches. Avant la PR, Claude exécute tests, build et linter et montre la sortie, puis un sous-agent relit le diff en contexte frais. CLAUDE.md décrit le projet ; REVIEW.md, écrit par les propriétaires du code, dit au relecteur ce qui compte. Sur chaque PR, plusieurs agents cherchent des bugs en parallèle, d'autres votent sur chaque finding, et seuls les findings retenus sont publiés, triés par gravité. Une revue de sécurité distincte et la CI bloquent la fusion tant qu'un point reste ouvert. Un classifieur fixe le niveau de risque, donc le nombre d'approbateurs humains (zéro, un ou deux) ; certains chemins exigent toujours une personne, et l'approbation d'un agent ne compte jamais comme celle d'un humain. Merge queue, feature flags, usage interne d'abord, canal latest avant stable et rollback rapide complètent le dispositif.

Le relecteur s'améliore en boucle. Les PR ayant causé des incidents, confirmées par des experts, forment un eval rejoué chaque jour. Le bruit se mesure à la réaction des auteurs, car un agent corrige chaque nit et relance une ronde. Une PR a enchaîné plus de cinquante rondes en une nuit ; l'équipe a plafonné les rondes à trois, limité la re-revue au nouveau diff et supprimé les répétitions, ce qui a fait passer la moyenne de 2,08 à 1,32 rondes.

Les humains gardent cinq décisions : faut-il le construire, le code risqué, l'architecture, la lecture des preuves et la responsabilité du résultat. Pour comprendre le code, on demande à Claude un explicateur de la tranche concernée. La norme « you land it, you own it » repose sur des changements petits et réversibles. L'article finit par une liste d'adoption par étape.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Addy Osmani | PERSONNE | publie | article How the Claude Code team does code review | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Morgan Westlee Lunt | PERSONNE | publie | article How the Claude Code team does code review | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Qing Wang | PERSONNE | publie | article How the Claude Code team does code review | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | mesure | changements quotidiens du monorepo : ~2 500 en mai → plus de 30 000 en septembre 2026 | MESURE | 0.95 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | mesure | PR fusionnées ×2+ et part revertée −40 %+ de juin à septembre 2026 | MESURE | 0.95 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | « un humain a-t-il lu le code ? » est un proxy imprécis de « quel contrôle doit attraper ce qui peut mal tourner ? » | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| revue de code agentique | METHODOLOGIE | réduit | temps de revue humain | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| revue de code agentique | METHODOLOGIE | utilise | Code Review for Claude Code | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| revue de code agentique | METHODOLOGIE | utilise | REVIEW.md | DOCUMENT | 0.92 | DYNAMIQUE | déclaré_article |
| revue de code agentique | METHODOLOGIE | utilise | CLAUDE.md | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| revue de code agentique | METHODOLOGIE | utilise | approbation graduée par le risque | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| revue de code agentique | METHODOLOGIE | utilise | /security-review | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Code Review for Claude Code | TECHNOLOGIE | mesure | PR internes avec commentaires substantiels : 16 % → 54 % | MESURE | 0.93 | STATIQUE | déclaré_article |
| approbation graduée par le risque | METHODOLOGIE | utilise | classifieur de risque | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| eval d'incidents | METHODOLOGIE | améliore | Code Review for Claude Code | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| plafond de rondes de revue | METHODOLOGIE | réduit | itérations revue-correction | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| plafond de rondes de revue | METHODOLOGIE | mesure | rondes moyennes avant passage : 2,08 → 1,32 ; cinq rondes ou plus : 8,9 % → 1,5 % | MESURE | 0.93 | STATIQUE | déclaré_article |
| Boris Cherny | PERSONNE | affirme_que | donner à Claude un moyen de vérifier son travail rend le résultat 2 à 3 fois meilleur | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | ne jamais laisser l'approbation d'un bot remplacer celle d'un humain requis | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | recommande | mesurer le temps humain avec taux de revert et d'incident comme garde-fou | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| You land it, you own it | CONCEPT | s_applique_à | Claude Code | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | merge queue | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | feature flags | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| article How the Claude Code team does code review | DOCUMENT | référence | Boris Cherny | PERSONNE | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Addy Osmani | PERSONNE | rôle | Co-auteur, équipe Claude Code (Anthropic) | AJOUT |
| Morgan Westlee Lunt | PERSONNE | rôle | Co-auteur, équipe Claude Code (Anthropic) | AJOUT |
| Qing Wang | PERSONNE | rôle | Co-auteur, équipe Claude Code (Anthropic) | AJOUT |
| article How the Claude Code team does code review | DOCUMENT | catégorie | Billet Engineering du blog claude.dev, 15 octobre 2026 | AJOUT |
| Code Review for Claude Code | TECHNOLOGIE | catégorie | Revue de PR multi-agents avec vote de vérificateurs, niveaux Quick/Standard/Deep, disponible sur Team et Enterprise | AJOUT |
| REVIEW.md | DOCUMENT | définition | Fichier écrit par les code owners qui dit au relecteur IA ce qui compte dans leur partie du code | AJOUT |
| approbation graduée par le risque | METHODOLOGIE | définition | Nombre d'approbateurs humains (0, 1 ou 2) fixé par un classifieur selon le changement, pas selon l'auteur | AJOUT |
| eval d'incidents | METHODOLOGIE | définition | Jeu de PR passées ayant causé incidents ou reverts, confirmées par des experts, rejoué chaque jour contre le relecteur | AJOUT |
| plafond de rondes de revue | METHODOLOGIE | définition | Trois rondes maximum, puis re-revue limitée au nouveau diff, sans répétition des findings | AJOUT |
| Claude Code | TECHNOLOGIE | contexte | Agent de codage dont Claude écrit ~90 % du code ; dépôts CLI, desktop, web et mobile | AJOUT |
| You land it, you own it | CONCEPT | définition | Norme d'équipe : l'auteur d'un changement petit ou moyen corrige ce qui casse, sans blâme | AJOUT |
| revue de code agentique | METHODOLOGIE | définition | Revue en couches où les machines lisent l'essentiel et l'attention humaine va au risque | AJOUT |
