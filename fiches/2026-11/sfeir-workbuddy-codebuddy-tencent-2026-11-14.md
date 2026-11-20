---
themes: [produits-services, economie-marche, politique-regulation]
source: SFEIR
---
# sfeir-workbuddy-codebuddy-tencent-2026-11-14

## Veille

Article SFEIR AI publié sur sfeir.com le **14 novembre 2026** (~900 mots), qui présente les deux agents de **Tencent** portés par la même équipe sous la direction de **Liu Yi** (vice-président de Tencent Cloud) : **CodeBuddy**, agent de code distribué en CLI depuis le **9 septembre 2025**, et **WorkBuddy**, agent de bureau pour tous les métiers, lancé en Chine le **9 mars 2026** et à l'international le **28 mai 2026** (*« the agentic AI workspace »*). Trois apports : (A) une chronologie de WorkBuddy (Enterprise et Agent Suite en juin, plateforme ouverte avec **plus de 100 partenaires** en septembre, espace Buddy One fin octobre) et ses modèles (Hunyuan, DeepSeek, GLM, Kimi, MiniMax en Chine ; *hy4-preview* à l'international) ; (B) les tarifs relevés le 14 novembre (gratuit, Pro **10 $/mois**, Team **40 $/siège/mois**) et les chiffres d'usage interne déclarés par Tencent en 2025 (**plus de 90 %** des ingénieurs sur CodeBuddy, **plus de 50 %** de code généré), présentés comme non vérifiés ; (C) le lien par **TencentDB Agent Memory**, qui prend en charge les deux agents, et la localisation des données (serveurs à **Singapour** pour l'édition internationale de WorkBuddy, accès possible d'équipes en Chine, conservation jusqu'à quatorze jours). L'article propose trois questions à poser par une DSI européenne. Volet de la série SFEIR sur la mémoire d'agent, à rapprocher de la fiche [[OpenClaw]], dont WorkBuddy accepte les skills.

## Titre Article

WorkBuddy et CodeBuddy : la double offensive agentique de Tencent

## Date

2026-11-14

## URL

https://www.sfeir.com/articles/workbuddy-codebuddy-offensive-agentique-tencent/

## Keywords

Tencent, WorkBuddy, CodeBuddy, CodeBuddy Code, Liu Yi, Tencent Cloud, agent de bureau, agent de code, Buddy One, Hunyuan, DeepSeek, GLM, Kimi, MiniMax, OpenClaw skills, WeCom, tarifs, TencentDB Agent Memory, Singapour, localisation des données, souveraineté, Matrice Souveraineté Agentique

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Article de panorama produit en français, de registre factuel, destiné aux DSI et responsables de la souveraineté. Le texte procède par tableaux et chronologies datées, chaque étape renvoyant à une source (communiqués, presse chinoise et internationale, page tarifaire, politique de confidentialité). Il distingue les chiffres déclarés par l'éditeur, qu'il reprend en le précisant, de ceux qu'il n'a pas pu rattacher à une source et qu'il écarte explicitement. Les extraits de la politique de confidentialité sont cités en anglais, sans commentaire. La conclusion est formulée en trois questions de due diligence et rappelle qu'un agent qui lit les fichiers du poste élargit le périmètre par rapport à un agent de code limité à un dépôt.

## Pense-betes

