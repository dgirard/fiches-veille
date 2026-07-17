---
themes: [agents-codage-ia-skills, philosophie-societe, transformation-adoption]
source: "lore.kernel.org (linux-media)"
---
# torvalds-llm-outil-kernel-2026-07-14

## Veille

Message de **Linus Torvalds** sur la mailing list **linux-media** (thread « Linking Patchwork with Sashiko? », outil LLM d'aide aux mainteneurs), où le créateur et **top-level maintainer** du noyau Linux **tranche officiellement la position du projet sur l'IA**. Répondant à Roman Gushchin qui pointait qu'un message adverse exprimait « une position très anti-LLM en général », Torvalds acquiesce (« Yes ») puis **récuse frontalement que ce soit la position du kernel** (« And no, that's not the position of the Linux kernel »). Il **pose le pied** en tant que mainteneur suprême : **« Linux n'est pas un de ces projets anti-IA »** ; ceux que cela dérange peuvent **« faire le truc open source : forker »** — « ou juste partir ». **Thèse centrale** : **« l'IA est un outil, comme les autres outils qu'on utilise, et clairement un outil utile »** ; ce n'était « peut-être pas si "clairement" il y a un an, mais ce n'est plus en question aujourd'hui ». Il distingue les questions **encore ouvertes** (« à quoi ressemblera vraiment l'économie de l'IA au final ») de la question **tranchée** (« est-ce utile ? ») — « quiconque en doute n'a clairement pas vraiment essayé ». Il **concède** que l'outil peut être **« douloureux »** — charge des mainteneurs, et le fait qu'il « n'arrête pas de trouver des bugs embarrassants » — mais refuse la posture de l'autruche (« mettre la tête dans le sable en chantant "La La La, I can't hear you" »). **La bonne réponse** : faire en sorte que **les outils LLM _aident_ les mainteneurs** plutôt que de leur causer de la peine. **Non-coercition assumée** : « on ne force personne à l'utiliser, mais **j'ignorerai très bruyamment ceux qui cherchent à empêcher d'autres de l'utiliser** ». Sur l'imperfection : « l'IA n'est pas parfaite, mais bon sang, quiconque pointe ses problèmes ferait bien de se pointer aussi lui-même dans le miroir » — « **l'intelligence naturelle n'est pas toujours si géniale non plus** ». **Cadre de gouvernance** : le projet kernel « a toujours été et restera une affaire de **technologie** » ; l'angle social de l'open source est un « bénéfice secondaire, pas le _but_ » ; **« ce n'est PAS un projet de "social warrior", ne l'a jamais été et ne le sera jamais »** ; « on fait de l'open source parce que ça produit une **meilleure technologie**, pas pour des raisons religieuses ». Conclusion-programme : **« on décide d'abord sur le mérite technique. Pas sur la peur des nouveaux outils. »** À lire comme une **prise de position doctrinale** d'une des figures les plus influentes du logiciel — écho au contre-témoignage pro-LLM d'ESR (autre pilier de l'open source, [[raymond-llm-coding-empowering-2026-07-08]]).

## Titre Article

