---
themes: [economie-marche, architecture-construction]
source: SFEIR
---
# sfeir-cout-site-conversationnel-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, volet de la série sur le site conversationnel de sfeir.com consacré au coût. Mesure faite sur la préversion (**1 157 échanges** du 29 octobre au 13 novembre 2026, testeurs internes, réglages de production), aux prix catalogue Cloudflare lus le 14 novembre. **(1)** Une question rédigée coûte **0,135 centime de dollar**, dont **87 %** pour la rédaction par **Llama 3.3 70B** (2 901 jetons lus, 143 écrits) ; les passages lus en contexte pèsent près des trois quarts du coût de rédaction. Moyenne, cache compris (13,1 % de réponses servies par le cache) : **1,12 $ pour 1 000 échanges**. **(2)** Socle fixe : forfait **Workers Paid à 5 $/mois**, rendu nécessaire par les 8,4 millions de dimensions stockées dans Vectorize. **(3)** Projections mensuelles : ≈ 5 $ pour 1 000 questions, ≈ **12,66 $** pour 10 000, ≈ **112,96 $** pour 100 000. **(4)** Rapport d'échelle : les **2 302 $** de construction (équivalent API) paieraient environ **1,7 million** de questions. Le verdict : *« le fonctionnement est négligeable ; la dépense réelle est dans la construction et la tenue de la base de connaissances »*. L'article ne présente pas ses chiffres comme un tarif général.

## Titre Article

Combien coûte un site conversationnel : nos chiffres mesurés et leur méthode

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/cout-site-conversationnel-chiffres-mesures/

## Keywords

coût, FinOps, site conversationnel, coût par question, Workers AI, neurones, Llama 3.3 70B, Clef-flash, bge-m3, Cloudflare Vectorize, Workers Paid, allocation gratuite, cache, jetons lus, jetons écrits, prix catalogue, projection mensuelle, Analytics Engine, GraphQL, construction vs fonctionnement, achats, SFEIR

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article d'analyse de coûts, écrit par le cabinet sur son propre système. Public déclaré : DSI et achats, secondairement CTO.

**Style** : comptable et vérifiable — chaque montant est rattaché à une consommation mesurée (jetons, neurones, requêtes, millisecondes) et à une page de prix datée. Deux tableaux (coût par composant, projection mensuelle) et une figure. Les calculs intermédiaires sont donnés (prix par million de jetons, rapport lecture/écriture de 20 pour 1).

**Position épistémique** : méthode exposée en tête (trois sources croisées : Analytics Engine, API GraphQL de Cloudflare, pages de prix). Une section « ce que ces chiffres ne disent pas » : trafic interne de préversion, Workers AI ne distinguant pas les scripts (écart ~3 %), calcul par échange estimé, prix susceptibles de changer, coût humain hors facture. Les projections sont qualifiées comme telles.

## Pense-betes

- **Coût d'une question rédigée** : 0,135 ¢ — rédaction 0,117 ¢ (106,6 neurones), décision Clef-flash 0,015 ¢ (4 055 jetons lus), Vectorize 0,002 ¢, bge-m3 négligeable, cache/quotas/Worker/mesure < 0,001 ¢.
- **Grille Workers AI** : 0,011 $ les 1 000 neurones ; Llama 3.3 70B à 0,293 $/M jetons lus et 2,253 $/M jetons écrits. Le jeton écrit coûte ~8× plus, mais le modèle lit 20× plus qu'il n'écrit.
- **Cache** : une question déjà servie coûte ~0,0001 ¢ ; moyenne cache compris 0,112 ¢ par échange.
- **Préversion** : 935 réponses rédigées, 151 servies par le cache, 36 arrêtées sur la colonne (dont 35 pour dépassement des 5 s), 35 posées aux agents de page.
- **Socle** : Workers Paid 5 $/mois (10 M requêtes, 30 M ms inclus) ; 8 230 vecteurs × 1 024 dimensions = 8,4 M dimensions sous les 10 M inclus ; remplissage complet des index = 5,5 centimes. Allocation gratuite Workers AI : 10 000 neurones/jour, ~une centaine d'échanges.
- **Gratuits** : Cloudflare Pages, Turnstile, liaison de service Pages → Worker.
- **Projection** : 1 000 → ≈ 5 $ ; 10 000 → ≈ 12,66 $ ; 100 000 → ≈ 112,96 $ (≈ 129 $ sans cache).
- **Construction** : 23,2 h humaines, 56 h de Claude, 2 302 $ équivalent API ≈ 1,7 M questions. Repères internes : ~100 k€ (2021), ~1 000 € (2025). Non comptés : 90 appels à un modèle relecteur, illustrations.
- **Leviers** : modèle de rédaction (87 %), quantité de passages (moins de contexte = moins cher et moins bon), cache des questions suggérées, quotas et anti-robot contre l'abus.
- **Achats** : comparer les prix par million de jetons lus et écrits, pas « par conversation » ; la dépendance se concentre sur la plateforme d'exécution, le modèle étant remplaçable.

