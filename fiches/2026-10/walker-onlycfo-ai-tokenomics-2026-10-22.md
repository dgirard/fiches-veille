---
themes: [economie-marche, outils-plateformes, strategie-frameworks]
source: "OnlyCFO"
---
# walker-onlycfo-ai-tokenomics-2026-10-22

## Veille

Article invité de **Peter Walker**, Head of Insights d'**OpenRouter**, publié le **22 octobre 2026** dans la newsletter Substack **OnlyCFO** (environ **1 500 mots**, graphiques OpenRouter). Le texte s'adresse aux directeurs financiers et tire ses chiffres du trafic de la passerelle d'inférence de l'auteur.

**(1)** Volume et prix : de **0,5 à 164 000 milliards de tokens par semaine** entre janvier 2025 et fin septembre 2026, pendant que le prix moyen payé passe de **0,77 $ à 0,14 $** le million de tokens. **(2)** Quatre forces : explosion de l'offre (**862** modèles depuis 2024) ; modèles open-weight à **~60 %** des tokens pour **26 %** de la dépense ; agents majoritaires depuis le **6 février 2026**, dont le coût dépend du *prompt caching* ; leader changeant (part de **40 % à 21 %**). **(3)** Découplage usage / dépense : startups IA-natives tokens ×18, dépense ×5,1. **(4)** Achat au *« landed cost »* : prix après remise de cache, coût d'attente et coût des reprises. **(5)** Critères hors prix : rétention zéro des données, disponibilité (**96,9 %** de succès après bascule automatique). **(6)** Quatre recommandations aux CFO.

L'article est rédigé à partir des données d'un intermédiaire dont le routage est l'objet de la recommandation. Il prolonge [[rafal-wenvision-tokenomics-foundation-finops-ia-2026-06-04]] sur le FinOps appliqué à l'IA.

## Titre Article

The Current State of AI Tokenomics | What CFOs Should Know

## Date

2026-10-22

## URL

https://www.onlycfo.io/p/ai-tokenomics

## Keywords

tokenomics, économie de l'inférence, CFO, directeur financier, coût de l'IA, prix par token, volume de tokens, OpenRouter, passerelle IA, marketplace de modèles, modèles open-weight, laboratoires chinois, fournisseurs d'inférence, endpoints, agents IA, trafic agentique, prompt caching, taux de cache, landed cost, coût des reprises, routage, bascule automatique, disponibilité, rétention zéro des données, ZDR, achat comme une matière première, découplage usage et dépense, garde-fous, FinOps

## Authors

Peter Walker — Head of Insights d'OpenRouter ; article invité dans la newsletter OnlyCFO.

## Ton

Profil : article invité de vulgarisation financière, en anglais, à la première personne du pluriel (« we » = OpenRouter), adressé aux CFO et plus largement aux « capital allocators ». L'introduction est signée par l'éditeur de la newsletter ; l'article est précédé d'un encart sponsorisé sans rapport (Remote).

Structure : un chiffre d'ouverture (volume contre prix), une thèse (l'inférence se comporte comme une matière première, pas comme un logiciel), quatre forces numérotées, une partie sur le prix, une sur le *« landed cost »*, une sur les critères hors prix, quatre recommandations.

Registre : pédagogique et assertif, appuyé sur un chiffre par paragraphe. Les analogies sont financières (*« landed cost »*, *« commodity input »*, *« the canary in the cost coal mine »*). L'humour reste discret (*« no comments on any or all upcoming IPOs! »*).

Preuves : exclusivement les données de la plateforme OpenRouter, sans méthodologie détaillée ni échantillon hors plateforme. La partie sur le routage décrit l'algorithme par défaut d'OpenRouter, et l'exemple de disponibilité compare les fournisseurs à OpenRouter.

## Pense-betes

