# boeckeler-harness-engineering-coding-agents-2026-04-02

## Veille

Harness engineering : modèle mental pour construire la confiance dans les agents de codage via guides feedforward et capteurs feedback

## Titre Article

Harness engineering for coding agent users

## Date

2026-04-02

## URL

https://martinfowler.com/articles/harness-engineering.html

## Keywords

harness engineering, agents de codage, feedforward, feedback, capteurs, guides, cybernétique, qualité logicielle, ingénierie de contexte, contrôles computationnels, contrôles inférentiels, harnais de maintenabilité, harnais d'architecture, harnais de comportement, harnachabilité, templates de harnais, boucle de pilotage, shift left, linters, tests structurels, revue de code IA

## Authors

Birgitta Böckeler

## Ton

**Profil** : Perspective analytique et pédagogique, registre technique accessible, niveau expert mais vulgarisé. Birgitta écrit comme une architecte logicielle senior qui structure un domaine émergent.

**Description** : Le ton est celui d'une ingénieure distinguée qui propose un cadre conceptuel rigoureux mais pragmatique. L'écriture est structurée, progressive, avec des définitions précises et des taxonomies claires (feedforward/feedback, computationnel/inférentiel). L'auteure utilise des métaphores de la cybernétique (gouverneur, régulateur, loi d'Ashby) pour ancrer le propos dans une théorie existante, tout en restant consciente de leurs limites ("les métaphores ne vont que jusqu'à un certain point"). Le style alterne entre exposition théorique et exemples concrets issus de la pratique chez Thoughtworks, OpenAI et Stripe. L'article s'adresse à des développeurs seniors et architectes qui utilisent déjà des agents de codage et cherchent un modèle mental pour structurer leur approche. Le ton est honnête sur les limites actuelles, notamment pour le harnais comportemental, et termine sur des questions ouvertes plutôt que des certitudes.

## Pense-betes

