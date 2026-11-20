---
themes: [qualite-securite, outils-plateformes, politique-regulation]
source: SFEIR
---
# girard-aikido-altar-securite-air-gap-2026-10-01

## Veille

Article de **Didier Girard** publié sur sfeir.com le **1er octobre 2026** (~2 300 mots, neuf sources). Il restitue l'annonce, le **21 septembre 2026**, d'**Altar** (Altar-1), premier modèle de sécurité open-weight d'**Aikido Security** (Gand), dérivé de **GLM-5.3** de **Z.ai**. Trois apports. **(A)** La méthode : quantification **AWQ** (experts routés en 4 bits, format W4A16) puis élagage d'experts **REAP** de Cerebras, calibré sur les traces du harnais de pentest d'Aikido, sans réentraînement ; le modèle passe de **1,51 To** à **328 Go** (168 experts gardés sur 256 par couche) et tourne sur **quatre H200**. **(B)** Les chiffres de l'éditeur : sur un benchmark interne de **32 CVE**, Altar retrouve **23 des 25** failles du modèle d'origine, pour **78,2 %** de stockage en moins et **5,2 points** de recall perdus. **(C)** Les limites que l'article énumère : benchmark étroit, licence héritée (MIT + revue de sécurité au-delà de **10 Md$** de CA), provenance chinoise des poids, coût du nœud, double usage. *« Chaque gigaoctet retiré du modèle revient aux agents »* résume l'argument mémoire. Prolonge les mesures de capacités cyber de GLM-5.3 de [[fasano-fleischer-anthropic-glm-5-3-advanced-cyber-capabilities-2026-09-29]].

## Titre Article

Aikido Altar : un modèle de sécurité open-weight taillé pour l'air gap

## Date

2026-10-01

## URL

https://www.sfeir.com/articles/aikido-altar-modele-securite-open-weight-air-gap/

## Keywords

Aikido Altar, Altar-1, Aikido Security, Aikido Machine, GLM-5.3, Z.ai, open-weight, air gap, pentest IA, sécurité, mixture-of-experts, élagage d'experts, REAP, Cerebras, quantification AWQ, W4A16, H200, vLLM, cache KV, recall, couverture, benchmark CVE, licence MIT, Entity List, souveraineté d'exécution, provenance des poids, double usage

## Authors

Didier Girard, SFEIR — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : article d'analyse technique publié sur le site d'un cabinet de conseil, à destination des DSI et RSSI de secteurs régulés (banque, santé, industrie OT). Français soigné, vocabulaire technique glosé à la première occurrence (quantification, mixture-of-experts, élagage).

**Style** : progression didactique — le besoin (deux impasses pour les secteurs régulés), la méthode (quantifier puis élaguer), les chiffres (tableau à trois versions), les limites, puis quatre recommandations transposables. Phrases courtes, chiffres précis et rapportés à leur source, distinction explicite entre **recall moyen** et **couverture**.

**Position épistémique** : les chiffres sont présentés comme **mesurés par l'éditeur** dans son propre harnais, et la section « Ce que les chiffres ne disent pas » en tire les conséquences : benchmark de redécouverte de CVE connues, seule preuve de terrain annoncée par Aikido, écart relevé par RuntimeWire entre le slogan *« frontier-grade defensive AI »* et les données. Le texte corrige aussi une lecture de la licence faite par une partie de la couverture tierce, en citant le texte de Z.ai. La note de sources (neuf entrées, dont la fiche Hugging Face et la licence) précise pour chacune ce qu'elle établit.

## Pense-betes

