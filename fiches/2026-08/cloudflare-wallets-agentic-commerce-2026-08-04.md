---
themes: [economie-marche, outils-plateformes, qualite-securite]
source: "Cloudflare"
---
# cloudflare-wallets-agentic-commerce-2026-08-04

## Veille

Annonce produit publiée sur le blog **Cloudflare** le **4 août 2026** par **Will Papper**, dans le cadre de l'**Agents Week** : **Cloudflare Wallets**, présenté comme *« the programmable wallet for the agentic Internet »*. **Le problème posé** est précis et bien choisi : un agent qui veut essayer une API doit traverser une page de connexion **conçue pour des humains**, faire ajouter un moyen de paiement par un humain, générer une clé d'API, puis comprendre comment appeler le service. Deux manques structurels l'expliquent — *« Agents do not have a stable identifier to sign up for an API, and they do not have a native way to pay for APIs »* — avec pour conséquence que *« AI agents often give up on these tasks entirely, kicking registration, payment methods, and API key generation back to humans »*. **L'architecture proposée tient en deux types de portefeuilles** : les **Account Wallets**, destinés aux humains propriétaires d'un compte Cloudflare (approvisionner, déléguer, retirer), et les **Virtual Wallets**, destinés aux agents, **opérant par clé d'API** et dont le plafond de dépense est **fixé par le détenteur du compte**. Les garde-fous annoncés sont explicites : **allocation, liste d'autorisation, montant maximal par transaction**. **Le rail de paiement est le protocole x402** (paiements attachés à des requêtes HTTP) et la monnaie est le **stablecoin** — ce qui place l'offre dans un camp distinct de celui des schémas adossés aux réseaux de cartes. **L'argument le plus intéressant est contre-intuitif et central** : *« These limits may seem like constraints, but counterintuitively they give agents more freedom. If an agent is responsible for $10, you can worry less about its spending than if it is responsible for $1,000. »* → **le plafond n'est pas ce qui bride l'autonomie, c'est ce qui la rend consentable.** **Second volet, plus stratégique que le premier** : l'identité, via un espace de noms **`cloudflare.pay`** — un agent de recherche pourrait vivre à `research.example.cloudflare.pay`, donnant au marchand la certitude qu'il parle à l'agent d'une organisation identifiée. Cloudflare revendique une ambition volontairement minimale (*« a human-readable identifier for a not-very-readable keypair, similar to the URL and IP-address pairings used in DNS »*), adossée à ses briques existantes (**Turnstile**, Bot Management, **Web Bot Auth** et ses paires de clés), et annonce vouloir adopter les schémas de la **x402 Foundation** à mesure qu'ils émergeront. **Réserve dirimante sur le statut du texte** : **presque tout est au futur**. Ce qui existe le jour de l'annonce, c'est la **réservation d'un handle** ; les paiements, les Virtual Wallets, les garde-fous et les rampes d'accès aux fonds sont annoncés (*« Soon, you will be able to… »*). C'est une **prise de position sur un espace de noms**, davantage qu'une mise en service.

## Titre Article

Announcing Cloudflare Wallets: the programmable wallet for the agentic Internet

## Date

2026-08-04

## URL

https://blog.cloudflare.com/wallets/

## Keywords

Cloudflare Wallets, commerce agentique, Agents Week, portefeuille programmable, Account Wallet, Virtual Wallet, délégation de dépense, plafond de dépense, allocation, liste d'autorisation, montant maximal par transaction, garde-fous, autonomie bornée, x402, micropaiement, requête HTTP payante, stablecoin, Monetization Gateway, marché biface, marchand agentique, onboarding d'agent, clé d'API, identifiant stable, identité d'agent, cloudflare.pay, espace de noms, sous-domaine d'agent, attribution, essai gratuit, crédits d'inscription, Web Bot Auth, paire de clés, identifiant lisible par un humain, analogie DNS, Turnstile, Bot Management, analogie VPN, x402 Foundation, Agents SDK, MCP Tools, rampe d'entrée, rampe de sortie, budget par salarié, revue humaine, dépense anormale, marketplace headless, trafic de bots, Will Papper

## Authors

