---
themes: [agents-codage-ia-skills, qualite-securite]
source: "Substack (Elevate)"
---
# osmani-agentic-verification-2026-10-14

## Veille

Billet d'**Addy Osmani** sur son Substack *Elevate*, publié le **14 octobre 2026** ; ~1 900 mots. Thèse : avec les modèles actuels, le goulot n'est plus l'écriture du code mais la **vérification** de sa justesse ; le travail humain passe de *« review every line »* à *« build loops the agent can run itself »*.

**(A)** La boucle auto-vérifiante : l'agent écrit, lance le contrôle, lit la sortie et recommence avant qu'un humain ne voie quoi que ce soit ; *« I would always prefer a much better feedback loop to a slightly better model »*. Les tests deviennent la manière dont l'agent *« senses the world and knows when it's done »*. **(B)** Trois familles de contrôles : les **tests E2E** comme oracle (difficiles à tromper, ils définissent « fini ») ; les **tests de propriétés** (fast-check, Hypothesis, proptest), qui disent ce qui ne doit jamais arriver (aller-retour, invariants, idempotence, équivalence) ; les **tests différentiels**, où l'ancien système sert d'oracle lors d'une migration, avec normalisation et liste des changements approuvés. **(C)** Une boucle **rapide et déterministe** : sinon l'agent apprend à relancer plutôt qu'à corriger. **(D)** *Écrire le contrôle avant le code.*