- **Source** : article invité de Peter Walker (OpenRouter) dans OnlyCFO, 22 octobre 2026 ; données OpenRouter.
- **Thèse** : les entreprises achètent l'IA comme un logiciel (fournisseur, engagement annuel) alors que l'inférence se comporte comme une **matière première** : coûts unitaires en baisse, volume en hausse, meilleur fournisseur changeant tous les quelques mois.
- **Volume / prix** : **0,5 → 164 T tokens/semaine** (janv. 2025 → fin sept. 2026) ; prix moyen **0,77 $ → 0,14 $/M tokens**.
- **Offre** : **862** modèles lancés depuis 2024, dont **362** en 2026 avant octobre ; modèles à plus de 1 T tokens/semaine : **3 → 27** en six mois.
- **Open-weight** : **~60 %** des tokens, **26 %** de la dépense ; deux tiers sur des modèles de laboratoires chinois, dont **44 %** servis par des fournisseurs basés aux États-Unis. Endpoints modèle × fournisseur : **~330 → 1 342** en 2026. Voir [[sfeir-kimi-k3-moonshot-frontier-open-weights-2026-07-16]].
- **Agents** : passent devant les humains le **6 février 2026** ; fin septembre, **131 T** tokens/semaine contre **18 T**.
  - Cache : les agents renvoient le même long contexte à chaque étape. Taux de cache du trafic agentique **88 %** pour les modèles du trimestre contre **55 %** au printemps 2025 ; fournisseurs à plus de 90 % de cache : **2/35 → 11/54**.
- **Leader** : changé **5 fois en 8 trimestres** ; part du premier laboratoire **~40 % → 21 %**. Dépense Anthropic + OpenAI : **~80 %** Anthropic début 2026, quasi à parité en septembre.
- **Découplage** : startups IA-natives tokens **×18**, dépense **×5,1** ; grandes organisations **×5,1** et **×2,4**.
- **Causes de la baisse** : modèles bon marché plus capables (Kimi K3, DeepSeek V4 Flash) ; cache optimisé ; modèles économiques des laboratoires de frontière (Luna, Haiku). Prix réellement payés **43 % à 89 %** sous le prix catalogue pour trois modèles open-weight.
- **Landed cost** : prix effectif après remise de cache + coût d'attente + coût des reprises. Une requête à 1,00 $ qui réussit à 80 % coûte **1,25 $** par réponse réussie. **77 %** des requêtes vont à des modèles servis par plusieurs fournisseurs.
- **Hors prix** : endpoints ZDR pour **93 %** des tokens (18 des 20 premiers modèles) ; **92,8 %** de succès au premier fournisseur, **96,9 %** après bascule ; pendant une saturation, **18 %** pour les 15 fournisseurs les plus touchés.
- **Recommandations** : plus de tokens ≠ plus de dépense ; un modèle open-weight varie selon le fournisseur ; garde-fous (ZDR, routage régional, plafonds par fonction, repli) ; s'attendre au changement.
- ⚠️ **Portée** : données d'un seul intermédiaire, qui vend le routage et la bascule qu'il recommande ; pas de méthodologie publiée dans l'article.

## RésuméDe400mots

Le 22 octobre 2026, la newsletter OnlyCFO publie un article invité de Peter Walker, responsable des analyses d'OpenRouter, une passerelle qui donne accès à plusieurs centaines de modèles de langage par un seul compte. L'éditeur présente le coût de l'IA comme en passe de devenir le premier poste de dépense des entreprises, et le sujet comme une affaire de direction financière.

Les données d'OpenRouter montrent une combinaison rare : le volume traité passe d'un demi-millier de milliards de tokens par semaine en janvier 2025 à 164 000 milliards fin septembre 2026, tandis que le prix moyen payé tombe de 0,77 à 0,14 dollar le million de tokens. L'auteur en conclut que l'inférence se comporte comme une matière première, et non comme un logiciel acheté à un fournisseur sur engagement annuel.

Quatre forces expliquent cette évolution. L'offre explose : 862 modèles lancés depuis 2024, dont 27 dépassent mille milliards de tokens hebdomadaires. Les modèles open-weight portent environ 60 % des tokens pour 26 % de la dépense ; deux tiers viennent de laboratoires chinois, mais l'hébergement se choisit séparément du modèle, et 44 % de ces tokens sont servis par des fournisseurs américains. Les agents sont devenus la première source de tokens le 6 février 2026 ; comme ils renvoient le même contexte à chaque étape, le cache de prompt devient la variable de prix décisive, et le taux de cache des modèles récents atteint 88 %. Enfin, le leader change sans cesse : cinq fois en huit trimestres.

L'usage et la dépense se découplent : chez les startups natives de l'IA, les tokens sont multipliés par 18 et la dépense par 5,1. La baisse tient à des modèles bon marché plus capables, à l'optimisation du cache et aux modèles économiques des laboratoires de frontière. Pour un même modèle open-weight, le prix réellement payé se situe entre 43 % et 89 % sous le prix catalogue, et le fournisseur le moins cher en catalogue n'est souvent pas le moins cher à l'usage.