Re: Linking Patchwork with Sashiko? (message linux-media sur la position du kernel Linux vis-à-vis de l'IA)

## Date

2026-07-14

## URL

https://lore.kernel.org/linux-media/CAHk-=wi4zC+Ze8e+p3tMv8TtG_80KzsZ1syL9anBtmEh5Z40vg@mail.gmail.com/

## Keywords

Linus Torvalds, Linux, noyau Linux, kernel, linux-media, lore.kernel.org, Patchwork, Sashiko, Roman Gushchin, mainteneurs, maintainers, top-level maintainer, LLM, IA, AI, outil utile, anti-IA, anti-LLM, position du projet, gouvernance open source, fork, forker, mérite technique, technical merit, peur des nouveaux outils, économie de l'IA, bugs embarrassants, charge des mainteneurs, intelligence naturelle, social warrior, raisons religieuses, meilleure technologie, non-coercition, aide aux mainteneurs, tri de patchs, revue de code, open source, doctrine, prise de position

## Authors

Linus Torvalds (torvalds@linuxfoundation.org) — ingénieur logiciel finlando-américain, **créateur et mainteneur suprême du noyau Linux** (depuis 1991) et de **Git** (2005). Employé de la **Linux Foundation**. Figure centrale et notoirement franche de l'open source, dont la parole sur les mailing lists du kernel fait autorité et jurisprudence dans la communauté. S'exprime ici en sa qualité de **top-level maintainer** pour fixer la position officielle du projet vis-à-vis des outils d'IA. Autres participants au thread cités : Roman Gushchin (linux.dev), Laurent Pinchart, Mauro Carvalho Chehab, Konstantin Ryabitsev (Linux Foundation), Steven Rostedt, Stephen Finucane, Jason Gunthorpe, entre autres. (Message de mailing list linux-media ; date : 2026-07-14 ; date d'ajout à la veille : 2026-07-17.)

## Ton

**Profil** : message de mailing list technique en registre **directif et doctrinal**, posté par une autorité qui **tranche** un débat de communauté. Ce n'est pas une opinion parmi d'autres : Torvalds **fixe la politique** du projet (« put my foot down as the top-level maintainer ») et assume le caractère non négociable de sa décision.

