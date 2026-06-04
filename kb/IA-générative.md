# IA générative

> **Type** : TECHNOLOGIE | 17 relations | 4 fiches sources

## Attributs

- **catégorie** : Technologie IA de génération de contenu
- **impact** : Découplage effort/compréhension dans l'open source
- **impact productivité** : +55% pour les développeurs
- **rôle** : multiplicateur de force pour l'ingénieur

## Relations (comme sujet)

### augmente

- [[kb/_entites-mineures#productivité-développeurs\|productivité développeurs]] (CONCEPT) — 0.95, DYNAMIQUE
  - [[fiches/2025-11/greyling-software-cost-collapse-permissionless-2025-11-04\|Effondrement coût et complexité logiciel, IA démocratise développement, logiciel devient "permissionless", dette technique sociétale, productivité développeurs +55% - Cobus Greyling - Medium]]

### découple

- [[kb/_entites-mineures#effort-et-compréhension\|effort et compréhension]] (CONCEPT) — 0.97, DYNAMIQUE
  - [[fiches/2026-02/ensarguet-signal-noise-contribution-ai-slop-open-source-2026-02-04\|Repenser la contribution open source face au "AI slop" - Signal vs bruit]]

### démocratise

- [[kb/_entites-mineures#création-logicielle\|création logicielle]] (CONCEPT) — 0.94, DYNAMIQUE
  - [[fiches/2025-11/greyling-software-cost-collapse-permissionless-2025-11-04\|Effondrement coût et complexité logiciel, IA démocratise développement, logiciel devient "permissionless", dette technique sociétale, productivité développeurs +55% - Cobus Greyling - Medium]]

### déplace

- [[kb/_entites-mineures#goulots-d'étranglement-en-aval\|goulots d'étranglement en aval]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2026-05/dropbox-okumura-beyond-code-generation-engineering-productivity-ai-agents-2026-05-28\|Billet du **Dropbox Tech blog** (rubrique *culture*), publié le **28 mai 2026** par **Kazuaki Okumura** (Dropbox, rôle non précisé dans l'article), reprenant une intervention à la conférence **DX Annual 2026** (productivité développeur). **Thèse-pivot** : la productivité d'ingénierie doit dépasser la *génération de code*. *« Accelerating code generation simply shifted some bottlenecks downstream »* — l'IA a massivement augmenté le débit de code, mais *« the faster code moves, the more pressure it puts on review queues, CI systems, validation workflows, release coordination, and production operations »*. Le vrai enjeu n'est plus d'écrire du code plus vite, mais de permettre à tout le SDLC d'**absorber, valider et livrer en sécurité** un volume bien plus grand. **De copilote à agent** : la première vague (explication de code, snippets, Q&A) opérait *« as copilots alongside the engineer »* ; l'agent, lui, *« can take a scoped task, inspect the codebase, edit files, run tests, iterate on failures, and return an artifact for human review »* — l'ingénieur restant *« accountable for intent, architecture, quality, and release decisions »* (plus de travail parallèle, plus d'options, délestage de l'exécution répétitive). **Nova** = plateforme d'agents de codage **interne** de Dropbox : décrire une tâche en langage naturel, exécution en environnement contrôlé avec le contexte du codebase. Datapoint canonique : ***« Nova's value comes less from the model itself than the systems surrounding it »*** (codebase context, internal practices, safe execution, workflow integration, human review) ; Nova représente **~1 PR sur 12 chez Dropbox** aujourd'hui (adoption en croissance), et s'étend au-delà des features : **migrations, remédiation de tests flaky, investigation de bugs, mises à jour de dépendances** (travail à forte pénibilité). **Mesurer la vélocité produit, pas l'output de code** : le *PR throughput*, signal utile quand la vélocité de codage était la contrainte, *« was no longer sufficient »*. Modèle de mesure en **4 étages** : ***Fuel*** (les outils IA sont-ils sollicités ?) → ***Adoption*** (comment les workflows changent à travers les équipes) → ***Output*** (l'IA contribue-t-elle au travail de production ?) → ***Impact*** (*« improving product velocity and reducing the time it takes to move from idea to customer value »*). Signaux qualité suivis : **code review turnaround time, first-run test pass rate, defect ratio, rework rate**. *« Quality and trust matter as much as speed »* — le cœur de la bascule : *« moving from local activity metrics toward broader system outcomes »*. **Les workflows doivent évoluer** : ce n'est *« not just a tooling shift »* mais un changement d'**operating model** — le rôle de l'ingénieur glisse vers *« defining intent, mapping problems, reviewing generated changes, and making higher-context architectural and quality decisions »*. L'**enablement** est aussi crucial que l'outil (hands-on learning, hackathons, workflow spotlights, bootcamps, peer-led examples) ; adoption à vitesses variables selon les équipes ; *« The goal is not to force every workflow through an agent »* — le rendre *« useful, safe, measurable, and repeatable where it creates meaningful leverage »*. **Ce qu'on a appris** : ***« AI doesn't eliminate bottlenecks in software development, but it does move them »*** (downstream : review, validation, testing, release, prod ops) → optimiser l'ancien goulot ne crée plus le même levier. *« The advantage will not come from access to the same foundation models everyone else can use. It will come from the systems built around those models : context, internal tooling, quality controls, and the workflows that connect them together. »* Pression aussi **en amont** (product & design) : specs structurées, design clarity, problem framing plus aiguisé. Clôture : ***« The future of engineering productivity will not be defined solely by who has the best models. It will be defined by who builds the best systems around them »*** ; *« The real challenge is no longer just generating more code, but building engineering systems that can reliably turn AI-assisted output into valuable experiences for our customers »*. Convergence directe avec **Salesforce/Tallapragada** (Effective Output : mesurer la valeur, pas le volume ; pas de tradeoff vitesse/qualité), **Gupta** (token-to-outcome attribution, cost of a completed outcome), **DORA** (au-delà du débit) et le déplacement du KPI vers le **system outcome** (idea→customer value).]]

### est_comparable_à

- [[kb/_entites-mineures#développeur-junior-non-supervisé\|développeur junior non supervisé]] (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2025-11/vibe-coding-vs-ai-assisted-engineering-osmani-2025-11-01\|Vibe coding vs AI-assisted engineering - Addy Osmani - Software development - Engineering principles - LinkedIn]]

### est_plus_efficace_que

- [[kb/_entites-mineures#un-ingénieur-humain\|un ingénieur humain]] (PERSONNE) — 0.90, DYNAMIQUE
  - [[fiches/2026-05/bfmtv-tech-co-business-ia-developpeurs-disparaissent-2026-05-05\|Débat télévisé sur BFM Business (émission *Tech & Co Business*, segment "Le débat", 17 minutes) avec **Rémi Jacquet** (DG Cast Software France, fondateur en 2023 d'un think tank d'une centaine de DSI sur l'impact de l'IA générative sur le développement, partenariat Cigref / Epita) et **Didier Girard** (CTO et DG de **SFEIR**, ESN française d'environ 1 000 personnes). Thèses fortes : *"écrire du code est devenu un anti-pattern"* (Girard), l'IA produit du code de qualité supérieure à la plupart des ingénieurs et est *"2 à 10× plus efficace"* — c'est une réalité, mais le métier ne disparaît pas. Le développeur devient **chef d'orchestre / manager d'agents / juge de paix**, les sprints de 14 jours sont remplacés par des ***bolts*** d'une heure à une demi-journée, la **Pizza Team** (8-10 personnes) ne fonctionne plus à l'ère agentique, un nouveau métier émerge — le ***product engineer*** —, la durée de vie d'une compétence passe de **10 ans à 1 an**, et la consommation de **tokens** devient le *fuel* de la création de valeur (anecdote NVIDIA qui verserait des primes en tokens, métaphore du chauffeur de taxi qui ne consomme pas d'essence). SFEIR revendique *"1 000 personnes, capacité de production 10 000"*. Côté Cast : positionnement sur le ***harness engineering*** (déterministe vs IA probabiliste, contrôle et garde-fous), aligné sur la tribune Sylvain Duranton (BCG X) dans *Les Échos* selon laquelle *"un agent = un LLM + des harnesses"*. Pivot historique 2024 *prompt engineering* → 2025 *context engineering* → 2026 *harness engineering*. Avertissement clé : *"plus l'IA devient forte, plus on baisse la garde — plus il y a de risques"* (Jacquet). Rôle pivot des DRH dans la transformation, remise à plat complète du SDLC, recommandation aux juniors de bétonner les fondamentaux d'architecture logicielle (*"le code est la partition, il faut maîtriser la symphonie"*).]]

### fait_passer_de

- [[kb/_entites-mineures#programmation-algorithmique-à-des-agents-Langchain\|programmation algorithmique à des agents Langchain]] (CONCEPT) — 0.88, ATEMPOREL
  - [[fiches/2024-02/rafal-wenvision-ia-generative-produit-techno-pas-projet-2024-02-23\|Tribune d'**Olivier Rafal** (Consulting Director Strategy chez **WeNvision**) publiée le **23 février 2024** sur **CIO-Online** (rubrique *Tribune*), qui pose une thèse encore contre-intuitive à l'époque : **l'IA générative relève davantage du produit technologique que du projet d'IA / data science**. **Argument 1 — la data science n'est pas le cœur du sujet** : créer un *foundation model* de toute pièce demande *« plusieurs mois, des millions d'euros et l'accès à d'énormes quantités de données »* — réservé à des acteurs aux datasets spécifiques et monétisables (ex. **Bloomberg** et son **BloombergGPT** pour la finance). Pour la quasi-totalité des entreprises, le bon réflexe n'est donc pas de recruter des data scientists. **Argument 2 — décalage de compétences** : il faut surtout des **ingénieurs de développement et d'intégration** (back/front), de **fortes compétences cloud** et du **DevOps**. Citation client : *« On n'a pas forcément besoin d'être data scientist, mais il faut comprendre les concepts de base, avoir des compétences de développement back office et de fortes compétences cloud. »* **Argument 3 — architecture de plateforme (orchestrateurs + API)** : construire une **plateforme d'IA générative** d'entreprise via orchestrateurs et API permet *« de travailler avec les meilleurs LLM du marché et d'en changer au fur et à mesure de leurs évolutions respectives, sans retoucher aux applications »* (anti vendor lock-in). **Argument 4 — du projet au produit** : *« La plate-forme […] il faut la considérer elle-même comme un produit »* ; au lieu d'un investissement ponctuel, prévoir un **flux de financement mensuel** (itérations continues, innovation permanente). **Argument 5 — gouvernance & shadow AI** : la démocratisation inédite de la GenAI engendre *« tant du shadow AI que de fortes attentes vis-à-vis de la DSI »* → gouvernance pour capter les besoins métiers, **prioriser les produits par la valeur**, superviser le bon fonctionnement. **Changement de paradigme** annoncé : *« on passe d'une programmation algorithmique classique à des agents Langchain qui gèrent une partie des décisions »*. **Intérêt pour la veille** : texte **fondateur (J-2 ans)** de la doctrine WeNvision (produit > projet, plateforme/API, financement en flux, gouvernance, shadow AI) que prolongeront les fiches [[wenvision-ai-agents-enterprise-deployment-2025-10-01]], [[habert-ia-agentique-production-2025-10-29]] et [[rafal-wenvision-tokenomics-foundation-finops-ia-2026-06-04]] (FinOps/token, financement en flux → gouvernance financière). Préfigure aussi le *harness/plateforme autour du modèle* (Dropbox/Okumura : *systems around the model*) et l'**indépendance modèle** par couche d'orchestration.]]

### peut_supprimer

- [[kb/_entites-mineures#tests-trop-couplés-à-l'implémentation-précédente\|tests trop couplés à l'implémentation précédente]] (CONCEPT) — 0.90, DYNAMIQUE
  - [[fiches/2026-05/farley-continuous-delivery-ai-assisted-development-trap-2026-05-13\|Continuous Delivery comme socle non-négociable du développement assisté par IA — Dave Farley sur sa chaîne *Modern Software Engineering* défend que sans CD, l'IA n'est pas un accélérateur mais un piège (theory of constraints + paradoxe de Jevons appliqués au code généré, ATDD/BDD comme garde-fou, pipeline de déploiement comme arbitre de qualité).]]

### produit

- [[kb/_entites-mineures#code-de-meilleure-qualité-que-la-plupart-des-ingénieurs\|code de meilleure qualité que la plupart des ingénieurs]] (CONCEPT) — 0.92, DYNAMIQUE
  - [[fiches/2026-05/bfmtv-tech-co-business-ia-developpeurs-disparaissent-2026-05-05\|Débat télévisé sur BFM Business (émission *Tech & Co Business*, segment "Le débat", 17 minutes) avec **Rémi Jacquet** (DG Cast Software France, fondateur en 2023 d'un think tank d'une centaine de DSI sur l'impact de l'IA générative sur le développement, partenariat Cigref / Epita) et **Didier Girard** (CTO et DG de **SFEIR**, ESN française d'environ 1 000 personnes). Thèses fortes : *"écrire du code est devenu un anti-pattern"* (Girard), l'IA produit du code de qualité supérieure à la plupart des ingénieurs et est *"2 à 10× plus efficace"* — c'est une réalité, mais le métier ne disparaît pas. Le développeur devient **chef d'orchestre / manager d'agents / juge de paix**, les sprints de 14 jours sont remplacés par des ***bolts*** d'une heure à une demi-journée, la **Pizza Team** (8-10 personnes) ne fonctionne plus à l'ère agentique, un nouveau métier émerge — le ***product engineer*** —, la durée de vie d'une compétence passe de **10 ans à 1 an**, et la consommation de **tokens** devient le *fuel* de la création de valeur (anecdote NVIDIA qui verserait des primes en tokens, métaphore du chauffeur de taxi qui ne consomme pas d'essence). SFEIR revendique *"1 000 personnes, capacité de production 10 000"*. Côté Cast : positionnement sur le ***harness engineering*** (déterministe vs IA probabiliste, contrôle et garde-fous), aligné sur la tribune Sylvain Duranton (BCG X) dans *Les Échos* selon laquelle *"un agent = un LLM + des harnesses"*. Pivot historique 2024 *prompt engineering* → 2025 *context engineering* → 2026 *harness engineering*. Avertissement clé : *"plus l'IA devient forte, plus on baisse la garde — plus il y a de risques"* (Jacquet). Rôle pivot des DRH dans la transformation, remise à plat complète du SDLC, recommandation aux juniors de bétonner les fondamentaux d'architecture logicielle (*"le code est la partition, il faut maîtriser la symphonie"*).]]
- [[kb/_entites-mineures#AI-slop-sans-direction-humaine\|AI slop sans direction humaine]] (CONCEPT) — 0.88, DYNAMIQUE
  - [[fiches/2026-04/soto-developer-taste-ai-slop-strategizeyourcareer-2026-04\|Goût du développeur face au code IA médiocre — Jugement et discipline — Embauche pour le goût — Qualité logicielle — Substack]]

### remplace

- [[kb/_entites-mineures#signal-d'effort-écrit\|signal d'effort écrit]] (CONCEPT) — 0.94, DYNAMIQUE
  - [[fiches/2023-06/mollick-setting-time-fire-button-temptation-2023-06-03\|Crise de sens au travail - Bouton "Help me write" - Setting time on fire - Signaux d'effort - Lettres de recommandation IA - Ethan Mollick - One Useful Thing]]

### réduit

- [[kb/_entites-mineures#temps-de-prototypage-(semaines-→-heures)\|temps de prototypage (semaines → heures)]] (CONCEPT) — 0.95, DYNAMIQUE
  - [[fiches/2025-08/a16z-one-prompt-zero-engineers-internal-dev-2025-08-19\|One Prompt Zero Engineers - a16z - No-code - Internal development - Gen AI - Democratization]]

### tend_à

- [[kb/_entites-mineures#grands-sauts-(giant-leaps)\|grands sauts (giant leaps)]] (CONCEPT) — 0.90, DYNAMIQUE
  - [[fiches/2026-05/farley-continuous-delivery-ai-assisted-development-trap-2026-05-13\|Continuous Delivery comme socle non-négociable du développement assisté par IA — Dave Farley sur sa chaîne *Modern Software Engineering* défend que sans CD, l'IA n'est pas un accélérateur mais un piège (theory of constraints + paradoxe de Jevons appliqués au code généré, ATDD/BDD comme garde-fou, pipeline de déploiement comme arbitre de qualité).]]

### transforme

- [[kb/_entites-mineures#développement-logiciel-interne\|développement logiciel interne]] (CONCEPT) — 0.97, DYNAMIQUE
  - [[fiches/2025-08/a16z-one-prompt-zero-engineers-internal-dev-2025-08-19\|One Prompt Zero Engineers - a16z - No-code - Internal development - Gen AI - Democratization]]
- [[kb/_entites-mineures#documents-comme-signaux\|documents comme signaux]] (CONCEPT) — 0.93, DYNAMIQUE
  - [[fiches/2023-06/mollick-setting-time-fire-button-temptation-2023-06-03\|Crise de sens au travail - Bouton "Help me write" - Setting time on fire - Signaux d'effort - Lettres de recommandation IA - Ethan Mollick - One Useful Thing]]
- [[kb/_entites-mineures#structures-organisationnelles\|structures organisationnelles]] (CONCEPT) — 0.93, DYNAMIQUE
  - [[fiches/2025-11/anand-wu-gen-ai-playbook-organizations-hbr-2025-11\|Framework stratégique IA générative - 4 quadrants déploiement - Paradoxe accès - Data as moat - Différenciation stratégique - Harvard Business Review - Bharat N. Anand - Andy Wu]]

## Relations (comme objet)

- [[kb/_entites-mineures#Adobe-Photoshop\|Adobe Photoshop]] **intègre** → IA générative — 0.92

## Fiches sources

- [[fiches/2025-11/anand-wu-gen-ai-playbook-organizations-hbr-2025-11\|Framework stratégique IA générative - 4 quadrants déploiement - Paradoxe accès - Data as moat - Différenciation stratégique - Harvard Business Review - Bharat N. Anand - Andy Wu]]
- [[fiches/2026-02/ensarguet-signal-noise-contribution-ai-slop-open-source-2026-02-04\|Repenser la contribution open source face au "AI slop" - Signal vs bruit]]
- [[fiches/2025-11/greyling-software-cost-collapse-permissionless-2025-11-04\|Effondrement coût et complexité logiciel, IA démocratise développement, logiciel devient "permissionless", dette technique sociétale, productivité développeurs +55% - Cobus Greyling - Medium]]
- [[fiches/2025-11/vibe-coding-vs-ai-assisted-engineering-osmani-2025-11-01\|Vibe coding vs AI-assisted engineering - Addy Osmani - Software development - Engineering principles - LinkedIn]]
