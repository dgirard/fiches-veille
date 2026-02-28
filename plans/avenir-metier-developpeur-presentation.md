# L'Avenir du Métier de Développeur à l'Ère de l'IA

## Plan de Présentation

**Durée estimée** : 30-45 minutes
**Public cible** : Développeurs, managers tech, décideurs IT
**Sources** : 53 fiches de veille technologique (2023-2026)

---

## Structure Narrative : Le Voyage du Développeur

### Arc narratif
Le développeur traverse une transformation comparable à celle des artisans lors de la révolution industrielle : non pas une disparition, mais une redéfinition profonde du métier. De "celui qui écrit du code" à "celui qui orchestre des systèmes intelligents".

---

## 1. INTRODUCTION : Le Moment Historique (5 min)

### 1.1 La Pierre Philosophale Réalisée
> "AI is the process of transmuting sand into thought"
> — Marc Andreessen, Lenny Podcast 2026

**Point clé** : L'IA réalise littéralement le rêve alchimiste - transformer le silicium (sable) en pensée. C'est la transformation la plus fondamentale de l'histoire de l'informatique.

**Source** : [andreessen-lenny-podcast-ai-jobs-agi-2026-02.md](../fiches/2026-02/andreessen-lenny-podcast-ai-jobs-agi-2026-02.md)

### 1.2 Le Timing Providentiel
- La force de travail mondiale commence à décliner
- L'IA arrive précisément à ce moment
- Ce n'est pas une menace mais une solution à une pénurie structurelle

### 1.3 La Question Centrale
> "Si vous ne comprenez pas comment écrire du code vous-même, vous ne pouvez pas évaluer ce que l'IA vous donne."
> — Marc Andreessen

**Transition** : Alors, qu'advient-il vraiment du développeur ?

---

## 2. ÉTAT DES LIEUX : Ce Qui Change Réellement (8 min)

### 2.1 Les Chiffres Qui Comptent

| Métrique | Valeur | Source |
|----------|--------|--------|
| Productivité multipliée | 10x à 1000x | Andreessen 2026 |
| Part du travail par IA (Salesforce) | 30-50% | Benioff 2025 |
| Force de travail remplaçable (MIT) | 11.7% ($1.2T) | MIT Iceberg Index |
| Gains de vitesse (FAANG) | +30% | Osmani 2025 |

**Sources** :
- [andreessen-ai-coding-programmers-redefined-orchestrating-bots-2026-02.md](../fiches/2026-02/andreessen-ai-coding-programmers-redefined-orchestrating-bots-2026-02.md)
- [mit-iceberg-index-ai-workforce-impact-cnbc-2025-11-26.md](../fiches/2025-11/mit-iceberg-index-ai-workforce-impact-cnbc-2025-11-26.md)

### 2.2 L'Iceberg du MIT : Ce Qu'on Ne Voit Pas
- **Visible (2.2%)** : Jobs tech/IT traditionnels
- **Caché (9.5%)** : Fonctions routinières dans tous secteurs (HR, logistique, finance, admin)
- **Impact national** : Pas seulement les hubs tech côtiers

**Source** : [mit-iceberg-index-ai-workforce-impact-cnbc-2025-11-26.md](../fiches/2025-11/mit-iceberg-index-ai-workforce-impact-cnbc-2025-11-26.md)

### 2.3 Exemple Concret : Migration CMS
- **Projet** : Migration cursor.com de CMS vers code
- **Durée** : 3 jours
- **Coût tokens** : $260
- **Résultat** : 344 requêtes agent, 67 commits, +43K/-322K lignes
- **Économies** : $56,848 en coûts CDN

**Source** : [robinson-coding-agents-complexity-budgets-cursor-2025-12.md](../fiches/2025-12/robinson-coding-agents-complexity-budgets-cursor-2025-12.md)

---

## 3. LA NOUVELLE DÉFINITION DU MÉTIER (10 min)

### 3.1 Du Codeur à l'Orchestrateur

```
AVANT                          APRÈS
─────                          ─────
Écrire du code                 Orchestrer des bots
Ligne par ligne                10 agents en parallèle
Exécuter                       Superviser
Produire                       Évaluer et corriger
```

> "Le job n'est plus de taper du code ligne par ligne. C'est d'orchestrer 10 bots de codage en parallèle, d'argumenter avec eux, de débugger leur output, de modifier les specs, et de les pousser vers le bon résultat."
> — Marc Andreessen

**Source** : [andreessen-ai-coding-programmers-redefined-orchestrating-bots-2026-02.md](../fiches/2026-02/andreessen-ai-coding-programmers-redefined-orchestrating-bots-2026-02.md)

