# Veille Technologique

Documentation personnelle de veille technologique sur l'intelligence artificielle, les agents de codage, et l'évolution du développement logiciel.

## Vue d'ensemble

Ce dépôt contient une collection de fiches d'analyse d'articles techniques, organisées par mois de publication et classées par thématiques. L'objectif est de suivre l'évolution rapide de l'écosystème IA et son impact sur l'ingénierie logicielle.

**Période couverte** : Décembre 1975 - Avril 2026
**Total d'articles** : 215 fiches
**Knowledge Base** : 1431 entités, 2731 triples

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
├── raw-data/                   # Contenu brut des articles (ignoré par git)
├── scripts/                    # Scripts d'extraction, conversion et KB
│   ├── fetch_urls.py           # Extraction des URLs des fiches
│   ├── download_raw_data.py    # Téléchargement et conversion en markdown
│   ├── build_knowledge_base.py # Construction du knowledge graph
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

- **Google** (10 articles) - Infrastructure, outils, recherche
- **Anthropic** (9 articles) - Claude, sécurité, mesure de biais
- **Ethan Mollick** (8 articles) - Adoption IA, productivité, stratégie
- **OpenAI** (4 articles) - Modèles, recherche
- **Martin Fowler** (2 articles) - Ingénierie logicielle, LLMs
- **Tony Seale** (2 articles) - Knowledge graphs, ontologie, agent sémantique
- **Stanford** (2 articles) - Recherche académique
- **Alistair Gray** (2 articles) - Stripe Minions, agents de codage
- **Lee Robinson** (2 articles) - Développement web, Vercel
- **Kent Beck** (2 articles) - TDD, qualité, craftsmanship
- **Jesse Vincent** (2 articles) - Méthodologie agents de codage

## Knowledge Base

Le dépôt intègre un knowledge graph construit automatiquement à partir des sections `GrapheDeConnaissance` de chaque fiche :

- **1431 entités** typées (PERSONNE, ORGANISATION, TECHNOLOGIE, CONCEPT, METHODOLOGIE, EVENEMENT, LIEU, DOCUMENT)
- **2731 triples** relationnels
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

- **215 fiches** analysées
- **Période** : Décembre 1975 - Avril 2026
- **1431 entités** et **2731 triples** dans la knowledge base
- **11 thématiques** principales
- **60+ auteurs** suivis
- **60+ sources** documentées

## Liens utiles

- [Index complet](index.md) - Toutes les fiches organisées
- [Knowledge Base](knowledge-base.md) - Dashboard entités et triples
- [CLAUDE.md](CLAUDE.md) - Instructions pour Claude Code
- [Synthèse Juillet-Octobre 2025](SYNTHESE-JUILLET-OCTOBRE-2025.md)

## Licence

Documentation personnelle à usage interne.

---

**Dernière mise à jour** : Avril 2026
