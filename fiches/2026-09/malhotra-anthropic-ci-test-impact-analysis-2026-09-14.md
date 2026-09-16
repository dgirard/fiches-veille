---
themes: [qualite-securite, agents-codage-ia-skills, architecture-construction]
source: "claude.com (Sachin Malhotra, Anthropic)"
---
# malhotra-anthropic-ci-test-impact-analysis-2026-09-14

## Veille

Billet d'ingénierie d'**Anthropic** publié le **14 septembre 2026** sur claude.com/blog (~1 400 mots, cinq sections), signé **Sachin Malhotra**. Il raconte la mise à l'échelle du service de **test impact analysis** — la sélection des tests à exécuter par changement — sous la pression du codage agentique. Les chiffres d'entrée et leur chaîne : les ingénieurs livrent en moyenne **8×** plus de code par trimestre qu'en 2021-2025, **Claude en écrit 80 %** et pèse aussi lourd dans la revue et l'approbation des PR ; le nombre de tests a été multiplié par **10** à effectifs quasi constants ; d'où **25× de jobs CI en six mois**. **(A)** L'architecture v0 tient en deux composants à garder synchronisés — un *listener* qui enregistre les résultats de chaque run, un *selector* qui décide quels tests tournent sur chaque PR — mais en **processus unique**, un historique tenu par test supposant un écrivain unique. **(B)** Le mode de défaillance est le retard du listener sur la file de PR : *« 20 minutes of listener lag can translate into tens of thousands of test updates not being applied »*, avec trois conséquences nommées — investigations inutiles, *flaky reds* qui bloquent les merges, test corrigé ou ajouté qui ne tourne pas. **(C)** Trois rustines dont la durée de vie s'effondre — **70 jours, 29 jours, moins d'un jour** : machine plus grosse, sharding par package, redémarrages quotidiens. Puis la refonte : un magasin de données **en mémoire**, des workers *listener* **sans état** donc scalables horizontalement, un journal agrégé toutes les quelques secondes. **Trois semaines pour un ingénieur ; un an plus tôt, un trimestre.** Prolonge par l'infrastructure les 80 % de [[clinton-anthropic-secure-ai-native-sdlc-2026-07-21]].

## Titre Article

Agentic coding is straining CI. Here's how we scaled test impact analysis at Anthropic

## Date

2026-09-14

## URL

https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic

## Keywords

intégration continue, CI, test impact analysis, sélection de tests, listener, selector, retard de listener, 25× de jobs CI en six mois, 80 % du code écrit par Claude, flaky reds, données de sélection périmées, processus unique, écrivain unique, sharding par package, scalabilité horizontale, workers sans état, magasin de données en mémoire, journal, saturation mémoire, refonte de service, planifier l'exponentielle, sur-ingénierie, v0 dimensionnée 10-20×, instrumentation, yeux et oreilles de Claude, Claude Tag, session longue, PR plus petites, charge en rafales

## Authors

Sachin Malhotra (ingénieur, Anthropic), sur le blog claude.com.

## Ton

**Profil** : retour d'expérience d'ingénierie à la première personne, en post-mortem assumé. Public : équipes plateforme, CI et outillage développeur qui verront arriver la même courbe. Anglais direct, schéma d'architecture et courbe avant/après à l'appui.

**Style** : le texte se construit sur **une suite de nombres qui décroît** — 70 jours, 29 jours, moins d'un jour — et cette suite *est* l'argument, bien plus que les techniques employées. L'auteur les déclasse d'ailleurs lui-même d'entrée : acheter une machine plus grosse, paralléliser, redémarrer le service *« (yeah, this one still works surprisingly well) »* sont *« common and not the insights to take from this article »*. La leçon est déplacée des moyens vers le **rythme** : chaque technique achète une fraction du temps qu'elle achetait il y a un an, tandis que la refonte complète coûte, elle aussi, une fraction de ce qu'elle coûtait. Deux captures de conversation illustrent le récit, honnêtement étiquetées — l'une *« recreated, based on real events »*, l'autre verbatim avec rédactions.

