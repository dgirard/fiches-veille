---
themes: [politique-regulation, agents-codage-ia-skills, qualite-securite]
source: SFEIR
---
# sfeir-clean-room-vs-reverse-engineering-2026-10-11

## Veille

Page pilier **SFEIR AI** publiée sur sfeir.com le **11 octobre 2026** et mise à jour le **23 octobre** (~1 700 mots, neuf sources), point d'entrée des questions de droit d'un dossier sur la rétro-ingénierie, avec l'avertissement *« Ceci n'est pas un conseil juridique »*. Elle part de **REA**, outil de rétro-ingénierie par agents sous licence MIT, qui promet d'examiner une fonctionnalité sans le code source puis de *« build a version for your project »*. Trois apports. **(A)** Une distinction : la **rétro-ingénierie** produit de la connaissance, la méthode **clean-room** organise une réécriture en séparant, de façon documentée, ceux qui analysent et ceux qui écrivent ; la salle blanche ne rend pas licite une étude initiale qui ne l'était pas. **(B)** Le cadre : directive **2009/24/CE** (articles 5 et 6) et article **L122-6-1** du CPI ; arrêts **Top System** (CJUE, **2021**, décompilation pour corriger des erreurs) et **SAS Institute** (**2012**, fonctionnalité non protégée) ; directive secret des affaires **2016/943** et article L151-3 du Code de commerce. **(C)** Le point de rupture : quand un même agent lit le décompilé puis réécrit, les deux rôles fusionnent ; Connor Turland juge que cela *« makes any clean-room argument pretty hard to defend »*, et la documentation de REA exige *« A separate account or container »*. Prolonge l'étude de cas [[sfeir-artcraft-clean-room-adobe-2026-10-09]].

## Titre Article

Clean-room ou reverse engineering : méthode et risque juridique à l'ère des agents

## Date

2026-10-11

## URL

https://www.sfeir.com/articles/clean-room-vs-reverse-engineering/

## Keywords

clean-room, salle blanche, rétro-ingénierie, reverse engineering, décompilation, REA, Reverse Engineer Anything, agents, directive 2009/24/CE, article L122-6-1, Code de la propriété intellectuelle, CJUE, Top System C-13/20, SAS Institute C-406/10, interopérabilité, correction d'erreurs, secret des affaires, directive 2016/943, L151-3 Code de commerce, séparation des rôles, traçabilité, conteneur séparé, Connor Turland, ArtCraft

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : page de référence juridique vulgarisée, publiée sur le site d'un cabinet, à destination des DSI et des équipes qui envisagent une réécriture assistée par agents. Français précis, encadré d'avertissement, FAQ en quatre questions.

**Style** : définitions d'abord (deux pratiques distinctes), puis textes applicables cités article par article, arrêts datés avec leur numéro, puis cas d'usage outillé (REA) et réflexe de preuve. Les citations de REA et de Connor Turland restent en anglais. Le texte renvoie à des pages satellites du dossier (décompilation, clauses de licence, WinDev, Cyber Resilience Act).

**Position épistémique** : prudente et délimitée — la page se présente comme un recueil de *« points d'attention »* à faire valider par un juriste. Elle précise la portée exacte de l'arrêt SAS Institute (l'acquéreur n'avait ni accédé au source ni décompilé) et rappelle que d'autres protections (brevet, secret des affaires, contrat, concurrence déloyale) peuvent jouer sur une fonctionnalité. L'argument central sur l'agent unique s'appuie sur la documentation de l'outil lui-même.

## Pense-betes

- **Rétro-ingénierie** : observer, tracer, décompiler pour comprendre ; produit pseudocode, schémas d'appels, description de format.
- **Clean-room** : équipe 1 rédige une spécification expurgée de tout code protégé ; équipe 2 réimplémente sans jamais avoir vu l'original. La barrière et la trace écrite font la valeur juridique.
- **Limite** : la salle blanche ne couvre pas une décompilation initiale faite hors des cas légaux.
- **Article 5 de la directive 2009/24/CE** : actes nécessaires à l'acquéreur légitime — observer, étudier, tester, corriger. **Top System (C-13/20, 6 octobre 2021)** : décompilation possible pour corriger des erreurs, dans la mesure nécessaire et dans le respect du contrat.
- **Article 6** : décompilation à seule fin d'interopérabilité ; interdit de produire un logiciel *« dont l'expression est substantiellement similaire »*.
- **SAS Institute (C-406/10, 2 mai 2012)** : fonctionnalité, langage et format de fichiers non protégés — solution fondée sur une étude sans accès au source ni décompilation.
- **Secret des affaires** : directive 2016/943 et L151-3 C. com. — observer, démonter, tester un produit licitement détenu est une obtention licite, sauf obligation contractuelle valide.
- **Agent unique** : lire le décompilé et réécrire dans la même session fusionne les rôles. REA documente que ses restrictions de projet laissent shell, fichiers et réseau accessibles.
- **Réflexe de preuve** : spécification relue et expurgée ; équipe de réécriture sur d'autres comptes et machines, sans accès à l'outil d'analyse ni à ses sorties ; journal de chaque passage de document.
- **Usage de REA** : ses sorties, qui accompagnent chaque conclusion de preuves et de limites, documentent l'analyse sans remplacer la séparation organisationnelle.