Deux encadrés citent **Lauren (@poteto)** (donner à l'agent « des mains et des yeux » via une skill/CLI et une *feature map*) et **Boris Cherny** (modèles Lean/TLA+ pour la concurrence). Le billet n'apporte pas de mesure ; les gains rapportés sur les migrations viennent d'équipes non nommées.

Prolonge [[laycock-thoughtworks-reviewing-all-this-code-2026-09-02]] sur le déplacement de la revue vers la preuve.

## Titre Article

Agentic Verification — The bottleneck has moved from writing code to knowing it's correct.

## Date

2026-10-14

## URL

https://addyo.substack.com/p/agentic-verification

## Keywords

vérification agentique, boucle de rétroaction, agent auto-vérifiant, tests de bout en bout, E2E, tests basés sur les propriétés, property-based testing, tests différentiels, oracle, migration, invariants, idempotence, déterminisme, tests instables, flaky tests, feature map, méthodes formelles, TLA+, Lean, critère de succès, revue de preuves

## Authors

Addy Osmani — ingénieur (Anthropic, cf. fiches antérieures) ; billet sur son Substack *Elevate*.

## Ton

Profil : guide de pratique adressé aux ingénieurs qui travaillent avec des agents de codage, sur un ton assuré et didactique. Le texte part d'une thèse (la vérification est le goulot), redéfinit le rôle des tests, puis déroule trois familles de contrôles, chacune avec ses avantages, ses limites et des conseils de démarrage, avant une liste « à quoi ressemble le bon » et une consigne finale. Les encadrés « Note » ouvrent sur des pratiques voisines (feature map, méthodes formelles, agents relecteurs). L'argument s'appuie sur l'expérience de l'auteur et sur des retours d'équipes non nommées, sans chiffre ni étude. Les commentaires prolongent le propos : IronBee (vérifier aussi l'API derrière l'UI) et un lecteur qui propose de rendre les critères d'acceptation inaccessibles à l'agent constructeur.

## Pense-betes

- **Thèse** : le goulot passe de l'écriture à la vérification ; l'humain définit le succès et relit des preuves, pas des diffs.
- **Boucle** : écrire → contrôler → lire → recommencer, avant tout regard humain ; mieux vaut une bien meilleure boucle qu'un modèle un peu meilleur.
- **Capitaliser le goût** : chaque erreur de l'agent devient config partagée, hook ou test.
- **E2E** : oracle fidèle à l'utilisateur ; doit dire *quoi* a échoué (captures, traces) ; peu nombreux et à forte valeur, car lents et instables.
- **Propriétés** : *« Example tests say what should happen; properties say what must not »* ; démarrer sur une fonction pure, écrire la propriété en anglais d'abord, garder le cas minimisé en régression.
- **Différentiel** : ancien système = oracle ; entrées aléatoires ou trafic réel rejoué ; normaliser l'insignifiant ; liste de changements approuvés motivés.
- **Boucle saine** : sous-seconde pour la boucle cœur, aléa seedé, horloge figée, réseau contrôlé ; test instable sorti de la suite ; sortie courte ; E2E et diff avant intégration.
- **Habitudes annexes** : reformuler les critères de succès avant de coder, agent relecteur en contexte frais, examiner les tests générés.
- Voisin de [[monperrus-end-of-code-review-agents-supersede-2026-06-11]] et [[osmani-three-joys-engineering-agents-2026-10-09]].

## RésuméDe400mots

Addy Osmani part d'un constat : donner à un agent un moyen de vérifier son travail améliore fortement la qualité de ce qu'il produit. Ce qui rendait le « bon code » coûteux (tests, benchmarks, spécifications, vrais parcours de bout en bout) peut désormais être demandé à l'agent. Le travail humain se déplace donc de la relecture ligne à ligne vers la construction de boucles que l'agent exécute seul, et le goût se capitalise : chaque erreur devient une configuration partagée, un hook ou un test. Un humain reste responsable de ce qui est livré, mais il examine des preuves plutôt que des diffs.

Selon lui, les modèles sont assez bons pour que le goulot soit la vérification. Un agent qui ne peut pas se contrôler devine, et la correction passe par un aller-retour humain lent, coûteux et impossible à étendre. Un agent qui se teste écrit, contrôle, lit le résultat et recommence avant toute intervention humaine. Les tests changent de rôle : ils sont la manière dont l'agent perçoit le monde et sait qu'il a fini.

Les tests de bout en bout sont l'oracle à privilégier : ils décrivent ce que fait l'utilisateur et sont difficiles à tromper, là où un test unitaire à base de mocks peut partager le malentendu de l'agent. Ils doivent indiquer l'étape en échec, et transforment une consigne vague en cible. Lents et instables, ils doivent rester peu nombreux.

Les tests de propriétés énoncent ce qui ne doit jamais arriver ; des outils comme fast-check, Hypothesis ou proptest génèrent des milliers d'entrées et réduisent l'échec au cas minimal. Propriétés courantes : aller-retour, invariants, idempotence, équivalence avec une version simple. Ils empêchent l'agent de choisir des exemples qui confirment sa propre logique et servent de spécification.

Pour une réécriture, les tests différentiels font de l'ancien système l'oracle : mêmes entrées, aléatoires ou issues du trafic réel, comparaison des sorties, normalisation de l'insignifiant et liste motivée des changements voulus, jusqu'à pouvoir retirer l'ancien système.

La boucle doit être rapide et déterministe : un agent face à des tests lents ou instables apprend à relancer plutôt qu'à corriger, ou espace ses exécutions et perd la trace des causes. Osmani recommande une boucle cœur sous la seconde, un aléa contrôlé, l'exclusion immédiate des tests instables, des sorties concises et les tests lourds avant intégration. Il conclut : écrire le contrôle avant le code.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Addy Osmani | PERSONNE | publie | article Agentic Verification | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Addy Osmani | PERSONNE | affirme_que | le goulot des agents de codage est la vérification, non l'écriture du code | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| Addy Osmani | PERSONNE | affirme_que | une bien meilleure boucle de rétroaction vaut mieux qu'un modèle un peu meilleur | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Agentic verification | METHODOLOGIE | améliore | Agents de codage | TECHNOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| Agentic verification | METHODOLOGIE | utilise | Tests E2E | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Agentic verification | METHODOLOGIE | utilise | Property-based testing | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Agentic verification | METHODOLOGIE | utilise | Differential testing | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Property-based testing | METHODOLOGIE | utilise | fast-check | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Property-based testing | METHODOLOGIE | utilise | Hypothesis | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Property-based testing | METHODOLOGIE | utilise | proptest | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Differential testing | METHODOLOGIE | s_applique_à | migration logicielle | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Tests instables | CONCEPT | réduit | Agentic verification | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| Addy Osmani | PERSONNE | recommande | écrire le contrôle avant le code | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Addy Osmani | PERSONNE | recommande | une boucle de tests rapide et déterministe, sous la seconde pour la boucle cœur | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Addy Osmani | PERSONNE | référence | Lauren (@poteto) | PERSONNE | 0.85 | STATIQUE | déclaré_article |
| Lauren (@poteto) | PERSONNE | recommande | Feature map | CONCEPT | 0.85 | STATIQUE | déclaré_article |
| Boris Cherny | PERSONNE | utilise | TLA+ | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | utilise | Lean | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Boris Cherny | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.85 | STATIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Addy Osmani | PERSONNE | rôle | Ingénieur, auteur du Substack Elevate | AJOUT |
| article Agentic Verification | DOCUMENT | catégorie | Billet Substack (Elevate), 14 octobre 2026 | AJOUT |
| Agentic verification | METHODOLOGIE | définition | Équiper l'agent de contrôles qu'il exécute seul (E2E, propriétés, différentiel) dans une boucle rapide et déterministe | AJOUT |
| Tests E2E | METHODOLOGIE | définition | Tests simulant un parcours utilisateur réel, oracle de « fini » pour l'agent | AJOUT |
| Property-based testing | METHODOLOGIE | définition | Énoncer une règle et générer des milliers d'entrées pour la casser, avec réduction au cas minimal | AJOUT |
| Differential testing | METHODOLOGIE | définition | Comparer ancien et nouveau système sur les mêmes entrées ; l'ancien sert d'oracle | AJOUT |
| Feature map | CONCEPT | définition | Inventaire des fonctionnalités du point de vue utilisateur : accès, raccourcis, sélecteurs, résultats attendus, pièges | AJOUT |
| Tests instables | CONCEPT | définition | Tests non déterministes (flaky) qui apprennent à l'agent à relancer plutôt qu'à corriger | AJOUT |
| fast-check | TECHNOLOGIE | catégorie | Bibliothèque de tests de propriétés JS/TS | AJOUT |
| Hypothesis | TECHNOLOGIE | catégorie | Bibliothèque de tests de propriétés Python | AJOUT |
| proptest | TECHNOLOGIE | catégorie | Bibliothèque de tests de propriétés Rust | AJOUT |
| TLA+ | TECHNOLOGIE | catégorie | Langage de spécification formelle | AJOUT |
| Lean | TECHNOLOGIE | catégorie | Assistant de preuve | AJOUT |
| Lauren (@poteto) | PERSONNE | rôle | Personne citée pour la feature map et l'outillage « mains et yeux » | AJOUT |
