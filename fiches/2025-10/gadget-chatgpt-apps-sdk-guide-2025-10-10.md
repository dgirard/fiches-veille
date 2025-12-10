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
