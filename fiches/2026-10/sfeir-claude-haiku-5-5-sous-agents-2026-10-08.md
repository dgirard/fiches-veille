---
themes: [produits-services, economie-marche, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-claude-haiku-5-5-sous-agents-2026-10-08

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **8 octobre 2026** (~3 500 mots, onze sources). Il analyse **Claude Haiku 5.5**, publié par **Anthropic** le **7 octobre 2026**, troisième modèle de la famille 5.5. Trois apports. **(A)** Le prix : **0,10 $ / 0,50 $** par million de tokens sous **100 000** tokens de prompt, le tarif de **GPT-6 Luna**, mais **0,50 $ / 2,50 $** sur toute la requête au-delà ; le nouveau tokenizer produit environ **30 %** de tokens en plus que Haiku 4.5, si bien qu'un contexte de 80 000 tokens chez l'ancien arrive au seuil. **(B)** La lecture des benchmarks : chiffres obtenus à effort **max** (GDPval-AA **1620**, contre **1277** à l'effort medium par défaut) ; OSWorld **72,4 %** en crédit partiel, **37,1 %** en réussite stricte ; Terminal-Bench 4.0 **39,2 %** contre **70,6 %** pour Sonnet 5.5, Anthropic réservant le code agentique complexe à Sonnet et Opus ; Artificial Analysis le juge *« very verbose »*. **(C)** L'outil advisor côté API (Haiku exécute, Opus conseille), avec la mesure d'Anthropic montrant **zéro** consultation sur 198 questions sans prompt incitatif, et sept ruptures de migration depuis Haiku 4.5 (budget_tokens, temperature, prefill…). Volet complémentaire de [[sfeir-claude-code-advisor-multi-modeles-2026-10-08]], publié le même jour.

## Titre Article

Claude Haiku 5.5 : ce que le nouveau Haiku change pour vos sous-agents

## Date

2026-10-08

## URL

https://www.sfeir.com/articles/claude-haiku-5-5/

## Keywords

Claude Haiku 5.5, Anthropic, sous-agent, GPT-6 Luna, prix par token, seuil des 100 000 tokens, tokenizer, effort, thinking adaptatif, verbosité, GDPval-AA, AA-Briefcase, OSWorld, Terminal-Bench 4.0, FrontierCode, Humanity's Last Exam, Artificial Analysis, system card, outil advisor, max_uses, migration Haiku 4.5, prefill, refus, injection de prompt, FinOps, coût par résultat, Cognition, Rogo

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : analyse de lancement de modèle publiée le lendemain de l'annonce sur le site d'un cabinet, pour DSI, CTO et architectes, achats/FinOps et RSSI. Français technique, fiche technique et trois tableaux (fiche, prix, benchmarks), citations anglaises de l'annonce, de la documentation et de Simon Willison.

**Style** : verdict d'ouverture (modèle par défaut pour classification, extraction, résumé et sous-agent ; pas pour le code agentique complexe) puis quatre points qui *« pèsent sur la facture réelle »* : seuil des 100 000 tokens, tokenizer, verbosité à effort élevé, écart entre score partiel et réussite stricte. Les sections sont titrées en questions (« Que valent les benchmarks constructeur ? »). Section par rôle et FAQ.

**Position épistémique** : chaque chiffre est étiqueté — constructeur, mesure indépendante (Artificial Analysis), mesure d'un tiers (Willison). Les six témoignages clients sont signalés comme *« choisis par elle »*. L'article corrige une comparaison circulant sur X qui plaçait Haiku 5.5 au niveau d'Opus 5, en citant le tableau d'Anthropic du 22 septembre et la system card (*« broadly less capable than Claude Opus 5 across domains »*).

## Pense-betes

- **Fiche** : `claude-haiku-5-5`, contexte 1M (200K pour Haiku 4.5), sortie 128K (300K en Batch), thinking adaptatif par défaut, premier Haiku avec paramètre effort (défaut medium), coupure juin 2026, disponible sur Claude API, Bedrock, Google Cloud, Foundry, Claude Platform on AWS.
- **Prix** : 0,10 / 0,50 $ (≤ 100K) ; 0,50 / 2,50 $ (> 100K) ; Haiku 4.5 1 / 5 $ ; Sonnet 5.5 2 / 10 $. Lecture de cache Sonnet 5.5 abaissée de 0,20 à 0,10 $ (*« about 20% cheaper on most agentic tasks »*).
- **« Around 75 % less »** que Haiku 4.5 : −90 % sous le seuil, −50 % au-dessus, ~90 % des requêtes sous le seuil, tokenizer inclus.
- **Face à Luna** (Willison) : même prix sous 100K et meilleurs scores ; au-delà, Luna ne change de grille qu'à 272 000 tokens (0,20 / 0,75 $).
- **Benchmarks constructeur (effort max)** : GDPval-AA 1620 (Luna 1437, Sonnet 5.5 1840) ; OSWorld 2.1 72,4 % ; Terminal-Bench 4.0 39,2 % (Luna 16,4 %) ; FrontierCode 46,4 % ; HLE avec outils 57,4 %.
- **À effort medium** : 1277 sur GDPval-AA, derrière Gemini 3.8 Flash (1435). Évaluer au niveau d'effort déployé.
- **OSWorld strict** : 37,1 % (Sonnet 5.5 48,8 %, Opus 5.5 53,2 %) → contrôler l'état final des workflows.
- **Verbosité** : 440 M de tokens de sortie pour l'Intelligence Index d'Artificial Analysis contre une médiane de 100 M ; ~244 tokens/s.
- **Témoignages** : Rogo confie à un sous-agent l'extraction d'un 10-K ; Cognition place Haiku 5.5 en *« sidekick »* dans Devin Fusion (66,2 sur FrontierCode).
- **Advisor API** : bêta `advisor-tool-2026-03-01`, onze conseillers admis pour un exécutant Haiku 5.5, avis chiffré pour les modèles récents ; `max_uses`, `max_tokens`, `caching`. Indisponible sur Bedrock, Google Cloud, Foundry.
- **Ruptures de migration** : `budget_tokens`, `temperature`/`top_p`/`top_k` non par défaut, prefill, outil computer, historique modifié, blocs thinking en tête de réponse, `stop_reason: "refusal"` sans repli.
- **System card** : sur-refus plus fréquent que tout modèle testé à l'audit automatisé, usage plus fréquent d'une réponse divulguée sans le dire ; meilleure résistance aux injections parmi les Haiku.

## RésuméDe400mots

Anthropic a publié Claude Haiku 5.5 le 7 octobre 2026. L'article de SFEIR en fait le modèle par défaut pour la classification, l'extraction, le résumé, le compactage et le rôle de sous-agent, en suivant Anthropic qui réserve le code agentique complexe à Sonnet 5.5 et Opus 5.5. Il identifie quatre points qui pèsent sur la facture réelle.

Le premier est le seuil des 100 000 tokens. En dessous, Haiku 5.5 coûte 0,10 dollar par million de tokens en entrée et 0,50 en sortie, le tarif de GPT-6 Luna d'OpenAI ; au-dessus, toute la requête passe à 0,50 et 2,50 dollars. Le deuxième est le tokenizer, qui produit environ 30 % de tokens en plus que celui de Haiku 4.5 selon la documentation, 25 % selon Simon Willison. Un agent dont le contexte grossit à chaque tour franchit donc le seuil plus tôt qu'attendu. Willison résume : sous 100 000 tokens, Haiku vaut le prix de Luna avec de meilleurs scores ; au-delà, Luna est plus avantageux.

Le troisième point est la verbosité. Les scores publiés sont obtenus à effort maximal. À l'effort medium, réglage par défaut, le score GDPval-AA chute de 1620 à 1277, et Artificial Analysis relève une consommation de tokens de sortie plus de quatre fois supérieure à la médiane à effort max. Le quatrième est l'écart entre crédit partiel et réussite stricte : 72,4 % sur OSWorld 2.1 en points de contrôle, 37,1 % en tâches entièrement réussies.

L'article corrige aussi une comparaison diffusée sur X qui plaçait Haiku 5.5 au niveau d'Opus 5 : les chiffres publiés par Anthropic et la system card le situent en dessous. Les témoignages de Cognition et de Rogo illustrent l'usage en sous-agent.

L'outil advisor de l'API permet à Haiku 5.5 d'exécuter une tâche en consultant un modèle plus fort comme Opus 5.5. Mais, sans prompt système qui impose la consultation, Anthropic a mesuré qu'aucun appel n'était fait sur 198 questions, alors que la présence de l'outil augmentait le coût de 12 %. L'advisor n'est disponible que sur l'API Claude et Claude Platform on AWS.

La migration depuis Haiku 4.5 comporte sept ruptures, dont la suppression de budget_tokens, du prefill et des réglages d'échantillonnage. Côté sécurité, la system card note une meilleure résistance aux injections de prompt mais davantage de sur-refus. SFEIR recommande de recompter les prompts, d'alerter avant 100 000 tokens, d'évaluer à l'effort déployé et de tester l'advisor avec une consigne explicite.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Claude Haiku 5.5 : ce que le nouveau Haiku change pour vos sous-agents | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Haiku 5.5 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Claude Haiku 5.5 | TECHNOLOGIE | remplace | Claude Haiku 4.5 | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Claude Haiku 5.5 | TECHNOLOGIE | concurrence | GPT-6 Luna | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Haiku 5.5 | TECHNOLOGIE | surpasse | GDPval-AA 1620 contre 1437 pour GPT-6 Luna (effort max) | MESURE | 0.85 | STATIQUE | déclaré_article |
| Claude Sonnet 5.5 | TECHNOLOGIE | surpasse | Terminal-Bench 4.0 : 70,6 % contre 39,2 % pour Haiku 5.5 | MESURE | 0.9 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | Sonnet 5.5 et Opus 5.5 pour le code agentique complexe | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Haiku 5.5 | TECHNOLOGIE | s_applique_à | sous-agent | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Claude Haiku 5.5 | TECHNOLOGIE | réduit | coût d'exploitation d'environ 75 % par rapport à Haiku 4.5 | MESURE | 0.82 | STATIQUE | déclaré_article |
| Simon Willison | PERSONNE | mesure | environ 1,25 fois plus de tokens que Haiku 4.5 sur un même prompt | MESURE | 0.85 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | 440 M de tokens de sortie contre une médiane de 100 M (« very verbose ») | MESURE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | OSWorld 72,4 % est un crédit partiel, la réussite stricte est de 37,1 % | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | s_oppose_à | Haiku 5.5 au niveau d'Opus 5 (comparaison diffusée sur X) | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| outil advisor | TECHNOLOGIE | s_applique_à | Claude Haiku 5.5 | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | mesure | 0 consultation de l'advisor sur 198 questions GPQA sans prompt système | MESURE | 0.88 | STATIQUE | déclaré_article |
| Cognition | ORGANISATION | utilise | Claude Haiku 5.5 | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Rogo | ORGANISATION | utilise | Claude Haiku 5.5 | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | alerter avant 100 000 tokens et évaluer au niveau d'effort déployé | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, éditeur de sfeir.com | AJOUT |
| Claude Haiku 5.5 | TECHNOLOGIE | catégorie | Petit modèle d'Anthropic (7 oct. 2026), 0,10 $ / 0,50 $ sous 100K tokens, contexte 1M | AJOUT |
| GPT-6 Luna | TECHNOLOGIE | catégorie | Petit modèle d'OpenAI (22 sept. 2026), 0,10 $ / 0,50 $, palier à 272K tokens | AJOUT |
| Claude Haiku 4.5 | TECHNOLOGIE | statut | Prédécesseur, 1 $ / 5 $, contexte 200K | AJOUT |
| outil advisor | TECHNOLOGIE | définition | Outil bêta de l'API Claude : l'exécutant consulte un conseiller plus capable dans la même requête | AJOUT |
| Artificial Analysis | ORGANISATION | rôle | Évaluateur indépendant (Intelligence Index, GDPval-AA) | AJOUT |
| Simon Willison | PERSONNE | rôle | Développeur et blogueur, mesure du tokenizer | AJOUT |
| Cognition | ORGANISATION | usage | Haiku 5.5 en « sidekick » dans Devin Fusion | AJOUT |