**Will Papper** — auteur de l'annonce sur le blog Cloudflare (lecture annoncée : 8 minutes). Publication rattachée à l'**Agents Week** de Cloudflare et étiquetée *Agents Week, AI, AI Bots, Developer Platform, Developers, Payments, Product News, x402*.

**Cloudflare** — l'éditeur est ici en position singulière : il n'est ni un laboratoire de modèles ni un acteur du commerce, mais l'**opérateur d'infrastructure** qui voit passer le trafic des deux côtés. C'est ce qui donne son sens à l'offre, présentée comme une pièce d'un ensemble : **Monetization Gateway** côté vendeurs (annoncé plus tôt dans le mois), **Wallets** côté acheteurs, **identité** pour l'attribution.

## Ton

**Profil** : **annonce produit d'infrastructure**, registre technique et posé, sans emphase commerciale. Format canonique du blog Cloudflare pendant une semaine thématique : problème concret → architecture → cas d'usage → position sur les standards → appel à réserver son handle.

**Style** : la construction est celle d'une **démonstration par la friction**. Le texte s'ouvre sur une séquence d'obstacles très concrète — page de connexion faite pour des humains, ajout manuel d'un moyen de paiement, génération de clé, découverte de l'API — avant d'en tirer les deux manques structurels. Le diagnostic est donc **observé avant d'être théorisé**, ce qui rend la suite difficile à contester.

**Trait notable : l'argument contre-intuitif assumé comme tel**, avec un chiffrage domestique qui le rend immédiatement intelligible — *« If an agent is responsible for $10, you can worry less about its spending than if it is responsible for $1,000. If an API only costs a few cents to try, then $10 is more than sufficient to pursue and evaluate many options. »* Cloudflare ne vend pas la contrainte comme un mal nécessaire, mais **comme la condition de l'autonomie**.

**Modestie affichée sur les standards** — et c'est le passage le plus habile du texte : *« We know that agentic identity standards are changing quickly, which is why we wanted to keep our approach simple… We are not trying to define a particular schema or other verification system. We only want to make identity simple to remember and easy to declare. »* Refuser de normaliser la sémantique **tout en occupant l'espace de noms** est une position confortable : on ne se met pas en travers des standards à venir, on se rend indispensable en amont d'eux.

**L'analogie qui porte le volet identité** est celle du **VPN** : *« If someone is unidentified, they are not inherently untrustworthy, but they need to prove themselves more. »* Elle évacue élégamment le procès en surveillance : ne pas se déclarer reste possible, cela coûte simplement plus de friction.

**Formules-marqueurs** : *« Agents do not have a stable identifier… and they do not have a native way to pay »*, *« kicking registration, payment methods, and API key generation back to humans »*, *« counterintuitively they give agents more freedom »*, *« the spending policies… did their job by imposing caps »*, *« a human-readable identifier for a not-very-readable keypair »*, *« a headless marketplace for the Internet »*.

## Pense-betes

- **Le diagnostic, en deux manques — la meilleure formulation vue du problème d'onboarding agentique** : *« Agents do not have a stable identifier to sign up for an API, and they do not have a native way to pay for APIs. »* Conséquence observée : les agents **abandonnent** et renvoient inscription, moyen de paiement et génération de clé à un humain. → **Ce n'est pas la capacité du modèle qui bloque l'essai d'une API, c'est l'absence d'identité et de moyen de paiement.** Argument transposable bien au-delà de Cloudflare.

- **L'architecture à deux étages, et pourquoi elle répond exactement à l'*ambient authority*** :
  | | **Account Wallet** | **Virtual Wallet** |
  |---|---|---|
  | Pour qui | l'humain, propriétaire du compte | l'agent |
  | Accès | interface de compte | **clé d'API** |
  | Peut | approvisionner, **déléguer**, retirer | dépenser dans la limite fixée |
  | Plafond | définit celui des Virtual Wallets | **fixé par le détenteur du compte** |
  | Garde-fous | — | allocation, liste d'autorisation, montant maximal par transaction |
  → C'est la réponse directe au problème d'**autorité ambiante** décrit dans [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] : là, l'agent hérite des permissions **complètes et surprovisionnées** de son humain ; ici il reçoit une **délégation bornée, avec un plafond explicite et révisable**. Même geste que la chaîne d'acteurs d'[[uber-engineering-agent-identity-crisis-zero-trust-spire-2026-05-21]], appliqué à l'argent plutôt qu'aux accès.

