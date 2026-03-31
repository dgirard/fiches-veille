# chow-compound-engineering-v260-review-pipeline-2026-03-31

## Veille

Compound Engineering v2.60, revue de code obligatoire avec scoring confiance, pipeline plan→work→review durci

## Titre Article

Compound Engineering: 3/31/2026

## Date

2026-03-31

## URL

https://x.com/trevin/status/2038893322333507781

## Keywords

Compound Engineering, revue de code obligatoire, scoring de confiance, faux positifs, pipeline agentique, ce:work, ce:plan, ce:brainstorm, ce:review, découverte de tests, mode headless, deepening interactif, diagrammes conditionnels, mermaid, clustering feedback PR, document-review, learnings track-based, Claude Code skills

## Authors

Trevin Chow

## Ton

**Profil** : Changelog/release notes enrichi, registre technique-décontracté, niveau détaillé pour praticiens.

**Description** : Chow adopte le format d'un changelog commenté, chaque section détaillant une skill ou fonctionnalité mise à jour avec le contexte du « pourquoi » en plus du « quoi ». Le ton est celui d'un mainteneur de projet qui parle directement à sa communauté d'utilisateurs : familier (« we know many of you just wanna rip »), auto-ironique (« I may change my mind on this »), et pragmatique. Chaque décision de design est justifiée par un raisonnement explicite (« mandate first, then reduce noise, otherwise we'd be mandating noise »). L'écriture est dense en détails techniques mais reste accessible grâce à un style conversationnel. Le public cible est constitué d'utilisateurs actifs de Compound Engineering / Claude Code qui veulent comprendre les changements et leur logique.

## Pense-betes

