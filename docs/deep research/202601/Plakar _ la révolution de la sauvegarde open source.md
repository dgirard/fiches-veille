# **Plakar : la révolution française de la sauvegarde open source**

**Plakar redéfinit la protection des données avec une architecture de stockage immuable, un chiffrement de bout en bout audité par des experts, et des performances jusqu'à 60 fois supérieures aux solutions existantes.** Fondée à Paris en septembre 2024 par Julien Mangeard (ex-CTO de Veepee) et Gilles Chehade (créateur d'OpenSMTPD, contributeur OpenBSD), cette startup française a levé **3 millions de dollars** en mai 2025 auprès d'investisseurs prestigieux dont Olivier Pomel (Datadog) et Solomon Hykes (Docker). En janvier 2026, Plakar a rejoint la **Linux Foundation et le CNCF**, marquant une étape décisive vers l'établissement d'un standard open source pour la résilience des données.

---

## **Une architecture en trois couches conçue pour l'ère cloud**

L'architecture de Plakar repose sur trois couches distinctes qui assurent modularité, sécurité et performances. La **couche de stockage** (Storage Layer) écrit et récupère des flux d'octets bruts et opaques vers des emplacements de stockage variés. Les données arrivant à cette couche sont déjà compressées et chiffrées, organisées de manière cohérente et strictement **immuables** : une fois stockées, elles ne sont jamais modifiées. Cette couche est entièrement parallélisée et sensible à la contre-pression, s'adaptant dynamiquement aux vitesses de stockage disponibles.

La **couche repository** agit comme proxy local d'encodage/décodage. Lors d'une sauvegarde, elle compresse puis chiffre les données localement avant de les transmettre à la couche de stockage. Lors d'une restauration, elle déchiffre et décompresse les données avant de les exposer aux couches supérieures. Cette couche maintient un **index local du contenu** permettant des vérifications d'existence rapides et une déduplication efficace.

La **couche snapshot** organise les chunks de données bruts en groupes de sauvegarde cohérents, capturant le type de snapshot (système de fichiers, base de données, application), la hiérarchie arborescente, les métadonnées POSIX, les hashs de contenu pour la déduplication et l'indexation pour les recherches rapides. Elle s'appuie sur un **système de fichiers virtuel (VFS) personnalisé** implémentant l'interface standard `fs.FS` de Go, soutenu par un **arbre B+ personnalisé** pour des recherches ordonnées efficaces.

---

## **Kloset : le moteur de stockage immuable qui change la donne**

**Kloset constitue le cœur technologique de Plakar** — décrit comme une bibliothèque API de stockage gérant toutes les opérations de stockage et de récupération de données. Ce moteur repose sur cinq principes de conception fondamentaux qui le distinguent des solutions traditionnelles.

Le **stockage immuable** divise les données en chunks dédupliqués, compressés et chiffrés, stockés par hash de contenu et jamais modifiés après écriture. Les **snapshots auto-descriptifs** incluent toutes les métadonnées nécessaires à la compréhension de leur structure et contexte, les rendant portables et navigables sans dépendances externes. Les **connecteurs modulaires** permettent des sources et cibles interchangeables — Kloset est agnostique quant aux sources de données.

L'**accès granulaire et sans état** permet d'inspecter ou de restaurer des fichiers spécifiques sans charger l'ensemble des données en mémoire. L'**auditabilité cryptographique** garantit que chaque snapshot porte un arbre de digests pour les données et métadonnées, le rendant vérifiable indépendamment et résistant à la falsification.

### **Processus de sauvegarde Kloset**

Le processus de sauvegarde se déroule en cinq étapes séquentielles. Le **chunking** divise le contenu en morceaux plus petits via le Content-Defined Chunking (CDC). La **déduplication** élimine les chunks déjà existants — si un chunk existe déjà, il n'est pas stocké à nouveau. La **compression** applique LZ4 aux chunks avant le chiffrement. Le **chiffrement** transforme les chunks en "blobs" envoyés au backend de stockage. Enfin, les blobs sont regroupés en **packfiles** plus volumineux pour un stockage efficace.

### **FastCDC : l'algorithme de chunking optimisé**

Plakar utilise **FastCDC** comme algorithme de chunking par défaut, implémenté dans leur bibliothèque open source go-cdc-chunkers. Cet algorithme emploie un hash roulant basé sur Gear avec une table de 256 entiers 64 bits aléatoires, une optimisation de saut de points de découpe, et un chunking normalisé pour une meilleure distribution des tailles de chunks.

Une innovation majeure est le **mode FastCDC clé** qui utilise une clé cryptographique pour randomiser la table Gear, empêchant les attaquants de prédire les limites des chunks sans pénalité de performance. Les benchmarks internes montrent des performances de **8 149 MB/s** pour FastCDC et **13 740 MB/s** pour l'algorithme JC, contre seulement **614 MB/s** pour le Rabin de Restic.

