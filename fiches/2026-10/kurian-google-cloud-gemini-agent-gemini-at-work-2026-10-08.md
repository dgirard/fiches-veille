---
themes: [produits-services, outils-plateformes, architecture-construction, qualite-securite]
source: "Google Cloud"
---
# kurian-google-cloud-gemini-agent-gemini-at-work-2026-10-08

## Veille

Billet du blog Google Cloud signé de **Thomas Kurian** (CEO de Google Cloud), publié le **8 octobre 2026**, adapté de sa keynote à **Gemini at Work 2026** ; texte long (~4 500 mots) dont plus de la moitié est un catalogue de témoignages clients. Il annonce le **Gemini agent**, « agent universel pour le travail » : un seul agent et une seule API pour répondre, produire du travail de bureau, créer images et médias, écrire et exécuter du code.

**(1)** Architecture : agent unique, accessible depuis tout appareil et canal (CLI, Workspace, Microsoft 365, Slack, mode *headless*), exécution persistante dans le cloud avec un seul graphe de personnalisation, sous-agents temporaires et **agents collègues** dotés d'une identité propre (adresse `@agents.company.com`, stockage, compte Workspace), choix du modèle découplé de l'agent (famille **Gemini** et modèles **Claude** d'**Anthropic** aujourd'hui, autres modèles privés et ouverts à venir). **(2)** Briques : registre d'outils (dont tout serveur **MCP**), registre de skills partagé, quatre mémoires (session, sémantique, procédurale, épisodique). **(3)** Workspace : assistance personnelle, délégation proactive, agent membre de l'équipe. **(4)** Données : skills pour ingénieurs data/ML et rapports opérationnels pour métiers, appuyés sur Knowledge Catalog, Smart Storage et Borderless Lakehouse ; *Bloomberg Media* annonce +63 % de précision SQL. **(5)** Spécialisations en préversion pour la **finance** (plus de 50 skills, sources FactSet, LSEG, S&P Global) et le **droit** (permissions de matter et murs éthiques hérités de NetDocuments et iManage). **(6)** Gouvernance : identité attestée par agent, autorisation par OAuth, journal d'audit attribué à l'agent, **Agent Sandbox** et **Agent Gateway** (pare-feu réseau d'IA appliquant une politique écrite une fois). **(7)** Coûts : orchestration multi-modèles, routage intelligent, plafonds de dépense en temps réel par projet ; prix par jeton en baisse de **98 %** depuis 2024 ; TPU 8i à **80 %** de meilleur rapport prix-performance ; modèles Argon, Flash, Omni, Gemma. Le texte ne donne ni tarifs, ni disponibilité générale, ni mesures indépendantes ; les chiffres clients sont déclaratifs.

Rapproche l'annonce de [[janakiram-agent-platform-portability-contract-2026-07-20]] sur la portabilité des plateformes d'agents.

## Titre Article

Welcome to Gemini at Work 2026: Introducing the Gemini agent

## Date

2026-10-08

## URL

https://cloud.google.com/blog/products/ai-machine-learning/welcome-to-gemini-at-work-2026

## Keywords

Gemini agent, Gemini Enterprise, Google Cloud, agent universel, agents collègues, sous-agents, multi-agents, orchestration multi-modèles, routage intelligent, plafonds de dépense, Agent Gateway, Agent Sandbox, identité des agents, MCP, registre de skills, registre d'outils, mémoire des agents, Knowledge Catalog, Smart Storage, Borderless Lakehouse, Google Workspace, services financiers, juridique, TPU 8i, Claude, Gemma

## Authors

Thomas Kurian — CEO de Google Cloud ; billet du blog Google Cloud adapté de sa keynote.

## Ton

Profil : discours de keynote d'éditeur, adressé aux décideurs et DSI. Structure en annonces numérotées, thèse posée d'emblée (« le travail commence dans la fenêtre de prompt »), puis déclinaison par domaine (agent, Workspace, données, industries, gouvernance, coûts, infrastructure) et long inventaire de clients par région. Registre affirmatif et chiffré, résultats clients rapportés sans méthode. Les engagements finaux (supprimer la friction, la complexité, garder la propriété des données) reprennent l'argumentaire de plateforme intégrée.

## Pense-betes

- **Quoi** : le **Gemini agent**, agent unique pour questions, travail de connaissance, médias et code, avec une API unique ; gouvernance et contrôle des coûts intégrés.
- **Agents collègues** : rôle persistant, identité propre (e-mail, calendrier, Drive, annuaire), ne voient que ce qu'on partage ; apparaissent sous leur nom dans l'historique des versions.
- **Mémoire** : session, sémantique, procédurale (skills que l'agent écrit lui-même), épisodique.
- **Modèle découplé de l'agent** : Gemini + **Claude** aujourd'hui ; argument : le meilleur modèle change tous les quelques mois, contexte, skills et données restent.
- **Outils et skills** : registres d'entreprise ; connexion à tout serveur **MCP** interne ou externe ; connecteurs Salesforce, ServiceNow, Jira, Snowflake, Databricks…
- **Gouvernance** : quatre questions (qui est l'agent, que peut-il faire, qu'a-t-il fait, que ne doit-il jamais toucher) → identité, autorisations OAuth, audit, **Agent Gateway** ; l'identité suit l'agent jusque dans les machines virtuelles d'exécution.
- **Coûts** : plafond de dépense par projet, agent mis en pause à l'atteinte, reprise en un clic ; routage entre modèles.
- **Chiffres clients déclarés** : Bradesco revue de documents 1 h → 5 min ; Snap diagnostic 30 min → 30 s ; Commerzbank 20 h → 1 h ; SOMPO plus de 10 000 agents ; armées américaines, 3 M d'utilisateurs, plus de 100 000 agents.
- ⚠️ **Portée** : annonce de keynote ; préversion pour finance et droit, « bientôt » pour public, santé, distribution ; aucune date de disponibilité générale ni grille tarifaire.

## RésuméDe400mots

Le 8 octobre 2026, Thomas Kurian, CEO de Google Cloud, présente à Gemini at Work 2026 le Gemini agent, décrit comme un agent universel pour le travail. Il répond aux questions, traite le travail de connaissance, crée images et médias, écrit et exécute du code, depuis une seule interface et une seule API. L'utilisateur lui confie des objectifs plutôt que des instructions et revient à un résultat terminé. Kurian s'appuie sur des chiffres d'adoption : près de 500 clients ont chacun traité plus d'un billion de jetons sur l'année, près de 80 % des clients utilisent les produits d'IA de Google Cloud et près de 90 % du Fortune 100 utilisent Gemini Enterprise.

L'architecture repose sur cinq principes. L'agent est unifié : il converse, travaille de façon autonome, planifie des tâches ou réagit à des événements. Il est accessible partout, y compris Microsoft 365 et Slack, et peut fonctionner sans interface. Son exécution est persistante dans le cloud, avec une mémoire unique quel que soit le canal. Il orchestre des sous-agents temporaires et des agents collègues dotés d'une identité et d'un stockage propres. Enfin, le modèle est un choix distinct de l'agent : Gemini choisit pour chaque tâche entre les modèles Gemini et les modèles Claude d'Anthropic, d'autres modèles devant suivre.

Trois briques le rendent utile : un registre d'outils, avec connexion à tout serveur MCP ; un registre de skills, global, départemental ou personnel ; et quatre mémoires (session, sémantique, procédurale, épisodique). Dans Workspace, Gemini opère dans Gmail, Drive, Docs, Slides, Sheets, Chat et Calendar, en assistant personnel, en délégation proactive ou en agent membre de l'équipe avec son propre compte.

Côté données, de nouvelles skills servent les ingénieurs data et ML (code PySpark, notebooks, entraînement, correction de pipelines) et les métiers (rapports opérationnels enregistrés, exécutables sans coût de jetons). Elles s'appuient sur le Knowledge Catalog, qui définit une fois les termes métier, sur Smart Storage, qui enrichit les données non structurées en place, et sur le Borderless Lakehouse, qui interroge S3, Azure et des tables Iceberg sans copie. Bloomberg Media rapporte un gain de 63 % de précision des requêtes SQL. Des spécialisations existent en préversion pour les services financiers et le droit, avec héritage des permissions et des murs éthiques des plateformes documentaires.

La gouvernance est ramenée à quatre questions : identité, permissions, traçabilité, et ce que l'agent ne doit jamais toucher. Chaque agent a une identité attestée, des droits minimaux, un journal d'audit à son nom, un bac à sable réseau et un passage obligé par Agent Gateway, pare-feu qui applique les politiques de l'organisation. Pour les coûts, Google propose l'orchestration multi-modèles, le routage intelligent et des plafonds de dépense par projet. Il cite une baisse de 98 % du prix par jeton depuis 2024 et un gain de 80 % de rapport prix-performance du TPU 8i.

Le reste du billet recense des déploiements par région (Europe, Asie-Pacifique, Amérique latine, Amérique du Nord) et trois engagements : retirer la friction, supprimer la complexité par une pile intégrée, garder les données chez le client.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Google Cloud | ORGANISATION | publie | Gemini agent | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Thomas Kurian | PERSONNE | dirige | Google Cloud | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Gemini agent | TECHNOLOGIE | utilise | Gemini | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Gemini agent | TECHNOLOGIE | utilise | Claude | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | collabore_avec | Google Cloud | ORGANISATION | 0.80 | DYNAMIQUE | inféré |
| Gemini agent | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Gemini agent | TECHNOLOGIE | utilise | Agent Gateway | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Gemini agent | TECHNOLOGIE | utilise | Agent Sandbox | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Gemini agent | TECHNOLOGIE | utilise | Knowledge Catalog | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Gemini agent | TECHNOLOGIE | s_applique_à | Google Workspace | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Agent Gateway | TECHNOLOGIE | résout | contrôle de ce que les agents ne doivent jamais toucher | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Agent collègue | CONCEPT | fait_partie_de | Gemini agent | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Gemini agent | TECHNOLOGIE | réduit | coût des agents par routage entre modèles et plafonds de dépense | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Google Cloud | ORGANISATION | mesure | baisse de 98 % du prix par jeton depuis 2024 | MESURE | 0.90 | STATIQUE | déclaré_article |
| TPU 8i | TECHNOLOGIE | améliore | rapport prix-performance de 80 % par rapport à la génération précédente | MESURE | 0.90 | STATIQUE | déclaré_article |
| Knowledge Catalog | TECHNOLOGIE | améliore | précision SQL de Bloomberg Media de 63 % | MESURE | 0.90 | STATIQUE | déclaré_article |
| Google Cloud | ORGANISATION | affirme_que | le meilleur modèle change tous les quelques mois, d'où le découplage agent/modèle | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Google Cloud | ORGANISATION | collabore_avec | Accenture | ORGANISATION | 0.88 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Gemini agent | TECHNOLOGIE | catégorie | Agent universel de travail de Google Cloud, annoncé le 8 octobre 2026 | AJOUT |
| Google Cloud | ORGANISATION | secteur | Cloud et IA d'entreprise (Alphabet) | AJOUT |
| Thomas Kurian | PERSONNE | rôle | CEO de Google Cloud | AJOUT |
| Gemini | TECHNOLOGIE | catégorie | Famille de modèles de Google | AJOUT |
| Claude | TECHNOLOGIE | catégorie | Modèles d'Anthropic orchestrables par le Gemini agent | AJOUT |
| Anthropic | ORGANISATION | secteur | Éditeur des modèles Claude | AJOUT |
| Model Context Protocol | TECHNOLOGIE | catégorie | Standard de connexion d'outils pris en charge par le Gemini agent | AJOUT |
| Agent Gateway | TECHNOLOGIE | catégorie | Pare-feu réseau d'IA appliquant les politiques aux flux des agents | AJOUT |
| Agent Sandbox | TECHNOLOGIE | catégorie | Bac à sable d'exécution des agents avec frontière réseau propre | AJOUT |
| Knowledge Catalog | TECHNOLOGIE | catégorie | Catalogue de définitions métier partagé par les agents de données | AJOUT |
| Google Workspace | TECHNOLOGIE | catégorie | Suite bureautique dans laquelle le Gemini agent opère | AJOUT |
| TPU 8i | TECHNOLOGIE | catégorie | Puce d'inférence de Google, 80 % de meilleur rapport prix-performance | AJOUT |
| Agent collègue | CONCEPT | définition | Agent à rôle persistant, avec identité, e-mail et stockage propres | AJOUT |
| Accenture | ORGANISATION | secteur | Conseil ; crée un Gemini Enterprise Business Group | AJOUT |
