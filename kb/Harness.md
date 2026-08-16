# Harness

> **Type** : CONCEPT | 5 relations | 3 fiches sources

## Attributs

- **catégorie** : Couche abstraction agent (outils, prompts, mémoire, sécurité)
- **rôle** : Couche que DeepSeek résume par l'équation « Agent = Model + Harness » : le modèle est *« l'âme de l'agent »*, le harnais est ce qui lui permet de comprendre son environnement, d'utiliser des outils et de continuer à travailler en conditions réelles. DSH en propose une définition opérationnelle par composition de plugins et journal unique, plutôt que par catalogue de fonctionnalités
- **équation** : Agent = Modèle + Harness ; modèle ~10 %, harness ~90 %

## Relations (comme sujet)

### permet

- transformer un modèle brut en agent capable de finir une tâche (CONCEPT) — 0.93, ATEMPOREL
  - [[fiches/2026-05/osmani-google-new-sdlc-vibe-coding-agentic-engineering-2026-05\|The New SDLC With Vibe Coding — From ad-hoc prompting to Agentic Engineering]]

### réduit

- dépendance aux cycles d'évolution des modèles (CONCEPT) — 0.90, ATEMPOREL
  - [[fiches/2025-11/chen-fioca-openai-future-proof-coding-agents-2025-11-23\|Future-Proof Coding Agents: Building Reliable Systems That Outlast Model Cycles]]

### résout

- complexité intégration modèles (CONCEPT) — 0.90, ATEMPOREL
  - [[fiches/2025-11/chen-fioca-openai-future-proof-coding-agents-2025-11-23\|Future-Proof Coding Agents: Building Reliable Systems That Outlast Model Cycles]]

## Relations (comme objet)

- [[kb/DeepSeek-Harness\|DeepSeek Harness]] **est_instance_de** → Harness — 0.97
- [[kb/Codex\|Codex]] **utilise** → Harness — 0.92

## Fiches sources

- [[fiches/2025-11/chen-fioca-openai-future-proof-coding-agents-2025-11-23\|Future-Proof Coding Agents: Building Reliable Systems That Outlast Model Cycles]]
- [[fiches/2026-08/deepseek-harness-everything-is-a-plugin-2026-08-13\|DeepSeek Harness developer preview: Everything is a plugin]]
- [[fiches/2026-05/osmani-google-new-sdlc-vibe-coding-agentic-engineering-2026-05\|The New SDLC With Vibe Coding — From ad-hoc prompting to Agentic Engineering]]
