# mcp-ui-conference-monday-liad-yosef-2025-10-18

## Veille
MCP-UI conférence détaillée, islands architecture, remote DOM, theming, état distribué, authentification, clients natifs - Monday.com

## Titre Article
MCP-UI: The Future of Agentic Interfaces (Conference Talk)

## Date
2025-10-18

## URL
https://www.youtube.com/watch?v=SIXTArBVL5w

## Keywords
MCP-UI, islands architecture, remote DOM, theming, sandboxed iframes, state management, authentication, native clients, post messages, web fragmentation, composable UI, intent-based communication, Shopify, Hugging Face, Postman, Monday.com

## Authors
Liad Yosef (AI & MCP Lead - Monday.com, co-modérateur UI work group)

## Pense-betes
- **Problème double** : perte d'identité fournisseurs (Shopify/Airbnb/Amazon) ET expérience utilisateur dégradée
- **MCP-UI = protocole ouvert** pour envoyer UI via MCP + standardiser communication host/UI
- **SDKs communautaires** : Ruby, Python, TypeScript, Go en cours
- **Adoptants majeurs** : Shopify (full), Postman, Goose, Hugging Face (tous les spaces), 11 Labs
- **Islands architecture** : différentes îles d'UI composées dans un contexte unique
- **Communication spectrum** : notify → tool call → prompt → intent (niveaux responsabilité croissants)
- **Sécurité** : sandboxed iframes, pas d'accès origin host, communication post messages uniquement
- **État 4 niveaux** : agent context, internal app state, backend, cookies/localStorage
- **Theming multi-layers** : custom CSS, CSS variables, theme tokens, remote DOM
- **Remote DOM** : séparation structure/rendering, même serveur → différents clients visuellement
- **Démo sprint management** : widget interactif Monday, intégration Gmail automatique, reassign Jordan
- **Future** : auth/SSO, clients natifs (non web-views), capabilities negotiation
- **Vision** : web fragmenté → apps déconstructées en atomes composables par assistant personnel
- **mcpui.dev** : guides, walkthroughs, exemples

## RésuméDe400mots

**Problématique Double et Solution**

Liad Yosef (AI & MCP Lead chez Monday.com, co-modérateur du UI work group) présente MCP-UI comme solution à un problème double. Premièrement, les interfaces textuelles créent des murs de texte pour les utilisateurs. Deuxièmement, et plus critique, les fournisseurs (Shopify, Airbnb, Amazon) **perdent leur identité** lorsqu'ils envoient uniquement du texte - le chat décide de l'affichage, les privant de leur place dans la chaîne de valeur. MCP-UI permet à chaque application d'envoyer des "chunks d'UI" - morceaux de leur identité - préservant reconnaissance visuelle et user experience perfectionée sur années.

**Architecture Technique et Sécurité**

MCP-UI est un **protocole ouvert** + SDK pour envoyer UI via MCP et standardiser communication host/UI. L'architecture repose sur **sandboxed iframes** garantissant sécurité : le code UI n'accède pas à l'origin du host, ne peut voler cookies/mémoire, communique uniquement via **post messages**. Trois types de contenu supportés : URLs externes, HTML brut, **remote DOM** (concept puissant séparant définition structure et rendering - même serveur MCP peut envoyer réponse identique à différents clients qui la rendront avec leurs propres composants).

**Spectrum de Communication et État**

MCP-UI définit un **spectrum de communication** représentant niveaux de responsabilité UI sur actions utilisateur : **(1) Notify** - UI exécute action backend et notifie chat ; **(2) Tool call** - UI demande trigger outil spécifique ; **(3) Prompt** - UI demande exécution prompt ; **(4) Intent** - UI envoie intention utilisateur, host décide quoi faire. Cette architecture **islands** (îles UI différentes composées dans contexte unique) nécessite gestion état sophistiquée sur **4 niveaux** : agent context (pour flow agentique), internal app state (préférences, steppers via cookies/localStorage), backend (data non pertinente pour flow agentique mais nécessaire synchronisation), et état partagé entre composants.

**Démonstration Concrète : Sprint Management**

La démo montre manager ingénierie demandant "sprint status". Au lieu de texte inutile, MCP-UI retourne **widget interactif Monday** avec breakdown visuel. Clic sur "stuck tasks" → affiche tâche "implementing authentication" assignée Sarah. Clic "analyze" → communication mechanism envoie prompt à agent qui, connecté à Gmail via autre serveur MCP, **fetch emails automatiquement** découvrant Sarah malade, Jordan connaît code. Widget injecte analyse colorisée suggérant reassign Jordan. Clic "reassign" → message intent déclenche tool call MCP complétant flow. Cruciale : **provider n'a pas créé intégration Gmail** - agent a fait connexion avec contexte existant.

**Theming Multi-Layers**

Pour éviter expérience "compilation d'UIs tierces", MCP-UI supporte **theming sophistiqué** : custom CSS (Shopify l'implémente déjà), CSS variables, theme tokens, et **remote DOM** (le plus puissant - UI distante rendue avec composants host, garantissant cohérence visuelle tout en préservant structure/interactions provider).

**Adoptants et Ecosystem**

Adoption massive déjà : **Shopify full deployment**, Postman, Goose, Libra chat (hosts) ; **Hugging Face** (tous spaces exposés MCP-UI), 11 Labs, MCP storefront (providers). SDKs communautaires Ruby, Python, TypeScript, Go. Projet communautaire sur **mcpui.dev** avec guides complets.

**Vision Future : Web Fragmenté Recomposé**

Vision transformative : aujourd'hui on ouvre 10 tabs différentes (Amazon, Calendar, Booking) pour tâche unique (planifier anniversaire), chacune avec UI complexe dont 90% irrelevant. Future : assistant personnel compose **atomes d'UI** de providers - Google Calendar envoie chunk event, Amazon chunk product list, Booking chunk listings+map. Aucune intégration provider-to-provider nécessaire - assistant a contexte complet. Résultat : **apps déconstructibles** en composants réutilisables, Jarvis accessible car overhead intégration disparu.

**Challenges Roadmap**

Trois défis majeurs : **(1) Auth/SSO** - actuellement état baked in context/UI ou auth in-UI, besoin SSO seamless ; **(2) Clients natifs** - ChatGPT/Claude vont natif, beaucoup ne supportent pas iframes/webviews, exploration **abstract payload** convertible HTML ou native avec **capabilities negotiation** ; **(3) Standardisation adoption** - technologie ready, besoin momentum communautaire.