### 3.2 Les Deux Paradigmes d'Addy Osmani

#### Mode Conductor (Synchrone)
- Interaction étroite avec un agent
- Boucles de feedback continues
- Validation temps réel
- **Outils** : Claude Code, Cursor, VSCode Copilot

#### Mode Orchestrator (Asynchrone)
- Délégation de tâches complètes
- Agents autonomes en parallèle
- Supervision et intégration
- **Outils** : GitHub Copilot Agent, Google Jules

**Compétence clé** : Maîtriser les deux modes selon le contexte

**Source** : [osmani-conductors-orchestrators-agentic-coding-2025-11-01.md](../fiches/2025-11/osmani-conductors-orchestrators-agentic-coding-2025-11-01.md)

### 3.3 Les Trois Catégories de Yves Caseau

| Profil | Description | Compétences |
|--------|-------------|-------------|
| **Computer System Engineers** | Backbone du code, assistés par IA | Fondamentaux solides, architecture |
| **Solutions Engineers** | Programmation en langage naturel | Orchestration agents, spécifications |
| **Citizen Developers** | Accès aux systèmes sans expertise IT | Compréhension métier, prompt engineering |

**Point crucial** : La programmation ne disparaît pas, elle se stratifie.

**Source** : [caseau-evolution-developpeur-ia-generative-2025-11-05.md](../fiches/2025-11/caseau-evolution-developpeur-ia-generative-2025-11-05.md)

---

## 4. LE PARADOXE DES FONDAMENTAUX (7 min)

### 4.1 L'Ironie Soulignée par Andreessen
> "Les meilleurs programmeurs aujourd'hui passent leur journée à sauter entre terminaux, gérer plusieurs bots de codage, corriger des erreurs et affiner des instructions. Pourtant, ils ont toujours besoin de fondamentaux solides, car sans eux, il est impossible de savoir quand l'IA se trompe."

**Le paradoxe** : Plus l'IA code à votre place, plus vous devez comprendre le code pour l'évaluer.

### 4.2 Les 4 Principes Karpathy pour Claude Code

```markdown
1. THINK BEFORE CODING
   → Hypothèses explicites, questions clarificatrices, approches multiples

2. SIMPLICITY FIRST
   → Code minimal, pas de features spéculatives, pas d'abstractions inutiles

3. SURGICAL CHANGES
   → Modifier uniquement ce qui est demandé, préserver le style existant

4. GOAL-DRIVEN EXECUTION
   → Définir des critères de succès vérifiables, pas des instructions impératives
```

**Insight clé** : "Les modèles excellent à boucler jusqu'à atteindre un objectif spécifique" - définir le succès plutôt que la méthode.

**Source** : [forrestchang-andrej-karpathy-skills-claude-code-2026-01-27.md](../fiches/2026-01/forrestchang-andrej-karpathy-skills-claude-code-2026-01-27.md)

### 4.3 Le "Curse of Instructions" d'Osmani
- Trop de règles simultanées = dégradation de l'adhérence IA
- **Solution** : Specs séparées, sous-agents spécialisés, agents parallèles
- **Structure** : SPEC_backend.md, SPEC_frontend.md, etc.

**Source** : [osmani-how-write-good-spec-ai-agents-2026-01-13.md](../fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13.md)

---

## 5. STOP CODING, START PLANNING (7 min)

### 5.1 La Thèse de Kieran Klaassen
> "L'IA nous a rendus négligents parce qu'elle nous a fait oublier comment planifier."

### 5.2 Le Framework "Three Fidelities"

| Fidélité | Type de tâche | Approche |
|----------|---------------|----------|
| **One** | One-liners, typos, bugs évidents | Exécution directe |
| **Two** | Multi-fichiers, scope clair, implémentation non-évidente | **ROI maximal de la planification** |
| **Three** | Features majeures, incertitude élevée | Vibe planning + planification rigoureuse |

### 5.3 La Capitalisation des Connaissances
> "Les plans enseignent aux systèmes ; le code résout les problèmes."

- 50+ revues de plans = le système apprend vos préférences architecturales
- Les plans persistent, les prototypes sont jetés
- **Compounding engineering** : La recherche parallèle enseigne les connaissances institutionnelles plus vite que la planification séquentielle humaine

**Source** : [klaassen-stop-coding-start-planning-every-2025-11-06.md](../fiches/2025-11/klaassen-stop-coding-start-planning-every-2025-11-06.md)

### 5.4 Les 8 Stratégies de Planification Senior

