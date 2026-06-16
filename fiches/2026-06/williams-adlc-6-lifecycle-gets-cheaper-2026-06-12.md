# williams-adlc-6-lifecycle-gets-cheaper-2026-06-12

## Veille

Sixième volet ADLC : Williams décrit la phase P7 « Distill » comme le composant qui fait baisser le coût à chaque run. Deux moitiés : la simplification post-merge (déduire après que le code existe, pas avant — « deduplicating before the code exists is speculative ») et le minage des leçons (un « lesson foundry » transforme les findings récurrents en règles de lint, skills et nouvelles questions d'interrogation). Chaque leçon est payée une fois puis rétrogradée de la détection probabiliste coûteuse vers la prévention déterministe gratuite. La bonne unité de compte est le « cost per merged, verified change », et « flat cost is failure ».

## Titre Article

The Lifecycle That Gets Cheaper Every Run

## Date

2026-06-12

## URL

https://www.voodootikigod.com/adlc-6-lifecycle-gets-cheaper

## Keywords

ADLC, phase Distill, P7, coût décroissant, simplification post-merge, déduplication observable, lesson foundry, minage de leçons, règle de lint, skill rot, model ratchet, ratcheting, cost per merged change, unité de compte, flat cost is failure, capitalisation, prévention déterministe, compounding

## Authors

Chris Williams (@voodootikigod)

## Ton

Profil : essai économico-technique (perspective praticien en anglais, registre analytique et prescriptif), niveau technique élevé, public cible leads et responsables de programme pilotant le coût d'usage des agents. Le ton est celui de la capitalisation systématique : Williams traite la connaissance produite par le cycle comme un actif à banker, et le coût comme une trajectoire à mesurer dans le temps plutôt qu'un instantané. L'autorité repose sur une thèse contre-intuitive et nette — « flat cost is failure » — et sur le choix d'une unité de compte correcte (cost per merged, verified change) qui requalifie la dépense de prosecution en investissement. Style à charpente diagnostique : deux moitiés de Distill, quatre indicateurs de boucle cassée, métaphores de fonderie (lesson foundry) et de cliquet (model ratchet) pour dire l'irréversibilité du gain capitalisé.

## Pense-betes

- **Thèse** : sans mécanisme intentionnel de capture des leçons, les agents n'offrent **aucun** avantage cumulatif — ils repartent de zéro à chaque cycle. La phase P7 Distill est le composant manquant qui fait baisser le coût run après run.
- **Distill, moitié 1 — Simplification** : la revue architecturale doit avoir lieu **après** le merge, pas avant. « Deduplicating before the code exists is speculative » ; la déduplication post-merge cible des patterns observables. Les tests garantissent la préservation du comportement pendant le nettoyage, ce qui permet à des modèles moins capables d'y participer sans risque.
- **Distill, moitié 2 — Minage (lesson foundry)** : transforme les findings récurrents en défenses permanentes — les problèmes déterministes deviennent des règles de lint avec tests ; les patterns contextuels alimentent un pipeline de skill-mining ; les lacunes de spec déclenchent de nouvelles questions d'interrogation (P1).
- **Économie de la leçon** : chaque leçon est payée **une seule fois**, puis rétrogradée d'une détection probabiliste coûteuse vers une prévention déterministe gratuite.
- **Skill rot** : des artefacts périmés délivrent une désinformation avec autorité. Parade : vérifications hebdomadaires qui extraient les claims vérifiables (commandes, chemins, versions) et marquent leur fraîcheur.
- **Model ratchet** : ré-auditer le code existant avec des modèles frontier après une release, pour capter ce que les versions antérieures avaient manqué — un cliquet qui ne recule pas.
- **Bonne unité de compte** : pas le « tokens-per-developer » mais le **« cost per merged, verified change »**. Ce cadrage requalifie la dépense : les coûts de la phase prosecution sont des investissements, pas du gaspillage.
- **Quatre indicateurs de boucle cassée** : concentration de la dépense en phase Build → skills manquantes ; dépense de prosecution en hausse → leçons non rapatriées ; atteinte du max d'itérations → specs faibles ; trajectoire de coût plate → échec du système.
- **Thèse-choc** : « flat cost is failure ». Un système qui marche montre un coût par changement mesurablement **décroissant** à mesure que les skills s'accumulent et que les couches de lint s'épaississent.

## RésuméDe400mots

Le sixième volet répond à la question qui décide de la viabilité économique des agents : pourquoi un cycle agentique devrait-il coûter moins cher à chaque exécution ? La réponse de Williams est qu'il ne le fait pas spontanément. Sans un mécanisme délibéré de capture et d'institutionnalisation des leçons, les agents n'offrent aucun avantage cumulatif : ils repartent d'une connaissance nulle à chaque cycle. Le composant qui change cela est la phase P7, Distill.

Distill comporte deux moitiés. La première est la simplification. Contre l'intuition, la revue architecturale et la déduplication doivent intervenir après le merge, pas avant. Dédupliquer avant que le code existe est spéculatif ; dédupliquer après cible des patterns réellement observables. Les tests, déjà en place, garantissent la préservation du comportement pendant ce nettoyage, ce qui autorise des modèles moins capables — donc moins chers — à y participer sans risque.

La seconde moitié est le minage des leçons, organisé en « lesson foundry ». Cette fonderie transforme les findings récurrents en défenses permanentes : les problèmes déterministes deviennent des règles de lint accompagnées de tests ; les patterns contextuels alimentent un pipeline de skill-mining ; les lacunes de spécification déclenchent de nouvelles questions dans la phase d'interrogation. L'économie sous-jacente est décisive : chaque leçon est payée une seule fois, puis rétrogradée d'une détection probabiliste coûteuse vers une prévention déterministe gratuite.

Williams identifie deux ennemis du gain capitalisé. Le skill rot d'abord : des artefacts périmés délivrent une désinformation avec autorité ; la parade est une vérification hebdomadaire qui extrait les claims vérifiables (commandes, chemins, versions) et marque leur fraîcheur. Le model ratchet ensuite : après chaque release, ré-auditer le code existant avec des modèles frontier pour capter ce que les versions antérieures avaient manqué — un cliquet qui n'autorise pas le recul.

Le volet culmine sur la bonne unité de compte. Plutôt que de suivre les tokens par développeur, les programmes qui réussissent mesurent le coût par changement mergé et vérifié. Ce recadrage transforme la lecture de la dépense : les coûts de la phase prosecution ne sont pas du gaspillage mais un investissement. Quatre indicateurs révèlent une boucle cassée : une dépense concentrée en phase Build signale des skills manquantes ; une prosecution de plus en plus chère signale des leçons non rapatriées ; les atteintes répétées du plafond d'itérations signalent des specs faibles ; et une trajectoire de coût plate signale l'échec du système. La thèse tient en quatre mots : « flat cost is failure ». Un système sain voit son coût par changement décroître mesurablement à mesure que les skills s'accumulent et que les couches de lint s'épaississent.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Chris Williams | PERSONNE | publie | The Lifecycle That Gets Cheaper Every Run | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| phase Distill | METHODOLOGIE | réduit | coût par changement run après run | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| phase Distill | METHODOLOGIE | fait_partie_de | cycle agentique en huit phases | METHODOLOGIE | 0.90 | ATEMPOREL | déclaré_article |
| simplification post-merge | METHODOLOGIE | surpasse | déduplication avant écriture du code | METHODOLOGIE | 0.89 | ATEMPOREL | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | dédupliquer avant que le code existe est spéculatif | CITATION | 0.91 | ATEMPOREL | déclaré_article |
| lesson foundry | METHODOLOGIE | permet | conversion des findings récurrents en règles de lint, skills et questions | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| règle de lint | METHODOLOGIE | remplace | détection probabiliste coûteuse par prévention déterministe | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| skill rot | CONCEPT | réduit | fiabilité des artefacts de connaissance | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| model ratchet | METHODOLOGIE | permet | ré-audit du code par modèles frontier après release | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| cost per merged change | CONCEPT | surpasse | tokens-per-developer comme unité de compte | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| Chris Williams | PERSONNE | affirme_que | un coût plat est un échec (« flat cost is failure ») | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| dépense de prosecution | CONCEPT | est_instance_de | investissement plutôt que gaspillage | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| phase Distill | METHODOLOGIE | composition | Simplification post-merge + minage des leçons (lesson foundry) | AJOUT |
| simplification post-merge | METHODOLOGIE | principe | Dédupliquer après que le code existe, sur des patterns observables, tests garantissant le comportement | AJOUT |
| lesson foundry | METHODOLOGIE | sorties | Règles de lint (déterministe), skills (contextuel), nouvelles questions d'interrogation (specs) | AJOUT |
| économie de la leçon | CONCEPT | principe | Payée une fois, puis rétrogradée de détection probabiliste à prévention déterministe gratuite | AJOUT |
| skill rot | CONCEPT | parade | Vérifications hebdomadaires extrayant claims vérifiables et marquant la fraîcheur | AJOUT |
| model ratchet | METHODOLOGIE | nature | Ré-audit post-release par modèles frontier ; cliquet qui ne recule pas | AJOUT |
| cost per merged change | CONCEPT | définition | Coût par changement mergé et vérifié — unité de compte correcte | AJOUT |
| indicateurs de boucle cassée | CONCEPT | liste | Concentration en Build, prosecution en hausse, max d'itérations atteint, coût plat | AJOUT |
