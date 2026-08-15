# Knowledge Base — Commerce Agentique (UCP/ACP)

> 14 fiches | Période : Février 2025 — Août 2026 | Généré le 2026-08-15

## Vue d'ensemble

Cette KB thématique couvre l'émergence du **commerce agentique** : la transformation du e-commerce par les agents IA, depuis les premiers signaux d'adoption consommateur jusqu'aux protocoles techniques (ACP d'OpenAI/Stripe, UCP de Google adossé à AP2) qui standardisent les interactions agent-marchand. Elle intègre aussi le **contre-courant des protocoles ouverts** (x402, mpp) fondés sur les micropaiements en stablecoins, qui critique les plateformes fermées ACP/UCP comme des « jardins clos » et anticipe la fin du modèle publicitaire face à des agents non distractibles.

**Le printemps-été 2026 déplace la bataille du checkout vers le portefeuille.**
Trois faits, dans cet ordre :

1. **Stripe — co-auteur d'ACP — contourne son propre protocole** (29 avr. 2026).
   Le portefeuille Link pour agents est bâti sur les rails **carte existants**,
   au motif explicite que *« machine payments protocols are still gaining
   adoption »*. Le pari sur les protocoles machine-natifs est reporté ; le
   produit livré est un **contournement**.
2. **Cloudflare prend l'autre camp** (4 août 2026) : Wallets s'adosse à **x402**
   et au **stablecoin**, hors des réseaux de cartes — et ajoute la pièce que
   personne n'avait posée, l'**identité de l'agent** (espace de noms
   `cloudflare.pay`, Web Bot Auth, Turnstile). Réserve : à la date de
   l'annonce, seule la **réservation d'un handle** existe.
3. **L'autorisation déléguée reste le nœud non résolu.** Stripe exige une
   approbation humaine **transaction par transaction** ; Cloudflare répond par
   des **plafonds** avec un argument contre-intuitif — *« si un agent est
   responsable de 10 $, vous vous inquiétez moins que s'il l'est de 1 000 $ »* :
   la limite n'est pas ce qui bride l'autonomie, c'est ce qui la rend
   **consentable**.

**Avertissement de nommage, valable pour toute lecture de ce corpus** : le sigle
**ACP** désigne **trois protocoles sans intersection technique** — *Agentic
Commerce Protocol* (agent ↔ marchand, OpenAI + Stripe), *Agent Client Protocol*
(client ↔ agent, Zed) et *Agent Communication Protocol* (agent ↔ agent, IBM
Research). Dans cette KB, **ACP = Agentic Commerce Protocol** et rien d'autre.
La collision a déjà produit une erreur d'attribution dans le graphe de veille
lui-même (cf. fiche Girard, août 2026) : **on n'indexe jamais un sigle seul**.

## Chronologie

### 2025 — Signaux d'émergence

- **Fév. 2025** — Graphite.io théorise le passage du SEO au AEO (Answer Engine Optimization)
- **Sep. 2025** — Google publie le Agent Payments Protocol (AP2) sur GitHub
- **Oct. 2025** — 73% des consommateurs utilisent déjà l'IA pour leurs achats (étude Riskified)
- **Oct. 2025** — ChatGPT Atlas lance le web conversationnel avec e-commerce intégré
- **Nov. 2025** — Shopify mesure un trafic IA ×7 et des commandes ×11 depuis janvier
- **Nov. 2025** — Barron Ernst analyse l'essor du commerce directement dans ChatGPT

### 2026 — Protocoles et standardisation

- **Jan. 2026** — Google annonce le Universal Commerce Protocol (UCP) au NRF 2026, Carrefour premier européen
- **Fév. 2026** — Wayfair et Etsy utilisent UCP en production. Nicolas Marette publie le guide technique ACP/UCP
- **Fév. 2026** — Max Thilén (Opascope) publie le guide de référence ACP vs UCP : 900M utilisateurs ChatGPT Instant Checkout, absence stratégique Amazon, crise attribution, triptyque Amazon/Google/OpenAI
- **Mars 2026** — Sam Ragsdale (Merit Systems) qualifie ACP/UCP d'« AOL du commerce agentique » et défend les protocoles ouverts x402 (Coinbase) et mpp (Tempo + Stripe) : micropaiements stablecoins sub-cent, 2000+ agents sur AgentCash 10 jours après lancement

