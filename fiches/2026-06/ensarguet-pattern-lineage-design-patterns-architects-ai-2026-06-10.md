---
themes: [architecture-construction]
source: "LinkedIn (Philippe Ensarguet)"
---
# ensarguet-pattern-lineage-design-patterns-architects-ai-2026-06-10

## Veille

Philippe Ensarguet (Orange) soutient que cinquante ans de design patterns forment une lignée continue : à l'heure où l'IA banalise le code et casse l'apprentissage traditionnel des architectes, la « pattern literacy » (lire un système par ses forces invariantes) devient la compétence durable à enseigner — comme une grammaire, pas comme des catalogues.

## Titre Article

The pattern lineage: Why fifty years of design patterns may hold the key to growing the architects AI cannot replace

## Date

2026-06-10

## URL

https://www.linkedin.com/pulse/pattern-lineage-why-fifty-years-design-patterns-may-hold-ensarguet-sldae/

## Keywords

design patterns, lignée des patterns, architecte logiciel, pattern literacy, jugement architectural, Christopher Alexander, Gang of Four, Hillside Group, forces invariantes, couplage et cohésion, frontière d'abstraction, isolation des pannes, gouvernance de l'état, indirection, boucle de rétroaction, non-déterminisme, IA agentique, platformisation, télécom, control plane / user plane, upskilling, montée en compétences, transmission du jugement

## Authors

Philippe Ensarguet

## Ton

Profil : tribune réflexive d'un dirigeant technique (perspective « je », CTO/VP Engineering chez un opérateur télécom), registre essayiste-professionnel en anglais, niveau technique élevé mais accessible, public cible architectes, CTO, responsables d'ingénierie et de formation. Le ton est celui d'une « intuition sous construction » assumée : Ensarguet expose une thèse personnelle, la documente historiquement (50 ans de livres de patterns, références bibliographiques fournies) et la soumet explicitement au débat (« I am publishing it precisely to stress-test it »). Autorité fondée sur l'expérience (« I'm 53 », 30 ans de métier, bibliothèque personnelle citée) et sur une généalogie rigoureuse reliant Alexander, le Gang of Four et les catalogues agentiques de 2024-2026. Style narratif structuré en mouvements (le pipeline qui casse, ce qu'est vraiment un pattern, l'arbre généalogique, les archétypes, la grammaire à enseigner), métaphores filées (l'arbre généalogique, la grammaire vs le catalogue, le pattern qui « change de vêtements sans changer de but »).

## Pense-betes

- **Paradoxe central** : le rôle d'architecte devient critique au moment précis où son pipeline de formation se brise — l'IA absorbe le travail d'entrée de gamme (écrire du code) qui forgeait jadis le jugement des architectes.
- **Thèse** : la réponse à « quoi enseigner aux futurs architectes » est sur les étagères depuis des années — la lignée des design patterns, lue comme une histoire continue.
- **Définition d'un pattern (Alexander, 1977)** : solution nommée et récurrente à un problème dans un contexte, incluant les forces en tension et les conséquences. Ce n'est pas une recette, c'est du **jugement mis en forme transmissible**.
- **Distinction recette vs jugement** : une recette dit quoi faire ; elle ne dit jamais quand ne PAS faire, ni ce qu'on sacrifie. Le jugement = décider sous pression en connaissant le coût de chaque option — ce que l'IA ne peut pas retirer.
- **Valeur durable du livre du Gang of Four** : pas les 23 patterns, mais le **format** (problème, contexte, forces, solution, conséquences) qui rend un compromis discutable et enseignable.
- **Arbre généalogique** : GoF (1994) → POSA (1996) → Fowler PEAA (2002) → Hohpe & Woolf EIP (2003) → Nygard Release It! (2007) → cloud (Wilder 2012, Azure/AWS) → Microservices/Cloud Native/Kubernetes Patterns (2018-2019) → catalogues agentiques (Anthropic, Ng) 2024-2026.
- **Six forces invariantes** : couplage/cohésion, frontière d'abstraction, isolation des pannes, gouvernance de l'état, indirection, boucle de rétroaction. **+ une septième** : le non-déterminisme (les systèmes agentiques cassent l'hypothèse d'acteurs déterministes → evaluators, reflectors, validation gates).
- **Filiation concrète** : Circuit Breaker (Nygard 2007) devient un champ de config dans un service mesh ; Proxy (1994) → Sidecar (cloud-native) → guardrails LLM ; prompt chaining (Anthropic) = Pipes and Filters.
- **Convergence IT / réseau télécom** : control plane / user plane = frontière d'abstraction + indirection ; network slicing = Bulkhead à l'échelle carrier ; intent-based networking = boucle de rétroaction (modèle opérateur Kubernetes). La grammaire est commune aux deux mondes.
- **L'IA comme alliée** : libérée de l'implémentation, la formation peut devenir délibérée — l'IA génère 3 architectures candidates, l'apprenti nomme les forces, pèse les compromis, justifie une décision. La machine produit des options, l'humain fournit le jugement.
- **Conclusion** : enseigner la **grammaire** (lire les forces), pas les **catalogues** (qui vieillissent). « The catalogues age; the way of thinking they encode does not. »

## RésuméDe400mots

