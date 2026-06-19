# klaassen-teach-ai-think-senior-engineer-every-2025-11-07

## Veille
8 stratégies planification IA - Research agents parallèles - Codebase grounding - Git history - Vibe prototyping - Style agents - Compounding engineering - Every Source Code - Kieran Klaassen

## Titre Article
Teach Your AI to Think Like a Senior Engineer

## Date
2025-11-07

## URL
https://every.to/source-code/teach-your-ai-think-like-a-senior-engineer

## Keywords
planning strategies, research agents, parallel operations, Cora email bankruptcy, reproduce and document, best practices grounding, codebase grounding, libraries grounding, git history, vibe prototyping, synthesis with options, style review agents, compounding engineering, institutional memory, CLAUDE.md, docs knowledge base, AppSignal logs, RubyLLM gem, EmailClassifier, event tracking, specialized reviewers, SDLC, cycle de vie logiciel, SDLC agentique

## Authors
Kieran Klaassen (General Manager, Cora)

## Ton
**Profil:** Tutoriel de praticien avancé | Première personne praticien | Prescriptif-systématique | Expert

Klaassen adopte une voix de praticien expérimenté partageant un playbook tactique concret, en suite de son article précédent plus philosophique. La structure en 8 stratégies (reproduire → bonnes pratiques → codebase → bibliothèques → git → vibe → synthèse → revue) démontre la pensée systématique typique d'un ingénieur senior. Le langage d'ingénieur de terrain (logs AppSignal, gem RubyLLM, helper methods, dénormalisation, pull requests), ancré dans des exemples de production de Cora, crée la crédibilité. Le ton prescriptif et confiant ("You can avoid building the wrong thing, too") reflète la maîtrise. Les liens GitHub directs et le système de planification open-sourcé montrent un engagement de partage ouvert de la connaissance. L'accent mis sur "comment faire capitaliser cela" après chaque stratégie renforce la thèse centrale d'accumulation de connaissance. Typique des tutoriels avancés de Source Code d'Every (Klaassen, articles techniques de Dan Shipper) visant une audience de praticiens prêts à implémenter immédiatement plutôt qu'une compréhension conceptuelle.

## Pense-betes
- **Suite de l'article précédent** : Stop Coding and Start Planning (2025-11-06)
- **Thèse centrale** : des opérations de recherche parallèles enseignent à l'IA votre façon de penser plus vite que la planification humaine séquentielle
- **8 stratégies de planification** selon les niveaux de fidelity (One : correctifs rapides, Two : périmètre clair, Three : exigences incertaines)

**Stratégie 1 : Reproduire et documenter**
- Fidelity : One & Two, corrections de bugs
- Rôle de l'agent : guide de reproduction pas à pas
- Exemple Cora : 19 utilisateurs bloqués sur l'email bankruptcy, les logs AppSignal ont révélé des erreurs de rate limit avalées, échecs silencieux
- Capitalisation : checklist @kieran-rails-reviewer mise à jour — "jobs en arrière-plan appelant des API externes : les rate limits sont-ils gérés ?"