- **L'argument central, et il rejoint la thèse la plus établie du corpus** : *« These limits may seem like constraints, but counterintuitively they give agents more freedom. »* Le raisonnement : un agent responsable de 10 $ inquiète moins qu'un agent responsable de 1 000 $, et si essayer une API coûte quelques centimes, 10 $ suffisent à en évaluer beaucoup. → **On n'accorde d'autonomie qu'à hauteur de ce dont on accepte de perdre le contrôle.** C'est mot pour mot la règle de *back-pressure* de [[sfeir-code-review-anneau-contraintes-2026-07-30]] (*« on ne confie à une boucle que l'autonomie qu'on sait vérifier à faible coût »*), et le principe de l'exécutable de [[lassiege-usine-logicielle-heure-ia-2026-07-28]] — **transposé du code à la dépense**. Le plafond est ici l'équivalent du test qui casse la CI : une contrainte mécanique, pas une consigne.

- **La question « pour le compte de qui » enfin outillée** : les Virtual Wallets sont précisément le mécanisme qui répond à la distinction posée dans girard-acp-deux-protocoles-un-sigle-2026-08-02 — *« qui consomme, et pour le compte de qui »*. Un agent en Virtual Wallet dépense **des fonds explicitement délégués**, sous un plafond nominatif, et non le quota indifférencié de son propriétaire. **La ligne architecturale que je notais comme à trancher à la conception devient un objet de produit.**

- **Cas d'usage donné, immédiatement parlant en entreprise** : *« Want to give every employee a $100 per week budget for AI inference? »* — un Account Wallet approvisionné, un Virtual Wallet par salarié avec la règle. Dépassement → demande de dérogation manuelle à un humain habilité. Dépense anormalement rapide → revue humaine, puis relèvement du plafond ou injection ponctuelle si intentionnelle ; sinon *« the spending policies… did their job by imposing caps »*. → **Une politique FinOps de token qui s'exprime en règles de portefeuille plutôt qu'en tableau de bord a posteriori.** À rapprocher de gupta-token-budget-wars-marginal-token-utility-2026-05-28 et tokenomics-foundation-linux-finops-token-economics-about-2026-06-03.

- **Le rail : x402 + stablecoin — et c'est un positionnement, pas un détail technique.** Les paiements sont **attachés aux requêtes HTTP** (x402) et libellés en **stablecoins**, avec rampes d'entrée/sortie dans les géographies supportées et auto-approvisionnement en stablecoins pour les éligibles. → **Cloudflare n'entre pas dans le camp des schémas adossés aux réseaux de cartes**, contrairement à l'Agentic Commerce Protocol (OpenAI + Stripe) ou à l'Universal Commerce Protocol et l'Agent Payments Protocol côté Google. C'est **la thèse « permissionless » de ragsdale-merit-open-agentic-commerce-protocols-2026-03-19 qui se matérialise chez un opérateur d'infrastructure de premier plan** — Ragsdale rangeait justement les protocoles de plateforme du côté de l'« AOL du commerce agentique » face aux protocoles ouverts.
  **Désambiguïsation** : ne pas confondre avec l'Agentic Commerce Protocol ni l'Universal Commerce Protocol — trois camps distincts, cf. marette-agentic-commerce-optimization-acp-ucp-2026-02-23, thilen-opascope-ai-shopping-assistant-agentic-commerce-protocols-2026-02-10, google-agentic-commerce-ap2-payment-protocol-2025-09-16 et nrf-2026-commerce-agentique-ucp-deep-research-2026-01-13.

