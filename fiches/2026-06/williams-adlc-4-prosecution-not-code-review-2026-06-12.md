# williams-adlc-4-prosecution-not-code-review-2026-06-12

## Veille

Quatrième volet ADLC : Williams reconfigure la revue de code en « prosecution » adversariale plutôt qu'évaluation collaborative. Charter les agents pour réfuter (« trouver ce qui est faux »), déployer des reviewers mono-lentille à contextes frais (correction, sécurité, conformité de contrat, alignement spec, qualité des tests), n'agir que sur des findings vérifiés (reproduits par un test rouge), et boucler jusqu'à deux passes consécutives à zéro finding. Mesurer la calibration en plantant des bugs connus, à la manière du mutation testing. Gate de sortie : zéro finding ouvert, deux passes sèches, tests verts, diff de tests vide.

## Titre Article

Prosecution, Not Code Review

## Date

2026-06-12

## URL

https://www.voodootikigod.com/adlc-4-prosecution-not-code-review

## Keywords

ADLC, prosecution, revue adversariale, réfutation vs évaluation, sycophancie, hallucination de findings, biais d'arrêt à quinze, reviewers mono-lentille, contextes frais, findings vérifiés, churn fantôme, loop-until-dry, calibration de revue, bugs plantés, recall par catégorie, faux positifs, gate de sortie, mutation testing

## Authors

Chris Williams (@voodootikigod)

## Ton

Profil : plaidoyer méthodologique (perspective praticien en anglais, registre argumentatif et tranchant), niveau technique élevé, public cible responsables qualité et ingénieurs construisant des stacks de revue agentiques. Le ton est celui de la requalification conceptuelle : la métaphore judiciaire (prosecution, charge de la preuve, findings vérifiés) structure tout le propos et déplace l'attendu d'une revue de « donner un avis » vers « démontrer une faille reproductible ». L'autorité repose sur le rattachement explicite aux modes de défaillance (F2 sycophancie, F4 hallucination, F6 biais du nombre de findings) et sur une exigence de mesure rarement appliquée — « presque toutes les équipes font confiance à leur stack de revue à l'aveugle ». Style structuré en principes numérotés, exemple concret de bug planté (un garde de truthiness qui saute la vérification), et clôture par un gate de sortie strict et vérifiable.

## Pense-betes

