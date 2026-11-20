---
themes: [politique-regulation, produits-services, economie-marche]
source: SFEIR
---
# sfeir-mistral-large-4-licence-auto-hebergement-2026-11-02

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **2 novembre 2026** (~25 000 signes, neuf sections, 11 sources, trois tableaux). Il fait suite à la publication par **Mistral AI**, le **29 octobre 2026**, des poids de **Mistral Large 4** (« Le Chonk ») : MoE de **1,05 billion** de paramètres, **49 Md** actifs par token, sous une licence maison, la **Mistral Ecosystem Open-Weight License**. Trois apports. **(A)** Une lecture de la licence : base MIT, mais l'article 2 impose une licence commerciale à toute activité de *Model as a Service*, **sans seuil de revenu** et filiales comprises ; l'article 3 exempte l'usage interne et les produits de Mistral. Comparée à GLM-5.3 (seuil de **10 Md$** de chiffre d'affaires) et Kimi K3 (**20 M$** de revenu), c'est la plus fermée des trois pour les hébergeurs. Conséquence pour la réversibilité : l'auto-hébergement reste entier, le changement de fournisseur géré dépend de Mistral. **(B)** Le coût matériel : checkpoint FP8 d'environ **1 060 Go** sur un nœud de 8 GPU, NVFP4 d'environ **610 Go** sur Blackwell, 2 bits sur Mac à 512 Go à titre d'essai. **(C)** Une relecture des scores : **41,4 %** sur Terminal-Bench 4.0 dans l'agent Mistral Vibe contre **26,26 %** chez Vals AI à harnais constant, sans progrès par rapport à la préversion ; l'économie de tokens est jugée l'argument le plus robuste. *« Un hébergeur, même européen, ne peut pas le servir à ses clients sans accord avec Mistral. »* Fait suite à [[mistral-large-4-le-chonk-2026-10-06]].

## Titre Article

Mistral Large 4 en poids ouverts : ce que la licence permet, ce que l'auto-hébergement coûte

## Date

2026-11-02

## URL

https://www.sfeir.com/articles/mistral-large-4-poids-ouverts-licence-auto-hebergement/

## Keywords

Mistral Large 4, Le Chonk, Mistral AI, poids ouverts, open-weight, licence, Mistral Ecosystem Open-Weight License, licence MIT modifiée, Model as a Service, usage interne, Apache 2.0, GLM-5.3, Kimi K3, réversibilité, Design to Exit, souveraineté, auto-hébergement, mixture-of-experts, FP8, NVFP4, GGUF, vLLM, SGLang, llama.cpp, DSpark, décodage spéculatif, Mistral Vibe, Terminal-Bench 4.0, Vals AI, Artificial Analysis, harnais, économie de tokens, cyberdéfense, ENISA, Microsoft Foundry

## Authors

SFEIR AI, voix éditoriale du cabinet SFEIR, article non signé individuellement, publié sur sfeir.com.

## Ton

**Profil** : analyse juridique, matérielle et comparative d'une sortie de modèle, publiée sur le site d'un cabinet, pour DSI, juristes, acheteurs, CTO et RSSI. Français précis, verdict posé dès l'introduction, articles de la licence cités et paraphrasés.

**Registre** : chaque affirmation porte sa source et son statut. Une note de fiabilité finale distingue les chiffres de Mistral, non reproduits, des mesures tierces de Vals AI, datées et susceptibles de bouger, et précise que la lecture de l'article 2 *« est une analyse de SFEIR, pas un avis juridique »*. L'écart de quinze points sur Terminal-Bench est expliqué par la différence de harnais, pas imputé à l'éditeur.

**Posture** : l'article prolonge une grille annoncée lors de la préversion (la souveraineté se jugera sur la licence) et la grille « Design to Exit ». Il reconnaît la logique de l'éditeur (*« ce qui se comprend pour un éditeur qui a entraîné ce modèle sur 3 800 GPU »*) tout en décrivant la conséquence pour l'acheteur. Une section « Ce que l'on ne sait pas encore » et un engagement de révision ferment le texte.

## Pense-betes

