---
themes: [outils-plateformes, agents-codage-ia-skills, economie-marche]
source: SFEIR
---
# sfeir-gemini-4-hydrogen-github-copilot-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, à destination des équipes qui administrent ou budgètent **GitHub Copilot**. **(1)** Le **13 novembre 2026**, **GitHub** ouvre **Gemini 4 Hydrogen**, modèle rapide de la génération 4 de **Google** publié la veille, sur les plans Pro, Pro+, Max, Business et Enterprise ; pour Business et Enterprise, activé par défaut via la *model policy* sauf réglage contraire. **(2)** Le même jour, GitHub fixe au **14 décembre** le retrait de **six modèles** de Copilot : Gemini 3.8 Flash, Gemini 4 Argon, Claude Fable 5, Claude Haiku 4.5, Grok 4.6, Kimi K3. **(3)** Le prix : Hydrogen coûte **1,50 $ / 7,50 $** par million de tokens (entrée/sortie), soit **le double** du tarif promotionnel de 3.8 Flash ; un scénario de Data Studios recalculé aux prix de GitHub donne **+89 %** par session d'agent. **(4)** Les mesures, lues *« selon qui mesure »* : **Artificial Analysis** (51 points, devant Argon à 50) ; chiffres de Google (×2,5 en vitesse, 57 % sur Terminal-Bench 4.1). **(5)** Le retrait est **propre à Copilot** : l'API Gemini continue de servir 3.8 Flash, mais l'aligne sur le prix d'Hydrogen au 1er janvier 2027. Une section « ce qu'on ne sait pas encore » liste sélection automatique, fenêtre de contexte dans Copilot et absence de mesure indépendante dans le harnais Copilot.

## Titre Article

Gemini 4 Hydrogen arrive dans GitHub Copilot : ce que vos équipes doivent régler avant le 14 décembre

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/gemini-4-hydrogen-github-copilot/

## Keywords

Gemini 4 Hydrogen, Gemini 3.8 Flash, Gemini 4 Carbon, Gemini 4 Argon, GitHub Copilot, model policy, retrait de modèles, dépréciation, AI Credits, prix au token, cache, Artificial Analysis, Terminal-Bench, SWE-sweep, niveaux de réflexion, fenêtre de contexte, Gemini Enterprise Agent Platform, API Gemini, Claude Fable, Claude Haiku, Grok, Kimi K3, coût par tâche réussie, harnais, Google DeepMind

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article d'actualité opérationnelle à échéance (« avant le 14 décembre »), publié sur le site d'un cabinet. Public : administrateurs Copilot, CTO et leads dev, achats et contrôle de gestion, DSI.

