# Structure d'analyse d'article pour la veille

## Organisation des fichiers

Les fiches de veille sont organisées dans des répertoires par mois de **publication** (et non par date de lecture) :

```
veille/
├── index.md                    # Index général avec liens vers toutes les fiches
├── fiches/
│   ├── 2025-08/               # Articles publiés en août 2025
│   ├── 2025-09/               # Articles publiés en septembre 2025
│   └── 2025-10/               # Articles publiés en octobre 2025
└── docs/                      # (ignoré par git)
```

Chaque fiche est un fichier markdown individuel nommé selon son identifiant technique.

## Format standardisé d'une fiche

Chaque fiche suit ce format :

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

## Langue de rédaction

**IMPORTANT : Toutes les fiches doivent être rédigées intégralement en français.**

Cela inclut :
- Les résumés (RésuméDe400mots)
- Les pense-bêtes
- Le ton of voice (Ton)
- Les keywords
- Le graphe de connaissance (GrapheDeConnaissance) : types, prédicats, en-têtes de tableau
- Toutes les sections de la fiche

Seuls les éléments suivants peuvent rester dans leur langue d'origine :
- Le titre original de l'article (Titre Article)
- L'URL
- Les noms d'auteurs

## Description des sections

- **Identifiant Technique** : Identifiant unique pour l'article (utilisé comme nom de fichier)
- **Veille** : Compression synthétique du titre de l'article, des keywords et du domaine du site (en français)
- **Titre Article** : Titre original de l'article (langue source)
- **Date** : Date de publication au format ISO (YYYY-MM-DD) - détermine le répertoire de stockage
- **URL** : Lien vers l'article source
- **Keywords** : Mots-clés associés à l'article (en français)
- **Authors** : Auteur(s) de l'article
- **Ton** : Analyse du ton et du style de l'article, incluant le profil (perspective narrative, registre, niveau technique) et une description détaillée du style d'écriture, des métaphores utilisées, de l'autorité de l'auteur et du public cible (en français)
- **Pense-betes** : Notes et remarques importantes (format liste à puces, en français)
- **RésuméDe400mots** : Résumé de l'article en 400 mots maximum (en français)
- **GrapheDeConnaissance** : Extraction structurée des entités et relations clés de l'article sous forme de triples (sujet, prédicat, objet). Contient deux sous-sections : `### Triples` (tableau des relations) et `### Entités` (tableau des entités avec attributs). Voir section dédiée ci-dessous pour le format complet.

## Section GrapheDeConnaissance — Format détaillé

La section `## GrapheDeConnaissance` est la 10e et dernière section de chaque fiche. Elle capture les entités et relations clés de l'article sous forme de knowledge graph structuré.

### Sous-section `### Triples`

Tableau markdown avec 8 colonnes :

```markdown
### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Boris Cherny | PERSONNE | a_créé | Claude Code | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | prompt caching | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Boris Cherny | PERSONNE | 0.97 | DYNAMIQUE | déclaré_article |
| Demande latente | CONCEPT | guide | développement produit | CONCEPT | 0.90 | ATEMPOREL | inféré |
```

### Sous-section `### Entités`

Tableau markdown avec 5 colonnes :

```markdown
### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Boris Cherny | PERSONNE | rôle | Créateur Claude Code | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
```

### Types d'entités

| Type | Description | Exemples |
|------|-------------|----------|
| `PERSONNE` | Individu nommé | Boris Cherny, Ethan Mollick, Marc Andreessen |
| `ORGANISATION` | Entreprise, labo, institution | Anthropic, Google, Y Combinator, Stanford |
| `TECHNOLOGIE` | Outil, framework, plateforme, langage | Claude Code, MCP, TypeScript, React |
| `CONCEPT` | Idée, principe, pattern | Demande latente, Bitter Lesson, prompt caching |
| `METHODOLOGIE` | Approche, workflow, pratique | Vibe coding, Plan mode, Compounding Engineering |
| `EVENEMENT` | Publication, annonce, incident | Opus 4.5 launch, 2026 Agentic Coding Report |
| `LIEU` | Localisation géographique | Silicon Valley, France, Japon |

### Types temporels

