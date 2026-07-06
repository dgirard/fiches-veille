# thariq-field-guide-fable-finding-unknowns-2026-07-03

## Veille

Fil X (thread illustré) de **Thariq Shihipar** (équipe Claude Code / Anthropic) : un *field guide* pour tirer le meilleur de **Claude Fable 5**. Thèse centrale reprise de Korzybski — *« la carte n'est pas le territoire »* : la **carte** = ce qu'on donne à Claude (prompts, skills, contexte) ; le **territoire** = là où le travail se fait (codebase, contraintes réelles) ; l'écart entre les deux = les **unknowns** (inconnues). Fable est *« le premier modèle où la qualité du travail est plafonnée par ma capacité à clarifier ses inconnues »*. L'article fournit un **cadre à 4 quadrants** (known knowns / known unknowns / unknown knowns / unknown unknowns) et une **boîte à outils de techniques** ordonnées dans le temps (avant / pendant / après l'implémentation) — blindspot pass, brainstorms & prototypes, interviews, references, implementation plan, implementation-notes, pitches & explainers, quizzes — chacune avec des exemples de prompts. Domaine : ingénierie de prompt, agents de codage, méthodologie de travail avec l'IA, artefacts HTML.

## Titre Article

A Field Guide to Fable: Finding Your Unknowns

## Date

2026-07-03

## URL

https://x.com/trq212/status/2073100352921215386

## Keywords

Unknowns, carte vs territoire, known/unknown knowns, unknown unknowns, blindspot pass, brainstorm, prototype, interview, references, implementation plan, implementation-notes.md, pitches et explainers, quizzes, artefacts HTML, Claude Fable 5, Claude Design, thought partner, ingénierie de prompt, tâches longue-horizon, découverte itérative des inconnues

## Authors

Thariq Shihipar (@trq212)

## Ton

**Profil** : guide de terrain (« field guide ») à la première personne, registre praticien réflexif et pédagogique, publié comme fil X longform illustré de 4 diagrammes. Niveau technique moyen-élevé, adressé aux utilisateurs quotidiens d'agents de codage.

**Style** : essai charpenté autour d'une **métaphore filée cartographique** empruntée à la sémantique générale (« the map is not the territory ») et déclinée jusqu'à la chute (« Matching the Map and Territory »). Structure temporelle explicite (avant / pendant / après l'implémentation) doublée d'un cadre conceptuel emprunté à Rumsfeld/Johari (la matrice 2×2 des connus/inconnus). Autorité par **auto-démonstration incarnée** : Thariq raconte comment il a monté la **vidéo de lancement de Fable** entièrement avec Claude Code alors qu'il n'y connaissait rien (transcription Whisper, découpe ffmpeg, UI timée via Remotion, *color grading* qu'il a fait *enseigner* par Claude). Chaque technique est livrée avec des **exemples de prompts** copiables — c'est un guide opérationnel, pas une théorie. Formules-doctrine : *« reducing and planning for your unknowns is THE skill of agentic coding »*, *« every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out what you didn't know before it gets expensive to fix »*, *« I only merge after I pass the quiz perfectly »*, *« what you learn becomes the map for next time »*. **Public cible** : ingénieurs et makers travaillant avec Claude, y compris hors de leur zone d'expertise.

## Pense-betes

- **Métaphore-cadre : la carte n'est pas le territoire.** La **carte** = ce qu'on donne à Claude (prompts, skills, contexte). Le **territoire** = où le travail se fait (codebase, monde réel, contraintes). L'écart entre les deux = les **unknowns**. Face à une inconnue, Claude *décide sur sa meilleure supposition de ce qu'on veut* → plus le travail est gros, plus il rencontre d'inconnues.
- **Le plateau Fable.** *« Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns »* — le goulot d'étranglement s'est déplacé du modèle vers **la clarté de l'humain**. Planifier à l'avance ne suffit pas : les inconnues surgissent en pleine implémentation, ou révèlent qu'il fallait résoudre le problème **autrement**. → processus **itératif** : découvrir ses inconnues **avant, pendant et après**.
- **Les 4 quadrants (matrice des inconnues)** : **Known knowns** = ce qui est dans le prompt (ce qu'on dit vouloir) ; **Known unknowns** = ce qu'on n'a pas encore résolu mais dont on est conscient ; **Unknown knowns** = *« trop évident pour l'écrire, mais je le reconnaîtrais »* (le « I'll know it when I see it ») ; **Unknown unknowns** = *« le nid-de-poule dont on ignorait que la route pouvait l'avoir »*.
- **La vraie compétence** : *« reducing and planning for your unknowns is THE skill of agentic coding »*. Les meilleurs (cite **Boris**, **Jarred**) ont **peu d'inconnues** (en phase avec le codebase ET les comportements du modèle) mais **assument** qu'il en reste. Bonne nouvelle : c'est une compétence qui **s'améliore en travaillant avec Claude**.
- **Instruire Claude = équilibre délicat.** Trop précis → Claude suit les instructions même quand un **pivot** serait meilleur. Trop vague → Claude comble avec les *industry best practices*, pas forcément adaptées. Sans gérer ses inconnues, **on échoue des deux côtés**. Remède : donner à Claude le **contexte de son point de départ** (où on en est dans sa réflexion, son expérience du problème) et le traiter en **thought partner**. Claude cherche codebase + web très vite et itère depuis l'échec plus vite que nous.
- **AVANT — Blindspot pass** : quand on travaille dans une zone inconnue (unknown unknowns), demander à Claude de **trouver et expliquer ses angles morts**. Utiliser les mots littéraux *« blindspot pass »* et *« unknown unknowns »* + contexte sur qui on est. Ex. *« I'm adding a new auth provider but I know nothing about the auth modules… do a blindspot pass »* ; *« teach me to understand my unknown unknowns about color grading so I can prompt better »*.
- **AVANT — Brainstorms & prototypes** : pour les **unknown knowns** (critères qu'on ne sait définir qu'en les voyant, ex. design visuel). Les verbaliser **tôt** car les découvrir en implémentation coûte cher (un petit changement de spec = code radicalement différent, dur à revert). Démarrer **presque chaque session** par une phase d'exploration/brainstorm pour cadrer le scope (ni trop étroit ni trop large). Ex. *« make me an HTML page with 4 wildly different design directions so I can react to them »* ; *« mock the new toolbar in a single HTML file with fake data before you touch the real app »* ; *« brainstorm 10 places we could intervene, cheapest to most ambitious »*.
- **AVANT — Interviews** : après le brainstorm, demander à Claude de **nous interviewer** sur les ambiguïtés restantes, **une question à la fois**, en priorisant *« questions where my answer would change the architecture »*.
- **AVANT — References** : quand on ne sait pas décrire ce qu'on veut, **la meilleure référence est du code source**. Pointer Fable vers un dossier/une lib (même dans un autre langage) et dire quoi y chercher. **Claude Design** fonctionne ainsi : pointé vers un module d'un site, il **lit le code sous-jacent** (markup, structure, construction réelle), pas juste la capture. Ex. *« this Rust crate implements the exact backoff I want — reimplement the same semantics in our TypeScript client »*.
- **AVANT — Implementation plan** : demander un plan **menant par les décisions les plus susceptibles de changer** (modèles de données, interfaces de types, flux UX) et **reléguant le refactoring mécanique en bas** (*« I trust you on that part »*). Le plan **fait remonter** ce qu'on aura vraiment besoin d'altérer.
- **PENDANT — Implementation notes** : quelle que soit la planification, **des unknown unknowns subsistent** (l'agent trouve un edge case en codant). Faire tenir à Claude Code un **`implementation-notes.md`** temporaire journalisant les décisions *« so we can learn from our next attempt »*. Ex. *« if you hit an edge case that forces a deviation, pick the conservative option, log it under 'Deviations', and keep going »*.
- **APRÈS — Pitches & explainers** : *shipper* = obtenir **buy-in et approbations**. Empaqueter prototype + spec + notes en **un seul doc** qui *« lead with the demo GIF »* → accélère la compréhension (les reviewers **partent des mêmes inconnues que soi**) et les approbations (les experts veulent voir qu'on a couvert leurs points de défaillance).
- **APRÈS — Quizzes** : après une longue session, lire les diffs ne donne qu'une compréhension **superficielle** (le comportement dépend de chemins de code existants). Demander à Claude un **rapport HTML + un quiz** sur les changements — *« I only merge after I pass the quiz perfectly »*.
- **Preuve par l'exemple : la vidéo de lancement de Fable**, montée **entièrement avec Claude Code** dans un domaine que Thariq ne maîtrisait pas — il part de ce qu'il sait (Claude sait éditer/transcrire de la vidéo par le code), fait **expliquer** Whisper/ffmpeg, **prototype** une UI timée aux mots via Remotion, puis fait **enseigner le color grading** par Claude (n'ayant pas d'idée de ce que « bon » veut dire) au lieu de générer des variantes à l'aveugle.
- **Chute** : *« every explainer, brainstorm, interview, prototype, and reference is a cheap way to find out what you didn't know before it gets expensive to fix »* → *« start your next project by asking Claude to help you find your unknowns »*. Le résidu d'apprentissage devient la carte de la prochaine fois (« what you learn becomes the map for next time »).
- **Liens** : converge avec le *Compounding Knowledge Lifecycle* (capitaliser l'appris), le *loop engineering* et la note **[[willison-fable-judgement-delegation-subagents-2026-07-03]]** (même auteur cité, Thariq, même moment sur Fable) — deux facettes complémentaires : Willison sur **laisser Fable juger**, Thariq sur **réduire ses propres inconnues pour mieux le guider**.

## RésuméDe400mots

Dans ce *field guide* publié le 3 juillet 2026, **Thariq Shihipar** (équipe Claude Code) formalise une pratique pour exploiter **Claude Fable 5**. Point de départ, emprunté à Korzybski : *« la carte n'est pas le territoire »*. La **carte**, c'est ce qu'on donne à Claude — prompts, skills, contexte. Le **territoire**, c'est là où le travail se fait — le codebase, le monde réel, ses contraintes. L'écart entre les deux, il l'appelle les **unknowns** : quand Claude y bute, il décide sur sa meilleure supposition de ce qu'on veut. Plus le travail est vaste, plus il rencontre d'inconnues. Fable est *« le premier modèle où la qualité du travail est plafonnée par ma capacité à clarifier ses inconnues »* — le goulot s'est déplacé du modèle vers la clarté de l'humain.

Thariq propose une **matrice 2×2** : *known knowns* (ce qui est dans le prompt), *known unknowns* (ce qu'on sait ne pas savoir), *unknown knowns* (l'évident qu'on n'écrit pas mais reconnaîtrait) et *unknown unknowns* (ce qu'on n'a jamais envisagé). Réduire et anticiper ses inconnues est, selon lui, **LA compétence** du codage agentique — et elle s'apprend en travaillant avec Claude. Instruire reste un équilibre : trop précis, Claude suit même quand un pivot vaudrait mieux ; trop vague, il comble avec des *best practices* inadaptées.

Suit une **boîte à outils** ordonnée dans le temps, chaque technique livrée avec des prompts. **Avant** : le *blindspot pass* (faire expliciter ses angles morts), les *brainstorms & prototypes* (verbaliser tôt les *unknown knowns*, ex. 4 directions de design en HTML), les *interviews* (Claude nous questionne une question à la fois, priorité à ce qui change l'architecture), les *references* (la meilleure étant du code source — c'est ainsi que fonctionne **Claude Design**), et l'*implementation plan* menant par ce qui risque de changer. **Pendant** : un `implementation-notes.md` où l'agent journalise ses déviations. **Après** : les *pitches & explainers* (un doc unique menant par la démo, car les reviewers partent des mêmes inconnues) et les *quizzes* (« I only merge after I pass the quiz perfectly »).

Preuve à l'appui : la **vidéo de lancement de Fable**, montée entièrement avec Claude Code dans un domaine inconnu de l'auteur, jusqu'à faire *enseigner* le color grading par le modèle. Morale : chaque artefact est un moyen bon marché de découvrir ce qu'on ignorait **avant que ce soit coûteux à corriger**. *« Start your next project by asking Claude to help you find your unknowns. »*

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Thariq Shihipar | PERSONNE | travaille_chez | équipe Claude Code (Anthropic) | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Thariq Shihipar | PERSONNE | affirme_que | "Fable est le premier modèle où la qualité du travail est plafonnée par ma capacité à clarifier ses inconnues" | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Finding Your Unknowns | METHODOLOGIE | s_applique_à | travail avec Claude Fable 5 | TECHNOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| Finding Your Unknowns | METHODOLOGIE | est_basé_sur | "la carte n'est pas le territoire" | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Matrice des inconnues | CONCEPT | fait_partie_de | Finding Your Unknowns | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| Thariq Shihipar | PERSONNE | affirme_que | "reducing and planning for your unknowns is THE skill of agentic coding" | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Blindspot pass | METHODOLOGIE | permet | expliciter les unknown unknowns avant l'implémentation | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Brainstorms & prototypes | METHODOLOGIE | permet | verbaliser tôt les unknown knowns (moins cher qu'en implémentation) | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| References (code source) | METHODOLOGIE | résout | l'incapacité à décrire ce qu'on veut en détail | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Claude Design | TECHNOLOGIE | utilise | lecture du code sous-jacent d'un module (pas seulement la capture) | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| implementation-notes.md | DOCUMENT | permet | journaliser les déviations pendant l'implémentation | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Quizzes | METHODOLOGIE | améliore | la compréhension réelle d'un changement avant le merge | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Pitches & explainers | METHODOLOGIE | permet | obtenir buy-in et approbations (reviewers partant des mêmes inconnues) | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | a_créé | vidéo de lancement de Fable | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Instruction de Claude | CONCEPT | affirme_que | trop spécifique empêche le pivot, trop vague invoque des best practices inadaptées | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Finding Your Unknowns | METHODOLOGIE | définition | Processus itératif de découverte des inconnues (avant/pendant/après) pour guider Fable | AJOUT |
| Matrice des inconnues | CONCEPT | structure | 4 quadrants : known knowns, known unknowns, unknown knowns, unknown unknowns | AJOUT |
| Unknowns | CONCEPT | définition | Écart entre la carte (prompts/contexte) et le territoire (codebase/réel) | AJOUT |
| Blindspot pass | METHODOLOGIE | usage | Faire expliciter par Claude ses unknown unknowns dans une zone inconnue | AJOUT |
| Brainstorms & prototypes | METHODOLOGIE | usage | Réagir tôt à des directions (ex. 4 designs HTML) pour capter les unknown knowns | AJOUT |
| Interviews | METHODOLOGIE | usage | Claude interroge l'humain une question à la fois, priorité aux réponses qui changent l'architecture | AJOUT |
| References | METHODOLOGIE | principe | La meilleure référence est du code source (même dans un autre langage) | AJOUT |
| Implementation plan | METHODOLOGIE | principe | Mener par les décisions susceptibles de changer (data models, types, UX) | AJOUT |
| implementation-notes.md | DOCUMENT | rôle | Fichier temporaire où l'agent journalise ses déviations pendant le build | AJOUT |
| Quizzes | METHODOLOGIE | règle | Ne merger qu'après avoir réussi parfaitement le quiz sur le changement | AJOUT |
| Claude Fable 5 | TECHNOLOGIE | caractéristique | Modèle dont la qualité de sortie est plafonnée par la clarté des inconnues de l'humain | AJOUT |
| Claude Design | TECHNOLOGIE | mécanisme | Lit le code sous-jacent d'un composant/site référencé, pas seulement le rendu | AJOUT |
| Thariq Shihipar | PERSONNE | rôle | Équipe Claude Code (Anthropic), auteur du field guide | AJOUT |
| Vidéo de lancement de Fable | DOCUMENT | production | Montée entièrement avec Claude Code (transcription Whisper, ffmpeg, Remotion, color grading) | AJOUT |
