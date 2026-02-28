# netflix-uda-unified-data-architecture-knowledge-graph-2025-06-12

## Veille
Architecture données unifiée Netflix, knowledge graph RDF/SHACL, modélisation domaine, Upper metamodel, mappings sémantiques, projections automatiques GraphQL/Avro/Iceberg - Netflix Technology Blog

## Titre Article
Model Once, Represent Everywhere: UDA (Unified Data Architecture) at Netflix

## Date
2025-06-12

## URL
https://netflixtechblog.com/uda-unified-data-architecture-6a6aee261d8d

## Keywords
UDA, Unified Data Architecture, knowledge graph, domain modeling, RDF, SHACL, Upper metamodel, semantic integration, data catalog, schema registry, GraphQL, Avro, Iceberg, Data Mesh, mappings, projections, transpilation, PDM, Sphere, Netflix, content engineering, connected data, ontologies, SPARQL, named graphs, federated schemas, CDC, devil fruit, data discovery, operational reporting, SKOS

## Authors
Alex Hutter, Alexandre Bertails, Claire Wang, Haoyuan He, Kishore Banala, Peter Royal, Shervin Afshar (Netflix Technology Blog)

## Ton
**Profil:** Engineering-Deep-Dive | Institutionnelle tech | Descriptive-Technique | Expert

Netflix engineering team adopte deep technical exposition voice typical Netflix Tech Blog showcasing architectural innovations. Multi-author collaboration (7 engineers) signals cross-team effort. Langage highly specialized (RDF/SHACL, Upper metamodel, semantic mappings, SPARQL) vise senior data engineers. Structure systematic (problem→solution→implementation→results) demonstrates engineering rigor. Tone confident technical authority sharing lessons at scale. Typique big tech engineering blogs (Uber, Airbnb, LinkedIn style) documenting complex systems visant engineering community learning from scale challenges.

## Pense-bêtes
- **Principe fondamental** : "Model once, represent everywhere" - modéliser une fois, représenter partout
- **Problème résolu** : modèles dupliqués/inconsistants, terminologie incohérente, qualité données, connectivité limitée
- **UDA = knowledge graph** pour données connectées en Content Engineering
- **Fondations RDF/SHACL** mais avec défis opérationnels enterprise-scale
- **Upper metamodel** : modèle de tous les modèles, auto-référentiel, auto-descriptif, auto-validant
- **Named-graph-first** information model pour résolution, modularité, gouvernance
- **Domain models** exprimés en RDF conceptuel dans named graphs
- **Data container representations** : interprétations fidèles des systèmes comme données de graphe
- **Mappings** : connectent modèles domaine aux conteneurs données concrets
- **Projections** : produisent conteneurs concrets (GraphQL schema, Data Mesh source, Iceberg table)
- **Transpilation automatique** : domaine model → GraphQL/Avro/Iceberg/Java avec préservation sémantique
- **PDM (Primary Data Management)** : vocabulaires contrôlés avec SKOS, UI générée
- **Sphere** : reporting opérationnel self-service, découverte via concepts métier
- **Upper construit sur RDFS/OWL/SHACL** mais abstraction plus élevée
- **GraphQL Federation** : support génération schémas fédérés
- **Intent-based automation** : UDA raisonne sur mouvement données préservant sémantique
- **Knowledge graph unifie** : modèles domaine + schémas transpilés + mappings
- **Programmable via Java/GraphQL/SPARQL**
- **Catalog sémantique** : ne trace que assets connectés aux domain models
- **Spider-Man problem** : même concept ("movie") modélisé différemment partout

## RésuméDe400mots

Netflix présente UDA (Unified Data Architecture), une infrastructure révolutionnaire basée sur un knowledge graph pour résoudre la fragmentation chronique des modèles de données à l'échelle de son écosystème Content Engineering. Le problème fondamental : des concepts métier centraux comme "actor" ou "movie" sont redéfinis indépendamment dans chaque système (GraphQL Gateway, asset management, media computing), créant duplication, incohérences terminologiques, problèmes qualité, et connectivité limitée.

**Architecture fondamentale : Knowledge Graph RDF/SHACL**

UDA adopte RDF et SHACL comme fondations techniques, mais confronte des défis opérationnels majeurs à l'échelle entreprise : RDF manquait d'information model utilisable, SHACL n'était pas conçu pour données enterprise avec schémas locaux et clés typées, les équipes manquaient de pratiques d'authoring partagées, et l'outillage ontologie n'offrait pas support pour modélisation collaborative. Solution : information model "named-graph-first" où chaque named graph se conforme à un governing model, lui-même named graph dans le knowledge graph.

