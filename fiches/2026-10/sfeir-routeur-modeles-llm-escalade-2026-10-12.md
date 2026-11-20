---
themes: [outils-plateformes, economie-marche, architecture-construction]
source: SFEIR
---
# sfeir-routeur-modeles-llm-escalade-2026-10-12

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **12 octobre 2026** (~20 000 signes, 14 sources). Il part des **Model Router Benchmarks** publiés par **OpenRouter** le 2 octobre 2026 (sept routeurs, six benchmarks, Router Index pondéré **60/20/20** qualité, temps, coût) et pose la question : confier le choix du modèle à un routeur, ou coder une escalade mesurée ? **(A)** Les exécutions brutes, consultées le 12 octobre : sur **GPQA Diamond**, Fugu Ultra atteint **0,946** pour **227,45 $** (594 questions), Switchyard **0,949** pour **7,09 $** (198 questions) ; l'Auto Router en palier « low » fait mieux (0,882) qu'en « high » (0,832) pour sept fois moins cher ; en vision, les routeurs restent sous GPT-6 Astra et Claude Opus 5.5 appelés seuls. **(B)** L'Auto Router suit la dépense de la communauté sur sept jours, pas la qualité chez l'utilisateur. **(C)** La méthode retenue : une barre de qualité par tâche, trois paliers testés sur 20 à 50 exemples, une escalade par seuil de confiance codée dans l'application — *« c'est votre code qui prend la décision d'escalade »* — et un jeu d'évaluation versionné. Le cache de préfixe plaide pour router par tâche au premier tour. Volet jumeau de [[sfeir-openrouter-production-reglages-2026-10-12]].

## Titre Article

Routeur de modèles LLM : quand il bat un modèle unique, et quand il perd

## Date

2026-10-12

## URL

https://www.sfeir.com/articles/routeur-modeles-llm-benchmarks-escalade/

## Keywords

