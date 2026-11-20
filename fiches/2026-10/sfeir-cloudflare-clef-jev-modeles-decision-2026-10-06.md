---
themes: [outils-plateformes, architecture-construction, economie-marche]
source: SFEIR
---
# sfeir-cloudflare-clef-jev-modeles-decision-2026-10-06

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **6 octobre 2026** (~2 700 mots, treize sources). Il confronte **Clef** et **Clef-flash**, modèles de décision publiés par **Cloudflare** le **1er octobre 2026** (27 et 9 Md de paramètres, post-entraînés de Qwen), à **Jev** de **TypeSafe AI**, lancé seize jours plus tôt. Trois apports. **(A)** Ce que Clef ajoute : poids ouverts sous **Apache 2.0**, même API que Jev (bascule par endpoint et nom de modèle), jusqu'à **quatre images** en entrée, post-entraînement sur les décisions du client annoncé en design partner. **(B)** La relecture des chiffres : le facteur **13** de latence compare un temps de calcul non documenté à un aller-retour HTTPS (**4,4** au p95) ; le classement où Clef est premier (**61,21**) est un miroir non officiel hébergé par Cloudflare ; Jev garde l'avantage sur les tâches de connaissance (GPQA Diamond **78,3** contre **48,0**). **(C)** Une grille de choix par situation (texte bas prix, images, connaissances, données qui ne sortent pas, fine-tuning) et un protocole d'évaluation : jeu d'essai tiré des journaux, option d'abstention, score de Brier, vecteur de probabilités journalisé. *« Sur la latence, la seule comparaison honnête est celle que vous ferez depuis votre infrastructure. »* Relit l'annonce [[chen-reneau-flansburg-clef-decision-models-2026-10-01]] à la lumière de [[almeida-system-one-models-jev-2026-09-15]].

## Titre Article

Cloudflare Clef face à Jev : quel modèle de décision choisir, et ce que valent les chiffres

## Date

2026-10-06

## URL

https://www.sfeir.com/articles/cloudflare-clef-modeles-de-decision/

## Keywords

Cloudflare Clef, Clef-flash, Jev, TypeSafe AI, modèle de décision, System One Models, Workers AI, open-weight, Apache 2.0, Qwen, LoRA, tête de décision, calibration, score de Brier, RLCD, Jev Decision Index, benchmarks auto-déclarés, latence, p95, GPQA Diamond, MMLU-Pro, BANKING77, BFCL, fine-tuning, design partner, prix par jeton, réversibilité, abstention, courbe de couverture

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : guide de choix comparatif publié sur le site d'un cabinet, à destination déclarée des CTO et architectes d'abord, puis DSI, RSSI et achats. Français technique, structure en questions (« Les latences annoncées se comparent-elles ? », « Clef est-il en tête du Jev Decision Index ? »).

**Style** : chaque chiffre est daté (« au 6 octobre 2026 ») et attribué — billet Cloudflare, changelog, fiche Hugging Face, index communautaire, mesure indépendante de Flavio Copes, relecture de Canberk. Deux tableaux : latences (quatre modèles, trois colonnes de sources) et critères de choix (six lignes, quatre options). Le texte se clôt sur une section par rôle (CTO, DSI, RSSI, achats) et un protocole d'évaluation en quatre points.

**Position épistémique** : la prudence est la ligne directrice — l'article cite la propre méthodologie de Cloudflare reconnaissant que ses latences auto-déclarées ne sont pas comparables, signale que le terme RLCD vient de TypeSafe, que la vidéo n'est pas dans le schéma d'entrée et que la plateforme de fine-tuning n'est pas au catalogue. Il précise que SFEIR n'a pas mesuré Clef et que le texte sera mis à jour quand l'index aura statué.

## Pense-betes