---

## **Un système cryptographique audité et approuvé par les experts**

### **L'audit de Jean-Philippe Aumasson**

La cryptographie de Plakar a été auditée par **Jean-Philippe Aumasson**, cryptographe reconnu internationalement, créateur d'algorithmes utilisés dans Plakar et auteur de plusieurs ouvrages de référence en cryptographie. L'audit, publié le 28 février 2025, a conclu :

« Notre évaluation générale est que la conception actuelle est cryptographiquement saine en termes de choix de composants et de paramètres. Nos observations n'incluent aucun problème de sécurité majeur, mais plutôt des recommandations en termes de robustesse et de performance. »

### **Algorithmes cryptographiques (post-audit)**

| Composant | Algorithme | Notes |
| ----- | ----- | ----- |
| **Dérivation de mot de passe** | Argon2id (RFC 9106\) | Paramètres : t=4, m=256 Mo. Remplace scrypt |
| **Chiffrement des chunks** | AES-256-GCM-SIV (RFC 8452\) | Résistant aux erreurs de nonce |
| **Chiffrement des sous-clés** | AES-KW (RFC 3394\) | Key wrapping sécurisé |
| **Hachage/MAC** | BLAKE3 clé | Remplace HMAC-SHA256 |

Le passage d'**AES-GCM** à **AES-GCM-SIV** élimine les risques liés à la qualité du hasard : ce mode produit un ciphertext déterministe pour un plaintext identique, ce qui n'est pas problématique puisque chaque sous-clé ne chiffre qu'un seul chunk. L'adoption d'**AES-KW** pour le key wrapping élimine les risques de collision de nonce à grande échelle. L'utilisation de **BLAKE3 clé natif** plutôt que HMAC-BLAKE3 simplifie l'implémentation tout en maintenant la sécurité.

### **Vulnérabilités corrigées**

L'audit a identifié et permis de corriger plusieurs points :

* Migration de scrypt vers Argon2id (256 Mo de mémoire, 4 itérations) pour une meilleure résistance aux attaques par force brute  
* Suppression complète des digests au profit des MACs uniquement, éliminant une fuite potentielle d'information via les checksums SHA-256  
* Correction d'un risque théorique de collision de nonce à \~8 pétaoctets de clés 32 octets

---

## **De tar (1979) à .ptar : 46 ans d'évolution des formats d'archive**

### **Les limitations fondamentales de tar**

Le format **tar** (Tape ARchive) a été introduit sous Unix en **janvier 1979**, conçu pour les lecteurs de bandes magnétiques — des périphériques séquentiels sans système de fichiers. Cette conception pose des problèmes fondamentaux dans l'ère moderne :

L'**accès séquentiel** impose de lire l'archive entière pour lister ou extraire des fichiers, causant des pénalités de performance sévères sur les grandes archives. Les **limites de taille** (8 Go originalement) et de **longueur de chemin** (100 caractères) ont nécessité des extensions complexes. L'absence de **déduplication native** signifie qu'archiver deux fois les mêmes fichiers double l'espace utilisé. L'absence de **chiffrement natif** force l'utilisation de GPG comme étape séparée.

Un test illustratif : archiver `~/Downloads` (8,8 Go) deux fois avec tar.gz produit **18 Go**. La même opération avec .ptar produit **8,2 Go** — identique à une seule archive, grâce à la déduplication.

### **Le format .ptar : l'archive moderne**

Annoncé le **27 juin 2025**, **.ptar** (prononcé "p-tar") est un format d'archive immuable qui encapsule les données dans un conteneur unique, autonome et adressé par contenu. Sa structure comprend :

* **Section de configuration** : version et paramètres pour la déduplication, compression et chiffrement  
* **Section de données** : blobs stockant structure, métadonnées et données de l'archive  
* **Section d'index** : tables de recherche pour une inspection rapide  
* **Footer** : offsets vers les sections pertinentes pour un accès immédiat  
* **MAC** : code d'authentification pour la vérification d'intégrité globale

### **Capacités clés de .ptar**

Le format supporte l'**accès aléatoire** permettant de parcourir le contenu sans extraction, y compris via HTTP avec des requêtes range pour un accès partiel distant. Le **support S3 natif** permet d'archiver directement des buckets S3 sans cycle téléchargement-tar-upload. La **restauration partielle** extrait des fichiers individuels. La **synchronisation** permet d'intégrer les archives .ptar dans des repositories Kloset standard.

**Kapsul**, publié le 7 juillet 2025 sous licence ISC, est un outil autonome pour créer et gérer des archives .ptar sans installation complète de Plakar.

