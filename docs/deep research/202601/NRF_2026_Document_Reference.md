# NRF 2026 : Retail's Big Show – Document de Référence

**Commerce Agentique, Universal Commerce Protocol et Transformation du Retail**

---

**11-13 janvier 2026 | Jacob K. Javits Convention Center, New York**  
40 000 visiteurs | 1 025 exposants | 100 pays | 335 000 m²

---

## Table des matières

1. [Contexte et Cadre de l'Événement](#1-contexte-et-cadre-de-lévénement)
2. [Universal Commerce Protocol (UCP)](#2-universal-commerce-protocol-ucp)
3. [Partenariat Walmart-Google](#3-partenariat-walmart-google)
4. [Carrefour : Premier Distributeur Alimentaire Européen](#4-carrefour--premier-distributeur-alimentaire-européen)
5. [IA Agentique : De l'Assistance à l'Exécution](#5-ia-agentique--de-lassistance-à-lexécution)
6. [Optimisation pour Agents IA (AIO vs SEO)](#6-optimisation-pour-agents-ia-aio-vs-seo)
7. [Renaissance du Magasin Physique](#7-renaissance-du-magasin-physique)
8. [Supply Chain, Circularité et Durabilité](#8-supply-chain-circularité-et-durabilité)
9. [Innovation Lab : Startups et Solutions Émergentes](#9-innovation-lab--startups-et-solutions-émergentes)
10. [Keynotes Majeures](#10-keynotes-majeures)
11. [Métriques et Études de Référence](#11-métriques-et-études-de-référence)
12. [Perspectives Internationales](#12-perspectives-internationales)
13. [Contexte Réglementaire et Préoccupations](#13-contexte-réglementaire-et-préoccupations)
14. [Recommandations et Actions Prioritaires](#14-recommandations-et-actions-prioritaires)
15. [Tableau Récapitulatif des Innovations Clés](#15-tableau-récapitulatif-des-innovations-clés)

---

## 1. Contexte et Cadre de l'Événement

### 1.1 Le Thème « The Next Now »

L'édition 2026 du NRF marque l'entrée du retail dans une phase d'industrialisation massive et d'exécution stratégique. La relation binaire traditionnelle entre acheteur et vendeur est déclarée obsolète. Dans une chaîne de valeur mondiale diversifiée, le comportement du consommateur évolue « d'un moment à l'autre ».

**Implications majeures :**

- **Urgence de l'implémentation** : Les technologies présentées (IA agentique, robotique, informatique spatiale) ne sont plus des concepts de R&D mais des impératifs opérationnels immédiats
- **Convergence temporelle** : La distinction entre gestion des opérations quotidiennes et planification stratégique à long terme s'effondre

### 1.2 Calendrier de l'Événement

| Composante | Dates | Lieu | Public cible |
|------------|-------|------|--------------|
| NRF 2026: Retail's Big Show | 11-13 janvier 2026 | Javits Center, NYC | Professionnels retail, technologie |
| NRF Rev | 11-12 janvier 2026 | Sheraton Times Square | Supply Chain, Logistique Inverse |
| VIP Awards | 9 janvier 2026 | Gotham Hall (Offsite) | Dirigeants, Partenariats |
| Retail Store Tours | 10 janvier 2026 | Divers lieux NYC | Benchmarking, innovation magasin |

### 1.3 Contexte Macroéconomique

L'atmosphère était décrite comme « stable et constructive ».

**Tensions structurantes :**

- **Pression tarifaire et Supply Chain** : Incertitude liée aux politiques commerciales américaines, poussant à la résilience par diversification des sources
- **Maturité de l'IA** : Passage de l'IA générative (création de contenu) à l'IA agentique (exécution d'actions autonomes)

---

## 2. Universal Commerce Protocol (UCP)

### 2.1 Annonce et Partenaires

Le **11 janvier 2026**, Sundar Pichai (CEO Alphabet/Google) a annoncé l'**Universal Commerce Protocol (UCP)**, un protocole open-source sous licence Apache 2.0, disponible sur GitHub. Ce standard permet aux agents IA de découvrir, négocier et finaliser des achats directement avec les systèmes retailers.

**Co-développeurs (5 entreprises) :**

| Entreprise | Rôle |
|------------|------|
| **Shopify** | Co-architecte principal, responsable de l'Embedded Checkout Protocol et du Checkout Kit |
| **Walmart** | Intégration inventaire temps réel et livraison rapide |
| **Target** | Checkout natif dans Gemini |
| **Etsy** | Représentation des vendeurs indépendants |
| **Wayfair** | Extension fulfillment pour livraison planifiée |

**Partenaires endorseurs (60+ organisations) :**

Visa, Mastercard, American Express, Stripe, Adyen, PayPal, Best Buy, Macy's, Sephora, Zalando, Gap Inc., The Home Depot, Ant International

### 2.2 Architecture Technique

L'UCP adopte une architecture en couches stratifiée inspirée du modèle TCP/IP :

| Couche | Fonction | Détails |
|--------|----------|---------|
| Shopping Service | Primitives fondamentales | Sessions checkout, articles panier, calcul totaux, gestion statuts |
| Capabilities | Fonctionnalités majeures | Checkout, Orders, Catalog – versionnées indépendamment |
| Extensions | Schémas spécifiques | Fulfillment, remises, programmes fidélité – ajoutés par marchands |

**Transports supportés (4) :**

1. **REST API** (obligatoire) – Basé sur OpenAPI 3.x
2. **Model Context Protocol (MCP)** d'Anthropic – Capabilities mappent directement aux outils LLM
3. **Agent2Agent (A2A)** – Communication inter-agents
4. **Embedded Protocol** – Intégration d'interfaces via JSON-RPC 2.0

**Découverte** : Les marchands publient leurs capacités à `/.well-known/ucp`, permettant aux agents de découvrir dynamiquement les fonctionnalités supportées.

### 2.3 Gouvernance Décentralisée

Modèle sans registre central utilisant le **reverse-domain naming** :
- `dev.ucp.shopping.checkout`
- `com.example.payments.installments`

La propriété d'un domaine suffit pour créer ses extensions.

> *« Nous avons pris tout ce que nous avons appris en construisant des checkouts pour des millions de commerces uniques pour créer un standard robuste. »*  
> — Vanessa Lee, VP Product, Shopify

### 2.4 Sécurité des Paiements

L'architecture repose sur un **triangle de confiance** impliquant le marchand, la plateforme (agent IA) et le fournisseur de credentials de paiement.

**Cycle de vie du paiement :**

1. **Négociation** : Le marchand analyse le panier et annonce les handlers disponibles
2. **Acquisition** : La plateforme exécute la logique du handler et génère un token sécurisé
3. **Completion** : Le token opaque est transmis au marchand pour capture des fonds

**Payment Handlers au lancement :**
- Google Pay (natif)
- Shop Pay et PayPal (« coming soon »)

**Garanties de sécurité PCI :**
- Flux unidirectionnel de credentials (plateforme vers marchand uniquement)
- Manipulation exclusive de tokens opaques, jamais de numéros de carte bruts
- **AP2 Mandates** : Preuves cryptographiques via Verifiable Credentials pour transactions autonomes à haute valeur

**Point crucial** : Le **Merchant of Record reste le détaillant**, pas Google. Le marchand conserve la propriété juridique de la transaction, le contrôle des données clients, et la possibilité de remarketing.

### 2.5 Native Checkout

Le checkout natif permet aux utilisateurs de finaliser leurs achats directement dans l'interface conversationnelle (AI Mode ou application Gemini) sans quitter la conversation.

**Flux d'achat :**

1. Requête conversationnelle
2. Affichage des produits avec images et détails
3. Tap sur « Buy »
4. Page de checkout pré-remplie avec Google Pay et adresse depuis Google Wallet
5. Confirmation en quelques taps

**États du checkout :**

| État | Description |
|------|-------------|
| `incomplete` | Informations manquantes que l'agent tente de résoudre via API |
| `requires_escalation` | Input acheteur requis avec handoff vers URL de continuation |
| `ready_for_complete` | Finalisation programmatique possible |

**Fonctionnalité agentique déjà live – Price Tracking** : L'utilisateur définit un budget cible, l'agent suit l'article, notifie quand le prix atteint l'objectif, et avec permission, finalise automatiquement l'achat via Google Pay.

### 2.6 Protocole Concurrent : Stripe Agentic Commerce Suite (ACS)

**Annonce du 12 janvier 2026** – Le lendemain du lancement de l'UCP par Google, **Stripe** et **commercetools** ont annoncé l'adoption enterprise de l'**Agentic Commerce Suite (ACS)**, un protocole concurrent pour le commerce agentique.

**JD Sports : Premier retailer européen à déployer l'ACS**

JD Sports Fashion plc devient le premier grand retailer européen à adopter l'ACS, marquant un engagement précoce dans la conversion de la découverte IA en transactions réelles.

> *« Nous voulons faciliter au maximum les achats de nos clients, peu importe où ils se trouvent ou comment ils préfèrent acheter. Alors que les interfaces pilotées par IA deviennent un véritable point d'entrée pour le commerce, notre partenariat avec commercetools et Stripe nous permet non seulement d'être découvrables, mais aussi d'être transactionnels à travers ces canaux, sans ajouter de complexité à nos opérations. »*  
> — Regis Schultz, Group CEO, JD Sports Fashion plc

**Composants de l'écosystème commercetools/Stripe :**

| Composant | Fonction |
|-----------|----------|
| **Agentic Commerce Suite (ACS)** | Connecte la découverte IA aux flux de checkout et paiement sécurisés |
| **AI Hub** | Fondation connective pour les workflows agentiques, maintient les retailers découvrables dans les expériences IA |
| **Agentic Jumpstart** | Programme d'accélération incluant AI Hub pour le déploiement rapide |

**Implications stratégiques :**

Cette annonce révèle une **fragmentation émergente de l'écosystème** du commerce agentique avec deux standards majeurs :

| Protocole | Leader | Retailers pilotes | Écosystème paiement |
|-----------|--------|-------------------|---------------------|
| **UCP** (Google) | Google, Shopify, Walmart | Carrefour, Target, Walmart, Sephora | Google Pay, PayPal (prévu) |
| **ACS** (Stripe) | Stripe, commercetools | JD Sports, Nespresso | Stripe |

> *« En 2026, les entreprises retail doivent passer de la compréhension à l'action. Le commerce évolue plus vite que la plupart des entreprises ne peuvent réarchitecturer. »*  
> — Dirk Hoerig, Founder & Chief Innovation Officer, commercetools

**Nouveaux clients commercetools annoncés** : Nespresso rejoint la plateforme pour préparer ses workflows agentiques.

---

## 3. Partenariat Walmart-Google

Annoncé conjointement par John Furner (CEO Walmart U.S.) et Sundar Pichai au NRF 2026, ce partenariat représente l'exemple le plus abouti de commerce agentique.

**Capacités intégrées :**

- Produits Walmart et Sam's Club automatiquement inclus dans Gemini avec inventaire temps réel
- Recommandations personnalisées basées sur l'historique d'achat en magasin ET en ligne
- Consolidation avec le panier existant
- Application automatique des avantages Walmart+ et Sam's Club
- **Livraison jusqu'à 30 minutes** pour des centaines de milliers de produits

> *« La transition de la recherche traditionnelle vers le commerce piloté par agents représente la prochaine grande évolution du retail. Nous ne regardons pas ce changement, nous le conduisons. »*  
> — John Furner, CEO Walmart U.S.

**Scénario démontré par Pichai** : Un utilisateur demande « Find a lightweight suitcase for an upcoming trip », Gemini affiche des options avec détails produits. Pour un nouveau client, le protocole permet de proposer un prix « nouveau membre » ou inscription fidélité instantanée. Pour un client existant, offres personnalisées et suggestions complémentaires (cubes de rangement).

**Expansion logistique Wing** : Livraison drone étendue à Houston, Orlando, Tampa, Charlotte. Objectif : 270 magasins couvrant ~10% de la population américaine d'ici 2027.

---

## 4. Carrefour : Premier Distributeur Alimentaire Européen

### 4.1 Adoption de l'UCP

**Emmanuel Grenier**, Directeur Supply Chain, E-commerce, Data et Transformation digitale de Carrefour, a confirmé l'adoption du protocole Universal Commerce Protocol.

> *« En soutenant le Universal Commerce Protocol de Google, nous souhaitons proposer à nos clients des parcours d'achat encore plus fluides, directement intégrés dans Google Search et l'application Gemini, dès que ces fonctionnalités seront déployées. »*  
> — Emmanuel Grenier, Carrefour

Cette annonce positionne Carrefour comme le **premier grand distributeur alimentaire européen** à s'engager dans le commerce agentique.

### 4.2 Présence au NRF 2026

| Élément | Statut |
|---------|--------|
| Adoption Universal Commerce Protocol (UCP) | ✅ Confirmé – partenaire de lancement |
| Intervention Emmanuel Grenier | ✅ Annonce officielle adoption UCP |
| Keynote Alexandre Bompard | ❌ Non présent (World Retail Congress Berlin, avril 2026) |
| Mention Carrefour par speakers | ✅ Elizabeth Lachhar (Rezolve AI) cite Carrefour |

### 4.3 Plan Carrefour 2026 – Objectifs Digitaux

| Objectif | Cible |
|----------|-------|
| GMV e-commerce | 10 milliards € (triple de 2021) |
| Investissements digitaux | 3 milliards € (2022-2026) |
| Migration cloud | 100% d'ici 2026 |
| Clients omnicanaux | 30% d'ici 2026 |
| ROC additionnel du digital | 600 millions € d'ici 2026 |

### 4.4 Écosystème Technologique

- **Hopla+** – Agent IA conversationnel déjà déployé sur l'application Carrefour
- **Google Cloud** – Partenariat infrastructure
- **VusionGroup** – Smart shelves (étiquettes électroniques)
- **SymphonyAI** – Vision IA magasins
- **Carrefour Links** – Régie retail media

### 4.5 Implications Stratégiques

**Actions recommandées pour Carrefour :**

- **Audit des données produits (PIM)** – S'assurer que chaque SKU est lisible par l'IA avec attributs précis (nutrition, origine, prix, stock local)
- **Capture des courses de réassort** – Utiliser l'UCP pour les achats de commodité (pain, lait, couches) via assistants vocaux
- **Monétisation retail media** – Accélérer le déploiement de Carrefour Links dans l'espace physique
- **Outils IA locaux** – Donner aux directeurs de magasin des outils d'IA pour ajuster merchandising et commandes

**Enjeu de marque** : Comment maintenir l'identité de marque (« Brand Equity ») si la transaction se déroule sur une interface tierce ? La réponse réside dans la capacité à offrir des services exclusifs (fidélité, livraison premium) via l'UCP.

**Implications concurrentielles** : Les concurrents français (Auchan, Leclerc, Casino/Intermarché) devront accélérer leurs stratégies agentiques pour éviter la désintermédiation.

---

## 5. IA Agentique : De l'Assistance à l'Exécution

### 5.1 Distinction IA Générative vs IA Agentique

| Caractéristique | IA Générative (2024-2025) | IA Agentique (2026+) |
|-----------------|---------------------------|----------------------|
| Rôle | Support à la décision | Prise de décision autonome |
| Interaction | Répond aux requêtes | Anticipe et agit |
| Cas d'usage clé | Chatbots, rédaction fiches produits | Réapprovisionnement auto, pricing dynamique |
| Intégration | Couche superficielle (Front-end) | Intégration profonde (Core Systems/ERP) |
| Posture | Passive, attend instruction | Proactive, orientée objectif |

### 5.2 Annonces des Géants Technologiques

#### Google

- **Universal Commerce Protocol (UCP)** – Standard ouvert pour commerce agentique
- **Gemini Enterprise for Customer Experience** – En preview avec Home Depot, McDonald's, Kroger
- **Business Agent** – Lancé le 12 janvier avec Lowe's, Michaels, Poshmark, Reebok
- **Métrique** : 90 000 milliards de tokens traités sur Google Cloud Vertex AI en décembre 2025 (croissance 11x)

#### Microsoft

- **Copilot Checkout** – Achat direct dans conversations Copilot (PayPal, Shopify, Stripe)
- **Brand Agents** – Assistants IA parlant avec la voix de la marque, déployables en quelques heures
- **Pegasus Program Startups** – Nimble (intelligence marché), YDISTRI (redistribution stocks), Omnistream (category management)

#### Salesforce

- **Agentforce Commerce** – SMS/WhatsApp/email bidirectionnel convertissant marketing en conversations de vente
- **Guided Shopping v2** – Interactions personnalisées avec recommandations contextuelles

#### SAP

- **SAP Retail Intelligence** – Disponibilité générale H1 2026, planification demande et gestion stocks IA
- **Order Reliability Agent** – Q2 2026, identifie proactivement les problèmes de commande
- **Joule Copilot** – Gestion assortiments en langage naturel

#### Oracle

- **Supply Chain Collaboration** – Insights IA pour prévisions, intégration ESG et conformité réglementaire

#### Mastercard

- **Agent Pay** – Infrastructure paiement pour agents autonomes : enregistrement via network tokens, standardisation interfaces, vérification intention, authentification biométrique

---

## 6. Optimisation pour Agents IA (AIO vs SEO)

L'avènement de l'UCP transforme radicalement les règles de la visibilité numérique. On passe du SEO (Search Engine Optimization) à l'**AIO (Artificial Intelligence Optimization)**.

> *« Les agents IA ne naviguent pas sur les pages web comme les humains – ils interrogent les APIs, analysent les flux de produits et évaluent les données structurées. »*  
> — Alex Moss, Search Engine Journal

> *« Schema.org est désormais la colle qui tient tout ensemble. »*  
> — Pascal Fleury, Google Search Central, décembre 2025

### 6.1 Nouveaux Attributs Merchant Center

- Réponses aux questions produits fréquentes
- Accessoires compatibles
- Produits de substitution
- Cas d'usage détaillés

### 6.2 Schémas JSON-LD Obligatoires

- `Product`
- `Offer`
- `AggregateRating`
- `MerchantReturnPolicy`
- `OfferShippingDetails`

Google travaille à une parité 1:1 entre le markup Schema.org et les spécifications des flux Merchant Center.

### 6.3 Answer Eligibility Engineering

Ce concept émergent remplace le ranking traditionnel. La visibilité ne dépend plus de la position SERP mais de l'éligibilité à être inclus dans les réponses IA.

**Signaux critiques :**

- **Autorité de marque** – Sentiment positif, citations tierces
- **Fiabilité de l'inventaire** – Données stock temps réel
- **Compatibilité protocoles standards** – UCP, ACP (OpenAI/Stripe), MCP (Anthropic)

> *« Le shopping piloté par agents génère des requêtes plus spécifiques, à haute intention. Les marchands doivent être stratégiques sur leur apparition dans les moteurs de réponse. »*  
> — BigCommerce

---

## 7. Renaissance du Magasin Physique

Le magasin physique est réaffirmé comme pivot central de la stratégie retail, avec des fonctions élargies : plateforme médiatique et nœud logistique critique.

### 7.1 Retail Media Networks In-Store

**Chiffres clés :**

| Métrique | Valeur |
|----------|--------|
| Dépenses retail media Amérique du Nord 2025 | 65-78 milliards USD |
| Croissance projetée 2026 | 17-24% |
| Revenus US captés par Amazon et Walmart | 80-86% |
| Consommateurs achetant en magasin | 72% |

> *« Le retail media en magasin est un géant endormi qui se réveille. »*  
> — Chris Riegel, CEO Stratacache

### 7.2 Technologies Magasin Connecté

| Solution | Description |
|----------|-------------|
| **Sensormatic FLEX** | Transforme les portiques de sécurité en supports d'affichage numérique dynamiques (100% du trafic capté) |
| **VusionGroup (SES-imagotag)** | Étiquettes électroniques devenant micro-écrans promotionnels « Shelf-Edge Media » |
| **Toshiba VisualStore** | Gestion unifiée des points de contact (caisses, self-checkout, bornes mobiles) |
| **Zello QR Assist** | QR codes pour demande d'aide sans chercher un vendeur |
| **Focal Systems** | Caméras sur étagères pour détecter ruptures et vols en temps réel |
| **Hanshow + Microsoft** | Framework Digital Twin pour magasin intelligent |

### 7.3 Renaissance des Centres Commerciaux

- Visites en mall indoor : **+1,8%** au S1 2025
- Durées de visite : **+3,3%**
- Exemple : Netflix House (10 000 m²) au King of Prussia

---

## 8. Supply Chain, Circularité et Durabilité

### 8.1 Résilience Supply Chain

La stratégie « Just-in-Time » évolue vers une approche **« Just-in-Case »** capable d'absorber les chocs.

- **Analyse prédictive IA** – Modélisation de scénarios complexes (tarifs douaniers, blocage de ports)
- **Visibilité bout en bout RFID** – Beontag, Temera : traçabilité unitaire absolue de l'usine au rayon

### 8.2 Logistique Inverse et NRF Rev

Avec des taux de retour e-commerce de 20-30%, la réintégration immédiate des produits retournés devient impérative.

- **Circularité profitable** – Routage vers stock vendable ou canaux Re-commerce
- **Digital Product Passport (DPP)** – Anticipation des régulations UE. Solutions Inriver, Tech Mahindra pour données traçabilité, composition, recyclabilité

### 8.3 RAIN Alliance RFID

Innovation prometteuse : intégration de lecteurs RFID directement dans les smartphones grand public. Permettra aux consommateurs de scanner eux-mêmes les produits pour vérifier authenticité, origine (DPP) ou disponibilité.

---

## 9. Innovation Lab : Startups et Solutions Émergentes

Le NRF Innovators Showcase a présenté 50 entreprises sélectionnées par le comité consultatif NRF et Forrester.

### 9.1 Startups Internationales Notables

| Startup | Solution | Impact |
|---------|----------|--------|
| **Rezolve AI** (NASDAQ: RZLV) | Brain Suite : IA conversationnelle, recherche visuelle, checkout autonome | Démonstration Microsoft + Fashable |
| **Nimble** | Navigateurs IA agentiques, intelligence marché temps réel | Pricing, assortiment, prévision |
| **YDISTRI** | Redistribution inventaire inter-magasins IA | Réduction démarques, optimisation prix |
| **VenHub Global** | Magasin autonome 24/7 (7m x 3m) | Déployé LAX, Hollywood Bowl |
| **PaperWeight AI** | Capteurs papier ultra-low-cost | Visibilité SKU temps réel étagères |
| **Lazuli** (Japon) | Product Data Platform (PDP) | Nettoyage, normalisation données produits |
| **Slip** | Ticket de caisse dynamique wallet mobile | Garanties, retours, fidélisation post-achat |
| **Spangle AI** | Landing pages dynamiques post-clic | Optimisation intention utilisateur |
| **Vody** | Préparation données recherche langage naturel | Findabilité conversationnelle |

### 9.2 Pavillon France (29 entreprises)

- **Autone** – Gestion stocks IA
- **OneStock** – OMS omnicanal
- **Revers.io** – Gestion retours
- **Faume** – Seconde main
- **Mirakl** – Session « Winning in the Agentic Era » par Anne-Claire Baschet (Chief Data & AI Officer)

---

## 10. Keynotes Majeures

### 10.1 Sundar Pichai (CEO Google/Alphabet)

L'IA comme « accélérateur d'ingéniosité humaine ». Responsabilité des plateformes technologiques de créer des standards ouverts (comme l'UCP) permettant à tous les acteurs, petits et grands, de participer à l'économie numérique sans être enfermés dans des jardins clos.

### 10.2 Ryan Reynolds (Acteur, Entrepreneur)

Session « From gin to global fandom ». Philosophie du « Maximum Effort » avec légèreté. Encourage le « Fast-vertising » (réactivité culturelle) plutôt que les processus de validation marketing lents.

> *« La connexion, la créativité et la culture génèrent plus de croissance que la taille du budget. »*

### 10.3 Michael Rubin (CEO Fanatics)

Ouverture du salon sur la disruption des modèles traditionnels. Intégration verticale, fabrication temps réel, agilité D2C. Philosophie « fan-first » : vitesse, innovation, connexion émotionnelle.

### 10.4 Fran Horowitz (CEO Abercrombie & Fitch)

Visionary Award pour l'un des redressements les plus spectaculaires du retail : **11 trimestres consécutifs de croissance**. Approche : écouter le client, responsabiliser les équipes, cultiver l'agilité.

### 10.5 LVMH : Stratégie « Quiet Technology »

**Gonzague de Pirey** (Chief Omnichannel & Data Officer) et **Soumia Hadjali** (Louis Vuitton). IA intégrée de manière « invisible » pour préserver l'artisanat tout en optimisant personnalisation, clienteling et prévisions de demande.

### 10.6 Youssef Seffar (LabelVie/Carrefour)

Directeur Pricing du Groupe LabelVie (franchisé Carrefour). Session « The retail leader's Edge: Pricing for AI, tariffs, and the new consumer » avec Revionics. Le pricing dynamique comme outil d'équilibre entre perception prix consommateur et protection des marges.

---

## 11. Métriques et Études de Référence

### 11.1 Adoption IA par les Consommateurs (Étude IBM-NRF)

| Usage IA | Pourcentage |
|----------|-------------|
| Consommateurs utilisant l'IA pendant achats | 45% |
| Recherche produits | 41% |
| Interprétation avis | 33% |
| Chasse aux bonnes affaires | 31% |

### 11.2 Croissance Commerce Agentique

| Source | Métrique |
|--------|----------|
| McKinsey projection | 3-5 trillions USD globalement d'ici 2030 |
| Adobe (fêtes 2025) | +693,4% croissance trafic via IA générative |
| Shopify (depuis janvier 2025) | x7 trafic IA, x11 commandes IA |
| Salesforce (fêtes 2025) | 20% des ventes retail générées par agents IA |
| Pilotes UCP | +122% de transactions complétées |

### 11.3 Confiance Consommateurs

- **Forrester** : Seulement 24% des consommateurs font confiance à l'IA pour effectuer des achats
- 60% veulent conserver le contrôle de la décision finale

### 11.4 Tendances Santé Impactant le Retail

- **12,4%** des Américains prennent des traitements GLP-1 (Ozempic, Wegovy) vs 5,8% en février 2024
- **6,5 milliards USD** de ventes grocery perdues sur le snacking

---

## 12. Perspectives Internationales

### 12.1 Europe

- **Carrefour (France)** – Premier distributeur alimentaire européen à adopter l'UCP
- **Zalando (Allemagne)** – Partenaire endorseur UCP
- **Préoccupations allemandes** – Duopole Amazon-Walmart (80-86%), manque de talents data
- **EuroShop 2026** – Düsseldorf, février 2026, opportunité européenne retail media in-store

### 12.2 Asie

- **Japon (top 10 pays participants)** – Seven-Eleven Japan, MUJI, Fujitsu, startups MUSE et Lazuli
- **Chine (Alibaba)** – Feiran Liu (Tmall Global) : session sur transformation IA chinoise
- **Hanshow (Beijing)** – Partenariat Microsoft pour Digital Twins magasin
- **Ant International** – EasySafePay : 200+ marchés, 1,8 milliard comptes, 150 millions marchands

### 12.3 Amérique Latine

**Brésil** positionné comme « laboratoire avancé » du retail mondial : 55% du e-commerce latino-américain, culture omnicanale naturelle, consolidation du paiement Pix.

### 12.4 Absences Notables

- **Amazon** – Bloque les crawlers IA, construit son propre système propriétaire « Buy for Me »
- **Apple** – Absence de l'écosystème UCP

---

## 13. Contexte Réglementaire et Préoccupations

### 13.1 Contexte Antitrust Google

- Reconnu coupable de monopole en ad tech (avril 2025)
- Reconnu coupable de monopole en recherche (août 2024)
- Plus de 8 milliards € d'amendes européennes accumulées

### 13.2 Préoccupations Soulevées

- **Digital Rights Watch** – Centralisation potentielle des données transactionnelles au sein des infrastructures Big Tech
- **Electronic Frontier Foundation** – Appel à des protocoles de consentement explicites et auditables
- **Coûts d'implémentation UCP** – Estimés 15 000-25 000 USD, risque de marginalisation des petits retailers

---

## 14. Recommandations et Actions Prioritaires

### 14.1 Actions Immédiates Retailers

1. **Auditer les données structurées Schema.org**
2. **Enrichir les flux Merchant Center** avec nouveaux attributs conversationnels
3. **Synchroniser l'inventaire temps réel**
4. **S'inscrire à la waitlist UCP** via developers.google.com/merchant/ucp
5. **Évaluer l'adoption du protocole UCP**

### 14.2 Actions Stratégiques

- **Gouvernance IA au COMEX** – L'IA quitte le périmètre IT pour devenir enjeu de direction générale
- **Infrastructure retail media** – Construire les capacités de mesure avant la concentration du marché
- **Data produits pour agents IA** – Préparer les catalogues pour requêtes en langage naturel
- **Outils IA locaux** – Donner aux directeurs de magasin des outils d'ajustement merchandising

### 14.3 Prédictions Clés 2026

1. **Décalage plateformes sociales** – Gen Z/Alpha migrent de TikTok vers Reels, Shorts et plateformes niche
2. **Investissements IA incontournables** – Le cycle d'engouement est terminé, l'IA devient outil essentiel
3. **GenAI rééquilibre le shopping** – Transformation des deux côtés du comptoir
4. **Compétences CMO critiques** – Analytics marketing, tech next-gen et stratégies sociales
5. **Rotation CEO continue** – 41 départs CEO retail en 2025 (+116%), plus haut turnover sectoriel

### 14.4 Calendrier à Retenir

| Événement | Date | Lieu |
|-----------|------|------|
| EuroShop 2026 | Février 2026 | Düsseldorf, Allemagne |
| World Retail Congress | Avril 2026 | Berlin, Allemagne |
| NRF Europe Paris | 15-17 septembre 2026 | Porte de Versailles, Paris |
| NRF 2027 Retail's Big Show | Janvier 2027 | Javits Center, New York |

---

## 15. Tableau Récapitulatif des Innovations Clés

| Technologie / Concept | Acteurs Clés | Impact Métier Retail | Maturité |
|-----------------------|--------------|----------------------|----------|
| **Universal Commerce Protocol (UCP)** | Google, Walmart, Shopify, Carrefour | Achat natif via agents IA. Redéfinit SEO/Acquisition | Lancement (Disruptif) |
| **Agentic Commerce Suite (ACS)** | Stripe, commercetools, JD Sports | Protocole concurrent pour checkout agentique | Lancement (12 jan.) |
| **IA Agentique** | Microsoft, SAP, Salesforce | Automatisation autonome (Supply, Pricing) | Émergent (Déploiement) |
| **In-Store Retail Media** | Sensormatic, VusionGroup | Monétisation trafic magasin via pub numérique | Croissance (Forte) |
| **Smart RFID & DPP** | Beontag, Temera, RAIN Alliance | Traçabilité totale, conformité RSE, anti-contrefaçon | Mature (Industrialisation) |
| **Data Cleaning AI** | Lazuli, Vody | Pré-requis infrastructurel pour toute stratégie IA | Critique (Fondation) |
| **Checkout Conversationnel** | Google Gemini, Microsoft Copilot | Finalisation achat sans quitter la conversation | Lancement (Pilotes US) |
| **Digital Twin Magasin** | Hanshow, Microsoft | Sensing, edge intelligence, simulation cloud | Émergent (R&D) |

---

## Conclusion

Le NRF 2026 ne fut pas une vitrine d'innovations spéculatives mais un **moment de clarification** sur l'exécution opérationnelle de l'IA. L'annonce du Universal Commerce Protocol par Google le 11 janvier, suivie dès le lendemain par l'Agentic Commerce Suite de Stripe/commercetools, illustre l'intensité de la course aux standards du commerce agentique.

**Deux écosystèmes émergent :**
- **UCP (Google)** : Carrefour, Walmart, Shopify, Target, Sephora
- **ACS (Stripe)** : JD Sports, Nespresso, commercetools

Cette **fragmentation précoce** rappelle les débuts du web et pose une question stratégique : les retailers devront-ils supporter plusieurs protocoles ou un standard finira-t-il par dominer ?

L'UCP comme l'ACS marquent un tournant infrastructurel pour le commerce numérique. Pour les retailers, l'adoption d'au moins un protocole représente désormais une **modernisation obligatoire**, pas une expérimentation optionnelle.

Les retailers qui n'auront pas engagé leur transformation agentique risquent une **désintermédiation structurelle** : les agents IA orienteront les consommateurs vers les enseignes techniquement intégrées, créant un avantage compétitif durable pour les pionniers.

Le défi n'est plus de « digitaliser » (c'est fait), mais d'« agentifier » le commerce : rendre produits, magasins et services intelligibles et accessibles par les agents artificiels qui guideront bientôt les choix de millions de consommateurs.

> ***La question n'est plus de savoir si le commerce agentique adviendra, mais qui en définira les règles.***

---

*Document compilé à partir des sources NRF 2026 — Mis à jour le 13 janvier 2026*
