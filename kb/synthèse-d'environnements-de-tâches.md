# synthèse d'environnements de tâches

> **Type** : METHODOLOGIE | 3 relations | 1 fiches sources

## Attributs

- **définition** : Pratique décrite par Z.ai pour lever le goulot du post-entraînement agentique : des agents de recherche convertissent des motifs de travail réel en environnements exécutables long-horizon à dépendances multi-étapes et état caché ; un agent juge tente chaque tâche pour vérifier qu'elle est résoluble ; les vérificateurs sont synthétisés sans accès à la solution de référence ; les trajectoires de solveur servent à découvrir puis fermer les raccourcis de récompense ; un vérificateur n'est retenu qu'après trois contrôles négatifs — oracle, no-op, unsolved-state. Reste dépendante d'un travail humain significatif

## Relations (comme sujet)

### permet

- « de produire des environnements long-horizon exécutables et leur signal de récompense à partir de motifs collectés sur du travail réel, un agent juge vérifiant au préalable que chaque tâche est effectivement résoluble » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-08/zai-glm-53-emergent-cyber-2026-08-14\|GLM-5.3: Frontier Coding with Emergent Cyber Capabilities]]

### recommande

- « de synthétiser les vérificateurs sans accès à la solution de référence et de ne les admettre qu'après trois contrôles négatifs — oracle, no-op et unsolved-state — afin d'obtenir une récompense binaire assez fiable pour entraîner directement dessus » (AFFIRMATION) — 0.94, ATEMPOREL
  - [[fiches/2026-08/zai-glm-53-emergent-cyber-2026-08-14\|GLM-5.3: Frontier Coding with Emergent Cyber Capabilities]]

### réduit

- « les raccourcis de récompense, les trajectoires de solveur servant à les découvrir puis à les fermer » (AFFIRMATION) — 0.90, ATEMPOREL
  - [[fiches/2026-08/zai-glm-53-emergent-cyber-2026-08-14\|GLM-5.3: Frontier Coding with Emergent Cyber Capabilities]]

## Fiches sources

- [[fiches/2026-08/zai-glm-53-emergent-cyber-2026-08-14\|GLM-5.3: Frontier Coding with Emergent Cyber Capabilities]]
