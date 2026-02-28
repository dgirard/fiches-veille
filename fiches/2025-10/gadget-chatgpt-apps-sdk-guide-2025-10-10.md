# gadget-chatgpt-apps-sdk-guide-2025-10-10

## Veille

Guide développement ChatGPT Apps SDK OpenAI - MCP, OAuth 2.1, Widgets

## Titre Article

Everything you need to know about building ChatGPT apps

## Date

2025-10-10

## URL

https://gadget.dev/blog/everything-you-need-to-know-about-building-chatgpt-apps

## Keywords

ChatGPT Apps, OpenAI SDK, MCP, Model Context Protocol, OAuth 2.1, Widgets, CORS, Vite, window.openai, Streamable HTTP, iframes, développement applicatif

## Authors

Harry (Gadget)

## Ton

**Profil** : Retour d'expérience technique de première main, registre décontracté mais expert, niveau technique élevé.

**Description** : L'auteur partage son expérience acquise "hot-off-the-presses" après plusieurs jours de développement intensif sur le SDK ChatGPT Apps. Le ton est celui d'un développeur qui s'adresse à ses pairs, mêlant humour ("Cross Origin Emotional Damage", "boy oh boy are we early") et expertise technique pointue. L'article adopte une posture de guide pratique, partageant les pièges rencontrés et les solutions trouvées. L'auteur n'hésite pas à critiquer les lacunes de la documentation officielle d'OpenAI tout en proposant des alternatives concrètes. Public cible : développeurs expérimentés souhaitant construire des applications ChatGPT.

## Pense-betes

