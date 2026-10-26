---
themes: [architecture-construction, agents-codage-ia-skills]
source: "LinkedIn (Rakesh Gohel)"
---
# gohel-knowledge-context-procedural-graph-2026-10-25

## Veille

Post LinkedIn de **Rakesh Gohel** (builder chez **JUTEQ**, gouvernance et infrastructure de preuve pour agents) publié vers le **25 octobre 2026**, ~250 mots, accompagné d'une **infographie** signée *@rakeshgohel01*. Il distingue trois graphes dont un agent a besoin pour décider, sur l'exemple *« Rebook this passenger »*.

**(1)** Le **knowledge graph** répond à *« what is true »* : passagers, vols, tarifs, routes, politiques, stables et gouvernés. **(2)** Le **context graph** répond à *« what matters now »* : un sous-graphe limité à la décision (porte C8, quatre places, neuf minutes avant fermeture) et les précédents. **(3)** Le **procedural graph** répond à *« what to do next »* : des procédures stockées en triplets *(procedure, relation, procedure)*, que l'agent suit et dont il peut s'écarter. **(4)** Chaque trace est réécrite : les précédents affinent le contexte, les échecs corrigent la procédure, les motifs répétés deviennent des faits gouvernés.

L'infographie ajoute une **« Semantic Spine »** à cinq maillons qui place l'**ontologie** en amont du knowledge graph. Prolonge [[gupta-garg-context-graphs-trillion-dollar-opportunity-2025-12-22]] sur le context graph comme mémoire des traces de décision.

## Titre Article

Knowledge Graph. Context Graph. Procedural Graph. — What's true → What matters now → What do I do next

## Date

2026-10-25

## URL

https://www.linkedin.com/posts/rakeshgohel01_aiagents-agenticai-generativeai-activity-7520100714279239681-QgHj

## Keywords

knowledge graph, graphe de connaissances, context graph, graphe de contexte, procedural graph, graphe procédural, ontologie, Semantic Spine, agents IA, mémoire d'agent, sous-graphe par décision, scoping du contexte, procédure en graphe, triplets procédure-relation-procédure, traces de décision, piste d'audit, escalade humaine, apprentissage par les traces, context engineering, gouvernance des agents

## Authors

Rakesh Gohel — builder chez JUTEQ (gouvernance et infrastructure de preuve pour agents IA) ; LinkedIn, newsletter rakeshgohel.substack.com.

## Ton