- **Le besoin.** Les modèles frontier fermés tournent chez l'éditeur : les utiliser fait sortir du réseau code source, documentation d'architecture et failles non corrigées. Les open-weight lèvent l'obstacle juridique mais en posent un matériel : GLM-5.3 pèse **1,51 To** en BF16 (753 Md de paramètres, MoE à 256 experts par couche, 8 actifs par token, ~40 Md actifs).
- **L'argument mémoire.** Un pentest agentique garde l'historique de ses étapes en mémoire GPU ; plusieurs investigations en parallèle se disputent la mémoire avec les poids. Sur quatre H200, les 328 Go d'Altar laissent la place au cache KV de plusieurs agents.
- **Étape 1 — quantification AWQ** (checkpoint de cyankiwi) : experts routés de 16 à 4 bits ; attention, expert partagé, couches denses et tête de sortie restent en BF16 → **488 Go**.
- **Étape 2 — élagage REAP** (Cerebras) : contribution d'un expert = poids du routeur × amplitude de sa sortie, pas la fréquence de sélection. Calibration sur les traces du harnais (code lu, appels d'outils, réponses), plus du raisonnement et des articles Wikipédia multilingues pour préserver le français et le néerlandais. Aucune donnée client. **88 experts retirés (34,4 %)**, 8 toujours activés par token.
- **Pas de bloc « cyber » isolable** : cybersécurité, code et langue se répartissent sur de nombreux experts ; à nombre d'experts égal, le résultat dépend de ceux qu'on garde (étude de fidélité de 0xSero).
- **Tableau** (32 CVE, 30 dépôts, 3 runs) : BF16 1 506,7 Go / 65,6 % / 25 ; AWQ INT4 488,2 Go / 61,5 % / 23 ; Altar 328,0 Go / 60,4 % / 23. L'élagage seul retire 160 Go pour ~1 point de recall.
- **Recall vs couverture** : le recall dit si le modèle trouve la faille régulièrement, la couverture s'il l'a trouvée au moins une fois sur trois essais.
- **Licence** : déclarée « other » sur Hugging Face, héritée de GLM-5.3 ; le texte de Z.ai reprend la MIT et n'ajoute qu'une revue de sécurité pour les exploitants « Model as a Service » au-delà de 10 Md$ de CA annuel. Non approuvée OSI.
- **Souveraineté d'exécution** : Aikido est belge, Z.ai figure sur l'Entity List américaine depuis janvier 2025 ; la souveraineté porte sur le lieu d'exécution, la provenance des poids reste une question d'homologation.
- **Quatre leçons pour un DSI/RSSI** : conserver (et nettoyer) les traces d'agents comme jeu de calibration ; dimensionner la mémoire GPU avec le contexte ; mesurer recall et couverture séparément ; inscrire modèle parent, laboratoire, licence et transformations dans le dossier d'achat.
- **Feuille de route Aikido Labs** : formats sous 4 bits (EXL3), optimisation de service sur H200, fine-tuning sur ses workflows — étape où, selon l'article, le risque de double usage change de nature.

## RésuméDe400mots

Le 21 septembre 2026, Aikido Security, société de Gand, a publié Altar, son premier modèle de sécurité open-weight. Didier Girard en détaille la méthode, les chiffres et les limites. Aikido a pris GLM-5.3 de Z.ai (753 milliards de paramètres, 1,51 To en pleine précision), l'a quantifié puis élagué jusqu'à 328 Go et environ 504 milliards de paramètres, et le sert sur un nœud de quatre GPU H200 avec vLLM, pour un contexte allant jusqu'à 128 000 tokens. Le modèle alimente Aikido Machine, appliance de pentest autonome installée dans le datacenter du client et capable de fonctionner sans connexion internet.

Le besoin vient des secteurs régulés : banques, hôpitaux, industriels dont le réseau OT n'a pas de route vers internet ne peuvent pas envoyer leur code et leurs failles à un modèle fermé hébergé par son éditeur. Les modèles ouverts règlent la question juridique mais posent un problème de mémoire, aggravé par les agents : leur historique d'investigation occupe la mémoire GPU, et chaque gigaoctet retiré du modèle leur revient.

La compression se fait en deux temps, sans réentraînement. La quantification AWQ fait passer les experts routés en 4 bits et ramène le modèle à 488 Go. L'élagage REAP, méthode de Cerebras, retire ensuite 88 des 256 experts de chaque couche, choisis selon leur contribution réelle mesurée sur les traces du harnais de pentest d'Aikido et sur des textes multilingues. Huit experts restent activés par token, soit environ 40 milliards de paramètres actifs.

Sur un benchmark interne de 32 CVE réparties dans 30 dépôts, avec trois runs par cas, Altar retrouve 23 des 25 vulnérabilités trouvées par le modèle d'origine, avec 78,2 % de stockage en moins et 5,2 points de recall moyen perdus. L'élagage seul ne fait perdre aucune des 23 failles couvertes par la version quantifiée.

