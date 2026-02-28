# context-engineering-domain-understanding-johnson-2025-07-23

## Veille
Context Engineering - Domain Understanding - DICE - Rod Johnson - LLM - Domain Model - Embabel

## Titre Article
Context Engineering Needs Domain Understanding

## Date
2025-07-23

## URL
https://medium.com/@springrod/context-engineering-needs-domain-understanding-b4387e8e4bf8

## Keywords
Context Engineering, Domain Understanding, LLM, Gen AI, Domain-Integrated Context Engineering (DICE), AI Agents, Business Value, Domain Model, Embabel, Prompt Engineering, bidirectional communication, structured context, testability

## Authors
Rod Johnson

## Ton
**Profil:** Professionnel-Technique | Première personne thought leader | Analytique-Prescriptive | Expert

Johnson (Spring Framework creator) adopte authoritative technical voice combinant software architecture expertise et Gen AI insights. Introduction nouveau concept DICE (Domain-Integrated Context Engineering) reveals framework builder mindset. Langage technique assumé (domain objects, bidirectional communication, structured persistence, Cypher queries) vise enterprise architects. Structure critique → proposition → benefits demonstrates systematic thinking. Emphasis integration existing systems over isolated capabilities shows pragmatic enterprise focus. Tone measured authoritative évitant both dismissive skepticism et naive enthusiasm. Typique technical thought leadership (Martin Fowler, Kent Beck style) proposing architectural patterns grounded practical experience.

## Pense-betes
- **"Context engineering"** plus précis que "prompt engineering" pour LLM apps
- **Context engineering traditionnel** overlook bidirectional nature (inputs AND outputs) et relation avec existing business apps
- **DICE (Domain-Integrated Context Engineering)** proposé : emphasize domain model pour structurer context et considérer LLM outputs
- **Domain objects** définissent focused behavior exposable à code manuel ET LLMs comme tools
- **Bénéfices DICE** : code pour structurer context, intégration easier/safer avec existing systems, delivery acceleré via reuse, structured persistence, improved testability, better debugging/tracing, enhanced context manipulation in multi-step flows
- **LLMs excellent avec natural language, mais adding structure** rend safer et more reliable
- **Business value réel Gen AI** nécessite bridging gap entre LLM capabilities et proven existing systems
- **Domain integration critique** pour unlock full business value, existing business apps = key adjacency pour Gen AI

## RésuméDe400mots

L'article "Context Engineering Needs Domain Understanding" de Rod Johnson introduit **Domain-Integrated Context Engineering (DICE)** comme évolution de context engineering pour construire LLM applications plus effectives et robustes. Johnson commence en reconnaissant "context engineering" comme valuable advancement sur "prompt engineering", le définissant comme art et science de populating LLM's context window avec relevant information. Néanmoins, il argue que cette définition est incomplete, failing to address deux aspects cruciaux : bidirectional nature de LLM communication (ce qui est envoyé *et* ce qui est reçu) et integration des LLM applications avec existing business understanding et systems.

**DICE : Extension Conceptuelle**

Pour bridge ces gaps, Johnson propose DICE, qui extend context engineering en emphasizing use d'un domain model pour structurer context et en considérant LLM outputs en plus de inputs. Le core idea est que bien que LLMs excellent avec natural language, **adding structure à inputs et outputs** les rend safer et more reliable. DICE enables LLMs à "converse" utilisant established terminology et concepts d'un business, fostering better integration avec existing applications. Domain objects, dans ce contexte, ne sont pas just data structures mais définissent focused behavior qui peut être exposed à manually authored code ET à LLMs comme tools.

**Bénéfices Compelling de DICE**

L'article highlights plusieurs bénéfices compelling d'adopting DICE. Premièrement, permet use de code pour structurer context, transforming "delicate art" en more scientific process où context peut être refined, reasoned about, et tested. Cela permet aussi precise filtering de content, improving results et saving tokens. Deuxièmement, DICE facilite easier et safer integration avec existing systems, moving beyond "demo-grade" Gen AI applications vers real-world scenarios où agents need to access existing functionality. En working avec domain objects, businesses peuvent reuse existing domain models, leveraging hard-won business understanding.

**Advantages Additionnels**

Further advantages incluent accelerated delivery et improved quality through reuse de domain models across applications et agents. DICE offre aussi structured persistence options, allowing plus precise retrieval using existing technologies comme SQL ou Cypher, potential supplement à vector search. L'added structure et encapsulation provided par domain model enhance testability, debugging, et tracing, car information appears dans observability tools dans structured, understandable format. Finalement, domain integration aide manage context dans multi-step flows, preventing quality degradation et controlling token usage costs.

**Positionnement Stratégique**

Johnson conclut que domain integration est paramount pour unlocking full business value de Generative AI, positioning existing business applications comme key adjacency pour Gen AI, plutôt que solely data science ou LLMs themselves. **L'argument central** : domain model structure transforme LLM capabilities de powerful-but-chaotic vers controlled-and-reliable, essential pour enterprise adoption. En conceptualizing domain objects comme behavior-defining entities exposable comme tools, DICE bridges conceptual gap entre LLM potential et enterprise reality, offrant framework pour systematic, reliable, et valuable Gen AI integration dans business workflows existants. Cette perspective pragmatique reconnaît que **Gen AI value réside not dans isolation**, mais dans harmonious integration avec proven systems où domain knowledge réside.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Rod Johnson | PERSONNE | a_créé | DICE | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Rod Johnson | PERSONNE | a_créé | Spring | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Rod Johnson | PERSONNE | a_fondé | Embabel | ORGANISATION | 0.99 | STATIQUE | déclaré_article |
| DICE | CONCEPT | est_basé_sur | context engineering | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| DICE | CONCEPT | améliore | context engineering | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| context engineering | CONCEPT | améliore | prompt engineering | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | a_défini | context engineering | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| DICE | CONCEPT | utilise | modèle de domaine | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| modèle de domaine | CONCEPT | améliore | intégration systèmes existants | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Embabel | ORGANISATION | démontre | approche DICE | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| MCP | TECHNOLOGIE | s_oppose_à | DICE | CONCEPT | 0.75 | ATEMPOREL | inféré |
| Martin Fowler | PERSONNE | a_conceptualisé | bounded contexts | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| bounded contexts | CONCEPT | fait_partie_de | modèle de domaine | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Rod Johnson | PERSONNE | rôle | Créateur Spring Framework, Fondateur Embabel | AJOUT |
| DICE | CONCEPT | définition | Domain-Integrated Context Engineering — extension du context engineering intégrant un modèle de domaine pour structurer inputs et outputs LLM | AJOUT |
| context engineering | CONCEPT | définition | Art et science de remplir la fenêtre de contexte LLM avec les bonnes informations (définition Karpathy) | AJOUT |
| Embabel | ORGANISATION | secteur | Plateforme IA agentic basée sur JVM, démontre l'approche DICE | AJOUT |
| modèle de domaine | CONCEPT | rôle | Structure les objets métier avec comportements exposables comme outils aux LLMs | AJOUT |
| bounded contexts | CONCEPT | origine | Concept de Martin Fowler appliqué à la structuration des contextes LLM | AJOUT |
| MCP | TECHNOLOGIE | limite | Interactions semi-typées perdant de la fidélité par rapport aux domain objects | AJOUT |
