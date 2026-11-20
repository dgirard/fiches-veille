---
themes: [politique-regulation, produits-services, qualite-securite]
source: SFEIR
---
# sfeir-mistral-large-4-souverainete-licence-2026-10-06

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **6 octobre 2026** et mis à jour le **2 novembre 2026** (~2 500 mots, dix sources). Il analyse la preview API de **Mistral Large 4** : MoE de **1 000 Md** de paramètres, **49 Md** actifs, multimodal en entrée, poids promis pour le **27 octobre**. Trois apports. **(A)** Un tableau annonce/mesure : Terminal-Bench 4 **28,3 %** annoncés contre **22,73 %** mesurés par Vals AI ; DeepSWE **61,7 %** contre un sommet de leaderboard vers **74 %** ; Harvey Legal Agent tient (**15,83 %**, premier open-weights) ; Vals Index **48,05 %**, 32e sur 44. **(B)** La cyberdéfense : **82 %** en reproduction de vulnérabilité (AA Cyber Index), là où Claude Opus 5.5 et GPT-6 Astra refusent la tâche ; l'article note que l'écart mesure à la fois une capacité et une politique de refus, et que les refus disparaissent avec la publication des poids (abliteration de GLM-5.3 chiffrée à **4 400 $**). **(C)** La souveraineté suspendue à la licence : trois régimes antérieurs (Research License, Apache 2.0, API seule), entraînement en Europe sur **3 800 GPU** NVIDIA, Series D de **3 Md€** menée par Samsung. La mise à jour indique des poids publiés le **29 octobre** sous une MIT modifiée avec licence commerciale obligatoire pour les hébergeurs. Complète l'annonce [[mistral-large-4-le-chonk-2026-10-06]].

## Titre Article

Mistral Large 4 : 1 000 milliards de paramètres en open-weights, une souveraineté qui se jugera sur la licence

## Date

2026-10-06

## URL

https://www.sfeir.com/articles/mistral-large-4-open-weights-souverainete/

## Keywords

Mistral Large 4, Le Chonk, Mistral AI, open-weights, mixture-of-experts, souveraineté numérique, licence des poids, Mistral Ecosystem Open-Weight License, Apache 2.0, Vals AI, DeepSWE, Terminal-Bench 4, Harvey Legal Agent, AA Cyber Index, Cybench, cyberdéfense, politique de refus, abliteration, red-teaming, GLM-5.3, Kimi K3, Series D, Samsung, NVIDIA Grace Blackwell, réversibilité, Design to Exit

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : analyse d'une annonce de modèle publiée le jour même sur le site d'un cabinet, pour DSI, RSSI, CTO et achats. Français soigné, citations anglaises traduites entre parenthèses, verdict posé dès l'introduction (*« à tester dès maintenant sur vos propres évaluations, à ne pas engager avant la licence et le checkpoint final »*).

**Style** : un tableau en cinq lignes oppose chiffres de l'éditeur et mesures tierces, avec une colonne « Lecture » ; l'article invite à lire la colonne de droite avant celle du milieu. Les propos de Pierre Stock, Guillaume Lample et d'un dirigeant cité par le Journal du Net sont restitués entre guillemets. Section finale par lecteur et liste « Ce que l'on ne sait pas encore ».

**Position épistémique** : la note de fiabilité distingue chiffres déclarés, mesures tierces datées et caractérisations propres à SFEIR (« politique de refus », « souveraineté relative »). L'article déclare le partenariat de SFEIR avec Anthropic (palier Preferred) et Google Cloud. La mise à jour du 2 novembre est placée en tête et renvoie à un second article pour l'analyse de la licence finale.

## Pense-betes

- **Fiche technique (preview du 6 octobre)** : 1 000 Md de paramètres, 49 Md actifs, MoE hybride, multimodal en entrée, 160 langues ; entraîné sur 3 800 GPU Grace Blackwell en deux mois environ, cluster d'une dizaine de MW en France ; prix de preview 1,36 $ / 4,18 $ par million de tokens.
- **Annonce vs mesure** : Terminal-Bench 4 28,3 % → 22,73 % (Vals, 20e sur 44) ; DeepSWE 61,7 % vs GLM-5.3 et Kimi K3 vers 69 %, GPT-6 Astra, Gemini 3.8 Flash, Claude Opus 5 vers 74 % (harnais différents) ; Harvey Legal Agent 15 % → 15,83 % (6e sur 75).
- **Formule de Mistral** : le modèle surpasserait tout open-weights américain ou européen ; l'article relève qu'elle exclut la Chine.
- **Run de RL en cours** : la preview n'est pas le modèle final (*« no signs of saturation »*).
- **Cyber** : AA Cyber Index 82 %, Cybench 93 % (chiffres éditeur, aucune mesure indépendante au 6 octobre). Refus moyen revendiqué supérieur aux open source sur JailbreakBench, StrongREJECT, AgentHarm.
- **Accès red-teaming** : trois semaines à moindre modération, réservé à des responsables cyber, partenaires vérifiés et autorités.
- **Tension relevée** : une fois les poids téléchargés, les refus côté serveur ne s'appliquent plus ; l'article renvoie à l'abliteration de GLM-5.3 évaluée par Anthropic à 4 400 $ de GPU. Conséquence pour le RSSI : la vitesse de correction du code interne devient la variable contrôlable.
- **Trois régimes de licence passés** : Large 2 (Mistral Research License), Large 3 (Apache 2.0, déc. 2025), premier Large et Medium (API seule).
- **Composition souveraine** : société et infrastructure françaises, puces NVIDIA, Series D de 3 Md€ (>21 Md€ post-money) menée par Samsung avec EQT et PSG Equity.
- **Auto-hébergement** : 49 Md actifs réduisent le calcul, pas la mémoire ; pour la plupart des DSI, le poids ouvert servira de garantie de sortie (Design to Exit).
- **Mise à jour (2 nov.)** : poids publiés le 29 octobre, Mistral Ecosystem Open-Weight License (MIT modifiée, usage interne libre, licence commerciale pour les hébergeurs sans seuil de revenu), API à 0,70 $ / 2,10 $.

