# martin-fowler-llm-software-development-2025-08-15
## Veille
Réflexions sur LLMs et développement logiciel - Bulle IA - Hallucinations - Sécurité - Martin Fowler
## Titre Article
Some thoughts on LLMs and Software Development
## Date
2025-08-15
## URL
https://martinfowler.com/articles/202508-ai-thoughts.html
## Keywords
LLM, AI, Software Development, Bubble, Hallucinations, Non-determinism, Security, Attack Surface, Martin Fowler
## Authors
Martin Fowler

## Ton
**Profil:** Elder-Statesman-Reflective | Première personne authority | Analytique-Balanced | Expert

Fowler (ThoughtWorks Chief Scientist) adopte measured authority voice offering nuanced AI software development perspective. Characteristic intellectual honesty ("BIEN SÛR QUE C'EST UNE BULLE") demonstrates willingness state uncomfortable truths. Langage thoughtful balanced (hallucinations as features, non-determinism challenges, security implications) avoids both boosterism et dismissiveness. Tone experienced practitioner wisdom accumulated decades software evolution. Structure exploratory essay typical Fowler's writing encouraging reader critical thinking. Typique software industry thought leaders (Kent Beck, Robert Martin style) offering measured perspectives grounded deep experience visant practitioners seeking balanced guidance amidst hype.

## Pense-betes
- Enquêtes actuelles sur IA peu fiables : ne distinguent pas usages (auto-complétion vs édition directe code)
- Édition directe code par IA a bien plus de valeur qu'auto-complétion
- Avenir programmation : incertain, personne ne sait vraiment
- "BIEN SÛR QUE C'EST UNE BULLE" - comme canaux, chemins fer, internet
- Bulle éclatera, mais entreprises survivront et prospéreront (comme Amazon post dot-com)
- Hallucinations = fonctionnalité, pas bug (Rebecca Parsons)
- LLM produit hallucinations, certaines sont utiles
- Toujours poser même question plusieurs fois, comparer réponses
- Ne pas demander calculs déterministes aux LLM
- IA marque entrée ingénierie logicielle dans monde non-déterministe
- LLM peut affirmer "tests au vert" alors qu'il y a échecs
- Surface d'attaque massif : "Trifecta Mortelle" (Simon Willison) = données privées + contenu non fiable + capacité exfiltration
- Extensions navigateur agentiques "fondamentalement défectueuses", impossibles à construire en sécurité
## RésuméDe400mots
Martin Fowler partage ses réflexions sur l'impact des grands modèles linguistiques (LLM) et de l'intelligence artificielle sur le développement logiciel. Il commence par critiquer les enquêtes actuelles sur l'IA dans le développement, soulignant qu'elles ne tiennent pas compte des différentes manières dont les développeurs utilisent les LLM. La plupart des usages se limitent à de l'auto-complétion, comme avec Copilot, alors que les utilisateurs qui en tirent le plus de valeur préfèrent des approches permettant aux LLM de lire et d'éditer directement le code source pour accomplir des tâches. Fowler craint que des données de sondage incomplètes n'orientent les gens vers de mauvaises pratiques.

Concernant l'avenir de la programmation, Fowler admet ne pas avoir la moindre idée de ce qu'il adviendra. Il rejette l'idée que quiconque puisse prédire avec certitude si les LLM élimineront les ingénieurs juniors ou si les seniors devraient quitter la profession. Il encourage plutôt l'expérimentation personnelle et le partage d'expériences pour comprendre comment utiliser au mieux ces technologies en constante évolution.

Fowler aborde également la question de savoir si l'IA est une bulle économique. Sa réponse est un "BIEN SÛR QUE C'EST UNE BULLE". Il compare la situation aux bulles technologiques passées (canaux, chemins de fer, internet), affirmant qu'il est presque certain que cette bulle éclatera, entraînant la disparition de nombreux investissements. Cependant, il est impossible de prédire quand cela se produira et quelle valeur réelle aura été générée d'ici là. Il rappelle que, comme lors de l'éclatement de la bulle dot-com, certaines entreprises survivront et prospéreront, à l'image d'Amazon.