- **Le volet identité est le vrai enjeu stratégique — et il est plus gros que le portefeuille.** Le problème posé est commercial avant d'être technique : *« It's easy to give a one-week free trial or sign-up credits to a human or an organization. It's hard to give these same perks to an agent that lacks a stable identity and when one human can spin up dozens of agents under their control. »* La réponse est un **espace de noms**, `cloudflare.pay`, où un agent peut vivre à `research.example.cloudflare.pay` — identité **optionnelle**, déléguée du compte, persistante.
  → **Cloudflare se propose comme registraire de l'identité des agents.** L'analogie qu'il choisit lui-même est révélatrice : *« similar to the URL and IP-address pairings used in DNS »*. Comparer son nouvel espace de noms à **DNS** n'est pas une analogie modeste. **Celui qui tient la couche de noms lisibles tient un point de passage**, et l'affirmation de neutralité sémantique (*« we are not trying to define a particular schema »*) rend la position d'autant plus confortable : on n'entre en conflit avec aucun standard futur, on s'installe en amont.

- **L'analogie VPN, et ce qu'elle escamote** : *« If someone is unidentified, they are not inherently untrustworthy, but they need to prove themselves more. »* Élégante — elle préserve le droit à l'anonymat tout en le tarifant en friction. Mais dans un monde où Cloudflare arbitre déjà une part majeure du trafic (Turnstile, Bot Management), « prouver davantage » n'est pas une posture neutre : **le coût de l'anonymat est fixé par le même acteur qui vend l'identité**. Le texte dit que c'est aux entreprises de décider si elles privilégient les agents connus ; il ne dit pas qui décide de la difficulté de l'alternative. À lire avec scrapfly-browser-math-os-fingerprint-2026-07-12, côté détection.

- **Continuité technique revendiquée** : **Web Bot Auth** permet déjà à un agent d'enregistrer son identité **par paire de clés** ; Wallets ne fait qu'y ajouter une couche **lisible par un humain**. La formule est bonne — *« a human-readable identifier for a not-very-readable keypair »*. Adoption annoncée des schémas de la **x402 Foundation** à mesure qu'ils se développent, avec intention d'y encourager les autres.

