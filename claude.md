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
├── gold/                      # Livrables générés + prompts (ignoré par git)
└── docs/                      # Brouillons & plans internes (sous-dossiers ignorés par git)
    └── solutions/             # Learnings versionnés : solutions à des problèmes passés (bugs,
                               #   conventions, workflow), par catégorie + frontmatter YAML
                               #   (module, tags, problem_type) — pertinent avant d'implémenter
                               #   ou de déboguer dans une zone documentée
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
| `TECHNOLOGIE` | Outil, framework, plateforme, langage, produit | Claude Code, MCP, TypeScript, React |
| `CONCEPT` | Idée, principe, pattern (PAS une proposition, un chiffre ou une citation — voir types épistémiques) | Demande latente, Bitter Lesson, prompt caching |
| `METHODOLOGIE` | Pratique actionnable avec des étapes/un workflow | Vibe coding, Plan mode, Compounding Engineering |
| `EVENEMENT` | Publication, annonce, incident | Opus 4.5 launch, 2026 Agentic Coding Report |
| `LIEU` | Localisation géographique (usage gelé : préférer un attribut d'entité ; ne créer une entité LIEU que si elle structure l'article) | Silicon Valley, France, Japon |
| `DOCUMENT` | Rapport, livre, étude, publication citée comme objet | AI Index Report 2025, DORA Report |

### Types épistémiques (objets de triples uniquement)

Quand l'objet d'un triple épistémique (`affirme_que`, `prédit`, `mesure`, `recommande`) n'est **pas une entité existante** mais une proposition, un chiffre ou un verbatim, le typer ainsi (au lieu de CONCEPT) :

| Type | Capture | Exemple d'objet |
|------|---------|-----------------|
| `AFFIRMATION` | Proposition complète affirmée par une source | "IA effectue 30-50% du travail chez Salesforce" |
| `MESURE` | Point de mesure chiffré, daté, périssable | "727% ROI sur 3 ans" |
| `CITATION` | Verbatim significatif (entre guillemets) | "Billable hours are dead" |

**Règles** : ces objets n'apparaissent **jamais** dans la table `### Entités` (ce ne sont pas des entités) et ne sont jamais sujets d'un triple. Si l'objet correspond à une entité existante du graphe, utiliser l'entité.

### Règles de désambiguïsation des types

- **ORGANISATION vs TECHNOLOGIE** (entreprises-produits : Cursor, Replit, Perplexity, GitHub, Manus…) : typer selon le **rôle dans la relation** — qui agit (lève des fonds, annonce, recrute) = ORGANISATION ; ce qui est utilisé/intégré/comparé = TECHNOLOGIE.
- **CONCEPT vs METHODOLOGIE** : METHODOLOGIE = pratique actionnable (on peut la suivre, elle a des étapes) ; CONCEPT = idée ou principe (on peut y adhérer). `Vibe coding`, `Compound Engineering`, `Plan mode`, `Context engineering` → METHODOLOGIE.
- **Familles génériques IA** : `IA`, `agents IA`, `IA générative`, `IA agentique` → TECHNOLOGIE (jamais CONCEPT).
- **Versions de produits** : préférer l'entité produit stable (ex. `Claude Opus`) avec la version en attribut ou via `est_variante_de`/`remplace` entre releases, plutôt qu'une entité par numéro de version.

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

### Registre fermé des prédicats (30)

