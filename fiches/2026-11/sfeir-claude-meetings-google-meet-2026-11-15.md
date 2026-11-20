---
themes: [produits-services, politique-regulation]
source: SFEIR
---
# sfeir-claude-meetings-google-meet-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026** (mis à jour le 18 novembre), consacré à **Claude Meetings**, présenté par **Anthropic** le **10 novembre 2026** et déployé en bêta sur les plans **Team** et **Enterprise**. Public déclaré : DSI, DPO, responsables de l'environnement de travail. **(1)** Le fonctionnement : Claude rejoint un appel **Google Meet** comme participant visible, prend des notes, relève les actions, répond par écrit dans le chat de l'appel et construit en direct documents, whiteboards et autres artefacts ; il interroge les outils connectés d'un participant avec son accord. **(2)** Les données : transcription, résumé et descriptions de l'écran partagé conservés, pas d'audio ; une page par réunion dans claude.ai. **(3)** Une divergence relevée entre la page de lancement (invités externes exclus par défaut) et le centre d'aide (*« Internal meetings only »* par défaut sur Enterprise, *« allowed »* sur Team). **(4)** Cinq réglages à décider par écrit avant activation : information des participants (RGPD), invités externes, connecteurs, conservation (données stockées aux États-Unis), contrôles laissés aux participants. L'article rapproche le lancement de [[sfeir-chatgpt-wallet-openai-paiement-2026-11-15]] : l'IA agit dans un système conçu pour des humains.

## Titre Article

Claude Meetings : Claude entre dans vos réunions Google Meet comme participant

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/claude-meetings-agent-reunions-google-meet/

## Keywords

Claude Meetings, Anthropic, Claude, Google Meet, agent en réunion, prise de notes, transcription, artefacts, whiteboard, connecteurs, invités externes, consentement, RGPD, DPO, analyse d'impact, transfert hors UE, rétention des données, Team, Enterprise, rôles Owner, bêta, zero data retention, HIPAA, CMEK, AgentCore, ChatGPT Wallet

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article d'actualité orienté décision de gouvernance, publié sur le site d'un cabinet. Public : DSI, DPO, responsables de l'environnement de travail, avec une attention explicite au cadre français et européen.

**Style** : descriptif puis prescriptif — d'abord ce que fait Claude pendant et après l'appel, puis les plans, exclusions et tarifs, enfin « cinq points [qui] méritent une décision écrite ». Le texte cite les intitulés exacts des réglages en anglais (« Meetings with external guests », « Members' connectors in meetings »).

**Position épistémique** : huit sources datées, majoritairement de la documentation d'Anthropic (page produit, centre d'aide, notes de version, centre de confidentialité), plus TechCrunch et le blog AWS. L'article relève une divergence entre deux documents d'Anthropic sur le réglage par défaut des invités externes. Section « limites » : bêta, aucune mesure de qualité publiée, langues de transcription non listées, trace écrite des écrans partagés. Renvoi final à l'offre FDE Claude du cabinet.

## Pense-betes

