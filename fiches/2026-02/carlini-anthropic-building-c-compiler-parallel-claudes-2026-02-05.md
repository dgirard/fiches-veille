# carlini-anthropic-building-c-compiler-parallel-claudes-2026-02-05
## Veille
Compilateur C en Rust construit par 16 agents Claude parallèles autonomes - Anthropic

## Titre Article
Building a C Compiler with a Team of Parallel Claudes

## Date
2026-02-05

## URL
https://www.anthropic.com/engineering/building-c-compiler

## Keywords
Compilateur C, Rust, agents parallèles, Claude Opus 4.6, autonomie agents IA, Claude Code, coding agentique, Linux 6.9, x86, ARM, RISC-V, 100 000 lignes, 20 000 dollars, Docker, synchronisation agents, tests automatisés, GCC, spécialisation agents, sécurité agents autonomes

## Authors
Nicholas Carlini (chercheur équipe Safeguards, Anthropic)

## Ton
**Profil** : Billet technique d'ingénierie, registre narratif-analytique, niveau technique très avancé

**Description** : Article de blog d'ingénierie Anthropic combinant récit d'expérimentation et leçons techniques. Le ton est celui d'un chercheur en sécurité qui partage avec enthousiasme et honnêteté un projet personnel poussant les limites du modèle. L'écriture alterne entre descriptions techniques précises (scripts bash, architecture Docker, algorithmes de synchronisation) et réflexions plus larges sur les implications. L'auteur reconnaît ouvertement les limitations et les risques de sécurité, apportant une perspective nuancée grâce à son background en tests de pénétration. Le public cible est constitué d'ingénieurs et chercheurs en IA s'intéressant aux systèmes multi-agents autonomes.

## Pense-betes
- **Résultat principal** : compilateur C en Rust de 100 000 lignes, construit par 16 agents Claude Opus 4.6 en parallèle, ~2 000 sessions Claude Code, coût ~20 000 $
- **Le compilateur compile Linux 6.9** sur x86, ARM et RISC-V, ainsi que QEMU, FFmpeg, SQLite, PostgreSQL, Redis et Doom
- **Architecture agents parallèles** :
  - Boucle bash simple relançant Claude en mode `--dangerously-skip-permissions`
  - Conteneurs Docker isolés, repos montés sur `/upstream`
  - Synchronisation par fichiers verrou dans `current_tasks/` + Git
  - Pas de communication inter-agents ni d'orchestration explicite — sélection autonome des tâches
- **Spécialisation par rôle** : déduplication de code, optimisation performance, efficacité du code généré, critique design Rust, documentation
- **Leçons clés pour les agents autonomes** :
  1. **Tests de très haute qualité** : les agents résolvent exactement ce qu'on leur spécifie, la précision des tests est donc critique
  2. **Se mettre à la place de Claude** : chaque agent entre dans un conteneur vierge → README exhaustifs nécessaires ; sortie tests minimale ; flag `--fast` pour échantillonnage aléatoire (1-10%)
  3. **Faciliter le parallélisme** : facile quand beaucoup de tests indépendants échouent, difficile pour tâche monolithique (ex: compilation Linux kernel). Solution : GCC comme "oracle de référence" + compilation aléatoire partielle
  4. **Rôles multiples** : spécialisation possible une fois le parallélisme en place
- **Progression des modèles** : Opus 4 = compilateur à peine fonctionnel, Opus 4.5 = premier compilateur passant des suites de tests, Opus 4.6 = compile Linux
- **Consommation** : 2 milliards tokens en entrée, 140 millions en sortie, ~20 000 $ — fraction du coût de développement humain
- **Limitations honnêtes** : pas de x86 16 bits (appelle GCC), assembleur/linker incomplets, compatibilité non universelle, code généré moins performant que GCC -O0, qualité du code Rust correcte mais non experte
- **Sécurité** : l'auteur (background pentest) souligne que passer les tests ne garantit pas la correction ; le déploiement de logiciel autonome non vérifié est un risque réel
- **Citation mémorable** : "Building this compiler has been some of the most fun I've had recently, but I did not expect this to be anywhere near possible so early in 2026."
- **Code source** : disponible sur GitHub (anthropics/claudes-c-compiler)

## RésuméDe400mots
Nicholas Carlini, chercheur de l'équipe Safeguards d'Anthropic, a dirigé une expérience ambitieuse : faire construire un compilateur C en Rust entièrement par des agents Claude Opus 4.6 travaillant en parallèle, sans intervention humaine directe sur le code.

**Architecture multi-agents** : 16 instances Claude ont travaillé simultanément dans des conteneurs Docker isolés, partageant un dépôt Git en amont. Chaque agent sélectionne autonomement sa prochaine tâche via un système de verrous fichiers. La synchronisation repose sur Git : un agent réclame une tâche, travaille dessus, push ses modifications, puis passe à la suivante. Aucune communication explicite entre agents n'est nécessaire.

**Résultats impressionnants** : en environ 2 000 sessions Claude Code et 20 000 dollars de coût API (2 milliards de tokens en entrée, 140 millions en sortie), le compilateur résultant de 100 000 lignes compile avec succès Linux 6.9 sur trois architectures (x86, ARM, RISC-V), ainsi que des projets majeurs comme QEMU, FFmpeg, SQLite, PostgreSQL, Redis et même Doom, avec 99% de réussite sur les suites de tests compilateur dont la suite de torture GCC.

**Leçons de conception** : L'auteur partage quatre enseignements clés. Premièrement, la qualité des tests est critique car les agents résolvent exactement ce qui est spécifié. Deuxièmement, il faut se mettre à la place de Claude : chaque agent entre dans un environnement vierge sans contexte, nécessitant une documentation exhaustive et une sortie minimale pour préserver la fenêtre de contexte. Troisièmement, faciliter le parallélisme est essentiel : facile quand de nombreux tests indépendants échouent, mais la compilation du noyau Linux a posé problème car tous les agents corrigeaient les mêmes bugs. La solution : utiliser GCC comme "oracle de référence" pour répartir aléatoirement les fichiers à compiler. Quatrièmement, la spécialisation des agents par rôle (déduplication, optimisation, design review, documentation) maximise l'efficacité.

**Progression des modèles** : L'article sert aussi de benchmark des capacités. Opus 4 produisait à peine un compilateur fonctionnel, Opus 4.5 a permis le premier compilateur passant des suites de tests, et Opus 4.6 repousse les limites en compilant de vrais projets à grande échelle.

**Enjeux de sécurité** : L'auteur, fort de son background en tests de pénétration, rappelle que passer les tests ne garantit pas la correction du logiciel. Le déploiement autonome de code non vérifié par des humains représente un risque réel nécessitant de nouvelles stratégies de sécurité. Le code source est disponible sur GitHub (anthropics/claudes-c-compiler).
