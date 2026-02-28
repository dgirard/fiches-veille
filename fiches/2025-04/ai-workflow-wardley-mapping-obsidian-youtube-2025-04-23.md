# ai-workflow-wardley-mapping-obsidian-youtube-2025-04-23

## Veille
Workflow IA pour générer Wardley Maps, LLM prompts capabilities, Obsidian graph, NetworkX clustering, bootstrap stratégique - Tutoriel vidéo

## Titre Article
AI Workflow for Creating Wardley Maps (Video Tutorial)

## Date
2025-04-23

## URL
https://www.youtube.com/watch?v=uU1fSE0piXM

## Keywords
Wardley Mapping automation, LLM prompts, capability decomposition, OpenAI API, Obsidian canvas, NetworkX clustering, value chain y-axis, graph relationships, strategic bootstrap, JSON output, capability relationships, proximity categorization, operational excellence

## Authors
Auteur vidéo (Product Manager ERP/Business Intelligence)

## Ton
**Profil:** Tutorial-Practitioner | Première personne educator | Pédagogique-Démonstrative | Intermédiaire-Expert

PM/BI practitioner adopte YouTube tutorial voice combinant hands-on demonstration et conceptual explanation. Langage technical accessible (LLM prompts, Obsidian canvas, NetworkX clustering) guides viewers through workflow. Format vidéo allows visual demonstration complex automation process. Tone enthusiastic practitioner sharing discovered workflow rather than authoritative expert. Structure tutorial typical (problem→solution→implementation) facilitates learning. Typique practitioner YouTube channels partageant personal workflows et discoveries visant fellow practitioners curious automation strategic thinking tools.

## Pense-betes
- **Objectif** : utiliser IA pour bootstrapper Wardley Map, obtenir bon point départ rapidement
- **Outil stack** : OpenAI API + Obsidian + Python NetworkX + custom frontend
- **Prompt 1 - Capabilities** : "I'm product manager for [product]. Frame capabilities as 'the ability to [blank]'. Break down using 'is a function of the ability to'. Return JSON."
- **Exemple capability** : "buy lunch for team" → décomposé en plan balanced meals, source quality ingredients, efficient meal preparation, adapt to preferences/allergies
- **Obsidian integration** : capabilities dropped into Obsidian, relationships automatiquement linkées (parent→subcapabilities)
- **Axe Y Wardley** : plus haut = closer to customer, plus bas = abstracted/invisible from customer
- **Prompt 2 - Y-axis positioning** : categorize capabilities based on proximity to different roles (operational excellence leaders → COO → strategic program managers → coaches/designers → operations/IT engineers → platform/data engineers → infrastructure/utility layers)
- **Toujours demander rationale** : "assign level + give rationale" permet tuning, "get into thinking of LLM"
- **Prompt 3 - Relationships** : "identify meaningful relationships: functionally similar OR enabling capabilities. Return JSON with pair (two related IDs) + type (similar/enables) + clear explanation"
- **Scanning aléatoire** : insert capabilities at random, strict analysis, comme "scanner board et tracer lignes entre similaires"
- **Exemple relationship** : "analyze data insights" ↔ "trend analysis" = similar (both focus on analyzing data to derive insights)
- **NetworkX clustering** : Python library pour social network graph analysis, identify clusters within each level
- **Canvas final** : capabilities organisées par level (Y-axis) + cluster (X-axis approximation), grouping feature Obsidian
- **Navigation value chain** : example "leader wants prioritization" → go down stack → find different things involved
- **Bootstrap not endpoint** : "this is just the start, now spend time nerding out learning about space"

## RésuméDe400mots

**Objectif et Contexte Méthodologique**

Tutoriel vidéo démontrant workflow pratique utilisant IA (LLMs) pour bootstrapper création Wardley Map. Auteur, product manager domaine ERP/Business Intelligence, cherche explorer espace product-agnostic et obtenir bon point départ rapidement plutôt que partir feuille blanche. Approche reconnaît que Wardley Mapping manuel long/complexe, propose automation partielle pour accélérer phase initiale exploration stratégique.

**Architecture Technique : Stack et Outils**

Workflow repose sur **quatre composants** : **(1) OpenAI API** pour génération capabilities/relationships via prompts structurés ; **(2) Obsidian** comme outil knowledge management exploitant graph relationships natives ; **(3) Python avec NetworkX** library pour clustering analysis type social network graph ; **(4) Custom frontend** (optionnel) pour faciliter entry prompts/capabilities. Integration fluide permet passer outputs JSON LLM directement dans Obsidian, puis exports vers Python pour analysis avancée, puis re-import enriched data dans Obsidian canvas.

**Trois Prompts Séquentiels Structurés**

**Prompt 1 - Capability Decomposition** : Format strict "I'm product manager for [product] in [space]. Frame capabilities as 'the ability to [blank]'. Break down capabilities using 'insert starting capability is a function of the ability to...' Return results in JSON." Exemple concret : "buy lunch for team" (top-level capability) décomposé automatiquement en subcapabilities : plan balanced meals, source quality ingredients, efficient meal preparation, adapt to preferences/allergies. Décomposition crée **hierarchical parent→child relationships** automatiquement linkées dans Obsidian graph.