---

## **Linux Foundation et CNCF : une gouvernance open source renforcée**

### **L'annonce du 7 janvier 2026**

Plakar a rejoint la **Linux Foundation** et le **Cloud Native Computing Foundation** comme organisation membre, décrivant cette étape comme « un pas pivot dans l'établissement d'un Standard Ouvert pour la Résilience ». Cette adhésion apporte :

* **Cadre de gouvernance neutre** : accès à l'écosystème vendor-neutral de la Linux Foundation  
* **Protection contre les brevets** : dissuasion renforcée contre les NPE via le partenariat Unified Patents  
* **Accès communautaire** : connexion aux 1 300+ entreprises membres et 275 000+ contributeurs de l'écosystème CNCF  
* **Crédibilité industrielle** : validation par l'organisme de gouvernance cloud-native de référence

### **Engagement open source**

Plakar utilise la **licence ISC** (style OpenBSD), une licence permissive approuvée par l'OSI. L'engagement clé : les composants principaux (Ptar, agent Plakar, Kloset) **resteront sous licence ISC de façon permanente**. Le repository GitHub compte **1 400+ étoiles**, 52 forks, 20 contributeurs et 5 967 commits, avec des fichiers CODE\_OF\_CONDUCT.md, CONTRIBUTING.md et SECURITY.md établis.

### **Projets comparables dans l'écosystème CNCF**

| Projet | Statut | Focus |
| ----- | ----- | ----- |
| **Velero** | Graduated | Backup et migration de clusters Kubernetes |
| **Rook** | Graduated | Orchestration de stockage cloud-native |
| **OpenEBS** | CNCF Project | Container Attached Storage |
| **Kanister** | Sandbox | Gestion de données au niveau applicatif |

Plakar se différencie en ciblant la protection des données au niveau applicatif (au-delà du seul Kubernetes), avec chiffrement zero-knowledge et portabilité inter-environnements.

---

## **Plakar face à la concurrence : analyse comparative approfondie**

### **Plakar vs Restic**

**Restic**, avec ses 27 000+ étoiles GitHub, représente la référence des sauvegardes modernes. Les premières versions de Plakar étaient \~25x plus lentes sur les sauvegardes subséquentes, mais l'adoption de l'architecture packfile de Restic a comblé cet écart. Sur **S3**, Plakar revendique une amélioration de **60x** (14 minutes → 13 secondes) grâce aux uploads parallélisés.

Plakar offre une **interface web intégrée** (Restic est CLI uniquement), un **garbage collection non-bloquant** (maintenance sans interrompre les sauvegardes/restaurations), et utilise des algorithmes de chunking plus rapides (FastCDC vs Rabin). Restic bénéficie d'une **communauté plus large** et d'une documentation plus mature.

### **Plakar vs BorgBackup**