**Style** : caractéristique de Torvalds — **direct, tranchant, imagé, sans détour**. Ultimatum assumé (« fork it. Or just walk away »), exclamations (« Christ »), figures parlantes (l'autruche qui chante « La La La, I can't hear you », le miroir de l'intelligence naturelle), majuscules d'emphase (« *NOT* some kind of "social warrior" project »). Le propos combine **pragmatisme technique** (l'IA comme outil jugé sur son mérite, pas sur la peur), **honnêteté sur les coûts** (l'outil est « douloureux », trouve des « bugs embarrassants ») et une **délimitation idéologique** nette : le kernel est un projet *technologique*, pas *militant*. Ton de gouvernance : non-coercitif sur l'usage, mais **intransigeant contre ceux qui voudraient l'interdire aux autres**.

## Pense-betes

- **La position officielle, tranchée par l'autorité suprême.** À retenir tel quel : **« Linux n'est pas un projet anti-IA »**, et Torvalds **« pose le pied »** en tant que top-level maintainer. Le désaccord n'est pas censuré mais il est **hors politique du projet** : « faites le truc open source, forkez — ou partez ». Rare cas où la doctrine IA d'un grand projet open source est **édictée explicitement**.
- **La thèse en une phrase : « l'IA est un outil, et clairement un outil utile ».** L'utilité **n'est plus une question ouverte** (« ça ne l'était peut-être pas il y a un an, ça ne l'est plus »). Torvalds **sépare deux débats** : (a) *questions encore ouvertes* — notamment **« à quoi ressemblera l'économie de l'IA »** ; (b) *question tranchée* — **« est-ce utile ? »**. Pique : « quiconque en doute **n'a clairement pas vraiment essayé** ».
- **Honnêteté sur le coût — l'IA est « douloureuse ».** Concession notable : surcharge des **mainteneurs**, et l'IA « n'arrête pas de trouver des **bugs embarrassants** ». Mais la réponse n'est pas l'**autruche** (« La La La, I can't hear you ») : c'est de **faire en sorte que les LLM _aident_ les mainteneurs** au lieu de leur nuire (c'est tout l'enjeu du thread Patchwork↔Sashiko).
- **Gouvernance : non-coercition + intransigeance.** Formule-clé : **« on ne force personne à l'utiliser, mais j'ignorerai très bruyamment ceux qui cherchent à empêcher les autres de l'utiliser »**. La liberté d'usage est protégée ; le **veto anti-IA imposé aux autres** ne l'est pas.
- **« L'intelligence naturelle n'est pas toujours géniale non plus. »** Réplique au reproche d'imperfection de l'IA : qui pointe ses défauts « ferait bien de se pointer aussi dans le miroir ». Argument à garder pour désamorcer le double standard humain/IA.
- **Délimitation idéologique : technologie, pas militantisme.** Le kernel « **a toujours été et restera une affaire de technologie** » ; l'angle social de l'open source est un **bénéfice secondaire, pas le but** ; **« ce n'est PAS un projet de social warrior »**. On fait de l'open source « parce que ça produit une **meilleure technologie**, pas pour des raisons religieuses ». Chute-programme : **« décisions d'abord sur le mérite technique — pas sur la peur des nouveaux outils »**.
- **Contexte : Patchwork ↔ Sashiko.** Le débat concret porte sur **relier Patchwork** (suivi des patchs par email du kernel) à **Sashiko** (assistant LLM d'aide aux mainteneurs). L'objection adverse : cela rendrait « le but de Sashiko — aider les mainteneurs — inatteignable » si l'on complexifie chaque cas d'usage pour éviter les LLM. Torvalds requalifie : le vrai sujet n'est pas *comment compliquer*, mais *assumer que les LLM aident*.
- **Usage veille** : **prise de position doctrinale** (pas du reporting), à haute valeur symbolique — deux **piliers de l'open source** (Torvalds ici, ESR dans [[raymond-llm-coding-empowering-2026-07-08]]) affichent en juillet 2026 un **pragmatisme pro-LLM** contre le camp « anti-IA ». Utile pour la thèse « l'adoption de l'IA de codage se joue en gouvernance de communauté et non seulement en outillage », et comme **contrepoint faisant autorité** aux discours de désillusion.

## RésuméDe400mots

Dans un message sur la mailing list **linux-media** (thread « Linking Patchwork with Sashiko? », à propos d'un outil LLM d'aide aux mainteneurs), **Linus Torvalds** — créateur et **mainteneur suprême du noyau Linux** — **fixe la position officielle du projet vis-à-vis de l'IA**.

**Le verdict.** Roman Gushchin observait qu'un message adverse exprimait « une position très anti-LLM en général ». Torvalds acquiesce (« Yes »), puis **récuse que ce soit la ligne du kernel** : **« Linux n'est pas un projet anti-IA »**, et il **« pose le pied » en tant que top-level maintainer**. Ceux que cela dérange peuvent **« faire le truc open source : forker »** — « ou juste partir ».

**La thèse.** **« L'IA est un outil, comme les autres, et clairement un outil utile. »** Ce n'était « peut-être pas si clair il y a un an, ça ne l'est plus aujourd'hui ». Il distingue les **questions ouvertes** (« à quoi ressemblera l'économie de l'IA au final ») de la **question tranchée** (« est-ce utile ? ») : « quiconque en doute **n'a pas vraiment essayé** ».

**Les coûts, assumés.** L'IA peut être un outil **« douloureux »** — pour la charge des **mainteneurs**, et parce qu'elle « n'arrête pas de trouver des **bugs embarrassants** ». Mais la réponse n'est pas l'**autruche** (« La La La, I can't hear you ») : c'est de **faire en sorte que les LLM _aident_** les mainteneurs plutôt que de leur nuire.

**La gouvernance.** **« On ne force personne à l'utiliser, mais j'ignorerai très bruyamment ceux qui cherchent à empêcher les autres de l'utiliser. »** Sur l'imperfection : « l'IA n'est pas parfaite, mais quiconque pointe ses problèmes ferait bien de se regarder dans le miroir — **l'intelligence naturelle n'est pas toujours si géniale non plus** ».

