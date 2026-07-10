---
themes: [outils-plateformes, produits-services, politique-regulation]
source: SFEIR
---
# sfeir-zml-llmd-docker-llm-inference-souveraine-2026-07-09

## Veille

Décryptage SFEIR (voix cabinet) du lancement, le 8 juillet 2026, de **LLMD** par la startup parisienne **ZML** (fondée par **Steeve Morin**, ex-VP Engineering de Zenly) : un serveur d'inférence qui fait tourner les LLM sur **cinq familles de puces** (NVIDIA CUDA, AMD ROCm, Google TPU, Intel oneAPI, Apple Metal) **depuis une seule base de code**. Thèse structurante : l'entraînement cède la vedette à l'**inférence**, où se jouent désormais le coût par token, la latence et surtout la **dépendance au silicium**. Le pari de ZML — résumé par la devise *model to metal* — est de **découpler le modèle du matériel** via un compilateur en **Zig + MLIR** produisant un binaire natif hermétique, sans Python dans le chemin d'exécution, exposé par une **API compatible OpenAI**. Deux briques, deux licences : **ZML** (framework, Apache-2.0, >90 % Zig) est open source ; **LLMD** (serveur) ne l'est pas, gratuit au lancement. L'article lit l'objet sous trois angles cabinet — **FinOps du token**, **liberté d'architecture** (Design to Exit), **souveraineté** (puces européennes émergentes, intégration dans le processeur VSORA Jotunn8) — puis livre un verdict sans complaisance : c'est une **alpha**, à mettre « sous surveillance active », pas à basculer aujourd'hui.

## Titre Article

ZML/LLMD : et si le « Docker des LLM » était français ?

## Date

2026-07-09

## URL

https://www.sfeir.com/articles/zml-llmd-docker-llms-inference-souveraine/

## Keywords

Inférence LLM, serving, ZML, LLMD, Steeve Morin, model to metal, Docker des LLM, découplage modèle-matériel, portable pas nivelé, Zig, MLIR, compilation AOT, binaire natif hermétique, API compatible OpenAI, continuous batching, paged attention, prefix caching, tool calling, DFlash, décodage spéculatif, zero-copy, Hugging Face, NVIDIA CUDA, AMD ROCm, Google TPU, Intel oneAPI, Apple Metal, cold start, FinOps IA, coût par token, coût par résultat, liberté d'architecture, Design to Exit, réversibilité, lock-in, souveraineté, puces européennes, Axelera, Kalray, SiPearl, VSORA, Jotunn8, Scaleway, Région Île-de-France, VivaTech 2026, Yann LeCun, Solomon Hykes, Clément Delangue, Julien Chaumond, Xavier Niel, vLLM, llama.cpp, technical preview, DGX Spark, Ryzen AI Max+ 395, Apple Silicon, souveraineté matérielle

## Authors

SFEIR (voix éditoriale du cabinet)

## Ton

**Profil** : décryptage technologique de cabinet (thought leadership SFEIR), adressé aux DSI, architectes et décideurs infra. Registre pédagogique et structuré (« En bref », étages de la pile, « Points clés »), technicité élevée mais vulgarisée, longueur moyenne (~1800 mots). Position clairement située : le cabinet parle à ses clients et relie l'objet à son offre (FinOps du token, multi-cloud/multi-hardware, Design to Exit).

**Style** : file la **métaphore Docker** (« le *docker run* de l'inférence : un modèle, une commande, n'importe quelle puce ») sans en être dupe — l'anecdote Solomon Hykes au capital sert la figure. Équilibre revendiqué entre enthousiasme et prudence : chaque promesse éditeur est **assortie de sa réserve** (« ces chiffres restent des annonces éditeur, en attendant des mesures indépendantes » ; le gain DFlash annoncé « jusqu'à 10× » est recadré au « ~6,17× » de la recherche sous-jacente). Section « Le verdict, sans complaisance » assume une posture d'analyste : distingue *technical preview* et production, nomme ce qui n'est **ni nommé ni benchmarké** par l'éditeur (DGX Spark, Ryzen AI Max+). Ancrage maison systématique : renvoie aux articles SFEIR sur l'architecture multi-LLM souveraine et le choix multi-cloud vs souverain, et au cas client France Télévisions (plateforme ALIX). Sourçage explicite et numéroté (zml.ai, TechCrunch, X, arXiv, GlobeNewswire).

## Pense-betes

