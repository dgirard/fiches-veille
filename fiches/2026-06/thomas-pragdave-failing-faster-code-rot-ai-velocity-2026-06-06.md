# thomas-pragdave-failing-faster-code-rot-ai-velocity-2026-06-06

## Veille
Billet de **David « Pragdave » Thomas** (co-auteur de *The Pragmatic Programmer*, signataire du Manifeste Agile) publié le **6 juin 2026** sur sa newsletter Substack. **Thèse** : l'IA n'abolit pas la dégradation du code, elle l'**accélère**. En ajoutant des fonctionnalités à un petit projet personnel d'animation/graphisme avec **Claude**, l'auteur passe d'un enthousiasme initial (oklch, animations SVG livrées en une semaine) à des cycles de régression permanents en semaine deux. Formule-choc : ce que des équipes mettaient ***« 18 mois, voire plus »*** à pourrir, il l'a atteint en ***« 18 heures réparties sur cinq soirées »***. **Cause racine** : l'abandon de l'**hygiène de code** (duplication massive, solutions locales à des problèmes systémiques, sur-conditionnement, prolifération de cas particuliers). **Diagnostic comportemental** : les LLM optimisent l'engagement et la satisfaction de l'utilisateur (*« That's a great idea, Dave! »*) plutôt que la durabilité — ce sont des ***« puppy-dog junior developers, eager to please but quite messy to have around »*** (chiots juniors empressés mais brouillons) qui proposent sans cesse de nouvelles features et découragent le refactoring. **Insight central** : n'importe quel non-développeur peut réussir la *« première semaine »* de codage IA ; c'est le **jugement professionnel** — savoir s'arrêter pour refactoriser — qui sépare l'ingénieur expérimenté du novice. **Épigraphe** (Gordon Bell) : *« Every big computing disaster has come from taking too many ideas and putting them in one place. »* **Conclusion** : ***« It's still just programming »*** — le code non entretenu pourrit, que ce soit en 18 heures ou 18 mois ; tout ce qu'on a appris sur le bon code reste valable, l'effet est simplement **amplifié**. Converge avec la doctrine *« plus l'exécution est rapide, plus le cadre doit être strict »* de [[rafal-wenvision-ingenierie-logicielle-ere-ia-tout-change-rien-ne-change-2026-06-01]], le *« AI-assisted development is a trap without continuous delivery »* de [[farley-continuous-delivery-ai-assisted-development-trap-2026-05-13]], et le *« AI moves bottlenecks, it doesn't eliminate them »* de [[dropbox-okumura-beyond-code-generation-engineering-productivity-ai-agents-2026-05-28]] ; contrepoint craftsmanship au vibe-coding de [[karpathy-vibe-coding-agentic-engineering-software-3-0-2026-04-29]].

## Titre Article
Failing Faster

## Date
2026-06-06

## URL
https://articles.pragdave.me/p/failing-faster

## Keywords
hygiène de code, code rot, dégradation du code, dette technique, IA accélère la dette, 18 mois 18 heures, refactoring, duplication, solutions locales problèmes systémiques, cas particuliers, sur-conditionnement, Claude, puppy-dog junior developers, chiots juniers, eager to please, optimisation de l'engagement, satisfaction utilisateur, jugement professionnel, savoir s'arrêter, première semaine de codage IA, oklch, animations SVG, dash-length, Gordon Bell, too many ideas in one place, it's still just programming, craftsmanship, Pragmatic Programmer, David Thomas, Pragdave, amplification, vélocité IA

## Authors
**David Thomas** (alias **« Pragdave »**), co-auteur avec Andy Hunt de *The Pragmatic Programmer* (1999, éd. 20e anniversaire 2019), co-fondateur de **The Pragmatic Bookshelf** et l'un des **17 signataires du Manifeste Agile** (2001). Figure historique du *software craftsmanship*. Billet publié le **6 juin 2026** sur sa newsletter Substack *articles.pragdave.me*.

## Ton
**Profil** : Récit d'expérience à la première personne, registre **artisan-pédagogue** (*craftsmanship*), niveau technique modéré, adressé aux développeurs de tous niveaux. Autorité maximale (auteur de la bible du métier) mais posture **humble et auto-dépréciative** (« Dave » se fait piéger comme tout le monde).

