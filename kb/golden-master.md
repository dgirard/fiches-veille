# golden master

> **Type** : METHODOLOGIE | 11 relations | 5 fiches sources

## Attributs

- **livrable** : golden_master.json par module, comparaison des écritures, états, exports
- **rôle** : Sorties de l'application d'origine servant d'oracle aux tests de la réécriture
- **usage** : Règle vue → cas de test ; règle inférée → confirmation métier
- **variante** : Inversé : le LLM propose les entrées, l'exécutable d'origine fournit les sorties

## Relations (comme sujet)

### affirme_que

- « le LLM génère les entrées, le code legacy seul génère les sorties » (CITATION) — 0.90, ATEMPOREL
  - [[fiches/2026-10/sfeir-migration-windev-software-factory-10x-2026-10-15\|Migrer WinDev avec la Software Factory 10x : la méthode SFEIR en six étapes, de l'audit à la bascule]]

### permet

- prouver l'équivalence fonctionnelle à partir de l'exécutable d'origine (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]
- transformer une sortie REA en tests de non-régression (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2026-10/sfeir-rea-evidence-sortie-agent-2026-10-15\|Lire une sortie REA : preuves, pseudocode et hallucinations]]

### s_applique_à

- réécriture par briques d'une application legacy (CONCEPT) — 0.86, ATEMPOREL
  - [[fiches/2026-10/sfeir-editeur-disparu-code-perdu-2026-10-19\|Éditeur disparu, code source perdu : plan de sauvetage d'une application critique]]
- [[kb/_entites-mineures#PowerBuilder\|PowerBuilder]] (TECHNOLOGIE) — 0.80, ATEMPOREL
  - [[fiches/2026-10/sfeir-retro-ingenierie-powerbuilder-nsdk-2026-10-20\|PowerBuilder et NSDK : état des lieux de la rétro-ingénierie par agents]]

## Relations (comme objet)

- [[kb/méthode-de-migration-WinDev-en-six-étapes\|méthode de migration WinDev en six étapes]] **utilise** → golden master — 0.92
- [[kb/plan-de-sauvetage-en-quatre-temps\|plan de sauvetage en quatre temps]] **utilise** → golden master — 0.92
- [[kb/golden-master-inversé\|golden master inversé]] **est_variante_de** → golden master — 0.90
- [[kb/rétro-documentation\|rétro-documentation]] **utilise** → golden master — 0.88
- [[kb/_entites-mineures#phase-transitoire-WinDev-sur-PostgreSQL\|phase transitoire WinDev sur PostgreSQL]] **permet** → golden master — 0.82
- [[kb/Software-Factory\|Software Factory]] **utilise** → golden master — 0.80

## Fiches sources

- [[fiches/2026-10/sfeir-editeur-disparu-code-perdu-2026-10-19\|Éditeur disparu, code source perdu : plan de sauvetage d'une application critique]]
- [[fiches/2026-10/sfeir-legacy-sans-code-source-2026-10-16\|Applications legacy sans code source : comprendre avant de réécrire]]
- [[fiches/2026-10/sfeir-migration-windev-software-factory-10x-2026-10-15\|Migrer WinDev avec la Software Factory 10x : la méthode SFEIR en six étapes, de l'audit à la bascule]]
- [[fiches/2026-10/sfeir-rea-evidence-sortie-agent-2026-10-15\|Lire une sortie REA : preuves, pseudocode et hallucinations]]
- [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]
