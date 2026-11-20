---
themes: [produits-services, qualite-securite]
source: SFEIR
---
# sfeir-chatgpt-wallet-openai-paiement-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, deux jours après le lancement de **ChatGPT Wallet** par **OpenAI** (13 novembre 2026). Public déclaré : DSI, RSSI, responsables e-commerce. **(1)** Le fonctionnement : les **dots**, agents de ChatGPT présentés fin septembre, remplissent le panier et paient pour l'utilisateur ; chaque achat est validé par **Face ID, Touch ID** ou empreinte ; le réseau de cartes fournit un **jeton de paiement**, si bien que ni l'agent ni le marchand ne voient le vrai numéro. **(2)** Un lancement étroit : abonnés **ChatGPT Pro** résidant aux États-Unis, cartes de crédit américaines (American Express, Chase, Mastercard, Visa), Wallet exclu de Chat, Work et Codex. **(3)** Côté marchands, aucune intégration propre, mais une configuration antifraude pour reconnaître les requêtes signées **Web Bot Auth** ; partenaires Forter, Riskified, Sardine, Signifyd, Adyen, Checkout.com, Stripe. **(4)** L'étape annoncée : la délégation sous plafonds, déjà prévue par les conditions du service. L'article la rapproche de la grille de l'**ANSSI** (exécution autonome / approbation obligatoire / action interdite). Rejoint, côté infrastructure, [[cloudflare-wallets-agentic-commerce-2026-08-04]].

## Titre Article

ChatGPT Wallet : les agents d'OpenAI passent à la caisse, l'humain signe chaque achat

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/chatgpt-wallet-agents-openai-paiement/

## Keywords

ChatGPT Wallet, OpenAI, dots, agents IA, commerce agentique, agentic commerce, paiement par agent, jeton de paiement, tokenisation, validation biométrique, Face ID, Touch ID, Web Bot Auth, antifraude, en-tête Forwarded, ChatGPT Pro, American Express, Stripe, Adyen, délégation sous plafonds, ANSSI, approbation humaine, trafic des bots, Cloudflare

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article d'actualité commentée, publié deux jours après l'annonce, sur le site d'un cabinet. Public : DSI, RSSI, responsables e-commerce, notamment français.