### Avril-août 2026 — Le portefeuille agentique, et la question de l'autorisation

- **29 avr. 2026** — **Stripe** lance le **portefeuille Link pour les agents** et
  **Issuing for agents** (Stripe Sessions 2026). Flux **OAuth** d'accès au
  portefeuille, puis *spend request* → **carte à usage unique** ou **Shared
  Payment Token** ; *« The agent never gets access to your raw payment
  credentials »*. Justificatif **scopé** (montant, devise, marchand) et
  **contexte de transaction** obligatoire pour que l'humain comprenne ce qu'il
  approuve. **Approbation humaine à chaque transaction** ; limites de dépense et
  agents autonomes sont **annoncés, pas livrés**. Distribution : Link revendique
  **200 M+ de consommateurs**.
- **2 août 2026** — **Didier Girard** démêle le sigle **ACP** : trois protocoles,
  aucune intersection. Le cœur de la note est l'échec constaté de sa propre base
  de veille (douze résultats, tous sur le protocole de commerce, zéro sur celui
  de Zed) et la règle qui en découle : **« on n'indexe jamais un sigle seul »**.
- **4 août 2026** — **Cloudflare Wallets** (Agents Week) : **Account Wallets**
  (humains) et **Virtual Wallets** (agents, par clé d'API, plafond fixé par le
  détenteur du compte) ; garde-fous **allocation / allowlist / montant maximal
  par transaction** ; rail **x402** et **stablecoin** ; identité d'agent via
  l'espace de noms **`cloudflare.pay`**. ⚠️ Presque tout est **au futur** : à la
  date de l'annonce, seule la réservation d'un handle est effective.
- **6 août 2026** — **Block** publie son T2 et assume ne pas savoir **comment
  facturer l'IA** (Dorsey : *« we can experiment with a number of models »*).
  Le fait marquant est ailleurs : la valeur est **encaissée par la structure de
  coûts avant de l'être par le prix** (~4 000 postes supprimés six mois plus
  tôt, profit brut +25 %, résultat net −83 % sous l'effet des indemnités). Côté
  commerce : **Moneybot** (Cash App, 1 M+ comptes actifs hebdo), **Managerbot**
  (Square) et **Square dans Google Maps** avec une expérience conversationnelle
  de découverte-commande. Les quatre voies de monétisation listées par Evercore
  ISI (bundles SaaS, abonnements, offres entreprise, usage) **n'en comptent
  aucune indexée sur le résultat**.

## Fiches sources

### Portefeuilles et autorisation de paiement agentique

- [[fiches/2026-04/hill-stripe-link-wallet-agents-issuing-2026-04-29\|Giving agents the ability to pay (Stripe) : portefeuille Link pour agents, Issuing for agents, approbation transaction par transaction]]
- [[fiches/2026-08/cloudflare-wallets-agentic-commerce-2026-08-04\|Cloudflare Wallets : Virtual Wallets pour agents, rail x402/stablecoin et espace de noms cloudflare.pay]]
- [[fiches/2026-08/paymentsdive-block-dorsey-pricing-ia-2026-08-06\|Block explores how to price AI : la monétisation par les coûts avant le prix, Moneybot/Managerbot, Square dans Google Maps]]

### Protocoles et guides ACP / UCP

