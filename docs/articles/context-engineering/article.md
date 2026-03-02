# Context Engineering — L'art de nourrir les agents IA

> De mai 2025 à février 2026, une discipline nouvelle s'est cristallisée : le context engineering. Trois contributions majeures en dessinent les contours — une étude empirique de 283 sessions, un cycle de vie inspiré de DevOps, et une méthodologie de terrain où chaque feature rend la suivante plus facile.

## Le paradoxe du prompt vide

Aristidis Vasilopoulos a mené [l'une des études quantitatives les plus détaillées du développement assisté par agents IA](../fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24.md) : 283 sessions sur 70 jours, 2 801 prompts humains, 16 522 tours autonomes. Au terme de cette immersion, un chiffre contre-intuitif : **80 % des prompts font moins de 100 mots**.

Pas parce que le développeur est paresseux. Parce que tout le travail a été fait en amont. Le contexte est déjà là — chargé, structuré, prêt à être consommé par l'agent. L'infrastructure contextuelle représente 24,2 % de la documentation totale du projet.

La plupart des développeurs font l'inverse. Ils rédigent de longs prompts ad-hoc, répètent les mêmes instructions, décrivent à chaque session l'architecture de leur projet. Ils font du prompt engineering artisanal quand le vrai levier se trouve ailleurs : dans tout ce qui arrive *avant* le prompt.

Patrick Debois, inventeur du terme DevOps, formule le même constat différemment : [le goulot d'étranglement du développement logiciel n'est plus la vitesse d'écriture du code, mais la qualité du contexte fourni aux agents](../fiches/2026-02/debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19.md). Pendant des décennies, l'industrie a optimisé la façon dont les humains écrivent du code — waterfall, agile, DevOps, platform engineering. Mais les agents écrivent désormais le code. Le nouveau goulot, c'est le contexte.

## Chaque session est un nouvel employé

Le problème fondamental est la mémoire. Les agents LLM n'ont pas de mémoire persistante entre sessions. Ils perdent la cohérence du projet et répètent les mêmes erreurs. Debois le résume d'une métaphore : **« chaque session est un nouvel employé »** — un employé qui repart de zéro, sans mémoire musculaire ni conversations de couloir.

C'est ce problème que le context engineering adresse. Non pas en formulant de meilleurs prompts, mais en construisant l'infrastructure qui rend n'importe quel prompt productif. La distinction est fondamentale : le prompt engineering optimise une interaction ; le context engineering optimise l'environnement dans lequel toutes les interactions se déroulent.

## L'architecture en trois tiers

Vasilopoulos n'a pas seulement posé le problème — il a construit et documenté la solution. Son [infrastructure de contexte codifié](../fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24.md) s'organise en trois tiers, chacun correspondant à un type de mémoire et une fréquence d'accès.

### Tier 1 — Constitution (Hot Memory)

C'est le contexte **toujours chargé** — la mémoire permanente de l'agent. Il encode les conventions, les patterns architecturaux, les modes de défaillance connus, et des tables de routage vers les agents spécialisés. C'est l'équivalent de la culture d'entreprise qu'un employé humain absorberait en quelques semaines, condensé dans un document que l'agent reçoit à chaque session.

Le principe fondamental : **une constitution basique améliore l'output dès le jour 1**. Pas besoin de perfection pour commencer.

### Tier 2 — Agents spécialisés (Warm Memory)

Ce sont des experts de domaine invoqués à la demande. Plus de la moitié de leur contenu est constituée de **faits** — formules, patterns, modes de défaillance — pas d'instructions comportementales. La connaissance du domaine prime sur les directives de comportement.

Dans l'étude de Vasilopoulos, le contrôle qualité et la correction domain-specific dominent les usages. Ce ne sont pas des assistants généralistes — ce sont des spécialistes qui portent la connaissance qu'un développeur humain senior accumulerait en des mois sur un sous-système.

### Tier 3 — Knowledge Base (Cold Memory)

La mémoire froide : des documents de spécification détaillés, récupérés à la demande. C'est le savoir de référence qu'on consulte quand la tâche l'exige.

L'impact mesuré par Vasilopoulos est significatif : des spécifications bien maintenues, référencées sur des dizaines de sessions, produisent des résultats sans erreur là où des tentatives sans contexte échouaient répétitivement. Chaque sous-système documenté accélère non seulement ses propres modifications futures, mais aussi **toutes les features adjacentes** qui en dépendent.

## Le CDLC — un DevOps pour le contexte

Si Vasilopoulos fournit l'architecture et les données empiriques, Debois fournit le cadre méthodologique. Son [Context Development Lifecycle (CDLC)](../fiches/2026-02/debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19.md) propose quatre phases qui traitent le contexte comme un artefact d'ingénierie à part entière — et non comme un simple fichier oublié dans un coin du projet.

### Phase 1 — Générer : rendre l'implicite explicite

La connaissance d'un projet existe à trois niveaux : technique (standards, patterns architecturaux), projet (priorités, scope), et business (conformité, attentes client). La plupart des équipes ne fournissent que le premier. Le CDLC exige de rendre explicites les deux autres.

Debois insiste sur un point crucial : **le contexte pourrit et entre en conflit**. Il ne suffit pas de le documenter une fois — il faut gérer activement sa fraîcheur et sa cohérence. Vasilopoulos confirme empiriquement : les specs obsolètes sont le principal mode de défaillance de son système. Un contexte périmé est pire que pas de contexte du tout — il induit activement en erreur.

### Phase 2 — Évaluer : le TDD du contexte

De même que le TDD définit le comportement attendu du code avant de l'écrire, le CDLC propose de définir le comportement attendu des agents avant de leur fournir du contexte. On exécute des scénarios, on évalue statistiquement les sorties (les LLMs étant non-déterministes), et on améliore le contexte en conséquence.

L'insight clé de Debois : **un échec d'évaluation n'est pas un défaut de l'agent, c'est une spécification non écrite**. Le problème est rarement le modèle — c'est le contexte incomplet. Cela rejoint Vasilopoulos : les explications répétées signalent le besoin de créer une spec. Si vous expliquez la même chose deux fois à un agent, le problème n'est pas l'agent — c'est l'absence de documentation.

### Phase 3 — Distribuer : le contexte comme package

Le contexte est traité comme un package versionné et sécurisé. L'insight fondamental de Debois concerne l'alignement des incitations. Pour la première fois dans l'histoire du développement logiciel, **partager la connaissance sert directement l'intérêt égoïste de l'auteur** : un meilleur contexte partagé améliore ses propres interactions avec les agents.

Debois ajoute un avertissement : le contexte est aussi une **surface d'attaque**. Il nécessite la même posture de sécurité que les dépendances logicielles — versionnement, audit, contrôle d'accès.

### Phase 4 — Observer : la boucle de feedback

En production, les agents révèlent les lacunes du contexte par leurs questions, leurs choix inattendus et leurs improvisations face au silence. Ces signaux alimentent le cycle suivant. La boucle se ferme.

Debois note que des fenêtres de contexte infinies ne résoudront pas le problème : plus de contexte signifie plus de contradictions. Le défi passe de la **curation** à la **gouvernance** — potentiellement plus complexe.

## Compound Engineering — l'inversion de la complexité

Si Debois pose le cadre théorique du cycle, Dan Shipper et Kieran Klaassen démontrent ce que ça donne en pratique. Leur [Compound Engineering](../fiches/2025-12/shipper-klaassen-compound-engineering-every-agents-2025-12-11.md) repose sur un renversement fondamental : en ingénierie traditionnelle, chaque feature rend la suivante **plus difficile** (dette technique, complexité croissante) ; en compound engineering, chaque feature rend la suivante **plus facile** grâce à une boucle d'apprentissage documentée.

Le processus se décompose en quatre étapes avec une répartition du temps qui brise les idées reçues :

**Plan (~40 % du temps)** — Recherche approfondie du contexte existant, des précédents et des meilleures pratiques. Production d'un document de planification complet. Klaassen l'a théorisé : planifier ne sert pas seulement le développeur — **planifier enseigne au système**. Un plan est du contexte structuré que l'agent peut consommer et réutiliser.

**Work (~10 % du temps)** — L'exécution du plan. C'est la partie la plus simple. Dix pour cent.

**Assess (~40 % du temps)** — Évaluation multi-perspective du résultat : qualité, sécurité, performance, complexité, architecture, cohérence avec les patterns existants. On retrouve ici la phase « Évaluer » du CDLC de Debois et l'esprit des agents spécialisés du Tier 2 de Vasilopoulos.

**Compound (~10 % du temps)** — C'est ce que Shipper appelle « l'étape magique ». Les leçons de chaque cycle sont résumées et stockées pour usage futur. Chaque bug, test échoué et insight est documenté et automatiquement distribué. Un nouveau développeur est aussi bien informé qu'un vétéran — car la connaissance ne réside plus dans les têtes, elle réside dans le contexte.

La répartition est parlante : **80 % du temps est consacré au Plan et à l'Assess**. Le travail d'exécution n'est que 10 %. Le contexte mange le code.

### L'inversion des incitations

Le compound engineering résout un problème historique de l'ingénierie logicielle : la documentation était un coût pur — du temps passé à écrire des choses que personne ne lirait. Avec les agents, la documentation devient le carburant direct de la productivité. Shipper le constate : l'estimation est qu'un développeur bien outillé produit aujourd'hui l'équivalent de cinq développeurs d'il y a quelques années. Non pas en codant plus vite, mais en structurant mieux le contexte.

L'étape Compound rend cette dynamique systématique. Avant chaque nouveau cycle, l'agent doit se poser trois questions : *Où est-ce que ça s'insère dans le système ? Faut-il ajouter à l'existant ou créer quelque chose de nouveau ? A-t-on déjà résolu un problème similaire ?* C'est du routage de contexte — exactement ce que Vasilopoulos encode dans ses tables de déclenchement au Tier 1.

## Trois visions, une convergence

Ce qui frappe dans ces trois travaux, c'est leur convergence indépendante vers les mêmes conclusions.

**Le contexte documenté compose.** Vasilopoulos le mesure empiriquement : chaque sous-système documenté accélère ses propres modifications futures et toutes les features adjacentes. Debois le théorise avec le [Context Flywheel](../fiches/2026-02/debois-tessl-context-flywheel-ai-coding-teams-2026-02-26.md) — le volant d'inertie contextuel : documenter le contexte → meilleur output → l'output enrichit le contexte → le contexte compose et accélère. Shipper et Klaassen le démontrent opérationnellement : l'étape Compound transforme chaque cycle en investissement pour les suivants.

**Le problème n'est jamais l'agent, c'est le contexte.** Vasilopoulos : « les explications répétées signalent le besoin de créer une spec ». Debois : « un échec d'évaluation est une spécification non écrite ». Klaassen : « planifier enseigne au système ». Trois formulations du même principe — le diagnostic fondamental du context engineering.

**Le partage de contexte est naturellement incitatif.** Debois le dit : « for the first time, there's a selfish reason to share knowledge ». Shipper le prouve : les leçons vivent dans le codebase, un nouveau développeur est aussi bien armé qu'un vétéran. Vasilopoulos le chiffre : 1-2 heures de maintenance par semaine pour un système qui s'améliore à chaque session. Le contexte est le premier artefact d'ingénierie dont le partage bénéficie autant à l'auteur qu'aux destinataires.

## L'ingénieur de demain est un ingénieur du contexte

Ces trois contributions dessinent ensemble une discipline cohérente. Vasilopoulos fournit l'architecture (trois tiers de mémoire), Debois le cycle de vie (Générer, Évaluer, Distribuer, Observer), Shipper et Klaassen le rythme opérationnel (Plan, Work, Assess, Compound).

Les principes convergents peuvent se résumer en cinq points :

1. **Le goulot d'étranglement a changé.** Ce n'est plus le code, c'est le contexte.
2. **Le contexte est un artefact d'ingénierie.** Il se conçoit, se teste, se versionne, se sécurise et se maintient.
3. **Le contexte compose.** Chaque investissement en documentation accélère les cycles suivants — la complexité n'est plus croissante mais décroissante.
4. **Le problème est toujours le contexte, jamais l'agent.** L'échec d'un agent est le symptôme d'une spécification absente.
5. **Le partage est naturellement incitatif.** Documenter le contexte sert directement celui qui le documente.

Le métier de développeur évolue. Il ne s'agit plus seulement d'écrire du code — il s'agit de structurer le contexte pour que les agents écrivent le bon code. L'expertise se déplace : de la syntaxe vers la sémantique, du prompt vers le système, de l'interaction vers l'architecture.

Et le coût d'entrée est modeste : Vasilopoulos l'estime à 1-2 heures de maintenance par semaine, pour un système dont la valeur compose à chaque session. Le volant d'inertie, une fois lancé, s'auto-alimente.

---

*Article basé sur l'analyse de 34 fiches de veille couvrant la période mai 2025 — février 2026. Trois sources principales structurent l'argumentation :*

- *[Vasilopoulos — Codified Context Infrastructure (2026-02)](../fiches/2026-02/vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24.md) — l'architecture et les données empiriques*
- *[Debois — Context Development Lifecycle (2026-02)](../fiches/2026-02/debois-tessl-context-development-lifecycle-ai-coding-agents-2026-02-19.md) — le cadre méthodologique*
- *[Shipper & Klaassen — Compound Engineering (2025-12)](../fiches/2025-12/shipper-klaassen-compound-engineering-every-agents-2025-12-11.md) — la mise en pratique*