- **Le statut du texte — la réserve à porter en tête de toute citation** : **presque tout est au futur.** Ce qui est disponible le 4 août, c'est la **réservation d'un handle**. Tout le reste — payer des API, créer des Virtual Wallets, poser des garde-fous, approvisionner — est annoncé : *« Soon, you will be able to set up and use your Cloudflare Wallet »*, *« Wallets will allow »*, *« We will start with simple ways to onramp and offramp »*. → **C'est une prise de position sur un espace de noms doublée d'une feuille de route, pas une mise en service.** Traiter les mécanismes comme une intention de conception documentée, jamais comme un dispositif éprouvé. Les garde-fous en particulier (allocation, liste d'autorisation, plafond par transaction) n'ont **aucun retour d'usage** à ce stade.

- **Autres points à ne pas laisser passer** :
  - **Le chiffre non sourcé** : *« with a majority of traffic on the web now being driven by bots »*. Affirmation lourde, aucune référence, chez un acteur qui a par ailleurs les données pour l'étayer (Radar). À ne pas reprendre sans source.
  - **Périmètre géographique** : rampes d'entrée/sortie *« within supported geographies »*, auto-approvisionnement en stablecoins *« for eligible users »*. Rien sur l'Europe, rien sur la conformité (KYC, DSP2, MiCA). Pour un lectorat européen, c'est **le premier obstacle de transposition** et le texte n'en dit rien.
  - **Concentration** : le même acteur fournirait le portefeuille de l'acheteur, la passerelle de monétisation du vendeur, l'identité des deux, et le contrôle de bot qui décide de la friction. *« All of these building blocks will create a headless marketplace for the Internet »* — la phrase est présentée comme une promesse d'écosystème ; elle décrit aussi une **intégration verticale complète d'un marché biface**.

- **Méta / à relier** : matérialise la thèse permissionless de ragsdale-merit-open-agentic-commerce-protocols-2026-03-19 face aux camps de plateforme ; répond en produit à l'autorité ambiante de valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20 et à l'identité déléguée d'uber-engineering-agent-identity-crisis-zero-trust-spire-2026-05-21 ; instrumente la distinction « pour le compte de qui » de girard-acp-deux-protocoles-un-sigle-2026-08-02 ; applique à la dépense la règle de back-pressure de sfeir-code-review-anneau-contraintes-2026-07-30 ; s'inscrit dans la stratégie agent-first de Cloudflare déjà vue dans martinho-allen-cloudflare-markdown-for-agents-2026-02-12 ; à confronter au volume d'agents anticipé par levie-building-trillions-agents-software-2026-03-07 et à la normalisation ouverte de openai-agentic-ai-foundation-linux-2025-12-09.

## RésuméDe400mots

Annonce publiée sur le blog **Cloudflare** le **4 août 2026** par **Will Papper**, pendant l'**Agents Week** : **Cloudflare Wallets**, *« the programmable wallet for the agentic Internet »*.

**Le problème.** Un agent qui veut essayer une API doit franchir une page de connexion conçue pour des humains, faire ajouter un moyen de paiement par un humain, générer une clé, puis découvrir l'API. Deux manques l'expliquent : *« Agents do not have a stable identifier to sign up for an API, and they do not have a native way to pay for APIs. »* Résultat, les agents abandonnent et renvoient tout à un humain.

**L'architecture.** Deux types de portefeuilles. Les **Account Wallets** appartiennent aux humains propriétaires d'un compte : approvisionner, déléguer, retirer. Les **Virtual Wallets** sont destinés aux agents, fonctionnent **par clé d'API**, et leur plafond est **fixé par le détenteur du compte** — avec allocation, liste d'autorisation et montant maximal par transaction. Le rail est le protocole **x402**, qui attache un paiement à une requête HTTP, et la monnaie est le **stablecoin** : un positionnement distinct des schémas adossés aux réseaux de cartes.

**L'argument central est contre-intuitif** : *« These limits may seem like constraints, but counterintuitively they give agents more freedom. If an agent is responsible for $10, you can worry less about its spending than if it is responsible for $1,000. »* Le plafond n'est pas ce qui bride l'autonomie, c'est ce qui la rend consentable — et si essayer une API coûte quelques centimes, dix dollars suffisent à en comparer beaucoup.

**Le second volet est l'identité**, et il est plus stratégique que le premier. Un agent peut vivre à `research.example.cloudflare.pay` : identité optionnelle, déléguée du compte, persistante, qui rend enfin attribuables les essais gratuits et crédits d'inscription. Cloudflare revendique une ambition minimale — *« a human-readable identifier for a not-very-readable keypair, similar to the URL and IP-address pairings used in DNS »* — en s'appuyant sur **Web Bot Auth** et en annonçant l'adoption des schémas de la **x402 Foundation**. L'analogie retenue est celle du VPN : n'être pas identifié ne rend pas suspect, cela oblige seulement à prouver davantage.

**Réserve dirimante** : presque tout est au futur. Ce qui existe le 4 août, c'est la **réservation d'un handle**. Les paiements, les portefeuilles virtuels, les garde-fous et les rampes de fonds sont annoncés. S'y ajoutent un chiffre non sourcé sur la majorité de trafic issue des bots, un silence complet sur la conformité européenne, et une intégration verticale où le même acteur fournirait le portefeuille, la passerelle marchande, l'identité et le contrôle de bot.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Cloudflare | ORGANISATION | publie | Cloudflare Wallets | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Will Papper | PERSONNE | travaille_chez | Cloudflare | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Will Papper | PERSONNE | affirme_que | les agents n'ont ni identifiant stable pour s'inscrire à une API ni moyen natif de la payer | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| absence d'identité et de moyen de paiement | CONCEPT | s_oppose_à | l'essai autonome d'une API par un agent, qui renvoie l'inscription à un humain | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Cloudflare Wallets | TECHNOLOGIE | utilise | x402 | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Cloudflare Wallets | TECHNOLOGIE | utilise | stablecoin | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Virtual Wallet | CONCEPT | permet | à un agent de dépenser des fonds explicitement délégués, sous un plafond fixé par le détenteur du compte | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Virtual Wallet | CONCEPT | réduit | le risque d'autorité ambiante, l'agent recevant une délégation bornée au lieu des permissions complètes de son humain | AFFIRMATION | 0.88 | ATEMPOREL | inféré |
| plafond de dépense | CONCEPT | permet | davantage d'autonomie à un agent, l'exploration devenant consentable parce que la perte maximale est bornée | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Cloudflare Wallets | TECHNOLOGIE | s_applique_à | l'achat d'API, d'outils Model Context Protocol et de contenu par des agents | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| cloudflare.pay | TECHNOLOGIE | permet | à un agent de déclarer une identité persistante et lisible, déléguée d'un compte | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| identité d'agent lisible | CONCEPT | résout | l'impossibilité d'attribuer essais gratuits et crédits d'inscription à un agent sans identité stable | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| cloudflare.pay | TECHNOLOGIE | est_basé_sur | Web Bot Auth | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Cloudflare | ORGANISATION | s_inspire_de | l'appariement entre URL et adresse IP dans le DNS | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Cloudflare | ORGANISATION | s_oppose_à | la définition d'un schéma de vérification propriétaire, préférant adopter ceux de la x402 Foundation | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Monetization Gateway | TECHNOLOGIE | permet | à un vendeur d'être payé sans infrastructure de paiement traditionnelle | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Cloudflare Wallets | TECHNOLOGIE | converge_avec | Monetization Gateway | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Cloudflare | ORGANISATION | affirme_que | l'ensemble portefeuille, passerelle de monétisation et identité formera un marché headless pour Internet | CITATION | 0.93 | DYNAMIQUE | déclaré_article |
| agent non identifié | CONCEPT | est_instance_de | un accédant non intrinsèquement suspect, mais tenu de prouver davantage — par analogie avec un VPN | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| Cloudflare Wallets | TECHNOLOGIE | fait_partie_de | Agents SDK | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Cloudflare | ORGANISATION | affirme_que | la majorité du trafic web est désormais produite par des bots | AFFIRMATION | 0.75 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Cloudflare Wallets | TECHNOLOGIE | définition | Portefeuille programmable annoncé le 4 août 2026 : un Account Wallet détenu par un humain délègue des fonds plafonnés à des Virtual Wallets opérés par des agents via clé d'API, pour payer API, outils et contenu en stablecoins par le protocole x402 | AJOUT |
| Cloudflare Wallets | TECHNOLOGIE | statut | Au 4 août 2026, seule la réservation d'un handle est disponible ; paiements, portefeuilles virtuels, garde-fous et rampes de fonds sont annoncés au futur | AJOUT |
| Virtual Wallet | CONCEPT | définition | Portefeuille destiné à un agent, opéré par clé d'API, dont l'allocation, la liste d'autorisation et le montant maximal par transaction sont fixés par le détenteur du compte humain | AJOUT |
| cloudflare.pay | TECHNOLOGIE | définition | Espace de noms proposé par Cloudflare donnant à un agent une identité lisible et persistante sous forme de sous-domaine délégué d'un compte, déclaration restant optionnelle | AJOUT |
| x402 | TECHNOLOGIE | rôle | Protocole attachant un paiement à une requête HTTP ; rail retenu par Cloudflare pour les micropaiements agentiques, distinct des schémas adossés aux réseaux de cartes | MISE_A_JOUR |
| Monetization Gateway | TECHNOLOGIE | définition | Offre Cloudflare permettant à un client de vendre contenu et API à des acheteurs agentiques sans infrastructure de paiement traditionnelle ; versant vendeur du dispositif dont Wallets est le versant acheteur | AJOUT |
| Web Bot Auth | TECHNOLOGIE | rôle | Mécanisme préexistant d'enregistrement d'identité d'agent par paire de clés, auquel Cloudflare Wallets ajoute une couche lisible par un humain | AJOUT |
| Cloudflare | ORGANISATION | positionnement | Opérateur d'infrastructure se dotant simultanément du portefeuille acheteur, de la passerelle vendeur, de l'espace de noms d'identité et du contrôle de bot qui fixe la friction des agents non identifiés | MISE_A_JOUR |
| Will Papper | PERSONNE | rôle | Auteur de l'annonce Cloudflare Wallets sur le blog Cloudflare, Agents Week 2026 | AJOUT |
