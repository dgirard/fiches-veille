---
themes: [outils-plateformes, economie-marche, qualite-securite]
source: SFEIR
---
# sfeir-openrouter-production-reglages-2026-10-12

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **12 octobre 2026** (~30 000 signes, 18 sources, extraits JSON). Il part de l'audit interne publié par **OpenRouter** le 28 septembre 2026 (**plus de 1 000 clés** d'API actives pour **85 employés**, dont **168** inutilisées) et donne l'ordre de configuration d'**OpenRouter** en production. (1) **Données d'abord** : `data_collection: "deny"` et `zdr: true`, applicables aussi au **BYOK** ; la résidence UE relève du plan Business (**8 %** contre **5,5 %**). (2) **Cache de préfixe** : le cache appartient au fournisseur, OpenRouter n'offre qu'un *« 10-minute best-effort pin »* via `session_id`, que cassent un changement de slug, un `provider.order` ou l'Auto Exacto. (3) **Coût** : `max_price` plutôt que `:floor`, **Batch API** à environ moitié prix, commission absente du prix affiché. (4) **Fallbacks** : la chaîne `models` se déclenche *« when a model returns an error, not when it returns a valid answer »*. (5) **Latence et clés** : `preferred_max_latency`, contrôles ajoutés à solde bas, Security Center. Complète, côté opérationnel, [[walker-onlycfo-ai-tokenomics-2026-10-22]].

## Titre Article

OpenRouter en production : cache, coûts, latence et données sous contrôle

## Date

2026-10-12

## URL

https://www.sfeir.com/articles/openrouter-production-bonnes-pratiques/

## Keywords

