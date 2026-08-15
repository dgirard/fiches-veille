---
themes: [economie-marche, outils-plateformes, qualite-securite]
source: "Stripe"
---
# hill-stripe-link-wallet-agents-issuing-2026-04-29

## Veille

Annonce produit publiée sur le blog **Stripe** le **29 avril 2026** par **Dan Hill** (Product Manager, Link Consumer Product), dans le prolongement de la keynote **Stripe Sessions 2026** : le lancement du **portefeuille Link pour les agents**, bâti sur une brique nouvelle, **Issuing for agents**. **Le diagnostic tient en une phrase, et c'est la plus importante du texte** : *« While machine payments protocols are still gaining adoption, agents need to work with the payment options sellers and consumers use today. »* → **Stripe acte que les protocoles de paiement machine-natifs ne sont pas prêts, et livre un contournement des rails existants plutôt qu'un pari sur les nouveaux.** **Le mécanisme** : un consommateur donne à un agent l'accès à son portefeuille Link par un **flux OAuth standard** ; l'agent émet ensuite une *spend request* et reçoit soit une **carte à usage unique**, soit un **Shared Payment Token** — adossés aux cartes et comptes bancaires déjà présents dans le portefeuille. Point cardinal : *« The agent never gets access to your raw payment credentials. »* Le justificatif est **scopé** (montant, devise, marchand) et l'agent doit fournir le **contexte de la transaction** pour que l'humain comprenne ce qu'il approuve — l'exemple donné en CLI est explicite : `amount 3500`, `merchant-name "Powdur"`, `context "Purchasing the Powdur Glow Renewal Vitamin C Serum as a gift for $35."`. **La contrainte structurante est temporelle et assumée** : *« Today, each request requires the person's review before the credential is shared with your agent »* — approbation **humaine, transaction par transaction**, sur le web ou dans les **nouvelles applications iOS et Android** de Link. Les limites de dépense et les cas où l'agent agirait **sans approbation supplémentaire** sont annoncés, pas livrés. **Le second étage est le vrai produit d'infrastructure** : **Issuing for agents** ouvre l'ensemble des API Issuing à qui veut bâtir son propre portefeuille agentique — cartes virtuelles à usage unique, stockage de fonds, contrôles de dépense, permissions au niveau de la carte, contrôles antifraude **à l'autorisation**, visibilité temps réel. Quatre débouchés sont cités : automatisation de la dépense interne, cartes agentiques encastrées chez les **fintechs**, plateformes **SaaS verticales** émettant des cartes aux PME sous leur marque, **places de marché** dont les agents vendeurs paient fournisseurs et logistique. **Argument de distribution** : Link revendique **plus de 200 millions de consommateurs**, et l'article cite **OpenClaw** comme exemple d'agent personnel bénéficiaire. ⚠️ **Deux réserves à porter en tête** : l'approbation par transaction est présentée comme une commodité de conception alors qu'elle est **l'aveu que l'autorisation déléguée d'un agent n'est pas résolue** ; et le stablecoin, les *agentic tokens* et « d'autres moyens de paiement » sont tous au **futur** (*« coming soon »*).

## Titre Article

Giving agents the ability to pay

## Date

2026-04-29

## URL

https://stripe.com/blog/giving-agents-the-ability-to-pay

## Keywords

Stripe, Link, portefeuille pour agents, Issuing for agents, commerce agentique, carte à usage unique, carte virtuelle, Shared Payment Token, justificatif de paiement, credential scopé, spend request, demande de dépense, approbation humaine, revue par transaction, contexte de transaction, OAuth, délégation de paiement, plafond de dépense, contrôle de dépense, permissions au niveau de la carte, contrôle antifraude à l'autorisation, monitoring de transaction, rails de cartes, protocole de paiement machine-natif, Agentic Commerce Protocol, stablecoin, agentic token, Link iOS, Link Android, 200 millions de consommateurs, OpenClaw, agent personnel, agent de shopping, fintech, SaaS vertical, place de marché, gestion de note de frais, dépense programmatique, achat récurrent, Stripe Sessions 2026, Dan Hill, infrastructure économique de l'IA

## Authors