- v2.60.0 du 31 mars 2026 — fil directeur : resserrer le pipeline bout en bout (reviews, plans, friction réduite)
- **ce:review — changement majeur** : mode headless pour invocation programmatique + revue de code rendue OBLIGATOIRE dans tout le pipeline (ce:work, ce:brainstorm, ce:plan). Full review par défaut, limited review nécessite justification
- Rubrique de confiance 6 niveaux (0.00–1.00) avec seuil de suppression à 0.60. 6 catégories de faux positifs ciblées : problèmes préexistants, nitpicks de style, patterns intentionnels, gérés ailleurs, reformulation du code, conseils génériques
- ~49% de réduction des faux positifs sans perte de détection de vrais bugs
- Vérification d'intention : les findings sont comparés au contexte PR (titre, body, issue liée) — les findings contradictoires avec l'objectif du PR sont supprimés
- Consensus multi-persona : si 2+ reviewers persona signalent le même problème, boost de confiance +0.10
- Findings en tableaux pipe-delimited (plus de prose libre) pour scannabilité et cohérence
- Philosophie : « mandate first, then reduce noise — otherwise we'd be mandating noise »
- **ce:work** : accepte maintenant des prompts bruts sans plan préalable. Évaluation automatique de complexité (trivial → skip cérémonie, medium → tâches inline, complex → recommande planning)
- Découverte universelle de tests avant implémentation. Délibération par tâche : « testing addressed » remplace le binaire « tests pass »
- 5e check du testing-reviewer : détecte les changements comportementaux (nouvelles branches, mutations d'état, changements API) sans tests correspondants
- Détection des noms de branches auto-générées (ex: « worktree-printing-ruby-raven ») + suggestion de renommage
- **ce:brainstorm** : bug corrigé — Phase 1.1 empêchait la lecture des fichiers techniques, conduisant à des affirmations non vérifiées (« table X does not exist » sans vérifier le schéma). Désormais : vérification de l'état actuel autorisée, affirmations non vérifiées étiquetées comme hypothèses
- **ce:plan** : mode deepening interactif — accepter, rejeter ou discuter les findings de chaque agent avant intégration (au lieu de l'auto-merge). Support /ce:plan "deepen" pour invoquer l'enrichissement directement
- document-review rendu obligatoire après deepening. Plans signalent les scénarios de test vides sur les unités fonctionnelles
- **Aides visuelles conditionnelles** : génération automatique de diagrammes (mermaid/ASCII) quand la complexité dépasse des seuils (5+ unités non-linéaires, 3+ surfaces interagissantes). Seuil plus élevé pour les descriptions de PR
- **resolve-pr-feedback** : clustering des commentaires PR par catégorie de préoccupation et proximité spatiale. Après 2 cycles fix-verify, les problèmes restants deviennent « recurring patterns ». Filtre d'actionnabilité (ignore les 👍, badges, texte wrapper)
- **document-review** simplifié : 3 tiers → 2 tiers (auto / present). Suggestion du next step selon le type de document
- **ce:compound** : schema track-based — bug-track (diagnostic complet) vs knowledge-track (template allégé). Check de découvrabilité : vérifie que docs/solutions/ est référencé dans AGENTS.md ou CLAUDE.md
- Infrastructure : normalisation des champs modèle centralisée (fix Qwen→sonnet mapping incorrect), support MiniMax, nettoyage des argument-hints

## RésuméDe400mots

Trevin Chow détaille les mises à jour de Compound Engineering culminant avec la v2.60.0 du 31 mars 2026. Le fil directeur est le resserrement du pipeline de bout en bout : les revues de code sont moins bruyantes et désormais obligatoires, les plans détectent plus de lacunes avant l'implémentation, et la friction d'utilisation quotidienne continue de diminuer.

Le changement le plus significatif concerne ce:review. Un mode headless permet l'invocation programmatique par d'autres skills, ce qui a débloqué l'étape suivante : rendre la revue de code obligatoire dans tout le pipeline (ce:work, ce:brainstorm, ce:plan). La full review est le niveau par défaut, la limited review nécessitant une justification explicite. Pour éviter de « mandater du bruit », une rubrique de confiance à 6 niveaux (0.00–1.00) avec un seuil de suppression à 0.60 a été ajoutée simultanément. Six catégories de faux positifs sont ciblées : problèmes préexistants, nitpicks de style, patterns intentionnels, cas gérés ailleurs, reformulation du code, et conseils génériques. Résultat : réduction de 49% des faux positifs sans perte de détection réelle. Les findings sont vérifiés contre le contexte du PR et le consensus multi-persona booste la confiance de 0.10.

ce:work accepte désormais des prompts bruts sans plan préalable, avec évaluation automatique de la complexité. La découverte universelle de tests avant implémentation garantit la synchronisation code/tests. Un nouveau check détecte les changements comportementaux sans tests correspondants.

ce:brainstorm corrige un bug subtil où la Phase 1.1 empêchait les agents de lire les fichiers techniques, produisant des affirmations non vérifiées comme « cette table n'existe pas » sans consulter le schéma. Désormais, la vérification de l'état actuel est autorisée tandis que les décisions d'implémentation restent différées à la planification.

ce:plan gagne un mode deepening interactif permettant d'accepter, rejeter ou discuter les findings de chaque agent avant intégration. La revue documentaire est rendue obligatoire après enrichissement.

Une fonctionnalité transversale génère automatiquement des diagrammes (mermaid/ASCII) quand la complexité dépasse certains seuils. Le resolve-pr-feedback détecte maintenant le « whack-a-mole » en clusterisant les commentaires similaires. Le document-review passe de 3 à 2 niveaux et suggère l'étape suivante selon le type de document. Enfin, ce:compound adopte un schéma par track (bug vs knowledge) avec un check de découvrabilité.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Compound Engineering | TECHNOLOGIE | publie | v2.60.0 | EVENEMENT | 0.99 | STATIQUE | déclaré_article |
| ce:review | TECHNOLOGIE | rend_obligatoire | revue de code dans pipeline | METHODOLOGIE | 0.98 | DYNAMIQUE | déclaré_article |
| ce:review | TECHNOLOGIE | réduit | faux positifs de 49% | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| ce:review | TECHNOLOGIE | utilise | scoring confiance 6 niveaux | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| ce:work | TECHNOLOGIE | accepte | prompts bruts sans plan | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| ce:work | TECHNOLOGIE | intègre | découverte universelle de tests | METHODOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| ce:brainstorm | TECHNOLOGIE | corrige | bug vérification fichiers techniques Phase 1.1 | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| ce:plan | TECHNOLOGIE | ajoute | mode deepening interactif | METHODOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Trevin Chow | PERSONNE | maintient | Compound Engineering | TECHNOLOGIE | 0.95 | DYNAMIQUE | inféré |
| Compound Engineering | TECHNOLOGIE | génère_automatiquement | diagrammes mermaid conditionnels | METHODOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| resolve-pr-feedback | TECHNOLOGIE | clusterise | commentaires PR similaires | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| ce:compound | TECHNOLOGIE | adopte | schema track-based bug vs knowledge | METHODOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Compound Engineering | TECHNOLOGIE | version | v2.60.0 (2026-03-31) | MISE_A_JOUR |
| Trevin Chow | PERSONNE | rôle | Mainteneur Compound Engineering | AJOUT |
| ce:review | TECHNOLOGIE | description | Skill de revue de code multi-persona avec scoring confiance | AJOUT |
| ce:work | TECHNOLOGIE | description | Skill d'exécution de plans avec découverte de tests | AJOUT |
| ce:plan | TECHNOLOGIE | description | Skill de planification avec deepening interactif | AJOUT |
| ce:brainstorm | TECHNOLOGIE | description | Skill de brainstorming avec vérification état technique | AJOUT |
| ce:compound | TECHNOLOGIE | description | Skill de documentation de solutions avec schema par track | AJOUT |
| resolve-pr-feedback | TECHNOLOGIE | description | Skill de résolution feedback PR avec clustering | AJOUT |
