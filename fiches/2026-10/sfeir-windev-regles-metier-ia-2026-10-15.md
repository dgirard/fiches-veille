---
themes: [architecture-construction, agents-codage-ia-skills, transformation-adoption]
source: SFEIR
---
# sfeir-windev-regles-metier-ia-2026-10-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** (~8 000 signes hors schéma, quatre sources notées), rattaché au guide SFEIR de la migration **WinDev**. Il décrit une **rétro-documentation spec first** : extraire avec l'IA les règles de gestion enfouies dans le **WLangage** avant toute réécriture. Point de départ : la doctrine de **Hamadi Jabloun** (sfeir.dev, 20 septembre 2026) — *« L'IA ne doit pas commencer par écrire le nouveau code. Elle doit commencer par écrire la spécification de l'ancien. »* Cinq étapes. **(1)** Rendre le code lisible via le **mode texte** de WinDev (depuis la version 25, projets hors GDS), l'analyse HFSQL en SQL et le `companion.md` de WinDev 2026. **(2)** Un **prompt d'archéologie** à cinq sections (règles, **Gherkin**, valeurs en dur, incohérences, zones d'ombre), avec les marqueurs « HYPOTHÈSE : » et « NÉANT ». **(3)** Une **double exécution** dans deux sessions, utilisée comme détecteur d'hallucination. **(4)** Des **ADR rétroactifs**. **(5)** La validation des zones d'ombre avec le métier. L'article estime à **20 à 40 %** la part de code mort d'un monolithe mature. Il prolonge la ligne spec-driven de SFEIR sur le brownfield.

## Titre Article

Extraire les règles métier d'une application WinDev avec l'IA : la rétro-documentation spec first

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/windev-extraire-regles-metier-ia/

## Keywords

WinDev, WLangage, PC SOFT, HFSQL, migration legacy, modernisation, rétro-documentation, spec first, spec-driven development, brownfield, règles de gestion, prompt d'archéologie, Gherkin, critères d'acceptation, valeurs en dur, zones d'ombre, double exécution, hallucination, ADR rétroactifs, code mort, mode texte, GDS, companion.md, Claude Code, validation métier, référentiel versionné

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé individuellement, publié sur sfeir.com.

## Ton

Profil : guide méthodologique d'une ESN, à la première personne du pluriel (« nous demandons », « nous ne sautons jamais »), registre procédural en français, public de DSI et de responsables d'applications métier WinDev. Le texte avance par étapes numérotées, chacune assortie d'une consigne concrète et d'un artefact (prompt, exemple Gherkin, schéma de chaîne). L'autorité est empruntée à une source interne datée (le billet de Hamadi Jabloun sur sfeir.dev) et à la documentation officielle de PC SOFT pour les faits produit, avec une distinction marquée entre fait documenté et avis (« relève à notre avis du même cas »). L'exemple de la remise volume, avec un commentaire qui contredit le code, sert de fil pédagogique jusqu'à la validation métier. Le ton reste pragmatique : la FAQ répond aux objections pratiques (relecteur WinDev, confidentialité du code, durée, absence de mode texte) et l'article souligne la valeur du livrable même sans migration. Clôture sur la méthode SFEIR en six étapes menée avec Claude Code.

## Pense-betes

- **Doctrine** (Jabloun) : spécifier l'ancien avant d'écrire le nouveau. Le risque majeur d'une refonte est **fonctionnel** : perdre une règle codée en dur par un développeur parti.
- **Étape 1, rendre le code lisible** : projets WinDev en binaire ; **mode texte** depuis la v25 (hors GDS) pour le code et les caractéristiques principales des fenêtres, propriétés avancées restées binaires. Compléments : script SQL de l'analyse HFSQL, procédures globales, classes, constantes, et en v2026 le `companion.md` généré par `/init_project`.
- **Étape 2, prompt d'archéologie** (interdiction de proposer une amélioration) :
  1. règles de gestion, une par ligne, avec la ligne de code d'origine ;
  2. critères d'acceptation **Gherkin**, un scénario par branche, valeurs de frontière nommées ;
  3. valeurs en dur porteuses de sens (seuils, taux, dates pivots) ;
  4. incohérences code / noms / commentaires, sans trancher ;
  5. zones d'ombre et ce qu'il faudrait pour trancher.
  Marqueurs : « HYPOTHÈSE : » et « NÉANT ». Les sections 4 et 5 sont celles qui *« rentabilisent l'exercice »*.
- **Étape 3, double exécution** : même prompt, deux sessions ; règles communes = fiables, règles vues une fois = relecture humaine. Justification : les modèles faiblissent sur les langages rares (COBOL, RPG, ABAP, PL/I) ; WLangage traité de même.
- **Étape 4, ADR rétroactifs** pour toute structure surprenante (table dupliquée, fichier temporaire persistant).
- **Étape 5, validation métier** : exécuter l'application pour observer, puis poser la question écrite au métier ; la réponse devient une décision tracée.
- **Code mort** : **20 à 40 %** sur un monolithe mature ; classer actif / suspect / probablement mort avant de documenter.
- **Livrable** : référentiel versionné (règles, `.feature`, valeurs en dur, ADR, décisions), utile même sans migration ; les scénarios Gherkin alimentent ensuite le golden master inversé.