**Style** : dense en tableaux (prix par modèle, modèles retirés et remplaçants) et en figures (frise du 12 novembre au 1er janvier 2027, carte de la famille Gemini au 15 novembre). Les citations des sources restent en anglais (*« Google's latest Flash model »*, *« our daily driver for agentic workflows »*). Conseils découpés par rôle.

**Position épistémique** : douze sources datées et consultées le 15 novembre. Les mesures sont explicitement réparties entre indépendantes (Artificial Analysis) et déclarées (Google, harnais Antigravity CLI, scores concurrents repris d'un classement public). La simulation de coût est qualifiée de scénario, avec la consigne de mesurer plutôt *« le coût par tâche réussie »*. L'article distingue soigneusement le périmètre Copilot de celui de l'API et d'Agent Platform.

## Pense-betes

- **Hydrogen dans Copilot** (13 novembre) : plans Pro, Pro+, Max, Business, Enterprise ; absent du plan gratuit et, au 15 novembre, de la sélection automatique (où 3.8 Flash est le seul Gemini). Disponible dans VS Code, Visual Studio, JetBrains, Xcode, Eclipse, Copilot CLI, coding agent, github.com, Mobile, Copilot SDK ; déploiement progressif.
- **Positionnement Google** (Koray Kavukcuoglu, 12 novembre) : Carbon et Argon pour le raisonnement long, Hydrogen pour exécuter vite, seul ou comme moteur d'exécution. Model card : *« adapted from Gemini 4 Carbon »*.
- **Mesures** : Artificial Analysis Intelligence Index v5.0.1 — Hydrogen 51 (high), 54 (xhigh), Argon 50. Google : ~2,5× plus rapide que 3.8 Flash ; Terminal-Bench 4.1 57 % (3.8 Flash 18,2 %, Claude Sonnet 5.5 63,9 %) ; SWE-sweep 13,5 % (Sonnet 5.5 3,1 %, GPT-6.1 Terra 5,8 %), harnais Antigravity CLI.
- **Caractéristiques** (Google) : texte, images, audio, vidéo ; 1 048 576 tokens partagés ; quatre niveaux de réflexion (low, medium, high par défaut, xhigh) ; GA sur Agent Platform, emplacement « eu » compris.
- **Prix Copilot** (AI Credits, 1 crédit = 0,01 $, depuis juin 2026) : Hydrogen 1,50 / 0,075 (cache) / 7,50 $ ; 3.8 Flash 0,75 / 0,075 / 3,75 $ (promo) ; Carbon 2 / 0,10 / 10 $, puis 4 / 0,20 / 20 $ au 1er décembre.
- **Scénario Data Studios** recalculé : 0,5265 $ contre 0,279 $ par session (+89 %) ; siège Business (19 $ de crédits) ≈ 36 sessions au lieu de 68.
- **Retraits du 14 décembre** et remplaçants : 3.8 Flash → Hydrogen ; Argon → Carbon ; Fable 5 → Fable 5.2 ; Haiku 4.5 → Haiku 5.5 ; Grok 4.6 → Grok 4.7 ; Kimi K3 → à annoncer.
- **Hors Copilot** : pas d'arrêt annoncé pour 3.8 Flash dans l'API ; Agent Platform le garde au moins jusqu'au 2 septembre 2027. Au 1er janvier 2027, l'API facture 3.8 Flash au prix d'Hydrogen, cache à 0,15 $.
- **Par rôle** : administrateur — ouvrir la model policy, chercher les configurations figeant un modèle retiré ; CTO — tester sur une vingtaine de tâches réelles ; achats — revoir l'enveloppe de crédits ; DSI — *un harnais que vous opérez vous-même*.

## RésuméDe400mots

Le 13 novembre 2026, GitHub a rendu Gemini 4 Hydrogen disponible dans GitHub Copilot et annoncé, le même jour, le retrait de six modèles au 14 décembre. SFEIR détaille ce que les équipes qui administrent ou budgètent Copilot doivent vérifier avant cette échéance.

Hydrogen est le modèle rapide de la génération 4 de Google, présenté le 12 novembre par Koray Kavukcuoglu comme le modèle quotidien des workflows agentiques, tandis que Gemini 4 Carbon et Argon traitent le raisonnement long. La fiche technique de Google DeepMind le dit adapté de Carbon. Dans Copilot, il est ouvert aux plans payants et, pour Business et Enterprise, activé par défaut par la politique de modèles sauf si un administrateur a coupé cette activation. Il n'est pas encore dans la sélection automatique.

L'article sépare les mesures selon leur origine. Artificial Analysis lui attribue 51 points sur son index, devant Argon. Google annonce des tâches terminées 2,5 fois plus vite que Gemini 3.8 Flash et 57 % sur Terminal-Bench 4.1, avec son propre harnais. Aucune mesure indépendante dans Copilot n'est publiée.

Le prix change la donne : Hydrogen est facturé 1,50 dollar en entrée et 7,50 dollars en sortie par million de tokens, le double du tarif promotionnel de 3.8 Flash, la lecture en cache restant identique. Un scénario de session d'agent publié par Data Studios, recalculé aux prix de GitHub, coûte 89 % de plus ; un siège Business couvrirait environ 36 sessions au lieu de 68. L'article recommande de mesurer le coût par tâche réussie sur ses propres dépôts.

Les six modèles retirés de Copilot le 14 décembre sont Gemini 3.8 Flash, Gemini 4 Argon, Claude Fable 5, Claude Haiku 4.5, Grok 4.6 et Kimi K3, chacun avec un remplaçant proposé, sauf Kimi K3. Ce retrait ne vaut que pour Copilot : l'API Gemini continue de servir 3.8 Flash, mais l'aligne sur le prix d'Hydrogen au 1er janvier 2027.

Les conseils sont donnés par rôle : vérifier la politique de modèles et les configurations qui nomment un modèle retiré, comparer les deux modèles sur une vingtaine de tâches réelles, revoir l'enveloppe de crédits, et, pour la DSI, opérer son propre harnais face à des fournisseurs capables de retirer six modèles avec un mois de préavis. Restent inconnus : la sélection automatique, la fenêtre de contexte appliquée par Copilot et le remplaçant de Kimi K3.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Google | ORGANISATION | publie | Gemini 4 Hydrogen | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| GitHub Copilot | TECHNOLOGIE | utilise | Gemini 4 Hydrogen | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Gemini 4 Hydrogen | TECHNOLOGIE | remplace | Gemini 3.8 Flash | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Gemini 4 Hydrogen | TECHNOLOGIE | est_variante_de | Gemini 4 Carbon | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Gemini 4 Hydrogen | TECHNOLOGIE | fait_partie_de | Gemini | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| Koray Kavukcuoglu | PERSONNE | travaille_chez | Google DeepMind | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | Gemini 4 Hydrogen 51 points (high), 54 (xhigh), Argon 50 sur l'Intelligence Index v5.0.1 | MESURE | 0.88 | STATIQUE | déclaré_article |
| Gemini 4 Hydrogen | TECHNOLOGIE | surpasse | Gemini 4 Argon | TECHNOLOGIE | 0.8 | STATIQUE | déclaré_article |
| Google | ORGANISATION | mesure | Hydrogen 57 % sur Terminal-Bench 4.1 contre 18,2 % pour 3.8 Flash | MESURE | 0.85 | STATIQUE | déclaré_article |
| Gemini 4 Hydrogen | TECHNOLOGIE | mesure | 1,50 $ / 7,50 $ par million de tokens dans Copilot, le double de 3.8 Flash | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | +89 % par session d'agent sur Hydrogen (scénario Data Studios recalculé) | MESURE | 0.82 | STATIQUE | déclaré_article |
| GitHub | ORGANISATION | publie | retrait de six modèles de Copilot le 14 décembre 2026 | EVENEMENT | 0.93 | STATIQUE | déclaré_article |
| Claude Fable | TECHNOLOGIE | fait_partie_de | GitHub Copilot | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | mesurer le coût par tâche réussie sur ses propres dépôts plutôt que le prix au token | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | opérer son propre harnais : politiques de modèles, budgets, jeu de tâches, configurations sans nom de modèle figé | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le retrait de Gemini 3.8 Flash ne vaut que pour Copilot, l'API Gemini continuant de le servir | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Gemini 4 Hydrogen | TECHNOLOGIE | caractéristiques | Modèle rapide génération 4, GA le 12/11/2026, 1 048 576 tokens, 4 niveaux de réflexion | AJOUT |
| Gemini 3.8 Flash | TECHNOLOGIE | statut | Retiré de Copilot le 14/12/2026 ; maintenu dans l'API, au prix d'Hydrogen au 1/1/2027 | AJOUT |
| GitHub Copilot | TECHNOLOGIE | facturation | AI Credits au token depuis juin 2026 (1 crédit = 0,01 $) | AJOUT |
| retrait de six modèles de Copilot le 14 décembre 2026 | EVENEMENT | périmètre | Gemini 3.8 Flash, Gemini 4 Argon, Claude Fable 5, Claude Haiku 4.5, Grok 4.6, Kimi K3 | AJOUT |
| Koray Kavukcuoglu | PERSONNE | rôle | SVP Google DeepMind, Chief AI Architect de Google | AJOUT |
| Artificial Analysis | ORGANISATION | secteur | Évaluation indépendante de modèles | AJOUT |
