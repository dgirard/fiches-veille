# Veille Technologique

Documentation personnelle de veille technologique sur l'intelligence artificielle, les agents de codage, et l'évolution du développement logiciel.

## 📋 Vue d'ensemble

Ce dépôt contient une collection de fiches d'analyse d'articles techniques, organisées par mois de publication et classées par thématiques. L'objectif est de suivre l'évolution rapide de l'écosystème IA et son impact sur l'ingénierie logicielle.

**Période couverte** : Juin 2023 - Novembre 2025
**Total d'articles** : 114 fiches

## 📁 Structure du projet

```
fiches-veille/
├── index.md                    # Index principal avec liens vers toutes les fiches
├── fiches/                     # Fiches organisées par mois de publication
│   ├── 2023-06/
│   ├── 2024-04/
│   ├── 2024-07/
│   ├── 2024-10/
│   ├── 2025-01/ à 2025-11/
├── docs/                       # Documentation et analyses complémentaires
├── raw-data/                   # Contenu brut des articles (ignoré par git)
├── scripts/                    # Scripts d'extraction et conversion
│   ├── fetch_urls.py          # Extraction des URLs
│   └── download_raw_data.py   # Téléchargement contenu brut
├── mobile-share/              # URLs collectées depuis mobile
├── CLAUDE.md                  # Instructions pour Claude Code
├── gemini.md                  # Instructions pour Gemini
└── urls-to-process.md         # URLs en attente de traitement
```

## 🎯 Thématiques principales

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

## 📝 Format des fiches

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
```

**Langue** : Toutes les fiches sont rédigées en français (sauf titre original et noms d'auteurs).

## 🔍 Principales sources

- **Blogs techniques** : One Useful Thing (Ethan Mollick), Pragmatic Engineer, RedMonk
- **Organisations** : Anthropic, Google, Stanford, a16z, DeepMind, OpenAI
- **Plateformes** : LinkedIn, Medium, GitHub, YouTube
- **Recherche** : Harvard Business Review, Wharton, METR, Apollo Academy
- **Entreprises** : HubSpot, Block/Square, Netflix, Xebia

## 👥 Auteurs principaux suivis

- **Ethan Mollick** (6 articles) - Adoption IA, productivité, stratégie
- **Google** (6 articles) - Infrastructure, outils, recherche
- **Anthropic** (6 articles) - Claude, sécurité, mesure de biais
- **Kent Beck** (2 articles) - TDD, qualité, craftsmanship
- **Jesse Vincent** (2 articles) - Méthodologie agents de codage
- **Simon Willison** (2 articles) - Skills, MCP
- **Kieran Klaassen** (2 articles) - Planning, engineering compounding
- **Cobus Greyling** (2 articles) - Écosystème IA, coûts

## 🚀 Workflow d'ajout d'article

1. **Ajouter l'URL** dans `urls-to-process.md` ou `mobile-share/`
2. **Créer la fiche** dans `fiches/YYYY-MM/identifiant.md`
3. **Sauvegarder le contenu brut** dans `raw-data/identifiant.md`
4. **Mettre à jour `index.md`** :
   - Section "Articles par date de publication"
   - Section "Thématiques" appropriée
   - Statistiques (total, auteurs, sources)

Voir [CLAUDE.md](CLAUDE.md) pour les instructions détaillées.

## 🛠️ Scripts utiles

```bash
# Extraire toutes les URLs des fiches
python3 scripts/fetch_urls.py

# Télécharger et convertir le contenu brut
python3 scripts/download_raw_data.py

# Vérifier les fiches manquantes
python3 scripts/check_missing.py
```

## 📊 Statistiques actuelles

- **114 articles** analysés
- **Période** : Juin 2023 - Novembre 2025
- **~40 auteurs** différents suivis
- **~50 sources** documentées
- **8 thématiques** principales

## 🔗 Liens utiles

- [Index complet](index.md) - Toutes les fiches organisées
- [CLAUDE.md](claude.md) - Instructions pour Claude Code
- [Synthèse Juillet-Octobre 2025](SYNTHESE-JUILLET-OCTOBRE-2025.md)

## 📜 Licence

Documentation personnelle à usage interne.

---

**Dernière mise à jour** : Novembre 2025