1. **Reproduire & documenter** les bugs avant de fixer
2. **S'ancrer dans les bonnes pratiques** (recherche web, patterns architecturaux)
3. **S'ancrer dans le codebase** (patterns existants, DRY)
4. **S'ancrer dans les librairies** (lire le code source pour fonctionnalités non-documentées)
5. **Étudier l'historique git** (comprendre les décisions, éviter de réintroduire des bugs)
6. **Vibe prototype** pour clarifier l'UX (prototypes jetables → specs concrètes)
7. **Synthétiser les options** (2-3 approches avec tradeoffs honnêtes)
8. **Review avec agents de style** (simplification, sécurité, préférences personnelles)

**ROI pratique** : 20 min de recherche économisent des heures de debugging.

**Source** : [klaassen-teach-ai-think-senior-engineer-every-2025-11-07.md](../fiches/2025-11/klaassen-teach-ai-think-senior-engineer-every-2025-11-07.md)

---

## 6. L'IMPACT ORGANISATIONNEL (5 min)

### 6.1 Le Problème McKinsey
- **Observation** : Gains individuels spectaculaires (10x) ne se traduisent pas en gains d'équipe (5-15% max)
- **Nouveaux goulots** : Explosion des code reviews, gaps de collaboration, dette technique

### 6.2 La Transition vers les "AI Native Workflows"

| Avant | Après |
|-------|-------|
| Story-driven development | **Spec-driven development** |
| Planification trimestrielle | Planification continue |
| Équipes "Two pizza" (8-10) | **Pods "One pizza" (3-5)** |
| Rôles séparés QA/Dev/Ops | Rôles consolidés via IA |
| PM écrit des specs | **PM prototype directement** |

### 6.3 L'Alerte McKinsey
> "70% des entreprises n'ont pas mis à jour les descriptions de poste."

**Source** : [harrison-maniar-mckinsey-reshaping-software-delivery-agents-2025-11-23.md](../fiches/2025-11/harrison-maniar-mckinsey-reshaping-software-delivery-agents-2025-11-23.md)

### 6.4 Le Modèle de Compensation 10x
- **Problème** : La compensation traditionnelle ne récompense pas la productivité 10x
- **Solution** : Payer les ingénieurs comme des commerciaux (outcome-based sur Story Points)
- **Résultat** : Équipes livrant 2-3x plus de features, meilleure qualité

**Source** : [hezarkhani-10x-paying-engineers-salespeople-2025-11-23.md](../fiches/2025-11/hezarkhani-10x-paying-engineers-salespeople-2025-11-23.md)

---

## 7. LES MISES EN GARDE (3 min)

### 7.1 La Perspective Martin Fowler
> "Bien sûr que c'est une bulle - comme les canaux, les chemins de fer, internet."

- Les hallucinations sont une **feature**, pas un bug (LLMs les produisent par nature)
- Le **non-déterminisme** entre dans l'ingénierie logicielle pour la première fois
- **Surface d'attaque massive** : données privées + contenu non-fiable + exfiltration

**Source** : [martin-fowler-llm-software-development-2025-08-15.md](../fiches/2025-08/martin-fowler-llm-software-development-2025-08-15.md)

### 7.2 Les Limites du Langage Naturel (Caseau)
> "Parfois spécifier = autant de travail que programmer"

- Chaque niveau d'abstraction historique atteint ses limites
- Assembly → C, Procédural → OO, maintenant Langage naturel
- Le mythe : "Écrire devient facile". La réalité : "Maintenir reste dépendant du contexte"

### 7.3 Le "Mexican Standoff" Produit
- **PM** : "J'en ai besoin pour la semaine prochaine"
- **Ingénieur** : "C'est très dur, ça prendra une éternité"
- **Designer** : "Si c'est pas beau, je ne signe pas"
- **Résultat** : Personne ne gagne. Les projets meurent.

L'IA n'élimine pas ce conflit humain fondamental.

**Source** : [andreessen-lenny-podcast-ai-jobs-agi-2026-02.md](../fiches/2026-02/andreessen-lenny-podcast-ai-jobs-agi-2026-02.md)

---

## 8. CONCLUSION : LE PROFIL DU DÉVELOPPEUR DE DEMAIN (5 min)

### 8.1 Les 8 Caractéristiques Émergentes

```
┌─────────────────────────────────────────────────────┐
│  LE DÉVELOPPEUR 2026+                               │
├─────────────────────────────────────────────────────┤
│ 1. Planifie méticuleusement (ne code pas d'abord)   │
│ 2. Orchestre des agents (n'écrit pas de lignes)     │
│ 3. Spécifie clairement ("specification engineer")   │
│ 4. Comprend les fondamentaux (pour évaluer l'IA)    │
│ 5. Maîtrise les deux modes (Conductor + Orchestrator)│
│ 6. Capitalise les connaissances institutionnelles   │
│ 7. Se concentre sur le "pourquoi" pas le "comment"  │
│ 8. Reste adaptable (outils évoluent rapidement)     │
└─────────────────────────────────────────────────────┘
```