**Dan Hill** — Product Manager, **Link Consumer Product** chez Stripe. Auteur de l'annonce sur le blog Stripe, rubrique *Product*. Le rattachement au produit *Link Consumer* est significatif : l'annonce est écrite depuis le **portefeuille grand public**, pas depuis l'équipe protocole ni depuis Issuing — ce qui explique que le consentement de l'utilisateur final structure tout le texte.

**Stripe** — position singulière dans le paysage du commerce agentique : co-auteur avec **OpenAI** de l'**Agentic Commerce Protocol** (29 septembre 2025), et simultanément **émetteur** (Issuing) et **portefeuille** (Link). L'entreprise n'est donc pas seulement un participant au débat sur les protocoles : elle détient les rails que ces protocoles prétendent remplacer. L'annonce est explicitement rattachée à la keynote **Stripe Sessions 2026**.

## Ton

**Profil** : **annonce produit d'infrastructure de paiement**, registre sobre et opérationnel, sans emphase prospective. Format court, canonique du blog Stripe : contexte → lancement → « comment ça marche » en trois temps illustrés → brique sous-jacente → cas d'usage → appel à la documentation.

**Style** : la **démonstration passe par le déroulé d'une transaction**, pas par l'argumentation. Stripe pose un scénario concret (un agent de shopping qui recommande des vêtements), puis fait défiler les trois étapes — OAuth, *spend request*, approbation — avec deux captures et **un extrait de CLI**. Le code est ici l'argument : voir `link-cli spend-request create` avec ses paramètres `merchant-name`, `amount`, `context`, `request-approval` en dit plus long que n'importe quelle promesse d'architecture. **On montre une commande qui existe plutôt qu'un schéma qui existera.**

**Trait le plus notable : la lucidité sur les protocoles.** *« While machine payments protocols are still gaining adoption, agents need to work with the payment options sellers and consumers use today. »* Venant du **co-auteur de l'Agentic Commerce Protocol**, la phrase est remarquable de franchise — Stripe constate publiquement que le standard qu'il promeut n'a pas encore la traction nécessaire, et livre le contournement. **Ce n'est pas une contradiction, c'est une couverture de risque.**

**La sécurité est formulée en négatif**, ce qui la rend plus crédible qu'une promesse : *« The agent never gets access to your raw payment credentials. »* On ne dit pas ce que le système protège, on dit ce que l'agent **n'obtient jamais**.

**Le futur est cantonné et honnête** : *« We're planning on expanding these controls to let people set spending limits, and choose when agents can act without additional approval »*, *« Support for agentic tokens, stablecoins, and other payment types are coming soon. »* Contrairement à beaucoup d'annonces du secteur, la part livrée et la part promise sont **nettement séparées** — le lecteur sait ce qu'il peut utiliser aujourd'hui.

**Formules-marqueurs** : *« agents are becoming active participants in the internet economy »*, *« making purchases across the internet remains difficult »*, *« The agent never gets access to your raw payment credentials »*, *« Today, each request requires the person's review »*, *« removes the need to build wallet infrastructure from scratch »*.

## Pense-betes

- **⭐⭐ La phrase à retenir de toute l'annonce, et elle contredit le camp de son propre auteur** : *« While machine payments protocols are still gaining adoption, agents need to work with the payment options sellers and consumers use today. »* → **Stripe, co-auteur de l'Agentic Commerce Protocol, constate publiquement que les protocoles machine-natifs ne sont pas prêts et livre un adaptateur vers les rails de cartes existants.** La carte à usage unique n'est pas une solution de paiement agentique : c'est une **cale de compatibilité** qui rend la guerre des protocoles temporairement sans objet pour le marchand, qui ne voit passer qu'une carte ordinaire. À confronter directement à [[girard-acp-deux-protocoles-un-sigle-2026-08-02]] (trois protocoles pour un sigle) et à [[marette-agentic-commerce-optimization-acp-ucp-2026-02-23]].

- **⭐⭐ L'approbation par transaction est le cœur du dispositif — et c'est un aveu, pas une commodité.** *« Today, each request requires the person's review before the credential is shared with your agent. »* Un humain valide **chaque** dépense, avec le contexte fourni par l'agent. → **Tant que l'identité et l'autorisation d'un agent ne sont pas résolues, l'ancre de confiance reste humaine et se paie en interruption par transaction.** C'est le problème d'identité agentique de [[uber-engineering-agent-identity-crisis-zero-trust-spire-2026-05-21]] et l'autorité ambiante de [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]], non pas résolus mais **déplacés vers l'humain**. ⚠️ Conséquence directe pour le dimensionnement : **le modèle ne passe pas à l'échelle d'un agent qui achète souvent** — il vise l'achat ponctuel et significatif, pas le micropaiement.