- **Sortie** : poids publiés le **29 octobre 2026** sur Hugging Face, checkpoint avec **trois semaines de RL** de plus que la préversion du 6 octobre. Mistral Large 3 (décembre 2025) était sous **Apache 2.0**.
- **Licence** : MIT modifiée. **Article 2** : tout licencié (ou affilié) exploitant un service de modèle — accès tiers à l'inférence ou au post-entraînement avec *« meaningful control »* sur entrées, paramètres ou données — doit signer une licence commerciale. Exclus : produits finaux embarquant le modèle dans des fonctions précises, simple relais. **Article 3** : usage interne et produits Mistral exemptés.
- **Comparaison** : GLM-5.3 (Z.ai) — revue au-delà de **10 Md$** de CA ; Kimi K3 — accord au-delà de **20 M$** de revenu ; Large 4 — **dès le premier euro**, filiales comprises.
- **Points juridiques à qualifier** : portée de « sociétés affiliées » (groupe dont une filiale vend de l'inférence), instance infogérée dédiée, frontière usage interne / filiales.
- **Réversibilité** : sortie 1 (auto-hébergement) entière ; sortie 2 (autre fournisseur géré) soumise à contrat avec Mistral. Hébergeurs cités : **Microsoft Foundry**, NVIDIA (NIM), OpenRouter ; **aucun cloud européen tiers**.
- **Architecture** : 128 experts routés, 4 actifs + 1 partagé, encodeur vision type Pixtral, contexte **1 M** de tokens. Entraîné sur **3 800** GPU Grace Blackwell.
- **Matériel** : FP8 ~1 060 Go, 8 GPU (8 × H200) ; NVFP4 ~610 Go, Blackwell (4 × B300) ; GGUF 2 bits sur Mac Ultra 512 Go (essai, aucun score) ; 4 × RTX 6000 Pro ≈ 10 tokens/s. Cache KV en sus.
- **Logiciel** : vLLM (recommandé), SGLang, Transformers, llama.cpp, Axolotl/Unsloth/TRL ; **DSpark** (décodage spéculatif par blocs de 3 tokens) jusqu'à **1,9x** de débit. Model card : *« we recommend using the Mistral AI API if local serving is subpar »*.
- **API** : **0,70 $ / 2,10 $** par million (0,07 $ en cache), environ la moitié du tarif de préversion (1,36 $ / 4,18 $).
- **Scores** : Terminal-Bench 4.0 41,4 % (Artificial Analysis, dans Mistral Vibe) contre **26,26 % ± 5,13** chez Vals AI (mini-swe-agent), préversion 27,78 % ; tokens par test **25 M** contre 41 M, coût 2,73 $ contre 5,18 $ ; Vals Index **56,5 %** (17e). Coding Agent Index **48 %** avec 8,5 M tokens contre GLM-5.3 49 % avec 15,9 M. Kimi K3 devant sur BrowseComp et FinWorkBench ; Claude Opus 5.5 préféré dans 78 % des cas (Surge Code).
- **Cyber** : AA Cyber Index **50,9 %** ; refus de **96,6 %** des requêtes malveillantes (chiffre éditeur) ; ENISA en test ; variante pentest réservée (Orange Cyberdefense). Le durcissement annoncé s'applique à l'API, pas aux poids publiés.
- **Inconnues** : rapport technique sans date, hébergeurs licenciés, prix de la licence commerciale, évaluation cyber indépendante des refus.

## RésuméDe400mots

Le 29 octobre 2026, Mistral publie sur Hugging Face les poids de Mistral Large 4, un mixture-of-experts d'environ mille milliards de paramètres, enrichi de trois semaines d'apprentissage par renforcement depuis la préversion d'octobre. SFEIR, qui avait écrit que la souveraineté du modèle se jugerait sur sa licence, analyse le texte et le coût de l'auto-hébergement.

La licence, dérivée de la MIT, autorise usage, modification, distribution et dérivés. Son article 2 impose en revanche une licence commerciale séparée à toute entreprise, ou société affiliée, qui exploite un service de modèle, c'est-à-dire qui donne à des tiers un accès à l'inférence avec un contrôle significatif. L'usage interne et l'intégration dans un produit restent libres. Là où GLM-5.3 et Kimi K3 fixent des seuils de revenu, Large 4 n'en a aucun : un petit hébergeur régional doit négocier comme un hyperscaler. SFEIR signale trois points à faire qualifier par un juriste, dont le statut d'une instance infogérée.

Pour la réversibilité, l'auto-hébergement reste entier, mais changer de fournisseur géré suppose que ce fournisseur ait signé avec Mistral. Au 2 novembre, seuls Microsoft Foundry, NVIDIA et OpenRouter sont cités, aucun cloud européen tiers.

Le matériel nécessaire est celui d'un modèle géant : environ un téraoctet de poids en FP8 sur un nœud de huit GPU, six cents gigaoctets en NVFP4 sur Blackwell, une version 2 bits sur Mac à titre d'essai. L'écosystème logiciel était prêt le jour de la sortie, et une tête de décodage spéculatif augmente le débit. L'API coûte environ moitié moins que pendant la préversion.

Les scores annoncés sont relus. Les 41,4 % sur Terminal-Bench viennent de l'agent maison de Mistral ; à harnais constant, Vals AI mesure 26 % et aucun progrès par rapport à la préversion, mais une consommation de tokens et un coût nettement réduits. SFEIR retient cette économie de tokens comme l'argument le plus solide. Côté cyber, les taux de refus élevés mesurés par l'éditeur valent pour les poids distribués, que leur détenteur peut modifier ; le durcissement annoncé ne concerne que l'API.

Les conseils sont donnés par lecteur : héberger le modèle pour ses équipes sans contrat, demander la liste des hébergeurs licenciés, faire qualifier la licence, rejouer ses tests en notant l'identifiant du checkpoint, raisonner en coût par tâche et ne pas compter sur les refus du modèle pour la sécurité.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Mistral Large 4 en poids ouverts : ce que la licence permet, ce que l'auto-hébergement coûte | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Mistral AI | ORGANISATION | publie | Mistral Large 4 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | utilise | Mistral Ecosystem Open-Weight License | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Mistral Ecosystem Open-Weight License | DOCUMENT | est_variante_de | licence MIT | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | remplace | Mistral Large 3 | TECHNOLOGIE | 0.85 | STATIQUE | inféré |
| Mistral Ecosystem Open-Weight License | DOCUMENT | affirme_que | tout service de modèle exige une licence commerciale avec Mistral, sans seuil de revenu | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la licence de Large 4 est plus fermée pour les hébergeurs que celles de GLM-5.3 et Kimi K3 | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | concurrence | GLM-5.3 | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | concurrence | Kimi K3 | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Design to Exit | METHODOLOGIE | s_applique_à | Mistral Large 4 | TECHNOLOGIE | 0.82 | ATEMPOREL | déclaré_article |
| Microsoft Foundry | TECHNOLOGIE | utilise | Mistral Large 4 | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | utilise | DSpark | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| DSpark | TECHNOLOGIE | améliore | jusqu'à 1,9 fois plus de débit sans changement des sorties | MESURE | 0.85 | STATIQUE | déclaré_article |
| Vals AI | ORGANISATION | mesure | Mistral Large 4 à 26,26 % sur Terminal-Bench 4.0 avec mini-swe-agent | MESURE | 0.9 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | Mistral Large 4 à 41 % sur Terminal-Bench 4.0 dans Mistral Vibe | MESURE | 0.88 | STATIQUE | déclaré_article |
| Mistral Vibe | TECHNOLOGIE | utilise | Mistral Large 4 | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | réduit | 25 millions de tokens par test contre 41 pour la préversion | MESURE | 0.85 | STATIQUE | déclaré_article |
| ENISA | ORGANISATION | utilise | Mistral Large 4 | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | comparer le coût par tâche et rejouer ses tests sur le checkpoint publié | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | faire qualifier la clause sur les sociétés affiliées et le statut d'une instance infogérée | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Mistral Large 4 | TECHNOLOGIE | catégorie | MoE 1,05 billion de paramètres, 49 Md actifs, poids publiés le 29/10/2026 | AJOUT |
| Mistral Large 4 | TECHNOLOGIE | prix API | 0,70 $ / 2,10 $ par million de tokens au 02/11/2026 | AJOUT |
| Mistral Ecosystem Open-Weight License | DOCUMENT | clause | Article 2 Model as a Service sans seuil ; article 3 exempte l'usage interne | AJOUT |
| Mistral Large 3 | TECHNOLOGIE | licence | Apache 2.0 (décembre 2025) | AJOUT |
| GLM-5.3 | TECHNOLOGIE | licence | MIT + clause au-delà de 10 Md$ de chiffre d'affaires (Z.ai) | AJOUT |
| Kimi K3 | TECHNOLOGIE | licence | Accord séparé au-delà de 20 M$ de revenu sur douze mois (Moonshot AI) | AJOUT |
| Design to Exit | METHODOLOGIE | définition | Grille SFEIR : le poids ouvert vaut comme garantie de sortie vers l'hébergeur de son choix | AJOUT |
| DSpark | TECHNOLOGIE | catégorie | Tête de décodage spéculatif par blocs de 3 tokens embarquée dans le checkpoint | AJOUT |
| Mistral Vibe | TECHNOLOGIE | catégorie | Agent de code en ligne de commande open source de Mistral | AJOUT |
| Vals AI | ORGANISATION | rôle | Évaluateur tiers à harnais constant (mini-swe-agent) | AJOUT |