L'auteur propose donc d'acheter au « landed cost » : le prix après remise de cache, plus le coût de l'attente et celui des reprises. Une requête à un dollar qui échoue une fois sur cinq coûte 1,25 dollar par réponse réussie. S'y ajoutent la rétention zéro des données, disponible pour 93 % des tokens, et la disponibilité : 96,9 % de succès après bascule automatique.

Il conclut par quatre conseils aux directeurs financiers : consommer plus ne signifie pas dépenser plus, un modèle ouvert varie selon son fournisseur, les garde-fous sont indispensables, et les plans doivent rester révisables.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Peter Walker | PERSONNE | travaille_chez | OpenRouter | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | publie | article The Current State of AI Tokenomics | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| OnlyCFO | ORGANISATION | publie | article The Current State of AI Tokenomics | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| article The Current State of AI Tokenomics | DOCUMENT | est_basé_sur | données de trafic d'OpenRouter | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| Peter Walker | PERSONNE | mesure | volume OpenRouter passé de 0,5 à 164 000 milliards de tokens par semaine entre janvier 2025 et septembre 2026 | MESURE | 0.95 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | mesure | prix moyen payé passé de 0,77 $ à 0,14 $ par million de tokens | MESURE | 0.95 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | affirme_que | l'inférence se comporte comme une matière première et non comme un logiciel acheté sur engagement annuel | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| open-weights | CONCEPT | mesure | environ 60 % des tokens hebdomadaires pour 26 % de la dépense sur OpenRouter | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | mesure | les agents dépassent les humains comme source de tokens le 6 février 2026 ; 131 T contre 18 T par semaine fin septembre | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| Prompt caching | CONCEPT | réduit | coût par token du trafic agentique | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Peter Walker | PERSONNE | mesure | taux de cache du trafic agentique de 88 % pour les modèles lancés ce trimestre contre 55 % au printemps 2025 | MESURE | 0.90 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | mesure | part du premier laboratoire en tokens tombée de 40 % à 21 % ; leader changé cinq fois en huit trimestres | MESURE | 0.90 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | concurrence | OpenAI | ORGANISATION | 0.90 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | mesure | dépense cumulée Anthropic + OpenAI passée d'environ 80 % Anthropic début 2026 à une quasi-parité en septembre | MESURE | 0.88 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | mesure | startups IA-natives : tokens ×18 et dépense ×5,1 ; grandes organisations : ×5,1 et ×2,4 | MESURE | 0.90 | DYNAMIQUE | déclaré_article |
| Kimi K3 | TECHNOLOGIE | concurrence | Claude Opus | TECHNOLOGIE | 0.75 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | recommande | Landed cost | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| OpenRouter | TECHNOLOGIE | utilise | Landed cost | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| OpenRouter | TECHNOLOGIE | améliore | taux de succès des requêtes de 92,8 % à 96,9 % par bascule automatique | MESURE | 0.88 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | recommande | Zero Data Retention | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | prédit | les dépenses d'IA deviendront le premier poste de coût de la plupart des entreprises | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Peter Walker | PERSONNE | référence | FinOps | METHODOLOGIE | 0.72 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Peter Walker | PERSONNE | rôle | Head of Insights d'OpenRouter | AJOUT |
| OpenRouter | ORGANISATION | secteur | Passerelle et marketplace d'inférence donnant accès à des centaines de LLM par un seul compte | AJOUT |
| OpenRouter | TECHNOLOGIE | catégorie | Passerelle d'inférence multi-fournisseurs ; routage par défaut au landed cost, bascule automatique | AJOUT |
| OnlyCFO | ORGANISATION | secteur | Newsletter Substack destinée aux directeurs financiers | AJOUT |
| article The Current State of AI Tokenomics | DOCUMENT | nature | Article invité dans OnlyCFO, 22 octobre 2026, données OpenRouter | AJOUT |
| Landed cost | CONCEPT | définition | Prix effectif d'une requête : prix après remise de cache + coût d'attente + coût des reprises | AJOUT |
| Zero Data Retention | CONCEPT | définition | Endpoint qui ne conserve pas les données des requêtes ; disponible pour 93 % des tokens sur OpenRouter | AJOUT |
| Prompt caching | CONCEPT | rôle | Variable de prix décisive du trafic agentique, qui renvoie le même contexte à chaque étape | MISE_A_JOUR |
| open-weights | CONCEPT | part de marché | ~60 % des tokens et 26 % de la dépense sur OpenRouter (sept. 2026) | MISE_A_JOUR |
