# block-goose-mcp-ui-future-agentic-interfaces-2025-08-25

## Veille
Block/Goose — MCP-UI et le futur des interfaces agentiques : composants web interactifs dans les conversations d'agents IA via Model Context Protocol (block.github.io)

## Titre Article
Block's Goose and the Future of Agentic Interfaces via Model Context Protocol

## Date
2025-08-25

## URL
https://block.github.io/goose/blog/2025/08/25/mcp-ui-future-agentic-interfaces/

## Keywords
Block, Goose, MCP, Model Context Protocol, interfaces agentiques, futur des UI, Square, outils développeurs, agents IA, évolution des interfaces, intégration d'outils, gestion du contexte

## Authors
Block (Square) Engineering team

## Ton
**Profil :** Developer advocacy | Institutionnel tech | Éducatif-Promotionnel | Intermédiaire

L'équipe Goose de Block (billet signé Ebony Louis, Developer Advocate) adopte une voix d'advocacy développeur enthousiaste, articulée autour d'un épisode du podcast « Wild Goose Case » avec les créateurs de MCP-UI (Ido Salomon et Liad Yosef, Monday.com) et Andrew Harvard (Block). L'ouverture par les irritants concrets (« murs de texte », copier-coller d'URLs) installe des points de douleur relatables. La structure problème → solution → architecture → démos → vision guide une compréhension progressive. Le langage technique reste accessible (iframes sandboxées, post messages, remote DOM) et les exemples concrets (Shopify, sièges d'avion, restaurants) ancrent le protocole abstrait. Le ton optimiste, sans hype naïf (le défi reconnu est l'adoption), est typique de l'advocacy open source de Block visant la communauté des développeurs d'agents.

## Pense-betes
- **Goose** : agent IA open source de Block, parmi les premières plateformes à supporter MCP-UI
- **MCP-UI = protocole + SDK** : composants web riches et interactifs intégrés directement dans les conversations d'agents
- **Créateurs** : Ido Salomon et Liad Yosef (Monday.com), avec Andrew Harvard (Block) ; présenté dans l'épisode « Wild Goose Case »
- **Problème visé** : interfaces texte-seulement inadaptées au grand public — murs de texte, copier-coller, onglets multiples
- **Philosophie** : ne pas jeter des décennies d'expertise web UI/UX, mais l'augmenter avec l'IA
- **Sécurité** : composants rendus dans des iframes sandboxées, communication avec l'hôte uniquement par post messages
- **Trois types de contenu** : URLs externes, HTML brut, remote DOM (workers séparés)
- **Démos** : catalogue Shopify interactif, carte visuelle de sélection de sièges d'avion, découverte de restaurants avec commande
- **Effet de réseau** : un composant MCP-UI implémenté une fois fonctionne sur tous les agents compatibles (Goose, extensions VS Code, futurs assistants mobiles)
- **Vision** : révolution de l'accessibilité (l'agent construit l'UI selon les préférences), générative UI à terme
- **Démarrage simple** : `createUIResource({ type: 'html', content: '<h1>Hello World</h1>' })`

## RésuméDe400mots

Le blog Goose de Block publie une plongée dans **MCP-UI**, technologie qui, selon l'équipe, condamne « les murs de texte sans fin » des conversations d'agents IA. L'article s'appuie sur un épisode du podcast « Wild Goose Case » réunissant les créateurs de MCP-UI, **Ido Salomon et Liad Yosef de Monday.com**, et **Andrew Harvard de Block**, pour explorer comment cette technologie redessine le futur des interfaces agentiques.

**Le problème des interfaces texte-seulement**

Demander à un agent de l'aide pour un achat aboutit aujourd'hui à un mur de texte : noms de produits, prix, descriptions, puis copier-coller d'URLs et onglets multiples — l'utilisateur refait tout le travail. Comme le résume Ido Salomon, tout le monde a connu ce moment de « rage quit » devant un assistant qui ne renvoie que du texte. Ces interfaces conviennent aux early adopters, pas au grand public.

**MCP-UI : protocole et SDK**

MCP-UI (Model Context Protocol User Interface) permet d'intégrer des **composants web riches et interactifs** directement dans les conversations d'agents. La philosophie est simple : pourquoi jeter des décennies d'expertise web UI/UX quand on peut l'augmenter avec l'IA ? Liad Yosef souligne que plus d'une décennie d'interfaces web perfectionnées pour les limites cognitives humaines ne doit pas disparaître avec les agents. Le système exploite les embedded resources de la spécification MCP : un serveur MCP peut retourner des composants UI au lieu de texte brut. Quatre apports clés : composants riches (catalogues, cartes de sièges, formulaires), **préservation de la marque** (Shopify garde son expérience), intégration sécurisée, et **compatibilité cross-platform**.

**Fondations techniques**

La sécurité prime : les composants sont rendus dans des **iframes sandboxées** qui ne communiquent avec l'hôte que par post messages, empêchant le code tiers de manipuler l'application parente. Trois types de contenu sont supportés : URLs externes, HTML brut, et remote DOM (rendu dans des workers séparés). Le démarrage est minimal : `createUIResource({ type: 'html', content: '<h1>Hello World</h1>' })`.

**Démonstrations et écosystème**

Les démos montrent un shopping visuel (catalogue Shopify interactif avec ajout au panier), la planification de voyage (sélection de siège sur carte visuelle, météo de destination automatique) et la découverte de restaurants (cartes avec photos, notes, menus, commande directe) — le tout sans quitter la conversation. Le succès repose sur quatre parties prenantes : développeurs d'agents (comme l'équipe Goose), développeurs de serveurs MCP, fournisseurs de services (Shopify, Square) et utilisateurs finaux. L'approche crée un **effet de réseau** : un composant implémenté une fois fonctionne sur tous les agents compatibles.

