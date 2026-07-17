---
themes: [agents-codage-ia-skills, transformation-adoption, philosophie-societe]
source: "Eric S. Raymond (X)"
---
# raymond-llm-coding-empowering-2026-07-08

## Veille

Post X d'**Eric S. Raymond** (ESR, auteur de *The Cathedral and the Bazaar*, co-fondateur de l'Open Source Initiative, ~50 ans de code) — **contre-témoignage frontal au discours « les LLMs génèrent du code pourri et hallucinent, inutiles pour programmer »**. Sa thèse : cela **ne lui arrive quasiment jamais**, et **plus du tout depuis les deux dernières générations** de modèles qu'il utilise (« chat GPT 5.4 et 5.5 » sous **codex**). L'ancien symptôme — un modèle qui « déraille » en approchant sa limite de contexte — a disparu : codex affiche désormais un **avertissement rouge** invitant à **vider la session** au lieu de partir en vrille. **Empan d'usage** : IA appliquée à des **feature changes, refactoring et debugging sur 63 projets** en **C, Go, Rust, Python et shell** ; rédaction de documentation ; **décompilation d'un binaire DOS en source lisible**. **Routine de travail** installée : quand il rouvre un projet, il lance d'abord les **tests de régression**, puis démarre codex et lui demande d'**auditer le code** (bugs + suggestions d'amélioration). Verdict : les LLMs sont **« excellents et formidablement capacitants »** ; leur **pire limite** est une **« vision en tunnel architecturale »** — excellents pour générer du code à la spécification, mais parfois **aveugles aux patterns de plus haut niveau** — ce qu'il assume comme le **job de son « meatbrain »**. Le point le plus fort, contre-intuitif : les LLMs **ne se trompent PAS sur les détails et les cas limites** ; il se dit **moins bon qu'eux** sur ce plan (malgré 50 ans d'XP) car si un changement doit **toucher cinq endroits**, le modèle **les retrouve les cinq de façon fiable**, là où l'humain en corrige quatre et **débogue des heures** avant de trouver le cinquième oublié. Il interroge alors les **« downshouters »** : vivent-ils dans un **autre univers** ? Utilisent-ils de **vieux modèles faibles** ? Y a-t-il un **skill issue** qu'il ne voit pas parce que ses **habitudes mentales et sa communication** collent bien aux « poignées » de ces outils ? Enjeu qu'il juge important à trancher, car « des **milliards de dollars seraient gaspillés en token spend mal dirigé** ». Sa recette, « très simple » : **« Be clear in your thinking, tell the model what you want with precision, and good things happen »** — chute : « what am I missing here? ». À lire comme **contrepoint pro-LLM d'une figure historique de l'open source** au débat récurrent sur la (dé)valeur des agents de codage — écho au « skill issue » et à la discipline de spécification (cf. [[martignole-token-manifesto-2026-07-17]]).

## Titre Article

What...what am I missing here? (post X sur les LLMs et le codage)

## Date

2026-07-08

## URL

https://x.com/esrtweet/status/2074889702381953222

## Keywords

Eric S. Raymond, ESR, esrtweet, The Cathedral and the Bazaar, Open Source Initiative, OSI, open source, Fetchmail, The Art of Unix Programming, Jargon File, LLM, agents de codage, codex, OpenAI Codex, ChatGPT 5.4, ChatGPT 5.5, hallucination, code pourri, crap code, skill issue, downshouters, refactoring, debugging, feature changes, tests de régression, audit de code, décompilation, binaire DOS, C, Go, Rust, Python, shell, vision en tunnel architecturale, architectural tunnel vision, patterns de haut niveau, détails et cas limites, edge cases, meatbrain, limite de contexte, context limit, clear session, token spend, milliards gaspillés, spécification, précision, empowerment, capacitant, contre-témoignage, adoption IA, développeur expérimenté

## Authors

