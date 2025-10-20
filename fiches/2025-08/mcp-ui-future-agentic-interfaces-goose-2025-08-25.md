# mcp-ui-future-agentic-interfaces-goose-2025-08-25

## Veille
MCP-UI révolutionne interfaces agents IA, composants web interactifs, sandboxed iframes, accessibilité, générative UI - Goose/Block

## Titre Article
MCP-UI: The Future of Agentic Interfaces

## Date
2025-08-25

## URL
https://block.github.io/goose/blog/2025/08/25/mcp-ui-future-agentic-interfaces/

## Keywords
MCP-UI, Model Context Protocol UI, agentic interfaces, rich interactive web components, visual AI interfaces, embedded UI resources, cross-platform AI integration, accessibility, generative UI, Shopify integration, Monday.com, Goose, sandboxed iframes, remote DOM, multi-modal experiences

## Authors
Ebony Louis (Developer Advocate - Block/Goose)

## Pense-betes
- **Problème résolu** : murs de texte dans conversations agents IA, copier-coller URLs, multiples onglets
- **MCP-UI = protocole + SDK** pour composants web interactifs dans conversations agents
- **Trois types de contenu** : URLs externes, HTML brut, remote DOM (workers séparés)
- **Sécurité** : iframes sandboxed, communication via post messages uniquement
- **Ecosystem stakeholders** : développeurs agents, développeurs serveurs MCP, fournisseurs services, utilisateurs finaux
- **Exemples concrets** : Shopify (catalogues visuels), voyage (sélection sièges avion), restaurants (cartes photos + commande)
- **Shopify** : support MCP déployé sur tous leurs stores
- **Accessibilité** : agents construisent interfaces personnalisées selon préférences utilisateurs
- **Standardisation cross-platform** : une implémentation fonctionne partout
- **Défi actuel** : adoption, pas faisabilité technique
- **Network effect** : composants UI fonctionnent universellement une fois implémentés
- **Préserve expertise web** : décennies d'UI/UX + identité de marque
- **Getting started** : simple HTML `createUIResource({ type: 'html', content: '<h1>Hello World</h1>' })`

## RésuméDe400mots

**Le Problème des Interfaces Textuelles Pures**

Les interfaces d'agents IA traditionnelles souffrent d'une limitation fondamentale : elles forcent les utilisateurs à consommer toute information via réponses textuelles. Lorsqu'on demande des recommandations produits, planification voyage ou recherche restaurants, on reçoit des murs de texte accablants avec descriptions, liens et données nécessitant copier-coller manuel et jonglage d'onglets. Cela défait l'objectif d'avoir un assistant intelligent et crée une expérience utilisateur médiocre, spécialement pour non-techniques. L'approche texte-seulement fonctionne pour early adopters mais crée des barrières à l'adoption mainstream, limitant l'utilité des agents pour tâches quotidiennes.

**Architecture Technique de MCP-UI**

MCP-UI (Model Context Protocol User Interface) est à la fois protocole et SDK permettant d'intégrer des composants web interactifs riches directement dans les conversations d'agents IA. Le système exploite les embedded resources de la spécification MCP, autorisant les serveurs MCP à retourner composants UI interactifs plutôt que texte brut. Ces composants sont rendus dans des **iframes sandboxed** qui communiquent avec l'application hôte uniquement via messages post sécurisés, garantissant que code tiers ne peut accéder ou manipuler l'application parente.

L'implémentation supporte **trois types de contenu** : URLs externes (apps web existantes dans iframes), HTML brut (HTML custom avec CSS et JavaScript), et remote DOM (UI rendue dans workers séparés pour sécurité renforcée). Les développeurs peuvent commencer avec simples ressources HTML et progressivement enrichir avec fonctionnalités interactives.

**Bénéfices Clés et Cas d'Usage**

MCP-UI préserve décennies d'expertise web UI/UX tout en l'augmentant avec capacités IA. Il maintient l'identité de marque pour entreprises comme Shopify, fournit compatibilité cross-platform seamless entre différents agents IA, et crée un **network effect** où composants UI fonctionnent universellement une fois implémentés. La technologie adresse l'accessibilité en permettant aux agents de construire interfaces adaptées aux préférences et besoins individuels. Elle crée aussi standardisation, éliminant besoin d'intégrations séparées pour chaque plateforme IA.

**Démonstrations Concrètes**

Trois exemples compellants : **(1) Shopping Visuel** - catalogues Shopify avec images, prix et éléments interactifs où cliquer ajoute items au panier ; **(2) Planification Voyage** - cartes sélection sièges avion visuelles avec lookup météo automatique pour destinations ; **(3) Découverte Restaurants** - navigation restaurants locaux avec cartes photos, ratings, menus et capacités commande directe, tout dans le flux conversationnel.

**Implications Futures**

MCP-UI pointe vers une **révolution accessibilité** où agents construisent interfaces personnalisées, **générative UI** créant expériences sur-mesure pour utilisateurs individuels, **expériences multi-modales** s'étendant au-delà du visuel vers voix et composants mobiles natifs, et **standardisation cross-platform**. Le défi actuel est l'adoption plutôt que faisabilité technique, avec acteurs majeurs comme Shopify implémentant déjà support MCP sur tous leurs stores.

**Détails Implémentation Technique**

L'écosystème de stakeholders implique quatre groupes : développeurs agents implémentant support MCP-UI, développeurs serveurs MCP construisant composants UI, fournisseurs services créant interfaces riches, et utilisateurs finaux bénéficiant d'interactions intuitives. Démarrer nécessite code minimal - développeurs peuvent commencer avec ressources HTML basiques comme `createUIResource({ type: 'html', content: '<h1>Hello World</h1>' })` et étendre depuis là. La technologie est déjà supportée dans Goose et disponible via documentation complète et communauté Discord active.

MCP-UI représente un shift fondamental des interactions IA text-heavy vers expériences riches, visuelles et intuitives qui font le pont entre le web tel qu'on le connaît et le futur agentique en construction.