L'article liste ensuite ce que ces chiffres ne disent pas. Le benchmark mesure la redécouverte de failles connues, pas la découverte à l'aveugle ni l'exploitation. La licence, héritée de GLM-5.3, reprend en réalité la licence MIT avec une seule condition visant les très grands opérateurs. Les poids descendent d'un laboratoire chinois inscrit sur l'Entity List américaine. Le nœud de quatre H200 reste un investissement de grand compte. Enfin, publier un modèle orienté pentest pose la question du double usage, qui deviendra plus aiguë avec le fine-tuning annoncé.

Le texte conclut par quatre pratiques transposables : garder les traces des agents, dimensionner la mémoire avec le contexte, mesurer recall et couverture séparément, documenter la provenance du modèle dans tout achat.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Didier Girard | PERSONNE | travaille_chez | SFEIR | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Aikido Security | ORGANISATION | publie | Altar | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Altar | TECHNOLOGIE | est_variante_de | GLM-5.3 | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Z.ai | ORGANISATION | a_créé | GLM-5.3 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Altar | TECHNOLOGIE | utilise | AWQ | METHODOLOGIE | 0.94 | STATIQUE | déclaré_article |
| Altar | TECHNOLOGIE | utilise | REAP | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Cerebras | ORGANISATION | a_créé | REAP | METHODOLOGIE | 0.93 | STATIQUE | déclaré_article |
| REAP | METHODOLOGIE | réduit | 88 experts retirés sur 256 par couche (34,4 %) | MESURE | 0.92 | STATIQUE | déclaré_article |
| Altar | TECHNOLOGIE | réduit | 1,51 To → 328 Go (−78,2 % de stockage) | MESURE | 0.93 | STATIQUE | déclaré_article |
| Aikido Security | ORGANISATION | mesure | 23 des 25 CVE du modèle d'origine retrouvées sur un benchmark de 32 CVE | MESURE | 0.9 | STATIQUE | déclaré_article |
| Aikido Machine | TECHNOLOGIE | utilise | Altar | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Altar | TECHNOLOGIE | permet | pentest IA en air gap | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Altar | TECHNOLOGIE | utilise | NVIDIA H200 | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| RuntimeWire | ORGANISATION | s_oppose_à | « frontier-grade defensive AI » n'est pas établi par les données d'Aikido | AFFIRMATION | 0.82 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | la licence GLM-5.3 reprend la MIT avec une seule condition au-delà de 10 Md$ de CA | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | la souveraineté d'Altar porte sur le lieu d'exécution, pas sur la provenance des poids | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | conserver et nettoyer les traces d'agents comme jeu de calibration | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | dimensionner la mémoire GPU en comptant le contexte des agents | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | mesurer séparément recall moyen et couverture | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Didier Girard | PERSONNE | rôle | Auteur, SFEIR | AJOUT |
| Aikido Security | ORGANISATION | secteur | Sécurité applicative, Gand (Belgique) | AJOUT |
| Altar | TECHNOLOGIE | définition | Modèle de sécurité open-weight (Altar-1), GLM-5.3 quantifié et élagué, 328 Go, ~504 Md de paramètres | AJOUT |
| Aikido Machine | TECHNOLOGIE | catégorie | Appliance de pentest autonome, serveur 4U installé chez le client, fonctionne en air gap | AJOUT |
| GLM-5.3 | TECHNOLOGIE | catégorie | Modèle MoE open-weight de Z.ai, 753 Md de paramètres, 256 experts par couche | AJOUT |
| Z.ai | ORGANISATION | statut | Laboratoire chinois inscrit sur l'Entity List américaine depuis janvier 2025 | AJOUT |
| REAP | METHODOLOGIE | définition | Router-weighted Expert Activation Pruning : élagage d'experts pondéré par le routeur et l'amplitude de sortie | AJOUT |
| AWQ | METHODOLOGIE | définition | Activation-aware Weight Quantization, quantification guidée par les activations | AJOUT |
| RuntimeWire | ORGANISATION | rôle | Média ayant commenté l'écart entre slogan et données | AJOUT |