**Prompt 2 - Y-Axis Positioning** : Wardley Maps utilisent axe Y représentant proximité customer (haut = visible for customer, bas = abstracted/invisible infrastructure). Prompt catégorise capabilities based on proximity to different roles within value chain focused operational excellence : **(Level 1)** Operational excellence leaders, COO, strategic program managers ; **(Level 2)** Coaches, designers ; **(Level 3)** Operations/IT engineers ; **(Level 4)** Platform engineers, data engineers ; **(Level 5)** Infrastructure/utility layers. Cruciale : **toujours demander rationale** avec assignment level. Permet "get into thinking of LLM", facilite tuning iteratif. Auteur souligne ce prompt nécessita tuning behind scenes pour domain spécifique.

**Prompt 3 - Capability Relationships** : "Given list of capabilities (each with ID, name, description), identify meaningful relationships. Should be either functionally similar OR enabling capabilities. Be very precise. Return JSON with: pair (two related capability IDs), type (similar/enables), reason (clear explanation why related or how one enables other)." Stratégie : **insert capabilities at random**, strict analysis, comme scanner board et tracer lignes entre items similaires. Exemple output : "analyze data insights" ↔ "trend analysis" = similar (both focus analyzing data derive insights/trends) ; "analyze data insights" enables "actionable intelligence" (derives intelligence from data patterns). Augmente richness relationships au-delà simple hierarchie parent-child.

**NetworkX Clustering et Canvas Final**

Après création capabilities + hierarchical relationships + similarity/enabling relationships + Y-axis levels, workflow utilise **Python NetworkX library** (standard social network graph analysis) pour **identify clusters within each level**. Analyse connexions/relationships density comme social network, assigne cluster IDs. Résultat : chaque capability possède **(1) Y-axis level** (proximity customer), **(2) cluster ID** (regroupement logique within level), **(3) parent-child links**, **(4) similarity/enabling links avec rationales**.

Data enrichie importée **Obsidian canvas** où capabilities visualisées. Auteur utilise **grouping feature** Obsidian pour clarity. Clustering NetworkX parfois produit groupements sensés (exemple : "timestamped entries, audit trails for key actions, historical data preservation" clustered ensemble).

**Navigation Value Chain et Philosophie Bootstrap**

Canvas permet **navigation value chain** : example "leader wants prioritization" (top map) → descendre stack level by level → identifier different things involved achieving prioritization. Démonstration concrète how high-level need décompose en capabilities progressivement abstraites/infrastructure.

**Leçon Clé** : Auteur insiste **"this is just the start, just to bootstrap"**. Output IA n'est pas carte finale mais **accelerated starting point**. Intention : "now spend lot of time nerding out and learning about particular space". IA réduit friction initiale blank page, permet product manager commencer immédiatement iteration/refinement avec structure baseline solide plutôt que weeks manual mapping.

**Implications Méthodologiques**

Workflow démontre **pragmatic AI augmentation** : ni fully automated strategy (impossible given nuance/context) ni fully manual (trop lent). Hybrid approach exploite LLM strengths (pattern recognition, decomposition logique, relationship identification) tout en reconnaissant human expertise indispensable pour validation, tuning prompts (via rationales), et deep learning domain post-bootstrap. Rationales systematiques créent **feedback loop** permettant practitioner comprendre LLM reasoning, ajuster prompts iterativement, améliorer quality outputs.

**Transferability Beyond Wardley Mapping**

Bien que focalisé Wardley Maps, techniques généralisables : capability decomposition, proximity categorization, relationship identification, clustering analysis applicables autres frameworks stratégiques nécessitant structured thinking about value chains, dependencies, abstractions layers. Stack Obsidian+NetworkX+LLM API particulièrement puissante pour knowledge workers explorant complex domains.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| workflow IA Wardley | METHODOLOGIE | utilise | OpenAI API | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| workflow IA Wardley | METHODOLOGIE | utilise | Obsidian | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| workflow IA Wardley | METHODOLOGIE | utilise | NetworkX | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| NetworkX | TECHNOLOGIE | permet | clustering de graphe de capacités | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Obsidian | TECHNOLOGIE | visualise | relations parent-enfant de capacités | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Wardley Map | METHODOLOGIE | utilise | axe Y basé sur proximité client | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| LLM | TECHNOLOGIE | accélère | bootstrapping de cartographie stratégique | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| décomposition de capacités | METHODOLOGIE | produit | hierarchie parent-enfant en JSON | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| rationale de prompt | CONCEPT | améliore | qualité des outputs LLM | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| workflow IA Wardley | METHODOLOGIE | s_applique_à | product managers ERP/BI | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| workflow IA Wardley | METHODOLOGIE | catégorie | Workflow d'automatisation de cartographie stratégique | AJOUT |
| Wardley Map | METHODOLOGIE | catégorie | Framework de cartographie de chaîne de valeur stratégique | AJOUT |
| OpenAI API | TECHNOLOGIE | usage | Génération de capacités et relations via prompts | AJOUT |
| Obsidian | TECHNOLOGIE | catégorie | Outil de gestion des connaissances avec graphe natif | AJOUT |
| NetworkX | TECHNOLOGIE | catégorie | Bibliothèque Python d'analyse de graphes et réseaux sociaux | AJOUT |
| décomposition de capacités | METHODOLOGIE | format_sortie | JSON hiérarchique parent-enfant | AJOUT |
| axe Y Wardley | CONCEPT | définition | Proximité client : haut = visible, bas = infrastructure | AJOUT |