Eric S. Raymond (ESR, @esrtweet sur X) — développeur, hacker et essayiste américain, **figure historique du mouvement open source**. Né le 4 décembre 1957 à Boston (Massachusetts) ; paralysie cérébrale de naissance, enfance en partie au Venezuela puis en Pennsylvanie. Auteur de l'essai très influent **« The Cathedral and the Bazaar »** (1997, livre 1999), qui oppose le modèle « cathédrale » (développement centralisé et fermé) au modèle « bazar » (décentralisé et ouvert, à la Linux) ; il a **popularisé le terme « open source »** (contre « free software ») et contribué à convaincre **Netscape** d'ouvrir son code (naissance de Mozilla). **Co-fondateur de l'Open Source Initiative (OSI)** en 1998, président jusqu'en 2005. A édité le **Jargon File** (*The New Hacker's Dictionary*), maintenu des projets comme **Fetchmail**, écrit **« The Art of Unix Programming »** (2003). Se revendique **libertarien**, défenseur du port d'armes, ceinture noire de taekwondo ; commente régulièrement tech, politique et open source sur X. Se présente ici comme codeur « très, très bon » avec **~50 ans d'expérience**. (Post X personnel ; date de publication : 2026-07-08 ; date d'ajout à la veille : 2026-07-17.)

## Ton

**Profil** : témoignage personnel argumentatif en registre **franc et un brin polémique**, posté sur X par un praticien vétéran. Pas de reporting ni de démonstration chiffrée : une **expérience vécue** opposée à un **discours dominant** (les « downshouters » qui dénigrent les LLMs), avec une **question sincère** — « qu'est-ce que je rate ? ».

**Style** : direct, familier (« bitching », « meatbrain », « downshouters »), assumant sa propre compétence sans fausse modestie (« I'm a very, very good coder… but the LLMs are better than me »). Rhétorique de l'**étonnement** (« increasingly puzzling », « are they living in a different universe? ») plus que de l'accusation : ESR ne conclut pas au « skill issue » de ses contradicteurs, il **l'hypothèse** parmi d'autres (vieux modèles, univers différent) et retourne l'interrogation contre lui-même. Formules mémorielles et **recette minimaliste** en clôture (« Be clear in your thinking, tell the model what you want with precision »). Le fond est **résolument pro-LLM**, mais nuancé par l'aveu d'une **limite réelle** (la « vision en tunnel architecturale »), ce qui donne au propos sa crédibilité.

## Pense-betes

- **La contre-intuition centrale : les LLMs excellent là où l'humain faillit — les détails et les cas limites.** Argument le plus fort d'ESR, à retenir tel quel : si un changement doit **toucher cinq endroits** du code, le modèle **les retrouve les cinq de façon fiable**, là où l'humain « en corrige quatre puis débogue des heures avant de découvrir le cinquième ». Inversion du cliché « l'IA hallucine les détails » : pour lui, c'est l'IA qui **fait la couverture exhaustive**, l'humain qui oublie.
- **La vraie limite, honnête : la « vision en tunnel architecturale ».** Les LLMs sont excellents pour **coder à la spécification** mais **parfois aveugles aux patterns de plus haut niveau** → la conception d'architecture reste le **« job du meatbrain »**. Répartition claire du travail : **humain = altitude/architecture ; modèle = exécution exhaustive/edge cases.** (Nuance qui rend le témoignage crédible plutôt que béat.)
- **« Ça n'arrive quasiment jamais » — et plus du tout depuis 2 générations.** Le « code pourri / hallucinations » qu'il ne constate pas, surtout sous **codex** avec « ChatGPT 5.4 et 5.5 ». Le dérapage à l'approche de la **limite de contexte** a été **remplacé par un garde-fou produit** : avertissement rouge + invitation à **vider la session** au lieu de laisser le modèle « dérailler ». (Le tooling qui discipline le contexte fait partie de l'explication.)
- **Empan d'usage réel (pas un jouet).** 63 projets, 5 langages (**C, Go, Rust, Python, shell**), sur **feature changes, refactoring, debugging** ; **documentation** ; **décompilation d'un binaire DOS** en source lisible. Signal : usage **large et exigeant** par un expert, pas de la démo.
- **La routine reproductible.** À chaque réouverture de projet : **(1)** lancer les **tests de régression**, **(2)** démarrer codex et lui demander d'**auditer** le code (bugs + améliorations). Pattern actionnable « harnais de tests d'abord, audit LLM ensuite ».
- **L'hypothèse « skill issue » — posée, pas assénée.** ESR retourne la question : les détracteurs utilisent-ils de **vieux modèles faibles** ? Vivent-ils dans un **autre univers** ? Ou ont-ils un **skill issue** qu'il ne perçoit pas car ses **habitudes mentales et sa communication** épousent bien les « poignées » de l'outil ? Il **inclut sa propre subjectivité** dans les variables. Recette proposée : **clarté de pensée + précision de la demande** (à rapprocher de la discipline de spécification du Token Manifesto, [[martignole-token-manifesto-2026-07-17]]).
- **L'enjeu chiffré (revendiqué) : « des milliards gaspillés en token spend mal dirigé ».** ESR relie le débat compétence/valeur des LLMs à un **gâchis économique** — d'où l'importance, selon lui, de comprendre pourquoi certains échouent là où lui réussit. Angle veille : la variance d'usage (et non l'outil) comme facteur de ROI.
- **Usage veille** : pièce d'**opinion / témoignage**, pas de mesure — à traiter comme telle (échantillon d'un seul praticien très expérimenté, biais de sélection assumé). Sa valeur : un **contrepoint pro-LLM crédible** signé d'une **figure de l'open source**, utile pour équilibrer le corpus face aux critiques (« crap code », désillusion) et pour la thèse « la valeur dépend de la clarté de la spécification et de la maturité du tooling, pas du modèle seul ».