### 8.2 Le Message Final

> "Le programmeur du futur n'est pas remplacé par l'IA - il est **augmenté** par elle. Il reste nécessaire d'apprendre à écrire et comprendre le code, car quand l'IA se trompe, ce sont les humains qui doivent savoir pourquoi."
> — Marc Andreessen

### 8.3 L'Optimisme Déterminé
- Croire en un futur meilleur
- Mais **travailler activement** pour le créer
- Il n'arrive pas tout seul

---

## ANNEXE : Sources Principales

### Fiches Veille Référencées

| Thème | Fiche | Auteur |
|-------|-------|--------|
| Orchestration | [andreessen-ai-coding-programmers-redefined-orchestrating-bots-2026-02](../fiches/2026-02/andreessen-ai-coding-programmers-redefined-orchestrating-bots-2026-02.md) | Marc Andreessen |
| Vision globale | [andreessen-lenny-podcast-ai-jobs-agi-2026-02](../fiches/2026-02/andreessen-lenny-podcast-ai-jobs-agi-2026-02.md) | Lenny/Andreessen |
| Paradigmes | [osmani-conductors-orchestrators-agentic-coding-2025-11-01](../fiches/2025-11/osmani-conductors-orchestrators-agentic-coding-2025-11-01.md) | Addy Osmani |
| Évolution rôles | [caseau-evolution-developpeur-ia-generative-2025-11-05](../fiches/2025-11/caseau-evolution-developpeur-ia-generative-2025-11-05.md) | Yves Caseau |
| Principes | [forrestchang-andrej-karpathy-skills-claude-code-2026-01-27](../fiches/2026-01/forrestchang-andrej-karpathy-skills-claude-code-2026-01-27.md) | Andrej Karpathy |
| Planification | [klaassen-stop-coding-start-planning-every-2025-11-06](../fiches/2025-11/klaassen-stop-coding-start-planning-every-2025-11-06.md) | Kieran Klaassen |
| Stratégies | [klaassen-teach-ai-think-senior-engineer-every-2025-11-07](../fiches/2025-11/klaassen-teach-ai-think-senior-engineer-every-2025-11-07.md) | Kieran Klaassen |
| Specs | [osmani-how-write-good-spec-ai-agents-2026-01-13](../fiches/2026-01/osmani-how-write-good-spec-ai-agents-2026-01-13.md) | Addy Osmani |
| Organisation | [harrison-maniar-mckinsey-reshaping-software-delivery-agents-2025-11-23](../fiches/2025-11/harrison-maniar-mckinsey-reshaping-software-delivery-agents-2025-11-23.md) | McKinsey |
| Compensation | [hezarkhani-10x-paying-engineers-salespeople-2025-11-23](../fiches/2025-11/hezarkhani-10x-paying-engineers-salespeople-2025-11-23.md) | 10x |
| ROI | [robinson-coding-agents-complexity-budgets-cursor-2025-12](../fiches/2025-12/robinson-coding-agents-complexity-budgets-cursor-2025-12.md) | Lee Robinson |
| Workforce | [mit-iceberg-index-ai-workforce-impact-cnbc-2025-11-26](../fiches/2025-11/mit-iceberg-index-ai-workforce-impact-cnbc-2025-11-26.md) | MIT |
| Prudence | [martin-fowler-llm-software-development-2025-08-15](../fiches/2025-08/martin-fowler-llm-software-development-2025-08-15.md) | Martin Fowler |

---

## Notes pour le Présentateur

### Accroches possibles
- "Le développeur de 2026 ne code plus - il orchestre"
- "L'IA a réalisé le rêve des alchimistes : transformer le sable en pensée"
- "Plus l'IA code à votre place, plus vous devez comprendre le code"

### Questions pour le public
1. "Combien d'entre vous utilisent déjà Claude Code ou Cursor quotidiennement ?"
2. "Qui a déjà 'argumenté' avec une IA sur un choix de design ?"
3. "Votre organisation a-t-elle mis à jour les descriptions de poste ?"

### Slides visuelles suggérées
- Diagramme Conductor vs Orchestrator
- Graphique 10x → 1000x productivity
- Pyramide des 3 profils Caseau
- Timeline "Du code à l'orchestration"

---

*Plan créé à partir de 53 fiches de veille technologique - Février 2026*
