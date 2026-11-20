---
themes: [politique-regulation, outils-plateformes, economie-marche]
source: SFEIR
---
# sfeir-openrouter-zdr-souverainete-2026-10-19

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **19 octobre 2026** (~850 mots, trois sources : la page Providers d'**OpenRouter** et un relevé de son API publique à la même date). Il décompose le filtre public « pas d'entraînement, rétention zéro » : **(1)** sur **94** fournisseurs, **41** passent le filtre ; leurs sièges se répartissent en **34** aux États-Unis, **4** à Singapour (entités d'éditeurs issus de l'écosystème chinois : Z.ai, Moonshot AI, Seed, SiliconFlow) et **3** en Europe (Inceptron, Nebius Token Factory, NextBit) ; Mistral en sort, OpenRouter lui attribuant une rétention par défaut de 30 jours. **(2)** Ces 41 fournisseurs servent **229** modèles ; lus avec un critère de juridiction (siège européen), il en reste **22**, tous open weights. **(3)** **GLM-5.3** compte **25** hébergeurs du filtre, ce qui permet de changer d'hébergeur sans toucher au modèle. L'article résume : le filtre *« répond à la question de l'usage des prompts ; la juridiction se lit dans la colonne des sièges »*. Rejoint, côté coûts, [[walker-onlycfo-ai-tokenomics-2026-10-22]].

## Titre Article

OpenRouter : rétention zéro ne veut pas dire souverain

## Date

2026-10-19

## URL

https://www.sfeir.com/articles/openrouter-providers-zdr-souverainete/

## Keywords

OpenRouter, rétention zéro, zero data retention, ZDR, souveraineté numérique, juridiction, Cloud Act, siège social, fournisseurs d'inférence, providers, Europe, Singapour, Inceptron, Nebius Token Factory, NextBit, Mistral, Z.ai, Moonshot AI, GLM-5.3, open weights, réversibilité, data_collection deny, routage LLM, RGPD

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Note courte et factuelle, en français, construite sur un relevé daté et chiffré. Le registre est celui du **décompte** : chaque nombre est rattaché à une source (page Providers filtrée, API publique) et l'article rappelle en conclusion que les compteurs bougent chaque semaine et que tous datent du 19 octobre 2026. Le point de départ est un post LinkedIn qui résumait le filtre en « Europe ou USA », que l'article confronte à la colonne des sièges. La distinction structurante (usage des données vs juridiction vs emplacement des datacenters) est posée sans emphase. La partie finale est opérationnelle (paramètres `data_collection: "deny"` et `zdr: true`, contrat signé avec l'hébergeur) et renvoie à des articles satellites du même dossier OpenRouter ; l'appel à l'action porte sur un audit du routage LLM par SFEIR.

## Pense-betes

- **Relevé du 19 octobre 2026** : **94** providers sur OpenRouter ; **41** passent le filtre « Does not train / Zero retention / Has terms of service ».
- **Sièges des 41** : **34 États-Unis**, **4 Singapour** (Z.ai, Moonshot AI, Seed/ByteDance, SiliconFlow), **3 Europe** (Inceptron en Suède, Nebius Token Factory aux Pays-Bas, NextBit en Espagne) ; aucun en France ni en Israël.
- **Mistral** et **AionLabs** hors filtre : politique par défaut à **30 jours** de rétention ; le filtre juge la politique du fournisseur, jamais l'endpoint (Mistral sert pourtant GLM-5.3 sur `mistral/zdr` et `mistral/nvfp4/eu`).
- **229 modèles** servis par les 41, dont **43** d'OpenAI, **15** d'Anthropic, **22** de Google, via Azure, Bedrock et Vertex ; OpenAI et Anthropic ne figurent pas eux-mêmes parmi les 41.
- **Cloud Act** : un siège américain y est soumis quel que soit l'engagement de rétention zéro ; le siège ne dit rien de l'emplacement des datacenters (routage UE = plan Business d'OpenRouter).
- **Critère de souveraineté** : 3 européens, **22 modèles, tous open weights** (GLM-5.x, Kimi K2.6/K2.7 Code, DeepSeek V4 Flash, Qwen3, Gemma, gpt-oss-120b, Nemotron, Hermes 4) ; aucun modèle propriétaire d'OpenAI, Anthropic ou Google par un siège européen.
- **GLM-5.3** (Z.ai, licence MIT) : **25** hébergeurs du filtre, dont Inceptron et Nebius ; changer d'hébergeur sans changer de modèle, de prompt ni de contexte.
- **Avant de router** : filtre = point de départ (déclarations à vérifier) ; poser `data_collection: "deny"` et `zdr: true`, fixer l'ordre des fournisseurs ; **contrat signé** avec l'hébergeur (*« Une case cochée dans une interface ne vaut pas un engagement »*).

## RésuméDe400mots

L'article examine le filtre public de confidentialité d'OpenRouter à partir d'un relevé effectué le 19 octobre 2026. Ce jour-là, la page Providers recense 94 fournisseurs d'inférence. Le filtre « pas d'entraînement sur les prompts, rétention zéro, conditions d'utilisation publiées » en retient 41, avec des sièges déclarés dans une liste de pays allant des États-Unis à la France. Un post LinkedIn avait résumé ce filtre en « Europe ou USA » ; l'article reprend la colonne des sièges.

Sur les 41, 34 ont leur siège aux États-Unis, 4 à Singapour et 3 en Europe ; aucun en Israël ni en France. Les quatre singapouriens sont les entités locales d'éditeurs issus de l'écosystème chinois (Z.ai, Moonshot AI, Seed de ByteDance, SiliconFlow). Les trois européens sont Inceptron (Suède), Nebius Token Factory (Pays-Bas) et NextBit (Espagne). Mistral manque, car OpenRouter lui attribue une rétention par défaut de 30 jours et le filtre juge la politique, pas l'endpoint, alors même que Mistral sert GLM-5.3 sur des endpoints étiquetés ZDR et UE. AionLabs sort pour le même motif.

Les 41 fournisseurs servent 229 modèles, dont 43 d'OpenAI, 15 d'Anthropic et 22 de Google, livrés via Azure, Amazon Bedrock et Google Vertex. Un siège américain relève du Cloud Act quel que soit l'engagement de rétention. Le filtre répond donc à la question de l'usage des prompts, la juridiction se lit dans le siège, et le siège ne renseigne pas l'emplacement des datacenters, le routage régional européen dépendant du plan Business d'OpenRouter. Avec un critère de souveraineté, il reste trois fournisseurs et 22 modèles, tous open weights (GLM, Kimi, DeepSeek V4 Flash, Qwen3, Gemma, gpt-oss-120b, Nemotron, Hermes 4) ; aucun modèle propriétaire des trois grands éditeurs américains n'arrive par un siège européen.

Le cas de GLM-5.3, modèle open weights de Z.ai sous licence MIT, illustre l'autre versant : 25 fournisseurs du filtre le servent, dont Inceptron et Nebius, plus Mistral hors filtre. On peut changer d'hébergeur sans toucher au modèle, au prompt ni au contexte, alors qu'un modèle propriétaire se loue chez son éditeur et deux ou trois hyperscalers.

L'article conclut par trois consignes : traiter le filtre comme un point de départ fondé sur des déclarations à vérifier, poser `data_collection: "deny"` et `zdr: true` en fixant soi-même l'ordre des fournisseurs, et signer un contrat avec l'hébergeur retenu. Tous les chiffres datent du 19 octobre 2026.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | OpenRouter : rétention zéro ne veut pas dire souverain | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | 41 providers OpenRouter sur 94 passent le filtre ZDR, dont 34 sièges aux États-Unis et 3 en Europe | MESURE | 0.93 | STATIQUE | déclaré_article |
| OpenRouter | TECHNOLOGIE | utilise | Zero Data Retention | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le filtre ZDR règle l'usage des prompts, pas la juridiction | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Cloud Act | CONCEPT | s_applique_à | fournisseurs d'inférence à siège américain | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| OpenRouter | TECHNOLOGIE | utilise | Inceptron | ORGANISATION | 0.85 | DYNAMIQUE | déclaré_article |
| OpenRouter | TECHNOLOGIE | utilise | Nebius Token Factory | ORGANISATION | 0.85 | DYNAMIQUE | déclaré_article |
| Mistral | ORGANISATION | utilise | GLM-5.3 | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Z.ai | ORGANISATION | a_créé | GLM-5.3 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | 25 hébergeurs du filtre servent GLM-5.3 | MESURE | 0.9 | STATIQUE | déclaré_article |
| GLM-5.3 | TECHNOLOGIE | permet | réversibilité d'hébergeur | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | mesure | 22 modèles, tous open weights, accessibles par un siège européen du filtre | MESURE | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | signer un contrat avec l'hébergeur plutôt que se fier à une case cochée | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | poser data_collection deny et zdr true et fixer l'ordre des fournisseurs | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| OpenRouter | TECHNOLOGIE | catégorie | routeur / marketplace d'inférence LLM, 94 providers au 19 octobre 2026 | AJOUT |
| Zero Data Retention | CONCEPT | définition | engagement de non-conservation des prompts, distinct de la juridiction du fournisseur | AJOUT |
| Cloud Act | CONCEPT | portée | loi américaine à portée extraterritoriale (2018) | AJOUT |
| GLM-5.3 | TECHNOLOGIE | licence | open weights MIT (Z.ai), 25 hébergeurs du filtre | AJOUT |
| Inceptron | ORGANISATION | siège | Suède | AJOUT |
| Nebius Token Factory | ORGANISATION | siège | Pays-Bas | AJOUT |
| Mistral | ORGANISATION | politique OpenRouter | rétention par défaut à 30 jours, hors filtre ZDR | AJOUT |
