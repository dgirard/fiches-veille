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
**Profil :** Professionnel-technique | Première personne thought leader | Analytique-prescriptif | Expert

Johnson (créateur du framework Spring) adopte une voix technique autoritaire combinant expertise en architecture logicielle et intuitions Gen AI. L'introduction du nouveau concept DICE (Domain-Integrated Context Engineering) révèle un état d'esprit de bâtisseur de frameworks. Langage technique assumé (domain objects, communication bidirectionnelle, persistance structurée, requêtes Cypher) visant les architectes d'entreprise. La structure critique → proposition → bénéfices témoigne d'une pensée systématique. L'accent mis sur l'intégration aux systèmes existants plutôt que sur des capacités isolées montre un focus enterprise pragmatique. Ton mesuré et autoritaire, évitant à la fois le scepticisme dédaigneux et l'enthousiasme naïf. Typique du thought leadership technique (style Martin Fowler, Kent Beck) proposant des patterns architecturaux ancrés dans l'expérience pratique.

## Pense-betes
- **« Context engineering »** plus précis que « prompt engineering » pour les applications LLM
- **Le context engineering traditionnel** néglige la nature bidirectionnelle (entrées ET sorties) et la relation avec les applications métier existantes
- **DICE (Domain-Integrated Context Engineering)** proposé : mettre l'accent sur le modèle de domaine pour structurer le contexte et considérer les sorties des LLM
- **Les domain objects** définissent des comportements ciblés exposables au code manuel ET aux LLMs comme outils
- **Bénéfices DICE** : code pour structurer le contexte, intégration plus simple/sûre avec les systèmes existants, livraison accélérée via la réutilisation, persistance structurée, testabilité améliorée, meilleur débogage/traçage, manipulation de contexte renforcée dans les flux multi-étapes
- **Les LLMs excellent en langage naturel, mais ajouter de la structure** les rend plus sûrs et plus fiables
- **La valeur métier réelle de la Gen AI** exige de combler le fossé entre capacités des LLM et systèmes existants éprouvés
- **L'intégration du domaine est critique** pour libérer la pleine valeur métier ; les applications métier existantes = adjacence clé pour la Gen AI

## RésuméDe400mots

L'article « Context Engineering Needs Domain Understanding » de Rod Johnson introduit le **Domain-Integrated Context Engineering (DICE)** comme une évolution du context engineering pour construire des applications LLM plus efficaces et robustes. Johnson commence par reconnaître le « context engineering » comme une avancée précieuse par rapport au « prompt engineering », le définissant comme l'art et la science de remplir la fenêtre de contexte du LLM avec les informations pertinentes. Il soutient néanmoins que cette définition est incomplète, car elle néglige deux aspects cruciaux : la nature bidirectionnelle de la communication avec les LLM (ce qui est envoyé *et* ce qui est reçu) et l'intégration des applications LLM avec la compréhension métier et les systèmes existants.

**DICE : extension conceptuelle**

Pour combler ces lacunes, Johnson propose DICE, qui étend le context engineering en mettant l'accent sur l'usage d'un modèle de domaine pour structurer le contexte et en considérant les sorties des LLM en plus des entrées. L'idée centrale : bien que les LLMs excellent en langage naturel, **ajouter de la structure aux entrées et sorties** les rend plus sûrs et plus fiables. DICE permet aux LLMs de « converser » en utilisant la terminologie et les concepts établis d'un métier, favorisant une meilleure intégration avec les applications existantes. Les domain objects, dans ce contexte, ne sont pas de simples structures de données mais définissent des comportements ciblés exposables au code écrit manuellement ET aux LLMs comme outils.

**Bénéfices convaincants de DICE**

L'article met en avant plusieurs bénéfices convaincants de l'adoption de DICE. Premièrement, il permet d'utiliser du code pour structurer le contexte, transformant un « art délicat » en processus plus scientifique où le contexte peut être affiné, raisonné et testé. Cela permet aussi un filtrage précis du contenu, améliorant les résultats et économisant des tokens. Deuxièmement, DICE facilite une intégration plus simple et plus sûre avec les systèmes existants, dépassant les applications Gen AI « de démonstration » vers des scénarios réels où les agents doivent accéder aux fonctionnalités existantes. En travaillant avec des domain objects, les entreprises peuvent réutiliser leurs modèles de domaine existants et capitaliser sur une compréhension métier durement acquise.

