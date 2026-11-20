---
themes: [produits-services, economie-marche, qualite-securite]
source: SFEIR
---
# sfeir-gemini-4-argon-moitie-prix-2026-10-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** (~11 000 signes, 15 sources, complété d'une note datée du 15 novembre). Il fait le point sur **Gemini 4 Argon**, présenté par **Koray Kavukcuoglu** (**Google DeepMind**) le 30 septembre et ouvert à tous les clients payants le **13 octobre**. **(1) Accès** : API Gemini, app Gemini (Pro, Ultra), Antigravity, AI Studio, Gemini Enterprise ; multirégion « eu » avec activation par défaut au 27 octobre, sans couverture de la Suisse ni du Royaume-Uni. **(2) Prix** : **2 $ / 10 $** le million de tokens jusqu'au 30 novembre, puis **4 $ / 20 $**, le tarif retenu par Meta pour Muse Wonder ; contexte de **1 048 576** tokens. **(3) Mesures** : Argon mène sur DeepSWE (77,9) et recule sur Terminal-bench 4.0 (57,4 contre 66,4 pour Claude Opus 5.5) ; **Artificial Analysis** lui donne 53 points et le taux d'hallucination le plus bas des modèles de tête (**15 %**) ; Bloomberg rapporte un scepticisme interne sur le code, que Google conteste. **(4) Cyber** : Google DeepMind ne peut exclure que la version sans garde-fous atteigne le seuil critique de son **Frontier Safety Framework** (cyberattaque grave **16,7 fois** moins chère) ; double régime d'accès via le **Fairwind Program**. Suite de la gamme dans [[sfeir-gemini-4-carbon-2026-10-28]] ; comparaison de prix avec [[sfeir-muse-wonder-meta-muse-code-2026-10-15]].

## Titre Article

Gemini 4 Argon : le modèle frontier de Google, à moitié prix jusqu'au 30 novembre

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/gemini-4-argon-disponible-moitie-prix-30-novembre/

## Keywords

