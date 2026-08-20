# log de session append-only

> **Type** : CONCEPT | 4 relations | 1 fiches sources

## Attributs

- **définition** : Journal en ajout seul qui est la source du contexte vu par le modèle dans DeepSeek Harness — et non son compte rendu : l'historique modèle en est projeté par `deriveMessages()`, et fork, reprise, transcripts, télémétrie et persistance en dérivent tous. Invariant associé, asserté à l'exécution : tout ce qui atteint une requête modèle doit être reconstructible depuis le journal, de sorte qu'un nouvel input visible du modèle exige un nouvel événement de session. Un tour rejeté sans aucun step est lui-même journalisé, pour que la tentative reste visible. Format non stabilisé en préversion

## Relations (comme sujet)

### affirme_que

- « tout ce qui atteint une requête modèle doit être reconstructible depuis le journal, un invariant runtime l'assurant — « Model-visible means logged » » (CITATION) — 0.94, ATEMPOREL
  - [[fiches/2026-08/deepseek-harness-everything-is-a-plugin-2026-08-13\|DeepSeek Harness developer preview: Everything is a plugin]]

### permet

- « d'enregistrer tout ce que le modèle voit — prompts système, raisonnement, appels d'outils et résultats, ordonnancement des subagents et chaque injection de contexte — la reprise, le fork, la recherche et le replay opérant tous sur le même flux d'événements » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-08/deepseek-harness-everything-is-a-plugin-2026-08-13\|DeepSeek Harness developer preview: Everything is a plugin]]

### s_oppose_à

- « l'archivage durable tant que SESSION_FORMAT_VERSION reste à 0 sans promesse de compatibilité et que les backends rejettent les anciens formats sur disque » (AFFIRMATION) — 0.90, DYNAMIQUE
  - [[fiches/2026-08/deepseek-harness-everything-is-a-plugin-2026-08-13\|DeepSeek Harness developer preview: Everything is a plugin]]

## Relations (comme objet)

- [[kb/DeepSeek-Harness\|DeepSeek Harness]] **utilise** → log de session append-only — 0.97

## Fiches sources

- [[fiches/2026-08/deepseek-harness-everything-is-a-plugin-2026-08-13\|DeepSeek Harness developer preview: Everything is a plugin]]
