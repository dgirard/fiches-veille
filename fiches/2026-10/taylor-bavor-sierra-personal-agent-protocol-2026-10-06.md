---
themes: [produits-services, outils-plateformes, strategie-frameworks]
source: "Sierra"
---
# taylor-bavor-sierra-personal-agent-protocol-2026-10-06

## Veille

Billet de blog de **Bret Taylor** et **Clay Bavor** (cofondateurs de **Sierra**), publié le **6 octobre 2026** sur sierra.ai, en lien avec le Sierra Summit 2026 ; texte court (~700 mots). Il annonce le **Personal Agent Protocol**, standard ouvert en cours de développement par **Meta** et **Sierra** avec **Genesys, Instinct, Rocket, Shopify, Stripe et Walmart**, qui définit comment les agents personnels des consommateurs interagissent avec les entreprises.

**(1)** Problème : les agents personnels utilisent aujourd'hui sites et apps comme des humains (pages, formulaires), ou appellent le support ; une connexion directe ferait la même tâche en quelques secondes. Trois besoins sont énoncés : consommateurs (vitesse, confiance), marques (visibilité et contrôle), éditeurs d'agents (accès direct et homogène). **(2)** Fonctionnement : le consommateur décide de l'accès accordé à son agent, l'entreprise fixe ce que l'agent peut faire. La découverte part du site ; la session démarre en invité puis peut s'authentifier (lecture seule ou écriture), est **fondée sur OAuth** et traverse les canaux. L'agent passe par le **site**, les **API** (MCP, OpenAPI) ou l'**agent de l'entreprise** (cas d'une réclamation de garantie). **(3)** Suite : spécification **v0.1 prévue en octobre**, ateliers de conception, implémentation de référence ; extensions envisagées : permissions fines, notifications push, paiements sans partage de carte. Citations de **Tony Bates** (Genesys), **Shawn Malhotra** (Rocket), **Mani Fazeli** (Shopify), **Kevin Miller** (Stripe). Le billet ne détaille ni le format des messages, ni la gouvernance, ni le calendrier au-delà de la v0.1.

Rapproche le protocole des standards de [[google-agentic-commerce-ap2-payment-protocol-2025-09-16]] et [[girard-acp-deux-protocoles-un-sigle-2026-08-02]].

## Titre Article

Introducing Personal Agent Protocol

## Date

2026-10-06

## URL

https://sierra.ai/blog/introducing-personal-agent-protocol

## Keywords

Personal Agent Protocol, standard ouvert, agents personnels, Sierra, Meta, Genesys, Instinct, Rocket, Shopify, Stripe, Walmart, OAuth, MCP, OpenAPI, authentification des agents, commerce agentique, service client, agent d'entreprise, permissions, spécification v0.1

## Authors

Bret Taylor et Clay Bavor — cofondateurs de Sierra, plateforme d'agents IA pour l'expérience client ; billet du blog Sierra.

## Ton

Profil : annonce de produit et de partenariat d'un éditeur, adressée aux entreprises et aux développeurs d'agents. Le texte part d'un constat grand public (les agents personnels « prennent le monde d'assaut »), pose trois besoins parallèles (consommateurs, marques, éditeurs d'agents), décrit le mécanisme en peu d'étapes, puis annonce un calendrier et des extensions possibles au conditionnel. Quatre citations de partenaires closent le billet. Le standard est présenté comme en cours de construction et ouvert à tout implémenteur.

## Pense-betes

- **Quoi** : standard ouvert pour l'interaction entre agents personnels et entreprises ; portage Meta + Sierra, partenaires Genesys, Instinct (rejoint l'effort), Rocket, Shopify, Stripe, Walmart.
- **Principe** : le consommateur choisit l'accès donné à son agent (lecture seule ou écriture) ; l'entreprise définit ce que l'agent peut faire et par quelle voie.
- **Session** : découverte depuis le site, démarrage en invité, connexion sur la page de l'entreprise ou via des identifiants déjà liés à l'agent ; fondée sur **OAuth**, continue d'un canal à l'autre (une question avant connexion et une modification de commande après relèvent de la même visite).
- **Trois voies d'accès** : site web ; API sur standards tels que **MCP** et **OpenAPI** ; agent de l'entreprise pour les tâches conversationnelles.
- **Calendrier** : v0.1 de la spécification « plus tard ce mois-ci », ateliers de conception, implémentation de référence.
- **Extensions envisagées** : permissions plus fines par action, notifications push (vol retardé, commande expédiée), extensions de paiement sans communiquer la carte.
- ⚠️ **Portée** : annonce sans spécification publiée ; ni format de protocole, ni gouvernance, ni modèle d'identification de l'agent côté marque ne sont décrits.

## RésuméDe400mots

Le 6 octobre 2026, Bret Taylor et Clay Bavor, cofondateurs de Sierra, annoncent le Personal Agent Protocol, un standard ouvert que Meta et Sierra développent avec Genesys, Instinct, Rocket, Shopify, Stripe et Walmart. Il vise à définir comment les agents personnels des consommateurs interagissent avec les entreprises : authentification, pouvoir donné au consommateur et visibilité pour l'entreprise sur ce que font ces agents, que ce soit par son site, ses API ou ses propres agents.

Le billet part d'un constat : la plupart des agents personnels utilisent aujourd'hui sites et applications comme le ferait une personne, en chargeant des pages et en remplissant des formulaires, et se rabattent parfois sur la ligne de support ou le chat. Cela prend du temps et la tâche peut échouer, alors qu'une connexion directe la réaliserait en quelques secondes. Pour être adoptée, elle doit servir trois parties : les consommateurs veulent rapidité, fiabilité et confiance, les marques veulent savoir quand un agent agit pour un client et décider de ce qu'il peut faire, et les éditeurs d'agents veulent un accès direct et homogène aux entreprises participantes.