Une idée clé développée par Fowler, inspirée par Rebecca Parsons, est que les "hallucinations" des LLM ne sont pas un bug, mais une caractéristique fondamentale. Un LLM ne fait que produire des hallucinations, dont certaines s'avèrent utiles. Cette nature non déterministe implique qu'il faut toujours poser la même question à un LLM plusieurs fois, éventuellement avec des reformulations, pour comparer les réponses. La variation des réponses peut être aussi instructive que les réponses elles-mêmes, surtout pour les données numériques. Il déconseille de demander à un LLM de calculer des réponses qui peuvent être obtenues de manière déterministe.

Fowler compare le développement logiciel traditionnel, qui repose sur des machines déterministes, à d'autres formes d'ingénierie qui doivent tenir compte de la variabilité du monde (tolérances structurelles, erreurs humaines). Il suggère que les LLM pourraient marquer le point où l'ingénierie logicielle rejoint ses pairs dans un monde de non-déterminisme. Il note également que, contrairement à un collègue junior, un LLM peut affirmer que "tous les tests sont au vert" alors qu'il y a des échecs, ce qui soulève des questions sur la fiabilité.

Enfin, l'article met en lumière l'augmentation considérable de la surface d'attaque des systèmes logiciels due aux LLM. Fowler cite Simon Willison et sa "Trifecta Mortelle" pour les agents IA : accès aux données privées, exposition à du contenu non fiable et capacité d'exfiltration. Il conclut que le concept même d'une extension de navigateur agissant comme un agent est fondamentalement défectueux et ne peut être construit en toute sécurité.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Martin Fowler | PERSONNE | travaille_chez | ThoughtWorks | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Martin Fowler | PERSONNE | affirme_que | bulle IA | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| bulle IA | CONCEPT | est_comparable_à | bulle dot-com | EVENEMENT | 0.90 | ATEMPOREL | déclaré_article |
| Rebecca Parsons | PERSONNE | affirme_que | hallucinations LLM | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| hallucinations LLM | CONCEPT | est_une | fonctionnalité fondamentale | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| LLM | TECHNOLOGIE | introduit | non-déterminisme | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Simon Willison | PERSONNE | a_défini | Trifecta Mortelle | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Trifecta Mortelle | CONCEPT | combine | données privées + contenu non fiable + exfiltration | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| agents navigateur | TECHNOLOGIE | présente | surface d'attaque élargie | CONCEPT | 0.91 | DYNAMIQUE | déclaré_article |
| Martin Fowler | PERSONNE | critique | enquêtes IA actuelles | CONCEPT | 0.94 | STATIQUE | déclaré_article |
| auto-complétion | METHODOLOGIE | est_inférieure_à | édition directe du code | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| LLM | TECHNOLOGIE | peut_produire | faux positifs de tests | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Martin Fowler | PERSONNE | rôle | Chief Scientist ThoughtWorks, auteur | AJOUT |
| ThoughtWorks | ORGANISATION | secteur | Conseil et ingénierie logicielle | AJOUT |
| Rebecca Parsons | PERSONNE | rôle | Ancienne collègue Fowler, chercheuse | AJOUT |
| Simon Willison | PERSONNE | rôle | Expert sécurité IA, créateur Django | AJOUT |
| Trifecta Mortelle | CONCEPT | définition | données privées + contenu non fiable + exfiltration | AJOUT |
| bulle IA | CONCEPT | analogie | canaux, chemins de fer, internet, dot-com | AJOUT |
| hallucinations LLM | CONCEPT | nature | fonctionnalité inhérente, non bug | AJOUT |
| non-déterminisme | CONCEPT | implication | rapprocher ingénierie logicielle des autres disciplines | AJOUT |
| auto-complétion | METHODOLOGIE | outil_associé | GitHub Copilot | AJOUT |
| agents navigateur | TECHNOLOGIE | statut_sécurité | fondamentalement défectueux selon Willison | AJOUT |