- **⭐ La comparaison avec Cloudflare Wallets est le meilleur angle de lecture, et l'antériorité compte.** Stripe publie le **29 avril 2026**, Cloudflare le **4 août 2026** ([[cloudflare-wallets-agentic-commerce-2026-08-04]]) — trois mois plus tard, sur le même problème, avec des choix opposés :
  | | **Stripe — Link wallet for agents** | **Cloudflare — Wallets** |
  |---|---|---|
  | Rail | **cartes** (usage unique) + Shared Payment Token | **x402** (paiement sur requête HTTP) |
  | Monnaie | cartes et comptes bancaires existants | **stablecoin** |
  | Autorisation | **approbation humaine par transaction** | **plafond** fixé une fois, puis autonomie |
  | Identité de l'agent | déléguée par **OAuth** depuis le compte humain | espace de noms `cloudflare.pay` |
  | Statut à l'annonce | **livré** (CLI, apps iOS/Android) | **réservation de handle**, reste au futur |
  | Cible | achat consommateur chez un marchand | achat d'API et d'outils par l'agent |
  → **Deux réponses opposées à la même question : Stripe borne par le consentement répété, Cloudflare par le plafond consenti une fois.** La seconde suppose l'identité d'agent résolue ; la première s'en passe. Et le rapprochement est instructif dans les deux sens : le principe de [[sfeir-code-review-anneau-contraintes-2026-07-30]] — *« on ne confie à une boucle que l'autonomie qu'on sait vérifier à faible coût »* — est ici respecté par **le prix maximal, pas par le plafond** : chaque justificatif est scopé en montant, devise et marchand, donc la perte maximale par transaction est bornée **même si l'humain approuve mal**.

- **⭐ Le contexte comme obligation de l'agent — un détail de conception qui mérite d'être repris.** L'agent doit fournir la raison de la dépense pour que l'humain puisse trancher : `context "Purchasing the Powdur Glow Renewal Vitamin C Serum as a gift for $35."` → **L'approbation n'est utile que si elle est informée ; exiger du demandeur qu'il produise la justification est un pattern transposable bien au-delà du paiement** (approbation d'un déploiement, d'un accès, d'une action irréversible). À rapprocher de la logique d'*exit criteria* vérifiables du corpus ADLC.

- **Le vrai produit d'infrastructure est le second étage, pas le premier.** *« Link's wallet for agents is built directly on top of Stripe's Issuing primitives. »* **Issuing for agents** expose les API à qui veut construire son propre portefeuille : cartes virtuelles à usage unique, stockage de fonds, contrôles de dépense, permissions **au niveau de la carte**, contrôles antifraude **à l'autorisation de la transaction**, visibilité historique et temps réel. → **Stripe vend deux choses à deux publics : un portefeuille fini aux agents grand public, et les primitives d'émission à ceux qui veulent le leur.** C'est le geste classique de la plateforme — occuper le produit ET la couche en dessous.

- **Les quatre débouchés cités, et ce qu'ils révèlent du marché visé** : (1) développeurs automatisant leur **propre** dépense d'entreprise par workflows programmatiques et achats récurrents ; (2) **fintechs** encastrant des cartes émises à des agents pour réconcilier la note de frais en temps réel ; (3) **plateformes SaaS verticales** émettant des cartes agentiques à leurs clients PME sous leur propre marque ; (4) **places de marché** émettant aux vendeurs, dont les agents automatisent paiements fournisseurs, logistique et approvisionnement. → **Trois des quatre sont B2B et passent par un intermédiaire.** Le portefeuille grand public sert de vitrine ; **la monétisation visée est l'émission déléguée**.

- **Distribution revendiquée** : *« helps you reach Link's customer base of more than 200 million consumers »*, et le portefeuille *« removes the need to build wallet infrastructure from scratch »* pour qui construit un agent grand public. → L'argument n'est pas technique mais **d'amorçage** : le problème d'un portefeuille agentique n'est pas de le coder, c'est d'avoir des utilisateurs qui y ont déjà une carte enregistrée. ⚠️ Chiffre déclaratif, non sourcé dans l'article, et **« customer base » de Link ≠ utilisateurs actifs du portefeuille agentique** — ne pas le citer comme une adoption.