- **Une équipe, deux produits** (Liu Yi, VP Tencent Cloud) : **CodeBuddy** (développeurs ; CLI `@tencent-ai/codebuddy-code`, IDE, extensions VS Code/JetBrains, Zed ; CLI depuis le 9 septembre 2025) ; **WorkBuddy** (métiers de bureau ; agent de bureau pilotable par messagerie). Code source non publié pour les deux.
- **WorkBuddy** agit sur fichiers, documents, présentations ; accepte les skills d'OpenClaw ; son mode Coding délègue à CodeBuddy ; pilotage par Discord, Slack, Telegram (hors Chine) ou WeCom (Chine).
- **Chronologie WorkBuddy** : tests internes 6 février 2026 → Chine 9 mars → international 28 mai (Tencent Cloud Day, Hong Kong) → Enterprise et Agent Suite 5 juin → plateforme ouverte 2 septembre (100+ partenaires) → Buddy One fin octobre.
- **Modèles** : Hunyuan, DeepSeek, GLM, Kimi, MiniMax en Chine ; *hy4-preview* dans le test AtlasCloud (4 novembre 2026).
- **Tarifs** (14 novembre 2026) : gratuit ; Pro 10 $/mois (96 $/an) ; Team 40 $/siège/mois (480 $/an) ; crédits mensuels changeants.
- **Chiffres Tencent** (9 septembre 2025, non vérifiés) : 90 %+ d'ingénieurs sur CodeBuddy, 50 %+ de code généré, gain d'efficacité 16 %+. Chiffres de fréquentation WorkBuddy écartés faute de source.
- **Mémoire commune** : TencentDB Agent Memory prend en charge CodeBuddy et WorkBuddy (client ajouté en 2.0.1, 25 août 2026) ; formule modèle + harnais + mémoire.
- **Données** : CodeBuddy Entreprise à Singapour (accès possible d'équipes en Chine), individuel possiblement en Chine continentale ; WorkBuddy international : *« stored in servers in Singapore »*, responsable Tencent Cloud International, entrées/sorties conservées jusqu'à 14 jours.
- **Trois questions DSI** : quelle édition, quelle région au contrat, quels modèles appelés.
- À relier : [[DeepSeek-organisation]].

## RésuméDe400mots

L'article présente les deux produits agentiques de Tencent, développés par une même équipe placée sous la responsabilité de Liu Yi, vice-président de Tencent Cloud. CodeBuddy est un agent de code destiné aux développeurs, disponible en ligne de commande depuis septembre 2025 ainsi que dans un IDE et des extensions. WorkBuddy, présenté comme un espace de travail agentique, s'adresse à tous les métiers de bureau ; lancé en Chine en mars 2026 puis à l'international en mai, il agit sur les fichiers, documents et présentations du poste. Le code source des deux produits n'est pas publié.

WorkBuddy accepte les skills d'OpenClaw, délègue les tâches de code au moteur de CodeBuddy et se pilote à distance par messagerie, Discord, Slack ou Telegram hors de Chine, WeCom en Chine. L'article retrace sa chronologie : tests internes en février, lancements chinois et international, édition Entreprise en juin, plateforme ouverte à plus de cent partenaires en septembre, puis un espace de travail baptisé Buddy One fin octobre. En Chine, l'utilisateur choisit entre plusieurs modèles chinois ; l'édition internationale testée utilisait un modèle Tencent.

Les tarifs relevés vont d'une formule gratuite à une formule équipe à 40 dollars par siège et par mois, avec des crédits dont le détail change souvent. Tencent a déclaré en 2025 que plus de 90 % de ses ingénieurs utilisaient CodeBuddy et que plus de la moitié de son code était généré par IA ; SFEIR précise que ces chiffres ne sont pas vérifiés de manière indépendante et écarte les chiffres de fréquentation de WorkBuddy, faute de source.

Le lien entre les deux produits passe par TencentDB Agent Memory, le hub de mémoire open source de Tencent Cloud, qui les prend en charge tous deux : un développeur et un chef de projet peuvent lire la même mémoire d'équipe avec des droits distincts. Tencent assemble ainsi modèle, harnais et mémoire.

La dernière partie porte sur la localisation des données. L'édition Entreprise de CodeBuddy et l'édition internationale de WorkBuddy stockent les données à Singapour, avec un accès possible d'équipes situées en Chine ; les entrées et sorties de WorkBuddy sont conservées jusqu'à quatorze jours. L'article recommande à une DSI européenne de vérifier l'édition, la région d'hébergement inscrite au contrat et les modèles appelés, en notant qu'un agent de bureau élargit le périmètre exposé.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | WorkBuddy et CodeBuddy : la double offensive agentique de Tencent | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Tencent | ORGANISATION | a_créé | WorkBuddy | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Tencent | ORGANISATION | a_créé | CodeBuddy | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Liu Yi | PERSONNE | travaille_chez | Tencent Cloud | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| Tencent Cloud | ORGANISATION | fait_partie_de | Tencent | ORGANISATION | 0.9 | DYNAMIQUE | inféré |
| WorkBuddy | TECHNOLOGIE | utilise | CodeBuddy | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| WorkBuddy | TECHNOLOGIE | utilise | OpenClaw | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| WorkBuddy | TECHNOLOGIE | utilise | Hunyuan | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| WorkBuddy | TECHNOLOGIE | utilise | DeepSeek | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Tencent | ORGANISATION | publie | lancement international de WorkBuddy | EVENEMENT | 0.93 | STATIQUE | déclaré_article |
| WorkBuddy | TECHNOLOGIE | mesure | Pro 10 $/mois, Team 40 $/siège/mois (14 novembre 2026) | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| Tencent | ORGANISATION | mesure | plus de 90 % des ingénieurs sur CodeBuddy, plus de 50 % de code généré par IA | MESURE | 0.8 | STATIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | s_applique_à | WorkBuddy | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| TencentDB Agent Memory | TECHNOLOGIE | s_applique_à | CodeBuddy | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| WorkBuddy | TECHNOLOGIE | affirme_que | Your personal information will be stored in servers in Singapore | CITATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | vérifier l'édition, la région d'hébergement au contrat et les modèles appelés | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| WorkBuddy | TECHNOLOGIE | catégorie | Agent de bureau Tencent ; Chine 9 mars 2026, international 28 mai 2026 | AJOUT |
| CodeBuddy | TECHNOLOGIE | catégorie | Agent de code Tencent ; CLI depuis le 9 septembre 2025 | AJOUT |
| Tencent | ORGANISATION | secteur | Groupe internet chinois | AJOUT |
| Liu Yi | PERSONNE | rôle | Vice-président de Tencent Cloud, dirige CodeBuddy et WorkBuddy | AJOUT |
| lancement international de WorkBuddy | EVENEMENT | date | 28 mai 2026, Tencent Cloud Day, Hong Kong | AJOUT |
| Hunyuan | TECHNOLOGIE | catégorie | Famille de modèles de Tencent | AJOUT |
