# karpathy-vibe-coding-agentic-engineering-software-3-0-2026-04-29

## Veille
Interview d'Andrej Karpathy (co-fondateur OpenAI, ex-Tesla Autopilot) qui passe de la *vibe coding* à l'*agentic engineering* : December 2025 comme bascule "never felt more behind as a programmer", taxonomie Software 1.0/2.0/3.0, exemple openclaw (script bash → texte à copier-coller dans l'agent) et MenuGen rendu obsolète par Nanobanana de Gemini, théorie de la *verifiability* expliquant pourquoi les LLMs sont *jagged* (math/code peakent, "marche jusqu'au lavage 50m" échoue), distinction *vibe coding* (raise the floor) vs *agentic engineering* (préserver le quality bar), métaphore "animaux vs fantômes", refonte du recrutement par projets agent-versus-agent, et formule clé : ***"You can outsource your thinking but you can't outsource your understanding."***

## Titre Article
Andrej Karpathy: From Vibe Coding to Agentic Engineering

## Date
2026-04-29

## URL
https://www.youtube.com/watch?v=96jN2OCOfLs

## Keywords
Andrej Karpathy, vibe coding, agentic engineering, Software 1.0, Software 2.0, Software 3.0, December 2025 transition, OpenAI co-founder, Tesla Autopilot, jagged intelligence, verifiability, RL environments, openclaw installation, copy-paste paradigm, MenuGen, Nanobanana, Gemini, image generation, LLM as computer, prompt as programming, neural net host process, Opus 4.7, car wash example, animals vs ghosts, ghosts metaphor, statistical simulation circuits, agent native infrastructure, sensors actuators, agent representation, hiring refactoring, Twitter clone red team, 10x engineer magnified, taste judgment design, plan mode, intern entities, micro GPT, LLM knowledge bases, wiki synthesis, outsource thinking understanding, fine tuning lever, council of LLM judges, jagged frontier, AI Startup School

## Authors
Andrej Karpathy (co-fondateur OpenAI, ex-Tesla Autopilot, créateur du terme "vibe coding")

## Ton
**Profil** : Interview-conférence en format Q&R sur scène, ton conversationnel et réflexif. Karpathy parle à la première personne avec hésitations naturelles ("uh", "I think", "yeah"), ce qui renforce l'autorité par contraste — il est l'un des architectes de l'IA moderne ("helped build modern AI, then explain modern AI, and then occasionally rename modern AI", co-fondateur OpenAI, créateur de l'Autopilot Tesla, inventeur du terme *vibe coding*). Public cible : fondateurs et ingénieurs en early stage AI, audience d'AI Startup School / Y Combinator, observateurs de la transition agentique.

**Style** : Discours oral semi-improvisé qui circule entre anecdote pratique (MenuGen, openclaw, micro GPT, car wash 50m) et abstraction théorique (Software 1.0/2.0/3.0, verifiability, jagged intelligence, animals vs ghosts). Karpathy excelle à rendre accessible l'inévitable : il transforme une bascule technique abstraite en moment vécu ("I just started to notice that with the latest models the chunks just came out fine"), puis remonte au cadre conceptuel. Métaphores travaillées : agents comme *interns* avec recall mais sans taste, *spiky entities* à coordonner, neural net comme *host process* avec CPU en *co-processor*, *jagged frontier* (peaks vs failures coexistants). Aphorismes plantés pour circulation virale : *"never felt more behind as a programmer"*, *"raise the floor vs preserve the quality bar"*, *"animals vs ghosts"*, *"you can outsource your thinking but you can't outsource your understanding"*. Le ton oscille entre humilité (heart attack devant le code généré, side projects folder "extremely full") et autorité technique (verifiability comme cadre explicatif, RL circuits comme grille de lecture). Position épistémique : observateur lucide qui refuse l'optimisme aveugle (*jagged intelligence* irréductible aujourd'hui) et le pessimisme défaitiste (tout est in fine automatisable). C'est un discours **doctrinal pour l'ère agentique** : il fixe le vocabulaire (*vibe coding* → *agentic engineering*) et signe la transition.

