# **Architecture de Coexistence Hybride et Stratégies de Double Livraison : Intégration Avancée de Microsoft 365 et Google Workspace**

## **Résumé Exécutif**

L'évolution des infrastructures numériques d'entreprise vers le cloud a traditionnellement imposé un choix binaire : standardiser l'organisation sur l'écosystème Microsoft 365 ou migrer intégralement vers Google Workspace. Cependant, la complexité croissante des environnements de travail modernes, souvent exacerbée par des fusions, des acquisitions ou des exigences spécifiques aux départements (telles que les équipes d'ingénierie préférant les outils Google et les départements financiers exigeant Excel et Outlook), remet en question cette orthodoxie de la plateforme unique. La question posée — savoir si une entreprise peut recevoir des courriels simultanément sur les deux plateformes tout en offrant aux employés la liberté de choisir leur environnement de travail — touche au cœur de l'ingénierie des systèmes collaboratifs hybrides.

La réponse technique est affirmative. Il est tout à fait possible de configurer un domaine d'entreprise unique (par exemple, @entreprise.com) pour qu'il s'étende sur les deux écosystèmes via une architecture de **livraison fractionnée** (Split Delivery). Dans ce modèle, le flux de messagerie entrant est dirigé vers une passerelle principale qui distribue intelligemment les messages vers le système de destination approprié en fonction de l'emplacement de la boîte aux lettres de l'utilisateur.

Néanmoins, permettre le « choix de l'employé » ne se résume pas à une simple configuration de routage SMTP. Pour garantir une expérience utilisateur transparente et éviter la fragmentation organisationnelle, les architectes informatiques doivent déployer une infrastructure complexe de synchronisation d'annuaires (pour assurer la visibilité dans la liste d'adresses globale), d'interopérabilité calendaire (pour les recherches de disponibilité Free/Busy) et de gestion unifiée des identités. Ce rapport examine en profondeur les mécanismes techniques, les protocoles de sécurité, les implications de licence et les stratégies opérationnelles nécessaires pour maintenir cet environnement hybride à haute fidélité.

## ---

**1\. Fondamentaux Architecturaux de la Coexistence de Messagerie**

La mise en œuvre d'un environnement où les employés peuvent choisir leur client de messagerie tout en conservant une identité d'entreprise unifiée nécessite une compréhension approfondie du flux de messagerie SMTP et de la gestion des enregistrements DNS. Contrairement à une configuration standard où les enregistrements MX (Mail Exchange) pointent vers un seul fournisseur qui héberge toutes les boîtes aux lettres, une configuration hybride introduit la notion de système « passerelle » et de système « destination ».

### **1.1 Le Modèle de Livraison Fractionnée (Split Delivery)**

Le concept central qui permet la coexistence est la **livraison fractionnée**. Ce mécanisme permet à deux systèmes de messagerie distincts de partager le même espace de noms de domaine public. L'un des systèmes est désigné comme le point d'entrée principal (via les enregistrements MX publics) et agit comme un routeur intelligent.1

Dans ce scénario, lorsqu'un courriel externe est envoyé à employe@entreprise.com, il arrive d'abord sur le serveur primaire. Ce serveur consulte son annuaire local :

1. **Livraison Locale :** Si l'utilisateur possède une boîte aux lettres sur ce système principal, le message est livré localement.  
2. **Relais vers l'Hôte Intelligent (Smart Host) :** Si l'utilisateur n'est pas trouvé localement (ou s'il est configuré avec une règle de routage spécifique), le serveur ne rejette pas le message. Au lieu de cela, il le relaie via un connecteur SMTP sécurisé vers le système secondaire.3

Cette architecture est invisible pour l'expéditeur externe. Pour lui, le domaine @entreprise.com est une entité monolithique. C'est en interne que la complexité réside, nécessitant une configuration précise pour éviter les boucles de messagerie (où les serveurs se renvoient mutuellement le message jusqu'à expiration) et pour assurer que les mécanismes de sécurité comme SPF et DKIM ne brisent pas l'authentification lors du relais.

### **1.2 Implications du « Choix de l'Employé »**

L'exigence spécifique de laisser le choix à l'employé transforme un défi purement technique en un défi de gestion du cycle de vie des identités. Dans une migration classique, la coexistence est temporaire et les utilisateurs sont déplacés par lots. Ici, la coexistence est un état permanent.5

Cela implique que l'état de chaque utilisateur (hébergé sur Google ou Microsoft) est une variable dynamique.

* **Scénario Google :** Si un employé choisit Google Workspace, sa boîte aux lettres principale réside dans le cloud de Google. Cependant, pour que ses collègues sur Microsoft 365 puissent le contacter, une représentation de son identité (un « Utilisateur de messagerie » ou « Contact ») doit exister dans l'annuaire Azure Active Directory (Microsoft Entra ID), avec une adresse de redirection pointant vers Google.7  
* **Scénario Microsoft :** Inversement, si un employé opte pour Outlook/Exchange, sa boîte aux lettres est dans Exchange Online. Son identité doit néanmoins exister dans l'annuaire Google pour permettre l'authentification aux services partagés (comme Drive ou Teams) et pour que les utilisateurs de Gmail puissent le trouver dans l'annuaire d'entreprise, mais sans licence Gmail active pour éviter le « split-brain » (où deux boîtes aux lettres existent pour le même utilisateur sans synchronisation).2

Cette fluidité exige une gouvernance stricte des identités. L'organisation ne peut pas simplement créer des comptes sur les deux plateformes ; elle doit orchestrer le routage de chaque individu en fonction de son choix, souvent via des attributs spécifiques dans un annuaire maître (comme Active Directory sur site ou un RHIS).

## ---

**2\. Topologies de Routage et Configuration de la Passerelle (Edge)**

Il existe deux topologies principales pour structurer cette coexistence, définies par le système qui reçoit le trafic MX initial. Le choix entre placer Google Workspace ou Microsoft 365 en frontal a des conséquences majeures sur le filtrage du spam, la latence et la gestion des incidents.

### **2.1 Architecture A : Google Workspace comme Passerelle Principale**

Dans cette configuration, les enregistrements MX du domaine public pointent vers les serveurs de Google (aspmx.l.google.com). Google reçoit l'intégralité du trafic entrant, applique ses filtres antispam et antivirus, livre les messages aux utilisateurs Gmail, et transfère les messages destinés aux utilisateurs Outlook vers Microsoft 365\.1

Cette approche est souvent privilégiée pour sa simplicité de mise en œuvre initiale dans le panneau d'administration Google et la robustesse reconnue du filtrage spam de Gmail.

#### **2.1.1 Configuration des Hôtes et du Routage**

Pour mettre en place cette topologie, les administrateurs utilisent les sections **Hôtes** et **Routage** de la console d'administration Google Workspace.

La première étape consiste à définir Microsoft 365 comme une destination valide pour le trafic SMTP. Cela se fait en créant un « Hôte de messagerie ».10

* **Nom de l'hôte :** Microsoft 365 (ou Exchange Online).  
* **Serveur de destination :** L'adresse MX spécifique du tenant Microsoft 365, généralement sous la forme \[domaine\].mail.protection.outlook.com.  
* **Port et Sécurité :** Le port 25 est standard, avec l'obligation d'activer le chiffrement TLS pour sécuriser le transit des données entre les deux clouds.

Une fois l'hôte défini, des règles de routage doivent être appliquées. Google offre une flexibilité significative ici. L'administrateur peut configurer une règle de **livraison fractionnée** qui s'applique à l'ensemble du domaine ou à des unités organisationnelles spécifiques.2

* La méthode la plus courante pour un environnement mixte est d'utiliser le routage basé sur l'appartenance. Si l'utilisateur n'est pas détecté comme ayant une boîte Gmail active, ou si une règle explicite l'indique, le message est transmis à l'hôte Microsoft 365\.  
* Une approche plus granulaire consiste à placer les utilisateurs « Microsoft » dans un groupe Google spécifique. Une règle de routage est alors configurée pour dire : « Pour tous les membres du groupe "Utilisateurs Outlook", modifier la route et envoyer vers l'hôte Microsoft 365 ».1

#### **2.1.2 Gestion des Alias de Routage (Subdomains)**

Pour assurer que le trafic relayé arrive à bon port sans boucler, il est crucial d'utiliser des domaines de routage technique. Lorsqu'un message est transféré de Google vers Microsoft, il ne doit pas être envoyé simplement à @entreprise.com (car l'enregistrement MX renverrait à Google), mais à l'adresse de routage technique du tenant Microsoft, souvent @entreprise.onmicrosoft.com.11

L'administration doit donc s'assurer que chaque utilisateur choisissant Microsoft possède un alias secondaire (proxy address) correspondant à ce domaine technique, et que la règle de routage Google réécrit l'enveloppe du message ou cible ce domaine spécifique.13

### **2.2 Architecture B : Microsoft 365 comme Passerelle Principale**

Dans cette seconde topologie, les enregistrements MX pointent vers Microsoft 365 (entreprise-com.mail.protection.outlook.com). Exchange Online Protection (EOP) agit comme la première ligne de défense. Les messages pour les utilisateurs Outlook sont livrés localement, tandis que ceux pour les utilisateurs Gmail sont relayés vers les serveurs de Google.3

C'est souvent l'architecture préférée des entreprises qui s'appuient sur **Microsoft Defender for Office 365** pour la sécurité avancée, ou qui ont une infrastructure hybride avec Active Directory sur site.

#### **2.2.1 La Configuration « Relais Interne » (Internal Relay)**

Le paramètre critique dans cette architecture est le type de domaine accepté dans Exchange Online. Par défaut, un domaine est configuré comme **Faisant autorité** (Authoritative), ce qui signifie qu'Exchange pense connaître tous les destinataires valides et rejette immédiatement tout message adressé à un utilisateur inconnu via le blocage DBEB (Directory-Based Edge Blocking).7

Pour permettre la coexistence, le domaine doit être basculé en mode **Relais Interne** (Internal Relay).4

* **Impact Technique :** En mode Relais Interne, lorsqu'Exchange reçoit un courriel pour un utilisateur qu'il ne trouve pas dans sa base de données locale (GAL), il ne génère pas d'erreur de non-remise (NDR) immédiate. Au lieu de cela, il consulte ses connecteurs sortants pour voir s'il existe une route pour transmettre ce message ailleurs.  
* **Le Connecteur Sortant :** Un connecteur doit être configuré dans le flux de messagerie Exchange pour diriger le trafic du domaine partagé vers le serveur intelligent (Smart Host) de Google, qui est aspmx.l.google.com.15

#### **2.2.2 Le Défi du Routage des Destinataires Inconnus**

Dans un modèle de « choix de l'employé », la gestion des utilisateurs inexistants devient complexe. Si Microsoft est en mode Relais Interne, il enverra tout message inconnu vers Google. Si Google ne connaît pas non plus l'utilisateur, il rejettera le message. Cependant, si Google est mal configuré (par exemple avec une règle de capture globale qui renvoie vers Microsoft), une **boucle de messagerie** catastrophique peut se former, saturant les serveurs et retardant la livraison des courriels légitimes.17

Pour mitiger ce risque, il est impératif que le système secondaire (Google dans ce cas) soit configuré pour rejeter fermement les destinataires inconnus (Authoritative) ou que la synchronisation des annuaires soit si précise que Microsoft ne relaie que les messages destinés aux utilisateurs valides de Google (identifiés comme « Contacts de messagerie »).19

### **2.3 Tableau Comparatif des Architectures**

| Caractéristique | Architecture A (Google MX) | Architecture B (Microsoft MX) |
| :---- | :---- | :---- |
| **Point d'entrée DNS** | aspmx.l.google.com | domaine.mail.protection.outlook.com |
| **Filtrage Primaire** | Google Spam Filters | Exchange Online Protection (EOP) |
| **Configuration Domaine** | Routage via "Hôtes" et Règles | Domaine en mode "Relais Interne" |
| **Complexité de gestion** | Modérée (Interface unifiée) | Élevée (Gestion des connecteurs et contacts) |
| **Expérience Utilisateur** | Native pour Gmail, relayée pour Outlook | Native pour Outlook, relayée pour Gmail |
| **Risque principal** | Latence de livraison vers Microsoft | Blocage DBEB si mal configuré, boucles |

## ---

**3\. Gestion de l'Identité et Synchronisation des Annuaires (GAL)**

La réussite d'un environnement où les employés choisissent leur outil dépend moins du routage des courriels que de la capacité des utilisateurs à se trouver mutuellement. Dans un environnement unifié, un utilisateur Microsoft s'attend à voir *tous* ses collègues dans le carnet d'adresses global (GAL), y compris ceux sur Google, et inversement. L'absence de synchronisation crée des silos invisibles qui nuisent à la collaboration.

### **3.1 Stratégie de Synchronisation Bidirectionnelle**

Puisqu'il n'existe pas de bouton natif « Synchroniser avec le concurrent » dans les consoles d'administration de Microsoft ou Google, cette synchronisation doit être construite, souvent à l'aide de scripts PowerShell ou d'outils tiers.

#### **3.1.1 Représentation des Utilisateurs Google dans Microsoft 365**

Pour les employés ayant choisi Google Workspace, leur existence dans l'annuaire Microsoft est cruciale mais subtile. Ils ne doivent pas avoir de boîte aux lettres Exchange (ce qui consommerait une licence et créerait un stockage local inutile), mais ils doivent être des objets activés pour la messagerie.8

Il existe deux types d'objets principaux dans Exchange Online pour ces utilisateurs :

1. **Contact de Messagerie (Mail Contact) :** C'est un simple pointeur d'annuaire. Il contient le nom, le prénom et l'adresse e-mail externe. Il est visible dans le GAL mais ne permet pas de se connecter à Microsoft 365\. C'est suffisant si l'employé « Google » n'a besoin d'aucun accès aux services Microsoft.  
2. **Utilisateur de Messagerie (Mail User) :** C'est un objet plus riche. Il possède des identifiants de connexion (User Principal Name \- UPN) dans Azure AD, ce qui permet à l'utilisateur de se connecter à Teams, SharePoint ou Office Web Apps, même si son e-mail est hébergé ailleurs. Pour une entreprise offrant le choix, c'est souvent l'option requise, car l'employé Google aura probablement besoin de collaborer sur des documents Office ou de rejoindre des réunions Teams.21

**Automatisation via PowerShell :** Les administrateurs doivent souvent mettre en place des scripts planifiés (via Azure Automation ou des tâches Windows) qui interrogent l'API Google Directory, récupèrent la liste des utilisateurs, et exécutent les commandes New-MailUser ou Set-MailUser dans Exchange Online. Un point critique est la gestion de l'attribut ExternalEmailAddress (ou TargetAddress). Cet attribut doit pointer vers l'adresse de routage réelle (par exemple user@gws.entreprise.com) pour forcer Exchange à router le courrier hors du tenant.23

#### **3.1.2 Représentation des Utilisateurs Microsoft dans Google Workspace**

Réciproquement, les utilisateurs Microsoft doivent apparaître dans l'annuaire Google pour l'autocomplétion dans Gmail et le partage dans Drive.

* **Google Cloud Directory Sync (GCDS) :** Anciennement GADS, cet outil est la norme pour synchroniser un annuaire LDAP (comme Active Directory sur site) vers Google. Il peut être configuré pour créer des comptes Google pour les utilisateurs Microsoft sans leur attribuer de licence Gmail, agissant ainsi comme des identités de répertoire.25  
* **Contacts Partagés (Domain Shared Contacts) :** Pour les environnements purement cloud (sans AD sur site), l'API « Domain Shared Contacts » permet d'injecter des fiches de contact externes dans l'annuaire global Google. Ces contacts sont visibles par tous mais ne sont pas des comptes Google complets.27

### **3.2 Gestion Unifiée des Identités (SSO)**

Si un employé a le choix de son outil de messagerie, il ne devrait pas avoir à gérer deux mots de passe différents. L'implémentation d'une authentification unique (Single Sign-On \- SSO) est indispensable.

L'architecture recommandée consiste à utiliser **Microsoft Entra ID (Azure AD)** comme fournisseur d'identité central (IdP).

* Google Workspace est configuré comme une « Application d'entreprise » dans Azure AD.  
* Le protocole SAML est utilisé pour l'authentification.  
* Lorsqu'un utilisateur Google tente de se connecter à Gmail, il est redirigé vers la page de connexion Microsoft.  
* Le provisionnement automatique des utilisateurs (SCIM) peut également être configuré depuis Azure AD vers Google, automatisant la création, la mise à jour et la désactivation des comptes Google en fonction des changements dans l'annuaire Microsoft.28

Cette centralisation simplifie considérablement les processus RH : lorsqu'un employé quitte l'entreprise, la désactivation de son compte Azure AD coupe instantanément l'accès aux deux environnements, réduisant les risques de sécurité.

## ---

**4\. Interopérabilité Calendaire et Gestion des Ressources**

Si la messagerie est le système circulatoire de l'entreprise, le calendrier en est le système nerveux. Dans un environnement mixte, la capacité à voir si un collègue est libre ou occupé (Free/Busy) est la fonctionnalité la plus critique après l'envoi de courriels. Sans cela, la planification de réunions devient un cauchemar logistique.

### **4.1 Architecture de Recherche de Disponibilité (Free/Busy)**

L'interopérabilité calendaire permet à un utilisateur Outlook d'ouvrir l'Assistant Planification et de voir les blocs bleus (occupé) d'un utilisateur Google, et vice versa. Cette magie technique repose sur des appels API croisés complexes.

#### **4.1.1 La Transition vers Microsoft Graph API**

Historiquement, Google utilisait l'API Exchange Web Services (EWS) pour interroger Microsoft. Cependant, avec la dépréciation progressive de l'authentification de base et des anciennes API par Microsoft, Google a migré son outil **Calendar Interop** pour utiliser l'API **Microsoft Graph**.30

Cette transition est cruciale pour les nouvelles configurations :

1. **Inscription de l'Application :** L'administrateur doit enregistrer une application dans le portail Azure AD, lui accordant des permissions spécifiques telles que Calendars.ReadBasic.All (pour voir les disponibilités) et Place.Read.All (pour les salles de réunion).  
2. **Comptes de Rôle (Role Accounts) :** L'architecture repose sur des comptes de service.  
   * Un **compte de rôle Exchange** (hébergé sur M365) est utilisé par Google pour effectuer les requêtes vers l'API Graph.  
   * Un **compte de rôle Google** est utilisé par Exchange pour interroger l'API Google Calendar.31  
   * Il est recommandé d'utiliser des comptes dédiés (ex: calendar-interop@entreprise.com) pour éviter que ces fonctions critiques ne soient liées au compte d'un administrateur humain susceptible de partir.33

#### **4.1.2 Configuration Côté Microsoft (Organization Relationships)**

Du côté de Microsoft, la configuration passe souvent par l'établissement d'une **Relation Organisationnelle** (Organization Relationship). Cela définit un niveau de confiance avec le domaine externe (Google). L'administrateur doit configurer l'espace d'adressage de disponibilité (Add-AvailabilityAddressSpace) pour indiquer à Exchange que les requêtes pour le domaine @gws.entreprise.com (ou le domaine principal si split) doivent être dirigées vers une URL spécifique de Google Interop.31

### **4.2 Gestion des Salles et Ressources Partagées**

Dans un modèle de choix, les salles de réunion physiques (Salles de conférence, Projecteurs) sont une ressource unique et indivisible. Elles ne peuvent pas exister en double. Généralement, les ressources sont hébergées sur la plateforme « dominante » ou principale.

Si les salles sont sur Exchange :

* Les utilisateurs Google doivent pouvoir les réserver. Google Calendar Interop permet cela en exposant les ressources Exchange dans l'interface Google.  
* Cependant, des limitations existent. Les fonctionnalités avancées comme l'approbation automatique conditionnelle ou les métadonnées de salle complexes peuvent ne pas traverser l'API parfaitement. Google recommande de créer des comptes de rôle supplémentaires pour l'équilibrage de charge si l'entreprise effectue un grand nombre de requêtes de réservation, afin d'éviter le « throttling » (limitation de débit) de l'API Graph.35

### **4.3 Limitations et Expérience Utilisateur**

Il est important de noter que la fidélité n'est pas absolue.

* **Détails des événements :** Souvent, seul le statut Libre/Occupé est synchronisé. Les titres et détails des réunions peuvent être masqués pour des raisons de confidentialité ou de limitation technique.  
* **Réunions Récurrentes :** C'est un point de friction majeur. La logique de récurrence (RFC 5545\) diffère légèrement entre Google et Microsoft. Modifier une occurrence unique d'une série récurrente dans un système peut parfois entraîner la désynchronisation de la série dans l'autre système.37 Les utilisateurs doivent être formés pour éviter des modifications complexes sur des séries inter-plateformes.

## ---

**5\. Cadre de Sécurité et Conformité des Protocoles de Messagerie**

L'un des risques les plus élevés dans une architecture de messagerie fractionnée est de compromettre involontairement la délivrabilité des courriels. Les protocoles modernes d'authentification de messagerie (SPF, DKIM, DMARC) sont conçus pour empêcher l'usurpation d'identité, mais ils peuvent interpréter le relais légitime entre Google et Microsoft comme une attaque s'ils ne sont pas configurés avec précision.

### **5.1 Sender Policy Framework (SPF) : Le Défi de l'Alignement**

Le protocole SPF utilise un enregistrement DNS TXT pour lister les adresses IP autorisées à envoyer des courriels pour un domaine.

* **Exigence Hybride :** Puisque les courriels peuvent partir à la fois de Google et de Microsoft, l'enregistrement SPF doit inclure les deux : v=spf1 include:spf.protection.outlook.com include:\_spf.google.com \-all.39  
* **La Limite des 10 Lookups :** SPF impose une limite stricte de 10 résolutions DNS. En incluant Google et Microsoft, on consomme déjà une partie significative de ce quota. Si l'entreprise utilise également Salesforce, Mailchimp ou d'autres services tiers, le risque de dépasser cette limite est réel, ce qui invaliderait l'enregistrement SPF. L'utilisation de mécanismes d'aplatissement SPF (SPF Flattening) peut être nécessaire.41

### **5.2 DKIM (DomainKeys Identified Mail) : Signature Cryptographique**

DKIM est plus robuste pour les environnements hybrides car il permet l'utilisation de plusieurs « sélecteurs ».

* L'entreprise doit configurer la signature DKIM sur **les deux** plateformes.  
* Google signera ses sortants avec un sélecteur (ex: google.\_domainkey).  
* Microsoft signera avec un autre (ex: selector1.\_domainkey).  
* Comme les sélecteurs sont uniques, il n'y a pas de conflit. Un serveur de réception validera la signature Google avec la clé publique Google et la signature Microsoft avec la clé Microsoft. C'est un avantage majeur pour maintenir une haute réputation de domaine.42

### **5.3 DMARC et le Problème du Relais Interne (Spoofing Interne)**

C'est ici que la situation se complique. Imaginons qu'un expéditeur externe (client@yahoo.com) envoie un courriel à votre entreprise. Le MX pointe vers Microsoft. Microsoft reçoit le courriel (SPF passe pour Yahoo). Microsoft relaie ensuite le message vers un utilisateur Google.

* Google reçoit le message venant de l'IP de Microsoft.  
* L'adresse de l'expéditeur est toujours yahoo.com.  
* Google vérifie le SPF : « Est-ce que l'IP de Microsoft est autorisée pour Yahoo? » **Non.** Le SPF échoue.  
* Si le message n'est pas signé DKIM par Yahoo, ou si la signature est brisée, le message risque d'atterrir en Spam ou d'être rejeté par la politique DMARC de Yahoo.

**Solutions Techniques :**

1. **ARC (Authenticated Received Chain) :** Ce protocole permet à Microsoft de « signer » le résultat de sa propre vérification d'authentification avant de relayer le message. Google, s'il fait confiance à la chaîne ARC de Microsoft, acceptera le message malgré l'échec SPF.  
2. **Liste Blanche de Passerelle Entrante (Inbound Gateway Whitelist) :** Dans Google Workspace, il est impératif de configurer une « Passerelle de messagerie entrante ». On y liste les plages IP de Microsoft Exchange Online. Cela instruit Google de ne pas effectuer les vérifications SPF sur ces IP, ou de faire confiance au relais. De plus, on peut activer l'option pour que Google tente de détecter l'IP d'origine (X-Forwarded-For) pour ses analyses.44

### **5.4 Sender Rewriting Scheme (SRS) dans Exchange Online**

Pour résoudre le problème des transferts automatiques sortants (par exemple, un utilisateur Microsoft transférant son courrier vers un compte personnel externe), Microsoft utilise le **SRS**.

* Le SRS réécrit l'adresse de l'enveloppe (P1 Mail From) avec un domaine technique appartenant à Microsoft (ex: bounces+SRS...@protection.outlook.com).  
* Ainsi, le serveur de destination voit le message venir de Microsoft et vérifie le SPF de Microsoft, qui réussit.  
* Dans une configuration de relais interne hybride, il faut s'assurer que le SRS est actif et fonctionne correctement sur les connecteurs sortants pour éviter que Google ne rejette les messages relayés.47

## ---

**6\. Expérience Utilisateur et Collaboration Unifiée**

Au-delà de l'infrastructure invisible, le « choix » impacte le quotidien numérique des employés. Les écosystèmes Microsoft et Google ont des philosophies différentes concernant la collaboration, ce qui crée des frictions au niveau applicatif.

### **6.1 Le Dilemme Teams vs Meet**

Dans un monde hybride, la visioconférence est le point de friction numéro un.

* Si un utilisateur Google organise une réunion, il génère par défaut un lien **Google Meet**.  
* Si un utilisateur Outlook organise, il génère un lien **Microsoft Teams**.  
* **L'Intégration Teams pour Google Workspace :** Pour fluidifier cela, Microsoft propose un « Add-on » officiel pour Google Workspace. Une fois déployé par l'administrateur, il ajoute un bouton Teams dans l'interface de création d'événement de Google Calendar. Cela permet à un utilisateur fidèle à Google de créer néanmoins des réunions Teams pour s'aligner sur le standard de l'entreprise si nécessaire.50  
* Inversement, des add-ins pour Outlook permettent d'insérer des liens Meet, bien que l'intégration soit souvent moins profonde.

### **6.2 Partage de Fichiers et Permissions**

L'employé qui choisit Google utilisera **Drive** ; celui qui choisit Microsoft utilisera **OneDrive/SharePoint**.

* Le partage de liens devient complexe. Un lien SharePoint envoyé à un utilisateur Google nécessitera une authentification Microsoft. Grâce au SSO (discuté au chapitre 3), cela est transparent, mais l'utilisateur Google se retrouvera dans l'interface web d'Office pour collaborer.  
* Les permissions « Partager avec toute l'organisation » peuvent se comporter différemment selon que l'annuaire sous-jacent est complet ou non. Il est crucial que tous les utilisateurs soient provisionnés dans les deux annuaires pour que la résolution des noms fonctionne lors du partage de documents.6

### **6.3 Gestion des Licences et Optimisation des Coûts**

Le modèle de choix a un coût financier direct.

* **Double Licence (Approche « Ceinture et Bretelles ») :** La solution la plus simple administrativement est d'attribuer une licence complète Microsoft 365 E3/E5 et une licence Google Workspace Enterprise à tout le monde. Cela garantit que tout fonctionne partout, mais double presque le budget IT.  
* **Licensing Optimisé :** Une approche plus fine consiste à mixer les licences.  
  * *Profil Google :* Licence Google Workspace Standard \+ Licence Microsoft « sans Exchange » (comme **Microsoft 365 Apps for Enterprise** ou une licence F3 pour l'accès web et Teams). L'utilisateur a ses apps Office locales mais son mail sur Gmail.  
  * *Profil Microsoft :* Licence Microsoft 365 E3 \+ Licence **Google Cloud Identity Free** (gratuite). Cette licence gratuite permet à l'utilisateur d'exister dans Google, d'avoir le SSO, mais pas de Gmail ni de Drive payant. C'est souvent suffisant pour qu'il puisse accéder aux documents partagés par ses collègues Google.52

## ---

**7\. Stratégie Opérationnelle et Gouvernance**

Permettre le choix impose une charge opérationnelle continue aux équipes IT. Ce n'est pas un projet « set and forget ».

### **7.1 Support et Formation**

Le Helpdesk doit être formé sur deux piles technologiques complètes.

* Un technicien doit savoir dépanner un problème de synchronisation Outlook *et* un problème d'accès Drive.  
* La documentation interne (Knowledge Base) doit être dupliquée : « Comment réserver une salle (Outlook) » et « Comment réserver une salle (Gmail) ».

### **7.2 Processus d'Arrivée et de Départ (Onboarding/Offboarding)**

Le processus RH doit intégrer la question du choix dès l'embauche.

* **Onboarding :** Le script de création de compte doit prendre un paramètre « Préférence Mail ». Si \= Google, le script PowerShell crée un Mail User dans Exchange et une Mailbox dans Google. Si \= Microsoft, l'inverse.  
* **Offboarding :** La désactivation doit être simultanée. L'utilisation d'un IdP central (Azure AD) est ici un filet de sécurité vital pour s'assurer qu'un ex-employé ne conserve pas d'accès à l'un des deux clouds.55

### **7.3 Risques de Fragmentation des Données**

Le risque stratégique majeur est la création de silos de données. L'eDiscovery (recherche légale) devient complexe : en cas de litige, les équipes juridiques doivent extraire des données de deux clouds différents, avec des formats et des outils de rétention différents. Il est impératif d'harmoniser les politiques de rétention (ex: garder les emails 7 ans) sur les deux plateformes pour assurer la conformité légale.6

## ---

**Conclusion**

À la question « Une entreprise peut-elle recevoir un mail depuis Microsoft 365 et Google Workspace, les employés ayant le choix? », la réponse est un **oui conditionnel**.

Techniquement, les protocoles de **livraison fractionnée**, de **relais interne** et de **synchronisation d'annuaires** sont matures et permettent cette coexistence. Cependant, cette liberté offerte aux employés se paie au prix d'une **complexité architecturale accrue**. L'organisation ne gère plus un système de messagerie, mais trois : le système Microsoft, le système Google, et le système d'interconnexion qui les lie.

Pour les entreprises qui s'engagent dans cette voie, l'architecture recommandée privilégie souvent **Microsoft 365 comme point d'entrée (MX)** pour bénéficier de ses capacités de sécurité avancées (Defender), tout en utilisant le mode **Relais Interne** pour desservir les utilisateurs Google. L'utilisation rigoureuse de **Microsoft Entra ID** comme source unique de vérité pour les identités, couplée à une synchronisation automatisée des listes d'adresses globales, est la clé de voûte qui empêche cet environnement hybride de devenir un chaos ingérable. Ce n'est pas seulement un choix technologique, c'est un engagement opérationnel fort vers une culture d'entreprise flexible.

#### **Works cited**

1. Email routing and delivery options for Google Workspace, accessed January 30, 2026, [https://support.google.com/a/answer/2685650?hl=en](https://support.google.com/a/answer/2685650?hl=en)  
2. Send email to 2 email systems with split delivery \- Google Workspace Admin Help, accessed January 30, 2026, [https://support.google.com/a/answer/12971016?hl=en](https://support.google.com/a/answer/12971016?hl=en)  
3. Google Workspace Split Delivery to Office 365 \[Complete Tutorial\] \- SysTools, accessed January 30, 2026, [https://www.systoolsgroup.com/updates/google-workspace-split-delivery/](https://www.systoolsgroup.com/updates/google-workspace-split-delivery/)  
4. Microsoft 365 Split Delivery \- ImprovMX, accessed January 30, 2026, [https://improvmx.com/guides/microsoft-365-split-delivery](https://improvmx.com/guides/microsoft-365-split-delivery)  
5. {Part 1}Two Part Series on Google Workspace and O365 Mail and Calendar Co-existence, accessed January 30, 2026, [https://medium.com/@mittal.saurabh89/part-1-two-part-series-on-google-workspace-and-o365-mail-and-calendar-co-existence-3f2a89b695c4](https://medium.com/@mittal.saurabh89/part-1-two-part-series-on-google-workspace-and-o365-mail-and-calendar-co-existence-3f2a89b695c4)  
6. Strategies for Separating Google Workspace Accounts \- HiView Solutions, accessed January 30, 2026, [https://hiviewsolutions.com/strategies-for-separating-google-workspace-accounts/](https://hiviewsolutions.com/strategies-for-separating-google-workspace-accounts/)  
7. Manage accepted domains in Exchange Online \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/manage-accepted-domains/manage-accepted-domains](https://learn.microsoft.com/en-us/exchange/mail-flow-best-practices/manage-accepted-domains/manage-accepted-domains)  
8. O365Synchronizer \- PowerShell module to synchronize contacts to user mailboxes and between O365 tenants : r/Office365 \- Reddit, accessed January 30, 2026, [https://www.reddit.com/r/Office365/comments/189wc2h/o365synchronizer\_powershell\_module\_to\_synchronize/](https://www.reddit.com/r/Office365/comments/189wc2h/o365synchronizer_powershell_module_to_synchronize/)  
9. Deliver email to multiple inboxes with dual delivery \- Google Workspace Admin Help, accessed January 30, 2026, [https://support.google.com/a/answer/9228551?hl=en](https://support.google.com/a/answer/9228551?hl=en)  
10. Google to Microsoft 365 (O365) Staged Migration with Dual Delivery and Coexistence during Migration \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/answers/questions/5159286/google-to-microsoft-365-(o365)-staged-migration-wi](https://learn.microsoft.com/en-us/answers/questions/5159286/google-to-microsoft-365-\(o365\)-staged-migration-wi)  
11. How to set up Email Split Delivery from O365 to Gmail \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/answers/questions/5267795/how-to-set-up-email-split-delivery-from-o365-to-gm](https://learn.microsoft.com/en-us/answers/questions/5267795/how-to-set-up-email-split-delivery-from-o365-to-gm)  
12. Google Workspace migration prerequisites in Exchange Online \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/exchange/mailbox-migration/google-workspace-migration-prerequisites](https://learn.microsoft.com/en-us/exchange/mailbox-migration/google-workspace-migration-prerequisites)  
13. Email Split Delivery to GSuite : r/Office365 \- Reddit, accessed January 30, 2026, [https://www.reddit.com/r/Office365/comments/y4qric/email\_split\_delivery\_to\_gsuite/](https://www.reddit.com/r/Office365/comments/y4qric/email_split_delivery_to_gsuite/)  
14. Accepted domains in Exchange Server \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/exchange/mail-flow/accepted-domains/accepted-domains](https://learn.microsoft.com/en-us/exchange/mail-flow/accepted-domains/accepted-domains)  
15. Setting up “Connector Based” Delivery of Emails from Microsoft 365 Using MX Records, accessed January 30, 2026, [https://www.infiflex.com/setting-up-connector-based-delivery-of-emails-from-microsoft-365-using-mx-records](https://www.infiflex.com/setting-up-connector-based-delivery-of-emails-from-microsoft-365-using-mx-records)  
16. Create a Send connector to route outbound mail through a smart host \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/outbound-smart-host-routing](https://learn.microsoft.com/en-us/exchange/mail-flow/connectors/outbound-smart-host-routing)  
17. Exchange Hybrid Environment \- Internal Relay vs Authoritative? : r/exchangeserver \- Reddit, accessed January 30, 2026, [https://www.reddit.com/r/exchangeserver/comments/x45ppr/exchange\_hybrid\_environment\_internal\_relay\_vs/](https://www.reddit.com/r/exchangeserver/comments/x45ppr/exchange_hybrid_environment_internal_relay_vs/)  
18. Change Accepted Domain from Internal Relay to Authoritative \- Microsoft Q\&A, accessed January 30, 2026, [https://learn.microsoft.com/en-au/answers/questions/1166659/change-accepted-domain-from-internal-relay-to-auth](https://learn.microsoft.com/en-au/answers/questions/1166659/change-accepted-domain-from-internal-relay-to-auth)  
19. Get the real meaning of a catch all mailbox and how to set it up \- CodeTwo, accessed January 30, 2026, [https://www.codetwo.com/admins-blog/catch-all-email-in-microsoft-exchange/](https://www.codetwo.com/admins-blog/catch-all-email-in-microsoft-exchange/)  
20. InternalRelay vs Authoritative \- Microsoft Q\&A, accessed January 30, 2026, [https://learn.microsoft.com/en-us/answers/questions/5126375/internalrelay-vs-authoritative](https://learn.microsoft.com/en-us/answers/questions/5126375/internalrelay-vs-authoritative)  
21. Switching from Internal Relay to Authoritative With Sub-Domains \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/answers/questions/1509438/switching-from-internal-relay-to-authoritative-wit](https://learn.microsoft.com/en-us/answers/questions/1509438/switching-from-internal-relay-to-authoritative-wit)  
22. How to disable "internal" tenant to tenant email routing and make Office 365 adhere to the MX record only‎? : r/Office365 \- Reddit, accessed January 30, 2026, [https://www.reddit.com/r/Office365/comments/1iuscgy/how\_to\_disable\_internal\_tenant\_to\_tenant\_email/](https://www.reddit.com/r/Office365/comments/1iuscgy/how_to_disable_internal_tenant_to_tenant_email/)  
23. Perform Google Workspace migration to Microsoft 365 or Office 365 using Exchange Online PowerShell, accessed January 30, 2026, [https://learn.microsoft.com/en-us/exchange/mailbox-migration/perform-gspace-migration-powershell](https://learn.microsoft.com/en-us/exchange/mailbox-migration/perform-gspace-migration-powershell)  
24. Solved: Office 365 \- mass edit all users contact information \- Experts Exchange, accessed January 30, 2026, [https://www.experts-exchange.com/questions/28960495/Office-365-mass-edit-all-users-contact-information.html](https://www.experts-exchange.com/questions/28960495/Office-365-mass-edit-all-users-contact-information.html)  
25. About Google Cloud Directory Sync \- Google Workspace Admin Help, accessed January 30, 2026, [https://support.google.com/a/answer/106368?hl=en](https://support.google.com/a/answer/106368?hl=en)  
26. Get started with Directory Sync | Google Workspace for Business Continuity, accessed January 30, 2026, [https://knowledge.workspace.google.com/business-continuity/directory-sync/get-started-with-directory-sync](https://knowledge.workspace.google.com/business-continuity/directory-sync/get-started-with-directory-sync)  
27. Manage your Global Address List \- Google Workspace Admin Help, accessed January 30, 2026, [https://support.google.com/a/answer/166870?hl=en](https://support.google.com/a/answer/166870?hl=en)  
28. Configure Federation Between Google Workspace And Microsoft Entra Id \- Windows Education, accessed January 30, 2026, [https://learn.microsoft.com/en-us/education/windows/configure-aad-google-trust](https://learn.microsoft.com/en-us/education/windows/configure-aad-google-trust)  
29. Federate Google Cloud with Microsoft Entra ID (formerly Azure AD), accessed January 30, 2026, [https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory](https://docs.cloud.google.com/architecture/identity/federating-gcp-with-azure-active-directory)  
30. Configure Calendar interoperability with Microsoft Office 365 using the Microsoft Graph API, accessed January 30, 2026, [https://workspaceupdates.googleblog.com/2025/05/calendar-interoperability-microsoft-office-365-with-microsoft-graph-api.html](https://workspaceupdates.googleblog.com/2025/05/calendar-interoperability-microsoft-office-365-with-microsoft-graph-api.html)  
31. Setup Free/busy Calendar Co-existence between Google Workspace and O365 | Medium, accessed January 30, 2026, [https://medium.com/@mittal.saurabh89/part-2-two-part-series-on-google-workspace-and-o365-mail-and-calendar-co-existence-c28742faaea5](https://medium.com/@mittal.saurabh89/part-2-two-part-series-on-google-workspace-and-o365-mail-and-calendar-co-existence-c28742faaea5)  
32. 3\. Allow Exchange users to see Calendar availability data \- Google Workspace Admin Help, accessed January 30, 2026, [https://support.google.com/a/answer/7438496?hl=en](https://support.google.com/a/answer/7438496?hl=en)  
33. An introduction to Google Calendar Interop | by SADA, An Insight Company, accessed January 30, 2026, [https://engineering.sada.com/an-introduction-to-google-calendar-interop-a46d14eaa7b4](https://engineering.sada.com/an-introduction-to-google-calendar-interop-a46d14eaa7b4)  
34. Create an organization relationship in Exchange Online \- Microsoft Learn, accessed January 30, 2026, [https://learn.microsoft.com/en-us/exchange/sharing/organization-relationships/create-an-organization-relationship](https://learn.microsoft.com/en-us/exchange/sharing/organization-relationships/create-an-organization-relationship)  
35. 5\. Allow Calendar users to book Exchange resources (Optional) \- Google Help, accessed January 30, 2026, [https://support.google.com/a/answer/9193836?hl=en](https://support.google.com/a/answer/9193836?hl=en)  
36. Scaling our Calendar Interop offering \- Google Workspace Updates, accessed January 30, 2026, [https://workspaceupdates.googleblog.com/2022/09/scaling-our-calendar-interop-offering.html](https://workspaceupdates.googleblog.com/2022/09/scaling-our-calendar-interop-offering.html)  
37. Recurring events | Google Calendar \- Google for Developers, accessed January 30, 2026, [https://developers.google.com/workspace/calendar/api/guides/recurringevents](https://developers.google.com/workspace/calendar/api/guides/recurringevents)  
38. Google Calendar gets improved interoperability with Outlook : r/gsuite \- Reddit, accessed January 30, 2026, [https://www.reddit.com/r/gsuite/comments/13j5u3d/google\_calendar\_gets\_improved\_interoperability/](https://www.reddit.com/r/gsuite/comments/13j5u3d/google_calendar_gets_improved_interoperability/)  
39. SPF, DKIM & DMARC: Essential Email Protocols Explained \- Red Sift, accessed January 30, 2026, [https://redsift.com/guides/email-protocol-configuration-guide/all-you-need-to-know-about-spf-dkim-and-dmarc](https://redsift.com/guides/email-protocol-configuration-guide/all-you-need-to-know-about-spf-dkim-and-dmarc)  
40. Set up SPF \- Google Workspace Admin Help, accessed January 30, 2026, [https://support.google.com/a/answer/33786?hl=en](https://support.google.com/a/answer/33786?hl=en)  
41. Step-By-Step Guide To Configuring Google Apps SPF Records \- DMARC Report, accessed January 30, 2026, [https://dmarcreport.com/blog/step-by-step-guide-to-configuring-google-apps-spf-records/](https://dmarcreport.com/blog/step-by-step-guide-to-configuring-google-apps-spf-records/)  
42. Do we care about SPF alignment? | Word to the Wise, accessed January 30, 2026, [https://www.wordtothewise.com/2024/11/do-we-care-about-spf-alignment/](https://www.wordtothewise.com/2024/11/do-we-care-about-spf-alignment/)  
43. SPF, DKIM, and DMARC: Best Practices for Microsoft 365 and Google Workspace Email Security \- Performance Connectivity, Inc., accessed January 30, 2026, [https://performanceconnectivity.com/spf-dkim-and-dmarc-best-practices-microsoft-365-google-workspace/](https://performanceconnectivity.com/spf-dkim-and-dmarc-best-practices-microsoft-365-google-workspace/)  
44. Set up an inbound mail gateway \- Google Workspace Admin Help, accessed January 30, 2026, [https://support.google.com/a/answer/60730?hl=en](https://support.google.com/a/answer/60730?hl=en)  
45. Allow Listing by IP Address in Google Workspace \- Hive Systems, accessed January 30, 2026, [https://www.hivesystems.com/ephishiency-knowledgebase/g-suite-ip-address](https://www.hivesystems.com/ephishiency-knowledgebase/g-suite-ip-address)  
46. Allowlisting with an Inbound Gateway in GSuite/Google Apps \- Knowledge Base, accessed January 30, 2026, [https://help.caniphish.com/hc/en-us/articles/5181889848591-Allowlisting-with-an-Inbound-Gateway-in-GSuite-Google-Apps](https://help.caniphish.com/hc/en-us/articles/5181889848591-Allowlisting-with-an-Inbound-Gateway-in-GSuite-Google-Apps)  
47. Sender Rewriting Scheme (SRS) in Microsoft 365, accessed January 30, 2026, [https://learn.microsoft.com/en-us/exchange/reference/sender-rewriting-scheme](https://learn.microsoft.com/en-us/exchange/reference/sender-rewriting-scheme)  
48. Sender Rewriting Scheme Upcoming Changes \- Microsoft Community Hub, accessed January 30, 2026, [https://techcommunity.microsoft.com/blog/exchange/sender-rewriting-scheme-upcoming-changes/2632829](https://techcommunity.microsoft.com/blog/exchange/sender-rewriting-scheme-upcoming-changes/2632829)  
49. M365 Changelog: (Updated) Sender Rewriting Scheme (SRS) Expanding to SMTP/Mailbox Forwarding \- Petri IT Knowledgebase, accessed January 30, 2026, [https://petri.com/microsoft-changelog/m365-changelog-sender-rewriting-scheme-srs-expanding-to-smtp-mailbox-forwarding/](https://petri.com/microsoft-changelog/m365-changelog-sender-rewriting-scheme-srs-expanding-to-smtp-mailbox-forwarding/)  
50. Schedule a Microsoft Teams meeting from Google calendar, accessed January 30, 2026, [https://support.microsoft.com/en-us/office/schedule-a-microsoft-teams-meeting-from-google-calendar-0b032e58-bb54-491a-9f10-5e5353521bc2](https://support.microsoft.com/en-us/office/schedule-a-microsoft-teams-meeting-from-google-calendar-0b032e58-bb54-491a-9f10-5e5353521bc2)  
51. Join from Google \- Microsoft Support, accessed January 30, 2026, [https://support.microsoft.com/en-us/office/join-from-google-bba2dfbe-0b2b-4ee7-be10-261ad80ddb60](https://support.microsoft.com/en-us/office/join-from-google-bba2dfbe-0b2b-4ee7-be10-261ad80ddb60)  
52. Compare Microsoft 365 Plans & Pricing (Formerly Office 365\) \- Microsoft Store, accessed January 30, 2026, [https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products](https://www.microsoft.com/en-us/microsoft-365/buy/compare-all-microsoft-365-products)  
53. Compare Exchange Online plans \- Microsoft 365, accessed January 30, 2026, [https://www.microsoft.com/en-us/microsoft-365/exchange/compare-microsoft-exchange-online-plans](https://www.microsoft.com/en-us/microsoft-365/exchange/compare-microsoft-exchange-online-plans)  
54. Microsoft 365 Business Plans and Pricing, accessed January 30, 2026, [https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-plans-and-pricing](https://www.microsoft.com/en-us/microsoft-365/business/microsoft-365-plans-and-pricing)  
55. How to Align Google Workspace and Microsoft 365 Policies Across a Hybrid Organization, accessed January 30, 2026, [https://advisorymsp.com/resources/how-to-align-google-workspace-and-microsoft-365-policies-across-a-hybrid-organization/](https://advisorymsp.com/resources/how-to-align-google-workspace-and-microsoft-365-policies-across-a-hybrid-organization/)