**Position épistémique** : entièrement *first-party* et non auditable — l'entreprise mesure son propre outillage avec ses propres compteurs, et les chiffres les plus repris (25×, 8×, 80 %) sont déclaratifs. Deux aveux font la valeur du texte : la tendance était lisible mais *« ownership was murky — no one wanted to own another piece of infrastructure »* ; et Claude, branché en supervision continue, **plaidait la refonte depuis des mois** pendant que l'équipe *« settled on another patch »*. L'auteur borne aussi la portée de l'incident au lieu de la dramatiser : aucun code non testé n'est parti en production, la sélection travaillait seulement sur des données périmées.

## Pense-betes

- **La chaîne causale, pas seulement le chiffre.** 8× de code livré par ingénieur et par trimestre, dont **80 % écrit par Claude**, plus un rôle important de l'IA dans la revue et l'approbation des PR ; **×10 sur le nombre de tests** à effectifs quasi constants. Résultat : **×25 sur les jobs CI en six mois**. *« Writing code is no longer the constraint, and once PR review gets accelerated, CI starts feeling the pressure. »* Le goulot ne disparaît pas, il descend d'un cran — variante infrastructurelle du « col étroit de la vérification » de [[sfeir-code-review-anneau-contraintes-2026-07-30]].
- **L'argument propre aux agents**, le plus transposable du texte. Tout exécuter sur chaque changement marche jusqu'à un point, puis les gates deviennent longs, coûteux et **non fiables** — donc ignorés. Surtout : un humain sait écarter un échec de test qui ne le concerne pas, un agent non — il lui faut plus de contexte et de direction. Donné un jeu de tests **valides et pertinents**, il s'auto-vérifie et itère seul. La sélection de tests cesse d'être une optimisation de coût pour devenir une **condition de l'autonomie**.
- **L'architecture v0 et son péché originel** : tenir un historique **par test** imposait un écrivain unique, donc un processus unique, donc **aucun sharding horizontal possible**. L'état était dans le processus.
- **La physique du retard** : 20 minutes de lag = des dizaines de milliers de mises à jour non appliquées. Trois conséquences distinctes — un mauvais merge fait échouer un test pour tout le monde et déclenche des investigations inutiles ; une dépendance qui se met à flaker produit des *reds* qui bloquent les merges ; un test corrigé ou ajouté ne tourne pas tant que le listener n'a pas rattrapé, au risque d'une régression.
- **Les trois rustines et leur demi-vie** : (1) doubler les cœurs — **70 jours** ; (2) **sharder par package** — le listener n'avait pas besoin d'un écrivain unique global, mais d'un écrivain unique *par package*, et Claude a généré le code — **29 jours** ; (3) redémarrages quotidiens — **moins d'un jour**, avec seulement quatre bugs trouvés, un changement d'allocateur mémoire sans effet, et le refus assumé de profiler la mémoire d'un singleton déjà sous charge.
- **La supervision déléguée**, détail à retenir : une **session longue dans une version interne de Claude Tag** dédiée au service, qui alerte l'auteur dès que le listener dépasse **50 000 jobs de retard** et reprend la conversation là où elle s'était arrêtée. Pendant des mois, sans avoir à recharger le contexte des tentatives passées. Et *« Claude often argued for an overhaul, but we usually settled on another patch »*.
- **La refonte** : donner une base au service — un magasin de données **en mémoire**. N'importe quel worker *listener* traite n'importe quel résultat, l'ajoute à un **journal** et repart sans rien garder : sans état, donc scalable horizontalement. Un consommateur séparé agrège le journal en historique par test toutes les quelques secondes. Plus cher à exploiter, mais **beaucoup plus facile à scaler et à profiler** qu'un singleton fragile. Le réglage fin (taille du journal, nombre de workers) a été fait par Claude en grande partie seul.
- **L'économie de la décision a changé.** Trois semaines pour un ingénieur, contre environ un trimestre un an plus tôt. C'est le vrai basculement : les demi-mesures achètent de moins en moins de temps pendant que la refonte en coûte de moins en moins — *« much more sustainable now that writing code is no longer the bottleneck »*.
- **Les quatre règles qu'il en tire** : supposer l'architecture à **×25 de charge dans deux trimestres**, qu'on construise ou qu'on achète ; admettre que la sur-ingénierie recule comme faute — viser **10-20×** l'échelle perçue dès la v0 si le budget suit ; **instrumenter les services pour qu'ils servent d'yeux et d'oreilles à Claude**, au minimum l'invariant « autant de jobs CI entrants que sortants » ; sortir l'état du processus dès le départ, jamais de service critique en instance unique non mesurable.
- **La forme de la charge change, pas seulement son volume** : Claude préfère des PR **plus petites et plus granulaires** (argument de plus contre l'exécution de tous les tests sur chaque PR), le plancher d'activité monte parce que les agents poussent la nuit et le week-end, mais la charge **reste en rafales** puisque les humains pilotent et approuvent encore une part significative des PR.
- **Le pari final**, à vérifier dans douze mois : *« I anticipate horizontally scaled test selection architecture will become industry standard »* à mesure que les agents produisent à la fois plus de PR et plus de tests.

## RésuméDe400mots

Sachin Malhotra, ingénieur chez Anthropic, raconte comment l'entreprise a dû refondre son service de test impact analysis sous la pression du codage agentique. Le point de départ est une chaîne de chiffres : les ingénieurs livrent en moyenne huit fois plus de code par trimestre qu'entre 2021 et 2025, Claude en écrit 80 % et intervient largement dans la revue et l'approbation des PR, le nombre de tests a été multiplié par dix à effectifs quasi constants. Le produit de tout cela est une multiplication par vingt-cinq des jobs CI en six mois. Écrire du code n'est plus la contrainte ; une fois la revue accélérée, c'est la CI qui encaisse.

Le service repose sur deux composants déterministes qui doivent rester synchronisés : un listener, qui enregistre les résultats de chaque exécution, et un selector, qui lit cet historique pour décider quels tests s'exécutent sur chaque PR. Tenir un historique par test imposait un écrivain unique, donc un processus unique, donc l'impossibilité de sharder horizontalement. Le mode de défaillance est le retard du listener : vingt minutes suffisent à laisser des dizaines de milliers de mises à jour non appliquées, ce qui déclenche des investigations inutiles, laisse des tests instables bloquer des merges, et empêche un test corrigé ou ajouté de s'exécuter.

Trois correctifs se succèdent, dont la durée de vie s'effondre : doubler les cœurs tient soixante-dix jours ; sharder par package — le listener n'avait pas besoin d'un écrivain unique global mais d'un par package, et Claude en a écrit le code — tient vingt-neuf jours ; les redémarrages quotidiens tiennent moins d'un jour. Entre-temps, une session longue dans une version interne de Claude Tag surveille le service et alerte au-delà de cinquante mille jobs de retard ; elle plaide la refonte pendant des mois, l'équipe préfère la rustine.

La refonte donne au service un magasin de données en mémoire. Chaque worker listener traite n'importe quel résultat, l'ajoute à un journal et repart sans rien conserver : sans état, donc scalable horizontalement. Un consommateur séparé agrège le journal en historique par test toutes les quelques secondes. Plus coûteux à exploiter, mais scalable et profilable. Trois semaines pour un ingénieur, contre un trimestre un an plus tôt.

Les leçons tiennent en quatre règles : anticiper l'exponentielle et supposer une charge vingt-cinq fois supérieure dans deux trimestres, dimensionner la v0 pour dix à vingt fois l'échelle perçue, instrumenter les services pour qu'ils servent d'yeux et d'oreilles à Claude, et garder l'état hors du processus dès le départ.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Sachin Malhotra | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | mesure | 8× plus de code livré par ingénieur et par trimestre qu'en 2021-2025 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | mesure | Claude écrit 80 % du code livré et pèse largement dans la revue des PR | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | mesure | ×10 sur le nombre de tests et ×25 sur les jobs CI en six mois | MESURE | 0.94 | STATIQUE | déclaré_article |
| IA agentique | TECHNOLOGIE | observé_dans | déplacement du goulot de la génération de code vers l'intégration continue | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Test impact analysis | METHODOLOGIE | s_applique_à | Intégration continue | METHODOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| Test impact analysis | METHODOLOGIE | utilise | historique de résultats par test et pertinence par package | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Test impact analysis | METHODOLOGIE | permet | à un agent de s'auto-vérifier et d'itérer sur un jeu de tests pertinents | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| retard de listener | CONCEPT | réduit | fraîcheur des données de sélection des tests | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| retard de listener | CONCEPT | mesure | 20 minutes de retard = des dizaines de milliers de mises à jour non appliquées | MESURE | 0.92 | ATEMPOREL | déclaré_article |
| retard de listener | CONCEPT | observé_dans | investigations inutiles, flaky reds bloquant les merges, test corrigé qui ne tourne pas | AFFIRMATION | 0.91 | ATEMPOREL | déclaré_article |
| Claude Tag | TECHNOLOGIE | observé_dans | session longue de supervision du service, alerte au-delà de 50 000 jobs de retard | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Claude Tag | TECHNOLOGIE | recommande | refondre le service plutôt qu'enchaîner les rustines | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Magasin de données en mémoire | TECHNOLOGIE | permet | des workers listener sans état, donc scalables horizontalement | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| scalabilité horizontale | CONCEPT | résout | saturation mémoire du processus unique | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | mesure | refonte livrée en trois semaines par un ingénieur, contre environ un trimestre un an plus tôt | MESURE | 0.92 | STATIQUE | déclaré_article |
| Sachin Malhotra | PERSONNE | affirme_que | "Always plan for the exponential" | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Sachin Malhotra | PERSONNE | recommande | supposer une charge ×25 dans les deux trimestres, qu'on construise ou qu'on achète | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Sachin Malhotra | PERSONNE | recommande | dimensionner la v0 pour 10-20× l'échelle perçue si le budget le permet | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Sachin Malhotra | PERSONNE | recommande | instrumenter les services pour qu'ils servent d'yeux et d'oreilles à Claude | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Sachin Malhotra | PERSONNE | recommande | sortir l'état du processus dès le départ, jamais de service critique en instance unique | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Sachin Malhotra | PERSONNE | prédit | l'architecture de sélection de tests scalée horizontalement deviendra un standard de l'industrie | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| IA agentique | TECHNOLOGIE | observé_dans | PR plus petites et granulaires, activité nocturne et de week-end, charge restant en rafales | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Sachin Malhotra | PERSONNE | rôle | Ingénieur chez Anthropic ; auteur du retour d'expérience sur la mise à l'échelle de la CI | AJOUT |
| Anthropic | ORGANISATION | mesure interne | ×25 de jobs CI en six mois, ×10 de tests, 8× de code livré par ingénieur, Claude auteur de 80 % du code | AJOUT |
| Test impact analysis | METHODOLOGIE | définition | Service déterministe de sélection des tests par changement : un listener enregistre les résultats de chaque run, un selector lit l'historique et décide quels tests tournent sur chaque PR | AJOUT |
| Intégration continue | METHODOLOGIE | point de tension | Devient le goulot suivant une fois la génération et la revue de code accélérées par les agents | AJOUT |
| retard de listener | CONCEPT | effet | 20 minutes suffisent à laisser des dizaines de milliers de mises à jour hors du selector ; la sélection travaille alors sur des données périmées | AJOUT |
| Magasin de données en mémoire | TECHNOLOGIE | rôle | Sort l'état du processus : journal en append, agrégation par un consommateur séparé toutes les quelques secondes | AJOUT |
| scalabilité horizontale | CONCEPT | condition | Exige des workers sans état ; le v0 à écrivain unique par test l'interdisait | AJOUT |
| Claude Tag | TECHNOLOGIE | usage | Session longue de supervision d'un service : seuil d'alerte à 50 000 jobs de retard, conversation reprise sans recharger le contexte | AJOUT |