## RésuméDe400mots

Ce volet de la série sur sfeir.com chiffre le coût de fonctionnement du site conversationnel, composant par composant, et le compare au coût de sa construction. Il s'adresse aux DSI et aux acheteurs, et précise qu'il ne s'agit pas d'un tarif général mais des chiffres d'une architecture particulière.

Les mesures portent sur la préversion, qui tournait avec les réglages de production : 1 157 échanges entre le 29 octobre et le 13 novembre 2026, posés par l'équipe et des testeurs internes. Trois sources sont croisées : une ligne de mesure par échange, les compteurs d'usage de Cloudflare par modèle et par service, et les pages de prix consultées le 14 novembre. Les montants sont en dollars, hors taxes, au prix catalogue.

Une question qui reçoit une réponse rédigée coûte 0,135 centime de dollar. La rédaction par Llama 3.3 70B en représente 87 %. Le jeton écrit coûte près de huit fois plus que le jeton lu, mais le modèle lit vingt fois plus qu'il n'écrit : ce sont les passages fournis en contexte qui pèsent, la réponse limitée à 120 mots comptant peu. Le petit modèle de décision, la recherche vectorielle et le reste de l'infrastructure ajoutent des fractions négligeables. Une question servie par le cache coûte environ un millième de ce montant ; en moyenne, cache compris, mille échanges coûtent 1,12 dollar.

Le socle fixe se limite au forfait Workers Paid de 5 dollars par mois, rendu nécessaire par la taille des index vectoriels. L'hébergement des pages, le contrôle anti-robot et la liaison entre Pages et le Worker sont gratuits. Les projections mensuelles donnent environ 5 dollars pour mille questions, 12,66 dollars pour dix mille et 112,96 dollars pour cent mille.

La construction de la couche conversationnelle, mesurée dans un autre article de la série, aurait coûté 2 302 dollars en équivalent API, soit l'équivalent d'environ 1,7 million de questions rédigées. D'où le verdict : le fonctionnement est négligeable, la dépense réelle est dans la construction et l'entretien de la base de connaissances.

Les leviers de la facture sont identifiés : le choix du modèle de rédaction, la quantité de contexte, le cache et les quotas contre les usages abusifs. Les limites sont posées : trafic interne, attribution imparfaite des appels, prix datés, coût humain hors facture. Le conseil aux achats : comparer les prix par million de jetons lus et écrits plutôt qu'un prix par conversation.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article Combien coûte un site conversationnel | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Workers AI | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Llama 3.3 70B | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Cloudflare Vectorize | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | mesure | 0,135 centime de dollar par question rédigée, dont 87 % pour la rédaction | MESURE | 0.93 | STATIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | mesure | 1,12 $ pour 1 000 échanges, cache compris | MESURE | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | prédit | ≈ 12,66 $ par mois pour 10 000 questions, ≈ 112,96 $ pour 100 000 | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| Workers AI | TECHNOLOGIE | mesure | 0,011 $ les 1 000 neurones ; Llama 3.3 70B à 0,293 $/M jetons lus et 2,253 $/M écrits | MESURE | 0.88 | DYNAMIQUE | déclaré_article |
| cache des réponses | METHODOLOGIE | réduit | coût d'une question déjà posée à ~0,0001 centime | MESURE | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le fonctionnement est négligeable ; la dépense réelle est dans la construction et la tenue de la base de connaissances | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les passages lus en contexte font près des trois quarts du coût de rédaction | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | 2 302 $ de construction en équivalent API, soit ~1,7 million de questions rédigées | MESURE | 0.86 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | comparer les prix par million de jetons lus et écrits, pas par conversation | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | mesurer par échange dès le premier jour avec des prix datés | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| quotas et contrôle anti-robot | METHODOLOGIE | réduit | coût d'un usage abusif | CONCEPT | 0.84 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Workers AI | TECHNOLOGIE | tarification | En neurones, 10 000 gratuits par jour (prix lus le 14/11/2026) | AJOUT |
| agent conversationnel sfeir.com | TECHNOLOGIE | coût mesuré | 0,135 ¢ par question rédigée ; forfait Workers Paid 5 $/mois | AJOUT |
| cache des réponses | METHODOLOGIE | fonctionnement | Première question complète gardée 7 jours ; 13,1 % des échanges en préversion | AJOUT |
| quotas et contrôle anti-robot | METHODOLOGIE | rôle | Borner le coût d'un script qui ferait tourner le modèle sans limite | AJOUT |