**Avantages additionnels**

D'autres avantages incluent une livraison accélérée et une qualité améliorée grâce à la réutilisation des modèles de domaine entre applications et agents. DICE offre aussi des options de persistance structurée, permettant une récupération plus précise via des technologies existantes comme SQL ou Cypher, complément potentiel à la recherche vectorielle. La structure et l'encapsulation ajoutées par le modèle de domaine renforcent la testabilité, le débogage et le traçage, car l'information apparaît dans les outils d'observabilité sous un format structuré et compréhensible. Enfin, l'intégration du domaine aide à gérer le contexte dans les flux multi-étapes, prévenant la dégradation de qualité et maîtrisant les coûts de tokens.

**Positionnement stratégique**

Johnson conclut que l'intégration du domaine est primordiale pour libérer la pleine valeur métier de l'IA générative, positionnant les applications métier existantes comme l'adjacence clé de la Gen AI, plutôt que la seule data science ou les LLMs eux-mêmes. **L'argument central** : la structure du modèle de domaine fait passer les capacités des LLM de puissantes-mais-chaotiques à contrôlées-et-fiables, condition essentielle de l'adoption en entreprise. En conceptualisant les domain objects comme des entités porteuses de comportements exposables comme outils, DICE comble le fossé conceptuel entre le potentiel des LLM et la réalité de l'entreprise, offrant un cadre pour une intégration Gen AI systématique, fiable et créatrice de valeur dans les workflows métier existants. Cette perspective pragmatique reconnaît que **la valeur de la Gen AI ne réside pas dans l'isolement**, mais dans l'intégration harmonieuse avec les systèmes éprouvés où réside la connaissance du domaine.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Rod Johnson | PERSONNE | a_créé | DICE | METHODOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Rod Johnson | PERSONNE | a_créé | Spring | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Rod Johnson | PERSONNE | a_créé | Embabel | ORGANISATION | 0.99 | STATIQUE | déclaré_article |
| DICE | METHODOLOGIE | est_basé_sur | context engineering | METHODOLOGIE | 0.98 | STATIQUE | déclaré_article |
| DICE | METHODOLOGIE | améliore | context engineering | METHODOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| context engineering | METHODOLOGIE | améliore | prompt engineering | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé | context engineering | METHODOLOGIE | 0.97 | STATIQUE | déclaré_article |
| DICE | METHODOLOGIE | utilise | modèle de domaine | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| modèle de domaine | CONCEPT | améliore | intégration systèmes existants | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Embabel | ORGANISATION | utilise | approche DICE | METHODOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| MCP | TECHNOLOGIE | s_oppose_à | DICE | METHODOLOGIE | 0.75 | ATEMPOREL | inféré |
| Martin Fowler | PERSONNE | a_créé | bounded contexts | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| bounded contexts | CONCEPT | fait_partie_de | modèle de domaine | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Rod Johnson | PERSONNE | rôle | Créateur Spring Framework, Fondateur Embabel | AJOUT |
| DICE | METHODOLOGIE | définition | Domain-Integrated Context Engineering — extension du context engineering intégrant un modèle de domaine pour structurer inputs et outputs LLM | AJOUT |
| context engineering | METHODOLOGIE | définition | Art et science de remplir la fenêtre de contexte LLM avec les bonnes informations (définition Karpathy) | AJOUT |
| Embabel | ORGANISATION | secteur | Plateforme IA agentic basée sur JVM, démontre l'approche DICE | AJOUT |
| modèle de domaine | CONCEPT | rôle | Structure les objets métier avec comportements exposables comme outils aux LLMs | AJOUT |
| bounded contexts | CONCEPT | origine | Concept de Martin Fowler appliqué à la structuration des contextes LLM | AJOUT |
| MCP | TECHNOLOGIE | limite | Interactions semi-typées perdant de la fidélité par rapport aux domain objects | AJOUT |
