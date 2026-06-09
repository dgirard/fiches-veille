# mollick-giving-ai-job-interview-2025-11-12

## Veille
Benchmarking IA au-delà des tests standards - Interview modèles IA pour use cases spécifiques - Jagged Frontier - OpenAI GDPval - Vibes vs mesures réelles - GuacaDrone example - Ethan Mollick - One Useful Thing

## Titre Article
Giving your AI a Job Interview

## Date
2025-11-12

## URL
https://www.oneusefulthing.org/p/giving-your-ai-a-job-interview

## Keywords
AI benchmarking, MMLU-Pro, ARC-AGI, METR Long Tasks, benchmarks limitations, vibes-based testing, OpenAI GDPval, real-world tasks, Jagged Frontier, model evaluation, GuacaDrone, risk assessment, otter on plane, pelican on bike, Simon Willison, Claude 4.5 Sonnet, GPT-5 Thinking, Gemini 2.5 Pro, Kimi K2 Thinking, Grok, Microsoft Copilot, model personality, advice at scale, job interview analogy, expert evaluation, model selection, organizational AI adoption, task-specific performance, judgment differences

## Authors
Ethan Mollick

## Ton
**Profil:** Éducateur-praticien | Première personne pédagogue | Analytique-prescriptif | Intermédiaire-accessible

Mollick adopte une voix d'éducateur mêlant rigueur analytique et accessibilité pragmatique. La structure pédagogique progressive (problème des benchmarks → solution "vibes" → solution monde réel → action prescriptive) est typique de One Useful Thing. Les exemples ludiques (loutres en avion, GuacaDrone, pélican à vélo) rendent les concepts abstraits tangibles sans sacrifier la profondeur. Le ton équilibré reconnaît les limites ("some problems", "not easy") tout en offrant des solutions actionnables ("you are going to need to interview your AI"). Les citations de données empiriques (graphiques Epoch AI, papier GDPval) confèrent de la crédibilité. Les analogies business (recruter un VP, entretien d'embauche) connectent l'adoption de l'IA à des pratiques de management familières. Style typique de Mollick (professeur à Wharton et blogueur accessible) démystifiant la complexité technique pour un public de praticiens.

## Pense-betes
- **Paradoxe du benchmarking** : il est "étonnamment difficile de mesurer à quel point ils sont 'intelligents', exactement"
- **Problèmes des benchmarks standards** :
  - Corrigés publics → incorporés dans l'entraînement (accidentellement ou pour gonfler les scores)
  - On ignore ce que les tests mesurent vraiment (MMLU-Pro : "capacité crânienne moyenne d'Homo erectus ?", "album live de Cheap Trick en 1979 ?")
  - Tests non calibrés : passer de 84% à 85% est-il aussi difficile que de 40% à 41% ?
  - Score maximal inatteignable (erreurs dans les questions, reporting inhabituel)
- **Valeur collective** : tous les benchmarks progressent "vers le haut et la droite" (AIME, GPQA, MMLU, SWE-bench, LiveBench, Terminal-Bench, ARC-AGI, METR Long Tasks)
- **Facteur de capacité sous-jacent** : corrélé à l'impact réel, de la médecine à la finance
- **Lacune des benchmarks** : focalisés sur maths, science, raisonnement, code — pas sur l'écriture, l'analyse sociologique, le conseil business, l'empathie
- **Citation clé** : "What you actually care about is which model would be best for YOUR needs"

