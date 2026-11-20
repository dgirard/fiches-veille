---
themes: [politique-regulation, qualite-securite]
source: SFEIR
---
# sfeir-licence-retro-ingenierie-clauses-nulles-2026-10-13

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **13 octobre 2026** (~7 000 signes, sept sources juridiques), présenté comme des « points d'attention » et non comme un conseil juridique. Il part du dernier alinéa de l'**article L122-6-1** du Code de la propriété intellectuelle — *« Toute stipulation contraire aux dispositions prévues aux II, III et IV du présent article est nulle et non avenue »* — et l'applique à l'arrivée d'outils comme **REA** qui donnent à un agent les moyens d'un rétro-ingénieur. **(1)** Trois droits d'ordre public : copie de sauvegarde (II), **observer, étudier, tester** le fonctionnement pendant les opérations autorisées (III, confirmé par l'arrêt **SAS Institute**, CJUE, 2 mai 2012), décompilation à fin d'interopérabilité (IV). **(2)** Ce qui reste contractuel : correction d'erreurs que l'auteur peut se réserver (arrêt **Top System**, 6 octobre 2021), copie de code, réutilisation de ressources, diffusion des résultats. **(3)** Le **secret des affaires** (directive 2016/943, art. L151-3 du Code de commerce) admet l'observation d'un produit sauf « obligation juridiquement valide » contraire. **(4)** Pour une licence de droit étranger, la portée de la règle française se discute au cas par cas. Prolonge le volet juridique de [[sfeir-rea-trois-schemas-architecture-usage-2026-10-12]].

## Titre Article

Clauses de licence et rétro-ingénierie : ce qui est nul en France

## Date

2026-10-13

## URL

https://www.sfeir.com/articles/licence-logiciel-retro-ingenierie/

## Keywords

rétro-ingénierie, clause de licence, EULA, article L122-6-1, Code de la propriété intellectuelle, nullité, ordre public, copie de sauvegarde, observer étudier tester, décompilation, interopérabilité, directive 2009/24/CE, CJUE, SAS Institute, Top System, correction d'erreurs, secret des affaires, directive 2016/943, L151-3, loi applicable, clean-room, REA

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, publiée sur sfeir.com (site éditorial de l'ESN).

## Ton

**Profil** : note d'information juridique vulgarisée à destination des DSI et responsables de projet. Français clair, articles de loi et arrêts cités avec leur référence, aucune technicité logicielle.

**Style** : ouverture sur la citation du texte légal, puis avertissement explicite (*« Ceci n'est pas un conseil juridique »*, « le conseil juridique n'est pas le métier de SFEIR »). Le corps suit la structure de l'article L122-6-1 paragraphe par paragraphe, puis traite le secret des affaires et les licences étrangères. Une grille de trois questions à se poser avant d'analyser un logiciel tiers et une FAQ de quatre questions concluent.

**Position épistémique** : sources exclusivement primaires (Légifrance, EUR-Lex, Curia) plus le disclaimer du dépôt REA. Les zones d'incertitude sont nommées comme telles (articulation droit d'auteur / secret des affaires, loi applicable aux EULA américaines) et renvoyées au juriste. Le clean-room est présenté comme un moyen de preuve, pas comme une obligation légale. Renvois internes vers les pages du site sur la décompilation, le clean-room et ArtCraft.

## Pense-betes

- **Phrase-clé** : dernier alinéa de **L122-6-1 CPI** — toute stipulation contraire aux **II, III et IV** est *« nulle et non avenue »*. Transpose la directive de 1991, codifiée par la **directive 2009/24/CE**.
- **II** : copie de sauvegarde nécessaire à l'utilisation.
- **III** : observer, étudier, tester le fonctionnement pour en déterminer idées et principes, **pendant** chargement, affichage, exécution, transmission ou stockage autorisés → une licence ne peut l'interdire. **CJUE, SAS Institute, C-406/10, 2 mai 2012**.
- **IV** : décompilation à seule fin d'interopérabilité, sous conditions.
- **I (contractuel)** : l'auteur peut se réserver la correction d'erreurs ; **CJUE, Top System, C-13/20, 6 octobre 2021** : décompiler pour corriger est admis, dans le respect du contrat.
- **Reste contractuel** : copier du code, réutiliser des ressources graphiques, décompiler au-delà de l'interopérabilité, diffuser les résultats.
- **Disclaimer REA** : une sortie qui ressemble à du code source *« does not grant rights to the original program »*.
- **Secret des affaires** : directive (UE) **2016/943**, art. 3 ; **L151-3 C. com.** — observation, démontage, test d'un produit public ou détenu licitement = obtention licite, sauf « obligation juridiquement valide ».
- **EULA américaines** : interdictions larges ; portée de la règle française selon la loi applicable, au cas par cas.
- **Trois questions avant d'analyser** : observation (III), interopérabilité (IV) ou correction (contrat) ? Résultat interne ? Réécriture prévue ? Si oui → séparation clean-room comme moyen de preuve.
- **Publication** : les droits protégés couvrent l'analyse, pas la diffusion.

