# thilen-opascope-ai-shopping-assistant-agentic-commerce-protocols-2026-02-10
## Veille
Guide technique AI shopping assistants 2026, protocoles ACP (OpenAI/Stripe) vs UCP (Google/coalition), implémentation marchands, attribution agentique

## Titre Article
AI Shopping Assistant Guide 2026: Agentic Commerce Protocols

## Date
2026-02-10

## URL
https://opascope.com/insights/ai-shopping-assistant-guide-2026-agentic-commerce-protocols/

## Keywords
commerce agentique, AI shopping assistant, ACP, UCP, Universal Commerce Protocol, Agentic Commerce Protocol, OpenAI, Google, Stripe, Shopify, Etsy, checkout agentique, feed produit, attribution, schema.org, Amazon Rufus, Alexa+, données structurées, Instant Checkout, ChatGPT, Merchant Center, measurement, incrementality testing

## Authors
Max Thilén (Opascope)

## Ton
**Profil** : Perspective de consultant e-commerce, registre professionnel et didactique, niveau avancé orienté décideurs et équipes techniques

**Description** : Max Thilén adopte le ton d'un analyste stratégique qui rédige un guide de référence exhaustif. L'article de 29 minutes combine vision macro (projections McKinsey $3-5T, Morgan Stanley) et micro-opérationnel (les 5 endpoints REST de l'API ACP, les champs obligatoires du feed produit). Le style est méthodique et structuré — chaque protocole est disséqué avec le même niveau de détail (statut, propriétaire, portée, frais, architecture), permettant une comparaison directe. L'auteur ne prend pas parti entre ACP et UCP mais conclut pragmatiquement que les marques ont besoin des deux. Les tableaux comparatifs, les exemples de code JSON-LD, les roadmaps par plateforme (Shopify, Etsy, custom) et la section attribution témoignent d'une orientation très actionnable. Le public cible est constitué de responsables e-commerce et développeurs devant préparer leurs marques à l'ère du commerce agentique.

## Pense-betes
- **Deux protocoles en compétition** : ACP (OpenAI + Stripe, live depuis sept. 2025) et UCP (Google + coalition, annoncé jan. 2026). ACP est opérationnel — ChatGPT Instant Checkout sert 900 millions d'utilisateurs hebdomadaires. UCP est plus ambitieux avec 20+ partenaires (Visa, Mastercard, PayPal, Shopify, Walmart, Target, etc.).
- **Frais ACP** : 4% de commission sur chaque transaction (confirmé jan. 2026), en plus du processing standard Stripe (~2.9% + $0.30). Total ~7% par transaction pour le marchand.
- **Architecture UCP modulaire** : quatre transports (REST, MCP d'Anthropic, A2A de Google, Embedded Protocol), deux modes checkout (natif dans l'interface IA vs iframe vers le site marchand), découverte via profil `/.well-known/ucp`. Trois capacités : Checkout, Identity Linking, Order Management.
- **Flux d'achat ACP** : l'utilisateur demande une recommandation → ChatGPT cherche dans les feeds marchands → affiche les résultats avec bouton "Buy" → Instant Checkout via Stripe → commande passée sans jamais visiter le site marchand. Rupture totale avec le modèle click-through.
- **Amazon absent des deux protocoles** : contrôle 40% du e-commerce US mais refuse la participation. Stratégie propriétaire avec Rufus AI (300M utilisateurs, +60% conversion), Alexa+ (voice commerce), et Buy for Me (achat chez concurrents depuis l'app Amazon). A bloqué les crawlers OpenAI via robots.txt (600M produits retirés). Le marché est donc un triptyque : Amazon propriétaire / Google UCP / OpenAI ACP.
- **Données produit = levier compétitif principal** : quand la publicité payante n'atteint pas les agents, la qualité des données structurées devient le seul différenciateur. ACP exige un feed JSONL/CSV/XML avec champs obligatoires (titre 150 chars, description 5000 chars orientée use-case, prix ISO 4217, disponibilité). UCP s'appuie sur Google Merchant Center avec 170+ attributs.
- **Descriptions pour IA ≠ SEO** : il faut décrire les cas d'usage, les matériaux, les avantages, pas les mots-clés. Exemple faible : "Men's Trail Running Shoe – Blue – Size 10". Exemple fort : "Lightweight trail shoe for technical terrain. Breathable mesh, aggressive lug pattern for wet rock and mud grip."
- **Crise de l'attribution** : 70-90% des parcours d'achat déjà invisibles aux analytics ; le commerce agentique pousse vers 100% d'invisibilité. Le premier signal est un webhook de commande. Impossible de mesurer combien de fois un produit est recommandé, quels concurrents sont comparés, quels facteurs influencent l'agent. Recommandation : tracking server-side par webhooks, incrementality testing, monitoring de la visibilité IA. Maturité estimée à 18-24 mois.
- **Implémentation Shopify** : ACP → candidature sur chatgpt.com/merchants + activation du canal. UCP → automatique via Shopify Agentic Storefronts. Friction minimale.
- **Projections marché** : McKinsey $3-5T global d'ici 2030, Morgan Stanley 10-20% du e-commerce capté par agents ($190-385B), Forrester 20% des vendeurs B2B confrontés à des négociations par agents fin 2026.
- **Lien avec fiches existantes** : complète la fiche Marette (guide technique ACP/UCP orienté implémentation française), la fiche NRF 2026 (annonce UCP), et la fiche AP2 (prédécesseur). Apporte la perspective OpenAI/ACP absente des autres fiches, le détail technique des APIs, la stratégie Amazon, et le problème de l'attribution.

## RésuméDe400mots
Max Thilén publie un guide de référence de 29 minutes sur les protocoles de commerce agentique qui structurent le e-commerce en 2026. Le constat de départ est radical : les clients complètent désormais des parcours d'achat entiers à l'intérieur de conversations IA, sans jamais visiter les sites marchands. ChatGPT Instant Checkout sert 900 millions d'utilisateurs hebdomadaires.

Deux protocoles se disputent cette infrastructure. L'**ACP** (Agentic Commerce Protocol), porté par OpenAI et Stripe, est opérationnel depuis septembre 2025. Il impose une commission de 4 % par transaction, un feed produit structuré et 5 endpoints REST pour le checkout. Le flux est entièrement conversationnel : l'utilisateur demande, l'agent cherche, affiche un bouton "Buy", et Stripe traite le paiement via un token partagé — l'agent ne voit jamais les données bancaires.

Le **UCP** (Universal Commerce Protocol), annoncé par Google en janvier 2026 au NRF, fédère une coalition massive : Shopify, Walmart, Target, Wayfair, Visa, Mastercard, PayPal et 20 autres partenaires. Son architecture est plus modulaire, avec quatre options de transport (REST, MCP, A2A, Embedded) et deux modes de checkout (natif dans l'interface IA ou iframe vers le site marchand). Les marchands déclarent leurs capacités via un profil `/.well-known/ucp`.

L'absence d'Amazon est stratégiquement significative. Contrôlant 40 % du e-commerce US, Amazon a choisi une voie propriétaire avec Rufus AI (300 millions d'utilisateurs, +60 % de conversion), Alexa+ pour le commerce vocal, et "Buy for Me" qui permet d'acheter chez des concurrents depuis l'app Amazon. Amazon a même bloqué les crawlers d'OpenAI, retirant 600 millions de produits. Le marché forme donc un triptyque : Amazon propriétaire, Google UCP, OpenAI ACP.

Le guide détaille les exigences techniques des deux protocoles, notamment les **données produit** qui deviennent le levier compétitif principal quand la publicité payante n'atteint pas les agents. Les descriptions doivent servir le traitement en langage naturel, pas le SEO classique : décrire les cas d'usage et matériaux plutôt que d'empiler des mots-clés.

La **crise de l'attribution** est le défi majeur : 70-90 % des parcours d'achat sont déjà invisibles aux analytics traditionnels, et le commerce agentique approche les 100 %. Le premier signal mesurable est un webhook de commande. Thilén recommande le tracking server-side, l'incrementality testing et le monitoring de visibilité IA, avec une maturité estimée à 18-24 mois.

Les projections sont considérables : McKinsey anticipe $3-5 trillions de revenus globaux d'ici 2030. Pour les marques, la conclusion est pragmatique : les deux protocoles comptent. ACP domine la découverte conversationnelle, UCP captera les requêtes intentionnelles via Google. Différents points d'entrée, même client.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| OpenAI | ORGANISATION | a_créé | Agentic Commerce Protocol (ACP) | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Stripe | ORGANISATION | co-développe | Agentic Commerce Protocol (ACP) | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Google | ORGANISATION | a_créé | Universal Commerce Protocol (UCP) | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| ACP | TECHNOLOGIE | impose | commission 4% par transaction | CONCEPT | 0.98 | DYNAMIQUE | déclaré_article |
| UCP | TECHNOLOGIE | supporte | quatre transports (REST, MCP, A2A, Embedded) | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Amazon | ORGANISATION | refuse_de_participer_à | ACP et UCP | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Amazon | ORGANISATION | a_créé | Rufus AI | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Rufus AI | TECHNOLOGIE | augmente | taux de conversion de 60% | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| ChatGPT Instant Checkout | TECHNOLOGIE | sert | 900 millions d'utilisateurs hebdomadaires | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| commerce agentique | CONCEPT | rend_invisible | attribution marketing traditionnelle | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| données produit structurées | CONCEPT | remplace | publicité payante comme levier compétitif | CONCEPT | 0.90 | ATEMPOREL | inféré |
| Max Thilén | PERSONNE | recommande | implémentation des deux protocoles ACP et UCP | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Shopify | ORGANISATION | intègre_automatiquement | UCP via Agentic Storefronts | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| McKinsey | ORGANISATION | prédit | $3-5T revenus commerce agentique global d'ici 2030 | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Max Thilén | PERSONNE | rôle | Analyste e-commerce, auteur guide Opascope | AJOUT |
| Opascope | ORGANISATION | catégorie | Cabinet conseil e-commerce / commerce agentique | AJOUT |
| Agentic Commerce Protocol (ACP) | TECHNOLOGIE | statut | Opérationnel depuis septembre 2025 | MISE_A_JOUR |
| Agentic Commerce Protocol (ACP) | TECHNOLOGIE | commission | 4% par transaction + Stripe processing | AJOUT |
| Agentic Commerce Protocol (ACP) | TECHNOLOGIE | licence | Apache 2.0 | AJOUT |
| Universal Commerce Protocol (UCP) | TECHNOLOGIE | transports | REST, MCP, A2A, Embedded Protocol | AJOUT |
| Universal Commerce Protocol (UCP) | TECHNOLOGIE | coalition | 20+ partenaires dont Visa, Mastercard, PayPal | MISE_A_JOUR |
| Rufus AI | TECHNOLOGIE | catégorie | Assistant IA shopping in-app Amazon | AJOUT |
| Rufus AI | TECHNOLOGIE | utilisateurs | 300 millions | AJOUT |
| Alexa+ | TECHNOLOGIE | catégorie | Commerce vocal avec achat automatisé Amazon | AJOUT |
| ChatGPT Instant Checkout | TECHNOLOGIE | catégorie | Checkout agentique sans visite site marchand | AJOUT |
| ChatGPT Instant Checkout | TECHNOLOGIE | utilisateurs hebdomadaires | 900 millions | AJOUT |