## Pense-betes
- **Date estimée** : avril 2026, AI Startup School / conférence "AIN" (référence à Sam Altman venu "last year"). Vidéo YouTube : https://www.youtube.com/watch?v=96jN2OCOfLs
- **Phrase choc d'ouverture** : *"He's never felt more behind as a programmer."* — déclaration qui a fait le tour de X/Twitter et que l'interviewer reprend pour démarrer.
- **Point de bascule December 2025** : Karpathy était en break, plus de temps, et constate que *"the chunks just came out fine and then I kept asking for more and it just came out fine"*. Plus besoin de corriger. Il insiste : *"a lot of people experienced AI last year as ChatGPT-adjacent thing. But you really had to look again and you had to look as of December because things have changed fundamentally."*
- **Software 1.0 / 2.0 / 3.0** :
  - **1.0** : code explicite écrit par humain
  - **2.0** : programmation par création de datasets + entraînement de réseaux de neurones (poids appris)
  - **3.0** : programmation = prompting ; le contexte est le levier sur l'interpréteur LLM ; le LLM devient un *programmable computer*
- **Exemple openclaw (illustratif Software 3.0)** : au lieu d'un shell script qui ballonne pour gérer toutes les plateformes, l'installation est *"un copy-paste de texte que tu donnes à ton agent"*. L'agent regarde l'environnement, fait du debug en boucle, c'est plus puissant qu'un script précis.
- **MenuGen → Nanobanana (cas extrême)** : Karpathy a vibe-codé MenuGen (photo menu restaurant → OCR + image generation pour visualiser plats) sur Vercel. Puis il découvre qu'on peut juste donner la photo à Gemini et dire *"use Nanobanana to overlay the things onto the menu"* — Nanobanana renvoie l'image originale avec les plats overlaid en pixels. *"All of my menu gen is spurious. It's working in the old paradigm. That app shouldn't exist."* Le neural net fait tout, le prompt est l'image, l'output est l'image. **Pas d'app entre les deux.** Karpathy en tire : ne pas penser AI comme accélération du paradigme existant, mais comme **nouvelles choses possibles**.
- **Nouvelles possibilités** : LLM Knowledge Bases — *"you get LLMs to create wikis for your organization or for you in person"*. Ce n'est pas du code, c'est une recompilation/réordonnancement de documents pour créer une projection nouvelle. *"This is not something that could exist before."*
- **Extrapolation 2026 (équivalent du web 90s, mobile 2010s, SaaS cloud)** : Karpathy imagine des **neural computers** où le neural net devient le *host process* et les CPUs deviennent les *co-processors* — diffusion qui rend une UI unique pour le moment, à partir de raw video/audio en input. *"In the 50s and 60s it was not really obvious whether computers would look like calculators or computers would look like neural nets. Of course we went down the calculator path."* Cette branche pourrait s'inverser piece by piece.
- **Verifiability framework** : pourquoi les LLMs sont *jagged* ?
  - *"Traditional computers can easily automate what you can specify in code; LLMs can easily automate what you can verify."*
  - Les frontier labs entraînent en RL avec verification rewards → peak en math/code et adjacents, *rough around the edges* ailleurs.
  - Combinaison : **verifiable** + **labs care** (ce qui rentre dans le data mix par valeur économique).
  - Anecdote chess GPT-3.5 → GPT-4 : amélioration énorme due à beaucoup de données chess intentionnellement ajoutées au pre-training, **pas** à une progression générale.
  - Conséquence : tu es *"slightly at the mercy of whatever the labs are doing"*. Si tu es dans un circuit RL, tu *flies*. Sinon, fine-tuning maison nécessaire.
- **Exemple jaggedness moderne** : *"I want to go to a car wash to wash my car and it's 50 meters away. Should I drive or should I walk? State-of-the-art models today will tell you to walk because it's so close. How is it possible that state-of-the-art Opus 4.7 will simultaneously refactor a 100,000 line codebase or find zero day vulnerabilities and yet tells me to walk to this car wash? This is insane."*
- **Conseil aux fondateurs** : viser des domaines **verifiable** où on peut créer ses propres RL environments / examples → fine-tuning works as a lever. *"Verifiability remains true even if the labs are not focusing on it directly."* Karpathy refuse de divulguer un domaine spécifique sur scène : *"I don't want to vibe post on stage."*
- **Sur ce qui n'est PAS automatisable** : *"Ultimately almost everything can be made verifiable to some extent. Even for writing, you can imagine having a council of LLM judges."* Pour Karpathy : **tout est in fine automatisable**, c'est juste plus ou moins facile.
- **Vibe coding vs Agentic engineering (distinction clé)** :
  - **Vibe coding** = raise the floor. Tout le monde peut vibe-coder n'importe quoi. Démocratisation.
  - **Agentic engineering** = preserve the quality bar de la software professionnelle. *"You're not allowed to introduce vulnerabilities due to vibe coding. You're still responsible for your software just as before, but can you go faster?"*
  - C'est une **discipline d'ingénierie** : coordonner des agents spiky/stochastiques pour aller vite sans sacrifier la qualité.
  - **Le 10x engineer est magnifié** : *"10x is not the speed up you gain. People who are very good at this peak a lot more than 10x."*
