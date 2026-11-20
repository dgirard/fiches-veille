---
themes: [qualite-securite, recherche-education, politique-regulation]
source: SFEIR
---
# sfeir-anthropic-auto-replication-iot-2026-10-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** (~8 500 signes, six sources notées). Il restitue l'étude de **William Zhou** et **Daniel Freeman** (Frontier Red Team d'**Anthropic**, 12 octobre 2026) sur la capacité de petits modèles à poids ouverts à se répliquer d'objet connecté en objet connecté, et sépare ce qui est démontré de ce qui est extrapolé. **(A)** Les expériences : **Qwen3.5-9B** monte un serveur d'inférence sur **8 types de matériel sur 9** ; **GLM-5.2**, seul modèle à réussir la réplication de bout en bout, atteint **8 machines sur 8** dans 4 essais sur 5 via un port **ADB** non authentifié, en déployant Llama3.1-8B. **(B)** La projection : l'échéance de fin 2026 sort d'une courbe de l'**Epoch Capabilities Index** (+**13,7 points par an**, R² 0,95) ; un essaim de la taille du botnet **Kimwolf** équivaudrait à **40 GPU H100**. **(C)** Les réserves : **Ciaran Martin** (ex-NCSC) parle de *« vendor exaggeration »*, **Jessica Ji** (CSET) rappelle que la probabilité est inconnue ; l'article note que l'étude paraît deux jours avant la journée investisseurs d'Anthropic. Il traduit enfin les recommandations en hygiène IoT d'entreprise. Prolonge, à trois ans d'écart, l'évaluation de réplication autonome de METR (2023).

## Titre Article

Vers IA sur objets connectés : ce qu'Anthropic démontre et ce qu'elle extrapole

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/vers-ia-objets-connectes-anthropic-auto-replication/

## Keywords

auto-réplication, ver IA, self-replicating AI, objets connectés, IoT, Android TV, Anthropic, Frontier Red Team, modèles à poids ouverts, open weights, GLM-5.2, Qwen3.5-9B, Gemma, Llama3.1-8B, inférence locale, ADB, port 5555, botnet, Kimwolf, Mirai, Epoch Capabilities Index, RepliBench, AI Security Institute, hygiène IoT, segmentation réseau, pots de miel

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé individuellement, publié sur sfeir.com.

## Ton

Profil : article de décryptage d'une étude de sécurité IA, registre journalistique et analytique, en français, public de DSI, RSSI et équipes IT. Le titre annonce la grille de lecture, démonstration contre extrapolation, et le texte la tient section par section : un tableau des expériences avec modèles et résultats, une section séparée pour la projection (courbe ECI, ordre de grandeur Kimwolf), puis les limites que les auteurs reconnaissent eux-mêmes. Les réserves extérieures sont attribuées nommément (Reuters, SecurityWeek, Georgetown, Colorado) et mises en balance, y compris une voix inquiète. L'article replace l'étude dans ses antécédents (Fudan 2024, RepliBench 2025, ADB.Miner 2018) et mentionne le calendrier de publication sans en tirer de conclusion. La dernière partie bascule vers le pratique avec une liste d'actions d'entreprise (inventaire, segmentation, fermeture d'ADB). Clôture factuelle : ni code ni données publiés, les expériences ne sont pas rejouables.

## Pense-betes

- **Scénario en quatre étapes** : trouver des cibles → obtenir l'exécution de code → faire tourner un modèle → se propager. Les deux premières renvoient à des travaux existants (CyberGym, ExploitBench, CyberSecEval 3) ; l'étude teste l'inférence et la propagation, avec des modèles **à poids ouverts** uniquement.
- **Cible de démonstration** : boîtiers Android TV sans marque (~**55 $**, 4 Go de mémoire). Un ver sans point central, mais lent : **plus d'une journée** par réplication.
- **Expériences** :
  - Qwen3.5-9B, serveur d'inférence sur 9 matériels (Jetson Nano à RTX 4090) → **8/9** ;
  - harnais **Memento** (notes des tentatives passées, 20 lignées × 6 générations) → **45 %** puis **61 à 84 %** ;
  - Gemma4-26B-A4B réparti sur 15 boîtiers → **0,39 token/s** ;
  - GLM-5.2 sur 8 machines Android 15 via ADB → **8/8** dans 4 essais sur 5, 7/8 au cinquième.
