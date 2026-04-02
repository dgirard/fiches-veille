# vincent-superpowers-agentic-skills-framework-github-2026-04-02

## Veille

Framework de compétences agentiques pour agents de codage — Superpowers — Méthodologie TDD — GitHub

## Titre Article

Superpowers: An agentic skills framework & software development methodology that works

## Date

2026-04-02

## URL

https://github.com/obra/superpowers

## Keywords

framework agentique, skills, agents de codage, Claude Code, TDD rouge/vert, git worktrees, subagents, brainstorming, méthodologie développement, plugin, YAGNI, DRY, workflow structuré, mémoire conversationnelle, marketplace, Prime Radiant

## Authors

Jesse Vincent (Prime Radiant)

## Ton

**Profil** : Documentation technique de projet open source, registre praticien-méthodologique, niveau technique intermédiaire à avancé.

**Description** : Le README adopte un ton de documentation pragmatique orienté développeur, centré sur le « comment ça marche » plutôt que sur la théorie. Le style est direct et structuré, avec des instructions d'installation pas à pas et une description fonctionnelle des compétences disponibles. L'autorité provient de l'expérience de terrain de Jesse Vincent et de la traction massive du projet (130k+ étoiles GitHub). Le registre est celui d'un artisan du logiciel qui partage ses outils éprouvés, pas celui d'un évangéliste. Le public cible est constitué de développeurs utilisant des agents de codage (Claude Code, Cursor, Codex, OpenCode) et cherchant à structurer leurs workflows agentiques.

## Pense-betes

- Superpowers est un framework de « skills » (fichiers SKILL.md en markdown) qui enseignent à l'agent de codage comment travailler de manière structurée
- Philosophie : l'agent ne code pas immédiatement — il brainstorme d'abord, fait valider un spec par l'humain par morceaux digestibles, puis planifie l'implémentation
- Principes fondamentaux : TDD rouge/vert strict, YAGNI (You Aren't Gonna Need It), DRY
- Installation via le système de plugins Claude Code : marketplace + plugin install
- Compatible multi-plateformes : Claude Code, Cursor, Codex, OpenCode (installation manuelle pour ces derniers)
- Catégories de skills : Testing (TDD, async, anti-patterns), Debugging (systématique, cause racine), Collaboration (brainstorming, planning, code review, agents parallèles), Development (git worktrees, branches, subagents), Meta (création et partage de skills)
- Écosystème de repos associés : superpowers-marketplace (marketplace curatée), superpowers-lab (skills expérimentaux), superpowers-skills (skills communautaires), superpowers-developing-for-claude-code
- Mémoire conversationnelle : duplique les transcriptions Claude hors de .claude (évite la suppression automatique après 1 mois), indexation vectorielle SQLite, résumés via Claude Haiku
- Très économe en tokens : le noyau injecte < 2k tokens, les skills sont chargés à la demande via script shell
- 130k+ étoiles GitHub en ~6 mois — l'un des projets développeur à la croissance la plus rapide
- Jesse Vincent est aussi connu pour K-9 Mail (devenu Thunderbird Android), VaccinateCA, et la maintenance du langage Perl
- Licence MIT — contribution ouverte via fork/PR

## RésuméDe400mots

Superpowers est un framework open source de compétences agentiques et une méthodologie de développement logiciel créé par Jesse Vincent et l'équipe de Prime Radiant. Disponible sur GitHub avec plus de 130 000 étoiles, il s'est imposé comme l'un des outils les plus adoptés pour structurer le travail des agents de codage IA.

Le principe fondateur est simple : au lieu de laisser l'agent se précipiter sur le code, Superpowers lui enseigne un workflow discipliné. Dès qu'un projet est détecté, l'agent engage d'abord une phase de brainstorming pour comprendre le véritable besoin. Il présente ensuite la spécification par morceaux suffisamment courts pour être réellement lus et validés par l'humain. Une fois le design approuvé, l'agent élabore un plan d'implémentation avant d'écrire la moindre ligne de code.

Le framework repose sur des fichiers SKILL.md en markdown qui servent d'instructions structurées. Ces skills couvrent cinq domaines : le testing (TDD rouge/vert strict, tests asynchrones, anti-patterns), le debugging (approche systématique, traçage de cause racine, vérification), la collaboration (brainstorming, planification, revue de code, agents parallèles), le développement (git worktrees, gestion de branches, workflows subagents) et les méta-compétences (création, test et partage de nouveaux skills).

L'architecture est remarquablement économe en tokens : le noyau injecte moins de 2 000 tokens au démarrage. Les skills supplémentaires sont chargés à la demande via un script shell qui les recherche et les lit. Cette frugalité est essentielle pour ne pas gaspiller le contexte de l'agent.

Superpowers intègre aussi un système de mémoire conversationnelle. Il duplique les transcriptions des conversations Claude en dehors du répertoire .claude (pour éviter leur suppression automatique après un mois), les indexe dans une base SQLite avec recherche vectorielle, et génère des résumés via Claude Haiku.

Le projet est compatible avec plusieurs plateformes d'agents : Claude Code via son système de plugins natif, Cursor, Codex et OpenCode (avec installation manuelle pour ces derniers). Un écosystème de dépôts satellites complète le projet principal : une marketplace curatée, un laboratoire de skills expérimentaux, une collection de skills communautaires et des outils pour développer des plugins Claude Code.

Les principes méthodologiques sous-jacents — TDD strict, YAGNI, DRY — traduisent une vision où la qualité logicielle ne doit pas être sacrifiée par l'automatisation, mais au contraire renforcée par une structure qui guide l'agent vers les bonnes pratiques.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Jesse Vincent | PERSONNE | a_créé | Superpowers | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Prime Radiant | ORGANISATION | développe | Superpowers | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | impose | workflow brainstorming avant code | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Superpowers | TECHNOLOGIE | applique | TDD rouge/vert strict | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Superpowers | TECHNOLOGIE | est_compatible_avec | Claude Code | TECHNOLOGIE | 0.98 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | est_compatible_avec | Cursor | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | utilise | fichiers SKILL.md | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Superpowers | TECHNOLOGIE | intègre | mémoire conversationnelle SQLite | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | consomme | moins de 2k tokens au démarrage | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Superpowers | TECHNOLOGIE | a_atteint | 130k+ étoiles GitHub | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Jesse Vincent | PERSONNE | a_créé | K-9 Mail | TECHNOLOGIE | 0.92 | STATIQUE | inféré |
| Superpowers | TECHNOLOGIE | respecte | YAGNI et DRY | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Skills communautaires | CONCEPT | étendent | Superpowers | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Superpowers | TECHNOLOGIE | catégorie | Framework de skills agentiques pour agents de codage | AJOUT |
| Superpowers | TECHNOLOGIE | licence | MIT | AJOUT |
| Superpowers | TECHNOLOGIE | étoiles GitHub | 130 000+ | AJOUT |
| Jesse Vincent | PERSONNE | rôle | Créateur Superpowers, CEO Prime Radiant | AJOUT |
| Prime Radiant | ORGANISATION | secteur | Outils de développement IA agentique | AJOUT |
| SKILL.md | CONCEPT | description | Fichiers markdown servant d'instructions structurées pour agents | AJOUT |
| Superpowers Marketplace | TECHNOLOGIE | description | Marketplace curatée de plugins Claude Code | AJOUT |
| Superpowers Lab | TECHNOLOGIE | description | Dépôt de skills expérimentaux en cours de test | AJOUT |
| K-9 Mail | TECHNOLOGIE | description | Client email Android devenu Thunderbird for Android | AJOUT |