- **Sur le hiring (point très actionnable)** : *"Most people have still not refactored their hiring process for agentic engineer capability. If you're giving out puzzles to solve, this is still the old paradigm. Hiring has to look like: give me a really big project and see someone implement that big project."* Exemple : *"Let's write a Twitter clone for agents, make it really good, make it really secure, then have some agents simulate activity, and I'm going to use 10 codecs 5.4x for X high to try to break your website. They should not be able to break it."* (Reformulation par Karpathy de **Sierra AI-native interview** — corroboration directe de Bret Taylor / Iyengar / Asemanfar / Wang.)
- **Compétences humaines qui prennent de la valeur** : *taste*, *aesthetics*, *judgment*, *oversight*, *spec design*. Les agents sont des *interns* — ils ont un excellent recall (les détails d'API PyTorch / NumPy / pandas qu'on n'a plus à mémoriser : keep_dims vs keep_dim, dim vs axis, reshape vs permute vs transpose), mais ils ratent les choses fondamentales. Anecdote MenuGen : l'agent a tenté de cross-correlate les fonds Stripe et Google par email address au lieu d'utiliser un user ID persistant — *"this is such a weird thing to do."*
- **Position de l'humain** : *"You're in charge of the taste, the engineering, the design, that it makes sense, that you're asking for the right things. The engineers are doing the fill in the blanks."* Karpathy n'aime pas trop le *plan mode* en lui-même mais croit à un travail de **spec détaillée** co-conçue avec l'agent.
- **Heart attack en lisant le code généré** : *"It's not super amazing code necessarily all the time and it's very bloaty and there's a lot of copy paste and there's awkward abstractions that are brittle and like it works but it's just really gross."* Sur micro GPT : il a essayé de faire simplifier par LLM, *"the models hate this. They can't do it. You feel like you're outside of the RL circuits. It's like pulling teeth."* — preuve que l'esthétique de simplicité n'est pas dans le RL des labs.
- **Animals vs Ghosts** : *"We're not building animals, we are summoning ghosts."* Les LLMs ne sont pas des intelligences animales (yelling at them ne change rien). Ce sont des *statistical simulation circuits* : substrat = pre-training (statistique), RL bolté par-dessus pour augmenter les *appendages*. Karpathy admet : *"I don't know that I have like here are the five obvious outcomes of how to make your system better. It's more just being suspicious of it and figuring out over time."*
- **Agent-native infrastructure** : *"Everything is still fundamentally written for humans and has to be moved around. I still use most of the time when I use different frameworks or libraries... they still have docs that are fundamentally written for humans. This is my favorite pet peeve. Why are people still telling me what to do? I don't want to do anything. What is the thing I should copy paste to my agent?"* Vision : décomposer les workloads en **sensors over the world / actuators over the world**. Test ultime : *"I would hope that I could give a prompt to an LLM 'build menu gen' and then I didn't have to touch anything and it's deployed."* Le déploiement Vercel/DNS/Stripe configurations était la vraie galère, pas le code.
- **Long terme** : *"I'll have my agent talk to your agent to figure out details of meetings."* Représentation par agent pour personnes et organisations.
- **Formule finale (sur l'éducation et la connaissance)** : *"You can outsource your thinking but you can't outsource your understanding."* Karpathy : *"I still have to somehow information still has to make it into my brain and I feel like I'm becoming a bottleneck of just even knowing what are we trying to build why is it worth doing how do I direct my agents."* Il défend les LLM Knowledge Bases comme outil d'**enhanced understanding**, par génération de données synthétiques sur un corpus fixe (ses articles → wiki personnel).
- **Articulation dossier veille** :
  - Confirme et popularise par sa voix le paradigme **Software 3.0** (cf. Greyling 2026-03-09 *"l'environnement de développement s'effondre"*, Rauch 2026-01-02 *"CLI as fundamental coding agent abstraction"*).
  - **Distinction vibe coding / agentic engineering** crystallise le débat porté depuis Kent Beck (2024-10), Mogère (2025-07), Yegge & Kim (2025-11), Beck *Starving Genies* (2026-04-03) — Karpathy fournit le **vocabulaire stable** pour l'opposition.
  - **Hiring refactoring** par grand projet adversariel = corroboration explicite de Sierra (Taylor 2026-04-20, Iyengar/Asemanfar/Wang 2026-04-22) et Soto (*Developer Taste* 2026-04).
  - **Verifiability** comme grille explicative de la *jagged frontier* étend Mollick (2025-11-12 *Giving your AI a Job Interview*) et donne un cadre opérationnel (créer ses propres RL environments).
  - **Animals vs ghosts** s'inscrit dans la lignée philosophique des fiches sur l'*ontological core* (Seale 2025-05-30) et la *malléabilité du monde* (Andreessen 2026-02 / refute Ralmuto 2026-03-17).
  - **Agent-native infrastructure** prolonge Cloudflare *Markdown for Agents* (2026-02-12), Levie *Building for Trillions of Agents* (2026-03-07), Sierra (2026-04).

## RésuméDe400mots

Andrej Karpathy — co-fondateur d'OpenAI, ex-architecte de l'Autopilot Tesla et créateur du terme *vibe coding* — déclare lors de cette interview qu'il **ne s'est jamais senti aussi en retard comme programmeur**. Le point de bascule : décembre 2025. Pendant un break, il observe que les *chunks* de code générés par les nouveaux modèles sortent justes du premier coup ; il cesse de corriger, fait confiance, vibe-code en continu. Sa conclusion : ceux qui ont expérimenté l'IA en 2024 comme un avatar de ChatGPT doivent **regarder à nouveau** — quelque chose a changé fondamentalement dans le workflow agentique cohérent.

Karpathy formalise sa taxonomie **Software 1.0 / 2.0 / 3.0** : code explicite, puis poids appris via datasets, puis **prompting comme programmation** d'un LLM-interpréteur. Deux exemples illustrent la rupture. **openclaw** : au lieu d'un shell script bloated qui couvre toutes les plateformes, l'installation est un texte à copier-coller dans l'agent qui débuggue en boucle. **MenuGen** : son app vibe-codée sur Vercel pour générer des images de plats devient obsolète quand il découvre qu'on peut donner la photo du menu directement à Gemini en demandant à Nanobanana d'overlayer les plats — pas d'app entre l'image input et l'image output. *"That app shouldn't exist."* Leçon : ne pas penser l'IA comme accélération du paradigme existant mais comme **possibilités neuves** (ex. LLM Knowledge Bases).

Sa théorie de la **verifiability** explique pourquoi les LLMs restent *jagged* : les labs entraînent en RL sur domaines verifiable (math, code), créant des pics de capacité et des creux ailleurs. Anecdote-marqueur : Opus 4.7 refactorise 100k lignes mais conseille de marcher 50m jusqu'au lavage de voiture. Conseil aux fondateurs : viser des domaines verifiable où l'on peut créer ses propres RL environments et fine-tuner.

Karpathy distingue **vibe coding** (raise the floor — démocratisation) et **agentic engineering** (preserve the quality bar — discipline ingénieur pour coordonner des agents *spiky/stochastiques*). Le 10x engineer est *magnifié bien au-delà de 10x*. Le hiring doit être refondé : finis les puzzles, place aux gros projets adversariels (Twitter clone agent vs agents red team).

Les agents sont des **interns** avec recall excellent mais sans *taste* — l'humain reste en charge de l'esthétique, du design, de la spec. Karpathy refuse la métaphore animale : on ne *construit pas des animaux, on convoque des fantômes* — circuits statistiques, pas vie. Il appelle à une **infrastructure agent-native** (sensors/actuators, docs pour agents, déploiement par prompt). Formule de clôture : ***"You can outsource your thinking but you can't outsource your understanding."*** L'humain reste le *bottleneck* de la compréhension qui dirige le système.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Andrej Karpathy | PERSONNE | a_co_fondé | OpenAI | ORGANISATION | 0.99 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | a_créé_terme | vibe coding | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | a_construit | Tesla Autopilot | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Andrej Karpathy | PERSONNE | affirme_que | "never felt more behind as a programmer" | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Décembre 2025 | EVENEMENT | marque_bascule | workflow agentique cohérent | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Software 3.0 | CONCEPT | redéfinit | programmation comme prompting | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| LLM | TECHNOLOGIE | est | programmable computer | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| MenuGen | TECHNOLOGIE | est_rendue_obsolète_par | Nanobanana | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Nanobanana | TECHNOLOGIE | fait_partie_de | Gemini | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Verifiability | CONCEPT | explique | jagged intelligence | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Frontier labs | ORGANISATION | entraînent_en | RL environments | METHODOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Opus 4.7 | TECHNOLOGIE | échoue_sur | car wash 50m question | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| Vibe coding | METHODOLOGIE | raise_the_floor_pour | software development | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Agentic engineering | METHODOLOGIE | préserve | quality bar professionnelle | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | recommande | refonte du hiring par gros projets adversariels | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Agents IA | TECHNOLOGIE | sont_comparés_à | interns avec recall | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | métaphorise | LLMs comme fantômes pas animaux | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Neural net | TECHNOLOGIE | pourrait_devenir | host process | CONCEPT | 0.88 | ATEMPOREL | inféré |
| LLM Knowledge Bases | TECHNOLOGIE | enrichit | understanding humain | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Andrej Karpathy | PERSONNE | affirme_que | "outsource thinking but not understanding" | CONCEPT | 0.99 | ATEMPOREL | déclaré_article |
| Sam Altman | PERSONNE | a_parlé_à | AI Startup School | EVENEMENT | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Andrej Karpathy | PERSONNE | rôle | Co-fondateur OpenAI, ex-Tesla Autopilot, créateur du terme vibe coding | AJOUT |
| Software 3.0 | CONCEPT | définition | Programmation = prompting d'un LLM-interpréteur, contexte = levier | AJOUT |
| Vibe coding | METHODOLOGIE | fonction | Raise the floor — démocratisation du software development | MISE_A_JOUR |
| Agentic engineering | METHODOLOGIE | fonction | Préserver le quality bar avec coordination d'agents stochastiques | AJOUT |
| Verifiability | CONCEPT | définition | Cadre expliquant pourquoi LLMs peakent en math/code (RL training) et stagnent ailleurs | AJOUT |
| Jagged intelligence | CONCEPT | exemple | Opus 4.7 refactorise 100k lignes mais conseille de marcher 50m au car wash | AJOUT |
| MenuGen | TECHNOLOGIE | catégorie | App vibe-codée par Karpathy (photo menu → images plats), rendue obsolète par Nanobanana | AJOUT |
| Nanobanana | TECHNOLOGIE | catégorie | Modèle d'image generation Google/Gemini capable d'overlay menu items dans pixels | AJOUT |
| Animals vs Ghosts | CONCEPT | définition | Métaphore Karpathy : LLMs sont des circuits de simulation statistique, pas des intelligences animales | AJOUT |
| Outsource thinking but not understanding | CONCEPT | source | Aphorisme cité par Karpathy comme phrase clé pour l'éducation à l'ère IA | AJOUT |
| Hiring refactoring par projets adversariels | METHODOLOGIE | exemple | Twitter clone agent vs 10 codecs red team — corroboration Sierra | AJOUT |
| LLM Knowledge Bases | TECHNOLOGIE | catégorie | Outil personnel Karpathy : wiki auto-construit à partir d'articles lus | AJOUT |
| Opus 4.7 | TECHNOLOGIE | capabilité | Refactor 100k lignes, find zero days — mais jagged sur questions simples | AJOUT |
| AI Startup School | EVENEMENT | catégorie | Conférence où Sam Altman et Karpathy ont parlé (référence "AIN") | AJOUT |
| December 2025 transition | EVENEMENT | description | Bascule observée par Karpathy : workflow agentique cohérent qui fonctionne enfin | AJOUT |
