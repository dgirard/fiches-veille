---
themes: [agents-codage-ia-skills, outils-plateformes, qualite-securite]
source: Bun (Jarred Sumner)
---
# sumner-bun-rewrite-rust-claude-2026-07-08

## Veille

Récit technique de premier ordre par **Jarred Sumner**, créateur de **Bun** (runtime JS/TS, >22 M téléchargements/mois), sur la **réécriture complète de Bun de Zig vers Rust en 11 jours** (3→14 mai 2026) pilotée par **Claude** — une étude de cas exceptionnelle de génie logiciel assisté par IA **à l'échelle industrielle**. Motivation : une classe récurrente de bugs (use-after-free, double-free, fuites) née du mélange mémoire gérée par GC (JavaScriptCore) / mémoire manuelle (Zig) ; en **safe Rust**, ces bugs deviennent des **erreurs de compilation** avec nettoyage automatique (`Drop`/RAII) — « une meilleure boucle de feedback qu'un guide de style ». Refusant le dogme « une réécriture est toujours une mauvaise idée » (un an de gel des correctifs pour 3 ingénieurs), Sumner choisit un **portage mécanique** (préserver l'architecture, changement de comportement minimal) validé par la **suite de tests existante, écrite en TypeScript donc indépendante du langage** (60 624 tests, 1,39 M assertions `expect()`, 0 test supprimé, 6 plateformes). Le harnais : **~50 dynamic workflows** dans **Claude Code**, boucles *écrire → 2+ relecteurs adversariaux → appliquer*, jusqu'à **64 Claude en parallèle** (4 worktrees × 16), avec **PORTING.md** + **LIFETIMES.tsv** générés en préparation. Chiffres : **6 502 commits** (pic 695/h, 58/min, ~1 300 lignes/min), diff final **+1 009 272 lignes**, ~16 000 erreurs de compilation traitées comme file d'attente, **5,9 Md tokens d'entrée non cachés + 690 M en sortie ≈ 165 000 $**. Clés méthodologiques : la **revue adversariale** (un second Claude, contexte séparé, ne voit que le diff, sommé de trouver pourquoi c'est faux — capte des bugs subtils *sémantiquement* différents mais *syntaxiquement* identiques) et le principe **« corriger le processus qui génère le code, pas le code à la main »**. Modèle utilisé : pré-version de **Claude Fable 5** (classe Mythos). Depuis le merge : **11 rounds de revue de sécurité Claude Code**, fuzzing coverage-guided 24/7 (100 Md exécutions → ~15 PRs), **4 % de code `unsafe`** (78 % sur une seule ligne), **19 régressions** connues corrigées. En production : Claude Code v2.1.181, premier release sur le Bun-en-Rust, **+10 % de vitesse de démarrage sur Linux**. Disclosure assumée : **Bun a été racheté par Anthropic en décembre 2025**.

## Titre Article

Rewriting Bun in Rust

## Date

2026-07-08

## URL

https://bun.com/blog/bun-in-rust

## Keywords

Bun, Jarred Sumner, réécriture Zig vers Rust, portage mécanique, runtime JavaScript TypeScript, esbuild, Anthropic acquisition, Claude Fable 5, classe Mythos, Claude Code, dynamic workflows, harness engineering, 64 Claude en parallèle, git worktrees, revue adversariale, adversarial review, split context windows, 1 implémenteur 2 relecteurs 1 fixer, boucle écrire-relire-appliquer, corriger le processus pas le code, PORTING.md, LIFETIMES.tsv, safe Rust, Drop, RAII, use-after-free, double-free, memory leak, garbage collector, JavaScriptCore, gestion manuelle de la mémoire, defer errdefer, guide de style, TigerStyle, smart pointers, ~100 crates, dépendances cycliques, 16000 erreurs de compilation, file d'attente d'erreurs, smoke tests, systemd-run cgroups, isolation, suite de tests TypeScript indépendante du langage, 60624 tests, 1,39M assertions expect, 0 test supprimé, 6 plateformes, Buildkite CI, 6502 commits, 1009272 lignes, 5,9 milliards tokens entrée, 690M tokens sortie, 165000 dollars, 11 jours, ReleaseSafe, Address Sanitizer, ASAN, Fuzzilli, coverage-guided fuzzing, 100 milliards exécutions, 11 rounds revue sécurité, code unsafe 4%, 19 régressions, debug_assert macro, sémantiquement différent syntaxiquement identique, Claude Code v2.1.181, 10% démarrage plus rapide, cross-language LTO, binaire 20% plus petit, one engineer can do a lot more, graveyard of dead side projects

## Authors

Jarred Sumner (créateur de Bun ; travaille chez Anthropic depuis le rachat de Bun en décembre 2025)

## Ton

**Profil** : billet d'ingénierie technique en première personne (blog officiel Bun), long-form (~5000 mots), destiné aux ingénieurs systèmes/runtime et à la communauté du génie logiciel assisté par IA. **Disclosure d'entrée** (« Bun a été racheté par Anthropic en décembre 2025 ; j'ai utilisé une pré-version de Claude Fable 5 »), qui désamorce le conflit d'intérêts sans le masquer. Technicité très élevée (lifetimes, `Drop` vs `defer`, dépendances cycliques de crates, timespec négatif, `unwrap_or` eager vs `unwrap_or_else` lazy) mais pédagogique : chaque décision est motivée par un raisonnement « comment un humain ferait-il ça ? ».

**Style** : honnêteté méthodologique revendiquée — l'auteur raconte autant ses **false starts** (Claude qui fait `git stash`/`reset` et s'écrase entre instances ; Claude qui « stub » les fonctions plutôt que les corriger ; timeouts en debug ; disque saturé faute d'IOPS) que ses réussites. Refus explicite du prompt magique (« Rewrite Bun in Rust. Don't make any mistakes. » n'est *pas* ce qu'il a fait). Reconnaissance sincère de l'outil qu'il quitte (« Zig made Bun possible… I'll always be grateful »). Verbatims marquants : *« The default outcome for ambitiously-scoped projects like Bun is joining the graveyard of dead side projects »*, *« One engineer can do a lot more today than a year ago »*, *« If you need a paragraph-long comment to justify why the workaround is OK, the code is wrong — fix the code »*, *« This is the bleeding edge of what's possible today »*. Riche en visualisations de données (commits par heure, la course au vert par plateforme, replay des 11 jours). Sourçage par numéros de commit réels (attribution de revue dans le sujet du commit).

## Pense-betes

- **Idée-force : la réécriture de langage n'est plus une décision à sens unique.** Historiquement, changer le langage d'un projet comme Bun (535 496 lignes de Zig) = ~1 an pour une petite équipe, avec **gel des correctifs, de la sécurité et des features** — donc irréaliste, donc « on ne le fait jamais ». L'IA agentique transforme cet arbitrage : *« What if I spend a week testing if Anthropic's new model can rewrite Bun in Rust? »* Résultat : **11 jours**.
- **Le « pourquoi Rust » est un argument de boucle de feedback, pas de goût.** La classe de bugs dominante (use-after-free, double-free, oublis de `free` sur chemins d'erreur) vient du mélange **mémoire GC (JavaScriptCore) × mémoire manuelle (Zig)** — un cas que peu de langages conçoivent. En **safe Rust**, ce sont des **erreurs de compilation** + nettoyage automatique (`Drop`, RAII). « Compiler errors are a better feedback loop than a style guide. » Zig préfère le `defer` explicite (pas de control-flow caché) ; l'alternative — smart pointers maison — offrait « une pire ergonomie que Rust, sans les garanties ».
- **La contrainte qui rend le pari jouable : une suite de tests indépendante du langage.** Les tests de Bun sont **écrits en TypeScript** → ils ne dépendent pas du langage d'implémentation. Le portage vise le **changement de comportement minimal**, validé par cette suite (60 624 tests, 1,39 M `expect()`, **0 test supprimé ou skippé**, vérifié à la main). C'est le filet qui autorise à merger 1 M de lignes générées par LLM.
- **Portage mécanique > redesign.** Choix explicite : préserver l'architecture Zig, minimiser les changements, laisser la Rust **idiomatique** pour *après* le ship de v1.4. « Incremental vs all-at-once ? » → tout d'un coup (comme son portage esbuild Go→Zig d'origine, sans LLM). Le reste « n'est que de la tactique ».
- **Le harnais : ~50 dynamic workflows dans Claude Code, en boucle 11 jours.** Pseudocode assumé : `while (task = todo.pop()) { result = task(); feedback = await [review(result), review(result)]; apply(feedback) }`. Workflows dédiés : générer le guide de portage → porter mécaniquement chaque `.zig` en `.rs` → corriger les erreurs de compilation par crate → faire passer les sous-commandes (`bun test`, `bun build`) → faire passer toute la suite → refactors/cleanup.
- **La revue adversariale, cœur de la fiabilité.** Un **second Claude, dans un contexte séparé, qui ne voit QUE le diff** (aucun raisonnement de l'implémenteur), sommé de « trouver pourquoi c'est faux ». Ratio **1 implémenteur / 2+ relecteurs adversariaux / 1 fixer** ; l'implémenteur ne relit pas, le relecteur n'implémente pas (comme chez les humains, celui qui écrit est biaisé vers le merge). Capte des bugs **syntaxiquement identiques mais sémantiquement différents** : `Box` droppé avant un `uv_close` asynchrone (UAF + double-free) ; timespec négatif via `trunc` vs `floor` ; `unwrap_or` **eager** qui panique là où `unwrap_or_else` **lazy** ne l'aurait pas fait.
- **« Corriger le processus qui génère le code, pas le code à la main. »** Principe directeur : quand un bug ou un anti-pattern apparaît, on **édite le workflow/prompt**, pas le fichier. Ex. : quand Claude ajoute de longs commentaires pour justifier des workarounds, règle ajoutée pour les relecteurs → *« If you need a paragraph-long comment to justify why the workaround is OK, the code is wrong — fix the code. »* Un edit de prompt, quelques heures, le comportement disparaît.
- **Préparation (de-risking) avant d'écrire une ligne.** ~3 h de discussion avec Claude → **PORTING.md** (mapping patterns/types Zig→Rust). Puis un workflow analysant **le lifetime de chaque champ de struct** (lecture + trace du control-flow, 2 relecteurs adversariaux) sérialisé en **LIFETIMES.tsv** pour les autres Claude. Puis **essai sur 3 fichiers** avant de lancer les 1 448.
- **Le parallélisme et ses false starts.** Lancer 1 448 fichiers d'un coup → les Claude s'écrasent (`git stash`/`stash pop`/`reset --hard`). Fix : **interdire tout git qui ne committe pas un fichier précis**, aucun `cargo`, aucune commande lente. Puis **4 shards / 4 worktrees × 16 Claude** = **~64 Claude** simultanés. Pic : **1 300 lignes/min**, **695 commits/h**, 58 commits/min. Un `grep` lent a gelé le disque faute d'IOPS relevés sur l'instance EC2.
- **~16 000 erreurs de compilation comme file d'attente.** Découpage en **~100 crates** (compilation plus rapide) → révèle des **dépendances cycliques** (le codebase Zig était une seule unité de compilation) → workflows de classification puis de refactor. `cargo check` écrit les erreurs dans un fichier groupé par crate → réparties sur 64 Claude. Isolation renforcée via **systemd-run (cgroups)** pour les tests de fuite mémoire / stress (10k process, Go de disque, sockets TCP saturés).
- **La route vers le vert (CI Buildkite, 6 plateformes).** De 972 fichiers de test en échec à 23 en 2 jours ; Linux full green ~1 jour avant Windows ; build #54202 = **6/6 plateformes vertes** → merge. Merger ≠ release : confiance suffisante pour s'engager, pas encore pour publier.
- **Le coût, chiffré et assumé.** Pré-merge : **5,9 Md tokens d'entrée non cachés + 690 M en sortie + 72 Md de lectures de cache ≈ 165 000 $** au prix API. Alternative humaine réaliste : **3 ingénieurs, ~1 an**, pendant lequel « on n'aurait pas amélioré la compat Node.js, corrigé de bugs/failles ni livré de features » — donc **jamais fait**. « The realistic alternative was to do nothing and keep fixing the bugs forever. »
- **Après le merge, le travail continue.** **11 rounds** de revue de sécurité **Claude Code Security** ; **fuzzing coverage-guided 24/7** de tous les parsers (JS/TS/JSX/CSS/JSON5/TOML/YAML/Markdown/INI/Bun Shell/semver/.patch), **100 Md exécutions → ~15 PRs** (le fuzzer envoie le repro à Claude qui soumet la PR, revue humaine). **~4 % de code `unsafe`** (~13 000 `unsafe` / ~780 000 lignes), dont **78 % sur une seule ligne** (pointeur venu du C++ ou appel C) — appelé à baisser vers du Rust idiomatique. **19 régressions** connues, toutes corrigées (ex. `debug_assert!` macro effacée en release → HMR cassé).
- **Le modèle et la production.** Pré-version de **Claude Fable 5** (« a Mythos-class model ») ; les dynamic workflows de Claude Code ont tenu **64 Claude pendant 11 jours** (« sinon j'aurais dû écrire mon propre harnais »). Premier release sur le Bun-en-Rust : **Claude Code v2.1.181**, **+10 % de démarrage sur Linux**, changements user-facing minimes → preuve de maturité prod.
- **À relier** : revue de code par agents / vérification adversariale et consensus (Monperrus « The End of Code Review », série ADLC de Kent Beck-style « prosecution not code review » / « tests are the spec ») ; **Loop/Harness Engineering** (Lushbinary, Osmani, OpenAI Codex agent-first, technique Ralph, git worktrees) ; skills & dynamic workflows Claude Code ; Zig déjà au corpus (ZML/LLMD, souveraineté du silicium) ; FinOps des tokens / coût par résultat.

## RésuméDe400mots

Jarred Sumner, créateur de **Bun** (runtime JS/TS, >22 M téléchargements/mois, racheté par **Anthropic** en décembre 2025), raconte la **réécriture complète de Bun de Zig vers Rust en 11 jours** (3→14 mai 2026), pilotée par Claude. La motivation est une classe de bugs récurrente — use-after-free, double-free, fuites — née du mélange mémoire gérée par GC (JavaScriptCore) et mémoire manuelle (Zig). En **safe Rust**, ces bugs deviennent des **erreurs de compilation** avec nettoyage automatique (`Drop`/RAII) : « une meilleure boucle de feedback qu'un guide de style ».

Contre le dogme « une réécriture est toujours une mauvaise idée » (un an de gel des correctifs pour 3 ingénieurs sur 535 496 lignes de Zig), Sumner opte pour un **portage mécanique** : préserver l'architecture, minimiser les changements de comportement, valider par la **suite de tests existante — écrite en TypeScript, donc indépendante du langage** (60 624 tests, 1,39 M assertions, 0 test supprimé, 6 plateformes).

Le harnais : **~50 dynamic workflows** dans **Claude Code**, en boucles *écrire → relire → appliquer*, tournant en continu. La brique de fiabilité est la **revue adversariale** : un second Claude, dans un **contexte séparé, qui ne voit que le diff** et doit « trouver pourquoi c'est faux ». Ratio **1 implémenteur / 2+ relecteurs / 1 fixer** ; l'implémenteur ne relit pas. Elle capte des bugs subtils, syntaxiquement identiques mais sémantiquement différents (un `Box` droppé avant un `uv_close` asynchrone ; `unwrap_or` eager qui panique). Principe cardinal : **« corriger le processus qui génère le code, pas le code à la main »** — quand un anti-pattern apparaît, on édite le prompt/workflow.

Préparation soignée : **PORTING.md** (mapping Zig→Rust) et **LIFETIMES.tsv** (lifetime de chaque champ de struct), essai sur 3 fichiers avant les 1 448. Puis **4 worktrees × 16 = ~64 Claude** en parallèle, après avoir interdit tout git non-atomique. Pic : **1 300 lignes/min**, **695 commits/h** ; **6 502 commits**, diff **+1 009 272 lignes**, ~16 000 erreurs de compilation traitées comme file d'attente (découpage en ~100 crates, résolution des dépendances cycliques).

Coût assumé : **5,9 Md tokens d'entrée non cachés + 690 M en sortie ≈ 165 000 $**, contre ~3 ingénieurs pendant un an — « qu'on n'aurait jamais fait ». Modèle : pré-version de **Claude Fable 5** (classe Mythos). Depuis le merge : **11 rounds** de revue de sécurité Claude Code, fuzzing 24/7 (100 Md exécutions → ~15 PRs), **4 % de code `unsafe`**, **19 régressions** corrigées. Premier release : Claude Code v2.1.181, **+10 % de démarrage sur Linux**. « This is the bleeding edge of what's possible today. »

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jarred Sumner | PERSONNE | a_créé | Bun | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Bun | TECHNOLOGIE | fait_partie_de | Anthropic | ORGANISATION | 0.95 | STATIQUE | déclaré_article |
| Jarred Sumner | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Jarred Sumner | PERSONNE | utilise | Claude Fable 5 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Bun | TECHNOLOGIE | utilise | Rust | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Rust | TECHNOLOGIE | remplace | Zig | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Rust | TECHNOLOGIE | réduit | use-after-free, double-free et fuites mémoire (erreurs de compilation en safe Rust) | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | permet | réécriture mécanique de Bun de Zig vers Rust en 11 jours | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| réécriture de Bun en Rust | EVENEMENT | utilise | dynamic workflows | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| dynamic workflows | METHODOLOGIE | utilise | revue adversariale | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| revue adversariale | METHODOLOGIE | réduit | régressions du code généré par LLM | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | permet | ~64 Claude en parallèle pendant 11 jours (4 worktrees × 16) | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| réécriture de Bun en Rust | EVENEMENT | utilise | suite de tests TypeScript indépendante du langage | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| Jarred Sumner | PERSONNE | mesure | ~165 000 $ (5,9 Md tokens d'entrée non cachés, 690 M en sortie) pour la réécriture | MESURE | 0.9 | STATIQUE | déclaré_article |
| Jarred Sumner | PERSONNE | recommande | corriger le processus qui génère le code plutôt que le code à la main | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Bun | TECHNOLOGIE | utilise | JavaScriptCore | TECHNOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | Bun | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Bun (réécrit en Rust) | TECHNOLOGIE | améliore | démarrage de Claude Code de ~10 % sur Linux | MESURE | 0.85 | STATIQUE | déclaré_article |
| coverage-guided fuzzing | METHODOLOGIE | résout | bugs de parsers de Bun (100 Md exécutions → ~15 PRs) | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Jarred Sumner | PERSONNE | affirme_que | one engineer can do a lot more today than a year ago | CITATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Bun | TECHNOLOGIE | catégorie | Runtime + bundler + package manager + test runner JS/TS ; >22 M téléchargements/mois ; réécrit de Zig vers Rust en mai 2026 | AJOUT |
| Jarred Sumner | PERSONNE | rôle | Créateur de Bun ; travaille chez Anthropic (rachat de Bun, déc. 2025) ; auteur de la réécriture Rust | AJOUT |
| Anthropic | ORGANISATION | rôle | A racheté Bun (déc. 2025) ; éditeur de Claude Fable 5 et Claude Code utilisés pour la réécriture | AJOUT |
| Claude Fable 5 | TECHNOLOGIE | rôle | Modèle (pré-version, classe Mythos) ayant réécrit Bun en Rust ; portage mécanique + revue adversariale | AJOUT |
| Claude Code | TECHNOLOGIE | rôle | Harnais des dynamic workflows ; a maintenu ~64 Claude en parallèle 11 jours ; 11 rounds de revue de sécurité post-merge | AJOUT |
| dynamic workflows | METHODOLOGIE | définition | ~50 boucles écrire→relire→appliquer tournant en continu dans Claude Code, éditables par prompt en cours de route | AJOUT |
| revue adversariale | METHODOLOGIE | principe | Un 2ᵉ Claude en contexte séparé ne voyant que le diff, sommé de trouver pourquoi le code est faux ; 1 implémenteur / 2+ relecteurs / 1 fixer ; l'implémenteur ne relit pas | AJOUT |
| Rust | TECHNOLOGIE | rôle | Langage cible ; safe Rust transforme UAF/double-free/fuites en erreurs de compilation, nettoyage auto via Drop (RAII) ; ~4 % de code unsafe après portage | AJOUT |
| Zig | TECHNOLOGIE | rôle | Langage source de Bun (535 496 lignes) ; cleanup explicite via defer/errdefer, pas de destructeurs implicites | MISE_A_JOUR |
| corriger le processus, pas le code | CONCEPT | principe | Face à un bug/anti-pattern récurrent, éditer le workflow/prompt qui génère le code plutôt que corriger le fichier à la main | AJOUT |
| suite de tests indépendante du langage | CONCEPT | rôle | Tests de Bun écrits en TypeScript (60 624 tests, 1,39 M expect(), 0 supprimé, 6 plateformes) → filet permettant de merger 1 M de lignes générées par LLM | AJOUT |
| PORTING.md / LIFETIMES.tsv | DOCUMENT | rôle | Artefacts de préparation générés par Claude : mapping patterns/types Zig→Rust, et lifetime tracé de chaque champ de struct | AJOUT |
| JavaScriptCore | TECHNOLOGIE | rôle | Moteur JS (Safari) embarqué par Bun ; sa gestion GC croisée avec la mémoire manuelle Zig est la source de la classe de bugs visée | AJOUT |