**Le vocabulaire des prédicats est FERMÉ.** Tout triple doit utiliser un prédicat de ce registre (aligné sur l'ontologie ATransverse v5, annexe D). Si aucun prédicat ne convient, choisir le plus proche ; ne jamais en inventer un nouveau.

| Famille | Prédicats | Équivalent v5 |
|---------|-----------|---------------|
| **Structurels** (5) | `fait_partie_de`, `est_instance_de`, `est_variante_de`, `remplace`, `publie` | partOf, instanceOf, variantOf, supersedes, releases |
| **Épistémiques** (9) | `affirme_que`, `soutient`, `s_oppose_à`, `affine`, `prédit`, `mesure`, `est_basé_sur`, `s_inspire_de`, `référence` | claims, supports, contradicts, refines, predicts, measures, derivedFrom, informedBy, referencesExternal |
| **Opérationnels** (8) | `utilise`, `permet`, `améliore`, `réduit`, `résout`, `s_applique_à`, `observé_dans`, `recommande` | uses, enables, improves, reduces, solves, appliesTo, observedIn, recommends |
| **Marché** (5) | `concurrence`, `surpasse`, `converge_avec`, `collabore_avec`, `a_créé` | competesWith, outperforms, convergesWith, partneredWith, created |
| **Personnes** (3) | `travaille_chez`, `dirige`, `emploie` | (spécifique veille — PERSONNE conservé) |

**Table de normalisation des prédicats hérités** (anciens → canoniques) :

| Anciens prédicats | Canonique |
|-------------------|-----------|
| `intègre`, `supporte`, `emploie` (objet non-PERSONNE), `requiert` | `utilise` |
| `a_développé`, `développe`, `crée`, `a_construit` | `a_créé` |
| `propose`, `préconise` | `recommande` |
| `a_publié`, `a_lancé`, `lance`, `sort` | `publie` |
| `augmente`, `accélère`, `optimise`, `transforme` (amélioration) | `améliore` |
| `génère`, `produit`, `fournit`, `offre`, `transforme` (capacité nouvelle) | `permet` |
| `contredit`, `critique`, `conteste` | `s_oppose_à` |
| `atteint` | `mesure` |
| `définit`, `représente`, `est` (proposition) | `affirme_que` |
| `est` (catégorisation : "X est un Y") | `est_instance_de` |
| `concurrence avec`, `rivalise_avec` | `concurrence` |

### Règles d'extraction

- **Seuil de confiance minimum** : 0.70 — Les triples en dessous ne sont pas inclus
- **Nombre cible** : 5 à 15 triples par fiche (ajuster selon la densité de l'article)
- **Prédicats** : uniquement issus du registre fermé ci-dessus
- **Prédicats épistémiques** (`affirme_que`, `prédit`, `recommande`, `mesure`) pour distinguer les faits des opinions ; leurs objets non-entités sont typés `AFFIRMATION`/`MESURE`/`CITATION`
- **Noms d'entités** : restent dans leur langue d'origine (comme pour Authors)
- **Tout le reste en français** : types, en-têtes de tableau, prédicats
- Privilégier les relations **structurantes** (qui relient des entités majeures) aux relations anecdotiques
- **En-tête du tableau Triples** : exactement `| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |` (avec l'accent sur `Prédicat`)

## Fiches de Skills (format spécial)

Une **skill** (capacité réutilisable décrite par un `SKILL.md`, ex. les skills Claude Code / agents) n'est **pas** un article : sa valeur tient dans son **fonctionnement réutilisable**, pas dans une opinion datée. Les fiches de skills suivent donc un format dérivé, **compatible avec le pipeline** (gate Bronze + `build_knowledge_base.py`) : on conserve les **10 sections canoniques dans l'ordre** et on **insère un bloc Skill** de 4 sections juste avant `## GrapheDeConnaissance` (qui reste 10ᵉ et dernière).

### Marqueur frontmatter

En tête de fiche (le frontmatter est ignoré par le lint et le build) :

```yaml
---
fiche_type: skill
skill_source: github.com/owner/repo        # dépôt / origine de la skill
skill_author: Nom Auteur
---
```

### Réinterprétation des sections canoniques

| Section canonique | Sens pour une skill |
|-------------------|---------------------|
| `Titre Article` | Nom de la skill + sa description `SKILL.md` |
| `Date` | **Date d'observation/ajout** (une skill est un artefact *vivant*, pas une publication datée) — détermine quand même le répertoire `fiches/YYYY-MM/` |
| `URL` | Lien vers le `SKILL.md` |
| `Authors` | Auteur(s) de la skill |
| `Ton` | **Registre opérationnel** que la skill impose à l'agent (voix, posture, métaphores) |
| Les autres (`Veille`, `Keywords`, `Pense-betes`, `RésuméDe400mots`, `GrapheDeConnaissance`) | inchangées |

### Bloc Skill (6 sections, inséré avant `## GrapheDeConnaissance`)

- `## Commentaire` — **explication pédagogique en prose** (« comment ça marche », à hauteur d'humain) : *en une phrase*, l'idée centrale, les principes, et un *en résumé*. C'est la section qui fait comprendre la skill d'un coup d'œil ; elle complète (et précède) les sections structurées. *(à ne pas omettre)*
- `## Lecture commentée du SKILL.md` — **annotation quasi ligne-à-ligne du source** : extraits **verbatim** du `SKILL.md` (frontmatter `name`/`description`, blocs structurants — ex. balises XML `<what-to-do>`/`<supporting-info>` —, chaque règle) + glose en français, et une note sur les **choix de design** (pattern de prompting, modularisation par fichiers annexes). Donne à voir *comment la skill est construite*, pas seulement ce qu'elle fait.
- `## Déclencheur` — quand la skill s'active (*when to use* / trigger) et ses entrées attendues.
- `## Fonctionnement` — le **mécanisme** structuré : la boucle, les principes, le workflow pas-à-pas. *(section cœur)*
- `## Artefacts` — fichiers/sorties produits par la skill (ex. `CONTEXT.md`, `docs/adr/`) et où.
- `## Anti-patterns` — quand **ne pas** l'utiliser, pièges et limites.

### Conventions

- **Identifiant** : préfixe `skill-` (ex. `skill-pocock-grill-with-docs-2026-06`).
- **KB dédiée** : les fiches de skills alimentent **`kb-skills.md`** (KB thématique curée, comme `kb-context-engineering.md` / `kb-commerce-agentique.md`). À tenir à jour à l'ajout d'une fiche de skill.
- **GrapheDeConnaissance** : une skill est typée `METHODOLOGIE` ; ses artefacts (`CONTEXT.md`, ADR…) sont `DOCUMENT`.

Exemple de référence : `fiches/2026-06/skill-pocock-grill-with-docs-2026-06.md`.

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

---

## Architecture médaillon (2026-06-11)

> Section ajoutée par le plan `docs/plans/2026-06-11-001-feat-architecture-medaillon-veille-plan.md`.
> Le médaillon est **logique** : il documente la correspondance étage → répertoire existant.
> **Aucun répertoire n'est renommé** (ATransverse3 consomme ce dépôt en sous-module lecture
> seule ; les liens d'`index.md` et les wikilinks Obsidian dépendent des chemins actuels).

### Correspondance des étages

| Étage | Répertoire(s) | Versionné | Gate / promotion |
|-------|---------------|-----------|------------------|
| **Raw** | `raw-data/` | Non (gitignoré) | — (contenu brut `curl` + `lynx`) |
| **Bronze** | `fiches/` | **Oui** | `python3 scripts/lint_fiches.py` (validation ontologie v2, bloquante) |
| **Silver** | `kb/`, `knowledge-base.md`, `kb-*.md` | **Oui** | `python3 scripts/build_knowledge_base.py` (promotion Bronze → Silver) |
| **Gold** | `gold/` (livrables + `gold/prompts/`) | Non (gitignoré) | checklist qualité des prompts de `gold/prompts/` |

### Workflow Gold

1. **Sélectionner les fiches sources** (et/ou une KB spécialisée) pour le livrable.
2. **Charger le prompt de la famille** dans `gold/prompts/` : `slides-sharp-artisan.md`
   (deck HTML 16:9), `rapport-html.md` (rapport long-form), `export-pptx.md` (conversion pptx).
3. **Générer le livrable dans `gold/`** avec l'en-tête de provenance obligatoire
   (commentaire HTML listant les `fiches/YYYY-MM/id.md` sources, la date et le prompt).
4. Valider avec la checklist qualité du prompt avant livraison.

### Anti-patterns

- **Ne jamais versionner `gold/`** ni y placer du contenu NDA différé au cabinet : le dépôt
  est public et les HTML inlinent le CSS Sharp Artisan (`_design-system/`, actif éditorial exclu).
- **Ne pas renommer les répertoires-étages** (`raw-data/`, `fiches/`, `kb/`) : le médaillon
  est documentaire, pas physique.
- **Ne pas committer de livrable dans `docs/`** : `docs/report/` a été supprimé (2026-06-12),
  `gold/` est la seule destination des livrables générés.

Test de régression du gate Bronze : `scripts/tests/test_lint_fiches.py` (à conserver vert,
avec `scripts/tests/test_frontmatter_compat.py`).