routeur de modèles LLM, model router, OpenRouter, Model Router Benchmarks, Router Index, Auto Router, cost_tier, Fugu, Sakana, Switchyard, NVIDIA, Jev Router, TypeSafe, Pareto, GPQA Diamond, barre de qualité par tâche, escalade, seuil de confiance, JSON schema strict, evals, jeu d'évaluation, LLM-as-a-judge, cache de préfixe, coût par tâche réussie, FinOps

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, publiée sur sfeir.com (site éditorial de l'ESN).

## Ton

**Profil** : article d'arbitrage technique destiné aux CTO, architectes, équipes FinOps et DSI qui mettent un agent en production. Français technique, chiffres extraits d'exécutions de benchmark, paramètres d'API cités dans leur syntaxe.

**Style** : verdict posé en ouverture (« un routeur se juge sur votre trafic, avec vos critères »), puis démonstration en sections interrogatives (que mesurent les benchmarks, pourquoi un index ne décide rien, la méthode qui tient). Les chiffres sont présentés par paires précision/coût pour montrer ce que la pondération lisse. Les citations de l'éditeur sont traduites en français entre guillemets. Une section de consignes par rôle et une FAQ de quatre questions terminent.

**Position épistémique** : l'article distingue les données brutes (« ils ne constituent pas un palmarès », volumes de questions variables d'une exécution à l'autre) des exemples que l'éditeur déclare lui-même illustratifs (routage de tickets, escalade à seuil 0,7). Il s'appuie presque entièrement sur des billets OpenRouter, complétés par la documentation Anthropic et l'article de Zheng et al. (NeurIPS 2023) sur le juge LLM. Le score de confiance d'un LLM est signalé comme autodéclaré, à calibrer sur ses propres données. Renvois internes vers d'autres articles du site (coût par outcome, un modèle par tâche, TDD du contexte).

## Pense-betes

- **Benchmarks OpenRouter (02/10/2026)** : 7 routeurs (Auto Router, Jev Router/TypeSafe, Pareto/Unbiased, Fugu Max et Ultra/Sakana, Switchyard/NVIDIA) × 6 benchmarks (deep_swe, swe_atlas_qa, terminal-bench-4.0, GPQA Diamond, mmmu_pro_vision, search_hle, tau3_bench_banking). Router Index 0-10, pondéré **60 % score / 20 % temps / 20 % coût** ; aucun classement publié en texte.
- **Quatre limites admises par OpenRouter** : cache reconstruit à chaque bascule ; complexité de la tâche illisible depuis le seul prompt ; signaux de session contradictoires ; latence ajoutée par la décision.
- **GPQA Diamond** : Fugu Ultra 0,946 / 227,45 $ (594 q.) ; Switchyard 0,949 / 7,09 $ (198 q.) ; Jev 0,939 / 3,15 $ → écart **> ×10** par question à précision équivalente.
- **Le palier ne paie pas** : Auto « low » **0,882 pour 8,99 $** vs « high » **0,832 pour 60,23 $** (990 questions).
- **Vision** (mmmu_pro_vision) : GPT-6 Astra seul 0,842, Claude Opus 5.5 0,818 ; meilleur routeur (Auto « medium ») 0,812.
- **Auto Router** : critère = dépense communautaire sur 7 jours glissants, ~30 types de tâches, `cost_tier` par défaut au moins cher → « que paient les autres », inexplicable en comité d'architecture.
- **Méthode coût/qualité** : barre par tâche ; 3 paliers sur 20-50 exemples ; retenir le moins cher qui passe avec une marge > variance entre exécutions ; coût lu dans `usage.cost`. Exemple illustratif : Luna 0,32 $ / 82 (sous la barre 85), **Gemini 3.7 Flash 1,09 $ / 89 retenu**, Opus 5 7,25 $ / 97.
- **Escalade par seuil** : sortie JSON stricte + score de confiance ; sous le seuil, le code relance vers le modèle fort. Illustration : seuil 0,7, **14 %** escaladé, erreur ~10 % → ~4 %. Les fallbacks de passerelle ne réagissent qu'aux erreurs.
- **Score de confiance autodéclaré** → calibrer sur son jeu d'éval, ou confier la décision à un modèle de décision (Jev, probabilités calibrées).
- **Evals** : 1-2 semaines de journaux, 20-50 items puis 100-1 000 ; *couverture des modes d'échec > volume* ; double annotation ; juge distinct du modèle noté (biais d'auto-complaisance, Zheng et al. : >80 % d'accord avec l'humain) ; porte de CI ; pas d'alias `-latest`. Ori Eval : 10-30 $ par eval.
- **Cache** : 80-90 % de réduction du prefill annoncée ; cache médian 44 % → 85 % (janv.-sept. 2026) ; toute bascule repart à vide → **router par tâche au premier tour, jamais par requête en cours de session**.

## RésuméDe400mots

L'article, signé SFEIR AI, examine quand un routeur de modèles LLM fait mieux qu'un modèle unique. Il s'appuie sur les Model Router Benchmarks publiés par OpenRouter le 2 octobre 2026 : sept routeurs comparés sur six benchmarks, avec un Router Index qui pondère à 60 % le score, 20 % le temps et 20 % le coût. Le même billet liste quatre limites : reconstruction du cache à chaque changement de modèle, information insuffisante dans le prompt pour juger la complexité, signaux de session trompeurs, latence ajoutée.

Le verdict est posé d'emblée : un routeur se juge sur son propre trafic, et le défaut défendable en production reste un modèle de base choisi sur une barre de qualité, avec une escalade codée dans l'application. Les exécutions brutes, consultées par SFEIR, appuient ce verdict. Sur GPQA Diamond, des précisions proches (0,946 à 0,949) s'obtiennent pour des coûts qui diffèrent de plus d'un facteur dix par question. Le palier de coût « high » de l'Auto Router fait moins bien que le palier « low », pour sept fois plus cher. En vision, aucun routeur n'atteint les meilleurs modèles appelés directement.

L'Auto Router choisit d'après la dépense de la communauté OpenRouter sur sept jours glissants, par type de tâche. L'article y voit un outil de découverte, mais un critère difficile à justifier devant un comité d'architecture.