Gemini 4 Argon, Google, Google DeepMind, modèle frontier, disponibilité générale, prix promotionnel, 2 $ / 10 $, 4 $ / 20 $, Batch, Flex, fenêtre de contexte, long decode, Gemini Enterprise, résidence des données UE, Antigravity, benchmarks, DeepSWE, Terminal-bench, Artificial Analysis, AA-Omniscience, hallucination, Frontier Safety Framework, cybersécurité, Fairwind Program, GPT-6 Astra, Claude Opus 5.5, Muse Wonder

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, publiée sur sfeir.com (site éditorial de l'ESN).

## Ton

**Profil** : fiche d'actualité produit destinée aux DSI, architectes, acheteurs et RSSI. Français factuel, prix, dates et tailles de contexte donnés à l'unité près, chaque affirmation rattachée à une source numérotée.

**Style** : sections fonctionnelles (qui peut l'utiliser et où, le prix, ce que disent les mesures, le volet cyber, que tester d'ici le 30 novembre). Un tableau de cinq benchmarks met chaque score d'Argon en regard du concurrent le mieux placé, avec la mention « Scores publiés par Google ». Une liste de quatre tests à mener pendant la fenêtre promotionnelle clôt le texte ; la note du 15 novembre (fin du tarif réduit, retrait de Copilot au 14 décembre, sortie de Gemini 4 Hydrogen) est portée en historique.

**Position épistémique** : distinction nette entre scores éditeur, mesures indépendantes (Artificial Analysis, The Batch) et presse (Bloomberg, Business Insider). Les signaux contradictoires sur le code sont présentés côte à côte, avec la contestation de Google. Le volet sécurité reprend les formulations négatives du rapport (« ne pas pouvoir exclure ») et cite le dilemme formulé par le Blog du Modérateur. Le conseil final renvoie au test sur ses propres cas (« seuls vos projets trancheront »).

## Pense-betes

- **Calendrier** : présenté le **30/09/2026** (Kavukcuoglu, Google DeepMind) aux cyberdéfenseurs du Fairwind Program ; ouvert à tous les clients payants le **13/10**.
- **Canaux** : API Gemini (palier payant, monde entier) ; app Gemini (Pro, Ultra) ; Antigravity (Ultra, Gemini Enterprise) ; AI Studio web (Ultra) ; Vertex AI, rebaptisé **Gemini Enterprise Agent Platform**, en GA.
- **Europe** : multirégion « eu » de Gemini Enterprise (données et traitement dans l'UE) ; Argon désactivé par défaut jusqu'au **27/10** ; ni Suisse ni Royaume-Uni.
- **Prix** : **2 $ / 10 $** jusqu'au 30/11, puis **4 $ / 20 $**, sans palier de contexte ; Batch et Flex à moitié prix. Même tarif que **Muse Wonder** (Meta, 12/10).
- **Contexte** : **1 048 576** tokens partagés ; sortie 65 536 par défaut, ~1 M en « long decode » (API v1beta1).
- **Benchmarks Google** : DeepSWE **77,9** vs 74,2 (Opus 5.5) ; Vals Index 68,9 vs 67,0 ; CWE-bench 68 = GPT-6 Astra ; Terminal-bench 4.0 **57,4 vs 66,4** ; FrontierSWE 55,0 vs 65,5 (GPT-6 Astra).
- **Mesures indépendantes** : Artificial Analysis Intelligence Index **53** (niveau GPT-6 Astra, derrière les derniers Anthropic) ; AA-Omniscience : hallucination **15 %**, la plus basse des modèles de tête. The Batch : brille en finance, fiscalité, droit, pas le meilleur choix pour le code.
- **Signaux internes** : Bloomberg (02/10) — employés soupçonnant une optimisation pour les benchmarks ; Business Insider (mi-septembre) — ingénieurs Google autorisés à utiliser Claude Opus 5 dans Antigravity.
- **Rapport de sécurité** : seuil critique cyber du Frontier Safety Framework non exclu pour la version sans garde-fous (attaque grave **~16,7× moins chère**) ; seuil biologique non exclu ; évaluations externes AISI britannique, NIST, Faculty.
- **Double régime** : version publique bloquant l'offensif ; variante `gemini-4-argon-cyber-permissive` pour Fairwind (candidature, vérification, usage interne cyber, MFA résistante au phishing, pas de revente) ; programme élargi à plusieurs centaines de partenaires le 13/10.
- **À tester d'ici le 30/11** : 30-50 tâches de connaissance réelles en comptant les erreurs factuelles ; code dans ses propres dépôts ; configuration « eu » ; candidature Fairwind pour les RSSI avec SOC interne.
- **Note du 15/11** : Copilot retire Argon le 14/12 au profit de Gemini 4 Carbon ; **Gemini 4 Hydrogen** (12/11, 1,50 $ / 7,50 $) à 51 points sur l'index v5.0.1, contre 50 pour Argon.

## RésuméDe400mots

L'article, signé SFEIR AI, fait le point sur Gemini 4 Argon, le modèle frontier de Google, ouvert le 13 octobre 2026 à tous les clients payants, deux semaines après une première diffusion réservée à des cyberdéfenseurs vérifiés. Google le destine au code, aux agents qui enchaînent de longues tâches, au travail de connaissance et à la cyberdéfense.

Le modèle est disponible sur l'API Gemini, l'app Gemini, Antigravity, AI Studio et la plateforme d'entreprise de Google Cloud. Les entreprises européennes peuvent passer par la multirégion « eu », qui garde données et traitement dans l'Union, mais ne couvre ni la Suisse ni le Royaume-Uni ; Argon y reste désactivé par défaut jusqu'au 27 octobre.

Jusqu'au 30 novembre, Google facture 2 dollars le million de tokens en entrée et 10 en sortie, puis 4 et 20, soit le tarif que Meta a retenu pour Muse Wonder. La fenêtre de contexte atteint un peu plus d'un million de tokens.

Les mesures sont contrastées. Dans le tableau publié par Google, Argon devance ses concurrents sur DeepSWE et le Vals Index, mais recule sur Terminal-bench 4.0 et FrontierSWE face à Claude Opus 5.5 et GPT-6 Astra. Artificial Analysis lui attribue 53 points sur son Intelligence Index, au niveau de GPT-6 Astra, et mesure le taux d'hallucination le plus bas parmi les modèles de tête, à 15 %. The Batch en conclut qu'Argon convient à la finance, à la fiscalité et au droit plus qu'au code. Bloomberg a par ailleurs rapporté le scepticisme d'employés de Google sur ses performances en développement, ce que Google conteste.

Le volet cyber occupe une place importante. Dans son rapport de sécurité, Google DeepMind indique ne pas pouvoir exclure que la version sans garde-fous atteigne le seuil critique cyber de son Frontier Safety Framework, et estime qu'elle rendrait une cyberattaque grave environ 16,7 fois moins chère. Google a donc prévu deux régimes : une version publique qui bloque les tâches offensives, et une variante permissive réservée aux membres du Fairwind Program, soumis à vérification et à des conditions d'usage strictes.

L'article recommande de profiter des sept semaines de prix réduit pour tester Argon sur des tâches réelles de connaissance en comptant les erreurs factuelles, dans ses propres dépôts pour le code, et de vérifier la configuration européenne. Une note ajoutée le 15 novembre signale la fin du tarif réduit, le retrait d'Argon de GitHub Copilot au 14 décembre et la sortie de Gemini 4 Hydrogen.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Gemini 4 Argon : le modèle frontier de Google, à moitié prix jusqu'au 30 novembre | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Google DeepMind | ORGANISATION | publie | Gemini 4 Argon | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Koray Kavukcuoglu | PERSONNE | travaille_chez | Google DeepMind | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | mesure | 2 $ / 10 $ le million de tokens jusqu'au 30 novembre 2026, puis 4 $ / 20 $ | MESURE | 0.95 | DYNAMIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | concurrence | GPT-6 Astra | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | concurrence | Claude Opus 5.5 | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | concurrence | Muse Wonder | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | surpasse | Claude Opus 5.5 | TECHNOLOGIE | 0.82 | STATIQUE | déclaré_article |
| Claude Opus 5.5 | TECHNOLOGIE | surpasse | Gemini 4 Argon | TECHNOLOGIE | 0.82 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | taux d'hallucination de Gemini 4 Argon à 15 % sur AA-Omniscience, le plus bas des modèles de tête | MESURE | 0.9 | STATIQUE | déclaré_article |
| The Batch | DOCUMENT | affirme_que | Gemini 4 Argon brille en finance, fiscalité et droit sans être le meilleur choix pour le code | AFFIRMATION | 0.86 | STATIQUE | déclaré_article |
| Google DeepMind | ORGANISATION | affirme_que | la version sans garde-fous d'Argon pourrait atteindre le seuil critique cyber et rendre une attaque grave ~16,7 fois moins chère | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | est_basé_sur | Frontier Safety Framework | DOCUMENT | 0.8 | STATIQUE | inféré |
| Fairwind Program | TECHNOLOGIE | permet | accès à la variante gemini-4-argon-cyber-permissive pour des équipes de cyberdéfense vérifiées | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | tester Argon sur 30 à 50 tâches réelles en comptant les erreurs factuelles avant le 30 novembre | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Gemini 4 Hydrogen | TECHNOLOGIE | surpasse | Gemini 4 Argon | TECHNOLOGIE | 0.8 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Gemini 4 Argon | TECHNOLOGIE | catégorie | Modèle frontier de Google, GA le 13 octobre 2026, contexte 1 048 576 tokens | AJOUT |
| Fairwind Program | TECHNOLOGIE | conditions | Candidature, vérification, usage cyber interne, MFA résistante au phishing, pas de revente | AJOUT |
| Frontier Safety Framework | DOCUMENT | rôle | Cadre de seuils critiques de Google DeepMind (cyber, biologie, R&D IA, manipulation) | AJOUT |
| Artificial Analysis | ORGANISATION | mesure Argon | 53 points sur l'Intelligence Index, hallucination 15 % (AA-Omniscience) | AJOUT |
| Koray Kavukcuoglu | PERSONNE | rôle | Google DeepMind, a présenté Gemini 4 Argon le 30 septembre 2026 | AJOUT |