## RésuméDe400mots

L'article, signé SFEIR AI, examine la validité en France des clauses de licence logicielle qui interdisent toute rétro-ingénierie. Le sujet devient concret, selon le texte, avec des outils comme REA qui donnent à un agent de code les moyens d'un rétro-ingénieur. L'article précise d'emblée qu'il ne constitue pas un conseil juridique et renvoie toute décision à un juriste.

Le point de départ est le dernier alinéa de l'article L122-6-1 du Code de la propriété intellectuelle, qui déclare nulle toute stipulation contraire à ses paragraphes II, III et IV. Cet article transpose la directive européenne de 1991, codifiée par la directive 2009/24/CE. Trois droits sont ainsi protégés contre le contrat. Le II autorise la copie de sauvegarde nécessaire. Le III autorise l'utilisateur légitime à observer, étudier ou tester le fonctionnement du logiciel pour en déterminer les idées et principes, à condition de le faire pendant les opérations qu'il a le droit d'effectuer. Le IV autorise la décompilation à seule fin d'interopérabilité. L'article insiste sur le III : faire tourner un logiciel exploité légalement et observer ses entrées, sorties et échanges réseau ne peut être interdit. La Cour de justice de l'Union européenne l'a confirmé dans l'arrêt SAS Institute du 2 mai 2012.

Le contrat garde cependant un champ. Le I permet à l'auteur de se réserver la correction des erreurs ; l'arrêt Top System du 6 octobre 2021 admet la décompilation pour corriger, dans le respect des conditions contractuelles. Copier du code, réutiliser des ressources graphiques, décompiler au-delà de l'interopérabilité ou diffuser les résultats restent soumis à la licence. Le disclaimer de REA rappelle qu'une sortie ressemblant à du code source ne confère aucun droit sur le programme d'origine.

Le secret des affaires forme un second volet. La directive 2016/943, transposée à l'article L151-3 du Code de commerce, range l'observation et le démontage d'un produit détenu licitement parmi les obtentions licites, sauf obligation juridiquement valide contraire. L'articulation avec le droit d'auteur est renvoyée au juriste. Pour les licences d'éditeurs américains, la portée des règles françaises dépend de la loi applicable au contrat et se discute au cas par cas.

L'article propose trois questions avant toute analyse d'un logiciel tiers : de quel régime relève l'analyse, le résultat restera-t-il interne, une réécriture est-elle prévue. Dans ce dernier cas, la séparation des équipes en clean-room, sans être une obligation légale, devient le moyen le plus sûr de démontrer que le nouveau code ne reprend pas l'ancien.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Clauses de licence et rétro-ingénierie : ce qui est nul en France | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Clauses de licence et rétro-ingénierie : ce qui est nul en France | DOCUMENT | référence | article L122-6-1 du CPI | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | est_basé_sur | directive 2009/24/CE | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | affirme_que | toute stipulation contraire aux II, III et IV est nulle et non avenue | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | permet | observer, étudier et tester le fonctionnement d'un logiciel | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| article L122-6-1 du CPI | DOCUMENT | permet | décompilation à fin d'interopérabilité | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| arrêt SAS Institute | DOCUMENT | soutient | l'acquéreur d'une licence peut observer, étudier et tester le programme sans porter atteinte au droit d'auteur | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| arrêt Top System | DOCUMENT | affirme_que | l'acquéreur légitime peut décompiler pour corriger des erreurs, dans le respect du contrat | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| CJUE | ORGANISATION | publie | arrêt SAS Institute | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| CJUE | ORGANISATION | publie | arrêt Top System | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| directive (UE) 2016/943 | DOCUMENT | affirme_que | l'observation, le démontage ou le test d'un produit détenu licitement est une obtention licite, sauf obligation valide contraire | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la diffusion des résultats d'une analyse reste soumise à la licence | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| clean-room | METHODOLOGIE | permet | démontrer que le nouveau code ne reprend pas l'ancien | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | relire la licence avec trois questions (régime, diffusion, réécriture) avant d'analyser un logiciel tiers | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | rétro-ingénierie | CONCEPT | 0.84 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| article L122-6-1 du CPI | DOCUMENT | portée | Droits de l'utilisateur de logiciel ; II, III et IV d'ordre public | AJOUT |
| arrêt SAS Institute | DOCUMENT | référence | CJUE, 2 mai 2012, C-406/10 | AJOUT |
| arrêt Top System | DOCUMENT | référence | CJUE, 6 octobre 2021, C-13/20 | AJOUT |
| directive (UE) 2016/943 | DOCUMENT | objet | Secret des affaires, transposée à l'article L151-3 du Code de commerce | AJOUT |
| directive 2009/24/CE | DOCUMENT | objet | Protection juridique des programmes d'ordinateur (23 avril 2009) | AJOUT |