La méthode proposée reprend un cadre publié par OpenRouter : fixer une barre de qualité par tâche, comparer trois paliers de modèles sur 20 à 50 exemples, retenir le moins cher qui passe la barre avec une marge supérieure à la variance, lire le coût dans la réponse de l'API. Pour l'escalade, le modèle économique répond dans un schéma JSON strict avec un score de confiance ; sous un seuil, le code applicatif relance la requête vers un modèle plus fort. Dans l'exemple de l'éditeur, 14 % des requêtes escaladent et l'erreur passe d'environ 10 % à 4 %. Les chaînes de secours de la passerelle ne remplacent pas ce mécanisme, car elles ne réagissent qu'aux erreurs.

Tout repose sur un jeu d'évaluation construit depuis le trafic de production, noté par un juge distinct du modèle évalué, intégré à la CI et protégé des alias qui changent de modèle sans commit. Dernier point, le cache de préfixe : chaque bascule le vide, alors que le taux médian de cache est passé de 44 % à 85 % en 2026. L'article recommande de fixer le modèle au premier tour d'une session d'agent et de comparer les options sur le coût par tâche réussie, pas sur le prix au token ni sur un index.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Routeur de modèles LLM : quand il bat un modèle unique, et quand il perd | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| OpenRouter | ORGANISATION | publie | Model Router Benchmarks | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Brian Thomas | PERSONNE | travaille_chez | OpenRouter | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| Model Router Benchmarks | DOCUMENT | affirme_que | les routeurs peuvent faire moins bien qu'un modèle appelé directement | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Fugu Ultra | TECHNOLOGIE | mesure | 0,946 sur GPQA Diamond pour 227,45 $ (594 questions) | MESURE | 0.88 | STATIQUE | déclaré_article |
| Switchyard | TECHNOLOGIE | mesure | 0,949 sur GPQA Diamond pour 7,09 $ (198 questions) | MESURE | 0.88 | STATIQUE | déclaré_article |
| Sakana | ORGANISATION | a_créé | Fugu Ultra | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| NVIDIA | ORGANISATION | a_créé | Switchyard | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| TypeSafe | ORGANISATION | a_créé | Jev | TECHNOLOGIE | 0.86 | STATIQUE | déclaré_article |
| Auto Router | TECHNOLOGIE | fait_partie_de | OpenRouter | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Auto Router | TECHNOLOGIE | utilise | dépense communautaire sur sept jours glissants | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| GPT-6 Astra | TECHNOLOGIE | surpasse | Auto Router | TECHNOLOGIE | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | une barre de qualité par tâche et le modèle le moins cher qui la passe avec marge | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| escalade par seuil de confiance | METHODOLOGIE | réduit | taux d'erreur d'environ 10 % à 4 % avec 14 % de requêtes escaladées (exemple illustratif) | MESURE | 0.8 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | l'escalade qualitative se code dans l'application, aucun paramètre de routage ne la fait | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| LLM-as-a-judge | METHODOLOGIE | est_basé_sur | Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena | DOCUMENT | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | fixer le modèle d'une session d'agent au premier tour pour préserver le cache de préfixe | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Model Router Benchmarks | DOCUMENT | contenu | 7 routeurs, 6 benchmarks, Router Index pondéré 60/20/20 (OpenRouter, 2 octobre 2026) | AJOUT |
| Auto Router | TECHNOLOGIE | critère | Dépense de la communauté OpenRouter par type de tâche, cost_tier de « low » à « max » | AJOUT |
| escalade par seuil de confiance | METHODOLOGIE | définition | Modèle économique avec score de confiance en JSON strict, relance vers un modèle fort sous un seuil | AJOUT |
| Jev | TECHNOLOGIE | catégorie | Modèle de décision de TypeSafe, choix et probabilités calibrées sans génération de texte | AJOUT |
| Switchyard | TECHNOLOGIE | catégorie | Routeur de modèles de NVIDIA | AJOUT |
| Fugu Ultra | TECHNOLOGIE | catégorie | Routeur de modèles de Sakana (variante Ultra) | AJOUT |