## RésuméDe400mots

L'article de SFEIR décrit comment extraire avec l'IA les règles métier d'une application WinDev, première étape d'une migration et selon l'article souvent la seule qui compte. Une application WinDev ancienne porte des règles de tarification, de contrôle et de calcul qui n'existent que dans son code WLangage, souvent écrit par un développeur parti. L'IA rend leur reconstitution abordable à condition de lui demander une spécification plutôt qu'une paraphrase.

Le principe vient d'un billet de Hamadi Jabloun publié sur sfeir.dev en septembre 2026 : l'IA doit d'abord écrire la spécification de l'ancien, pas le nouveau code. La démarche prolonge le spec-driven development appliqué à un dépôt existant.

La première étape rend le code lisible. Les projets WinDev sont stockés en binaire, mais depuis la version 25 un mode texte, réservé aux projets hors gestionnaire de sources GDS, exporte le code et les caractéristiques principales des fenêtres. On y ajoute le script SQL de l'analyse HFSQL, les procédures, classes et constantes, et en version 2026 le fichier de vue d'ensemble produit par le compagnon IA de l'éditeur.

La deuxième étape est un prompt d'archéologie qui exige cinq livrables : les règles de gestion avec leur ligne d'origine, des critères d'acceptation en Gherkin par branche d'exécution, les valeurs en dur porteuses de sens, les incohérences entre code et commentaires, et les zones d'ombre. Toute supposition est marquée « HYPOTHÈSE », toute section vide « NÉANT ». Un exemple montre une remise volume dont le commentaire annonce un seuil différent de celui du code.

La troisième étape exécute le même prompt dans deux sessions distinctes : seules les règles présentes dans les deux sorties sont tenues pour fiables, les autres partent en relecture humaine. L'article justifie cette précaution par la faiblesse des modèles sur les langages peu représentés, dont il range le WLangage. Viennent ensuite des ADR rétroactifs pour expliquer les structures surprenantes, puis la validation des zones d'ombre avec le métier, après observation de l'application en fonctionnement.

L'article recommande de supprimer le code mort avant de documenter, estimé à 20 à 40 % d'un monolithe mature. Le livrable est un référentiel versionné qui garde sa valeur même sans migration : il réduit la dépendance à une personne clé, accélère l'intégration, éclaire une négociation avec l'éditeur et devient la spécification de la future application. Une FAQ précise qu'un relecteur connaissant WinDev reste nécessaire et que la disponibilité du métier est en général le facteur limitant.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Extraire les règles métier d'une application WinDev avec l'IA | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| rétro-documentation spec first | METHODOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| rétro-documentation spec first | METHODOLOGIE | est_variante_de | spec-driven development | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| rétro-documentation spec first | METHODOLOGIE | est_basé_sur | Du Legacy à l'état de l'art | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Hamadi Jabloun | PERSONNE | affirme_que | l'IA doit commencer par écrire la spécification de l'ancien code, pas le nouveau code | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| rétro-documentation spec first | METHODOLOGIE | utilise | prompt d'archéologie | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| prompt d'archéologie | METHODOLOGIE | utilise | Gherkin | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| rétro-documentation spec first | METHODOLOGIE | utilise | double exécution | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| double exécution | METHODOLOGIE | réduit | hallucination | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| rétro-documentation spec first | METHODOLOGIE | utilise | ADR rétroactifs | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| mode texte WinDev | TECHNOLOGIE | fait_partie_de | WinDev | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| PC SOFT | ORGANISATION | a_créé | WinDev | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| WinDev | TECHNOLOGIE | utilise | WLangage | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | 20 à 40 % de code mort sur un monolithe mature | MESURE | 0.82 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | supprimer le code mort avant de documenter | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| rétro-documentation spec first | METHODOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| rétro-documentation spec first | METHODOLOGIE | définition | Extraction par l'IA des règles de gestion d'un existant en spécification versionnée, avant réécriture | AJOUT |
| prompt d'archéologie | METHODOLOGIE | structure | Cinq sections : règles, Gherkin, valeurs en dur, incohérences, zones d'ombre | AJOUT |
| double exécution | METHODOLOGIE | rôle | Même prompt dans deux sessions ; les règles non communes passent en relecture humaine | AJOUT |
| ADR rétroactifs | METHODOLOGIE | rôle | Expliquer après coup les décisions derrière les structures surprenantes du legacy | AJOUT |
| WinDev | TECHNOLOGIE | catégorie | AGL de PC SOFT, langage WLangage, base HFSQL | AJOUT |
| mode texte WinDev | TECHNOLOGIE | disponibilité | Depuis la version 25, projets hors GDS ; propriétés avancées restées binaires | AJOUT |
| Hamadi Jabloun | PERSONNE | rôle | Auteur sur sfeir.dev (SFEIR) | AJOUT |
| Du Legacy à l'état de l'art | DOCUMENT | publication | Billet de Hamadi Jabloun, sfeir.dev, 20 septembre 2026 | AJOUT |