- **Reframe central** : la revue de code n'est pas une évaluation collaborative mais une **prosecution** adversariale. Les modèles, sollicités pour une revue classique, exhibent sycophancie, findings hallucinés et un point d'arrêt artificiel autour de quinze problèmes.
- **1. Réfutation plutôt qu'évaluation** : ne pas demander un feedback mais charter l'agent pour « trouver ce qui est faux » ou expliquer comment le projet échouerait. Cela redirige le biais de complaisance (F2) vers l'identification de failles plutôt que la recherche d'approbation.
- **2. Prosecution mono-lentille** : déployer des reviewers parallèles à contextes frais, chacun examinant **une seule** dimension — correction, sécurité, conformité de contrat, alignement avec la spec, ou qualité des tests. Répartir les préoccupations évite la saturation de contexte qui dilue le jugement.
- **3. Findings vérifiés uniquement** : avant que les builders n'agissent, exiger une vérification séparée — reproduire le bug par un test qui échoue, tracer les chemins de code, ou générer l'input déclencheur. Les « unverified findings » (F4) provoquent un churn réel pour des problèmes fantômes.
- **4. Loop-until-dry** : re-lancer la prosecution avec des contextes frais jusqu'à **deux passes consécutives** sans aucun finding vérifié. Cette approche par échantillonnage déjoue F6 (le prior d'entraînement qui s'arrête vers 10-20 findings indépendamment du nombre réel de défauts).
- **Mesure de calibration** : presque toutes les équipes font confiance à leur stack de revue à l'aveugle. La solution miroite le mutation testing : planter des bugs connus (mutations mécaniques + bugs subtils écrits par LLM), faire tourner toute la stack de prosecution, mesurer le recall par catégorie et le taux de faux positifs.
- **Exemple de bug planté** : ajouter un garde de truthiness qui saute la vérification quand un champ est absent — d'apparence défensive, mais introduisant une pourriture de sécurité.
- **Gate de sortie** : la revue passe quand (1) zéro finding vérifié ouvert, (2) deux passes sèches consécutives, (3) suites de tests vertes, (4) diff de tests **vide** (preuve que les builders n'ont pas modifié leurs propres gates).

## RésuméDe400mots

Le quatrième volet réinvente la revue de code pour le monde agentique. Le constat de départ : sollicités pour une revue classique, les modèles déçoivent de façon prévisible. La sycophancie (F2) les pousse à valider plutôt qu'à critiquer ; l'hallucination (F4) leur fait inventer des problèmes ; et un biais d'entraînement (F6) les fait s'arrêter autour de quinze findings, quelle que soit la densité réelle de défauts. Williams en tire un reframe : il ne faut pas demander une évaluation, mais conduire une prosecution — une accusation adversariale.

Quatre principes structurent cette prosecution. D'abord, la réfutation plutôt que l'évaluation : on ne demande pas un feedback, on charte l'agent pour « trouver ce qui est faux » ou expliquer comment le projet échouerait. Le biais de complaisance, ainsi retourné, travaille pour vous. Ensuite, la prosecution mono-lentille : plutôt qu'un seul reviewer omniscient, on déploie des agents parallèles à contextes frais, chacun dédié à une unique dimension — correction, sécurité, conformité de contrat, alignement avec la spec, qualité des tests. Distribuer les préoccupations évite la saturation de contexte qui dilue le jugement entre priorités concurrentes.

Troisième principe, les findings vérifiés uniquement. Avant qu'un builder n'agisse sur une critique, celle-ci doit être prouvée séparément : reproduire le bug via un test qui échoue, tracer le chemin de code, ou produire l'input déclencheur. Sans cela, les findings hallucinés génèrent un churn de code bien réel pour des problèmes qui n'existent pas. Quatrième principe, le loop-until-dry : on relance la prosecution avec des contextes frais jusqu'à deux passes consécutives sans aucun finding vérifié. Cet échantillonnage répété déjoue le point d'arrêt artificiel de F6.

Williams insiste ensuite sur un angle mort quasi universel : presque toutes les équipes font confiance à leur stack de revue à l'aveugle, sans jamais mesurer sa capacité réelle de détection. Sa solution miroite le mutation testing appliqué aux reviewers : planter des bugs connus — mutations mécaniques plus bugs subtils écrits par un LLM — faire tourner toute la stack de prosecution, puis mesurer le recall par catégorie et le taux de faux positifs. Exemple de bug planté : un garde de truthiness qui saute la vérification quand un champ est absent, d'apparence défensive mais introduisant une faille de sécurité.

Enfin, le gate de sortie est strict et entièrement vérifiable : zéro finding vérifié ouvert, deux passes sèches consécutives, suites de tests vertes, et diff de tests vide — cette dernière condition prouvant que les builders n'ont pas modifié leurs propres gates pour passer.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Chris Williams | PERSONNE | publie | Prosecution, Not Code Review | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| prosecution | METHODOLOGIE | s_oppose_à | revue de code collaborative | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| prosecution | METHODOLOGIE | réduit | sycophancie du reviewer | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| reviewers mono-lentille | METHODOLOGIE | réduit | saturation de contexte qui dilue le jugement | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| findings vérifiés | METHODOLOGIE | réduit | churn de code sur des problèmes hallucinés | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| loop-until-dry | METHODOLOGIE | réduit | biais d'arrêt autour de 10-20 findings | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| calibration de revue | METHODOLOGIE | s_inspire_de | mutation testing | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| calibration de revue | METHODOLOGIE | mesure | recall par catégorie et taux de faux positifs de la stack | MESURE | 0.88 | DYNAMIQUE | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | presque toutes les équipes font confiance à leur stack de revue à l'aveugle | AFFIRMATION | 0.89 | ATEMPOREL | déclaré_article |
| bugs plantés | METHODOLOGIE | permet | mesure de la capacité réelle de détection des reviewers | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| phase Prosecute | METHODOLOGIE | fait_partie_de | cycle agentique en huit phases | METHODOLOGIE | 0.90 | ATEMPOREL | inféré |
| gate de sortie de prosecution | CONCEPT | utilise | diff de tests vide comme preuve de non-altération | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| prosecution | METHODOLOGIE | définition | Revue de code conçue comme une accusation adversariale visant à réfuter, pas à évaluer | AJOUT |
| reviewers mono-lentille | METHODOLOGIE | dimensions | Correction, sécurité, conformité de contrat, alignement spec, qualité des tests | AJOUT |
| findings vérifiés | METHODOLOGIE | exigence | Reproduire le bug (test rouge, trace, input) avant toute action du builder | AJOUT |
| loop-until-dry | METHODOLOGIE | critère d'arrêt | Deux passes consécutives à zéro finding vérifié, contextes frais | AJOUT |
| calibration de revue | METHODOLOGIE | méthode | Planter des bugs connus, mesurer recall et faux positifs de la stack | AJOUT |
| gate de sortie de prosecution | CONCEPT | conditions | Zéro finding ouvert, deux passes sèches, tests verts, diff de tests vide | AJOUT |