- **⚠️ Ce que l'article ne dit pas, et qu'il faut poser en question ouverte** :
  - **Rien sur la responsabilité en cas d'achat erroné.** Un agent obtient un justificatif approuvé, se trompe de produit ou de quantité : qui supporte ? Le texte parle de contrôles antifraude à l'autorisation, jamais de **recours après une transaction régulièrement autorisée**. C'est pourtant le risque propre à l'agentique — la fraude est un problème connu, **l'erreur de mandat ne l'est pas**.
  - **Rien sur l'Europe, ni sur la DSP2 / l'authentification forte.** Une approbation dans l'app Link satisfait-elle le SCA ? Question dirimante pour toute transposition européenne, absente du texte.
  - **Rien sur ce que le marchand voit.** Une carte à usage unique le laisse dans l'ignorance qu'un agent a acheté — commodité d'adoption immédiate, mais elle prive le marchand de toute politique agent-aware, à rebours de ce que visent l'Agentic Commerce Protocol et l'Universal Commerce Protocol.
  - **`OpenClaw` cité comme exemple d'agent personnel** : mention non commentée, à vérifier avant réemploi.

- **Méta / à relier** : contrepoint le plus direct à [[cloudflare-wallets-agentic-commerce-2026-08-04]] (cartes + approbation vs x402 + plafond) ; matérialise côté rails établis ce que [[ragsdale-merit-open-agentic-commerce-protocols-2026-03-19]] range du côté des protocoles de plateforme ; déplace vers l'humain le problème d'identité d'[[uber-engineering-agent-identity-crisis-zero-trust-spire-2026-05-21]] et l'autorité ambiante de [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] ; à lire avec la désambiguïsation des protocoles de [[girard-acp-deux-protocoles-un-sigle-2026-08-02]], [[marette-agentic-commerce-optimization-acp-ucp-2026-02-23]] et [[google-agentic-commerce-ap2-payment-protocol-2025-09-16]] ; ordre de grandeur du marché adressé dans [[levie-building-trillions-agents-software-2026-03-07]] et [[nrf-2026-commerce-agentique-ucp-deep-research-2026-01-13]] ; autre facette de Stripe en tant qu'utilisateur d'agents dans [[gray-stripe-minions-coding-agents-part1-2026-02-09]].

## RésuméDe400mots

Annonce publiée sur le blog **Stripe** le **29 avril 2026** par **Dan Hill**, Product Manager Link Consumer Product, dans le prolongement de la keynote **Stripe Sessions 2026** : le **portefeuille Link pour les agents**, bâti sur **Issuing for agents**.

**Le diagnostic.** Les agents sont devenus capables, mais acheter sur Internet leur reste difficile. Et surtout : *« While machine payments protocols are still gaining adoption, agents need to work with the payment options sellers and consumers use today. »* Venant du **co-auteur de l'Agentic Commerce Protocol**, le constat est notable — Stripe reconnaît que les protocoles machine-natifs n'ont pas la traction requise et livre un **adaptateur vers les rails existants**.

**Le mécanisme.** Le consommateur donne à l'agent l'accès à son portefeuille Link par un **flux OAuth standard**. L'agent émet ensuite une *spend request* et obtient soit une **carte à usage unique**, soit un **Shared Payment Token**, adossés aux cartes et comptes bancaires déjà enregistrés. *« The agent never gets access to your raw payment credentials. »* Le justificatif est **scopé** en montant, devise et marchand, et l'agent doit joindre le **contexte** de la transaction — l'exemple en CLI porte sur un sérum à 35 $ acheté en cadeau. Le consommateur approuve sur le web ou dans les **nouvelles applications iOS et Android** de Link, puis suit la dépense et gère les agents connectés.

**La contrainte est assumée** : *« Today, each request requires the person's review before the credential is shared with your agent. »* Une approbation humaine **par transaction**. Les limites de dépense et les cas d'action sans approbation supplémentaire sont **annoncés, pas livrés** — comme les *agentic tokens*, les stablecoins et les autres moyens de paiement.