**Stratégie 2 : S'ancrer dans les bonnes pratiques**
- Fidelity : toutes, surtout pour les patterns peu familiers
- Agent : @agent-best-practices-researcher
- Cas d'usage : architecture technique, copywriting, recherche de pricing, chemins de mise à niveau
- Exemple : gem en retard de 2 versions ; l'agent a trouvé le guide officiel + 3 billets de blog avec cas limites ; 3 min de recherche ont évité des heures de debugging
- Capitalisation : sauvegarder les trouvailles dans docs/*.md (pay-gem-upgrades.md, pricing-research.md) ; l'agent consulte d'abord les docs locales avant le web

**Stratégie 3 : S'ancrer dans sa codebase**
- Fidelity : tout ce qui risque de dupliquer une fonctionnalité existante
- Rôle de l'agent : chercher dans le code existant les implémentations apparentées
- Exemple : feature d'event tracking ; l'agent a trouvé un système de tracking existant oublié, avec helper methods
- Capitalisation : création d'un agent @event-tracking-expert distillant tous les patterns de tracking, exécuté automatiquement sur les features concernées

**Stratégie 4 : S'ancrer dans ses bibliothèques**
- Fidelity : bibliothèques qui évoluent vite ou mal documentées
- Rôle de l'agent : analyser le code source pour comprendre les capacités
- Exemple : la gem RubyLLM évolue constamment, la doc est en retard ; l'agent a lu le source et trouvé le support streaming v1.9 non documenté
- Capitalisation : la connaissance se met à jour automatiquement à chaque mise à jour de dépendance, jamais d'information périmée

**Stratégie 5 : Étudier l'historique git**
- Fidelity : refactorings, continuation de travaux, comprendre le "pourquoi"
- Rôle de l'agent : rechercher les décisions passées et leur contexte
- Exemple : EmailClassifier v1 vs v2 ; l'agent a trouvé une PR vieille de 3 mois montrant que le passage en v2 avait été tenté, avait cassé des cas limites et avait été délibérément annulé
- Capitalisation : mémoire institutionnelle préservée et cherchable, les nouveaux membres de l'équipe héritent du raisonnement

**Stratégie 6 : Vibe prototyper pour clarifier**
- Fidelity : Three, incertitude UX, exploratoire
- Rôle de l'agent : construire rapidement des versions jetables avec lesquelles interagir
- Exemple : refonte de l'interface Brief, 5 prototypes de 5 min chacun, feedback utilisateur "bouton archiver en haut à gauche — réflexe hérité de Gmail"
- Capitalisation : le vibe coding transforme l'incertitude en spécifications concrètes, les réactions utilisateurs sont documentées

**Stratégie 7 : Synthétiser avec des options**
- Fidelity : fin de la phase de recherche avant implémentation
- Rôle de l'agent : présenter 2-3 pistes de solution avec avantages/inconvénients honnêtes
- Exemple : synchronisation de l'inbox Gmail, 3 options (greffer sur l'existant / temps réel / cache miroir), compromis (rapide mais sale / propre mais lent / effort initial mais meilleur long terme)
- Capitalisation : le choix révèle les préférences ("je préfère le largement supporté au cutting-edge"), codifiées pour les décisions similaires futures

**Stratégie 8 : Relire avec des agents de style**
- Fidelity : dernière étape de planification avant implémentation
- Rôle de l'agent : détecter les désalignements avec le style de code et l'architecture
- Trois agents de revue :
  - Simplification : signale le sur-engineering
  - Sécurité : vérifie les vulnérabilités
  - Style-Kieran : préférences personnelles (requêtes simples vs jointures complexes, dénormalisation)
- Capitalisation : les agents accumulent du goût avec le temps, chaque "je n'aime pas ça" rend le système plus intelligent

**Guide pratique de démarrage** :
- Choisir une feature Fidelity Two (multi-fichiers, périmètre clair)
- 15-20 min de recherche : bonnes pratiques (web), patterns (codebase), capacités des bibliothèques (docs/source)
- Laisser l'IA synthétiser : problème (1 phrase), 2-3 approches (avantages/inconvénients), correspondance avec les patterns existants, cas limites/sécurité
- Capturer ses réactions de revue : noter "trop complexe" ou "meilleure façon" — écrire le POURQUOI
- Livrer la feature, comparer l'implémentation au plan, noter les divergences
- Codifier 1 apprentissage : l'ajouter à CLAUDE.md ("Quand X, vérifier Y" ou "Préférer A à B parce que C")
- Créer des agents spécialisés : Event Tracking Expert, Security Checker
- Répéter : la semaine suivante, se référer aux notes ; le deuxième plan est meilleur que le premier

**Open-source** : marketplace GitHub d'Every, commande /plan + agents de recherche prêts à l'emploi

## RésuméDe400mots

Kieran Klaassen présente 8 stratégies concrètes transformant la philosophie de planification en systèmes opérationnels pour enseigner à l'IA à penser comme un ingénieur senior. Suite de son article précédent sur la planification vs le vibe coding, ce guide tactique détaille comment exécuter des opérations de recherche parallèles plus rapides que la planification humaine séquentielle.

**Framework des 8 stratégies**

**1. Reproduire et documenter** : avant de corriger un bug, le reproduire et le documenter. Exemple de l'email bankruptcy de Cora : 19 utilisateurs bloqués ; l'agent a parcouru les logs AppSignal → des erreurs de rate limit étaient avalées silencieusement. Fini de deviner. Capitalisation : mise à jour permanente de la checklist @kieran-rails-reviewer.

**2. S'ancrer dans les bonnes pratiques** : @agent-best-practices-researcher cherche sur le web comment d'autres ont résolu le problème. Cas d'usage : architecture, copywriting, pricing, mises à niveau. Gem en retard de 2 versions : 3 min de recherche ont trouvé le guide officiel + 3 billets de blog sur les cas limites, évitant des heures de debugging. Capitalisation : sauvegarder les trouvailles dans docs/*.md, l'agent consulte d'abord les docs locales.

**3. S'ancrer dans la codebase** : chercher les patterns existants avant de recréer. Feature d'event tracking : l'agent a trouvé un système existant oublié avec ses helper methods, évitant de construire un second système incompatible. Capitalisation : l'agent @event-tracking-expert distille tous les patterns et s'exécute automatiquement.

**4. S'ancrer dans les bibliothèques** : pour les bibliothèques rapides et mal documentées, lire le code source. Gem RubyLLM : l'agent a découvert le support streaming v1.9, non documenté mais présent dans la suite de tests. Capitalisation : mise à jour automatique à chaque montée de version de dépendance.

**5. Étudier l'historique git** : comprendre le "pourquoi" des décisions passées. Mise à niveau d'EmailClassifier : l'agent a trouvé une PR de 3 mois montrant que la v2 avait été tentée, avait cassé des cas limites (inbox→archive et archive→inbox inversés) et avait été délibérément annulée avec un raisonnement détaillé. 5 min de recherche ont évité de réintroduire un bug déjà débuggé. Capitalisation : mémoire institutionnelle préservée et cherchable.

**6. Vibe prototyper pour clarifier** : Fidelity Three, UX incertaine. Interface Brief : 5 prototypes de 5 min chacun, feedback utilisateur concret ("bouton archiver en haut à gauche — réflexe Gmail"). Les prototypes sont supprimés, la connaissance passe dans le plan. Capitalisation : l'incertitude devient des spécifications concrètes documentées.

**7. Synthétiser avec des options** : combiner toute la recherche en 2-3 approches avec des compromis honnêtes. Synchronisation Gmail : option A (greffer sur l'existant — rapide mais sale), B (temps réel — propre mais lent), C (cache miroir — effort initial mais meilleur à long terme). L'agent fait la recherche, l'humain juge. Capitalisation : les choix révèlent des préférences codifiées ("préférer le largement supporté au cutting-edge").

**8. Relire avec des agents de style** : 3 relecteurs spécialisés en passe finale. Agent simplification (signale le sur-engineering), agent sécurité (vulnérabilités), agent style-Kieran (préférences personnelles : requêtes simples vs jointures complexes, dénormalisation). Capitalisation : les agents accumulent du goût avec le temps.

**Cas email bankruptcy révélateur** : jugé facile au départ ("archiver 53 000 emails en masse, quelle difficulté ?"). 20 min d'agent de recherche ont ramené à la réalité : les rate limits Gmail tuent à 2 000, timeouts système, longue attente utilisateur. La feature simple est devenue un défi architectural de 3 jours. La planification a évité de construire entièrement la mauvaise chose.

**Mise en œuvre pratique** : choisir une feature Fidelity Two → 15-20 min de recherche (bonnes pratiques web + patterns codebase + capacités des bibliothèques) → l'IA synthétise le plan (problème/approches/patterns/cas limites) → capturer le POURQUOI de ses réactions de revue → livrer → comparer implémentation et plan → codifier 1 apprentissage dans CLAUDE.md → créer des agents spécialisés → répéter la semaine suivante.

**Contribution open-source** : Klaassen a open-sourcé son système de planification sur la marketplace GitHub d'Every avec la commande /plan et des agents de recherche prêts à l'emploi. Philosophie : ne pas repartir de zéro, adapter des systèmes éprouvés existants.

Chaque stratégie inclut un volet "comment faire capitaliser cela", démontrant la thèse centrale : les opérations de recherche parallèles enseignent à l'IA une connaissance institutionnelle qui s'accumule plus vite que la planification humaine séquentielle.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Kieran Klaassen | PERSONNE | a_créé | Compounding Engineering | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | dirige | Cora | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Kieran Klaassen | PERSONNE | travaille_chez | Every | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Compounding Engineering | METHODOLOGIE | est_basé_sur | opérations de recherche parallèles | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| opérations de recherche parallèles | CONCEPT | remplace | planification séquentielle humaine | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Kieran Klaassen | PERSONNE | utilise | Claude Code | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Cora | TECHNOLOGIE | utilise | Gmail API | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Gmail API | TECHNOLOGIE | mesure | limite de débit à 2000 emails | MESURE | 0.95 | STATIQUE | déclaré_article |
| AppSignal | TECHNOLOGIE | permet | diagnostic logs production | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Cora | TECHNOLOGIE | utilise | RubyLLM | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| CLAUDE.md | TECHNOLOGIE | référence | préférences architecturales | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| git history | TECHNOLOGIE | permet | mémoire institutionnelle | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| vibe coding | METHODOLOGIE | permet | transformation des incertitudes UX en spécifications | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Every | ORGANISATION | publie | planning system open-source | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Kieran Klaassen | PERSONNE | rôle | General Manager de Cora | AJOUT |
| Every | ORGANISATION | secteur | Media / Outils IA | AJOUT |
| Cora | TECHNOLOGIE | catégorie | Produit email géré par Every | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| AppSignal | TECHNOLOGIE | catégorie | Système de tracking d'erreurs production | AJOUT |
| RubyLLM | TECHNOLOGIE | catégorie | Gem Ruby pour appels API LLM | AJOUT |
| Gmail API | TECHNOLOGIE | contrainte | Rate limit 2000 emails par batch | AJOUT |
| Compounding Engineering | METHODOLOGIE | principe | Chaque feature améliore le système pour la suivante | AJOUT |
| opérations de recherche parallèles | CONCEPT | avantage | Plus rapide que planification séquentielle humaine | AJOUT |
| mémoire institutionnelle | CONCEPT | mécanisme | Git history + agents spécialisés + docs/*.md | AJOUT |
| CLAUDE.md | TECHNOLOGIE | usage | Codifier préférences et règles de l'ingénieur | AJOUT |
| vibe coding | METHODOLOGIE | usage | Prototypage rapide jetable pour clarifier les exigences | AJOUT |
