# context engineering

> **Type** : METHODOLOGIE | 8 relations | 4 fiches sources

## Attributs

- **catégorie** : Ingénierie du contexte fourni aux agents IA
- **définition** : Fournir aux agents un contexte riche et structuré (6 types ; statique vs dynamique)
- **période_dominante** : 2025

## Relations (comme sujet)

### améliore

- [[kb/_entites-mineures#prompt-engineering\|prompt engineering]] (METHODOLOGIE) — 0.95, ATEMPOREL
  - [[fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23\|Context Engineering - Domain Understanding - DICE - Rod Johnson - LLM - Domain Model - Embabel]]
- [[kb/_entites-mineures#qualité-du-code-généré-par-IA\|qualité du code généré par IA]] (CONCEPT) — 0.93, ATEMPOREL
  - [[fiches/2026-05/osmani-google-new-sdlc-vibe-coding-agentic-engineering-2026-05\|Whitepaper Google (volet « Day 1 » d'une série, par Addy Osmani, Shubham Saboo et Sokratis Kartakis) qui cartographie la mutation du cycle de vie logiciel (SDLC) à l'ère des agents de codage. Thèse : le basculement fondamental n'est pas un nouveau langage mais le passage de l'écriture de code à l'**expression d'intention**. Le document pose un spectre allant du *vibe coding* (prompter et accepter) à l'*agentic engineering* (l'IA implémente sous contraintes, tests et boucles de feedback conçus par l'humain), avec le **context engineering** comme compétence centrale, le modèle de l'**usine logicielle** (le livrable du dev = le système qui produit le code), le **harness engineering** (Agent = Modèle + Harness) et une analyse économique CapEx/OpEx du coût total de possession.]]

### remplace

- [[kb/_entites-mineures#Prompt-Engineering\|Prompt Engineering]] (METHODOLOGIE) — 0.92, STATIQUE
  - [[fiches/2026-05/bfmtv-tech-co-business-ia-developpeurs-disparaissent-2026-05-05\|Débat télévisé sur BFM Business (émission *Tech & Co Business*, segment "Le débat", 17 minutes) avec **Rémi Jacquet** (DG Cast Software France, fondateur en 2023 d'un think tank d'une centaine de DSI sur l'impact de l'IA générative sur le développement, partenariat Cigref / Epita) et **Didier Girard** (CTO et DG de **SFEIR**, ESN française d'environ 1 000 personnes). Thèses fortes : *"écrire du code est devenu un anti-pattern"* (Girard), l'IA produit du code de qualité supérieure à la plupart des ingénieurs et est *"2 à 10× plus efficace"* — c'est une réalité, mais le métier ne disparaît pas. Le développeur devient **chef d'orchestre / manager d'agents / juge de paix**, les sprints de 14 jours sont remplacés par des ***bolts*** d'une heure à une demi-journée, la **Pizza Team** (8-10 personnes) ne fonctionne plus à l'ère agentique, un nouveau métier émerge — le ***product engineer*** —, la durée de vie d'une compétence passe de **10 ans à 1 an**, et la consommation de **tokens** devient le *fuel* de la création de valeur (anecdote NVIDIA qui verserait des primes en tokens, métaphore du chauffeur de taxi qui ne consomme pas d'essence). SFEIR revendique *"1 000 personnes, capacité de production 10 000"*. Côté Cast : positionnement sur le ***harness engineering*** (déterministe vs IA probabiliste, contrôle et garde-fous), aligné sur la tribune Sylvain Duranton (BCG X) dans *Les Échos* selon laquelle *"un agent = un LLM + des harnesses"*. Pivot historique 2024 *prompt engineering* → 2025 *context engineering* → 2026 *harness engineering*. Avertissement clé : *"plus l'IA devient forte, plus on baisse la garde — plus il y a de risques"* (Jacquet). Rôle pivot des DRH dans la transformation, remise à plat complète du SDLC, recommandation aux juniors de bétonner les fondamentaux d'architecture logicielle (*"le code est la partition, il faut maîtriser la symphonie"*).]]

## Relations (comme objet)

- [[kb/DICE\|DICE]] **est_basé_sur** → context engineering — 0.98
- [[kb/Andrej-Karpathy\|Andrej Karpathy]] **a_créé** → context engineering — 0.97
- [[kb/DICE\|DICE]] **améliore** → context engineering — 0.97
- [[kb/Harness-engineering\|Harness engineering]] **est_variante_de** → context engineering — 0.95
- [[kb/Harness-engineering\|Harness Engineering]] **remplace** → context engineering — 0.92

## Fiches sources

- [[fiches/2026-05/bfmtv-tech-co-business-ia-developpeurs-disparaissent-2026-05-05\|Débat télévisé sur BFM Business (émission *Tech & Co Business*, segment "Le débat", 17 minutes) avec **Rémi Jacquet** (DG Cast Software France, fondateur en 2023 d'un think tank d'une centaine de DSI sur l'impact de l'IA générative sur le développement, partenariat Cigref / Epita) et **Didier Girard** (CTO et DG de **SFEIR**, ESN française d'environ 1 000 personnes). Thèses fortes : *"écrire du code est devenu un anti-pattern"* (Girard), l'IA produit du code de qualité supérieure à la plupart des ingénieurs et est *"2 à 10× plus efficace"* — c'est une réalité, mais le métier ne disparaît pas. Le développeur devient **chef d'orchestre / manager d'agents / juge de paix**, les sprints de 14 jours sont remplacés par des ***bolts*** d'une heure à une demi-journée, la **Pizza Team** (8-10 personnes) ne fonctionne plus à l'ère agentique, un nouveau métier émerge — le ***product engineer*** —, la durée de vie d'une compétence passe de **10 ans à 1 an**, et la consommation de **tokens** devient le *fuel* de la création de valeur (anecdote NVIDIA qui verserait des primes en tokens, métaphore du chauffeur de taxi qui ne consomme pas d'essence). SFEIR revendique *"1 000 personnes, capacité de production 10 000"*. Côté Cast : positionnement sur le ***harness engineering*** (déterministe vs IA probabiliste, contrôle et garde-fous), aligné sur la tribune Sylvain Duranton (BCG X) dans *Les Échos* selon laquelle *"un agent = un LLM + des harnesses"*. Pivot historique 2024 *prompt engineering* → 2025 *context engineering* → 2026 *harness engineering*. Avertissement clé : *"plus l'IA devient forte, plus on baisse la garde — plus il y a de risques"* (Jacquet). Rôle pivot des DRH dans la transformation, remise à plat complète du SDLC, recommandation aux juniors de bétonner les fondamentaux d'architecture logicielle (*"le code est la partition, il faut maîtriser la symphonie"*).]]
- [[fiches/2026-04/boeckeler-harness-engineering-coding-agents-2026-04-02\|Harness engineering : modèle mental pour construire la confiance dans les agents de codage via guides feedforward et capteurs feedback]]
- [[fiches/2025-07/context-engineering-domain-understanding-johnson-2025-07-23\|Context Engineering - Domain Understanding - DICE - Rod Johnson - LLM - Domain Model - Embabel]]
- [[fiches/2026-05/osmani-google-new-sdlc-vibe-coding-agentic-engineering-2026-05\|Whitepaper Google (volet « Day 1 » d'une série, par Addy Osmani, Shubham Saboo et Sokratis Kartakis) qui cartographie la mutation du cycle de vie logiciel (SDLC) à l'ère des agents de codage. Thèse : le basculement fondamental n'est pas un nouveau langage mais le passage de l'écriture de code à l'**expression d'intention**. Le document pose un spectre allant du *vibe coding* (prompter et accepter) à l'*agentic engineering* (l'IA implémente sous contraintes, tests et boucles de feedback conçus par l'humain), avec le **context engineering** comme compétence centrale, le modèle de l'**usine logicielle** (le livrable du dev = le système qui produit le code), le **harness engineering** (Agent = Modèle + Harness) et une analyse économique CapEx/OpEx du coût total de possession.]]