**Le cadre.** Le projet kernel « a toujours été et restera une affaire de **technologie** » ; l'angle social de l'open source est un **bénéfice secondaire, pas le but** ; **« ce n'est PAS un projet de "social warrior" »**. On fait de l'open source « parce que ça produit une **meilleure technologie**, pas pour des raisons religieuses ». D'où la conclusion-programme : **« on décide d'abord sur le mérite technique. Pas sur la peur des nouveaux outils. »**

Une **prise de position doctrinale** faisant autorité, à lire en écho au contre-témoignage pro-LLM d'Eric S. Raymond, autre pilier de l'open source.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Linus Torvalds | PERSONNE | dirige | Linux | TECHNOLOGIE | 0.98 | DYNAMIQUE | généré_assistant |
| Linus Torvalds | PERSONNE | affirme_que | l'IA est un outil comme les autres, et clairement un outil utile | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | Linux n'est pas un projet anti-IA ; c'est la position officielle du kernel | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | l'utilité de l'IA n'est plus une question ouverte ; quiconque en doute n'a pas vraiment essayé | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | l'IA peut être un outil douloureux (charge des mainteneurs) mais trouve des bugs embarrassants | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Linus Torvalds | PERSONNE | recommande | faire en sorte que les outils LLM aident les mainteneurs plutôt que de leur causer de la peine | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | on ne force personne à utiliser l'IA, mais il ignorera bruyamment ceux qui veulent empêcher les autres de l'utiliser | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | le projet kernel décide d'abord sur le mérite technique, pas sur la peur des nouveaux outils | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | le kernel est un projet technologique, pas un projet de social warrior ; l'angle social est un bénéfice secondaire | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | l'économie de l'IA reste une question ouverte, contrairement à son utilité | AFFIRMATION | 0.8 | DYNAMIQUE | déclaré_article |
| Sashiko | TECHNOLOGIE | permet | aider les mainteneurs du kernel via des LLM | AFFIRMATION | 0.8 | DYNAMIQUE | déclaré_article |
| Sashiko | TECHNOLOGIE | s_applique_à | Patchwork | TECHNOLOGIE | 0.75 | DYNAMIQUE | déclaré_article |
| LLM | TECHNOLOGIE | permet | trouver des bugs embarrassants dans le code | AFFIRMATION | 0.8 | ATEMPOREL | déclaré_article |
| Roman Gushchin | PERSONNE | soutient | l'usage des LLM pour aider les mainteneurs (Sashiko) | AFFIRMATION | 0.8 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Linus Torvalds | PERSONNE | rôle | Créateur et mainteneur suprême du noyau Linux (et de Git) ; fixe ici la position officielle du projet pro-outils IA, sur critère de mérite technique | AJOUT |
| Linux | TECHNOLOGIE | catégorie | Noyau open source dirigé par Torvalds ; adopte officiellement une position non anti-IA (l'IA comme outil jugé sur son mérite technique) | AJOUT |
| Sashiko | TECHNOLOGIE | catégorie | Outil/assistant à base de LLM destiné à aider les mainteneurs du kernel ; objet du thread « Linking Patchwork with Sashiko? » | AJOUT |
| Patchwork | TECHNOLOGIE | catégorie | Outil de suivi des patchs par email de la communauté kernel ; envisagé en liaison avec Sashiko | AJOUT |
| Roman Gushchin | PERSONNE | rôle | Développeur kernel (linux.dev) ; défend dans le thread l'usage des LLM pour aider les mainteneurs, contre une position jugée « très anti-LLM » | AJOUT |
| mérite technique | CONCEPT | principe de gouvernance | Critère de décision revendiqué du projet kernel : on adopte les outils (dont l'IA) sur leur valeur technique, « pas sur la peur des nouveaux outils » ni pour des raisons idéologiques | AJOUT |
| IA comme outil | CONCEPT | position Torvalds | L'IA traitée comme un outil parmi d'autres, « clairement utile » ; utilité non négociable, imperfections assumées (« l'intelligence naturelle non plus n'est pas parfaite »), usage non imposé mais interdiction refusée | AJOUT |