Borg utilise **Buzhash** pour le chunking contre FastCDC pour Plakar, avec des ratios de déduplication comparables (70-85% pour Borg vs 91,4% revendiqués pour Plakar). Borg est plus **efficace en bande passante** (\~15% d'économie) mais plus lent sur les systèmes distants limités en CPU. Borg **nécessite SSH** pour les sauvegardes distantes sans support S3 natif, nécessitant rclone.

La courbe d'apprentissage de Plakar est **plus simple** selon les retours communautaires. L'architecture B+tree de Plakar avec caching de nœuds offre des accélérations de **6-10x** sur les grands corpus.

### **Plakar vs Duplicity, Duplicacy et Kopia**

**Duplicity** utilise un modèle full+incrémental nécessitant des sauvegardes complètes périodiques, causant des pics de stockage. Son chiffrement GPG est robuste mais externe. **Duplicacy** excelle en **déduplication globale** sans verrou pour les flottes de serveurs similaires, mais sa licence est commerciale pour usage professionnel.

**Kopia** offre une interface graphique de bureau et web comparable à Plakar, avec une communauté plus active actuellement. Cependant, des utilisateurs rapportent des problèmes de **corruption de repository** que Plakar évite grâce à son stockage tamper-evident avec vérification cryptographique.

### **Matrice comparative**

| Fonctionnalité | Plakar | Restic | Borg | Duplicity | Kopia |
| ----- | ----- | ----- | ----- | ----- | ----- |
| Déduplication | ✅ FastCDC | ✅ Rabin | ✅ Buzhash | ⚠️ Limité | ✅ |
| Compression par défaut | ✅ LZ4 | ⚠️ Optionnel | ✅ lz4 | ✅ | ✅ |
| Chiffrement | ✅ AES-256-GCM-SIV | ✅ AES-256 | ✅ AES-256 | ✅ GPG | ✅ AES-256 |
| S3 natif | ✅ | ✅ | ❌ | ✅ | ✅ |
| Interface web | ✅ Intégrée | ❌ | ❌ | ❌ | ✅ |
| Audit sécurité | ✅ 2025 | ⚠️ Informel | ❌ | ❌ | ❌ |
| Support Windows | ✅ | ✅ | ⚠️ WSL | ⚠️ WSL | ✅ |

---

## **Adoption en entreprise et cas d'usage**

### **État actuel du déploiement**

Plakar Enterprise est en **beta fermée** sur AWS Marketplace depuis décembre 2025\. L'équipe compte 8 ingénieurs avec « un siècle d'expérience open source combinée ». Les fonctionnalités Enterprise incluent l'orchestration multi-store, l'application de politiques, l'intégration avec les gestionnaires de secrets (KMS), une couche proxy zero-knowledge et un tableau de bord unifié de posture de sauvegarde.

### **Benchmarks de performance**

Les benchmarks officiels (à vérifier indépendamment) revendiquent :

* **Amélioration S3 de 60x** : sauvegardes passant de \~14 minutes à \~13 secondes  
* **Gains de x2 à x10** selon les workloads  
* **Réduction de 91,4%** de l'espace de stockage : 327 Go → 28 Go pour 10 sauvegardes de mêmes données  
* Capacité de gérer **des millions de fichiers** avec une empreinte mémoire minimale

### **Intégrations cloud**

Le support S3 est le plus mature, fonctionnant avec AWS S3, MinIO, Ceph, Wasabi, Scaleway, Backblaze, OVH, Infomaniak, Clever Cloud et Exoscale SOS. Le support GCP est disponible via plugin. Le support Azure est limité aux endpoints compatibles S3.

### **Cas d'usage cibles**

* **IA/ML** : sauvegarde et versioning de grands datasets et pipelines  
* **Services financiers** : sauvegardes sécurisées, conformes et traçables  
* **Santé** : backups conformes HIPAA des données patients  
* **Cybersécurité** : infrastructure de sauvegarde zero-knowledge, zero-trust  
* **Résilience-as-a-Service** : les MSP gèrent la rétention/réplication sans accéder aux données clients

---

## **Couverture médiatique multilingue**

### **Sources françaises**

La couverture francophone est **positive à très positive**, avec un accent sur l'origine française du projet. **Korben.info** titre « La solution de backup open source française qui décoiffe » et affirme que « Plakar atomise Restic et Borg ». **Le Monde Informatique** détaille l'offre Enterprise et cite Julien Mangeard : « Personne n'a réussi à créer un standard open source dans cette industrie. Nous construisons ce standard. »

**LinuxFr.org** accueille des discussions techniques sur ptar avec participation active de Gilles Chehade. **Le Comptoir Open Source** conclut que Plakar est une « alternative plus puissante que Borg ou duplicity, sans les complexités ». La communauté suggère une certification ANSSI via financement participatif.

### **Couverture internationale limitée**

Les recherches en **allemand et néerlandais** n'ont identifié **aucune couverture** de Plakar malgré des recherches sur Heise, Golem, Pro-Linux, ubuntuusers.de et Tweakers.net. Les **sources espagnoles, italiennes et portugaises** sont quasi inexistantes, à l'exception d'un article sur vInfrastructure.it. Les **sources japonaises** ne contiennent **aucune mention** de Plakar sur Qiita, Zenn ou les communautés BSD japonaises.

Cette absence reflète le caractère récent du projet (stable depuis mai 2025 seulement) et sa concentration initiale sur les marchés anglophone et francophone.

---

## **Conclusion : un challenger prometteur avec un potentiel de disruption**

Plakar représente une **innovation architecturale significative** dans le domaine de la sauvegarde, résolvant le compromis historique entre déduplication et chiffrement grâce à son approche « dédupliquer puis chiffrer ». L'audit cryptographique par Jean-Philippe Aumasson, l'adhésion à la Linux Foundation et au CNCF, et le financement par des investisseurs de premier plan confèrent une crédibilité technique et institutionnelle rare pour un projet si jeune.

Les **performances S3** (60x d'amélioration revendiquée), l'**interface web intégrée**, le **format .ptar** portable et le **garbage collection non-bloquant** constituent des avantages différenciants face à Restic et Borg. Cependant, la **communauté plus restreinte**, l'**absence de déploiements enterprise vérifiés à grande échelle** et la **documentation moins extensive** que les alternatives établies appellent à la prudence.

Pour les organisations à forte orientation S3/AWS, les équipes DevOps capables de gérer le niveau de maturité actuel, et les early adopters recherchant une solution française souveraine, Plakar mérite une évaluation sérieuse. Pour les environnements de production critiques, une période de test sur des workloads non-critiques reste recommandée en attendant que l'écosystème mature davantage.

