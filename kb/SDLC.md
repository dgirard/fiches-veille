# SDLC

> **Type** : METHODOLOGIE | 7 relations | 2 fiches sources

## Attributs

- **catégorie** : Cycle de développement logiciel hérité, pensé pour des humains
- **phases** : Définir → construire → vérifier → déployer → maintenir (invariant)

## Relations (comme sujet)

### réduit

- [[kb/_entites-mineures#modes-de-défaillance-humains-(ego,-fatigue,-oubli)\|modes de défaillance humains (ego, fatigue, oubli)]] (CONCEPT) — 0.90, ATEMPOREL
  - [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|Chris Williams (@voodootikigod) ouvre sa série ADLC en soutenant que faire tourner le SDLC humain sur des modèles est une erreur de catégorie : le cycle classique a été conçu pour contrer des modes de défaillance humains (ego, fatigue, oubli) absents chez les LLM. Il catalogue huit modes de défaillance porteurs (F1-F8) et cinq propriétés exploitables (E1-E5), et pose le principe fondateur : chaque phase d'un cycle agentique doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite.]]

## Relations (comme objet)

- [[kb/BMAD\|BMAD]] **s_applique_à** → SDLC — 0.97
- [[kb/IA\|IA]] **s_applique_à** → SDLC — 0.97
- [[kb/_entites-mineures#Phase-3-Intégration-et-Systématisation\|Phase 3 Intégration et Systématisation]] **s_applique_à** → SDLC — 0.96
- [[kb/IA\|IA]] **améliore** → SDLC — 0.95
- [[kb/ADLC\|ADLC]] **s_oppose_à** → SDLC — 0.92
- [[kb/Compound-Engineering\|Compound Engineering]] **est_instance_de** → SDLC — 0.88

## Fiches sources

- [[fiches/2026-06/rafal-wenvision-ingenierie-logicielle-ere-ia-tout-change-rien-ne-change-2026-06-01\|Tribune d'**Olivier Rafal** (Consulting Director Strategy, **WeNvision** — groupe **SFEIR** ; ex-rédacteur en chef du *Monde Informatique*) publiée le **1er juin 2026** sur **CIO-Online**, structurée autour d'un **paradoxe** : à l'ère de l'IA, l'ingénierie logicielle **change tout… et rien ne change**. **Ce qui change = le modèle opérationnel.** Les rôles sont redéfinis : le **Product Owner** passe de la découpe de backlog à la **génération de contexte exploitable par l'IA** ; le **développeur** passe de l'écriture de code au **cadrage, à l'orientation et à la révision** de l'exécution des agents ; le **QA** gagne la possibilité de définir en amont les **preuves attendues**. La structure d'équipe bascule des *« double pizza teams »* (chaînes de hand-off à ~8 personnes) vers les ***« sandwich teams »*** : un **binôme serré expert métier + tech lead augmentés par l'IA**, les autres compétences en appui. Chiffre interne **Sfeir** : *« ce binôme pilote désormais environ 80 % de la chaîne de production »*, les ~20 % restants (architecture, gouvernance de la donnée, sécurité) étant centralisés. Citation-pivot : ***« Le sujet n'est pas un sujet d'outil, mais un sujet de modèle opérationnel. »*** **Ce qui ne change pas = la discipline du cycle.** Les phases du **SDLC** (définir → construire → vérifier → déployer → maintenir) restent identiques et non négociables ; l'IA n'en supprime aucune, elle les **intensifie** : ***« tous ces relâchements que le rythme humain absorbait tant bien que mal deviennent, à la vitesse de l'IA, des défauts industriels »*** (métaphore sport amateur vs professionnel). D'où **trois *gates* inviolables** (contrôle humain) : **spécification, planification, revue de livraison** ; validation **par la preuve** (pas par les assertions de l'IA) ; **capitalisation systématique** (chaque cycle enrichit le suivant) → résultat mesuré : **−30 % d'itérations de correction après ~10 cycles**. Principe : ***« plus l'exécution est rapide, plus le cadre doit être strict »***. Concepts mobilisés : **harnais** (règles agentiques adaptées au contexte), **vibe-coding** jugé **intenable en entreprise**. **Troisième pilier = gouvernance, FinOps & pilotage par la valeur** : coûts IA **variables et récurrents** (~**10 €/heure** par poste augmenté), bascule licence forfaitaire → facturation à l'usage (parallèle cloud 2010s) ; le **FinOps** ne vise pas à réduire les coûts mais à *« optimiser l'efficience des outils »* (coût rapporté à la valeur) ; aligner en amont les **métriques métier** (time-to-market, fonctionnalités, performance, écoconception). **Conclusion** : l'accélération rend les fondamentaux **non négociables** ; le défi est **organisationnel et culturel**, pas technologique — sans sécuriser relation métier et discipline collective, une SDLC dopée à l'IA ne fait qu'**amplifier les problèmes** (aller plus vite dans le mur). Prolonge la doctrine WeNvision de [[rafal-wenvision-ia-generative-produit-techno-pas-projet-2024-02-23]] et [[rafal-wenvision-tokenomics-foundation-finops-ia-2026-06-04]] ; converge avec *systems around the model* [[dropbox-okumura-beyond-code-generation-engineering-productivity-ai-agents-2026-05-28]], le *harness engineering* [[osmani-agent-harness-engineering-2026-04-19]], Salesforce agentique et le débat *manager d'agents* (BFM/Girard, SFEIR).]]
- [[fiches/2026-06/williams-adlc-1-models-arent-human-2026-06-12\|Chris Williams (@voodootikigod) ouvre sa série ADLC en soutenant que faire tourner le SDLC humain sur des modèles est une erreur de catégorie : le cycle classique a été conçu pour contrer des modes de défaillance humains (ego, fatigue, oubli) absents chez les LLM. Il catalogue huit modes de défaillance porteurs (F1-F8) et cinq propriétés exploitables (E1-E5), et pose le principe fondateur : chaque phase d'un cycle agentique doit se rattacher à un mode de défaillance qu'elle défend ou à une propriété qu'elle exploite.]]