- [[fiches/2026-03/ragsdale-merit-open-agentic-commerce-protocols-2026-03-19\|Commerce agentique ouvert : protocoles x402/mpp, micropaiements stablecoins, fin du modèle publicitaire]]
- [[fiches/2026-02/thilen-opascope-ai-shopping-assistant-agentic-commerce-protocols-2026-02-10\|AI Shopping Assistant Guide 2026 : ACP vs UCP, Amazon absent, attribution agentique, feed produit IA]]
- [[fiches/2026-02/marette-agentic-commerce-optimization-acp-ucp-2026-02-23\|Agentic Commerce Optimization : guide technique préparation protocoles ACP et UCP Google]]
- [[fiches/2026-01/nrf-2026-commerce-agentique-ucp-deep-research-2026-01-13\|NRF 2026 - Universal Commerce Protocol Google, commerce agentique, Carrefour premier européen, Stripe ACS]]
- [[fiches/2025-09/google-agentic-commerce-ap2-payment-protocol-2025-09-16\|Agent Payments Protocol (AP2) - Google Agentic Commerce - Secure payments]]
- [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport — désambiguïsation et règle « on n'indexe jamais un sigle seul »]]

### Adoption et signaux marché

- [[fiches/2025-11/shopify-ai-traffic-orders-growth-techcrunch-2025-11-04\|Shopify - Croissance IA - Traffic 7x - Commandes 11x - Commerce agentique]]
- [[fiches/2025-10/novik-ai-online-shopping-consumers-2025-10-26\|73% consommateurs utilisent IA pour achats en ligne, confiance équivalente vendeurs humains]]
- [[fiches/2025-11/barron-ernst-rise-of-commerce-chatgpt-2025-11-08\|L'essor du commerce sur ChatGPT]]
- [[fiches/2025-10/rafal-chatgpt-atlas-web-conversationnel-2025-10-22\|Web conversationnel, ChatGPT Atlas, e-commerce conversationnel]]

### Visibilité et découverte IA

- [[fiches/2025-02/graphite-aeo-is-the-new-seo-2025-02-01\|AEO (Answer Engine Optimization) - SEO - Moteurs de réponse IA]]

## Entités clés

### Protocoles et technologies

- [[kb/Universal-Commerce-Protocol\|Universal Commerce Protocol (UCP)]] — Protocole commerce agentique Google (annoncé jan. 2026)
- [[kb/Agentic-Commerce-Protocol\|Agentic Commerce Protocol (ACP)]] — Protocole commerce agentique OpenAI/Stripe, live sept. 2025, 4% commission
- [[kb/_entites-mineures#ChatGPT-Instant-Checkout\|ChatGPT Instant Checkout]] — Checkout agentique sans visite site, 900M utilisateurs hebdomadaires
- [[kb/_entites-mineures#Rufus-AI\|Rufus AI]] — Assistant IA shopping in-app Amazon, 300M utilisateurs, +60% conversion
- [[kb/_entites-mineures#Alexa+\|Alexa+]] — Commerce vocal automatisé Amazon
- [[kb/AP2\|AP2]] — Agent Payments Protocol, prédécesseur
- [[kb/_entites-mineures#Merchant-Center\|Merchant Center]] — Plateforme catalogue Google
- schema.org — Données structurées, socle des ontologies commerce
- OAuth 2.0 — Liaison identité agent-utilisateur
- [[kb/_entites-mineures#WordLift\|WordLift]] — Outil SEO sémantique et diffusion visuelle
- [[kb/AEO\|AEO]] — Answer Engine Optimization
- [[kb/_entites-mineures#x402\|x402]] — Protocole de paiement agentique ouvert (Coinbase), basé sur le code HTTP 402
- [[kb/_entites-mineures#mpp\|mpp]] — Protocole de micropaiement ouvert (Tempo + Stripe)
- [[kb/_entites-mineures#AgentCash\|AgentCash]] — Balance unique + découverte marchands pour agents (x402scan.com, mppscan.com)
- [[kb/_entites-mineures#HTTP-402\|HTTP 402]] — Code « Payment Required » créé en 1997, jamais implémenté faute de micropaiements viables
- [[kb/_entites-mineures#Stablecoins\|Stablecoins]] — Coûts de transaction sub-cent, socle des micropaiements agentiques
- [[kb/Link-wallet-for-agents\|Link (portefeuille pour agents)]] — Portefeuille Stripe accessible à un agent par OAuth ; 200 M+ de consommateurs revendiqués
- [[kb/_entites-mineures#Issuing-for-agents\|Issuing for agents]] — Brique d'infrastructure Stripe : cartes virtuelles à usage unique, contrôles de dépense et antifraude à l'autorisation, pour bâtir son propre portefeuille agentique
- [[kb/_entites-mineures#Shared-Payment-Token\|Shared Payment Token]] — Justificatif de paiement **scopé** (montant, devise, marchand) délivré à l'agent sans jamais exposer les identifiants bruts
- [[kb/Cloudflare-Wallets\|Cloudflare Wallets]] — Account Wallets (humains) + Virtual Wallets (agents, par clé d'API), rail x402/stablecoin
- [[kb/_entites-mineures#Virtual-Wallet\|Virtual Wallet]] — Portefeuille d'agent à plafond fixé par le détenteur du compte (allocation, allowlist, montant max par transaction)
- [[kb/_entites-mineures#cloudflare.pay\|cloudflare.pay]] — Espace de noms lisible donnant à un agent une **identité stable** face au marchand (`research.example.cloudflare.pay`)
- [[kb/_entites-mineures#Web-Bot-Auth\|Web Bot Auth]] / Turnstile — Briques d'identité et de vérification Cloudflare réutilisées pour authentifier l'agent payeur
- [[kb/Agent-Client-Protocol\|Agent Client Protocol]] — **Homonyme d'ACP à ne pas confondre** : client ↔ agent (Zed, JSON-RPC sur stdio) ; sans rapport avec le commerce agentique
- [[kb/_entites-mineures#Moneybot\|Moneybot]] (Cash App) / [[kb/_entites-mineures#Managerbot\|Managerbot]] (Square) — Agents grand public et marchands de Block ; 1 M+ de comptes actifs hebdo pour Moneybot

### Organisations

- [[kb/Google\|Google]] — Créateur UCP/ACP/AP2
- [[kb/Shopify\|Shopify]] — Trafic IA ×7, commandes ×11
- [[kb/OpenAI\|OpenAI]] — ChatGPT Atlas, Instant Checkout, ACP co-créateur
- [[kb/Amazon\|Amazon]] — Rufus AI, Alexa+, Buy for Me, absent des protocoles ouverts
- [[kb/_entites-mineures#Opascope\|Opascope]] — Cabinet conseil e-commerce agentique
- [[kb/_entites-mineures#Wayfair\|Wayfair]] — Premier utilisateur UCP
- [[kb/_entites-mineures#Etsy\|Etsy]] — Premier utilisateur UCP
- [[kb/_entites-mineures#Carrefour\|Carrefour]] — Premier européen UCP (NRF 2026)
- [[kb/Stripe\|Stripe]] — Agent Commerce Service (ACS), co-créateur du protocole mpp avec Tempo
- [[kb/_entites-mineures#Custplace\|Custplace]] — Preuve sociale tierce pour LLMs
- [[kb/_entites-mineures#Merit-Systems\|Merit Systems]] — Infrastructure commerce agentique ouvert (AgentCash)
- [[kb/Cloudflare\|Cloudflare]] — Wallets, `cloudflare.pay`, Web Bot Auth ; parie sur x402 et le stablecoin plutôt que sur les réseaux de cartes
- [[kb/Block\|Block]] — Cash App / [[kb/_entites-mineures#Square\|Square]] ; Moneybot et Managerbot déployés **avant** d'avoir choisi un modèle de prix ; Square intégré à Google Maps

### Personnes

- [[kb/_entites-mineures#Nicolas-Marette\|Nicolas Marette]] — Guide technique ACP/UCP
- [[kb/_entites-mineures#Barron-Ernst\|Barron Ernst]] — Commerce sur ChatGPT
- [[kb/Olivier-Rafal\|Olivier Rafal]] — Web conversationnel
- [[kb/_entites-mineures#Max-Thilén\|Max Thilén]] — Guide référence ACP vs UCP (Opascope)
- [[kb/_entites-mineures#Sam-Ragsdale\|Sam Ragsdale]] — Manifeste commerce agentique ouvert (Merit Systems)
- [[kb/_entites-mineures#Dan-Hill\|Dan Hill]] — Product Manager Link Consumer Product (Stripe) ; auteur de « Giving agents the ability to pay »
- [[kb/_entites-mineures#Will-Papper\|Will Papper]] — Auteur de l'annonce Cloudflare Wallets (Agents Week)
- [[kb/Jack-Dorsey\|Jack Dorsey]] — Block ; « nous pouvons expérimenter plusieurs modèles » de tarification de l'IA
- [[kb/Didier-Girard\|Didier Girard]] — Désambiguïsation du sigle ACP et règle d'indexation associée

## Concepts structurants

### Architecture UCP — 6 capacités

1. **Découverte produit** pour agents IA
2. **Gestion panier** avec règles de prix complexes
3. **Liaison identité** via OAuth 2.0
4. **Checkout** sécurisé
5. **Gestion commandes** via webhooks
6. **Extensions verticales** (voyage, services, biens numériques, hôtellerie)

### Chaîne de valeur commerce agentique

```
Visibilité (AEO/schema.org)
  → Découverte (agents IA interrogent catalogues)
    → Sélection (preuve sociale, attributs conversationnels)
      → Transaction (UCP/ACP checkout + OAuth 2.0)
        → Post-achat (webhooks, fidélité, support)
```

### Jardins clos vs protocoles ouverts (débat Ragsdale, mars 2026)

- **Parallèle historique** : AOL (jardin clos, bundle curé) vs Mosaic/HTTP (protocoles ouverts) — AOL a semblé gagner (fusion Time Warner $350Md), puis les protocoles ouverts l'ont emporté
- **« Checkout in ChatGPT is the AOL of agentic commerce »** : ACP/UCP vus comme des plateformes fermées, culs-de-sac pour l'innovation venue des marges
- **La pub ne fonctionne plus** : les agents IA ne sont pas distractibles ; même les jardins clos (Facebook, TikTok) sont percés par les agents computer-use qui imitent le trafic humain
- **x402 (Coinbase) et mpp (Tempo + Stripe)** : 28 ans après l'invention du code HTTP 402 (Berners-Lee, 1997), les stablecoins rendent enfin les micropaiements viables — paiement sans accord commercial préalable, sans whitelist
- **Les skills comme artefact transitionnel** : les agents modernes découvrent une API inconnue, lisent son schéma et l'utilisent sans entraînement préalable

### Le portefeuille agentique : deux camps, un même nœud

La couche disputée n'est plus le **checkout** (ACP/UCP) mais le **portefeuille**
— qui détient les fonds, qui autorise la dépense, et sous quelle identité.

| | **Stripe — Link pour agents** (29 avr. 2026) | **Cloudflare Wallets** (4 août 2026) |
|---|---|---|
| **Rail** | Cartes et comptes bancaires **existants** | **x402** + **stablecoin** |
| **Accès de l'agent** | Flux **OAuth** sur le portefeuille du consommateur | **Clé d'API** rattachée à un Virtual Wallet |
| **Justificatif** | Carte à usage unique ou **Shared Payment Token**, scopé (montant, devise, marchand) | Allocation, **allowlist**, montant max par transaction |
| **Autorisation** | **Approbation humaine à chaque transaction** | **Plafond** fixé à l'avance par le détenteur du compte |
| **Identité de l'agent** | Non traitée (l'agent agit sous le compte de l'humain) | **`cloudflare.pay`**, Web Bot Auth, Turnstile |
| **Maturité au jour J** | Produit livré ; limites de dépense « coming soon » | **Réservation de handle** seulement ; le reste au futur |

- **Le fait le plus significatif est stratégique** : Stripe, **co-auteur d'ACP**,
  livre un contournement des rails existants plutôt qu'un pari sur son propre
  protocole — *« agents need to work with the payment options sellers and
  consumers use today »*. Le clivage jardins clos / protocoles ouverts se rejoue
  **un étage plus bas**, et l'un de ses promoteurs joue les deux tableaux.
- **Le nœud commun est l'autorisation déléguée**, et aucun des deux ne la
  résout. L'approbation transaction par transaction n'est pas une commodité de
  conception : c'est **l'aveu** que le problème est ouvert. Le plafond
  Cloudflare est l'autre réponse — moins sûre, plus praticable : *« ces limites
  peuvent sembler des contraintes ; contre-intuitivement, elles donnent aux
  agents plus de liberté »*.
- **L'identité de l'agent devient une couche à part entière** : un agent n'a ni
  identifiant stable pour s'inscrire à une API, ni moyen natif de la payer — et
  *« abandonne souvent la tâche, renvoyant l'inscription et le paiement aux
  humains »*. C'est le trou que `cloudflare.pay` vise (analogie DNS assumée :
  un nom lisible pour une paire de clés qui ne l'est pas).

### Désambiguïsation : trois protocoles pour un sigle

| Sigle | Protocole | Périmètre | Origine |
|---|---|---|---|
| ACP | **Agentic Commerce Protocol** | agent ↔ marchand | OpenAI + Stripe (29 sept. 2025) |
| ACP | **Agent Client Protocol** | client ↔ agent | Zed (août 2025, JSON-RPC 2.0 sur stdio, Apache-2.0) |
| ACP | **Agent Communication Protocol** | agent ↔ agent | IBM Research / BeeAI (marginal) |

- **MCP relie un agent à ses outils ; ACP (Zed) relie un client à un agent** —
  les deux s'empilent, ils ne se concurrencent pas.
- **Règle d'ingénierie de la connaissance** : *on n'indexe jamais un sigle
  seul*. L'entité est le nom complet ; « ACP » n'est qu'un **alias**, porté par
  trois entités distinctes. Le corpus de veille en a fait les frais — une page
  KB attribuait le protocole de commerce à Google alors qu'il est d'OpenAI +
  Stripe.

### Signaux clés

- **900M utilisateurs hebdomadaires** ChatGPT Instant Checkout (déc. 2025)
- **73%** des consommateurs utilisent déjà l'IA pour acheter (oct. 2025)
- **×7 trafic IA** et **×11 commandes** chez Shopify (nov. 2025)
- **Schema.org reste le ciment** de toutes les ontologies commerce
- **Attributs conversationnels** : nouveau paradigme (FAQ, substituts, accessoires, couleurs enrichies)
- **Preuve sociale tierce** (Trustpilot, G2, Custplace) fréquemment citée par les LLMs
- **ACP : 4% commission** + ~2.9% Stripe = ~7% total par transaction
- **Amazon absent des protocoles ouverts** : stratégie propriétaire (Rufus, Alexa+, Buy for Me), 40% du e-commerce US
- **Triptyque écosystème** : Amazon propriétaire / Google UCP / OpenAI ACP
- **Attribution agentique invisible** : 70-90% des parcours déjà invisibles, premier signal = webhook commande
- **McKinsey : $3-5T global** de revenus commerce agentique d'ici 2030
- **Descriptions produit pour IA ≠ SEO** : cas d'usage et matériaux plutôt que mots-clés
- **StackOverflow : -75% de vues depuis GPT-4**, trafic des sites tech news -60% — le modèle publicitaire s'effondre face aux agents
- **AgentCash : 2000+ agents actifs** 10 jours après le lancement, registres marchands x402scan.com et mppscan.com
- **Stripe : 200 M+ de consommateurs** sur Link — l'argument de distribution qui rend le contournement des protocoles crédible
- **Block, T2 2026** : profit brut **+25 %** (3,2 Md$), revenus +10 % (6,62 Md$), **résultat net −83 %** (89 M$, indemnités de départ) après ~**4 000 suppressions de postes** (~40 % des effectifs) six mois plus tôt — la valeur de l'IA encaissée **par les coûts avant le prix**
- **Block** : *« Starting in June, agentic AI helped write and review nearly all of our production code changes »* — déclaration **auto-rapportée aux investisseurs**, sans définition de « nearly all » ni de « review »
- **Square dans Google Maps** : découverte et commande conversationnelles, présentées comme « la première étape d'un partenariat plus large »
- **Aucune des quatre voies de monétisation** listées par Evercore ISI pour l'IA de Block (bundles SaaS, abonnements, offres entreprise, usage) **n'est indexée sur le résultat**
- **Cloudflare Wallets, jour de l'annonce** : seule la **réservation d'un handle** est en service — une prise de position sur un espace de noms plus qu'une mise en service
