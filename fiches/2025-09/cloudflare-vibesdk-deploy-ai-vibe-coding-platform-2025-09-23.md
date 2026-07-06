---
themes: [agents-codage-ia-skills]
source: "Cloudflare"
---
# cloudflare-vibesdk-deploy-ai-vibe-coding-platform-2025-09-23

## Veille
VibeSDK - Plateforme vibe coding open-source - Cloudflare Sandboxes - Workers for Platforms - AI Gateway - Déploiement one-click - Cloudflare

## Titre Article
Deploy your own AI vibe coding platform -- in one click!

## Date
2025-09-23

## URL
https://blog.cloudflare.com/deploy-your-own-ai-vibe-coding-platform/

## Keywords
VibeSDK, vibe coding, Cloudflare, Sandboxes, Workers for Platforms, AI Gateway, open source, Agents SDK, code generation, isolated environments, deployment at scale, Gemini models, project templates, GitHub export, observability, caching, multi-model support, untrusted code execution, wrangler deploy, dispatch namespace, LLM integration

## Authors
Ashish Kumar Singh, Abhishek Kankani, Dina Kozlov

## Ton
**Profil:** Annonce produit technique | Première personne collective organisationnelle | Éducatif-promotionnel | Expert accessible

L'équipe Cloudflare adopte une voix de lancement produit combinant plongée technique approfondie et accessibilité. La structure en tutoriel pas-à-pas (étapes 0 à 4 + section déploiement) illustre l'approche d'éducation des développeurs typique du blog Cloudflare. Le langage d'ingénieur infrastructure (sandboxes, environnements isolés, dispatch namespace, Workers for Platforms), mêlé à des exemples de code concrets, crée une expérience d'apprentissage pratique. Le ton enthousiaste-pragmatique (« It's an exciting time to build applications ») reflète une culture orientée développeurs. L'accent sur la philosophie open source (même raison que l'open-sourcing du runtime Workers) positionne la démarche comme une démocratisation de plateforme. Typique des fournisseurs d'infrastructure (Cloudflare, Vercel, Railway) produisant du contenu technique pour des développeurs cherchant des solutions clés en main pour des scénarios de déploiement complexes.

## Pense-betes
- **VibeSDK** : plateforme open source complète pour déployer sa propre plateforme de vibe coding en un clic
- **Démo disponible** : plateforme utilisable + bouton de déploiement instantané
- **Cloudflare Sandboxes** : environnements isolés à base de conteneurs pour exécuter du code IA non fiable
- **Sandboxes par session** : chaque utilisateur obtient un sandbox persistant entre les sessions
- **Workflow de génération de code** : l'IA génère → écrit les fichiers → installe les paquets → démarre le serveur
- **Templates de projets** : stockage dans un bucket R2 pour un démarrage rapide plutôt qu'une génération de zéro
- **URL de preview publiques** : le Sandbox SDK expose les ports pour une prévisualisation instantanée des applications
- **Auto-débogage** : logs et erreurs capturés et renvoyés au LLM pour corrections automatiques
- **Workers for Platforms** : déploiement scalable de milliers/millions de Workers isolés dans un dispatch namespace
- **URL uniques** : chaque application déployée reçoit une URL isolée (my-app.vibe-build.example.com)
- **Sandbox de déploiement** : sandbox spécialisé séparé exécutant wrangler deploy
- **Capacité d'export** : les utilisateurs exportent vers leur propre compte Cloudflare ou un dépôt GitHub
- **Intégration AI Gateway** : point d'accès unifié multi-fournisseurs (OpenAI, Anthropic, Google)
- **Modèles Gemini** : gemini-2.5-pro, gemini-2.5-flash-lite, gemini-2.5-flash par défaut
- **Cache intégré** : mise en cache des réponses populaires (ex. « build to-do list app »)
- **Observabilité** : suivi des requêtes, tokens consommés, temps de réponse et coûts multi-fournisseurs
- **Cas d'usage** : équipes internes (marketing, produit, support) + intégration SaaS pour personnalisations utilisateur
- **Agents SDK** : motorise l'intégration LLM pour générer, construire, déboguer et itérer en temps réel
- **Architecture de référence** : documentation complète de conception d'une plateforme de vibe coding

## RésuméDe400mots

Cloudflare lance VibeSDK, une plateforme open-source complète permettant à quiconque de déployer sa propre plateforme de vibe coding alimentée par IA en un seul clic. Cette initiative démocratise l'accès à la construction de plateformes où utilisateurs internes et externes peuvent créer applications simplement en décrivant leurs besoins en langage naturel.

**Architecture et composants**

VibeSDK intègre tous les composants nécessaires : intégration LLM via Agents SDK pour génération de code et debugging temps réel, environnements de développement isolés dans Cloudflare Sandboxes pour exécution sécurisée de code AI non fiable, déploiement à échelle infinie via Workers for Platforms sur le réseau global Cloudflare, observabilité et caching multi-providers via AI Gateway, templates de projets pour accélération développement, et export one-click vers comptes Cloudflare ou GitHub repos.

