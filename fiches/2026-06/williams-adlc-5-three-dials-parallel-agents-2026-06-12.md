---
themes: [agents-codage-ia-skills]
source: "voodootikigod.com (Chris Williams)"
---
# williams-adlc-5-three-dials-parallel-agents-2026-06-12

## Veille

Cinquième volet ADLC : orchestrer des agents en parallèle sans « merge hell ». Williams pose trois cadrans couplés — coût (choix du modèle), temps mural (largeur de parallélisation), précision (qualité des contrats) — et un principe d'architecture : « control flow is code; judgment is models » (des scripts déterministes orchestrent, les modèles ne fournissent que le jugement). Quatre lanes (Contract Desk frontier, Builder Pool single-writer, Prosecution Pool partagé, Integrator séquentiel), un forecast de conflits de merge à partir de quatre signaux (largeur certifiée typiquement 3-5 agents), et la désambiguïsation par consensus de N agents pas chers plutôt que par questions de clarification.

## Titre Article

Three Dials: Parallel Agents Without Merge Hell

## Date

2026-06-12

## URL

https://www.voodootikigod.com/adlc-5-three-dials-parallel-agents

## Keywords

ADLC, orchestration multi-agents, trois cadrans, coût-temps-précision, control flow is code, parallélisation, merge hell, lanes, Contract Desk, Builder Pool, single-writer, Prosecution Pool, Integrator, routing de modèle, rail density, escalation ladder, DAG float, merge-forecast, work-stealing queue, désambiguïsation par consensus

## Authors

Chris Williams (@voodootikigod)

## Ton

Profil : exposé d'ingénierie système (perspective praticien en anglais, registre architectural et précis), niveau technique très élevé, public cible ingénieurs plateforme construisant des orchestrateurs d'agents. Le ton est celui de l'optimisation sous contraintes couplées : Williams traite le parallélisme comme un problème d'ordonnancement où trois variables interdépendantes (coût, temps mural, précision) ne peuvent être optimisées séparément. L'autorité s'appuie sur une discipline anti-magique — refuser que des modèles frontier prennent les décisions d'ordonnancement — résumée par l'axiome « control flow is code; judgment is models ». Style à forte densité d'ingénierie : taxonomie de lanes, signaux prédictifs nommés et quantifiés (largeur certifiée 3-5 agents), pratiques de terrain énumérées (batch des permissions, work-stealing queues, ordre de merge foundation → packages → apps).

## Pense-betes

- **Trois cadrans couplés** : coût (sélection du modèle), temps mural (largeur de parallélisation), précision (qualité des contrats). Ils sont liés : le parallélisme n'améliore l'efficience-coût à précision constante que si la partition du travail est propre.
- **Principe d'architecture** : « control flow is code; judgment is models ». Ne pas laisser des modèles frontier prendre les décisions d'ordonnancement — des scripts déterministes orchestrent, les modèles ne fournissent du jugement que là où il est nécessaire.
- **Quatre lanes spécialisées** : Contract Desk (modèle frontier, dessine les contrats), Builder Pool (single-writer par partition), Prosecution Pool (partagé, contextes frais), Integrator Lane (séquentielle).
- **Trois principes de routing de tier** : (1) rail density (couverture de tests, checks déterministes) ; (2) escalation ladder (régénérer à l'échec, monter d'un tier) ; (3) DAG float (l'analyse du chemin critique décide s'il faut « ladder » ou aller direct au tier supérieur).
- **Optimisation du temps mural** : quatre signaux prédisent les conflits de merge **avant** de lancer le travail — chevauchement de scope de fichiers, rayon dans le graphe d'imports, couplage historique de co-changement, collisions de namespace. La largeur certifiée par le forecast tourne typiquement entre **3 et 5 agents**.
- **Précision sans introspection** : au lieu de poser des questions de clarification au modèle, on fan-out des agents pas chers pour générer plusieurs interprétations — « where all N agree, the request is demonstrably unambiguous ». Le désaccord devient une ambiguïté mesurée et actionnable.
- **Pratiques de terrain** : batcher les prompts de permission en pré-vol ; distinguer validateurs in-flight et gates de prosecution ; utiliser des work-stealing queues plutôt que des assignations statiques ; respecter un ordre de merge précis : foundation → shared packages → apps.

## RésuméDe400mots

Le cinquième volet aborde le passage à l'échelle : faire travailler des agents en parallèle sans tomber dans le « merge hell ». Williams pose d'emblée que l'orchestration multi-agents revient à équilibrer trois cadrans interdépendants — le coût (déterminé par le choix du modèle), le temps mural (déterminé par la largeur de parallélisation) et la précision (déterminée par la qualité des contrats). Ces facteurs sont couplés : le parallélisme n'améliore l'efficience-coût à précision constante que si la partition du travail est propre. Augmenter la largeur sans contrats nets dégrade la précision et fait exploser les conflits.

