---
themes: [produits-services, qualite-securite, outils-plateformes]
source: SFEIR
---
# sfeir-microsoft-autopilot-openclaw-ignite-2026-11-18

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **18 novembre 2026** (~16 000 signes, treize sources : billets de Satya Nadella, Jared Spataro et Omar Shahine, posts X, blog d'OpenClaw, Microsoft Learn, presse). Il traite de **Microsoft Autopilot**, agent personnel autonome ouvert aux clients du programme **Frontier** à l'ouverture d'**Ignite** le **17 novembre 2026**. Trois apports. **(A)** Les engagements de contrôle cités du billet de Spataro : un **Entra Agent ID** et un responsable nommé par agent, **Work IQ** dans les permissions existantes, un agent qui *« can check with you before key actions »*, des connexions journalisées sous son nom. **(B)** Une chronologie des déclarations publiques (31 mars, 2 juin, 25 septembre, 15 et 17 novembre 2026) établissant qu'Autopilot repose sur **OpenClaw** : *« We are building Autopilot on @openclaw »* (Shahine), alors qu'aucun des trois billets d'Ignite ne nomme le runtime. **(C)** Ce que Microsoft ajoute autour du runtime (identité, contexte, hébergement, gouvernance Agent 365, facturation à l'usage) et ses contributions au projet, puis six points à vérifier par la DSI avant un pilote, dont le réglage **flex routing** hors EU Data Boundary. Rejoint l'analyse du harnais comme composant de [[trivedy-langchain-anatomy-agent-harness-2026-03-10]].

## Titre Article

Microsoft Autopilot tourne sur OpenClaw, et Ignite ne l'a pas dit

## Date

2026-11-18

## URL

https://www.sfeir.com/articles/microsoft-autopilot-openclaw-ignite-2026/

## Keywords

Microsoft Autopilot, OpenClaw, Ignite 2026, agent personnel autonome, Microsoft 365, Copilot, programme Frontier, Entra Agent ID, Work IQ, Agent 365, Scout, OpenClaw Foundation, runtime open source, harness engineering, facturation à l'usage, flex routing, EU Data Boundary, injection de consignes, permissions héritées, gouvernance des agents, DSI, SFEIR

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé publié sur sfeir.com, site éditorial du groupe.

## Ton

Article d'analyse produit en français, destiné aux DSI. Le texte procède par citations en anglais tirées des billets de Microsoft et des posts publics, chacune sourcée, et insiste sur la lettre des engagements (« Le verbe compte : l'agent *peut* demander »). Le lien entre Autopilot et OpenClaw est établi par un tableau chronologique de déclarations signées par les intéressés, l'article précisant que ce lien *« ne vient pas d'une fuite »*. Le registre reste factuel sur les zones d'ombre, regroupées en fin d'article (disponibilité en UE, prix, état par défaut, part exacte d'OpenClaw). La section opérationnelle prend la forme d'une checklist de pilote. Un paragraphe d'interprétation, appuyé sur Patrick Moorhead (*« The model is now a component »*), étend le raisonnement au runtime. Renvois internes vers les articles SFEIR sur la sécurité et le shadow AI d'OpenClaw.

## Pense-betes

- **Autopilot** : agent personnel autonome *« personal to you, always on »*, ouvert le **17 novembre 2026** aux clients **Frontier** ; présent dans Teams, Outlook, documents, mentionné comme un collègue. Nadella : *« keeps moving your work forward 24×7 »*. À ne pas confondre avec **Windows Autopilot**.
- **Quatre engagements (Spataro)** : Entra Agent ID + responsable nommé ; Work IQ *« within existing permissions »* ; l'agent *« can check with you before key actions »* (pas « toujours ») ; l'IT peut le borner et le bloquer, journaux sous son propre nom.
- **Shahine** : identité, mémoire, espace de travail et *« remote computer »* propres ; exemple de **40 brouillons** Teams non envoyés avant relecture ; *« Preparing a reply and sending it are different things. »* Accès : Frontier + licence Copilot + facturation à l'usage.
- **Lien OpenClaw** (OpenClaw : créé fin 2025 par **Peter Steinberger**, MIT, confié en février 2026 à l'OpenClaw Foundation) : 31 mars, Shahine quitte Word pour *« Bringing OpenClaw + personal agents to Microsoft 365 »* ; 2 juin, Scout à Build ; 25 septembre, Autopilot (ex-Scout) et *« We are building Autopilot on @openclaw »*, Steinberger : travail commun depuis mars ; 17 novembre, OpenClaw confirme le déploiement.
- **Autour du runtime** : identité, contexte (Work IQ, **19,5 exaoctets**, 90 milliards de courriels), hébergement dans le tenant, gouvernance **Agent 365** (*« over 50 million agents »*), facturation à l'usage.
- **Contributions Microsoft à OpenClaw** : plugin de conformité de politique, sandbox Windows, correctif d'ordonnanceur de la Gateway, garde anti-boucle après compaction, masquage des secrets, compagnon Windows, Azure OpenAI. Règle de Shahine : ne pas relancer une commande au résultat inconnu.
- **Lecture proposée** : le harnais devient un composant commun open source ; la valeur se déplace vers identité, contexte, gouvernance, facture (Moorhead : *« cost and context »*).
- **Checklist DSI** : droits hérités (nettoyer les partages excessifs avant), actions soumises à validation écrites, injection de consignes, plafond budgétaire par agent, **flex routing** (activé par défaut sur les tenants éligibles créés après le 25 mars 2026), périmètre du pilote.
- **Inconnues** : pays de la préversion, grille de prix, état par défaut, part exacte d'OpenClaw.

## RésuméDe400mots

Le 17 novembre 2026, à l'ouverture d'Ignite, Microsoft commence à déployer Autopilot auprès des clients de son programme Frontier. L'article de SFEIR AI décrit ce produit, établit le logiciel qui le fait tourner et liste ce qu'une DSI doit vérifier avant un pilote.

Autopilot est un agent personnel autonome qui travaille en continu pour un collaborateur, dans Teams, Outlook et les documents. Le billet de Jared Spataro formule quatre engagements : chaque agent possède un Entra Agent ID et un responsable nommé, accède au contexte via Work IQ dans les permissions existantes, peut consulter son utilisateur avant une action importante, et voit ses connexions et actions journalisées sous son propre nom. L'article souligne que Microsoft écrit « peut » et non « doit ». Omar Shahine, CVP du produit, ajoute qu'Autopilot dispose d'une identité, d'une mémoire, d'un espace de travail et d'un ordinateur distant, et cite 40 brouillons préparés pendant son absence, restés non envoyés jusqu'à sa relecture.

Aucun des trois billets d'Ignite ne nomme le runtime. L'article reconstitue pourtant, par des déclarations publiques datées, qu'Autopilot repose sur OpenClaw, l'agent open source créé par Peter Steinberger et confié à l'OpenClaw Foundation : annonce du nouveau poste de Shahine en mars, présentation de Scout à Build en juin, puis en septembre « We are building Autopilot on @openclaw », confirmé par Steinberger et par le blog d'OpenClaw. Microsoft ne publie pas de schéma d'architecture.

Les apports revendiqués par Microsoft sont extérieurs à la boucle d'agent : identité Entra, contexte Work IQ, hébergement dans le tenant, gouvernance Agent 365, facturation à l'usage. Dans l'autre sens, des ingénieurs de Microsoft ont contribué à OpenClaw : plugin de conformité de politique, sandbox Windows, correctifs de fiabilité, masquage des secrets. L'article en tire une lecture : le harnais d'agent devient un composant commun et la valeur se déplace vers ce qui l'entoure.

La checklist proposée aux DSI porte sur six points : les droits hérités, à nettoyer avant le pilote ; les actions qui restent des brouillons ; l'injection de consignes via courriels et invitations ; le budget, faute de grille publiée ; la localisation des données, le réglage flex routing de Copilot pouvant faire sortir l'inférence de l'EU Data Boundary ; et un périmètre de pilote restreint. L'article situe Autopilot dans une vague d'agents always-on (Meta, Anthropic, Google) et termine sur les inconnues : disponibilité en UE, prix, état par défaut, part exacte d'OpenClaw.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Microsoft Autopilot tourne sur OpenClaw, et Ignite ne l'a pas dit | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Microsoft | ORGANISATION | publie | Microsoft Autopilot | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Microsoft Autopilot | TECHNOLOGIE | utilise | OpenClaw | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Microsoft Autopilot | TECHNOLOGIE | remplace | Scout | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Omar Shahine | PERSONNE | dirige | Microsoft Autopilot | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Omar Shahine | PERSONNE | travaille_chez | Microsoft | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Peter Steinberger | PERSONNE | a_créé | OpenClaw | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Microsoft | ORGANISATION | collabore_avec | OpenClaw Foundation | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| Microsoft Autopilot | TECHNOLOGIE | utilise | Entra Agent ID | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Microsoft Autopilot | TECHNOLOGIE | utilise | Work IQ | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Agent 365 | TECHNOLOGIE | permet | gouvernance des agents | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Jared Spataro | PERSONNE | affirme_que | Autopilot peut consulter l'utilisateur avant les actions importantes | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Satya Nadella | PERSONNE | affirme_que | Work IQ est la base de données la plus importante de toute organisation | AFFIRMATION | 0.84 | STATIQUE | déclaré_article |
| Patrick Moorhead | PERSONNE | affirme_que | le modèle est désormais un composant | CITATION | 0.84 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la valeur se déplace du runtime d'agent vers identité, contexte, gouvernance et facturation | AFFIRMATION | 0.84 | ATEMPOREL | déclaré_article |
| flex routing | CONCEPT | permet | inférence Copilot hors EU Data Boundary | CONCEPT | 0.84 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | nettoyer les partages excessifs avant un pilote Autopilot | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | fixer un plafond budgétaire par agent | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle (groupe SFEIR) | AJOUT |
| Microsoft Autopilot | TECHNOLOGIE | catégorie | Agent personnel autonome Microsoft 365, préversion Frontier depuis le 17 novembre 2026 | AJOUT |
| OpenClaw | TECHNOLOGIE | licence | Agent personnel open source (MIT), runtime d'Autopilot | AJOUT |
| OpenClaw Foundation | ORGANISATION | rôle | Fondation gardienne d'OpenClaw depuis février 2026 | AJOUT |
| Omar Shahine | PERSONNE | rôle | CVP Microsoft chargé d'Autopilot, ex-responsable de l'équipe Word | AJOUT |
| Jared Spataro | PERSONNE | rôle | Directeur marketing de l'IA au travail chez Microsoft | AJOUT |
| Work IQ | TECHNOLOGIE | rôle | Couche d'accès au contenu Microsoft 365 pour les agents | AJOUT |
| Entra Agent ID | TECHNOLOGIE | rôle | Identité d'annuaire propre à chaque agent | AJOUT |
| flex routing | CONCEPT | défaut | Activé sur les tenants UE/AELE éligibles créés après le 25 mars 2026 | AJOUT |
