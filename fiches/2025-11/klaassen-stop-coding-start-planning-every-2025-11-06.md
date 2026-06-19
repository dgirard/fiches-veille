# klaassen-stop-coding-start-planning-every-2025-11-06

## Veille
Planification vs Vibe Coding - Compounding Engineering - Three Fidelities - AI Agents - Cora Email Bankruptcy - Plans teach systems - Every Source Code

## Titre Article
Stop Coding and Start Planning

## Date
2025-11-06

## URL
https://every.to/source-code/stop-coding-and-start-planning

## Keywords
planification, vibe coding, compounding engineering, AI agents, three fidelities, Cora, email bankruptcy, Figma to code, planning agents, institutional knowledge, Claude Code, research phase, prototyping, vibe planning, View Components, GitHub plans, Puppeteer review, teaching AI systems, SDLC, cycle de vie logiciel, SDLC agentique

## Authors
Kieran Klaassen (General Manager, Cora)

## Ton
**Profil:** Tutoriel de praticien | Première personne praticien | Éducatif-narratif | Expert-accessible

Klaassen (GM de Cora) adopte une voix de praticien expérimenté partageant des leçons durement acquises en construisant un produit email. La structure de tutoriel narratif (problème → insight → solution → exemple) illustre une pédagogie par le récit. Le langage d'ingénieur praticien (rate limiting, couche de cache, système de queue, race conditions), ancré dans l'exemple concret de l'email bankruptcy de Cora, crée la crédibilité. Le ton honnête et réflexif, admettant ses propres erreurs ("I did it, too") avant de prescrire des solutions, construit la confiance. Les anecdotes personnelles (5 écrans Figma, deadline d'un weekend, prototypes jetés) humanisent les concepts techniques. L'accent sur la pensée systémique ("enseigner à l'IA comment vous pensez") plutôt que l'exécution tactique reflète une perspective d'ingénieur senior. Typique des chroniqueurs de Source Code d'Every.to (Dan Shipper, Nathan Baschez) combinant tutoriels pratiques et cadres stratégiques pour une audience de builders cherchant des workflows IA durables au-delà de la hype.

## Pense-betes
- **Thèse centrale** : "AI made us sloppy because it made us forget how to plan"
- **Vibe coding** : "Make this feature work" → espérer que l'IA prenne la bonne route → 3h de debugging vs 10 min de planification
- **Planifier avec l'IA** : rechercher dans la codebase, vérifier la bibliothèque, consulter les bonnes pratiques, créer un plan avec 3 approches + compromis
- **Les plans enseignent des systèmes, le code résout des problèmes** : plans = savoir institutionnel, code = solution unique
- **Compounding engineering** : chaque unité de travail rend la suivante plus facile en enseignant l'IA
- **Framework des Three Fidelities** :
  - **Fidelity One (correctif rapide)** : changement d'une ligne, typo, bug évident. Planification légère. Claude Sonnet 4.5 élargit ce périmètre (changements de pricing, normalisation d'emails, corrections de tests)
  - **Fidelity Two (sweet spot)** : multi-fichiers, refactoring, périmètre clair, implémentation non évidente. ROI massif de la planification. Exemple : outil d'archivage par requête
  - **Fidelity Three (gros et incertain)** : features majeures, périmètre flou, exigences incertaines. Vibe planning = prototypage rapide + planification rigoureuse. Exemple : email bankruptcy, 53 000 emails