## RésuméDe400mots

**Eric S. Raymond** (ESR) — auteur de *The Cathedral and the Bazaar*, co-fondateur de l'Open Source Initiative, ~50 ans de code — publie sur X un **contre-témoignage** au discours « les LLMs génèrent du code pourri, hallucinent, sont inutiles pour programmer ». Un discours qu'il trouve **« de plus en plus déroutant »**, car cela ne lui arrive **quasiment jamais**.

**L'expérience.** Depuis **deux générations de modèles** (« ChatGPT 5.4 et 5.5 » sous **codex**), il ne constate plus de dérapage. L'ancien symptôme — un modèle qui « déraille » près de sa **limite de contexte** — a laissé place à un **avertissement rouge** invitant à **vider la session**. Son empan est large : IA appliquée à des **feature changes, refactoring et debugging sur 63 projets** en **C, Go, Rust, Python et shell**, rédaction de **documentation**, et même **décompilation d'un binaire DOS** en source lisible. Sa **routine** : à chaque réouverture d'un projet, lancer les **tests de régression**, puis demander à codex d'**auditer** le code (bugs + améliorations).

**Le verdict.** Les LLMs sont **« excellents et formidablement capacitants »**. Leur **pire limite** est une **« vision en tunnel architecturale »** : excellents pour coder **à la spécification**, mais parfois **aveugles aux patterns de haut niveau** — ce qui reste, dit-il, le **job de son « meatbrain »**. Le point le plus fort, contre-intuitif : les LLMs **ne se trompent pas sur les détails et les cas limites**. Il s'y déclare **moins bon qu'eux** : si un changement doit **toucher cinq endroits** du code, le modèle **les trouve tous les cinq**, là où l'humain en corrige quatre et **débogue des heures** avant de repérer le cinquième.

**L'interrogation.** ESR questionne les **« downshouters »** : vivent-ils dans un **autre univers** ? Utilisent-ils de **vieux modèles faibles** ? Ont-ils un **skill issue** qu'il ne perçoit pas, parce que ses **habitudes mentales et sa communication** collent bien aux « poignées » de ces outils ? Il juge la question **importante** car « des **milliards de dollars** seraient gaspillés en **token spend mal dirigé** ». Sa recette, « très simple » : **« Be clear in your thinking, tell the model what you want with precision, and good things happen »** — avant la chute : « what…what am I missing here? ».