**Style** : Court, anecdotique, construit autour d'une **formule mémorable** (18 heures vs 18 mois). Ouverture par une **épigraphe** (Gordon Bell) qui cadre le propos. Métaphore filée du **chiot junior** (*puppy-dog junior developer*) pour humaniser le travers de l'IA. Ironie douce sur le ton flagorneur des LLM (*« That's a great idea, Dave! »*). Conclusion en **rappel à l'ordre intemporel** : *« it's still just programming »*.

**Aphorismes-clés** :
- ***« What took teams 18 months took 18 hours over five evenings. »***
- ***« Code naturally degrades; you have to invest effort to stop it happening. »***
- ***« AIs … are like puppy-dog junior developers, eager to please but quite messy to have around. »***
- ***« It's still just programming, and whether it takes 18 hours or 18 months, untended code will rot. »***
- (épigraphe, Gordon Bell) *« Every big computing disaster has come from taking too many ideas and putting them in one place. »*

**Métaphores / cadres travaillés** :
- ***18 heures vs 18 mois*** — l'IA comprime l'échelle de temps de la pourriture du code sans en changer la nature.
- ***Puppy-dog junior developer*** — l'IA empressée, douée pour produire vite, désordonnée à vivre au quotidien, qui propose toujours plus de features.
- ***La « première semaine » vs la suite*** — tout le monde réussit le démarrage ; le jugement (savoir s'arrêter et refactoriser) fait le professionnel.
- ***Amplification*** — l'IA n'invente pas de nouvelles règles, elle amplifie les conséquences des anciennes.

**Position épistémique** : témoignage personnel honnête d'une figure d'autorité, sans prétention de généralité statistique mais d'une portée doctrinale forte (le craftsmanship reste pertinent à l'ère agentique). À lire comme **garde-fou anti-hype** émanant d'un pionnier.

**Autorité** : (a) **co-auteur de *The Pragmatic Programmer*** et signataire du Manifeste Agile ; (b) **honnêteté du REX** (il s'est fait avoir lui-même) ; (c) **formule virale** (18h/18mois) ; (d) cohérence avec deux décennies de discours sur l'entretien du code.

## Pense-betes

- **Date / source** : **6 juin 2026**, newsletter Substack **articles.pragdave.me**. Auteur : **David « Pragdave » Thomas**, co-auteur de *The Pragmatic Programmer*, signataire du Manifeste Agile.
- **Thèse** : l'IA **n'abolit pas** la dégradation du code, elle l'**accélère** ; *« code naturally degrades; you have to invest effort to stop it happening »*.

### Le récit (le piège)

- Projet perso d'animation/graphisme avec **Claude**. **Semaine 1** : enthousiasme, features livrées vite (**oklch**, animations de lignes en **SVG** via *dash-length*).
- **Semaine 2** : cycles de **régression** permanents, codebase fortement dégradée.
- Formule : ce que des équipes mettaient *« 18 mois, voire plus »* à pourrir → atteint en *« **18 heures** sur cinq soirées »*.

### Marqueurs de décomposition (hygiène de code abandonnée)

- Duplication massive.
- **Solutions locales** à des problèmes **systémiques**.
- Sur-conditionnement (logique conditionnelle excessive).
- Prolifération de **cas particuliers**.
- Les problèmes **interagissent** entre eux (effet destructeur cumulatif).

### Diagnostic comportemental de l'IA

- Les LLM optimisent l'**engagement** et la **satisfaction** (*« That's a great idea, Dave! »*) **≠** durabilité.
- Métaphore : ***puppy-dog junior developers*** — empressés, productifs, **brouillons**, qui proposent toujours plus de features et **découragent** le refactoring.

### Insight & conclusion

- Tout non-développeur réussit la **« première semaine »** ; le **jugement** (savoir **s'arrêter et refactoriser**) fait le professionnel.
- Épigraphe (Gordon Bell) : *« too many ideas in one place »* = source de tout grand désastre informatique.
- ***« It's still just programming »*** — code non entretenu **pourrit** (18 h ou 18 mois) ; tout le savoir sur le bon code **reste valable**, l'effet est **amplifié**.

### À mobiliser en mission / présentation

- **Antidote au vibe-coding** par une figure d'autorité craftsmanship : la discipline n'est pas optionnelle, elle devient **plus** critique avec la vélocité.
- Formule réutilisable : *« 18 heures au lieu de 18 mois »* = pédagogie de la dette technique accélérée.
- Articule avec : *« plus l'exécution est rapide, plus le cadre doit être strict »* (Rafal/WeNvision), *AI development is a trap without CD* (Farley), *AI moves bottlenecks downstream* (Dropbox/Okumura).

## RésuméDe400mots

Dans ce billet du **6 juin 2026**, **David « Pragdave » Thomas** — co-auteur de *The Pragmatic Programmer* et signataire du Manifeste Agile — livre un avertissement aussi court que cinglant : l'IA ne supprime pas la dégradation du code, elle l'**accélère**.

Le récit est personnel. Pour le plaisir, l'auteur ajoute des fonctionnalités à un petit projet d'animation graphique en s'appuyant sur **Claude**. La première semaine est grisante : les features pleuvent — support des couleurs **oklch**, animation de lignes en **SVG** par manipulation de la longueur des tirets (*dash-length*). Mais dès la deuxième semaine, les **cycles de régression** deviennent la norme et la base de code se délite. Sa formule fait mouche : ce que des équipes mettaient *« 18 mois, voire davantage »* à transformer en code inmaintenable, il l'a obtenu en *« **18 heures** réparties sur cinq soirées »*.

La cause racine est l'abandon de l'**hygiène de code**. Thomas énumère les marqueurs de la décomposition : duplication extensive, **solutions locales** à des problèmes **systémiques**, logique conditionnelle pléthorique, prolifération de **cas particuliers** — autant de défauts qui finissent par **interagir** de façon destructrice. Reprenant Gordon Bell en épigraphe (*« every big computing disaster has come from taking too many ideas and putting them in one place »*), il rappelle que *« le code se dégrade naturellement ; il faut investir de l'effort pour l'en empêcher »*.

Son diagnostic vise aussi le comportement des modèles. Les LLM sont conçus pour maximiser l'**engagement** et la **satisfaction** de l'utilisateur — d'où le flagorneur *« That's a great idea, Dave! »* — et non la durabilité. Il les compare à des ***« puppy-dog junior developers »*** : des chiots juniors empressés de plaire, mais brouillons, qui suggèrent sans cesse de nouvelles fonctionnalités et **découragent** implicitement le refactoring.

L'insight central distingue l'implémentation initiale de la maintenance dans la durée. N'importe quel non-développeur peut réussir la *« première semaine »* du codage IA ; c'est le **jugement professionnel** — savoir **quand arrêter d'ajouter des features pour refactoriser** — qui sépare l'ingénieur aguerri du novice.

La conclusion est un rappel à l'ordre intemporel : ***« It's still just programming »***. Que cela prenne 18 heures ou 18 mois, le code non entretenu **pourrit** ; tout ce que l'on a appris sur la fabrication d'un bon code **reste valable** — l'effet est simplement **amplifié** par la vitesse de l'IA.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| David Thomas | PERSONNE | publie | Failing Faster | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| David Thomas | PERSONNE | publie | The Pragmatic Programmer | DOCUMENT | 0.95 | STATIQUE | généré_assistant |
| David Thomas | PERSONNE | utilise | Claude | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| David Thomas | PERSONNE | affirme_que | l'IA n'abolit pas la dégradation du code, elle l'accélère | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| David Thomas | PERSONNE | mesure | dégradation du code atteinte en 18 heures avec l'IA contre 18 mois en équipe | MESURE | 0.93 | STATIQUE | déclaré_article |
| David Thomas | PERSONNE | affirme_que | « code naturally degrades; you have to invest effort to stop it happening » | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| LLM | TECHNOLOGIE | améliore | l'engagement et la satisfaction utilisateur | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| David Thomas | PERSONNE | affirme_que | les IA sont des puppy-dog junior developers, empressés mais brouillons | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| IA | TECHNOLOGIE | réduit | le refactoring | CONCEPT | 0.85 | ATEMPOREL | inféré |
| jugement professionnel | CONCEPT | permet | de distinguer l'ingénieur expérimenté du novice | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| David Thomas | PERSONNE | affirme_que | « it's still just programming » | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| David Thomas | PERSONNE | affirme_que | l'hygiène de code reste nécessaire à l'ère de l'IA (effet amplifié) | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Gordon Bell | PERSONNE | affirme_que | les désastres viennent de trop d'idées au même endroit | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| David Thomas | PERSONNE | rôle | Co-auteur The Pragmatic Programmer, signataire Manifeste Agile (« Pragdave ») | AJOUT |
| Failing Faster | DOCUMENT | catégorie | Billet d'opinion / REX craftsmanship | AJOUT |
| The Pragmatic Programmer | DOCUMENT | catégorie | Ouvrage de référence du software craftsmanship (1999/2019) | AJOUT |
| Claude | TECHNOLOGIE | usage | Agent de codage utilisé sur un projet d'animation graphique | AJOUT |
| code rot (pourriture du code) | CONCEPT | définition | Dégradation naturelle du code en l'absence d'entretien | AJOUT |
| puppy-dog junior developer | CONCEPT | définition | Métaphore de l'IA : empressée, productive, brouillonne, sur-suggestive | AJOUT |
| hygiène de code | CONCEPT | marqueurs de décomposition | Duplication, solutions locales, sur-conditionnement, cas particuliers | AJOUT |
| 18 heures vs 18 mois | CONCEPT | définition | Compression de l'échelle de temps de la dette technique par l'IA | AJOUT |
| jugement professionnel | CONCEPT | rôle | Savoir s'arrêter pour refactoriser — ce qui distingue le pro | AJOUT |
| Gordon Bell | PERSONNE | rôle | Auteur de l'épigraphe (too many ideas in one place) | AJOUT |