**Vision**

Au-delà d'interfaces plus jolies : une **révolution de l'accessibilité** (« quoi de plus accessible qu'un agent qui vous connaît et construit l'UI selon vos préférences ? ») et, à terme, une **générative UI** produisant des interfaces adaptées aux besoins de chaque utilisateur.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Ebony Louis | PERSONNE | publie | article MCP-UI agentic interfaces | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| MCP-UI | TECHNOLOGIE | est_basé_sur | Model Context Protocol | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Ido Salomon | PERSONNE | a_créé | MCP-UI | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Liad Yosef | PERSONNE | a_créé | MCP-UI | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Ido Salomon | PERSONNE | travaille_chez | Monday.com | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Liad Yosef | PERSONNE | travaille_chez | Monday.com | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Andrew Harvard | PERSONNE | travaille_chez | Block | ORGANISATION | 0.96 | DYNAMIQUE | déclaré_article |
| MCP-UI | TECHNOLOGIE | utilise | iframes sandboxées | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| MCP-UI | TECHNOLOGIE | remplace | interfaces textuelles des agents IA | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Goose | TECHNOLOGIE | utilise | MCP-UI | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Shopify | ORGANISATION | utilise | MCP | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| MCP-UI | TECHNOLOGIE | permet | préservation de l'expérience de marque | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| MCP-UI | TECHNOLOGIE | permet | interfaces UI génératives personnalisées | CONCEPT | 0.85 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| MCP-UI | TECHNOLOGIE | catégorie | Protocole et SDK d'interface utilisateur pour agents IA | AJOUT |
| Goose | TECHNOLOGIE | éditeur | Block, Inc. | AJOUT |
| Block | ORGANISATION | secteur | Fintech / Outillage développeur IA | AJOUT |
| Monday.com | ORGANISATION | secteur | SaaS / Productivité | AJOUT |
| Ebony Louis | PERSONNE | rôle | Developer Advocate chez Block | AJOUT |
| Ido Salomon | PERSONNE | rôle | Créateur MCP-UI / Monday.com | AJOUT |
| Liad Yosef | PERSONNE | rôle | Créateur MCP-UI / Monday.com | AJOUT |
| Andrew Harvard | PERSONNE | rôle | Contributeur MCP-UI / Block | AJOUT |
| Shopify | ORGANISATION | secteur | E-commerce | AJOUT |
| iframes sandboxées | CONCEPT | rôle | Mécanisme d'isolation sécurisée des composants UI | AJOUT |