| Type | Quand l'utiliser | Exemple |
|------|-----------------|---------|
| `STATIQUE` | Fait ponctuel, ne change pas | "a publié en 2026", "a été fondé en 2021" |
| `DYNAMIQUE` | Fait qui peut évoluer | "travaille chez Anthropic", "utilise VS Code" |
| `ATEMPOREL` | Vérité générale, principe | "le cache fonctionne par préfixe" |

### Types de source

| Type | Description |
|------|-------------|
| `déclaré_article` | Fait explicitement énoncé dans l'article |
| `inféré` | Relation déduite du contexte de l'article |
| `généré_assistant` | Relation ajoutée par Claude pour enrichir le contexte |

### Actions (Entités)

| Action | Quand l'utiliser |
|--------|-----------------|
| `AJOUT` | Nouvelle entité ou attribut identifié (cas standard) |
| `MISE_A_JOUR` | L'article corrige une information connue |
| `INVALIDATION` | L'article contredit une information connue |

### Règles d'extraction

- **Seuil de confiance minimum** : 0.70 — Les triples en dessous ne sont pas inclus
- **Nombre cible** : 5 à 15 triples par fiche (ajuster selon la densité de l'article)
- **Prédicats en français**, sous forme verbale courte (1-3 mots) : `a_créé`, `utilise`, `emploie`, `publie`, `critique`, `recommande`, `transforme`, `remplace`, `améliore`, `réduit`, `augmente`, `affirme_que`, `prédit`, `contredit`, `s_oppose_à`, `fait_partie_de`, `est_basé_sur`, `collabore_avec`
- **Prédicats épistémiques** (`affirme_que`, `prédit`, `recommande`) pour distinguer les faits des opinions
- **Noms d'entités** : restent dans leur langue d'origine (comme pour Authors)
- **Tout le reste en français** : types, en-têtes de tableau, prédicats
- Privilégier les relations **structurantes** (qui relient des entités majeures) aux relations anecdotiques

## Workflow d'ajout d'un nouvel article

1. **Extraire les informations** de l'article source
2. **Créer un identifiant technique** descriptif (ex: `nom-auteur-sujet-YYYY-MM-DD`)
3. **Créer le fichier** dans le répertoire correspondant au mois de publication : `fiches/YYYY-MM/identifiant.md`
4. **Remplir toutes les sections** selon le format standardisé
5. **Sauvegarder le contenu brut** dans `raw-data/` (voir section suivante)
6. **Mettre à jour `index.md`** (voir section plus bas)

## Gestion des données brutes (raw-data)

**IMPORTANT : Pour chaque article ajouté, le contenu brut de l'URL source doit être sauvegardé dans le répertoire `raw-data/`.**

### Objectif
Conserver le texte original des articles au format markdown pour :
- Permettre des analyses futures du contenu source
- Faciliter la vérification et mise à jour des fiches
- Archiver le contenu en cas de disparition de l'article source

### Structure
```
veille/
├── raw-data/                          # Contenus bruts des articles (ignoré par git)
│   ├── identifiant-article-1.md      # Format: {identifiant}.md
│   └── identifiant-article-2.md
├── scripts/                           # Scripts d'extraction et conversion
│   ├── fetch_urls.py                 # Extraction des URLs des fiches
│   └── download_raw_data.py          # Téléchargement et conversion en MD
└── fiches/                            # Fiches d'analyse
```

### Workflow de sauvegarde du contenu brut

#### 1. Vérifier la configuration

**Avant toute opération, vérifier que :**

- [ ] Le répertoire `raw-data/` existe (le créer si nécessaire : `mkdir raw-data`)
- [ ] `raw-data/` est bien dans le `.gitignore`
- [ ] Les scripts sont disponibles dans `scripts/`

```bash
# Vérifier .gitignore
grep "raw-data/" .gitignore

# Si absent, ajouter :
echo "# Raw data from article URLs" >> .gitignore
echo "raw-data/" >> .gitignore
```

#### 2. Sauvegarder le contenu brut lors de l'ajout d'une fiche

**Deux méthodes possibles :**

**Méthode A : Automatique (pour tous les articles)**
```bash
# Depuis la racine du projet
python3 scripts/fetch_urls.py        # Extrait toutes les URLs
python3 scripts/download_raw_data.py # Télécharge et convertit
```

**Méthode B : Manuel (pour un article spécifique)**
```bash
# Télécharger et convertir avec curl + lynx
curl -sL "URL_ARTICLE" | lynx -dump -stdin -nolist > raw-data/identifiant-article.md
```

#### 3. Format du fichier brut

Chaque fichier dans `raw-data/` doit :
- Porter le même nom que l'identifiant de la fiche : `{identifiant}.md`
- Contenir le contenu en markdown converti depuis le HTML
- Inclure en en-tête : l'identifiant et l'URL source

**Exemple de structure :**
```markdown
# identifiant-article-2025-11-05

**URL:** https://example.com/article

---

[Contenu converti en markdown]
```

### Notes importantes

- ⚠️ **Le répertoire `raw-data/` est ignoré par git** : les contenus ne sont pas versionnés
- 📦 **Taille** : Prévoir ~100-500 Ko par article en moyenne
- 🔄 **Mise à jour** : Relancer `download_raw_data.py` pour récupérer les articles manquants
- ❌ **Exclusions** : Certains domaines peuvent être exclus (ex: yahoo.com)

## Mise à jour de index.md

Le fichier `index.md` est l'index principal qui référence toutes les fiches. Il doit être mis à jour à chaque ajout d'article.

### Structure de index.md

```markdown
# Veille Technologique

## Articles par date de publication
### [Mois] [Année]
- **[YYYY-MM-DD]** [Titre](fiches/YYYY-MM/identifiant.md) - Description courte - Source

## Thématiques
### [Nom de la thématique]
- [Titre](fiches/YYYY-MM/identifiant.md) - Auteur

## Statistiques
- **Total d'articles** : XX
- **Période couverte** : [Période]
- **Principaux auteurs** : [Liste]
- **Sources principales** : [Liste]
```

### Étapes de mise à jour

#### 1. Ajouter dans la section "Articles par date de publication"

**Position** : Insérer l'article dans l'ordre chronologique **décroissant** (plus récent en premier) dans le mois approprié.

**Format** :
```markdown
- **[YYYY-MM-DD]** [Titre court et descriptif](fiches/YYYY-MM/identifiant.md) - Description en quelques mots - Source
```

**Exemple** :
```markdown
### Octobre 2025
- **[2025-10-15]** [Nouvelle architecture agents IA](fiches/2025-10/nouvelle-architecture-agents-2025-10-15.md) - Design patterns émergents - TechBlog
- **[2025-10-11]** [Intelligence Artificielle et monopsychisme](fiches/2025-10/ia-monopsychisme-serres-averroes-aquin-2025-10-11.md) - Philosophie médiévale/moderne - Revue Thomiste
```

**Note** : Si le mois n'existe pas encore, créer une nouvelle section avec le titre `### [Mois] [Année]`.

#### 2. Ajouter dans la section "Thématiques"

**Identifier la thématique** : Choisir la catégorie la plus appropriée parmi :
- Agents de codage IA & Skills
- Architecture & Construction
- Transformation & Adoption
- Qualité & Sécurité
- Économie & Marché
- Philosophie & Société
- *(Créer une nouvelle thématique si nécessaire)*

**Format** :
```markdown
- [Titre court](fiches/YYYY-MM/identifiant.md) - Auteur ou source
```

**Position** : Ajouter à la fin de la liste de la thématique appropriée.

**Exemple** :
```markdown
### Agents de codage IA & Skills
- [Méthodologie agents de codage IA](fiches/2025-10/coding-agents-methodology-vincent-2025-10-05.md) - Jesse Vincent
- [Nouvelle architecture agents IA](fiches/2025-10/nouvelle-architecture-agents-2025-10-15.md) - Jane Doe
```

#### 3. Mettre à jour les statistiques

**Incrémenter le total** : Ajouter +1 au nombre total d'articles

**Mettre à jour la période** : Ajuster si nécessaire (ex: "Août - Octobre 2025" → "Août - Novembre 2025")

**Actualiser les auteurs** : Ajouter l'auteur s'il apparaît pour la première fois ou incrémenter son compteur

**Actualiser les sources** : Ajouter la source si elle est nouvelle

**Exemple** :
```markdown
## Statistiques

- **Total d'articles** : 16  ← était 15
- **Période couverte** : Août - Octobre 2025
- **Principaux auteurs** : Jesse Vincent (2), Jane Doe (1), Simon Willison (1), Martin Fowler (1)
- **Sources principales** : LinkedIn, Blogs techniques, Recherche Anthropic, Google Cloud, TechBlog
```

### Checklist de mise à jour

- [ ] Article ajouté dans "Articles par date de publication" (ordre chronologique décroissant)
- [ ] Article ajouté dans la thématique appropriée
- [ ] Total d'articles incrémenté
- [ ] Période couverte actualisée si nécessaire
- [ ] Auteur ajouté ou compteur incrémenté
- [ ] Source ajoutée si nouvelle
- [ ] Liens vérifiés (format `fiches/YYYY-MM/identifiant.md`)
- [ ] Orthographe et formatage vérifiés

### Conventions de nommage dans index.md

**Titres** : Courts et descriptifs (max 60 caractères), éviter les sous-titres

**Descriptions** : 3-5 mots clés séparés par tirets, décrivant le contenu principal

**Sources** : Nom court reconnaissable (ex: "LinkedIn", "Pragmatic Engineer", "Revue Thomiste")

**Thématiques** : Utiliser les catégories existantes en priorité, ne créer une nouvelle catégorie que si vraiment nécessaire

---

## Frontmatter de promotion vers le référentiel transverse cabinet (v3, 2026-04-30)

> Section ajoutée par le plan ATransverse v3 — Unit 4. Voir
> `ATransverse/docs/plans/2026-04-29-001-feat-pipeline-capitalisation-v3.1-plan.md`
> et `ATransverse/docs/architecture/2026-04-29-architecture-pipeline-capitalisation-v3.1.md` § 8.

Une fiche peut être marquée comme **candidate à promotion** vers le référentiel transverse cabinet (ATransverse) via l'ajout d'un bloc YAML frontmatter en tête de fichier :

```yaml
---
cabinet_promotion_candidate: true
proposed_class: Concept            # Concept | Pattern | Framework | BenchmarkDatapoint
proposed_capability: capability/software-factory
notes: "Aligne avec ce qu'on observe chez 3 clients"
---
# <Identifiant Technique>

## Veille
…
```

Le frontmatter est **optionnel** : seules les fiches candidates en sont enrichies. Une fiche sans frontmatter reste une fiche valide.

### Compatibilité — patch obligatoire de `extract_fiche_veille()`

`scripts/build_knowledge_base.py` :: `extract_fiche_veille()` a été patché pour ignorer un éventuel bloc YAML frontmatter en tête. **Ne pas régresser ce patch** — sans skip, la première ligne non-`#` retournée serait `---`, ce qui produirait un alias incorrect pour toutes les fiches portant un frontmatter.

Test de régression : `scripts/tests/test_frontmatter_compat.py` (7 tests, à conserver verts).

### Workflow Pont V

1. À l'ajout d'une fiche jugée candidate à promotion, enrichir le frontmatter avec les 4 champs ci-dessus (cf. `ATransverse/docs/templates-drafts/atransverse/concept.md` ou autre template selon `proposed_class`).
2. Optionnellement, ajouter une entrée détaillée dans `_capitalization/to-transverse.md` à la racine de ce dépôt.
3. Le Lab transverse parcourt le `_capitalization/to-transverse.md` en revue mensuelle (cf. `ATransverse/docs/governance-drafts/lab-charter.md`) et tranche promote / clarification_needed / reject.
4. Si `promote` : un asset transverse est créé dans `ATransverse/00-raw/from-pont-v/` avec `references_external` pointant vers le `fiche_id` ici.

### Anti-patterns

- **Modifier l'identifiant de la fiche après marquage** : casse la traçabilité du `fiche_id` côté transverse.
- **Réutiliser le frontmatter pour autre chose que la promotion cabinet** : si le besoin émerge, ajouter une nouvelle convention sans casser celle-ci (cf. `ontology/ontology.yaml` côté ATransverse pour le schéma autoritaire).