OpenRouter, production, routage LLM, politique de données, data_collection, zero data retention, ZDR, BYOK, résidence UE, cache de préfixe, prompt caching, session_id, routage collant, max_price, :floor, quantification, Batch API, commission, fallbacks, require_parameters, reproductibilité, latence, Security Center, gestion des clés, FinOps, RGPD

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, publiée sur sfeir.com (site éditorial de l'ESN).

## Ton

**Profil** : guide opérationnel destiné aux CTO, architectes, RSSI, DPO et équipes FinOps qui ont déjà retenu OpenRouter. Français technique, extraits JSON exacts, paramètres cités dans leur syntaxe d'origine.

**Style** : progression ordonnée (« par quoi commencer », puis cache, coût, fallbacks, latence, clés), chaque section terminée par une consigne. Les citations de documentation restent en anglais et en italique implicite (*« 10-minute best-effort pin »*, *« locks onto the cheapest endpoint »*). Une table « Les réglages en une page » résume dix paramètres avec leur piège ; une section « Ce qui casse en production » met en scène quatre incidents types (le `provider.order` posé « pour être sûr », le fallback qui ne vient pas, le `:floor` hérité du prototype, le solde à 6 $ un vendredi soir).

**Position épistémique** : sources presque toutes éditeur (documentation, blog, newsletter OpenRouter), qualifiées comme telles dans la bibliographie (« mesure de l'éditeur sur son propre trafic, non auditée », « chiffres de bêta autodéclarés »). Un retour terrain GitHub est signalé « non revérifié par SFEIR ». Les tarifs sont datés au jour de consultation. L'article renvoie à plusieurs pages du même site (trois métiers des LLM routers, marketplace OpenRouter, coût par outcome).

## Pense-betes

- **Point de départ** : audit OpenRouter du 28/09/2026 — **1 000+ clés actives pour 85 employés**, **168** inactives depuis des mois.
- **Données avant prix** : sans paramètre `provider`, n'importe quel hébergeur peut servir, y compris un qui conserve ou entraîne. `data_collection: "deny"` + `zdr: true`, par requête ou par compte, combinés en union. Par défaut côté fournisseurs, `data_collection` vaut `"allow"`.
- **Résidence** : routage régional UE/US réservé au plan **Business (8 %)** vs Standard (**5,5 %**) → 2,5 points à budgéter, et définition contractuelle de « in-region » à lire.
- **BYOK** : *« Your data policies apply to BYOK endpoints »* ; deux pièges — repli par défaut sur les endpoints OpenRouter (« Shared capacity fallback ») et dépense BYOK hors budgets tant que `include_byok_in_budgets` est désactivé.
- **Cache = fournisseur** : OpenRouter fait du routage collant vers l'endpoint qui détient le préfixe ; expiration après **10 min** d'inactivité ; `session_id` (256 caractères max) épingle dès la première requête réussie.
- **Préfixe à l'octet** : Anthropic *« 100% identical prompt segments »* ; minimum **512 tokens** (Fable 5.1, Opus 5.5, Sonnet 5.5, Haiku 5.5), **1 024** chez OpenAI dès GPT-5.6 ; modifier une définition d'outil invalide tout le cache. Horodatage, ordre d'outils variable, identifiant en tête = cache perdu.
- **Ce qui casse l'épinglage** : changer de slug, poser `provider.order`, Auto Exacto sur requêtes avec outils. `openrouter:tool_search` + `defer_loading: true` sort les définitions d'outils du préfixe.
- **Chiffres éditeur** : jusqu'à **80-90 %** de réduction du prefill ; sans cache, 20 000-90 000 tokens/tour = **5-10 s** de prefill. Taux de cache médian par fournisseur : **44 %** (janv. 2026) → **85 %** (sept.) ; DeepSeek ~**96 %**.
- **Coût** : routage par défaut pondéré par l'inverse du carré du prix ; `:floor` verrouille l'endpoint le moins cher (souvent quantifié FP8/FP4) → hors ligne seulement ; en production, `max_price` fait échouer plutôt que dépasser.
- **Batch API** (22/09/2026) : ~**50 %** du prix, fenêtre 24 h ; bêta : 230 000+ batches, médiane **7 min**, p99 10,3 h ; un fournisseur par batch.
- **Commission** : 5,5 % (min 0,80 $), 8 % Business, 5 % crypto ; BYOK gratuit jusqu'à **25 000 $/mois**, puis 5 %.
- **Fallbacks** : sur erreur uniquement, jamais sur réponse médiocre ; un HTTP 200 peut porter une erreur → tester le JSON ; `require_parameters: true` pour les sorties structurées.
- **Reproductibilité** : `provider.only` + `allow_fallbacks: false` (réglage d'eval) ; éviter les alias `-latest`.
- **Latence** : `preferred_max_latency` (fenêtre 5 min, préférence souple) ; caches de bord froids 1-2 min ; contrôles supplémentaires quand le solde tombe à quelques dollars.
- **Recommandation CTO** : un wrapper d'une cinquantaine de lignes, versionné, appels directs interdits.

## RésuméDe400mots

L'article, signé SFEIR AI, s'adresse aux équipes qui ont déjà choisi OpenRouter comme marketplace de modèles et doivent le passer en production. Il s'ouvre sur l'audit interne publié par l'éditeur le 28 septembre 2026 : plus de 1 000 clés d'API actives pour 85 employés, dont 168 inutilisées depuis des mois. Les réglages par défaut, explique le texte, sont ceux d'un bac à sable, et l'article propose un ordre de configuration.

Premier poste, la politique de données. Une requête sans paramètre `provider` peut être servie par un hébergeur qui conserve ou entraîne sur les prompts. Les clés `data_collection: "deny"` et `zdr: true` ferment cette porte, y compris pour les clés apportées par le client (BYOK). La résidence européenne relève du plan Business, facturé 8 % contre 5,5 %. Deux réglages BYOK sont signalés : le repli par défaut sur les endpoints d'OpenRouter et l'exclusion de la dépense BYOK des budgets.

Deuxième poste, le cache de préfixe, présenté comme le lieu où se joue la facture. Le cache appartient au fournisseur d'inférence ; OpenRouter ne fait que ramener les requêtes vers le même endpoint pendant dix minutes, au mieux, via un `session_id`. Changer de slug, fixer `provider.order` ou laisser l'Auto Exacto changer de fournisseur casse cet épinglage. Côté prompt, le préfixe doit être identique à l'octet, au-dessus d'un minimum de 512 tokens chez Anthropic et 1 024 chez OpenAI. Les chiffres de l'éditeur : jusqu'à 80 à 90 % de réduction du prefill, et un taux de cache médian passé de 44 % à 85 % entre janvier et septembre 2026.

Troisième poste, le coût. Le suffixe `:floor` verrouille l'endpoint le moins cher, souvent quantifié ; l'article lui préfère un plafond `max_price`. La Batch API, lancée le 22 septembre, facture environ la moitié du prix avec une fenêtre de 24 heures. La commission (5,5 %, 8 % ou 5 % en cryptomonnaie, BYOK gratuit jusqu'à 25 000 $ par mois) doit entrer dans toute comparaison avec un proxy LiteLLM auto-hébergé.

Quatrième poste, les fallbacks : la chaîne `models` réagit aux erreurs, jamais à une réponse valide mais fausse, et un HTTP 200 peut contenir une erreur. L'escalade relève du code applicatif ; `require_parameters` restreint le routage aux endpoints qui honorent le format demandé. La reproductibilité exige `provider.only` sans fallbacks.

Enfin, la latence se borne par `preferred_max_latency`, et le Security Center signale les clés sans plafond, sans expiration ou inactives. L'article conclut par des consignes par rôle : wrapper unique pour les CTO, périmètre contractuel pour RSSI et DPO, trois chiffres (commission, seuil BYOK, taux de cache) pour le FinOps.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | OpenRouter en production : cache, coûts, latence et données sous contrôle | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| OpenRouter en production : cache, coûts, latence et données sous contrôle | DOCUMENT | référence | OpenRouter | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| OpenRouter | ORGANISATION | mesure | plus de 1 000 clés d'API actives pour 85 employés, dont 168 inutilisées | MESURE | 0.92 | STATIQUE | déclaré_article |
| OpenRouter | TECHNOLOGIE | utilise | routage collant | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| routage collant | CONCEPT | permet | prompt caching | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| prompt caching | CONCEPT | réduit | jusqu'à 80 à 90 % du temps et du coût de prefill | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| OpenRouter | ORGANISATION | mesure | taux de cache médian par fournisseur de 44 % (janv. 2026) à 85 % (sept. 2026) | MESURE | 0.85 | STATIQUE | déclaré_article |
| Zero Data Retention | CONCEPT | s_applique_à | BYOK | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| OpenRouter Batch API | TECHNOLOGIE | fait_partie_de | OpenRouter | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| OpenRouter Batch API | TECHNOLOGIE | réduit | environ 50 % du prix par token, fenêtre de 24 h | MESURE | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | préférer un plafond max_price au suffixe :floor en production | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les fallbacks se déclenchent sur erreur, jamais sur une réponse valide mais médiocre | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| OpenRouter Security Center | TECHNOLOGIE | fait_partie_de | OpenRouter | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| OpenRouter | TECHNOLOGIE | concurrence | LiteLLM | TECHNOLOGIE | 0.8 | DYNAMIQUE | inféré |
| Stripe | ORGANISATION | collabore_avec | OpenRouter | ORGANISATION | 0.78 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | encapsuler les réglages OpenRouter dans un wrapper versionné et interdire les appels directs | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| OpenRouter | TECHNOLOGIE | catégorie | Marketplace et routeur de modèles LLM (rachat par Stripe non clôturé au 8 octobre 2026) | AJOUT |
| routage collant | CONCEPT | définition | Renvoi des requêtes d'un même fil vers l'endpoint qui détient le préfixe en cache, 10 min best-effort | AJOUT |
| OpenRouter Batch API | TECHNOLOGIE | lancement | 22 septembre 2026 ; un fournisseur par batch, hors audio/vidéo/recherche web | AJOUT |
| OpenRouter Security Center | TECHNOLOGIE | fonction | Détection des clés sans plafond, sans expiration ou inactives depuis plus de 90 jours | AJOUT |
| Zero Data Retention | CONCEPT | paramètre | zdr: true, par requête, groupe de modèles ou compte | AJOUT |
| BYOK | CONCEPT | tarif | 25 000 $ d'inférence par mois sans frais, puis 5 % du prix catalogue | AJOUT |