Philippe Ensarguet (Orange) part d'une question en apparence administrative — concevoir un parcours de montée en compétences vers le rôle d'architecte — pour formuler une intuition de fond. Ce rôle est critique pour la « platformisation » d'un opérateur télécom (réunir les mondes IT et réseau, séparés depuis des décennies, en plateformes programmables). Or il devient critique au moment précis où son pipeline de formation se brise : la demande d'architectes augmente (platforming, cloud-native, IA agentique déplacent la complexité des composants vers les relations entre eux), tandis que la chaîne d'approvisionnement en talents se démantèle. Le chemin traditionnel passait par des années d'écriture de code ; l'IA en absorbe désormais une part croissante. Si le travail d'entrée de gamme qui forgeait les architectes est délégué aux machines, d'où viendra la prochaine génération ?

La réponse, selon Ensarguet, est sur les étagères depuis cinquante ans. Il revient au sens originel d'un pattern, défini par l'architecte-bâtisseur Christopher Alexander (1977) : une solution nommée et récurrente à un problème dans un contexte, incluant les forces en tension et les conséquences. Ce n'est pas une recette, c'est du jugement transmissible. Le livre du Gang of Four (1994), issu du Hillside Group réuni par Kent Beck et Grady Booch, a donné à l'industrie son premier vocabulaire partagé — sa valeur durable étant le format (problème, contexte, forces, solution, conséquences), pas les 23 patterns.

Ensarguet déroule un arbre généalogique : POSA (1996), Fowler (2002), Hohpe & Woolf (2003), Nygard (2007, Circuit Breaker), les catalogues cloud (2012+), microservices et Kubernetes (2018-2019), jusqu'aux corpus agentiques en train de se former (Anthropic « Building Effective Agents », les quatre patterns d'Andrew Ng, le cadre à deux axes de Huang & Zhou en 2026 — écho des deux axes du GoF trente ans plus tôt). Sous les catalogues subsistent six forces invariantes : couplage/cohésion, frontière d'abstraction, isolation des pannes, gouvernance de l'état, indirection, boucle de rétroaction — auxquelles s'ajoute une septième, le non-déterminisme introduit par les systèmes agentiques.

Cette « pattern literacy » est la compétence résiliente, et la seule à enfin relier IT et réseau (control plane/user plane = indirection ; network slicing = Bulkhead ; intent-based networking = boucle de rétroaction). L'IA devient alors alliée : libérée de l'implémentation, la formation peut être délibérée — la machine produit des options, l'humain fournit le jugement. Il faut enseigner la grammaire, pas les catalogues : les catalogues vieillissent, la façon de penser qu'ils encodent, non. Ensarguet publie cette thèse pour la mettre à l'épreuve du débat.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Philippe Ensarguet | PERSONNE | travaille_chez | Orange | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Philippe Ensarguet | PERSONNE | publie | The pattern lineage | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Philippe Ensarguet | PERSONNE | affirme_que | la pattern literacy est la compétence durable que l'IA ne peut remplacer | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Philippe Ensarguet | PERSONNE | recommande | enseigner la grammaire des patterns, pas les catalogues | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Christopher Alexander | PERSONNE | a_créé | concept de design pattern | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| design patterns | METHODOLOGIE | permet | transmission du jugement architectural entre générations | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Gang of Four | DOCUMENT | s_inspire_de | travaux de Christopher Alexander | DOCUMENT | 0.90 | STATIQUE | déclaré_article |
| Kent Beck | PERSONNE | a_créé | Hillside Group | ORGANISATION | 0.88 | STATIQUE | déclaré_article |
| pattern literacy | METHODOLOGIE | s_applique_à | rôle d'architecte logiciel | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| IA agentique | TECHNOLOGIE | réduit | apprentissage traditionnel des architectes par l'écriture de code | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| design patterns agentiques | METHODOLOGIE | est_basé_sur | forces invariantes nommées depuis des décennies | CONCEPT | 0.88 | ATEMPOREL | inféré |
| prompt chaining | METHODOLOGIE | est_variante_de | Pipes and Filters | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| non-déterminisme | CONCEPT | affine | les six forces invariantes des patterns | CONCEPT | 0.87 | ATEMPOREL | déclaré_article |
| Philippe Ensarguet | PERSONNE | affirme_que | le rôle d'architecte devient critique quand son pipeline de formation se brise | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| pattern literacy | METHODOLOGIE | converge_avec | mondes IT et réseau télécom | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | publie | Building Effective Agents | DOCUMENT | 0.90 | STATIQUE | déclaré_article |
| IA | TECHNOLOGIE | permet | formation délibérée au jugement architectural | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Philippe Ensarguet | PERSONNE | rôle | Orange Fellow, VP Cloud & Software Engineering | AJOUT |
| Orange | ORGANISATION | secteur | Opérateur télécom | AJOUT |
| Christopher Alexander | PERSONNE | rôle | Architecte-bâtisseur, théoricien des patterns | AJOUT |
| design patterns | METHODOLOGIE | catégorie | Mécanisme de transmission du jugement architectural | AJOUT |
| pattern literacy | METHODOLOGIE | définition | Lire un système par ses forces invariantes | AJOUT |
| Gang of Four | DOCUMENT | nature | Design Patterns (Gamma, Helm, Johnson, Vlissides, 1994) | AJOUT |
| Hillside Group | ORGANISATION | rôle | Groupe fondateur des conférences Pattern Languages of Programs | AJOUT |
| Kent Beck | PERSONNE | rôle | Co-initiateur du Hillside Group | AJOUT |
| forces invariantes | CONCEPT | liste | Couplage/cohésion, frontière d'abstraction, isolation des pannes, gouvernance de l'état, indirection, boucle de rétroaction, non-déterminisme | AJOUT |
| non-déterminisme | CONCEPT | rôle | Septième force introduite par les systèmes agentiques | AJOUT |
| IA agentique | TECHNOLOGIE | rôle | Banalise le code, casse l'apprentissage traditionnel | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