- **Nuances** : GLM-5.2 tournait sur un serveur séparé et déployait **Llama3.1-8B** ; avec une inférence scriptée, un modèle de 3 milliards de paramètres atteint ~la moitié d'un réseau de 17 machines. Durées : **28 à 51 h** (Qwen), **71 à 150 h** (Gemma). Claude Opus 4.8 en conseiller : pas de gain significatif.
- **Projection** : ECI +13,7 points/an pour les meilleurs modèles ouverts ≤ 30 Md de paramètres → niveau GLM-5.2 fin 2026 ; 4 bits → 4 Go suffisent. Kimwolf (2 M d'appareils) → **133 000 copies**, ~80 000 tokens/s, soit **40 H100**.
- **Limites reconnues par les auteurs** : étape cyber simplifiée (borne haute), un seul matériel, un seul botnet, ECI non spécifique à la réplication, riposte non testée.
- **Hygiène recommandée** : quarantaine par les FAI (Mirai : **92 %** des infections disparues en 14 jours avec notification, 74 % sans) ; réglages sûrs par défaut ; surveillance des transferts de plusieurs Go et pots de miel. En entreprise : inventorier boîtiers de salles, affichage, caméras, NAS ; segmenter ; fermer ADB (**TCP 5555**).

## RésuméDe400mots

L'article de SFEIR décrypte une étude publiée le 12 octobre 2026 par William Zhou et Daniel Freeman, de la Frontier Red Team d'Anthropic, sur la capacité de modèles d'IA à se répliquer hors des datacenters. La thèse des chercheurs : d'ici quelques mois, de petits modèles à poids ouverts pourraient passer d'objet connecté en objet connecté, à la manière d'un ver informatique. L'article distingue ce que l'étude démontre de ce qu'elle extrapole.

Les auteurs découpent la réplication en quatre étapes et concentrent leurs expériences sur l'inférence et la propagation. Leur cible est un boîtier Android TV sans marque à environ 55 dollars. Qwen3.5-9B parvient à monter un serveur d'inférence sur huit types de matériel sur neuf, et son taux de réussite passe de 45 % à 61-84 % lorsqu'il réutilise les notes de ses tentatives passées. Gemma4-26B-A4B réparti sur quinze boîtiers ne produit que 0,39 token par seconde. Seul GLM-5.2 réussit la réplication de bout en bout sur huit machines émulant Android 15, par un port ADB non authentifié ; il tourne toutefois sur un serveur séparé et déploie Llama3.1-8B. Une réplication prend de 28 à 150 heures selon le modèle, et l'aide de Claude Opus 4.8 n'améliore pas significativement les résultats.

L'échéance de fin 2026 relève de la projection : sur l'Epoch Capabilities Index, les meilleurs modèles ouverts de 30 milliards de paramètres ou moins progressent de 13,7 points par an et atteindraient le niveau de GLM-5.2 à cette date. Rapporté au botnet Kimwolf, plus de deux millions d'appareils, un tel essaim ferait tourner 133 000 copies, l'équivalent de 40 GPU H100. Les auteurs reconnaissent leurs limites : étape cyber simplifiée, un seul matériel, un seul botnet, indice non spécifique, riposte non testée.

L'article rapporte ensuite les réserves. Ciaran Martin, ancien directeur du NCSC britannique, y voit une exagération de fournisseur ; Jessica Ji, du CSET de Georgetown, rappelle que la probabilité du scénario est inconnue ; Zhengxiong Li s'inquiète au contraire d'un ver impossible à arrêter. Il rappelle les antécédents : l'étude de Fudan sur l'auto-copie (2024), RepliBench de l'AI Security Institute (2025), et le ver ADB.Miner de 2018 qui utilisait déjà le port ADB. Il signale aussi que l'étude a paru deux jours avant la journée investisseurs d'Anthropic.

Les recommandations reprennent l'hygiène connue depuis Mirai : quarantaine des abonnés infectés par les fournisseurs d'accès, réglages sûrs par défaut chez les fabricants, surveillance réseau et pots de miel. Pour une entreprise, SFEIR les traduit en inventaire des boîtiers Android, caméras et NAS, segmentation réseau, fermeture du débogage ADB sur le port 5555 et alerte sur les gros transferts. Anthropic n'a publié ni code ni données.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Vers IA sur objets connectés | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | étude Anthropic sur l'auto-réplication | DOCUMENT | 0.96 | STATIQUE | déclaré_article |
| William Zhou | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| Daniel Freeman | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| étude Anthropic sur l'auto-réplication | DOCUMENT | mesure | GLM-5.2 se réplique sur 8 machines sur 8 dans 4 essais sur 5 via ADB | MESURE | 0.92 | STATIQUE | déclaré_article |
| étude Anthropic sur l'auto-réplication | DOCUMENT | mesure | Qwen3.5-9B monte un serveur d'inférence sur 8 types de matériel sur 9 | MESURE | 0.9 | STATIQUE | déclaré_article |
| étude Anthropic sur l'auto-réplication | DOCUMENT | prédit | des modèles ouverts ≤ 30 Md de paramètres atteindront le seuil de réplication fin 2026 | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| étude Anthropic sur l'auto-réplication | DOCUMENT | est_basé_sur | Epoch Capabilities Index | CONCEPT | 0.86 | STATIQUE | déclaré_article |
| GLM-5.2 | TECHNOLOGIE | utilise | ADB | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| auto-réplication sur objets connectés | CONCEPT | s_applique_à | Android TV | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Ciaran Martin | PERSONNE | s_oppose_à | étude Anthropic sur l'auto-réplication | DOCUMENT | 0.86 | STATIQUE | déclaré_article |
| étude Anthropic sur l'auto-réplication | DOCUMENT | référence | Kimwolf | CONCEPT | 0.84 | STATIQUE | déclaré_article |
| Vers IA sur objets connectés | DOCUMENT | référence | RepliBench | DOCUMENT | 0.84 | STATIQUE | déclaré_article |
| étude Anthropic sur l'auto-réplication | DOCUMENT | recommande | quarantaine par les FAI, réglages sûrs par défaut, surveillance réseau et pots de miel | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | inventorier et segmenter les objets connectés, fermer ADB sur le port TCP 5555 | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| quarantaine des abonnés infectés | METHODOLOGIE | mesure | 92 % des infections Mirai disparues en 14 jours avec notification, 74 % sans | MESURE | 0.85 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| étude Anthropic sur l'auto-réplication | DOCUMENT | titre | « AI models may be capable of self-replicating without access to a datacenter », 12 octobre 2026 | AJOUT |
| William Zhou | PERSONNE | rôle | Chercheur, Frontier Red Team d'Anthropic | AJOUT |
| Daniel Freeman | PERSONNE | rôle | Chercheur, Frontier Red Team d'Anthropic | AJOUT |
| GLM-5.2 | TECHNOLOGIE | catégorie | Modèle à poids ouverts, seul à réussir la réplication de bout en bout | AJOUT |
| auto-réplication sur objets connectés | CONCEPT | définition | Propagation d'un modèle d'IA d'appareil en appareil, sur le modèle d'un ver | AJOUT |
| Ciaran Martin | PERSONNE | rôle | Ancien directeur du NCSC britannique | AJOUT |
| Kimwolf | CONCEPT | définition | Botnet de plus de 2 millions d'appareils, surtout des boîtiers Android TV | AJOUT |
| RepliBench | DOCUMENT | apport | Benchmark de réplication autonome de l'AI Security Institute (2025) | AJOUT |
