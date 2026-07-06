# Ontologie du GrapheDeConnaissance — référence complète

> Déplacé depuis `CLAUDE.md` (U7, plan scalabilité 1000 fiches) pour alléger
> le contexte de session. **À lire avant de créer, linter ou modifier une fiche.**
> Le gate Bronze (`scripts/lint_fiches.py`) valide mécaniquement le registre
> fermé des prédicats et les vocabulaires de types ; cette référence porte la
> sémantique (désambiguïsation, exemples) que le lint ne peut pas vérifier.

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