- **Cas Cora email bankruptcy** : 5 écrans Figma → pixel-perfect en un weekend avec des agents de planification
- **Workflow à deux agents** : Agent 1 (analyse Figma → plan), Agent 2 (comparaison Puppeteer → itérer jusqu'à correspondance)
- **Accumulation de connaissance** : 50+ revues de plans → le système apprend les préférences et la pensée architecturale
- **Phase de recherche critique** : l'archivage par requête a révélé un outil de recherche existant et les quotas de l'API Gmail
- **Vibe planning** : prototypes jetables pour clarifier les exigences avant l'implémentation réelle
- **Découper Fidelity Three** : prototyper 3 solutions (temps réel, cache simple, queue) → apprendre → découper en morceaux Fidelity Two
- **Préférence View Components** : codifiée dans les instructions d'agent → automatique pour tous les designs futurs
- **Les plans persistent, les prototypes sont jetés** : la connaissance est extraite puis le prototype abandonné
- **Les prochains modèles en bénéficient automatiquement** : GPT-5/Claude améliorent les plans, mais le savoir institutionnel se capitalise séparément

## RésuméDe400mots

Kieran Klaassen, General Manager de Cora (produit email d'Every), argumente que l'IA générative nous a rendus "sloppy" en nous faisant oublier comment planifier. Le vibe coding initial ("Make this feature work") génère rapidement du code mais conduit souvent à 3 heures de debugging qu'une session de 10 minutes de planification aurait évitées, tout en repartant de zéro à chaque feature au lieu que l'IA s'améliore avec chaque requête.

**Planification vs Vibe Coding**

Le contraste est frappant. Vibe coding : "Add email validation to the signup form" → espérer que l'IA prenne la bonne route. Planning avec IA : "Research how we handle validation elsewhere in codebase, check if our email library has built-in validation, look up best practices for user-friendly error messages, then create a plan showing three approaches with tradeoffs." Une approche ship une feature. L'autre ship une feature ET enseigne au système comment vous pensez pour la prochaine fois.

**Framework des Three Fidelities**

Klaassen propose un framework pour catégoriser le travail d'engineering :

- **Fidelity One (Quick fix)** : changements one-line, typos, bugs évidents. Planning lightweight suffit. Avec Claude Sonnet 4.5, cette catégorie s'étend : changements pricing cross-codebase, normalisation emails, reorganisation code, migration dépendances - du travail multi-heures devenu 10 minutes avec plan well-constructed.

- **Fidelity Two (Sweet spot)** : features multi-files, refactoring requis, scope clair mais implémentation non-évidente. C'est ici que compounding engineering brille. Exemple : ajouter capacité "archive by query" pour Cora. Plutôt que prompt direct, phase de recherche révèle tool existant réutilisable et quotas stricts Gmail API. 20 minutes de compréhension saved heures de debugging production failures.

- **Fidelity Three (Big uncertain)** : features majeures avec requirements épiques, scope flou. Planning seul insuffisant. Requiert "vibe planning" = prototypage rapide disposable pour clarifier, puis planning rigoureux pour build properly. Email bankruptcy feature (53,000 emails) semblait Fidelity Two, devint Fidelity Three quand découverte complexité rate limiting, caching, queue systems. Solution : 3 prototypes ascending difficulty → learn what works → break into sequential Fidelity Two pieces.

**Cas concret : Email Bankruptcy**

Klaassen avait 5 écrans Figma designs et un weekend. Au lieu de coder manuellement, il créa deux agents : Agent 1 analyse Figma screenshot → output detailed plan grounded in patterns/components. Agent 2 compare Figma vs built (Puppeteer screenshots) → iterate until match. Résultat : 5 screens pixel-perfect, including mobile layouts jamais designés, en un weekend. Plan guida work, pixel perfection émergea.

**Compounding Knowledge**

La vraie puissance : chaque plan review accumule institutional knowledge. Code enseigne "Here's how to solve THIS problem." Plans enseignent "Here's how to THINK about problems like this." Après 50+ plan reviews, plans returned reflètent automatiquement préférences architecturales (ex: View Components by default pour design system). Next models (GPT-5, Claude Sonnet 4.5+) amélioreront plans automatically, mais institutional knowledge compounds séparément.

**Fastest way to teach**

Klaassen conclut : planning est highest-leverage activity en AI-assisted development. Une heure investie improving planning system makes every future hour more productive. Fastest way to teach AI n'est pas through code you write, mais through plans you review.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Kieran Klaassen | PERSONNE | dirige | Cora | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | travaille_chez | Every | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | recommande | planification avec IA | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| vibe coding | METHODOLOGIE | s_oppose_à | planification avec IA | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Compound Engineering | METHODOLOGIE | est_basé_sur | plans enseignant le système | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Three Fidelities | METHODOLOGIE | s_applique_à | travail d'engineering | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Fidelity Two | CONCEPT | améliore | Compound Engineering | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| Fidelity Three | CONCEPT | utilise | vibe planning | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| agent de planification Figma | TECHNOLOGIE | utilise | Puppeteer | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | améliore | planification Fidelity One | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Cora | ORGANISATION | a_créé | email bankruptcy feature | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| quotas Gmail API | CONCEPT | s_applique_à | opérations bulk | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| plans | CONCEPT | permet | connaissance institutionnelle | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Kieran Klaassen | PERSONNE | rôle | General Manager de Cora | AJOUT |
| Cora | TECHNOLOGIE | catégorie | Produit email / Every | AJOUT |
| Every | ORGANISATION | secteur | Médias / IA / Newsletters | AJOUT |
| Compound Engineering | METHODOLOGIE | définition | Chaque unité de travail rend la suivante plus facile en enseignant l'IA | AJOUT |
| Three Fidelities | METHODOLOGIE | niveaux | Fidelity One / Two / Three selon complexité et clarté | AJOUT |
| vibe planning | METHODOLOGIE | usage | Prototypage rapide disposable pour Fidelity Three | AJOUT |
| email bankruptcy feature | CONCEPT | périmètre | Traitement bulk de 53 000 emails via cache + queue | AJOUT |
| Claude Code | TECHNOLOGIE | usage_décrit | Exécution de plans détaillés en Fidelity One et Two | AJOUT |
| Puppeteer | TECHNOLOGIE | rôle | Capture screenshots pour agent de revue visuelle | AJOUT |
| Gmail API | TECHNOLOGIE | contrainte | Quotas stricts sur opérations bulk | AJOUT |
| Lucas Crespo | PERSONNE | rôle | Designer Every (Figma designs Cora) | AJOUT |
| Daniel Rodrigues | PERSONNE | rôle | Designer Every (Figma designs Cora) | AJOUT |