**Benchmarking "aux vibes"**
- **Simon Willison** : test du pélican à vélo
- **Tests de Mollick** : loutre en avion, panneau de contrôle de vaisseau spatial en JavaScript, poème difficile, jeux vidéo/shaders, analyse d'articles, écriture sur le voyage dans le temps
- **Questions posées** : Fait-il des erreurs ? Réponses similaires aux autres ? Thèmes/biais récurrents ?
- **Exercice d'écriture** : "Quelqu'un distribue les mots restants comme des rations de guerre, on vous annonce qu'il vous en reste 10 000 à vie. À 47 mots, vous tenez un nouveau-né."
- **Patterns de résultats** :
  - Claude 4.5 Sonnet : modèle d'écriture solide
  - Gemini 2.5 Pro : ne tient pas le compte de mots (actuellement le plus faible)
  - GPT-5 Thinking : styliste exubérant, métaphores complexes, parfois incohérent
  - Kimi K2 Thinking : tournures intéressantes, mais l'histoire n'a pas de sens
- **Limites des vibes** : idiosyncratiques, réponses différentes à chaque fois, meilleurs prompts = meilleurs résultats, on se fie à des impressions plutôt qu'à des mesures

**Benchmarking sur le monde réel : OpenAI GDPval**
- **Étape 1** : des experts (14 ans d'expérience en moyenne : finance, droit, retail) créent des projets réalistes complexes de 4 à 7 heures de travail humain
- **Étape 2** : plusieurs modèles IA + experts humains (payés à l'heure) réalisent les tâches
- **Étape 3** : un troisième groupe d'experts note les résultats en aveugle (IA vs humain inconnu), plus d'une heure par question
- **Points forts** : les meilleurs modèles battent les humains en développement logiciel et conseil financier personnel
- **Points faibles** : pharmaciens, ingénieurs industriels et agents immobiliers battent facilement l'IA
- **Différences entre modèles** : ChatGPT meilleur directeur commercial, Claude meilleur conseiller financier
- **Révèle la forme de la Jagged Frontier** et son évolution dans le temps

**Expérience GuacaDrone**
- **Pitch** : idée douteuse — livraison de guacamole par drones
- **Méthode** : chaque modèle IA note la viabilité de 1 à 10, dix fois chacun (les réponses varient à chaque fois)
- **Résultats** :
  - Grok : excellente idée (enthousiaste)
  - Microsoft Copilot : emballé
  - GPT-5 et Claude 4.5 : plus sceptiques
  - Mollick personnellement : noterait 2 ou moins
- **Implication** : "Noter systématiquement les idées 3-4 points plus haut ou plus bas, c'est vous orienter systématiquement dans une direction différente"
- **Impact business** : certains veulent une IA qui embrasse le risque, d'autres qui l'évite — comprendre comment l'IA "pense" les questions critiques est essentiel

**Prescription "interviewez votre modèle"**
- **Individus** : les vibes suffisent, faites le test de la loutre (devenu trop facile — mis à niveau en "images documentaires des années 1960 du dernier concert célèbre avant l'incident avec un banc de loutres" dans Sora 2)
- **Organisations à grande échelle** : défi différent
  - "Meilleur" ne suffit pas pour des milliers de tâches et des centaines d'employés
  - Il faut savoir spécifiquement en quoi VOTRE IA est bonne, pas en moyenne
  - GDPval l'a révélé : la performance des meilleurs modèles varie significativement selon la tâche
  - GuacaDrone : jugement sur questions ambiguës, conseils systématiquement différents
  - Les différences se cumulent à l'échelle
- **Ne pas se fier** : ni aux vibes, ni aux benchmarks généraux
- **À faire** :
  - Tester systématiquement l'IA sur le travail réel qu'elle fera et les jugements réels qu'elle rendra
  - Créer des scénarios réalistes reflétant les cas d'usage
  - Exécuter plusieurs fois pour voir les patterns
  - Faire évaluer les résultats par des experts
  - Comparer les modèles tête-à-tête sur les tâches qui comptent
  - "La différence entre 'ce modèle a obtenu 85% au MMLU' et 'ce modèle est plus précis sur nos tâches d'analyse financière mais plus conservateur dans l'évaluation des risques'"
  - Plusieurs fois par an, à mesure que de nouveaux modèles sortent
- **Analogie finale** : "Vous n'embaucheriez pas un VP sur la seule base de ses scores au SAT. Vous ne devriez pas choisir une IA qui conseillera des milliers de décisions sur le fait qu'elle sache que la capacité crânienne moyenne d'Homo erectus est d'un peu moins de 1 000 centimètres cubes."

## RésuméDe400mots

Ethan Mollick soutient que malgré les progrès mesurables de l'IA, les benchmarks standards échouent à capturer ce qui importe vraiment : la performance sur VOS tâches spécifiques avec VOS critères de jugement. Il prescrit d'"interviewer" les modèles IA comme des candidats à l'embauche plutôt que de se fier aux scores de tests génériques.

**Problèmes des benchmarks standards**

Des benchmarks comme MMLU-Pro posent des questions obscures ("capacité crânienne moyenne d'Homo erectus ?", "titre de l'album live de Cheap Trick en 1979 ?") dont on ignore ce qu'elles mesurent vraiment. Les tests ne sont pas calibrés (la difficulté de passer de 84% à 85% versus de 40% à 41% est inconnue), contiennent des erreurs, et les meilleurs scores peuvent être inatteignables. Pire : les corrigés publics permettent leur incorporation dans l'entraînement (accidentelle ou délibérée). Collectivement, tous les benchmarks (AIME, GPQA, MMLU, SWE-bench, ARC-AGI, METR) progressent "vers le haut et la droite", mesurant un facteur de capacité sous-jacent corrélé à l'impact réel. Mais leur focalisation sur les maths, la science, le raisonnement et le code laisse des lacunes sur l'écriture, le conseil business et l'empathie. "What you actually care about is which model would be best for YOUR needs."

**Benchmarking "aux vibes" : approche individuelle**

Les praticiens développent des tests idiosyncratiques : Simon Willison demande un pélican à vélo, Mollick une loutre en avion, un panneau de contrôle de vaisseau spatial en JavaScript, des poèmes difficiles, des jeux vidéo. Un exercice d'écriture révèle des patterns : Claude 4.5 Sonnet est solide en écriture, Gemini 2.5 Pro (actuellement le plus faible) ne tient pas le compte de mots, GPT-5 Thinking est un styliste exubérant parfois incohérent, Kimi K2 Thinking produit des tournures intéressantes mais une histoire sans queue ni tête. Les vibes donnent une "sensation" des modèles, mais restent idiosyncratiques : les réponses varient à chaque fois et on se fie à des impressions plutôt qu'à de vraies mesures.

**Benchmarking sur le monde réel : la méthode GDPval**

Le papier GDPval d'OpenAI démontre une approche rigoureuse : (1) des experts de 14 ans d'expérience en moyenne créent des projets réalistes complexes de 4 à 7 heures de travail humain, (2) plusieurs modèles IA et des experts humains réalisent les tâches, (3) un troisième groupe d'experts note en aveugle, plus d'une heure par question. L'étude révèle les points forts de l'IA (développement logiciel, conseil financier : elle bat les humains) et ses faiblesses (pharmaciens, ingénieurs industriels, agents immobiliers battent l'IA). Des différences entre modèles émergent : ChatGPT est meilleur directeur commercial, Claude meilleur conseiller financier. La forme de la "Jagged Frontier" se dessine.

**GuacaDrone révèle la personnalité des modèles**

Mollick pitche une idée douteuse, la "livraison de guacamole par drones", et demande aux modèles de noter sa viabilité de 1 à 10, dix fois chacun. Grok est enthousiaste, Copilot emballé, GPT-5 et Claude sceptiques. Mollick lui-même noterait 2 ou moins. "Noter systématiquement les idées 3-4 points plus haut ou plus bas, c'est vous orienter systématiquement dans une direction différente." Selon les entreprises, on voudra une IA qui embrasse ou évite le risque : il faut comprendre comment l'IA "pense" les questions critiques.

**Prescription pour les organisations**

Les vibes suffisent aux individus. Les organisations qui déploient à grande échelle ont besoin de tests systématiques : l'IA sur le travail et les jugements réels, des scénarios réalistes, exécutés plusieurs fois, évalués par des experts, avec comparaison tête-à-tête sur les tâches qui comptent. "La différence entre 'le modèle a obtenu 85% au MMLU' et 'le modèle est plus précis en analyse financière mais plus conservateur sur les risques'." À refaire plusieurs fois par an au rythme des nouveaux modèles.

Analogie finale : "Vous n'embaucheriez pas un VP sur ses seuls scores au SAT. Ne choisissez pas l'IA qui conseillera des milliers de décisions sur sa connaissance de la capacité crânienne moyenne d'Homo erectus."

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Ethan Mollick | PERSONNE | publie | Giving your AI a Job Interview | DOCUMENT | 0.99 | STATIQUE | déclaré_article |
| Ethan Mollick | PERSONNE | recommande | interviewer modèles IA sur tâches réelles | METHODOLOGIE | 0.98 | ATEMPOREL | déclaré_article |
| Ethan Mollick | PERSONNE | affirme_que | les benchmarks standards échouent à mesurer la performance tâche-spécifique | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| questions de valeur incertaine | CONCEPT | fait_partie_de | MMLU-Pro | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | GDPval paper | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| GDPval | METHODOLOGIE | mesure | Jagged Frontier des capacités IA | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Claude 4.5 Sonnet | TECHNOLOGIE | surpasse | autres modèles en écriture | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Claude | TECHNOLOGIE | surpasse | ChatGPT en conseil financier | TECHNOLOGIE | 0.87 | DYNAMIQUE | déclaré_article |
| biais pro-risque dans évaluation idées | CONCEPT | observé_dans | Grok | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Simon Willison | PERSONNE | utilise | test pelican sur vélo | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Ethan Mollick | PERSONNE | utilise | test loutre sur avion | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Ethan Mollick | PERSONNE | affirme_que | le vibes-based testing est insuffisant pour les organisations déployant l'IA à grande échelle | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| GDPval | METHODOLOGIE | mesure | différences significatives de performance entre modèles par tâche | MESURE | 0.96 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Ethan Mollick | PERSONNE | affiliation | Wharton School / One Useful Thing | AJOUT |
| Ethan Mollick | PERSONNE | rôle | Professeur-Blogueur, éducateur IA | AJOUT |
| GDPval | METHODOLOGIE | méthode | Experts 14 ans d'expérience, évaluation en aveugle | AJOUT |
| GDPval | METHODOLOGIE | portée | Finance, droit, retail, développement logiciel | AJOUT |
| benchmarks standards | CONCEPT | exemples | MMLU-Pro, AIME, GPQA, SWE-bench, ARC-AGI, METR | AJOUT |
| Jagged Frontier | CONCEPT | définition | Carte irrégulière des forces/faiblesses des IA par domaine | AJOUT |
| vibes-based testing | METHODOLOGIE | usage | Individus practioners, évaluation subjective modèles | AJOUT |
| Claude 4.5 Sonnet | TECHNOLOGIE | point fort | Qualité d'écriture créative | AJOUT |
| Gemini 2.5 Pro | TECHNOLOGIE | point faible | Suivi de compte de mots (nov. 2025) | AJOUT |
| GPT-5 Thinking | TECHNOLOGIE | style | Styliste exubérant, métaphores complexes, parfois incohérent | AJOUT |
| Grok | TECHNOLOGIE | biais | Sur-évaluation des idées risquées (biais pro-risque) | AJOUT |
| OpenAI | ORGANISATION | secteur | IA / Recherche | AJOUT |
| Simon Willison | PERSONNE | rôle | Practitioner IA, développeur, blogger | AJOUT |
| GuacaDrone | CONCEPT | rôle | Cas test révélateur de biais d'évaluation des modèles | AJOUT |
