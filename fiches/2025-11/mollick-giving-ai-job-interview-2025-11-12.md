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
**Profil:** Educator-Practitioner | Première personne pédagogue | Analytical-Prescriptive | Intermédiaire-Accessible

Mollick adopte educator voice mêlant rigueur analytique et accessibilité pragmatique. Structure pédagogique progressive (problem benchmarks → vibes solution → real-world solution → prescriptive action) typique One Useful Thing. Exemples ludiques (otters on planes, GuacaDrone, pelican on bike) rendent concepts abstraits tangibles sans sacrifier profondeur. Tone équilibré acknowledge limitations ("some problems", "not easy") tout en offrant solutions actionnables ("you are going to need to interview your AI"). Citations données empiriques (Epoch AI graphs, GDPval paper) confèrent crédibilité. Analogies business (hiring VP, job interview) connectent AI adoption à pratiques management familières. Typique Mollick style (Wharton professor meets accessible blogger) démystifiant complexité technique pour audience practitioner.

## Pense-bêtes
- **Paradoxe benchmarking** : "Surprisingly hard time measuring how 'smart' they are, exactly"
- **Problèmes benchmarks standards** :
  - Answer keys publics → incorporés training (accidentel ou score gaming)
  - Don't know what tests really measure (MMLU-Pro: "mean cranial capacity Homo erectus?", "Cheap Trick 1979 live album?")
  - Tests uncalibrated : 84%→85% aussi difficile que 40%→41%?
  - Top score unachievable (errors in questions, unusual reporting)
- **Valeur collective** : Tous benchmarks trending "up and to the right" (AIME, GPQA, MMLU, SWE-bench, LiveBench, Terminal-Bench, ARC-AGI, METR Long Tasks)
- **Underlying ability factor** : Real-world impact medicine to finance
- **Lacune benchmarks** : Focus math, science, reasoning, coding - pas writing, sociological analysis, business advice, empathy
- **Citation clé** : "What you actually care about is which model would be best for YOUR needs"

**Benchmarking on Vibes**
- **Simon Willison** : pelican on bike test
- **Mollick tests** : otter on plane, JavaScript "starship control panel in distant future", challenging poem, build video games/shaders, analyze papers, time travel writing
- **Insights** : Does it make errors? Answers similar to others? Themes/biases?
- **Writing exercise** : "Someone doles out remaining words like wartime rations, told only 10,000 left lifetime. At 47 words, holding newborn."
- **Results patterns** :
  - Claude 4.5 Sonnet : strong writing model
  - Gemini 2.5 Pro : doesn't accurately keep word count (currently weakest)
  - GPT-5 Thinking : wild stylist, complex metaphor, sometimes incoherent
  - Kimi K2 Thinking : interesting phrases, story doesn't make sense
- **Limitation vibes** : Idiosyncratic, different answers every time, better prompts = better outcomes, relying on feelings vs real measures

**Benchmarking on Real World : OpenAI GDPval**
- **Step 1** : Experts avg 14 years experience (finance, law, retail) generate complex realistic projects 4-7 hours human time
- **Step 2** : Multiple AI models + human experts (paid by hour) complete tasks
- **Step 3** : Third expert group grade results blind (AI vs human unknown), over 1 hour per question
- **Strong areas** : Best models beat humans software development, personal financial advisors
- **Weak areas** : Pharmacists, industrial engineers, real estate agents easily beat AI
- **Model differences** : ChatGPT better sales manager, Claude better financial advisor
- **Reveals Jagged Frontier** shape + how changing over time

**GuacaDrone experiment**
- **Pitch** : Dubious idea - guacamole delivery via drones
- **Method** : Each AI model rate viability 1-10, ten times each (AI answers differ every time)
- **Results** :
  - Grok : great idea (enthusiastic)
  - Microsoft Copilot : excited
  - GPT-5 & Claude 4.5 : more skeptical
  - Mollick personally : would rate 2 or less
- **Implication** : "Consistently rating ideas 3-4 points higher or lower means consistently steering you in different direction"
- **Business impact** : Some want AI embraces risk, others avoid - important understand how AI "thinks" critical issues