**Isolation sécurisée avec Sandboxes**

Le défi majeur du vibe coding est l'exécution sécurisée de code généré par IA. Cloudflare Sandboxes fournit des environnements isolés container-based où le code AI peut installer packages npm, exécuter builds, démarrer serveurs, sans risque d'affecter autres utilisateurs ou systèmes. Chaque utilisateur reçoit un sandbox assigné à sa session, permettant persistance des fichiers entre visites.

**Workflow de génération et preview**

Le workflow orchestré couvre l'ensemble du cycle : l'IA génère structure application (React, Node.js, full-stack), écrit fichiers directement dans le sandbox, installe dépendances via `bun install`, démarre le serveur de développement. Le Sandbox SDK expose ensuite le port 3000 avec une URL publique de preview, permettant aux utilisateurs de voir instantanément leur application générée par IA en ligne. Les logs, erreurs, et sorties console sont capturés et retournés au LLM pour auto-debugging itératif.

**Déploiement à grande échelle**

Une fois l'application développée, un "deployment sandbox" spécialisé package le contenu et exécute `wrangler deploy` via Workers for Platforms. Le système peut déployer milliers ou millions de Workers dans un dispatch namespace unique, tous isolés par défaut sans cross-tenant access. Chaque application déployée reçoit une instance Worker isolée avec URL unique.

**Multi-model et observabilité**

VibeSDK utilise par défaut les modèles Gemini de Google (gemini-2.5-pro, flash-lite, flash) pour planification projet, génération code et debugging. L'intégration AI Gateway offre accès unifié aux providers (OpenAI, Anthropic, Google), caching automatique des réponses populaires (économie coûts inference), observabilité centralisée des requests/tokens/response times, et tracking des coûts cross-models.

**Cas d'usage et personnalisation**

Les organisations peuvent déployer VibeSDK pour équipes internes (marketing, produit, support créant landing pages, prototypes, outils sans dépendre engineering) ou l'embedder dans produits SaaS permettant aux users de construire customizations. La plateforme open-source permet custom logic pour prompts LLM spécifiques, contrôle complet sur environnement développement et hosting, garantissant privacy et contrôle des données.

Cloudflare open-source VibeSDK avec la même philosophie que le Workers runtime : développement optimal se fait dans l'ouvert, économisant mois d'intégration pour quiconque souhaite construire plateforme vibe coding.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Cloudflare | ORGANISATION | publie | VibeSDK | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| VibeSDK | TECHNOLOGIE | est_basé_sur | Agents SDK | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| VibeSDK | TECHNOLOGIE | utilise | Cloudflare Sandboxes | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| VibeSDK | TECHNOLOGIE | utilise | Workers for Platforms | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| VibeSDK | TECHNOLOGIE | utilise | AI Gateway | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| VibeSDK | TECHNOLOGIE | utilise | Gemini models | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| AI Gateway | TECHNOLOGIE | permet | multi-model support | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| Cloudflare Sandboxes | TECHNOLOGIE | permet | isolation du code généré par IA | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Workers for Platforms | TECHNOLOGIE | permet | déploiement à grande échelle de Cloudflare Workers | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| vibe coding | METHODOLOGIE | améliore | développement logiciel | CONCEPT | 0.88 | DYNAMIQUE | inféré |
| VibeSDK | TECHNOLOGIE | permet | déploiement one-click | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| AI Gateway | TECHNOLOGIE | réduit | coûts inference | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Cloudflare | ORGANISATION | secteur | Infrastructure cloud / réseau global | AJOUT |
| VibeSDK | TECHNOLOGIE | catégorie | Plateforme vibe coding open-source | AJOUT |
| Agents SDK | TECHNOLOGIE | rôle | Orchestration LLM pour génération de code | AJOUT |
| Cloudflare Sandboxes | TECHNOLOGIE | catégorie | Environnements isolés container-based | AJOUT |
| Workers for Platforms | TECHNOLOGIE | catégorie | Déploiement Workers à grande échelle | AJOUT |
| AI Gateway | TECHNOLOGIE | catégorie | Accès unifié multi-providers LLM | AJOUT |
| Gemini models | TECHNOLOGIE | catégorie | Modèles LLM Google (2.5-pro, flash, flash-lite) | AJOUT |
| vibe coding | METHODOLOGIE | définition | Développement applicatif par description langage naturel | AJOUT |
| Ashish Kumar Singh | PERSONNE | rôle | Auteur de l'article Cloudflare Blog | AJOUT |
| Abhishek Kankani | PERSONNE | rôle | Auteur de l'article Cloudflare Blog | AJOUT |
| Dina Kozlov | PERSONNE | rôle | Auteur de l'article Cloudflare Blog | AJOUT |