Le principe retenu est que le consommateur décide de l'accès donné à son agent et que l'entreprise fixe les paramètres de ce que l'agent peut faire. Le protocole commence sur le site, où l'agent découvre l'offre et les moyens de joindre l'entreprise, puis ouvre une session pour le compte de son utilisateur. Il peut démarrer en invité, ce qui suffit pour vérifier une disponibilité ou une politique de retour. Si la tâche exige l'accès au compte, le client se connecte sur la page de l'entreprise ou utilise des identifiants déjà configurés auprès de son agent, et choisit entre lecture seule et écriture. La session repose sur OAuth et se poursuit d'un canal à l'autre. L'agent peut ensuite agir par le site web, par des API fondées sur des standards comme MCP et OpenAPI, ou par l'agent de l'entreprise pour les tâches conversationnelles comme une réclamation de garantie. L'entreprise choisit ce qu'elle expose.

Pour la suite, les auteurs prévoient de publier la version 0.1 de la spécification avant la fin du mois, d'organiser des ateliers de conception et de fournir une implémentation de référence. Ils évoquent des permissions plus détaillées par action, des notifications push (retard de vol, expédition d'une commande) et des extensions de paiement permettant d'acheter sans partager de numéro de carte.

Des responsables de Genesys, Rocket, Shopify et Stripe commentent l'annonce. Genesys parle d'une « nouvelle porte d'entrée de l'entreprise » où les marques doivent savoir qui représente l'agent, ses autorisations et son intention. Rocket décrit un agent Muse développé avec Sierra qui se déplace sur sa plateforme, de la recherche d'un logement au financement. Shopify y voit une nouvelle frontière du service client, et Stripe un moyen de reconnaître les agents des clients et d'interagir efficacement avec eux.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Meta | ORGANISATION | collabore_avec | Sierra | ORGANISATION | 0.97 | STATIQUE | déclaré_article |
| Sierra | ORGANISATION | publie | Personal Agent Protocol | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Meta | ORGANISATION | a_créé | Personal Agent Protocol | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Sierra | ORGANISATION | collabore_avec | Shopify | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Sierra | ORGANISATION | collabore_avec | Stripe | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Sierra | ORGANISATION | collabore_avec | Walmart | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Sierra | ORGANISATION | collabore_avec | Genesys | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Sierra | ORGANISATION | collabore_avec | Rocket | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Instinct | ORGANISATION | collabore_avec | Sierra | ORGANISATION | 0.90 | STATIQUE | déclaré_article |
| Bret Taylor | PERSONNE | travaille_chez | Sierra | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Clay Bavor | PERSONNE | travaille_chez | Sierra | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Personal Agent Protocol | TECHNOLOGIE | utilise | OAuth | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Personal Agent Protocol | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Personal Agent Protocol | TECHNOLOGIE | utilise | OpenAPI | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Personal Agent Protocol | TECHNOLOGIE | résout | accès des agents personnels aux entreprises par pages et formulaires | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Personal Agent Protocol | TECHNOLOGIE | permet | visibilité des entreprises sur les actions des agents personnels | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Sierra | ORGANISATION | recommande | que le consommateur décide de l'accès de son agent et l'entreprise de ses actions permises | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Sierra | ORGANISATION | prédit | extensions de permissions fines, notifications push et paiements sans partage de carte | AFFIRMATION | 0.80 | DYNAMIQUE | déclaré_article |
| Tony Bates | PERSONNE | affirme_que | l'IA personnelle crée une nouvelle porte d'entrée de l'entreprise | CITATION | 0.93 | STATIQUE | déclaré_article |
| Tony Bates | PERSONNE | travaille_chez | Genesys | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Personal Agent Protocol | TECHNOLOGIE | catégorie | Standard ouvert d'interaction entre agents personnels et entreprises ; annoncé le 6 octobre 2026, spécification v0.1 prévue en octobre | AJOUT |
| Sierra | ORGANISATION | secteur | Plateforme d'agents IA pour l'expérience client | AJOUT |
| Meta | ORGANISATION | secteur | Partenaire de développement du protocole | AJOUT |
| Instinct | ORGANISATION | secteur | Rejoint l'effort annoncé | AJOUT |
| Shopify | ORGANISATION | secteur | Commerce en ligne ; partenaire du protocole | AJOUT |
| Stripe | ORGANISATION | secteur | Paiements ; partenaire du protocole | AJOUT |
| Genesys | ORGANISATION | secteur | Expérience client ; partenaire du protocole | AJOUT |
| Rocket | ORGANISATION | secteur | Immobilier et financement ; partenaire du protocole | AJOUT |
| Walmart | ORGANISATION | secteur | Distribution ; partenaire du protocole | AJOUT |
| Bret Taylor | PERSONNE | rôle | Cofondateur de Sierra | AJOUT |
| Clay Bavor | PERSONNE | rôle | Cofondateur de Sierra | AJOUT |
| Tony Bates | PERSONNE | rôle | Chairman et CEO de Genesys | AJOUT |
| OAuth | TECHNOLOGIE | catégorie | Standard d'autorisation d'accès, base des sessions du protocole | AJOUT |
| MCP | TECHNOLOGIE | catégorie | Standard d'API cité pour l'accès des agents | AJOUT |
| OpenAPI | TECHNOLOGIE | catégorie | Standard d'API cité pour l'accès des agents | AJOUT |