À lire comme un **contrepoint pro-LLM crédible**, signé d'une figure historique de l'open source, au débat récurrent sur la valeur des agents de codage — en résonance avec la discipline de spécification défendue ailleurs (cf. Token Manifesto).

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Eric S. Raymond | PERSONNE | a_créé | The Cathedral and the Bazaar | DOCUMENT | 0.98 | STATIQUE | généré_assistant |
| Eric S. Raymond | PERSONNE | a_créé | Open Source Initiative | ORGANISATION | 0.9 | STATIQUE | généré_assistant |
| Eric S. Raymond | PERSONNE | utilise | Codex | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Eric S. Raymond | PERSONNE | affirme_que | les LLMs sont d'excellents outils, formidablement capacitants pour la programmation | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Eric S. Raymond | PERSONNE | affirme_que | le code pourri et les hallucinations ne lui arrivent quasiment jamais, et plus du tout depuis les deux dernières générations de modèles | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Eric S. Raymond | PERSONNE | affirme_que | les LLMs ne se trompent pas sur les détails et les cas limites : ils retrouvent de façon fiable les cinq endroits à modifier là où l'humain en oublie un | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Eric S. Raymond | PERSONNE | affirme_que | la pire limite des LLMs est une vision en tunnel architecturale : bons à coder à la spécification, parfois aveugles aux patterns de haut niveau | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Eric S. Raymond | PERSONNE | recommande | être clair dans sa pensée et dire au modèle ce qu'on veut avec précision | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Eric S. Raymond | PERSONNE | utilise | tests de régression | METHODOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Codex | TECHNOLOGIE | permet | auditer le code d'un projet pour détecter des bugs et suggérer des améliorations | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Codex | TECHNOLOGIE | résout | le dérapage du modèle à l'approche de la limite de contexte (avertissement + vidage de session) | AFFIRMATION | 0.75 | DYNAMIQUE | déclaré_article |
| Eric S. Raymond | PERSONNE | affirme_que | des milliards de dollars sont gaspillés en token spend mal dirigé | AFFIRMATION | 0.7 | DYNAMIQUE | déclaré_article |
| clarté de la spécification | CONCEPT | améliore | la qualité du code produit par les LLMs | AFFIRMATION | 0.75 | ATEMPOREL | inféré |
| skill issue | CONCEPT | observé_dans | l'écart entre praticiens satisfaits et détracteurs des LLMs de codage | AFFIRMATION | 0.7 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Eric S. Raymond | PERSONNE | rôle | Développeur et essayiste, figure historique de l'open source (auteur de *The Cathedral and the Bazaar*, co-fondateur de l'OSI, Fetchmail, *The Art of Unix Programming*) ; ~50 ans d'expérience ; témoin pro-LLM du débat sur les agents de codage | AJOUT |
| The Cathedral and the Bazaar | DOCUMENT | rôle | Essai fondateur (1997/1999) d'ESR opposant développement « cathédrale » (centralisé/fermé) et « bazar » (décentralisé/ouvert) ; a popularisé le terme « open source » | AJOUT |
| Open Source Initiative | ORGANISATION | rôle | Organisation co-fondée par ESR en 1998 (président jusqu'en 2005) promouvant l'open source | AJOUT |
| Codex | TECHNOLOGIE | catégorie | Agent de codage (OpenAI) utilisé par ESR avec « ChatGPT 5.4/5.5 » ; audit de code, garde-fou de limite de contexte (avertissement rouge + vidage de session) | AJOUT |
| vision en tunnel architecturale | CONCEPT | définition | Pire limite des LLMs selon ESR : excellents pour générer du code à la spécification mais parfois aveugles aux patterns de plus haut niveau — l'architecture reste le « job du meatbrain » humain | AJOUT |
| skill issue | CONCEPT | débat | Hypothèse posée (non assénée) par ESR pour expliquer l'écart entre son expérience très positive des LLMs et le discours des « downshouters » : vieux modèles, univers différent, ou compétence de communication/spécification | AJOUT |
| token spend mal dirigé | CONCEPT | enjeu | ESR relie la mauvaise utilisation des LLMs à des « milliards de dollars gaspillés » — la variance d'usage (clarté/précision) comme facteur de ROI, pas l'outil seul | AJOUT |