- **Idée-force : l'inférence est le nouveau goulot d'étranglement.** Après deux ans focalisés sur la taille des modèles et le coût d'entraînement, la mise en production déplace le curseur : ce qui pèse au quotidien, c'est le **coût par token servi**, la latence perçue, et la **dépendance à un unique fournisseur de silicium**. Le serving devient « à la fois la facture cloud et la marge de manœuvre stratégique ».
- **Le pari ZML : *model to metal*, découpler le modèle du matériel.** Pas un énième modèle, mais une couche d'abstraction. La pile a **quatre étages** : (1) modèles (Qwen, Gemma, Mistral, LLaMa) chargés **zero-copy** via FS virtuel depuis HF/S3/GCS, sans téléchargement local ; (2) **LLMD**, serveur exposant une **API compatible OpenAI** (drop-in) avec continuous batching, paged attention, prefix caching, tool calling, métriques Prometheus ; (3) **ZML**, compilateur **AOT** (Zig + MLIR) vers un **binaire natif hermétique**, sans Python dans le chemin d'exécution ; (4) exécution sur **5 backends** : NVIDIA CUDA, AMD ROCm, Google TPU, Intel oneAPI, Apple Metal.
- **Choix de design décisif : « portable, pas nivelé ».** Plutôt que de réduire tous les accélérateurs à un plus petit dénominateur commun, ZML **préserve les chemins spécifiques par puce** (FlashAttention sur NVIDIA, noyaux AITER sur AMD). C'est ce qui distingue une abstraction utile d'un plancher de performance.
- **Chiffres annoncés (à vérifier, éditeur).** Images conteneur très compactes : ~**1,7 Go** (CUDA), **280 Mo** (TPU), **~140 Mo** (build Apple). **Cold start** de l'ordre de **1 à 2 s** sur un modèle 8B. Le cabinet insiste : « en attendant des mesures indépendantes ».
- **DFlash — le décodage spéculatif embarqué.** ZML met en avant « jusqu'à **10×** » ; la recherche sous-jacente (arXiv:2602.06036, *block diffusion for flash speculative decoding*) rapporte plutôt **~6,17×** sur Qwen3-8B. Nuance à conserver face à un public technique.
- **La démo en deux commandes (Mac Apple Silicon).** `brew install zml/zml/llmd` puis `llmd --model=hf://Qwen/Qwen3.6-27B` → serveur local en API OpenAI, interrogeable via `curl localhost:8000/v1/chat/completions`. Toute la valeur de la compat OpenAI : scripts/librairies se rebranchent **sans réécriture**. Deux réserves : 1re requête plus lente (compilation du graphe) ; un **27B en BF16** réclame **≥ 64 Go de mémoire unifiée**.
- **Deux briques, deux licences (à avoir en tête avant de bâtir dessus).** **ZML** = framework open source (Apache-2.0, Zig). **LLMD** = serveur **non open source**, gratuit au lancement le temps de **collecter les usages** avant une future monétisation.
- **Trois enjeux cabinet.** (1) **Économique / FinOps** : découpler le workload du silicium = droit de choisir la puce la moins chère ou la plus disponible → agir sur le coût du token (logique « coût par résultat »). (2) **Liberté d'architecture** : sortir du « un code par cible matérielle » réduit dette technique et coût de migration, préserve le **pouvoir de négociation** — c'est le **Design to Exit** (payer d'avance la couche qui rend le fournisseur remplaçable), prolongé jusqu'au niveau de la puce ; parallèle avec le cas **France Télévisions / plateforme ALIX**. (3) **Souveraineté** : ZML se pose en facilitateur des **puces européennes émergentes** (Axelera, Kalray, SiPearl, VSORA).
- **Ancrage souveraineté concret : VivaTech 2026.** Partenariat **ZML × Scaleway × VSORA × Région Île-de-France** autour d'une chaîne de valeur souveraine de l'inférence (du silicium à l'exploitation), avec intégration de la couche ZML dans le processeur **VSORA Jotunn8**.
- **Crédibilité par le capital.** Fondée à Paris en 2023, ~20 personnes, ~**20 M$** levés (20VC, Kima Ventures/Xavier Niel, Kindred Capital, LocalGlobe, Puzzle Ventures). Business angels signifiants : **Solomon Hykes** (créateur de Docker — clin d'œil à la métaphore), **Clément Delangue** & **Julien Chaumond** (Hugging Face), et **Yann LeCun** (Turing) qui soutient publiquement.
- **Verdict sans complaisance.** LLMD est une **technical preview** : pas pour la production, catalogue de modèles en expansion. Surtout, le support des machines locales que tout le monde a en tête (**DGX Spark** ARM64+Blackwell, **Ryzen AI Max+ 395**, Mac récents) **se déduit** des backends mais n'est **ni nommé ni benchmarké** — « à vérifier par vous-même ». Positionnement concurrentiel : **vLLM** reste la référence débit sur GPU serveur (mais Apple Silicon communautaire/expérimental) ; **llama.cpp** reste roi du local mono-utilisateur ; LLMD vise l'entre-deux — « un vLLM qui s'installe sur un Mac ». Recommandation : **ne pas basculer, mettre sous surveillance active.**
- **À relier** : famille « souveraineté / multi-cloud vs souverain » et « architecture multi-LLM souveraine » (articles SFEIR) ; FinOps de l'IA générative et coût par résultat (fiche AI4IT vs AI4Business de Didier Girard) ; Steeve Morin déjà présent dans le corpus (hôte du podcast « À la French »).

## RésuméDe400mots

Le 8 juillet 2026, la startup parisienne **ZML** publie **LLMD**, un serveur d'inférence qui fait tourner les grands modèles de langage sur **cinq familles de puces** (NVIDIA, AMD, Google, Intel, Apple) depuis **une seule base de code**. SFEIR y voit un signal : à mesure que l'entraînement cède la vedette à l'**inférence**, le vrai champ de bataille — et de coût — se déplace vers le **serving**, où se jouent le coût par token, la latence et la dépendance au silicium.

Le pari de ZML tient en trois mots, *model to metal* : ne pas proposer un énième modèle, mais une couche qui **découple le modèle du matériel**. La pile a quatre étages. En haut, les modèles (Qwen, Gemma, Mistral, LLaMa) chargés **zero-copy** via un système de fichiers virtuel depuis Hugging Face, S3 ou GCS. Puis **LLMD**, serveur exposant une **API compatible OpenAI** (drop-in) avec continuous batching, paged attention, prefix caching, tool calling et métriques Prometheus. En dessous, **ZML** compile le graphe **en amont, une fois pour toutes**, vers un **binaire natif hermétique** en **Zig + MLIR**, sans Python dans le chemin d'exécution. Ce binaire s'exécute sur cinq backends : CUDA, ROCm, TPU, oneAPI, Metal. L'élégance : « portable, pas nivelé » — les chemins spécifiques par puce (FlashAttention, AITER) sont préservés. Chiffres annoncés (éditeur) : images de 1,7 Go (CUDA) à ~140 Mo (Apple), cold start de 1-2 s sur un 8B, et l'accélérateur **DFlash** (« jusqu'à 10× » revendiqué, ~6,17× dans la recherche).

Deux briques, deux licences : **ZML** (framework) est open source (Apache-2.0, >90 % Zig) ; **LLMD** (serveur) ne l'est pas, gratuit au lancement le temps de collecter les usages. La démo tient en deux commandes sur Mac Apple Silicon ; un 27B en BF16 réclame ≥ 64 Go de mémoire unifiée.

SFEIR lit l'objet sous trois angles clients : **FinOps** (choisir la puce la moins chère → agir sur le coût du token), **liberté d'architecture** (**Design to Exit**, réversibilité construite, cf. France Télévisions/ALIX) et **souveraineté** (puces européennes Axelera, Kalray, SiPearl, VSORA ; partenariat VivaTech 2026 avec Scaleway, VSORA et la Région Île-de-France, intégration dans le processeur Jotunn8).

Verdict sans complaisance : c'est une **alpha**, pas pour la production ; le support des machines locales précises (DGX Spark, Ryzen AI Max+) n'est ni nommé ni benchmarké. Face à vLLM (débit GPU serveur) et llama.cpp (local mono-utilisateur), LLMD vise l'entre-deux. Ne pas basculer aujourd'hui, mais mettre « sous surveillance active » : un candidat sérieux, *made in France*, pour devenir le « *docker run* de l'inférence ».

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| ZML | ORGANISATION | publie | LLMD | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Steeve Morin | PERSONNE | dirige | ZML | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| LLMD | TECHNOLOGIE | permet | inférence LLM sur cinq familles de puces depuis une seule base de code | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| LLMD | TECHNOLOGIE | utilise | ZML | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| ZML | TECHNOLOGIE | utilise | Zig | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| ZML | TECHNOLOGIE | utilise | MLIR | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| LLMD | TECHNOLOGIE | utilise | API compatible OpenAI | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| LLMD | TECHNOLOGIE | utilise | DFlash | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| DFlash | TECHNOLOGIE | améliore | vitesse de décodage jusqu'à ~6,17× sur Qwen3-8B | MESURE | 0.8 | STATIQUE | déclaré_article |
| model to metal | CONCEPT | réduit | dépendance à un unique fournisseur de silicium | CONCEPT | 0.9 | ATEMPOREL | inféré |
| LLMD | TECHNOLOGIE | s_applique_à | FinOps de l'IA générative | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| LLMD | TECHNOLOGIE | s_applique_à | Design to Exit | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| ZML | ORGANISATION | collabore_avec | Scaleway | ORGANISATION | 0.9 | STATIQUE | déclaré_article |
| ZML | ORGANISATION | collabore_avec | VSORA | ORGANISATION | 0.9 | STATIQUE | déclaré_article |
| ZML | TECHNOLOGIE | fait_partie_de | processeur VSORA Jotunn8 | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Yann LeCun | PERSONNE | soutient | ZML | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| Solomon Hykes | PERSONNE | a_créé | Docker | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| LLMD | TECHNOLOGIE | concurrence | vLLM | TECHNOLOGIE | 0.85 | DYNAMIQUE | inféré |
| LLMD | TECHNOLOGIE | concurrence | llama.cpp | TECHNOLOGIE | 0.85 | DYNAMIQUE | inféré |
| ZML | TECHNOLOGIE | est_variante_de | Apache-2.0 (open source) | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | mettre LLMD sous surveillance active plutôt que basculer en production aujourd'hui | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| ZML | ORGANISATION | profil | Startup parisienne (fondée 2023), ~20 pers., ~20 M$ levés ; framework d'inférence homonyme (Apache-2.0, >90 % Zig) | AJOUT |
| LLMD | TECHNOLOGIE | catégorie | Serveur d'inférence LLM multi-backend ; API compatible OpenAI ; non open source, gratuit au lancement (alpha) | AJOUT |
| Steeve Morin | PERSONNE | rôle | Fondateur/CEO de ZML, ex-VP Engineering de Zenly (rachetée par Snap) | AJOUT |
| model to metal | CONCEPT | définition | Découpler le modèle du matériel : compilation AOT vers un binaire natif hermétique exécutable sur cinq familles de puces | AJOUT |
| Zig | TECHNOLOGIE | rôle | Langage bas niveau dans lequel ZML est écrit (>90 %) ; pas de Python dans le chemin d'exécution | AJOUT |
| MLIR | TECHNOLOGIE | rôle | Infrastructure de compilation utilisée par ZML pour produire le binaire natif | AJOUT |
| DFlash | TECHNOLOGIE | perf | Décodage spéculatif (block diffusion) ; ~6,17× sur Qwen3-8B (recherche), « jusqu'à 10× » annoncé (arXiv:2602.06036) | AJOUT |
| vLLM | TECHNOLOGIE | positionnement | Référence de débit sur GPU serveur ; support Apple Silicon communautaire/expérimental | AJOUT |
| llama.cpp | TECHNOLOGIE | positionnement | Roi de l'inférence locale mono-utilisateur | AJOUT |
| VSORA | ORGANISATION | rôle | Concepteur de puces (processeur Jotunn8) ; puce européenne émergente intégrant la couche ZML | AJOUT |
| Scaleway | ORGANISATION | rôle | Partenaire cloud de la chaîne de valeur souveraine de l'inférence (VivaTech 2026) | AJOUT |
| Jotunn8 | TECHNOLOGIE | catégorie | Processeur IA de VSORA intégrant la couche ZML | AJOUT |
| Design to Exit | METHODOLOGIE | principe | Payer d'avance la couche d'abstraction qui rend le fournisseur remplaçable, plutôt qu'espérer une réversibilité non construite | AJOUT |
| FinOps de l'IA générative | METHODOLOGIE | principe | Payer la charge au bon prix sur le bon matériel ; logique « coût par résultat / coût du token servi » | AJOUT |
| Yann LeCun | PERSONNE | rôle | Lauréat du prix Turing ; soutient publiquement ZML | AJOUT |
| Solomon Hykes | PERSONNE | rôle | Créateur de Docker ; business angel au capital de ZML | AJOUT |
