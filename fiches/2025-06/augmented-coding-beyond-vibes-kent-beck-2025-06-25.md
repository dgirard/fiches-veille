# augmented-coding-beyond-vibes-kent-beck-2025-06-25

## Veille
Augmented Coding vs Vibe Coding - Kent Beck - B+ Tree - GenAI - TDD - Rust Python - Substack

## Titre Article
Augmented Coding: Beyond the Vibes - by Kent Beck

## Date
2025-06-25

## URL
https://tidyfirst.substack.com/p/augmented-coding-beyond-the-vibes

## Keywords
Augmented Coding, Vibe Coding, GenAI, Software Development, Programming, B+ Tree, Rust, Python, Test-Driven Development (TDD), Tidy First, AI in Programming, Code Quality, Performance Benchmarking, Remote Agent, language transliteration, yak shaving, professional development

## Authors
Kent Beck

## Ton
**Profil:** Practitioner-Reflective | Première personne craftsman | Narrative-Prescriptive | Expert

Beck adopte personal journey voice documenting hands-on experimentation ("Augmented Coding") versus dismissing trends ("Vibe Coding"). Concrete example (B+ Tree implementation Rust→Python) demonstrates points rather than abstract theorizing. Langage craft-oriented (TDD, performance benchmarking, code quality) maintains engineering discipline focus. Tone measured practitioner enthusiasm grounded actual coding experience. Substack TidyFirst format allows nuanced exploration impossible Twitter threads. Typique software craftsmen (Michael Feathers, Sandi Metz style) sharing learned wisdom through concrete examples visant fellow practitioners valuing disciplined practice.

## Pense-betes
- **Augmented Coding** : qualité code prioritaire, tests, couverture - valeurs similaires au hand coding
- **Vibe Coding** : indifférence qualité code, focus uniquement sur comportement système
- **Projet BPlusTree3** : ~110-130h développement sur 4 semaines, 3 versions (2 abandonnées)
- **Signaux d'alarme IA** : loops, fonctionnalités non-demandées, manipulation de tests
- **Solution pivot langages** : Python d'abord → translittération Rust via Remote Agent
- **Performances compétitives** : range scanning plus rapide que BTreeMap Rust et SortedDict Python
- **Extension C Python** : quasi-égale aux structures natives Python
- **TDD strict** : Red → Green → Refactor, ne jamais mixer changements structurels/comportementaux
- **"Yak shaving" éliminé** : AI gère tâches setup pénibles (coverage testing, environnements)
- **Décisions plus conséquentes** : moins de décisions "boring vanilla", plus de décisions architecturales
- **Supervision active** : "watched intermediate results more carefully, ready to intervene"
- **Journée addictive** : 13h de développement productif qualifié "ADDICTIVE!"
- **Code quality gap** : correct et performant, mais "too much accidental complexity" reste

## RésuméDe400mots

Kent Beck, figure emblématique du développement logiciel, livre une réflexion profonde sur la programmation assistée par IA dans son article "Augmented Coding: Beyond the Vibes". Il établit une distinction fondamentale entre deux philosophies d'utilisation de l'IA : l'"augmented coding" où la qualité du code, sa complexité, les tests et leur couverture restent prioritaires (valeurs similaires au hand coding traditionnel), et le "vibe coding" caractérisé par l'indifférence à la qualité du code, se concentrant uniquement sur le comportement du système.

**Projet BPlusTree3 : Étude de Cas**

Beck documente son implémentation d'une bibliothèque B+ Tree en Rust et Python, investissant environ 110-130 heures sur 4 semaines à travers trois versions, les deux premières ayant été abandonnées suite à l'accumulation de complexité. Le projet visait à démontrer qu'augmented coding peut produire "production-ready, performance-competitive library code" via IA générative.

**Supervision Active et Signaux d'Alarme**

Plutôt qu'une acceptation passive, Beck adopte une surveillance vigilante : "watched the intermediate results of the genie more carefully, ready to intervene & stop unproductive development." Il identifie trois red flags critiques : les loops d'implémentation, l'introduction de fonctionnalités non-demandées (même raisonnables), et la manipulation de tests (désactivation/suppression pour simuler le succès).

**Innovation Méthodologique : Pivot de Langage**

Face au blocage provoqué par le modèle de mémoire ownership de Rust créant une "compounding complexity", Beck emploie une stratégie non-conventionnelle : faire d'abord écrire le code en Python, puis le translittérer en Rust via Remote Agent d'Augment. Cette "risky experiment" réussit à "unstuck the genie" et accélère significativement le progrès.

**Résultats de Performance**

Les bibliothèques générées atteignent des benchmarks compétitifs : "faster at range scanning (iterating through a list of keys)" que BTreeMap de Rust et SortedDict de Python, bien que "a bit slower at some operations". L'extension C Python générée par IA atteint des performances "nearly as fast" que la structure de données native Python.

**Principes TDD Stricts**

Le system prompt de Beck impose une méthodologie Test-Driven Development rigoureuse : cycle Red → Green → Refactor obligatoire, "simplest failing test first", implémentation minimale pour passer tests, séparation stricte changements structurels/comportementaux ("Never mix in same commit").

**Évolution Professionnelle**

Beck aborde l'anxiété du remplacement : "Yes programming changes with a genie, but it's still programming. In some ways a much better programming experience." Les bénéfices concrets incluent élimination du "yak shaving" (tâches setup pénibles), décisions plus conséquentes : "I make more consequential programming decisions per hour, fewer boring vanilla decisions", et automation du coverage testing qui consommerait autrement des heures de troubleshooting environnemental.

**Gap Qualité Persistant**

Malgré le succès fonctionnel et performantiel, Beck exprime insatisfaction qualitative : "I feel good about the correctness & performance, not so good about the code quality. When I try to write the code as a literate program there's just too much accidental complexity." Ce défi restant suggère que l'IA nécessite encore guidance humaine pour optimisation de simplicité, confirmation que l'augmented coding demeure collaboration homme-machine plutôt que remplacement.