**Style** : informatif et procédural — le parcours d'un achat est décrit étape par étape à partir de la documentation d'OpenAI (annonce, centre d'aide, conditions du service, documentation développeurs). Le texte traduit la portée pour une entreprise française (service inaccessible aux salariés, mais concernant tout site vendant à des clients américains).

**Position épistémique** : huit sources numérotées, dont quatre documents d'OpenAI, CNBC, Tom's Hardware, Forbes et l'ANSSI. Les chiffres de trafic sont qualifiés (mesure de requêtes sur le réseau Cloudflare, base de comparaison non publiée pour les +1 700 %). Section « limites » : déploiement progressif, aucun chiffre d'usage publié, achats pas toujours aboutis. Le texte renvoie en fin de parcours à l'offre FDE du cabinet.

## Pense-betes

- **Lancement** : 13 novembre 2026. Les dots paient chez le marchand pour l'utilisateur ; chaque achat validé biométriquement.
- **Écran de validation** (conditions du service) : marchand, articles et quantités, prix total ou maximum (taxes, frais, livraison), carte, éventuel prélèvement récurrent, acompte ou autorisation en attente. Si un détail important change, nouvelle demande d'accord.
- **Jeton de carte** : numéro, code et date de substitution fournis par le réseau ; valable pour la seule transaction approuvée, sauf abonnement consenti.
- **Rôles** : OpenAI n'est ni banque, ni émetteur, ni réseau, ni marchand ; le marchand garde relation client, prix, livraison, retours, décision antifraude. Pas de commission au lancement (CNBC).
- **Éligibilité** : ChatGPT Pro, résidents américains de 18 ans et plus, cartes de crédit émises aux États-Unis ; débit et cartes virtuelles refusées ; uniquement dans les conversations avec un dot.
- **Marchands** : achats depuis le navigateur cloud de ChatGPT, risque de blocage par l'antifraude ; configurer CDN/pare-feu pour **Web Bot Auth** ; signaux utilisateur transmis dans l'en-tête HTTP `Forwarded`.
- **American Express** (Luke Gebb) : première intégration de ses « Agentic Commerce Experiences ».
- **Trafic** : Matthew Prince (3 juin 2026) — les bots dépassent le trafic humain (57,5 % contre 42,5 % des requêtes HTTP sur Cloudflare) ; Forbes (1er octobre) — requêtes d'agents IA +1 700 % en un an.
- **Étape suivante** : délégation sous plafond, catégories, période ; non disponible, mais déjà prévue par les conditions en vigueur depuis le 12 novembre.
- **Grille ANSSI** (*Sécuriser un système IA agentique*, v1.0) : classer chaque action en autonome / approbation obligatoire / interdite ; montrer l'action exacte à l'approbateur ; garder l'approbation hors de portée de l'agent. Wallet place aujourd'hui tout paiement dans la deuxième catégorie.

## RésuméDe400mots

Le 13 novembre 2026, OpenAI a lancé ChatGPT Wallet, qui permet aux dots, les agents de ChatGPT présentés fin septembre, de payer chez un marchand pour le compte de l'utilisateur. SFEIR décrit le fonctionnement du service et ses effets pour les DSI, les RSSI et les responsables e-commerce.

L'utilisateur enregistre sa carte une fois dans un formulaire sécurisé, hors de la conversation. Lorsqu'il demande à son dot d'acheter un produit ou de réserver un hôtel, celui-ci présente une demande d'achat qui affiche le marchand, les articles, le prix total ou maximum, la carte et les éventuels prélèvements récurrents. L'utilisateur approuve par Face ID, Touch ID ou empreinte. Le réseau de cartes fournit alors un jeton de paiement de substitution : ni l'agent ni le marchand ne voient le vrai numéro. Si un détail change avant la commande, l'accord est redemandé. OpenAI précise qu'il n'est ni banque, ni émetteur, ni marchand, et que le marchand garde la relation client.

Le lancement est étroit : abonnés ChatGPT Pro résidant aux États-Unis, avec une carte de crédit américaine. Wallet ne fonctionne que dans les conversations avec un dot. Une entreprise française n'y a donc pas accès pour ses salariés, mais tout site vendant à des clients américains est concerné.

Pour les marchands, aucune intégration spécifique n'est requise, le jeton passant dans les pages de paiement existantes. La difficulté vient de l'antifraude : le dot achète depuis un navigateur cloud que les outils de détection peuvent prendre pour un robot. OpenAI demande de reconnaître les requêtes signées avec Web Bot Auth et transmet des signaux sur l'utilisateur dans un en-tête HTTP. Des spécialistes de la fraude et des prestataires de paiement, dont Stripe et Adyen, sont associés. L'article cite aussi Cloudflare, selon qui les bots ont dépassé le trafic humain en juin 2026.

OpenAI annonce l'étape suivante : une délégation complète des achats dans des limites fixées par l'utilisateur, déjà prévue par les conditions du service mais pas encore ouverte. SFEIR la rapproche du guide de l'ANSSI, qui demande de classer chaque action d'un agent en exécution autonome, approbation obligatoire ou action interdite. Wallet range aujourd'hui tout paiement dans la deuxième catégorie ; les plafonds en feront passer une partie dans la première. L'article conseille aux DSI d'opérer ce classement pour leurs propres agents. Il signale ses limites : déploiement progressif, absence de chiffres d'usage, achats qui n'aboutissent pas toujours.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| OpenAI | ORGANISATION | publie | ChatGPT Wallet | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| ChatGPT Wallet | TECHNOLOGIE | fait_partie_de | ChatGPT | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| ChatGPT Wallet | TECHNOLOGIE | utilise | dots | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| ChatGPT Wallet | TECHNOLOGIE | utilise | jeton de paiement | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| ChatGPT Wallet | TECHNOLOGIE | utilise | Web Bot Auth | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| ChatGPT Wallet | TECHNOLOGIE | utilise | validation biométrique | METHODOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | collabore_avec | Stripe | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | collabore_avec | Adyen | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | collabore_avec | American Express | ORGANISATION | 0.86 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | prédit | délégation des achats sous plafond de dépense, catégories et période | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| ANSSI | ORGANISATION | publie | Sécuriser un système IA agentique | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Sécuriser un système IA agentique | DOCUMENT | recommande | classer chaque action d'un agent en exécution autonome, approbation obligatoire ou action interdite | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Matthew Prince | PERSONNE | affirme_que | les bots ont dépassé le trafic humain en ligne (57,5 % des requêtes HTTP sur Cloudflare) | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Matthew Prince | PERSONNE | dirige | Cloudflare | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | classer les actions de ses propres agents avant que l'outil ne propose de le faire | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| ChatGPT Wallet | TECHNOLOGIE | s_applique_à | commerce agentique | CONCEPT | 0.9 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| ChatGPT Wallet | TECHNOLOGIE | lancement | 13 novembre 2026 ; ChatGPT Pro, États-Unis, cartes de crédit américaines | AJOUT |
| dots | TECHNOLOGIE | définition | Agents de ChatGPT présentés fin septembre 2026 | AJOUT |
| Web Bot Auth | TECHNOLOGIE | rôle | Signature des requêtes d'agents pour les faire reconnaître par l'antifraude des marchands | AJOUT |
| Sécuriser un système IA agentique | DOCUMENT | référence | ANSSI, collection Les Essentiels, version 1.0 | AJOUT |
| ANSSI | ORGANISATION | secteur | Agence nationale de la sécurité des systèmes d'information (France) | AJOUT |