- **Définition clé** : le "harnais" (harness) d'un agent de codage = tout ce qui entoure le modèle. Distinction entre le harnais interne (construit par le créateur de l'agent) et le harnais externe (construit par l'utilisateur pour son contexte)
- **Deux axes fondamentaux** : guides (feedforward, avant l'action) et capteurs (feedback, après l'action) ; chacun pouvant être computationnel (déterministe, rapide, CPU) ou inférentiel (sémantique, non-déterministe, GPU)
- **Boucle de pilotage** : le rôle de l'humain est d'itérer sur le harnais quand un problème se répète, pas de corriger chaque erreur manuellement
- **Shift left** : distribuer les contrôles au plus tôt dans le cycle de vie (pré-commit, pré-intégration, pipeline, monitoring continu)
- **Trois catégories de régulation** : maintenabilité (le plus facile, outillage existant), fitness architecturale (fitness functions), comportement (le plus difficile, "éléphant dans la pièce")
- **Harnachabilité** : toutes les codebases ne sont pas également harnachables. Les langages fortement typés, les frameworks abstraits (Spring), les frontières modulaires claires augmentent la harnachabilité. Le legacy lourdement endetté est le plus difficile à harnacher mais en a le plus besoin
- **"Ambient affordances"** (Ned Letcher) : propriétés structurelles de l'environnement qui le rendent lisible et navigable par les agents
- **Loi d'Ashby** : un régulateur doit avoir au moins autant de variété que le système qu'il gouverne. Définir des topologies de services réduit la variété, rendant un harnais complet plus atteignable
- **Templates de harnais** : évolution des templates de services existants en bundles de guides+capteurs par topologie (dashboard, CRUD, event processor)
- **Limite importante** : les harnais ne capturent pas fiablement les problèmes de haut niveau (mauvais diagnostic, sur-ingénierie, instructions mal comprises). L'expérience humaine reste un "harnais implicite" irremplaçable
- **Relation avec le context engineering** : le harness engineering est une forme spécifique de context engineering appliquée aux agents de codage
- **Exemples concrets** : OpenAI utilise des linters custom + tests structurels + "garbage collection" ; Stripe utilise des pre-push hooks + heuristiques + blueprints
- **L'injection de prompt positive** : les messages de linter customisés incluant des instructions de correction sont une forme bénéfique d'injection de prompt

## RésuméDe400mots

Le terme "harnais" (harness) désigne tout ce qui entoure un modèle d'IA dans un agent. Birgitta Böckeler propose un cadre conceptuel spécifique aux utilisateurs d'agents de codage, distinguant le harnais interne (construit par le créateur de l'agent) du harnais externe (que les utilisateurs construisent pour leur contexte).

Le modèle s'articule autour de deux mécanismes complémentaires. Les **guides** (contrôles feedforward) anticipent le comportement de l'agent et le dirigent avant qu'il n'agisse : conventions de codage, spécifications, skills, serveurs MCP. Les **capteurs** (contrôles feedback) observent après l'action et permettent à l'agent de s'auto-corriger : linters, tests, analyses statiques, revues de code IA. Chaque mécanisme peut être **computationnel** (déterministe, rapide, fiable) ou **inférentiel** (sémantique, plus coûteux, non-déterministe). Les deux sont nécessaires : sans feedback, l'agent répète ses erreurs ; sans feedforward, il encode des règles sans savoir si elles fonctionnent.

L'article applique le principe du **shift left** : distribuer les contrôles au plus tôt dans le cycle de développement. Les contrôles rapides (linters, tests unitaires) s'exécutent avant le commit, tandis que les plus coûteux (tests de mutation, revue architecturale) s'exécutent dans le pipeline d'intégration. Des capteurs continus surveillent la dérive du code et les métriques de production.

Trois **catégories de régulation** sont identifiées. Le harnais de **maintenabilité** est le plus mature, s'appuyant sur l'outillage existant (linters, analyseurs de complexité, couverture de tests). Le harnais de **fitness architecturale** reprend le concept de fitness functions pour les caractéristiques non-fonctionnelles. Le harnais de **comportement** reste le défi majeur : comment vérifier que l'application fait ce qu'elle doit faire ? Les suites de tests générées par l'IA ne sont pas encore suffisamment fiables.

Le concept de **harnachabilité** souligne que toutes les codebases ne sont pas également aptes au harnachage. Les langages typés, les frameworks abstraits et les architectures modulaires offrent davantage de prises. La loi d'Ashby de la cybernétique justifie les **templates de harnais** : en réduisant la variété des topologies possibles (dashboard, CRUD, event processor), on rend un harnais complet plus atteignable.

L'auteure conclut que l'expérience humaine reste un "harnais implicite" irremplaçable. L'objectif n'est pas d'éliminer l'humain mais de diriger son attention vers ce qui compte le plus. Le harness engineering est une pratique d'ingénierie continue, pas une configuration ponctuelle, et de nombreuses questions restent ouvertes sur la cohérence, l'évaluation et l'orchestration des harnais.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Birgitta Böckeler | PERSONNE | a_écrit | Harness engineering for coding agent users | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Birgitta Böckeler | PERSONNE | travaille_chez | Thoughtworks | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Harness engineering | METHODOLOGIE | est_une_forme_de | Context engineering | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Harness engineering | METHODOLOGIE | utilise | Guides feedforward | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| Harness engineering | METHODOLOGIE | utilise | Capteurs feedback | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| Guides feedforward | CONCEPT | augmente | Probabilité de bons résultats | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Capteurs feedback | CONCEPT | permet | Auto-correction de l'agent | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Harnais de comportement | CONCEPT | est_décrit_comme | Défi majeur non résolu | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Loi d'Ashby | CONCEPT | justifie | Templates de harnais | CONCEPT | 0.88 | ATEMPOREL | inféré |
| Ned Letcher | PERSONNE | a_créé | Ambient affordances | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | utilise | Linters custom et tests structurels | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Stripe | ORGANISATION | utilise | Pre-push hooks et blueprints | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Harnachabilité | CONCEPT | dépend_de | Typage fort et modularité | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Expérience humaine | CONCEPT | constitue | Harnais implicite irremplaçable | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Birgitta Böckeler | PERSONNE | rôle | Distinguished Engineer, experte IA-assisted delivery chez Thoughtworks | AJOUT |
| Birgitta Böckeler | PERSONNE | expérience | 20+ ans en développement logiciel, architecture et leadership technique | AJOUT |
| Thoughtworks | ORGANISATION | secteur | Conseil en ingénierie logicielle | AJOUT |
| Harness engineering | METHODOLOGIE | catégorie | Pratique d'ingénierie pour construire la confiance dans les agents de codage | AJOUT |
| Context engineering | METHODOLOGIE | catégorie | Ingénierie du contexte fourni aux agents IA | AJOUT |
| Guides feedforward | CONCEPT | définition | Contrôles anticipatifs qui dirigent l'agent avant qu'il n'agisse | AJOUT |
| Capteurs feedback | CONCEPT | définition | Contrôles observationnels permettant l'auto-correction après action | AJOUT |
| Harnachabilité | CONCEPT | définition | Degré auquel une codebase est apte au harnachage par des agents | AJOUT |
| Ambient affordances | CONCEPT | définition | Propriétés structurelles rendant un environnement lisible et navigable par les agents | AJOUT |
| Loi d'Ashby | CONCEPT | domaine | Cybernétique - loi de la variété requise | AJOUT |
| Ned Letcher | PERSONNE | rôle | Collègue de Böckeler chez Thoughtworks | AJOUT |
| Kief Morris | PERSONNE | rôle | Collègue Thoughtworks, a proposé le lien avec la cybernétique | AJOUT |
| OpenAI | ORGANISATION | secteur | IA / Recherche | MISE_A_JOUR |
| Stripe | ORGANISATION | secteur | Paiements / Fintech | MISE_A_JOUR |
| Approved fixtures | METHODOLOGIE | catégorie | Pattern de test pour harnais comportemental | AJOUT |
