---
themes: [qualite-securite, architecture-construction, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-windev-golden-master-inverse-2026-10-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** (~7 000 signes hors schéma, deux sources notées), rattaché au guide SFEIR de la migration **WinDev**. Il décrit une méthode de non-régression, le **golden master inversé**, et la règle qui la fonde : *« aucun test dont le LLM a écrit les valeurs attendues »*. Trois apports. **(A)** L'inversion, reprise de **Hamadi Jabloun** (sfeir.dev, 20 septembre 2026) — *« le LLM génère les ENTRÉES. Le code legacy, lui seul, génère les SORTIES »* : le modèle propose des entrées aux frontières, l'application WinDev les rejoue, les sorties observées (erreurs comprises) forment le golden master. **(B)** Ce qu'on compare : écritures en base (facilité par une étape transitoire sur **PostgreSQL**), états imprimés, exports normalisés ; reproductibilité par neutralisation de l'indéterminisme ; **score de mutation** (PIT, mutmut) plutôt que taux de couverture. **(C)** La bascule : trafic réel aspiré, **shadow run** où seule la réponse WinDev fait foi, puis bascule derrière feature flag selon le motif **Strangler Fig**. Les écarts sont signalés par l'agent, jamais corrigés en silence. Fait suite, dans la même série, à l'article sur l'extraction des règles métier par prompt d'archéologie.

## Titre Article

Tests de non-régression d'une migration WinDev : la méthode du golden master inversé

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/windev-tests-non-regression-golden-master/

## Keywords

WinDev, migration legacy, tests de non-régression, golden master, golden master inversé, tests de caractérisation, valeurs attendues, LLM, frontières, Gherkin, HFSQL, PostgreSQL, états, exports, EDI, indéterminisme, score de mutation, PIT, mutmut, trafic réel, shadow run, shadow traffic, Strangler Fig, feature flag, écarts à arbitrer, DORA, Winfall

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé individuellement, publié sur sfeir.com.

## Ton

Profil : guide méthodologique d'une ESN, registre prescriptif à la première personne du pluriel, en français, public de responsables de migration et d'équipes de test. Le texte s'ouvre sur un énoncé net (« une application migrée qui tourne ne prouve rien ») et pose une règle présentée sans exception, en gras. La construction est celle d'un anti-pattern suivi de son correctif : d'abord le piège (le modèle fige sa propre interprétation du code), puis le circuit en quatre temps, illustré par un schéma où l'anti-pattern est barré. Les sections suivantes sont techniques et concrètes (tables, états, exports, horloge paramétrable, commit isolé). L'autorité vient d'un billet interne daté de sfeir.dev et d'une citation d'un acteur tiers (Winfall) présentée comme convergence de pratique. La FAQ traite les objections opérationnelles (copie de production, bug historique, application desktop, volume de cas). Clôture sur la place du golden master dans la méthode SFEIR en six étapes.

## Pense-betes

- **Le piège** : demander au LLM d'écrire des tests de caractérisation, c'est le laisser écrire les **valeurs attendues** depuis sa lecture du code et des commentaires, jamais depuis l'exécution. Il fige son interprétation ; corriger le code pour faire passer le test revient à modifier une règle en production.
- **Règle** : *« aucun test dont le LLM a écrit les valeurs attendues »*.
- **Circuit en quatre temps** : (1) le LLM propose des entrées maximisant la couverture des branches (code + Gherkin issus de l'extraction des règles) ; (2) rejeu sur WinDev en environnement de test ; (3) sorties observées, erreurs comprises = **golden master** ; (4) la nouvelle application est jugée contre lui seul.
- **Que comparer** :
  - écritures en base (lignes créées, modifiées, supprimées) ; l'étape WinDev-sur-PostgreSQL met les deux applications sur le même moteur ;
  - états (factures, bons) : extraction texte et montants, ou comparaison visuelle avec tolérance ;
  - exports (comptables, EDI, CSV) : octet par octet après normalisation des horodatages et identifiants.
- **Reproductibilité** : neutraliser date, aléatoire, compteurs, réseau (horloge paramétrable, numérotation injectée) ; le commit qui rend testable ne touche à aucune règle.
- **Mesure** : le **score de mutation** (PIT, mutmut) mesure le filet ; la couverture ne dit rien des assertions.
- **Vraie donnée** : enregistrer les couples entrée/sortie de production sur une période incluant au moins une **clôture de mois**.
- **Shadow run** : deux implémentations en parallèle, seule WinDev fait foi, divergences journalisées une à une ; un bug ancien corrigé = décision produit portée par le métier. Divergence nulle → bascule derrière feature flag, ancien module gardé pour retour arrière (**Strangler Fig**).
- **Consigne à l'agent** : un cas jugé erroné est signalé dans une liste d'écarts à arbitrer, jamais corrigé.

## RésuméDe400mots

L'article de SFEIR décrit la méthode de non-régression que le cabinet applique aux migrations d'applications WinDev. Il part d'un constat : une application migrée qui s'ouvre et enregistre une commande ne prouve rien. La preuve attendue est qu'elle produit les mêmes écritures, documents et exports que l'application d'origine, bugs compris, sauf décision explicite du métier.

Les applications WinDev anciennes ont rarement des tests ; on génère donc des tests de caractérisation qui figent le comportement actuel. L'article identifie le piège courant : laisser le modèle de langage écrire ces tests, et donc les valeurs attendues, à partir de sa lecture du code plutôt que de son exécution. Le modèle fige alors son interprétation, et la tentation de corriger le code pour faire passer le test revient à modifier une règle en production. La règle posée est sans exception : aucun test dont le LLM a écrit les valeurs attendues. Elle reprend une formule de Hamadi Jabloun publiée sur sfeir.dev : le LLM génère les entrées, le code legacy seul génère les sorties.

Le circuit inversé compte quatre temps. Le modèle propose des jeux d'entrées aux frontières, à partir du code et des scénarios Gherkin issus de l'extraction des règles métier ; ces entrées sont rejouées sur l'application WinDev ; les sorties observées forment le golden master ; la nouvelle application est jugée contre lui seul.

L'article détaille ce qu'on compare : l'état des tables après chaque scénario, facilité par une étape où WinDev tourne déjà sur PostgreSQL ; les états imprimés, par extraction ou comparaison visuelle ; les exports, octet par octet après normalisation. Le golden master doit être reproductible, ce qui impose de neutraliser l'heure, l'aléatoire, les compteurs et le réseau dans un commit qui ne touche à aucune règle. La qualité du filet se mesure par le score de mutation, avec des outils comme PIT ou mutmut, et non par la couverture.

Le meilleur golden master reste le trafic réel enregistré sur une période représentative, incluant une clôture de mois. Avant bascule, les deux implémentations tournent en parallèle en shadow run ; seule la réponse WinDev fait foi et chaque divergence est analysée. Quand le taux de divergence tombe à zéro, le module bascule derrière un feature flag selon le motif Strangler Fig, l'ancien restant disponible. L'agent qui écrit le code cible doit signaler, et non corriger, tout cas qui lui semble faux. L'article cite Winfall comme acteur appliquant le même principe.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Tests de non-régression d'une migration WinDev | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| golden master inversé | METHODOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | est_variante_de | golden master | METHODOLOGIE | 0.9 | ATEMPOREL | inféré |
| golden master inversé | METHODOLOGIE | est_basé_sur | Du Legacy à l'état de l'art | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Hamadi Jabloun | PERSONNE | affirme_que | le LLM génère les ENTRÉES, le code legacy lui seul génère les SORTIES | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | aucun test dont le LLM a écrit les valeurs attendues | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | utilise | tests de caractérisation | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | utilise | score de mutation | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| score de mutation | CONCEPT | utilise | PIT | TECHNOLOGIE | 0.82 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | utilise | shadow run | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| shadow run | METHODOLOGIE | permet | Strangler Fig | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| golden master inversé | METHODOLOGIE | utilise | PostgreSQL | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un taux de couverture élevé ne dit rien de la qualité des assertions | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | que l'agent signale les cas jugés erronés dans une liste d'écarts au lieu de les corriger | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Winfall | ORGANISATION | soutient | golden master inversé | METHODOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| golden master inversé | METHODOLOGIE | définition | Le LLM propose les entrées, l'application legacy produit seule les sorties de référence | AJOUT |
| shadow run | METHODOLOGIE | définition | Exécution parallèle ancien/nouveau sur flux réel, seul l'ancien fait foi | AJOUT |
| score de mutation | CONCEPT | rôle | Mesure de la capacité d'une suite à détecter des erreurs injectées | AJOUT |
| tests de caractérisation | METHODOLOGIE | définition | Tests qui figent le comportement actuel, juste ou faux | AJOUT |
| Strangler Fig | METHODOLOGIE | rôle | Remplacement module par module avec retour arrière possible | AJOUT |
| Winfall | ORGANISATION | secteur | Prestataire de migration WinDev vers C# / .NET | AJOUT |
| Hamadi Jabloun | PERSONNE | rôle | Auteur sur sfeir.dev (SFEIR) | AJOUT |