**Interview Your Model prescription**
- **Individuals** : Vibes-based enough, run otter test (though now too easy - upgraded to "documentary footage 1960s famous last concert before incident with swarm of otters" in Sora 2)
- **Organizations at scale** : Different challenge
  - "Better" isn't enough thousands tasks, hundreds employees
  - Need know specifically what YOUR AI good at, not average
  - GDPval revealed : top models performance varies significantly by task
  - GuacaDrone : judgment on ambiguous questions, consistently different advice
  - Differences compound at scale
- **Can't rely on** : Vibes OR general benchmarks
- **Must do** :
  - Systematically test AI on actual work it will do + actual judgments it will make
  - Create realistic scenarios reflecting use cases
  - Run multiple times see patterns
  - Experts assess results
  - Compare models head-to-head on tasks that matter
  - "Difference between 'this model scored 85% MMLU' and 'this model more accurate our financial analysis tasks but more conservative risk assessments'"
  - Multiple times per year as new models released
- **Analogie finale** : "You wouldn't hire VP based solely on SAT scores. You shouldn't pick AI advising thousands decisions based on whether it knows mean cranial capacity Homo erectus is just under 1,000 cubic centimeters."

## RésuméDe400mots

Ethan Mollick argumente que malgré progrès mesurables IA, benchmarks standards échouent capturer ce qui importe vraiment : performance sur VOS tâches spécifiques avec VOS critères jugement. Il prescrit "interviewer" modèles IA comme candidats emploi plutôt que se fier scores tests génériques.

**Problèmes benchmarks standards**

Benchmarks comme MMLU-Pro posent questions obscures ("mean cranial capacity Homo erectus?", "Cheap Trick 1979 live album title?") dont on ignore ce qu'elles mesurent vraiment. Tests sont uncalibrated (difficulté 84%→85% vs 40%→41% inconnue), contiennent erreurs, et top scores peuvent être inatteignables. Pire : answer keys publics permettent incorporation training (accidentel ou gaming). Collectivement tous benchmarks (AIME, GPQA, MMLU, SWE-bench, ARC-AGI, METR) trending "up and to right", mesurant underlying ability factor corrélé real-world impact. Mais focus math/science/reasoning/coding laisse lacunes writing, business advice, empathy. "What you actually care about is which model would be best for YOUR needs."

**Benchmarking on vibes : approche individuelle**

Practioners développent tests idiosyncratiques : Simon Willison demande pelican on bike, Mollick otter on plane, JavaScript "starship control panel distant future", challenging poems, video games. Writing exercise révèle patterns : Claude 4.5 Sonnet strong writing, Gemini 2.5 Pro (currently weakest) doesn't track word count, GPT-5 Thinking wild stylist parfois incohérent, Kimi K2 Thinking phrases intéressantes mais story nonsensical. Vibes donnent "feel for AI models" mais idiosyncratiques, AI answers differ every time, rely feelings vs measures.

**Benchmarking real world : GDPval method**

OpenAI GDPval paper démontre approche rigoureuse : (1) Experts 14 years experience génèrent complex realistic projects 4-7 hours human time, (2) Multiple AI models + human experts complete tasks, (3) Third expert group grade blind over 1 hour per question. Révèle AI strong areas (software development, financial advisors beat humans) vs weak (pharmacists, industrial engineers, real estate agents beat AI). Model differences émergent : ChatGPT better sales manager, Claude better financial advisor. Reveals "Jagged Frontier" shape.

**GuacaDrone reveals model personality**

Mollick pitch dubious idea "guacamole delivery drones", demande AI models rate viability 1-10 ten times each. Grok enthusiastic, Copilot excited, GPT-5/Claude skeptical. Mollick personally rate 2 or less. "Consistently rating ideas 3-4 points higher or lower means consistently steering you in different direction." Companies may want risk-embracing vs risk-avoiding AI - must understand how AI "thinks" critical issues.

**Prescription organizations**

Vibes suffisent individuals. Organizations deploying at scale need systematic testing : AI on actual work + actual judgments, realistic scenarios, run multiple times, experts assess, compare head-to-head tasks matter. "Difference between 'model scored 85% MMLU' and 'model more accurate financial analysis but more conservative risk assessments.'" Multiple evaluations yearly as new models released.

Analogie finale : "You wouldn't hire VP based solely SAT scores. Shouldn't pick AI advising thousands decisions based whether knows mean cranial capacity Homo erectus just under 1,000 cubic centimeters."