**Le second étage.** **Issuing for agents** ouvre les API Issuing à qui veut bâtir son propre portefeuille agentique : cartes virtuelles à usage unique, stockage de fonds, contrôles de dépense, permissions au niveau de la carte, contrôles antifraude **à l'autorisation**, visibilité temps réel. Quatre débouchés sont cités — automatisation de la dépense interne, cartes encastrées chez les **fintechs** pour la note de frais, **plateformes SaaS verticales** émettant aux PME sous leur marque, **places de marché** dont les agents vendeurs paient fournisseurs et logistique. Trois sur quatre sont B2B : **la monétisation visée est l'émission déléguée**, le portefeuille grand public servant de vitrine et d'amorçage — Link revendique **plus de 200 millions de consommateurs**.

⚠️ **Réserves.** L'approbation par transaction est présentée comme une commodité alors qu'elle est **l'aveu que l'autorisation déléguée d'un agent n'est pas résolue** ; elle interdit de fait le micropaiement. L'article est par ailleurs muet sur la **responsabilité en cas d'achat erroné mais régulièrement autorisé**, sur la **conformité européenne** (DSP2, authentification forte), et sur le fait que le marchand, ne voyant qu'une carte ordinaire, perd toute politique agent-aware.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Stripe | ORGANISATION | publie | Link wallet for agents | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Stripe | ORGANISATION | publie | Issuing for agents | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Dan Hill | PERSONNE | travaille_chez | Stripe | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| Dan Hill | PERSONNE | affirme_que | les protocoles de paiement machine-natifs gagnent encore en adoption, donc les agents doivent composer avec les moyens de paiement utilisés aujourd'hui | CITATION | 0.97 | DYNAMIQUE | déclaré_article |
| Link wallet for agents | TECHNOLOGIE | est_basé_sur | Issuing for agents | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Link wallet for agents | TECHNOLOGIE | utilise | carte à usage unique | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Link wallet for agents | TECHNOLOGIE | utilise | Shared Payment Token | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Link wallet for agents | TECHNOLOGIE | utilise | OAuth | TECHNOLOGIE | 0.94 | ATEMPOREL | déclaré_article |
| carte à usage unique | CONCEPT | permet | à un agent de payer sans jamais accéder aux identifiants de paiement bruts du consommateur | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| carte à usage unique | CONCEPT | résout | l'incompatibilité entre agents et rails de paiement existants, sans attendre l'adoption d'un protocole machine-natif | AFFIRMATION | 0.90 | ATEMPOREL | inféré |
| justificatif de paiement scopé | CONCEPT | réduit | la perte maximale d'une transaction agentique, le montant, la devise et le marchand étant bornés à l'émission | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| approbation humaine par transaction | METHODOLOGIE | fait_partie_de | Link wallet for agents | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| approbation humaine par transaction | METHODOLOGIE | s_oppose_à | le micropaiement agentique, dont la fréquence rend la revue humaine impraticable | AFFIRMATION | 0.86 | ATEMPOREL | inféré |
| approbation humaine par transaction | METHODOLOGIE | est_instance_de | une ancre de confiance restée humaine faute d'autorisation déléguée d'agent résolue | AFFIRMATION | 0.88 | DYNAMIQUE | inféré |
| contexte de transaction fourni par l'agent | CONCEPT | permet | à l'humain d'approuver une dépense en comprenant ce qu'il autorise | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Issuing for agents | TECHNOLOGIE | permet | à une entreprise de bâtir son propre portefeuille agentique avec contrôles de dépense, permissions par carte et antifraude à l'autorisation | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Issuing for agents | TECHNOLOGIE | s_applique_à | l'émission de cartes agentiques par les fintechs, les plateformes SaaS verticales et les places de marché | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| Link wallet for agents | TECHNOLOGIE | s_applique_à | les agents personnels grand public effectuant un achat autorisé pour le compte de leur utilisateur | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| OpenClaw | TECHNOLOGIE | utilise | Link wallet for agents | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Stripe | ORGANISATION | a_créé | Agentic Commerce Protocol | TECHNOLOGIE | 0.93 | STATIQUE | généré_assistant |
| Link wallet for agents | TECHNOLOGIE | concurrence | Cloudflare Wallets | TECHNOLOGIE | 0.88 | DYNAMIQUE | inféré |
| Link wallet for agents | TECHNOLOGIE | s_oppose_à | le pari sur un rail machine-natif, en adossant la dépense agentique aux réseaux de cartes existants | AFFIRMATION | 0.89 | DYNAMIQUE | inféré |
| Stripe | ORGANISATION | mesure | plus de 200 millions de consommateurs dans la base clients de Link | MESURE | 0.80 | DYNAMIQUE | déclaré_article |
| Stripe Sessions 2026 | EVENEMENT | référence | Link wallet for agents | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| limites de dépense sans approbation | CONCEPT | est_instance_de | une capacité annoncée mais non livrée au 29 avril 2026 | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Link wallet for agents | TECHNOLOGIE | définition | Portefeuille Stripe lancé le 29 avril 2026 donnant à un agent un accès programmatique à Link par OAuth : sur demande de dépense approuvée par l'humain, l'agent reçoit une carte à usage unique ou un Shared Payment Token adossé aux moyens de paiement déjà enregistrés, sans jamais accéder aux identifiants bruts | AJOUT |
| Link wallet for agents | TECHNOLOGIE | statut | Livré au 29 avril 2026 (CLI, applications iOS et Android) ; les limites de dépense, l'action sans approbation supplémentaire, les agentic tokens et les stablecoins sont annoncés au futur | AJOUT |
| Issuing for agents | TECHNOLOGIE | définition | Brique Stripe exposant les API Issuing pour construire des portefeuilles et cartes agentiques sur mesure : cartes virtuelles à usage unique, stockage de fonds, contrôles de dépense, permissions au niveau de la carte, antifraude à l'autorisation, visibilité temps réel | AJOUT |
| carte à usage unique | CONCEPT | rôle | Cale de compatibilité entre agents et rails de cartes existants : le marchand ne voit qu'une carte ordinaire, ce qui dispense d'attendre l'adoption d'un protocole de paiement machine-natif mais le prive de toute politique agent-aware | AJOUT |
| Shared Payment Token | TECHNOLOGIE | définition | Justificatif de paiement machine-natif, alternative à la carte à usage unique dans le portefeuille Link pour agents, scopable en montant, devise et marchand | AJOUT |
| approbation humaine par transaction | METHODOLOGIE | définition | Règle de fonctionnement du portefeuille Link pour agents au lancement : chaque demande de dépense est revue et approuvée par la personne avant que le justificatif ne soit transmis à l'agent, sur le web ou dans l'application Link | AJOUT |
| approbation humaine par transaction | METHODOLOGIE | limite | Borne l'usage à l'achat ponctuel et significatif : la fréquence d'un agent micro-payeur rendrait la revue impraticable | AJOUT |
| contexte de transaction fourni par l'agent | CONCEPT | définition | Obligation faite à l'agent de joindre la raison de la dépense à sa demande, afin que l'approbation humaine soit informée — pattern transposable à toute autorisation d'action irréversible | AJOUT |
| justificatif de paiement scopé | CONCEPT | définition | Credential remis à l'agent après approbation — carte à usage unique ou Shared Payment Token — borné en montant, devise et marchand, de sorte que la perte maximale d'une transaction est fixée à l'émission | AJOUT |
| limites de dépense sans approbation | CONCEPT | statut | Capacité annoncée par Stripe le 29 avril 2026 mais non livrée : plafonds paramétrables et choix des cas où un agent agit sans revue humaine supplémentaire | AJOUT |
| Dan Hill | PERSONNE | rôle | Product Manager Link Consumer Product chez Stripe, auteur de l'annonce du portefeuille Link pour agents (29 avril 2026) | AJOUT |
| Stripe | ORGANISATION | positionnement | Co-auteur de l'Agentic Commerce Protocol avec OpenAI, et simultanément émetteur (Issuing) et portefeuille (Link) : détient les rails de cartes que les protocoles machine-natifs prétendent remplacer | MISE_A_JOUR |
| Stripe Sessions 2026 | EVENEMENT | rôle | Keynote Stripe où a été posée la thèse des agents comme participants actifs de l'économie d'Internet, dont cette annonce est la déclinaison produit | AJOUT |
| OpenClaw | TECHNOLOGIE | rôle | Agent personnel cité par Stripe comme exemple de bénéficiaire du portefeuille Link pour agents ; mention non commentée dans l'article | AJOUT |