Post pédagogique au format LinkedIn : une question d'ouverture, trois flèches qui déroulent un exemple unique (le réacheminement d'un passager aérien), une leçon à retenir en une phrase, puis une question d'engagement au lecteur. Le vocabulaire est assertif et sans source citée ; il s'agit d'un cadre conceptuel, pas d'un retour d'expérience chiffré. L'infographie, dense et soignée, porte une partie du propos absente du texte (l'ontologie, la colonne des fonctions, le stockage *Trace & Learn*) et se termine par un appel à suivre l'auteur et sa newsletter. Le registre est celui d'un praticien qui vend une infrastructure de gouvernance d'agents, ce que son titre affiché indique.

## Pense-betes

- **Trois questions par décision** : vrai (knowledge graph), pertinent maintenant (context graph), suite (procedural graph).
- **Knowledge graph** : faits stables, *« enterprise-wide memory »* ; nœuds de l'exemple : Passenger, Aircraft, Fare, Flight, Route, Airport, Weather, Policy.
- **Context graph** : *« Don't retrieve everything. Scope the graph to what this decision needs. »* État vivant (Flight 34/185, Gate C8, 4 seats left, 9 min to close), contexte organisationnel, historique de décisions.
- **Procedural graph** : Check Availability → (si requis) Check Visa ; → Compare Alternatives ; *No Options* → Escalate to human ; *Options Found* → Apply Fare Rules → Resolved. *« Guides the next step. Doesn't dictate it. »*
- **Agent** : raisonne sur le graphe scopé, suit l'arête suivante, s'écarte *« when the graph is wrong »*.
- **Boucle Trace & Learn** (infographie) : Action → stockage des traces de succès et d'échec → retour vers l'agent ; les traces mettent à jour connaissance, contexte et procédure.
- **Semantic Spine** (infographie, absente du texte) : Ontology (*what things are*) → Knowledge Graph (*what's true*) → Context Graph (*what matters now*) → Procedural Graph (*what to do next*) → AI Agent (*acting, and writing it back*).
- **Leçon de l'auteur** : scoper le graphe par étape, stocker la procédure *« as a graph instead of a prompt »*, journaliser chaque décision comme piste d'audit.
- Voisin de [[kb-context-engineering]].

## RésuméDe400mots

Rakesh Gohel, qui développe chez JUTEQ une infrastructure de gouvernance pour agents IA, soutient que chaque décision d'un agent repose sur trois questions : qu'est-ce qui est vrai, qu'est-ce qui compte maintenant, que faut-il faire ensuite. Un knowledge graph répond bien à la première ; chacune des deux autres mérite selon lui son propre graphe.

Il prend l'exemple d'une demande simple adressée à un agent de compagnie aérienne : réacheminer un passager. Le knowledge graph contient ce qui est vrai à l'échelle de l'entreprise : passagers, avions, vols, tarifs, routes, aéroports, météo, politiques, maintenus stables et gouvernés. Le context graph en extrait une petite tranche limitée à la décision en cours : la porte C8, le vol 34/185, quatre places restantes, neuf minutes avant la fermeture, et la manière dont des cas similaires ont été traités. L'infographie résume ce principe : ne pas tout récupérer, mais scoper le graphe à ce dont la décision a besoin.

Le procedural graph stocke les procédures sous forme de triplets procédure-relation-procédure. L'agent passe de la vérification de disponibilité à la comparaison des alternatives puis à la résolution, vérifie le visa si nécessaire, applique les règles tarifaires quand des options existent et escalade vers un humain quand il n'y en a aucune. Le graphe guide l'étape suivante sans la dicter : l'agent raisonne sur le contexte scopé, suit l'arête suivante et reste libre de s'en écarter si le graphe est faux.

Chaque trace est réécrite. Les précédents affinent le contexte, les exécutions échouées corrigent la procédure et les motifs répétés deviennent des faits gouvernés. L'infographie matérialise cette boucle par un stockage « Trace & Learn » qui collecte les traces de succès et d'échec et met à jour connaissance, contexte et procédure.

Elle ajoute un élément absent du texte, la « Semantic Spine », chaîne en cinq maillons : l'ontologie dit ce que sont les choses, le knowledge graph ce qui est vrai, le context graph ce qui compte maintenant, le procedural graph ce qu'il faut faire ensuite, et l'agent agit puis réécrit le résultat.

La leçon de l'auteur tient en trois consignes : scoper le graphe à chaque étape, stocker la procédure comme un graphe plutôt que comme un prompt, et journaliser chaque décision, car ce journal devient la piste d'audit. Le post se conclut en demandant au lecteur lequel des trois graphes manque à son agent.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Rakesh Gohel | PERSONNE | travaille_chez | JUTEQ | ORGANISATION | 0.90 | DYNAMIQUE | déclaré_article |
| Rakesh Gohel | PERSONNE | a_créé | Semantic Spine | CONCEPT | 0.85 | STATIQUE | déclaré_article |
| Rakesh Gohel | PERSONNE | affirme_que | chaque décision d'agent dépend de trois questions : ce qui est vrai, ce qui compte maintenant, ce qu'il faut faire ensuite | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Semantic Spine | CONCEPT | utilise | ontologie | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Semantic Spine | CONCEPT | utilise | knowledge graph | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Semantic Spine | CONCEPT | utilise | context graph | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Semantic Spine | CONCEPT | utilise | procedural graph | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| context graph | CONCEPT | est_basé_sur | knowledge graph | TECHNOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| context graph | CONCEPT | est_basé_sur | traces de décision | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| procedural graph | CONCEPT | remplace | procédure en prompt | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| procedural graph | CONCEPT | permet | escalade humaine | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| agents IA | TECHNOLOGIE | utilise | procedural graph | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| traces de décision | CONCEPT | améliore | procedural graph | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| traces de décision | CONCEPT | permet | piste d'audit | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Rakesh Gohel | PERSONNE | recommande | scoper le graphe à chaque étape plutôt que tout récupérer | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Rakesh Gohel | PERSONNE | recommande | stocker la procédure comme un graphe plutôt que comme un prompt et journaliser chaque décision | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Rakesh Gohel | PERSONNE | affirme_que | le graphe procédural guide l'étape suivante sans la dicter ; l'agent s'en écarte quand le graphe est faux | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Rakesh Gohel | PERSONNE | rôle | Builder chez JUTEQ, gouvernance et infrastructure de preuve pour agents IA ; newsletter Substack | AJOUT |
| JUTEQ | ORGANISATION | secteur | Gouvernance d'agents IA et infrastructure de preuve | AJOUT |
| Semantic Spine | CONCEPT | définition | Chaîne ontologie → knowledge graph → context graph → procedural graph → agent, qui réécrit ses traces | AJOUT |
| context graph | CONCEPT | définition | Sous-graphe scopé à une décision : état vivant, contexte organisationnel, historique de décisions similaires | AJOUT |
| procedural graph | CONCEPT | définition | Procédures stockées en triplets (procédure, relation, procédure) qui guident l'étape suivante d'un agent sans la dicter | AJOUT |
| knowledge graph | TECHNOLOGIE | rôle | Mémoire d'entreprise des faits stables et gouvernés (ce qui est vrai) | AJOUT |
| traces de décision | CONCEPT | rôle | Traces de succès et d'échec réécrites pour mettre à jour connaissance, contexte et procédure | AJOUT |