**Upper Metamodel : Le modèle de tous les modèles**

Upper constitue le langage formel pour décrire domaines métier ou systèmes, organisant concepts en domain models : vocabulaires contrôlés définissant classes d'entités clés, attributs, relations. Crucially, Upper est bootstrapping upper ontology : auto-référentiel (modélise lui-même), auto-descriptif (définit concept de domain model), auto-validant (conforme à son propre modèle). Upper projette vers API Java Jena-based et schéma GraphQL fédéré dans Enterprise Gateway. Comme tous domain models sont extensions conservatives d'Upper, intégration seamless runtime garantit sémantique données cohérente.

**Mappings et Projections : Connexion et Automation**

Mappings connectent éléments domain models aux data container representations (GraphQL resolvers, Data Mesh sources, Iceberg tables). Tout est adressable : du domain model à l'attribut spécifique, du table Iceberg à la colonne individuelle. Mappings permettent discovery bidirectionnelle : du concept métier au système physique stockant données, et inverse. Projections produisent conteneurs concrets implémentant caractéristiques dérivées du domain model enregistré, avec transpilation automatique vers GraphQL/Avro schemas preservant sémantique.

**Adopteurs Production : PDM et Sphere**

PDM (Primary Data Management) gère vocabulaires contrôlés authoritative utilisant modèle SKOS (W3C). Prend domain model comme input, génère UI automatiquement, provisionne Domain Graph Services et pipelines Data Mesh via projections UDA. Vocabulaires consommateurs ignorent SKOS—travaillent avec terminologie domaine familière.

Sphere : système reporting opérationnel self-service UDA-powered. Discovery via concepts métier ("actors", "movies"), non tables techniques. UDA knowledge graph génère requêtes SQL via graph traversal, éliminant joins manuels et médiation technique. Métadonnées agrégées présentées avec vocabulaire unifié, boundaries et islands data landscape identifiées automatiquement.

**Impact transformationnel**

UDA transforme modèles conceptuels en control plane actif : non seulement documente concepts, mais génère schémas, provisionne services, orchestre data movement, et enforce consistency automatiquement. Futurs développements : support Protobuf/gRPC, matérialisation knowledge graph instance data, résolution challenges Graph Search initiaux ayant inspiré ce travail.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Netflix | ORGANISATION | a_développé | UDA | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| UDA | TECHNOLOGIE | est_basé_sur | RDF | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| UDA | TECHNOLOGIE | est_basé_sur | SHACL | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Upper | TECHNOLOGIE | est_composant_de | UDA | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Upper | TECHNOLOGIE | génère | GraphQL | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Upper | TECHNOLOGIE | génère | Avro | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| UDA | TECHNOLOGIE | permet | PDM | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| UDA | TECHNOLOGIE | permet | Sphere | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| PDM | TECHNOLOGIE | utilise | SKOS | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Sphere | TECHNOLOGIE | génère | requêtes SQL | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| UDA | TECHNOLOGIE | résout | duplication_modèles | CONCEPT | 0.97 | ATEMPOREL | inféré |
| UDA | TECHNOLOGIE | connecte | domain models | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Netflix | ORGANISATION | applique | principe "Model Once Represent Everywhere" | CONCEPT | 0.94 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Netflix | ORGANISATION | secteur | Streaming / Content Engineering | AJOUT |
| UDA | TECHNOLOGIE | catégorie | Architecture données unifiée basée sur knowledge graph | AJOUT |
| Upper | TECHNOLOGIE | rôle | Métamodèle auto-référentiel pour modélisation domaine | AJOUT |
| PDM | TECHNOLOGIE | fonction | Gestion vocabulaires contrôlés et taxonomies | AJOUT |
| Sphere | TECHNOLOGIE | fonction | Reporting opérationnel self-service UDA-powered | AJOUT |
| RDF | TECHNOLOGIE | rôle | Fondation technique knowledge graph UDA | AJOUT |
| SHACL | TECHNOLOGIE | rôle | Validation et contraintes du knowledge graph UDA | AJOUT |
| Data Mesh | TECHNOLOGIE | rôle | Plateforme de mouvement de données dans l'écosystème Netflix | AJOUT |
| SKOS | TECHNOLOGIE | standard | W3C - modélisation de connaissances pour PDM | AJOUT |
| principe "Model Once Represent Everywhere" | CONCEPT | nature | Principe architectural central d'UDA | AJOUT |
