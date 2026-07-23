# Veille Technologique

Documentation personnelle de veille technologique sur l'intelligence artificielle, les agents de codage, et l'évolution du développement logiciel.

> ### 🌐 Site officiel — **[www.thekb.eu](https://www.thekb.eu/)**
>
> Ces fiches sont publiées, traduites et enrichies sur **[theKB.eu](https://www.thekb.eu/)**, la **base de connaissance de référence sur l'IA, les agents de codage et l'évolution du développement logiciel (SDLC)** — disponible en **5 langues** : 🇬🇧 [English](https://www.thekb.eu/en/) · 🇫🇷 [Français](https://www.thekb.eu/fr/) · 🇩🇪 [Deutsch](https://www.thekb.eu/de/) · 🇪🇸 [Español](https://www.thekb.eu/es/) · 🇮🇹 [Italiano](https://www.thekb.eu/it/).
>
> **Ce dépôt GitHub est la source ; [www.thekb.eu](https://www.thekb.eu/) en est la version canonique et consultable.** Pour lire, citer ou parcourir les analyses, rendez-vous sur **[www.thekb.eu](https://www.thekb.eu/)**.

## 🌐 Site officiel : theKB.eu

**[theKB.eu](https://www.thekb.eu/)** est le site de référence multilingue qui publie ces fiches de veille sous forme de pages web lisibles, traduites automatiquement et reliées par un graphe de connaissance. C'est la **version officielle et canonique** de ce dépôt : le contenu ci-dessous est la matière première, **[www.thekb.eu](https://www.thekb.eu/) en est la publication de référence**.

### Explorer les analyses

- 🏠 **[www.thekb.eu](https://www.thekb.eu/)** — accueil, dernières fiches de veille sur l'IA et les agents de codage
- 📚 **[Toutes les thématiques](https://www.thekb.eu/en/topics/)** — 11 sujets couvrant l'IA appliquée au développement logiciel :
  - [AI Coding Agents & Skills](https://www.thekb.eu/en/topics/coding-agents-skills/) — agents de codage, skills, art du prompt
  - [Architecture & Construction](https://www.thekb.eu/en/topics/architecture-construction/) — architecture logicielle à l'ère de l'IA
  - [Transformation & Adoption](https://www.thekb.eu/en/topics/transformation-adoption/) — adoption de l'IA dans les équipes
  - [Quality & Security](https://www.thekb.eu/en/topics/quality-security/) — qualité et sécurité du code généré
  - [Economy & Market](https://www.thekb.eu/en/topics/economy-market/) — économie et marché de l'outillage IA
  - [Strategy & Frameworks](https://www.thekb.eu/en/topics/strategy-frameworks/) — frameworks stratégiques pour la transition IA
- 🔎 **[Recherche](https://www.thekb.eu/en/search/)** · 🗂️ **[Glossaire](https://www.thekb.eu/en/glossary/)** · 🕸️ **[Entités (graphe de connaissance)](https://www.thekb.eu/en/entities/)**

### Pour les agents & les IA (GEO / AEO)

theKB.eu offre une **double ergonomie** — pages web pour les humains, surface agent-native pour les IA :

- 🤖 **[llms.txt](https://www.thekb.eu/llms.txt)** — index des fiches optimisé pour les LLM (chaque page a un jumeau Markdown à `{url}.md`)
- 🔌 **[Serveur MCP](https://www.thekb.eu/en/developers/mcp/)** (`mcp.thekb.eu`) — accès programmatique en lecture seule (recherche, fiches, graphe)

**Licence** : contenu sous [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — libre de citation, réutilisation et entraînement, avec **attribution à [theKB.eu](https://www.thekb.eu/)** (et un lien).

## Vue d'ensemble

Ce dépôt contient une collection de fiches d'analyse d'articles techniques, organisées par mois de publication et classées par thématiques. L'objectif est de suivre l'évolution rapide de l'écosystème IA et son impact sur l'ingénierie logicielle.

<!-- stats:begin -->

- **Total** : 353 fiches
- **Par année** : 2026 (176) · 2025 (160) · 2024 (9) · 2023 (3) · 2022 (2) · 2019 (1) · 1975 (2)
- **Par thème** :
  - Agents de codage IA & Skills : 120
  - Architecture & Construction : 37
  - Transformation & Adoption : 73
  - Qualité & Sécurité : 25
  - Économie & Marché : 64
  - Philosophie & Société : 22
  - Stratégie & Frameworks : 16
  - Outils & Plateformes : 29
  - Recherche & Éducation : 9
  - Produits & Services : 9
  - Politique & Régulation : 14
- **Auteurs (top 20)** :
  - Ethan Mollick (11)
  - SFEIR (9)
  - Anthropic (8)
  - Chris Williams (7)
  - Deep Research Veille Interne (7)
  - Philippe Ensarguet (6)
  - Addy Osmani (6)
  - Boris Cherny (5)
  - Kieran Klaassen (4)
  - Olivier Rafal (4)
  - OpenAI (4)
  - Thariq Shihipar (3)
  - Simon Willison (3)
  - Andrew Ng (3)
  - Dan Shipper (3)
  - Kent Beck (3)
  - Jesse Vincent (3)
  - Cobus Greyling (3)
  - Janakiram MSV (2)
  - Nicolas Martignole (2)
- **Sources (top 20)** :
  - Anthropic (13)
  - SFEIR (9)
  - LinkedIn (7)
  - voodootikigod.com (Chris Williams) (7)
  - Deep Research (7)
  - Google (7)
  - OpenAI (5)
  - Ethan Mollick (4)
  - GitHub (4)
  - One Useful Thing (4)
  - Addy Osmani (3)
  - a16z (3)
  - Netflix (2)
  - LinkedIn (Philippe Ensarguet) (2)
  - CIO-Online (Olivier Rafal) (2)
  - The Batch / DeepLearning.AI (2)
  - Finout (2)
  - Kent Beck (2)
  - Anthropic (X/Twitter) (2)
  - Tessl (2)

<!-- stats:end -->

_Statistiques générées par `scripts/build_index.py`._

## Structure du projet

```
veille/
├── index.md                    # Index principal avec liens vers toutes les fiches
├── fiches/                     # Fiches organisées par mois de publication
│   ├── 2019-01/
│   ├── 2023-06/ à 2023-10/
│   ├── 2024-04/ à 2024-10/
│   ├── 2025-01/ à 2025-12/
│   └── 2026-01/ à 2026-04/
├── kb/                         # Knowledge base générée (entités, index par type)
├── knowledge-base.md           # Dashboard KB (entités, triples, navigation)
├── docs/                       # Documentation et analyses complémentaires
├── gold/                       # Livrables générés + prompts (ignoré par git)
├── raw-data/                   # Contenu brut des articles (ignoré par git)
├── scripts/                    # Scripts d'extraction, conversion et KB
│   ├── fetch_urls.py           # Extraction des URLs des fiches
│   ├── download_raw_data.py    # Téléchargement et conversion en markdown
│   ├── build_knowledge_base.py # Construction du knowledge graph
│   ├── lint_fiches.py          # Validation ontologie des fiches (gate Bronze)
│   ├── check_missing.py        # Vérification des fiches manquantes
│   └── list_missing_kg.sh      # Détection des fiches sans GrapheDeConnaissance
├── mobile-share/               # App Flutter pour capturer des URLs depuis mobile
├── CLAUDE.md                   # Instructions pour Claude Code
├── gemini.md                   # Instructions pour Gemini
└── urls-to-process.md          # URLs en attente de traitement
```

## Thématiques principales

### Agents de codage IA & Skills
Méthodologies, frameworks et retours d'expérience sur l'utilisation d'agents IA pour le développement logiciel.

### Architecture & Construction
Patterns d'architecture, protocoles (MCP, RAG), et systèmes de documentation automatisée.

### Transformation & Adoption
Stratégies d'adoption, changements organisationnels et impact sur les équipes.

### Qualité & Sécurité
Code quality, testing, security, bias measurement et incidents de production.

### Économie & Marché
Modèles économiques, disruption du conseil, commerce agentique et tendances marché.

### Philosophie & Société
Réflexions sur l'impact sociétal et philosophique de l'IA.

### Stratégie & Frameworks
Wardley Mapping, frameworks d'adoption, playbooks organisationnels.

### Outils & Plateformes
Claude Code, Gemini CLI, Deepnote, Linear et autres outils AI-first.

### Recherche & Éducation
Publications académiques, benchmarks et ressources éducatives.

### Produits & Services
Lancements de produits, plateformes et services IA.

### Politique & Régulation
Politiques publiques, régulation de l'IA et cadres légaux.

## Format des fiches

Chaque fiche suit un format standardisé :

```markdown
# [Identifiant Technique]
## Veille
## Titre Article
## Date
## URL
## Keywords
## Authors
## Ton
## Pense-betes
## RésuméDe400mots
## GrapheDeConnaissance
```

Chaque fiche inclut un graphe de connaissance structuré (triples sujet-prédicat-objet et entités typées) qui alimente la knowledge base.

**Langue** : Toutes les fiches sont rédigées en français (sauf titre original et noms d'auteurs).

## Principales sources

- **Blogs techniques** : One Useful Thing (Ethan Mollick), Pragmatic Engineer, RedMonk, martinfowler.com
- **Organisations** : Anthropic, Google, Stanford, a16z, DeepMind, OpenAI, Mistral AI
- **Plateformes** : LinkedIn, Medium, GitHub, YouTube, Substack
- **Recherche** : Harvard Business Review, Wharton, METR, Apollo Academy, arXiv
- **Entreprises** : HubSpot, Block/Square, Netflix, Xebia, Stripe, Cloudflare, Replit

## Auteurs principaux suivis

Le classement des auteurs et sources les plus suivis est **généré automatiquement** et
maintenu à jour dans le bloc de statistiques en tête de ce README (`scripts/build_index.py`).
On y retrouve notamment Ethan Mollick, Anthropic, Chris Williams, SFEIR, Philippe Ensarguet,
Addy Osmani, Boris Cherny, OpenAI, Simon Willison, Andrew Ng ou Kent Beck.

## Knowledge Base

Le dépôt intègre un knowledge graph construit automatiquement à partir des sections `GrapheDeConnaissance` de chaque fiche :

- **2845 entités** typées (PERSONNE, ORGANISATION, TECHNOLOGIE, CONCEPT, METHODOLOGIE, EVENEMENT, LIEU, DOCUMENT)
- **5020 triples** relationnels
- Pages individuelles par entité avec backlinks dans `kb/`
- Dashboard de navigation dans `knowledge-base.md`
- Visualisation via le graph view d'Obsidian

## Workflow d'ajout d'article

1. **Ajouter l'URL** dans `urls-to-process.md` ou via l'app mobile (`mobile-share/`)
2. **Créer la fiche** dans `fiches/YYYY-MM/identifiant.md`
3. **Sauvegarder le contenu brut** dans `raw-data/identifiant.md`
4. **Mettre à jour `index.md`** (chronologie, thématiques, statistiques)
5. **Reconstruire la KB** avec `python3 scripts/build_knowledge_base.py`

Voir [CLAUDE.md](CLAUDE.md) pour les instructions détaillées.

## Scripts utiles

```bash
# Extraire toutes les URLs des fiches
python3 scripts/fetch_urls.py

# Télécharger et convertir le contenu brut
python3 scripts/download_raw_data.py

# Construire/reconstruire la knowledge base
python3 scripts/build_knowledge_base.py

# Vérifier les fiches manquantes
python3 scripts/check_missing.py

# Lister les fiches sans GrapheDeConnaissance
bash scripts/list_missing_kg.sh
```

## App mobile (mobile-share)

Application Flutter/Dart pour capturer des URLs depuis le partage natif du téléphone et les synchroniser vers le dépôt GitHub. Architecture BLoC, stockage local SQLite.

## Statistiques actuelles

- **349 fiches** analysées
- **Période** : Décembre 1975 - Juillet 2026
- **2845 entités** et **5020 triples** dans la knowledge base
- **11 thématiques** principales
- **60+ auteurs** suivis
- **60+ sources** documentées

## Liens utiles

- 🌐 **[www.thekb.eu](https://www.thekb.eu/)** — **site officiel** : version publiée, multilingue et canonique de cette veille
- [Index complet](index.md) - Toutes les fiches organisées
- [Knowledge Base](knowledge-base.md) - Dashboard entités et triples
- [CLAUDE.md](CLAUDE.md) - Instructions pour Claude Code
- [Synthèse Juillet-Octobre 2025](SYNTHESE-JUILLET-OCTOBRE-2025.md)

## Licence

Documentation personnelle à usage interne.

---

**Dernière mise à jour** : Juillet 2026