- **Rappel de la catégorie** : un modèle de décision reçoit un état et des questions typées à options fermées, renvoie une probabilité calibrée par option, sans générer de texte ; TypeSafe l'a nommée **System One Models**, Clef en reprend le contrat.
- **Architecture Clef** : Qwen gelé (Qwen3.8-27B / Qwen3.5-9B) + tête de décision + adaptateurs LoRA, sans boucle autorégressive. Données et code d'entraînement privés → **open-weight**, pas open source. Calibration par perte de Brier et un renforcement nommé RLCD.
- **Fenêtre** : 65 536 jetons ; Cloudflare l'oppose aux 32k de Jev, la documentation TypeSafe donne 64k par requête dont 32k pour l'état.
- **Images** : quatre au plus (PNG, JPEG, WebP) ; Flavio Copes mesure 13 à 30 s par requête image, et un base64 de 1,3 Mo dépasse la fenêtre.
- **Latences** (médiane, ms) : Clef 209,3 / Clef-flash 38,8 (auto-déclarés) ; Jev 524,1 (index, HTTPS) ; Flavio Copes : Clef 524-726, Clef-flash 191-205.
- **Leaderboard** : le Jev Decision Index (communautaire, 43 benchmarks, v0.2.1) ne contient pas Clef au 6 octobre. Sur le miroir Cloudflare : Clef 61,21, Jev 57,91, Clef-flash 57,07 (cinquième), deux benchmarks manquants comptés zéro.
- **Benchmarks du billet** : Clef mène 7 sur 10 (BANKING77 94,20 contre 79,74 ; BFCL 98,76 contre 95,75) ; Jev garde When2Call et BRIGHT et domine GPQA Diamond / MMLU-Pro (78,3 / 82,7 contre 48,0 / 65,9).
- **Prix** (par million de jetons d'entrée) : Clef 0,24 $, Clef-flash 0,09 $, Jev 0,042 $ sortie gratuite (5,7 et 2,1 fois moins cher) ; correction du prix de Clef annoncée le 4 octobre, non appliquée au 6.
- **Grille de choix** : texte à haut volume → Jev ; images → Clef ; décisions qui demandent des connaissances → Jev ou LLM génératif derrière le seuil ; données confinées → poids auto-hébergés, Clef-flash en premier ; post-entraînement → Clef en design partner.
- **Protocole** : 100 à 1 000 décisions tirées des journaux, schéma avec option d'abstention, score de Brier et calibration par tranche, seuils sur la courbe couverture/erreur avec repli, vecteur de probabilités journalisé.
- **Seul usage interne testé** : classification de domaines par la Threat Intelligence de Cloudflare (2,2 s contre 4,7 s pour gpt-oss-120b).

## RésuméDe400mots

Le 1er octobre 2026, Cloudflare a publié Clef et Clef-flash, deux modèles de décision de 27 et 9 milliards de paramètres, post-entraînés par l'équipe Workers AI à partir de modèles Qwen. Ils visent Jev, lancé le 15 septembre par TypeSafe AI, dont ils reprennent l'API. Un modèle de décision reçoit un état et des questions à options fermées et renvoie une probabilité calibrée par option, sans générer de texte. L'article de SFEIR examine ce que Clef apporte, ce que valent ses chiffres et comment choisir.

Clef ajoute quatre éléments à Jev. Ses poids se téléchargent sous licence Apache 2.0, mais données et code d'entraînement restent privés. L'API est la même, si bien qu'une intégration bascule en changeant l'endpoint et le nom du modèle. Le modèle accepte jusqu'à quatre images par requête, avec des temps de réponse de 13 à 30 secondes mesurés par Flavio Copes. Enfin, Cloudflare annonce un post-entraînement sur les décisions du client, d'abord en partenariat accompagné, la version en libre-service étant encore en construction.

Les chiffres demandent une lecture attentive. Le gain de latence de 13 fois revendiqué pour Clef-flash compare un temps de calcul sur un matériel non divulgué à un aller-retour HTTPS vers l'API de Jev ; au p95, le rapport tombe à 4,4. La méthodologie de Cloudflare reconnaît elle-même que ses latences auto-déclarées ne sont pas comparables. Le classement où Clef arrive premier est un miroir non officiel hébergé par Cloudflare, l'index communautaire ne l'ayant pas encore intégré. Clef mène sur sept des dix benchmarks choisis, mais Jev l'emporte nettement dès que la décision demande des connaissances, sur GPQA Diamond comme sur MMLU-Pro. Clef est aussi plus cher par jeton d'entrée.

L'article propose donc un choix par situation : Jev pour le texte à bas prix et les décisions qui mobilisent des connaissances, Clef pour les images et le post-entraînement, les poids auto-hébergés pour les données qui ne peuvent pas sortir. Il recommande d'évaluer sur un jeu d'essai tiré des journaux de l'entreprise, avec une option d'abstention, un score de Brier, une courbe de couverture contre erreur et un repli vers un LLM ou un humain sous le seuil, et de journaliser le vecteur de probabilités pour l'audit. Chaque rôle reçoit une consigne : interface interchangeable pour les architectes, budget au volume pour le DSI, courbe de fiabilité exigée par le RSSI, pas de contrat sur le tarif de lancement pour les achats. SFEIR précise n'avoir pas mesuré Clef lui-même.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Cloudflare Clef face à Jev | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Cloudflare | ORGANISATION | publie | Clef | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| TypeSafe AI | ORGANISATION | publie | Jev | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | concurrence | Jev | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Clef | TECHNOLOGIE | est_instance_de | modèle de décision | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Jev | TECHNOLOGIE | est_instance_de | modèle de décision | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Clef | TECHNOLOGIE | est_basé_sur | Qwen | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Clef-flash | TECHNOLOGIE | est_variante_de | Clef | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | utilise | score de Brier | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | permet | décisions sur images en entrée | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le facteur 13 de latence compare un temps de calcul non documenté à un aller-retour HTTPS | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Jev | TECHNOLOGIE | surpasse | GPQA Diamond 78,3 contre 48,0 pour Clef | MESURE | 0.87 | STATIQUE | déclaré_article |
| Clef | TECHNOLOGIE | mesure | 7 benchmarks sur 10 en tête (auto-déclaré) | MESURE | 0.85 | STATIQUE | déclaré_article |
| Jev Decision Index | DOCUMENT | référence | Jev | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Flavio Copes | PERSONNE | mesure | médiane Clef-flash 191 à 205 ms via API REST | MESURE | 0.85 | STATIQUE | déclaré_article |
| Canberk | PERSONNE | affirme_que | tant que l'index n'a pas validé les scores, l'avance de Clef est la mesure de Cloudflare | AFFIRMATION | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | évaluer sur un jeu d'essai tiré des journaux avec score de Brier et courbe de couverture | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | journaliser le vecteur de probabilités avec chaque décision | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, éditeur de sfeir.com | AJOUT |
| Cloudflare | ORGANISATION | rôle | Éditeur de Clef via l'équipe Workers AI | AJOUT |
| Clef | TECHNOLOGIE | définition | Modèle de décision 27 Md de paramètres, Apache 2.0, API compatible Jev, images en entrée | AJOUT |
| Clef-flash | TECHNOLOGIE | définition | Variante 9 Md de paramètres de Clef, post-entraînée de Qwen3.5-9B | AJOUT |
| Jev | TECHNOLOGIE | définition | Modèle de décision fermé de TypeSafe, texte seul, 0,042 $ par million de jetons d'entrée | AJOUT |
| TypeSafe AI | ORGANISATION | rôle | Créateur de Jev et de la catégorie System One Models | AJOUT |
| modèle de décision | CONCEPT | définition | Modèle renvoyant une probabilité calibrée par option fermée, sans génération de texte | AJOUT |
| Jev Decision Index | DOCUMENT | définition | Classement communautaire Hugging Face, 43 benchmarks, sans affiliation avec TypeSafe | AJOUT |
| score de Brier | CONCEPT | définition | Moyenne du carré de l'écart entre probabilité annoncée et résultat | AJOUT |
| Flavio Copes | PERSONNE | rôle | Auteur d'une mesure indépendante de Clef via l'API REST | AJOUT |