Le principe d'architecture est tranchant : « control flow is code; judgment is models ». Williams refuse de confier les décisions d'ordonnancement à des modèles frontier ; ce sont des scripts déterministes qui orchestrent, les modèles n'intervenant que là où un jugement est réellement requis. Le système s'organise en quatre lanes spécialisées : un Contract Desk (modèle frontier) qui dessine les contrats, un Builder Pool en single-writer par partition (un seul agent écrit dans une partition donnée), un Prosecution Pool partagé à contextes frais, et une Integrator Lane séquentielle.

Le routing de tier de modèle obéit à trois principes : la rail density (plus la couverture de tests et les checks déterministes sont denses, plus on peut descendre en tier), l'escalation ladder (en cas d'échec, régénérer en montant d'un tier), et le DAG float (l'analyse du chemin critique décide s'il vaut mieux gravir l'échelle ou aller directement au tier supérieur pour ne pas retarder le chemin critique).

Pour le temps mural, Williams identifie quatre signaux qui prédisent les conflits de merge avant même de lancer le travail : le chevauchement de scope de fichiers, le rayon dans le graphe d'imports, le couplage historique de co-changement, et les collisions de namespace. La largeur certifiée par ce forecast se situe typiquement entre trois et cinq agents — au-delà, le risque de collision annule le gain.

Enfin, la précision sans introspection : plutôt que de poser des questions de clarification à un modèle (peu fiable), on fan-out des agents pas chers pour générer plusieurs interprétations de la demande. Là où les N agents convergent, la demande est démontrablement non ambiguë ; là où ils divergent, l'ambiguïté devient mesurée et actionnable. Williams clôt sur des pratiques de terrain : batcher les permissions en pré-vol, distinguer validateurs in-flight et gates de prosecution, préférer des work-stealing queues aux assignations statiques, et respecter un ordre de merge strict — foundation, puis shared packages, puis apps.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Chris Williams | PERSONNE | publie | Three Dials: Parallel Agents Without Merge Hell | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| orchestration multi-agents | METHODOLOGIE | affirme_que | coût, temps mural et précision sont trois cadrans couplés | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | le control flow est du code, le jugement vient des modèles | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| scripts déterministes | METHODOLOGIE | surpasse | modèles frontier pour les décisions d'ordonnancement | TECHNOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| orchestration multi-agents | METHODOLOGIE | utilise | quatre lanes (Contract Desk, Builder Pool, Prosecution Pool, Integrator) | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Builder Pool | CONCEPT | utilise | single-writer par partition | METHODOLOGIE | 0.89 | ATEMPOREL | déclaré_article |
| routing de modèle | METHODOLOGIE | est_basé_sur | rail density, escalation ladder, DAG float | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| merge-forecast | METHODOLOGIE | prédit | conflits de merge avant le lancement du travail | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| merge-forecast | METHODOLOGIE | mesure | largeur certifiée typique de 3 à 5 agents | MESURE | 0.87 | DYNAMIQUE | déclaré_article |
| désambiguïsation par consensus | METHODOLOGIE | surpasse | questions de clarification au modèle | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| désambiguïsation par consensus | METHODOLOGIE | permet | mesurer l'ambiguïté via le désaccord entre N agents | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| phase orchestration | METHODOLOGIE | fait_partie_de | cycle agentique en huit phases | METHODOLOGIE | 0.85 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| trois cadrans | CONCEPT | définition | Coût (modèle), temps mural (largeur de parallélisation), précision (qualité des contrats) — couplés | AJOUT |
| control flow is code | CONCEPT | principe | L'ordonnancement est déterministe ; les modèles ne fournissent que le jugement | AJOUT |
| quatre lanes | CONCEPT | composition | Contract Desk (frontier), Builder Pool (single-writer), Prosecution Pool (frais), Integrator (séquentiel) | AJOUT |
| routing de modèle | METHODOLOGIE | principes | Rail density, escalation ladder, DAG float | AJOUT |
| merge-forecast | METHODOLOGIE | signaux | Scope de fichiers, rayon d'imports, co-changement historique, collisions de namespace | AJOUT |
| merge-forecast | METHODOLOGIE | sortie | Largeur certifiée typiquement 3-5 agents | AJOUT |
| désambiguïsation par consensus | METHODOLOGIE | principe | Là où N agents convergent, la demande est non ambiguë ; le désaccord mesure l'ambiguïté | AJOUT |
| ordre de merge | METHODOLOGIE | séquence | Foundation → shared packages → apps | AJOUT |