## RésuméDe400mots

Le 6 octobre 2026, Mistral a ouvert en preview publique par API Mistral Large 4, un mixture-of-experts de 1 000 milliards de paramètres dont 49 milliards actifs par token, multimodal en entrée et texte en sortie, avec des poids promis pour le 27 octobre. L'article de SFEIR situe le modèle dans la catégorie des meilleurs open-weights chinois, GLM-5.3 et Kimi K3, sans avance sur eux, et à distance des modèles fermés en code agentique.

Un tableau confronte les chiffres de Mistral aux mesures tierces publiées le même jour. Sur Terminal-Bench 4, les 28,3 % annoncés deviennent 22,73 % chez Vals AI. Sur DeepSWE, les 61,7 % restent honorables, mais le sommet du leaderboard public se situe douze points plus haut. Seul Harvey Legal Agent tient à la mesure indépendante, où Large 4 est le premier open-weights. Le Vals Index le classe 32e sur 44. Le run d'apprentissage par renforcement étant en cours, la preview diffère du modèle final.

Le point que Mistral met en avant est la cyberdéfense : 82 % en reproduction de vulnérabilité sur l'AA Cyber Index, là où Claude Opus 5.5 et GPT-6 Astra obtiennent un score proche de zéro parce qu'ils refusent la tâche. L'article souligne que ce test mesure à la fois une capacité et une politique de refus. Mistral ouvre trois semaines d'accès à moindre modération à des acteurs de cybersécurité vérifiés. Une fois les poids publiés, les filtres côté serveur ne s'appliquent plus et peuvent être retirés, comme l'a montré l'évaluation de GLM-5.3 par Anthropic ; la défense dépendra alors de la vitesse de correction des failles.

Sur la souveraineté, l'article attend la licence. Mistral a déjà pratiqué une licence de recherche, Apache 2.0 et le service par API seule. L'entraînement a eu lieu en Europe sur 3 800 GPU NVIDIA, et la dernière levée de 3 milliards d'euros a été menée par Samsung. Héberger 1 000 milliards de paramètres demande une grappe de GPU récents : pour la plupart des DSI, le poids ouvert jouera le rôle de garantie de sortie, dont la valeur dépend de la licence.

Recommandations par lecteur : inscrire Large 4 comme candidat à la couche européenne d'une architecture multi-LLM sans engagement contractuel avant la licence ; demander l'accès red-teaming et préparer la sortie des poids ; tester sur ses propres évaluations en notant le checkpoint ; annexer la licence à tout contrat d'API. La mise à jour du 2 novembre signale des poids publiés le 29 octobre sous une licence MIT modifiée imposant une licence commerciale aux hébergeurs.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Mistral Large 4 : une souveraineté qui se jugera sur la licence | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Mistral AI | ORGANISATION | publie | Mistral Large 4 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | remplace | Mistral Large 3 | TECHNOLOGIE | 0.85 | STATIQUE | inféré |
| Mistral Large 4 | TECHNOLOGIE | concurrence | GLM-5.3 | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | concurrence | Kimi K3 | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Vals AI | ORGANISATION | mesure | Terminal-Bench 4 : 22,73 % mesurés contre 28,3 % annoncés | MESURE | 0.9 | STATIQUE | déclaré_article |
| Vals AI | ORGANISATION | mesure | Harvey Legal Agent 15,83 %, 6e sur 75 | MESURE | 0.88 | STATIQUE | déclaré_article |
| Mistral AI | ORGANISATION | affirme_que | 82 % en reproduction de vulnérabilité sur l'AA Cyber Index | MESURE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le score cyber mesure à la fois une capacité et une politique de refus | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les refus côté serveur ne protègent plus une fois les poids publiés | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Guillaume Lample | PERSONNE | travaille_chez | Mistral AI | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Pierre Stock | PERSONNE | travaille_chez | Mistral AI | ORGANISATION | 0.94 | DYNAMIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | utilise | NVIDIA Grace Blackwell | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Samsung Electronics | ORGANISATION | collabore_avec | Mistral AI | ORGANISATION | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la valeur souveraine de Large 4 dépend de la licence des poids | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | utilise | Mistral Ecosystem Open-Weight License | DOCUMENT | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | ne pas engager contractuellement avant la licence et le checkpoint final | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | annexer la licence des poids à tout contrat d'API | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, éditeur de sfeir.com | AJOUT |
| Mistral AI | ORGANISATION | financement | Series D de 3 Md€ (sept. 2026), >21 Md€ post-money | AJOUT |
| Mistral Large 4 | TECHNOLOGIE | définition | MoE 1 000 Md de paramètres, 49 Md actifs, preview 6 oct. 2026, poids publiés 29 oct. 2026 | AJOUT |
| Vals AI | ORGANISATION | rôle | Évaluateur indépendant de modèles (Vals Index) | AJOUT |
| Guillaume Lample | PERSONNE | rôle | Cofondateur de Mistral AI | AJOUT |
| Pierre Stock | PERSONNE | rôle | VP science et premier salarié de Mistral AI | AJOUT |
| Mistral Ecosystem Open-Weight License | DOCUMENT | définition | MIT modifiée : usage interne libre, licence commerciale pour les hébergeurs revendant l'accès | AJOUT |
| Samsung Electronics | ORGANISATION | rôle | Chef de file de la Series D de Mistral AI | AJOUT |
