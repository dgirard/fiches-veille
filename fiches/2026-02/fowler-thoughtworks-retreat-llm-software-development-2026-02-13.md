# fowler-thoughtworks-retreat-llm-software-development-2026-02-13

## Veille

Retraite Thoughtworks sur l'avenir du développement logiciel avec les LLM — réflexions sur l'impact organisationnel, la dette cognitive et la programmation supervisée

## Titre Article

Fragments: February 13

## Date

2026-02-13

## URL

https://martinfowler.com/fragments/2026-02-13.html

## Keywords

LLM, développement logiciel, agents IA, dette cognitive, expérience développeur, intensification du travail, programmation supervisée, architecture logicielle, Thoughtworks, taille des équipes, pair programming, refactoring, IDE, épuisement professionnel

## Authors

Martin Fowler

## Ton

**Profil** : Perspective narrative à la première personne, registre professionnel réflexif, niveau technique intermédiaire-avancé.

**Description** : Le ton est celui d'un observateur chevronné et respecté de l'industrie logicielle, qui rapporte et synthétise les discussions d'une retraite entre pairs de haut niveau. L'écriture est caractéristique de Fowler : sobre, nuancée, évitant les hyperboles. Il alterne entre le compte-rendu factuel des interventions d'autres experts et ses propres réflexions mesurées. Le style est fragmentaire et délibérément non-conclusif — il pose des questions plutôt que d'imposer des réponses. L'autorité vient de l'expérience et du réseau (les intervenants cités sont tous des figures reconnues). Le public cible est constitué de développeurs seniors, architectes et leaders techniques soucieux de comprendre les transformations en cours sans céder à l'enthousiasme aveugle ni au rejet catégorique.

## Pense-betes

- Les développeurs seniors sont majoritairement optimistes sur les LLM, surtout quand ils se concentrent sur l'architecture — ils comparent la gestion des agents LLM à celle de développeurs juniors
- Un tiers des seniors initialement résistants changent d'avis après des exercices pratiques avec les LLM
- Les développeurs de niveau intermédiaire sont les plus vulnérables : carrière construite avant les LLM, mais sans l'expertise senior pour piloter les agents
- Concept clé de Margaret-Anne Storey : la « dette cognitive » — quand une équipe ne peut plus expliquer ses décisions de conception, elle ne peut plus faire évoluer le code
- Distinction importante entre « cruft » (dégradation par ignorance) et « dette » (coût délibéré et conscient)
- Laura Tacho : le diagramme de Venn entre expérience développeur et expérience agent est un cercle — ce qui aide les devs aide les agents
- Observation critique : les dirigeants font pour les LLM des accommodations qu'ils refusaient de faire pour les humains
- Recherche HBR (Ranganathan & Ye) : l'adoption de l'IA provoque une intensification du travail et de l'épuisement professionnel, les gains initiaux cèdent la place à une baisse de qualité
- Camille Fournier : « tout le monde devient manager » — la programmation supervisée engendre une fatigue de changement de contexte
- Les équipes « deux pizzas » gardent la même taille mais produisent davantage — la question du pair programming avec des agents reste ouverte
- Les IDE évoluent vers un modèle hybride : tâches non-déterministes (LLM) + tâches déterministes (refactoring), avec des possibilités d'orchestration

## RésuméDe400mots

Martin Fowler partage ses réflexions issues de la retraite Thoughtworks sur l'avenir du développement logiciel, un événement réunissant des experts de l'industrie pour examiner l'impact des LLM sur les pratiques de développement.

Premier constat : les développeurs seniors se montrent majoritairement optimistes vis-à-vis des LLM. Leur approche consiste à se concentrer sur l'architecture et à traiter les agents IA comme des développeurs juniors à superviser. Fait notable, un tiers des seniors initialement sceptiques changent d'avis après des exercices pratiques. En revanche, les développeurs de niveau intermédiaire se retrouvent dans une position délicate : leur carrière s'est construite avant l'ère des LLM, mais ils ne disposent pas encore de l'expertise senior nécessaire pour orchestrer efficacement ces outils.

