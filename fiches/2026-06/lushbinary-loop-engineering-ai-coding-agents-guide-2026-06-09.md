---
themes: [agents-codage-ia-skills]
source: "Lushbinary"
---
# lushbinary-loop-engineering-ai-coding-agents-guide-2026-06-09

## Veille

Guide technique approfondi (blog d'agence Lushbinary) sur le **Loop Engineering** : concevoir les systèmes qui pilotent les agents de codage en boucle, plutôt que de les prompter manuellement. Couvre la filiation prompt → context → loop engineering, la technique Ralph (Geoffrey Huntley), les **cinq briques + la mémoire** d'une boucle, leur implémentation dans Claude Code et OpenAI Codex, l'écriture de conditions d'arrêt vérifiables, une échelle de maturité d'adoption et les risques qui s'aggravent à mesure que les boucles se sophistiquent. Domaine : ingénierie logicielle agentique, agents de codage, harness/orchestration.

## Titre Article

Loop Engineering: The Guide for AI Agents

## Date

2026-06-09

## URL

https://lushbinary.com/blog/loop-engineering-ai-coding-agents-guide/

## Keywords

Loop engineering, agents de codage, harness engineering, technique Ralph, conditions d'arrêt, /goal, /loop, git worktrees, skills, sub-agents, maker-checker, MCP, mémoire d'entreprise, Claude Code, OpenAI Codex, échelle de maturité, dette de compréhension, vérification adversariale, FinOps tokens

## Authors

Lushbinary Team

## Ton

**Profil** : guide pédagogique B2B à la troisième personne, registre instructif et structuré (titres, tableaux comparatifs, exemples de code shell/markdown/TOML), niveau technique élevé visant les ingénieurs et lead techs. Article à double fonction : pédagogie de fond + accroche commerciale finale (section « Why Lushbinary » + consultation gratuite).

**Style** : explicatif et didactique, avec des formules-slogans condensant chaque idée (« Agents forget. Repositories remember. », « The leverage shifted, complexity didn't decrease. », « Write stop conditions like contracts, not wishes. », « You remain the ceiling. », « Build loops staying engineers. »). Métaphores : la boucle comme « battement de cœur » (heartbeat) du système ; les conditions d'arrêt comme des « contrats » / « tests d'acceptation » ; Ralph Wiggum (personnage des Simpsons) pour la simplicité déterministe. Autorité revendiquée par l'expérience opérationnelle (intégrations IA en production, santé/fintech/SaaS/e-commerce « depuis l'ère GPT-4 ») et l'ancrage dans des sources nommées (Addy Osmani, Peter Steinberger, Boris Cherny, Geoffrey Huntley). Note de transparence finale : contenu reformulé pour conformité de licence, capacités sourcées de la doc officielle Anthropic/OpenAI.

## Pense-betes

- **Définition en une phrase** : le loop engineering construit des systèmes qui promptent les agents **selon un planning et vers un objectif**, au lieu de taper des prompts individuels. Le levier passe de la *qualité d'un prompt* à la *conception du système*.
- **Deux niveaux de boucle** : la *boucle interne* (perceive-reason-act-observe à chaque tour, déjà native aux agents) vs la *boucle externe* qu'on conçoit (planning, helpers, auto-alimentation en travail, persistance sur de nombreux tours).
- **Filiation en 3 couches** (chacune englobe la précédente) : Prompt Engineering (1 instruction) → Context Engineering (contenu de la fenêtre) → Loop Engineering (système qui décide quoi prompter, quand, et si le résultat est acceptable). Le prompt et le contexte restent indispensables — un mauvais prompt produit juste du mauvais travail plus vite.
- **Origine du terme** : popularisé par **Addy Osmani** (Google) en juin 2026, sur les observations de **Peter Steinberger** (*« you should be designing loops that prompt your agents »*) et de **Boris Cherny** (lead Claude Code chez Anthropic : son focus est passé à *écrire des boucles* plutôt qu'à prompter directement).
- **Technique Ralph** (Geoffrey Huntley, début 2026, d'après Ralph Wiggum) : faire tourner l'agent dans une simple boucle `while`, même prompt à chaque itération, contre une spec écrite, **contexte neuf à chaque tour**. L'innovation non-évidente = le **reset du contexte** (évite la dégradation des longues sessions). L'intelligence vient des specs claires + résultats vérifiables + **mémoire externe** (`PLAN.md`, `STATUS.md`), pas de runs héroïques.
- **Le loop engineering productise Ralph** : le `while` devient automation planifiée, les resets deviennent worktrees/sub-agents, le check « ALL TASKS DONE » devient une condition `/goal` vérifiée par un modèle séparé.
- **5 briques + mémoire** : (1) **Automations** (déclencheurs planifiés de découverte/tri) ; (2) **Worktrees** (agents parallèles sans collision) ; (3) **Skills** (savoir projet documenté) ; (4) **Plugins/connecteurs** (MCP, accès aux outils réels) ; (5) **Sub-agents** (séparer génération et vérification) ; (6) **Mémoire** (markdown, boards Linear/GitHub — hors fenêtre de contexte). *« Agents forget. Repositories remember. »*
- **Claude Code et Codex embarquent les 5 briques + mémoire** sous des noms différents mais structures identiques → concevoir des boucles qui survivent au changement d'outil.
- **Automations** : Codex (onglet Automations, runs vers Triage inbox, runs vides s'auto-archivent) ; Claude Code (`/loop` + hooks + intégration GitHub Actions). Primitive in-session clé = **`/goal`** : maintient le travail jusqu'à ce que la condition spécifiée soit vérifiablement vraie, **un modèle plus petit distinct note la complétion à chaque tour** (l'agent ne s'auto-évalue pas).
- **État mi-2026** : `/goal` livré dans Claude Code **v2.1.139 (11 mai 2026)**, branche 2.1.x avec **Opus 4.8** par défaut + workflows dynamiques orchestrant de larges flottes de sub-agents ; Codex a ajouté `/goal` en **CLI 0.128.0**. Des praticiens rapportent des agents travaillant des dizaines d'heures sans surveillance → **les conditions d'arrêt deviennent l'élément le plus critique**.
- **Écrire les conditions d'arrêt comme des contrats** : état final + preuve + contraintes + plafond turns/budget. Ex. « couverture `src/billing` ≥ 90 % ; `npm test` sort 0 ; aucune API publique modifiée ; stop après 25 tours ou 5 $ ».
- **Trois pratiques pour des boucles fiables** (équipes Claude Code) : préserver les erreurs (pour que la boucle apprenne au lieu de répéter), intégrer la vérification *dès le départ*, traiter tests rouges / CI rouge comme des **signaux d'honnêteté**. Une boucle sans preuve d'échec croit toujours avoir réussi.
- **Worktrees** = isolation git réelle (répertoires séparés sur branches distinctes, historique partagé). Mais **« You remain the ceiling »** : la capacité humaine de revue, pas le nombre de worktrees, détermine combien d'agents parallèles on fait vraiment tourner.
- **Sub-agents maker-checker** = le changement structurel le plus puissant : un agent vérificateur **adversarial** (modèle fort, haute réflexion, instruit pour rejeter ce qui n'est pas prouvé) gardant le travail avant la revue humaine. Les modèles qui notent leur propre travail sont trop généreux.
- **Échelle de maturité (Niveaux 0→4)** : 0 Manuel → 1 Triage (findings en markdown, pas de code) → 2 Draft (fixes sur branches isolées) → 3 Verified PR (sub-agent vérificateur en gate) → 4 Auto-merge (catégories à faible risque sur CI verte). Ne monter d'un cran que si le niveau actuel produit du travail qu'on aurait fait soi-même.
- **3 risques qui s'aggravent (pas s'atténuent)** : la **vérification reste ta responsabilité** (« done » = revendication, pas preuve) ; la **dette de compréhension s'accélère** (le code part plus vite qu'on ne le comprend) ; la **capitulation cognitive** (accepter les sorties sans jugement) — deux personnes construisant la même boucle obtiennent des résultats opposés selon qu'elles l'utilisent pour avancer sur du travail compris ou pour éviter de le comprendre.
- **Attention aux tokens** : boucles planifiées + modèles vérificateurs post-tour brûlent des tokens vite. Commencer avec des cadences lentes et des conditions serrées, monitorer les coûts plusieurs jours, scaler seulement après preuve de travail mergé utile.
- **Sécurité** : les boucles autonomes avec connecteurs touchent la prod → garde-fous, permissions, audit logging nécessaires.

## RésuméDe400mots

Ce guide de l'agence Lushbinary théorise le **loop engineering** : le passage du *prompting manuel* d'un agent de codage à la *conception des systèmes qui le promptent automatiquement*. Pendant deux ans, tirer de la valeur d'un agent suivait un schéma simple (prompt, contexte, revue, instruction suivante) où le développeur gardait le contrôle à chaque tour. À partir de juin 2026, le levier se déplace : le développeur cesse d'être le prompteur principal pour devenir le concepteur d'une **boucle externe** qui découvre le travail, le distribue, valide les résultats, documente et décide de la suite. Le terme, popularisé par **Addy Osmani** (Google), s'appuie sur Peter Steinberger (*« design loops that prompt your agents »*) et Boris Cherny (Claude Code/Anthropic : écrire des boucles plutôt que prompter).

Le loop engineering est la **troisième couche** d'une pile (prompt → context → loop), chacune englobant la précédente ; la complexité ne diminue pas, le levier se déplace vers la conception. La **technique Ralph** de Geoffrey Huntley (début 2026) en est la validation pré-terminologique : une boucle `while`, même prompt, **contexte neuf à chaque itération**, état durable sur disque (`PLAN.md`, `STATUS.md`). Le loop engineering la productise.

Une boucle fonctionnelle requiert **cinq briques + la mémoire** : (1) **automations** planifiées (Codex Automations ; Claude Code `/loop`, hooks, `/goal`) ; (2) **worktrees** git pour des agents parallèles sans collision ; (3) **skills** capturant le savoir projet (`SKILL.md`) ; (4) **plugins/connecteurs** via MCP (portables entre outils) ; (5) **sub-agents** séparant le « maker » du « checker » ; (6) **mémoire** hors contexte (markdown, boards). Claude Code et OpenAI Codex embarquent désormais ces briques sous des noms différents mais structures identiques.

La primitive `/goal` (Claude Code v2.1.139, 11 mai 2026, Opus 4.8 par défaut ; Codex CLI 0.128.0) maintient le travail jusqu'à une condition **vérifiée par un modèle distinct**. D'où l'impératif : écrire les conditions d'arrêt **comme des contrats** (état final, preuve, contraintes, plafond turns/budget). Le split **maker-checker** (vérificateur adversarial) est le changement le plus puissant. Une **échelle de maturité** en 5 niveaux (Manuel → Triage → Draft → Verified PR → Auto-merge) guide une adoption prudente, l'humain restant dans le chemin tant que la preuve ne permet pas de s'en retirer.

Trois risques **s'aggravent** avec la sophistication : la vérification reste humaine (« done » = revendication, pas preuve), la **dette de compréhension** s'accélère, et la **capitulation cognitive** guette. Conclusion : concevoir ses boucles « comme quelqu'un qui compte rester ingénieur ».

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Addy Osmani | PERSONNE | publie | Loop Engineering | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Loop Engineering | METHODOLOGIE | s_inspire_de | "you should be designing loops that prompt your agents" | CITATION | 0.92 | STATIQUE | déclaré_article |
| Boris Cherny | PERSONNE | affirme_que | "mon focus est passé à écrire des boucles plutôt qu'à prompter directement" | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Loop Engineering | METHODOLOGIE | remplace | prompting manuel des agents | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | est_basé_sur | Context Engineering | METHODOLOGIE | 0.88 | ATEMPOREL | inféré |
| Geoffrey Huntley | PERSONNE | a_créé | technique Ralph | METHODOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Technique Ralph | METHODOLOGIE | utilise | réinitialisation du contexte à chaque itération | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | est_basé_sur | technique Ralph | METHODOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Git worktrees | TECHNOLOGIE | résout | collisions de fichiers entre agents parallèles | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Sub-agents maker-checker | METHODOLOGIE | permet | séparation génération / vérification | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| /goal | TECHNOLOGIE | fait_partie_de | Claude Code | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Claude Code | TECHNOLOGIE | utilise | Opus 4.8 | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Skills | TECHNOLOGIE | réduit | coût de ré-explication du contexte projet | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Mémoire externe | CONCEPT | permet | persistance de l'état entre runs | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| MCP | TECHNOLOGIE | permet | connecteurs portables entre Codex et Claude Code | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Loop Engineering | METHODOLOGIE | affirme_que | "la dette de compréhension s'accélère avec des boucles plus rapides" | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Conditions d'arrêt | CONCEPT | recommande | écriture comme des contrats (état, preuve, contraintes, budget) | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Loop Engineering | METHODOLOGIE | définition | Concevoir les systèmes qui promptent les agents (boucle externe) plutôt que prompter manuellement | AJOUT |
| Addy Osmani | PERSONNE | rôle | Ingénieur Google, a popularisé le terme « loop engineering » (juin 2026) | AJOUT |
| Peter Steinberger | PERSONNE | contribution | Observation fondatrice (« design loops that prompt your agents »), checklist de boucle | AJOUT |
| Boris Cherny | PERSONNE | rôle | Lead Claude Code chez Anthropic | AJOUT |
| Geoffrey Huntley | PERSONNE | contribution | Auteur de la technique Ralph (début 2026) | AJOUT |
| Technique Ralph | METHODOLOGIE | principe | Boucle `while`, même prompt, contexte neuf, mémoire externe (PLAN.md/STATUS.md) | AJOUT |
| Claude Code | TECHNOLOGIE | versions | `/goal` livré v2.1.139 (11 mai 2026), branche 2.1.x, Opus 4.8 par défaut | AJOUT |
| OpenAI Codex | TECHNOLOGIE | capacités | Automations, worktrees, skills, sub-agents TOML, `/goal` (CLI 0.128.0) | AJOUT |
| /goal | TECHNOLOGIE | mécanisme | Travail jusqu'à condition vérifiable, notée par un modèle distinct | AJOUT |
| Git worktrees | TECHNOLOGIE | fonction | Isolation d'agents parallèles (répertoires/branches séparés, historique partagé) | AJOUT |
| Sub-agents maker-checker | METHODOLOGIE | fonction | Vérificateur adversarial gardant le travail avant revue humaine | AJOUT |
| MCP | TECHNOLOGIE | fonction | Protocole de connecteurs portables (Codex ↔ Claude Code) | AJOUT |
| Échelle de maturité | CONCEPT | niveaux | 0 Manuel → 1 Triage → 2 Draft → 3 Verified PR → 4 Auto-merge | AJOUT |
| Dette de compréhension | CONCEPT | risque | Le code part plus vite qu'on ne le comprend | AJOUT |
| Capitulation cognitive | CONCEPT | risque | Accepter les sorties de la boucle sans jugement | AJOUT |
| Lushbinary | ORGANISATION | secteur | Agence d'intégrations IA / workflows agentiques (santé, fintech, SaaS, e-commerce) | AJOUT |