- **Annonce** : 10 novembre 2026 (TechCrunch) ; page produit du 12 ; bêta Team et Enterprise ; Google Meet seulement, autres outils « bientôt ».
- **Pendant l'appel** : participant visible qui signale sa présence dans le chat ; notes, actions, réponses écrites visibles de toute la réunion ; artefacts (documents, whiteboards, slides). Connecteurs d'un participant : accord demandé la première fois, valable ensuite ; pour une demande orale, confirmation de qui parle à chaque fois.
- **Après l'appel** : transcription, résumé, descriptions de l'écran partagé ; **pas d'audio**. Page de réunion dans claude.ai, consultable et partageable par les membres invités.
- **Invités externes** : divergence documentaire — lancement : exclus par défaut ; centre d'aide : « Internal meetings only » par défaut sur Enterprise, « allowed » sur Team. Si exclus, Claude quitte l'appel à l'arrivée d'un externe, y compris le robot de notes d'une autre entreprise.
- **Activation** : Team activé par défaut ; Enterprise désactivé par défaut, activable par rôles personnalisés. Réglages réservés à Owner / Primary Owner ; le rôle Admin intégré ne peut pas ouvrir la page.
- **Exclusions bêta** : organisations en zero data retention, HIPAA ou CMEK.
- **Tarifs** : notes et transcriptions gratuites ; réponses via outil connecté décomptées de l'usage de la personne qui l'a connecté ; artefacts gratuits jusqu'au 10 février 2027.
- **Cinq décisions écrites** : information des participants (RGPD, responsabilité laissée au client) ; invités externes ; connecteurs (réglage global « Members' connectors in meetings ») ; conservation (stockage aux États-Unis, rétention personnalisée ≥ 30 jours sur Enterprise seulement, couverture des pages de réunion non précisée) ; contrôles utilisateurs (participation automatique non imposable, pause, retrait, 8 h maximum).
- **Partenaires annoncés** : Gong, Attention, Granola, Fireflies.ai, Otter, Plaud (envoi des transcriptions, sans date).
- **Cadre** : citation d'AWS (AgentCore) — *« what is this agent allowed to do when no one is watching it act? »*

## RésuméDe400mots

Le 10 novembre 2026, Anthropic a présenté Claude Meetings, déployé en bêta sur les plans Team et Enterprise. Claude rejoint un appel Google Meet comme participant visible et travaille pendant la réunion. SFEIR décrit le produit et les décisions qu'il impose aux DSI, DPO et responsables de l'environnement de travail.

Claude entre dans l'appel quand quelqu'un l'ajoute, ou automatiquement si l'utilisateur l'a réglé, et signale sa présence dans le chat. Il prend des notes, relève les actions, répond par écrit aux questions posées à l'oral ou dans le chat, et construit en direct des documents, whiteboards ou slides. Il peut interroger les outils connectés d'un participant, avec son accord donné une fois pour toutes. Après l'appel, Anthropic conserve la transcription, le résumé et des descriptions de l'écran partagé, sans l'audio ; chaque réunion dispose d'une page partageable en interne.

Sur les invités externes, l'article relève une divergence : la page de lancement les présente comme exclus par défaut, alors que le centre d'aide indique ce réglage par défaut sur Enterprise seulement, les externes étant admis par défaut sur Team. Quand ils sont admis, leurs propos figurent dans la transcription. Anthropic laisse au client la responsabilité du consentement.

La bêta est activée par défaut sur Team et désactivée sur Enterprise ; seuls les rôles Owner peuvent la régler. Les organisations en zero data retention, HIPAA ou avec clés gérées par le client en sont exclues. Notes et transcriptions sont gratuites ; les réponses passant par un outil connecté sont décomptées de l'usage de son propriétaire ; les artefacts sont gratuits jusqu'en février 2027.

L'article liste cinq points à trancher par écrit avant activation : l'information des participants au titre du RGPD, l'admission des invités externes, l'usage des connecteurs dont les réponses s'affichent devant tous, la conservation des données, stockées aux États-Unis et donc à documenter comme transfert hors Union européenne, et les contrôles laissés aux participants.

Il rapproche ce lancement de ChatGPT Wallet, publié trois jours plus tard : dans les deux cas, l'IA agit dans un système conçu pour des humains, et les règles d'accès, de consentement et de conservation se décident avant le déploiement. Les limites signalées : produit en bêta, aucune mesure de qualité publiée, langues de transcription non listées, trace écrite laissée par les écrans partagés.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Anthropic | ORGANISATION | publie | Claude Meetings | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Claude Meetings | TECHNOLOGIE | fait_partie_de | Claude | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Claude Meetings | TECHNOLOGIE | utilise | Google Meet | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Claude Meetings | TECHNOLOGIE | permet | transcription et notes de réunion | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Meetings | TECHNOLOGIE | permet | artefacts construits en réunion | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Claude Meetings | TECHNOLOGIE | utilise | connecteurs | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Meetings | TECHNOLOGIE | s_applique_à | plans Team et Enterprise | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la page de lancement et le centre d'aide divergent sur le réglage par défaut des invités externes | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la transcription d'une réunion est un traitement de données personnelles au sens du RGPD | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Claude Meetings | TECHNOLOGIE | observé_dans | RGPD | DOCUMENT | 0.75 | DYNAMIQUE | inféré |
| SFEIR | ORGANISATION | recommande | décider par écrit information des participants, invités externes, connecteurs, conservation et contrôles avant activation | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Claude Meetings | TECHNOLOGIE | concurrence | Microsoft | ORGANISATION | 0.75 | DYNAMIQUE | déclaré_article |
| Claude Meetings | TECHNOLOGIE | converge_avec | ChatGPT Wallet | TECHNOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| Amazon Bedrock AgentCore | TECHNOLOGIE | référence | « what is this agent allowed to do when no one is watching it act? » | CITATION | 0.8 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | collabore_avec | Granola | ORGANISATION | 0.75 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Claude Meetings | TECHNOLOGIE | lancement | Annoncé le 10 novembre 2026, bêta Team et Enterprise, Google Meet uniquement | AJOUT |
| Claude Meetings | TECHNOLOGIE | données conservées | Transcription, résumé, descriptions de l'écran partagé ; pas d'audio | AJOUT |
| Claude Meetings | TECHNOLOGIE | exclusions bêta | Organisations en zero data retention, HIPAA ou CMEK | AJOUT |
| RGPD | DOCUMENT | portée | Transcription de réunion = traitement de données personnelles | AJOUT |