## RésuméDe400mots

Cette page de SFEIR sert de point d'entrée juridique à un dossier sur la rétro-ingénierie à l'heure des agents. Elle part de REA, un outil publié sous licence MIT qui fait examiner une fonctionnalité d'application par un agent, sans le code source, puis propose d'en construire une version pour son propre projet. La page précise d'emblée qu'elle ne constitue pas un conseil juridique et doit être validée par un juriste.

Elle distingue deux pratiques. La rétro-ingénierie observe, trace ou décompile un logiciel pour en comprendre le fonctionnement ; elle produit de la connaissance. La méthode clean-room organise une réécriture : une équipe rédige une spécification sans code protégé, une autre réimplémente à partir de cette seule spécification sans avoir vu l'original. La barrière entre les deux équipes et la trace écrite qui la prouve font la valeur juridique de la méthode, qui ne rend pas licite pour autant une étude initiale illicite.

Le cadre européen et français est rappelé. La directive 2009/24/CE, transposée à l'article L122-6-1 du Code de la propriété intellectuelle, autorise l'acquéreur légitime à observer, étudier et tester un programme, et à le décompiler pour corriger des erreurs selon l'arrêt Top System de 2021. Elle autorise aussi la décompilation à seule fin d'interopérabilité, sans permettre de produire un logiciel substantiellement similaire. L'arrêt SAS Institute de 2012 établit que la fonctionnalité, le langage et le format des fichiers ne sont pas protégés, dans une affaire où l'acquéreur n'avait ni lu le source ni décompilé. La directive sur le secret des affaires admet l'observation et le démontage d'un produit licitement détenu, sauf obligation contractuelle.

L'argument clean-room se fragilise quand un même agent lit le pseudocode décompilé puis écrit la réimplémentation : les deux rôles fusionnent. Connor Turland, qui a analysé Slack avec REA, juge l'argument alors difficile à défendre, et la documentation de REA demande un compte ou un conteneur séparé, interdisant l'accès à l'outil, à la cible et aux résultats, pour toute séparation clean-room. L'étude de cas ArtCraft illustre la difficulté.

La page recommande un réflexe de preuve : une spécification relue et expurgée, une équipe de réécriture sur d'autres comptes et d'autres machines, et la journalisation de chaque passage de document entre les deux. Les sorties de REA aident à documenter l'analyse mais ne remplacent pas la séparation organisationnelle.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Clean-room ou reverse engineering : méthode et risque juridique à l'ère des agents | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la rétro-ingénierie produit de la connaissance, le clean-room organise une réécriture | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | permet | rétro-ingénierie par agents | METHODOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| directive 2009/24/CE | DOCUMENT | affirme_que | la décompilation est autorisée à seule fin d'interopérabilité, sans produire un logiciel substantiellement similaire | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | est_basé_sur | directive 2009/24/CE | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| arrêt Top System | DOCUMENT | affirme_que | l'acquéreur légitime peut décompiler pour corriger des erreurs, dans la mesure nécessaire | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| arrêt SAS Institute | DOCUMENT | affirme_que | ni la fonctionnalité, ni le langage, ni le format des fichiers ne sont protégés par le droit d'auteur | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| directive (UE) 2016/943 | DOCUMENT | affirme_que | observer, démonter ou tester un produit licitement détenu est une obtention licite, sauf obligation valide | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Connor Turland | PERSONNE | affirme_que | un agent ayant lu le décompilé « makes any clean-room argument pretty hard to defend » | CITATION | 0.88 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | recommande | un compte ou un conteneur séparé pour l'équipe de réécriture | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un même agent qui lit le décompilé puis réécrit fusionne les deux rôles de la salle blanche | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | spécification expurgée, équipe de réécriture sur d'autres comptes et machines, journal des passages de documents | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | référence | ArtCraft | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, éditeur de sfeir.com | AJOUT |
| réimplémentation clean-room | METHODOLOGIE | définition | Une équipe spécifie le comportement, une autre réécrit sans voir le code d'origine ; la barrière se prouve par la trace écrite | AJOUT |
| rétro-ingénierie | METHODOLOGIE | définition | Observer, tracer ou décompiler un logiciel pour en comprendre le fonctionnement | AJOUT |
| REA | TECHNOLOGIE | définition | Reverse Engineer Anything, outil de rétro-ingénierie par agents, licence MIT (morluto/rea) | AJOUT |
| directive 2009/24/CE | DOCUMENT | référence | Protection juridique des programmes d'ordinateur, articles 5 et 6 | AJOUT |
| article L122-6-1 du CPI | DOCUMENT | référence | Transposition française des exceptions de la directive 2009/24/CE | AJOUT |
| arrêt Top System | DOCUMENT | référence | CJUE, 6 octobre 2021, C-13/20 | AJOUT |
| arrêt SAS Institute | DOCUMENT | référence | CJUE, 2 mai 2012, C-406/10 | AJOUT |
| directive (UE) 2016/943 | DOCUMENT | référence | Protection des secrets d'affaires, article 3 | AJOUT |
| Connor Turland | PERSONNE | rôle | Auteur d'un test de REA sur Slack (atcyrus.com, 20 oct. 2026) | AJOUT |