- Une ChatGPT App = serveur MCP + extension UI (widgets) + optionnellement OAuth 2.1/OIDC
- Privilégier `StreamableHTTPServerTransport` plutôt que la version SSE des exemples OpenAI
- Les exemples officiels utilisent une map session en mémoire qui ne fonctionne pas en serverless
- Utiliser le MCP Inspector pour déboguer avant ChatGPT (messages d'erreur ChatGPT non informatifs)
- OAuth 2.1 : vous êtes le **provider**, pas le client - inversion du modèle habituel
- Les widgets sont des iframes sandboxées avec HTML statique (pas de SSR possible)
- Vite recommandé pour développer les widgets (TypeScript, Tailwind, HMR)
- `window.openai` permet d'appeler les outils MCP depuis le widget avec auth gratuite
- Alternative : `fetch` direct mais perte de l'auth et de la visibilité LLM sur les interactions
- CORS : configuration nécessaire pour MCP, OAuth 2.1 et assets frontend
- Origin des widgets : `https://web-sandbox.oaiusercontent.com`
- Plugin Vite pour ChatGPT Widgets disponible sur GitHub Gadget

## RésuméDe400mots

L'équipe Gadget partage son retour d'expérience après plusieurs jours de développement intensif sur le nouveau SDK ChatGPT Apps d'OpenAI. L'article détaille les trois composantes essentielles d'une application ChatGPT : un serveur MCP conforme au Model Context Protocol, une extension permettant d'afficher des interfaces utilisateur dans les conversations, et optionnellement un serveur OAuth 2.1 avec OIDC pour l'authentification.

Pour la construction de serveurs MCP, l'article recommande d'utiliser le transport Streamable HTTP plutôt que la version SSE présentée dans les exemples officiels d'OpenAI. Les exemples fournis utilisent une map de sessions en mémoire inadaptée aux plateformes serverless. Le MCP Inspector est conseillé pour le débogage initial car les messages d'erreur de ChatGPT sont peu informatifs.

L'implémentation de l'authentification OAuth 2.1 représente un changement de paradigme : contrairement à l'usage habituel où l'on redirige vers un provider externe comme Google, ici l'application doit elle-même être le provider OAuth pour OpenAI. Cela nécessite d'implémenter les endpoints OIDC de découverte permettant à ChatGPT d'obtenir des tokens.

La fonctionnalité la plus innovante est la possibilité de servir des widgets UI interactifs aux utilisateurs. Ces widgets sont en réalité des iframes sandboxées qui chargent un document HTML statique, mis en cache à l'installation de l'application. Cette contrainte impose le développement d'applications client-side single-page, sans rendu serveur dynamique. L'équipe recommande Vite pour la compilation TypeScript, le bundling, le hot-module-reloading et le support Tailwind. Un plugin Vite dédié est disponible sur GitHub.

Pour la communication avec le backend depuis un widget, deux approches existent. L'objet `window.openai` injecté par OpenAI permet d'appeler les outils MCP avec l'authentification gérée automatiquement et une visibilité pour le LLM sur les interactions. L'alternative via `fetch` direct nécessite de gérer l'authentification manuellement et perd la conscience contextuelle du LLM.

Le CORS constitue un défi majeur avec trois configurations distinctes à gérer : les routes MCP, les routes OAuth 2.1, et les assets frontend. Pour les deux premières, un header permissif `Access-Control-Allowed-Origin: *` est recommandé car l'authentification sécurise déjà les appels. Pour les assets de widgets, il faut autoriser l'origin `https://web-sandbox.oaiusercontent.com` utilisée par OpenAI.

L'article conclut que l'écosystème est encore très jeune mais prometteur, avec des templates prêts à l'emploi disponibles chez Gadget pour accélérer le démarrage.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Gadget | ORGANISATION | a_publié | guide ChatGPT Apps SDK | EVENEMENT | 0.98 | STATIQUE | déclaré_article |
| Harry Brundage | PERSONNE | a_rédigé | guide ChatGPT Apps SDK | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| ChatGPT App | CONCEPT | est_basé_sur | MCP server | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| ChatGPT App | CONCEPT | utilise | OAuth 2.1 | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| ChatGPT App | CONCEPT | intègre | widgets iframes | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Gadget | ORGANISATION | recommande | StreamableHTTPServerTransport | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | ChatGPT Apps SDK | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| ChatGPT Apps SDK | TECHNOLOGIE | nécessite | OAuth 2.1 provider | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Vite | TECHNOLOGIE | améliore | développement widgets ChatGPT | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| window.openai | TECHNOLOGIE | fournit | authentification gratuite | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| CORS | CONCEPT | bloque | développement ChatGPT Apps | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| MCP Inspector | TECHNOLOGIE | facilite | débogage MCP | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Gadget | ORGANISATION | s_oppose_à | exemples officiels OpenAI | CONCEPT | 0.88 | STATIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Harry Brundage | PERSONNE | rôle | Auteur principal, développeur Gadget | AJOUT |
| Gadget | ORGANISATION | secteur | Plateforme de développement full-stack | AJOUT |
| OpenAI | ORGANISATION | secteur | IA / Produits LLM | AJOUT |
| ChatGPT Apps SDK | TECHNOLOGIE | catégorie | SDK pour applications ChatGPT intégrées | AJOUT |
| MCP server | TECHNOLOGIE | catégorie | Serveur Model Context Protocol | AJOUT |
| OAuth 2.1 | TECHNOLOGIE | rôle | Protocole d'authentification provider-side | AJOUT |
| StreamableHTTPServerTransport | TECHNOLOGIE | statut | Transport recommandé vs SSE obsolète | AJOUT |
| Vite | TECHNOLOGIE | usage | Bundler TypeScript/HMR pour widgets | AJOUT |
| window.openai | TECHNOLOGIE | catégorie | Objet injecté dans iframe par OpenAI | AJOUT |
| MCP Inspector | TECHNOLOGIE | usage | Outil de débogage MCP hors ChatGPT | AJOUT |
| CORS | CONCEPT | catégorie | Contrainte sécurité cross-origin navigateur | AJOUT |
| widgets iframes | CONCEPT | contrainte | HTML statique, SPA obligatoire, mis en cache à l'installation | AJOUT |