Margaret-Anne Storey introduit le concept de « dette cognitive », décrivant la situation où une équipe devient incapable de modifier son code parce qu'elle ne peut plus expliquer les décisions de conception sous-jacentes. Fowler souligne la distinction entre le « cruft » — la dégradation involontaire par ignorance — et la véritable dette technique, qui implique un choix conscient et un coût calculé.

Laura Tacho propose une observation percutante : le diagramme de Venn entre l'expérience développeur et l'expérience agent est un cercle parfait. Tout ce qui facilite le travail des développeurs humains facilite aussi celui des agents. Paradoxe révélateur : les dirigeants acceptent de faire pour les LLM des aménagements (documentation, clarté du code, environnements propres) qu'ils refusaient obstinément de faire pour leurs équipes humaines.

Du côté des IDE, l'évolution s'oriente vers un modèle hybride combinant des tâches non-déterministes gérées par les LLM et des tâches déterministes comme le refactoring, ouvrant de nouvelles possibilités d'orchestration.

Sur la taille des équipes, le consensus est que les équipes « deux pizzas » conserveront leur taille mais augmenteront leur productivité. La question du pair programming avec des agents reste ouverte et prometteuse.

Des recherches publiées dans la Harvard Business Review par Ranganathan et Ye apportent un contrepoint important : l'adoption de l'IA entraîne une intensification du travail et un épuisement professionnel. Les gains de productivité initiaux laissent place à une dégradation de la qualité sur le moyen terme.

Camille Fournier résume cette tension par la formule « tout le monde devient manager » : la programmation supervisée transforme chaque développeur en gestionnaire d'agents, générant une fatigue liée au changement de contexte permanent. Ce nouveau paradigme exige des compétences de supervision plus que d'exécution directe.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Martin Fowler | PERSONNE | a_participé_à | Thoughtworks Future of Software Development Retreat | EVENEMENT | 0.98 | STATIQUE | déclaré_article |
| Thoughtworks | ORGANISATION | a_organisé | Thoughtworks Future of Software Development Retreat | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Margaret-Anne Storey | PERSONNE | a_introduit | dette cognitive | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Laura Tacho | PERSONNE | affirme_que | expérience développeur équivaut à expérience agent | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Camille Fournier | PERSONNE | affirme_que | programmation supervisée | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Ranganathan & Ye | PERSONNE | a_publié | recherche intensification travail IA | EVENEMENT | 0.90 | STATIQUE | déclaré_article |
| LLM | TECHNOLOGIE | transforme | développement logiciel | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Développeurs seniors | CONCEPT | comparent | agents LLM à développeurs juniors | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Développeurs intermédiaires | CONCEPT | sont_vulnérables_face_à | adoption des LLM | CONCEPT | 0.85 | DYNAMIQUE | inféré |
| Adoption IA | CONCEPT | provoque | intensification du travail | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Adoption IA | CONCEPT | provoque | épuisement professionnel | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| IDE | TECHNOLOGIE | évolue_vers | modèle hybride déterministe/non-déterministe | CONCEPT | 0.82 | DYNAMIQUE | déclaré_article |
| Programmation supervisée | CONCEPT | engendre | fatigue de changement de contexte | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Dette cognitive | CONCEPT | empêche | évolution du code | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Martin Fowler | PERSONNE | rôle | Auteur, Chief Scientist Thoughtworks | AJOUT |
| Thoughtworks | ORGANISATION | secteur | Conseil en technologies / Développement logiciel | AJOUT |
| Margaret-Anne Storey | PERSONNE | rôle | Chercheuse en génie logiciel | AJOUT |
| Laura Tacho | PERSONNE | rôle | Experte en expérience développeur | AJOUT |
| Camille Fournier | PERSONNE | rôle | Leader technique, auteure | AJOUT |
| Ranganathan & Ye | PERSONNE | rôle | Chercheurs publiés dans HBR | AJOUT |
| Dette cognitive | CONCEPT | catégorie | Risque lié à l'utilisation des LLM en développement | AJOUT |
| Programmation supervisée | CONCEPT | catégorie | Nouveau paradigme de développement avec agents IA | AJOUT |
| Thoughtworks Future of Software Development Retreat | EVENEMENT | date | 2026-02 | AJOUT |
| Harvard Business Review | ORGANISATION | secteur | Publication académique / Management | AJOUT |
