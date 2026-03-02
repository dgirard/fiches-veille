# Context Engineering — L'art de nourrir les agents IA
## Présentation 20 slides — ~30 minutes

---

## Slide 1 — Titre

# Context Engineering
### L'art de nourrir les agents IA

*Basé sur l'analyse de 34 fiches de veille — Mai 2025 / Février 2026*

---

## Slide 2 — Le paradoxe

# 80 % des prompts font moins de 100 mots

Aristidis Vasilopoulos — 283 sessions, 2 801 prompts, 70 jours

Pas parce que les développeurs sont paresseux.
Parce que **tout le travail a été fait en amont**.

---

## Slide 3 — Le vrai goulot d'étranglement

# Ce n'est plus le code. C'est le contexte.

> « Chaque session est un nouvel employé — sans mémoire musculaire ni conversations de couloir. »
> — Patrick Debois, inventeur du terme DevOps

Pendant des décennies : optimiser comment les humains écrivent du code.
Maintenant : optimiser le contexte que les agents consomment.

---

## Slide 4 — Prompt Engineering vs Context Engineering

| | Prompt Engineering | Context Engineering |
|---|---|---|
| **Optimise** | Une interaction | L'environnement de toutes les interactions |
| **Durée de vie** | Éphémère (1 session) | Persistant (cross-sessions) |
| **Échelle** | Artisanal | Industriel |
| **Retour** | Linéaire | Composé |

---

# PARTIE 1 — L'ARCHITECTURE
## Vasilopoulos : la preuve par les données

---

## Slide 5 — L'étude : 283 sessions

| Métrique | Valeur |
|----------|--------|
| Durée | 70 jours |
| Codebase | 108 000 lignes C# (système distribué) |
| Sessions | 283 |
| Prompts humains | 2 801 |
| Tours autonomes | 16 522 |
| Infrastructure contextuelle | 24,2 % de la documentation totale |

L'une des évaluations quantitatives les plus détaillées du développement assisté par agents IA.

---

## Slide 6 — Tier 1 : Constitution (Hot Memory)

### 1 fichier Markdown — 660 lignes — toujours chargé

Contient :
- Conventions de nommage
- Commandes de build
- Patterns architecturaux
- Modes de défaillance connus
- **Tables de routage** vers agents spécialisés

> « Une constitution basique améliore l'output dès le jour 1. »

---

## Slide 7 — Tier 2 : Agents spécialisés (Warm Memory)

### 19 agents — 9 300 lignes

- Plus de 50 % du contenu = **faits codebase** (formules, patterns, modes de défaillance)
- Pas d'instructions comportementales — de la connaissance pure

**Top agents invoqués :**
| Agent | Invocations |
|-------|-------------|
| Code reviewer | 154 |
| Network-protocol-designer | 85 |

→ Contrôle qualité et correction domain-specific dominent.

---

## Slide 8 — Tier 3 : Knowledge Base (Cold Memory)

### 34 documents — 16 250 lignes — via MCP

**Études de cas :**

| Cas | Résultat |
|-----|----------|
| Spec sauvegarde (283 lignes, 74 sessions) | **Zéro bug de corruption** |
| Agent réseau (915 lignes) | 3 bugs subtils identifiés après 5 tentatives échouées |
| Patterns synchronisation UI | Réussite au **premier essai** sur la feature suivante |
| Spec système de drop | Accélération de **dizaines** d'interactions ultérieures |

---

## Slide 9 — Les 3 guidelines à retenir

### 1. Constitution basique = gains immédiats
Pas besoin de perfection pour commencer.

### 2. Explication répétée = spec à écrire
Si vous expliquez la même chose deux fois, documentez-le.

### 3. Spec obsolète = pire que rien
Le principal mode de défaillance. Un contexte périmé induit activement en erreur.

**Coût de maintenance : 1-2 heures par semaine.**

---

# PARTIE 2 — LE CYCLE DE VIE
## Debois : le cadre méthodologique

---

## Slide 10 — Le CDLC en 4 phases

```
    ┌──────────┐
    │ GÉNÉRER  │ ← Rendre l'implicite explicite
    └────┬─────┘
         ↓
    ┌──────────┐
    │ ÉVALUER  │ ← TDD pour le contexte
    └────┬─────┘
         ↓
    ┌────────────┐
    │ DISTRIBUER │ ← Contexte comme package versionné
    └────┬───────┘
         ↓
    ┌──────────┐
    │ OBSERVER │ ← Boucle feedback en production
    └────┬─────┘
         ↓
    (retour à GÉNÉRER)
```

**Context Development Lifecycle** — Patrick Debois (Tessl)

---

## Slide 11 — Générer + Évaluer

### Générer : 3 niveaux de contexte

| Niveau | Exemples | Fourni par les équipes ? |
|--------|----------|-------------------------|
| Technique | Standards, patterns architecturaux | Souvent |
| Projet | Priorités, scope, timelines | Rarement |
| Business | Conformité, attentes client | Presque jamais |

### Évaluer : le TDD du contexte

> « Un échec d'évaluation n'est pas un défaut de l'agent — c'est une spécification non écrite. »

Scénarios définis → sorties évaluées statistiquement → contexte amélioré.

---

## Slide 12 — Distribuer + Observer

### Distribuer

Le contexte comme package versionné et sécurisé.

> « For the first time, there's a selfish reason to share knowledge. »

Partager le contexte améliore **ses propres** interactions avec les agents.

⚠️ Le contexte est aussi une **surface d'attaque** — même posture de sécurité que les dépendances.

### Observer

Les agents révèlent les lacunes par leurs questions et choix inattendus.
Ces signaux alimentent le cycle suivant.

---

## Slide 13 — Le Context Flywheel

```
Documenter le contexte
    → Les agents produisent mieux
        → L'output enrichit le contexte
            → Le contexte compose et accélère
                → (boucle vertueuse)
```

⚠️ Des fenêtres de contexte infinies ne résolvent pas le problème :
plus de contexte = plus de contradictions.
Le défi passe de la **curation** à la **gouvernance**.

---

# PARTIE 3 — LA PRATIQUE
## Shipper & Klaassen : le terrain

---

## Slide 14 — Compound Engineering

# Chaque feature rend la suivante *plus facile*

En ingénierie traditionnelle : chaque feature rend la suivante **plus difficile**.

En compound engineering : une boucle d'apprentissage documentée
fait que chaque bug, test échoué et insight **accélère** le cycle suivant.

> « 1 développeur avec IA = 5 développeurs d'il y a quelques années. »
> — Dan Shipper, CEO Every

---

## Slide 15 — La boucle Plan-Work-Assess-Compound

```
┌──────────────────────────────────────────────┐
│                                              │
│   PLAN ████████████████████  40%             │
│                                              │
│   WORK █████                 10%             │
│                                              │
│   ASSESS ██████████████████  40%             │
│                                              │
│   COMPOUND █████             10%             │
│                                              │
└──────────────────────────────────────────────┘
```

**80 % = Plan + Assess.** Le codage = 10 %.

Le contexte mange le code.

---

## Slide 16 — L'étape Compound : le secret

> « This is the money step. » — Dan Shipper

Après chaque cycle :
1. L'agent **résume** les leçons apprises
2. Les leçons sont **stockées dans le codebase**
3. Elles sont **automatiquement distribuées** à toute l'équipe

Résultat : un new hire est aussi bien armé qu'un vétéran.

**Questions de routage (agent Cora) :**
- Où est-ce que ça va dans le système ?
- Faut-il ajouter à l'existant ou créer quelque chose de nouveau ?
- A-t-on déjà résolu un problème similaire ?

---

## Slide 17 — Every en chiffres

| Métrique | Valeur |
|----------|--------|
| Produits | 5 (Cora, Spiral, Sparkle, Monologue...) |
| Dev par produit | **1 personne** |
| Utilisateurs | Milliers quotidiennement |
| Subagents de review | 12 en parallèle |
| Code écrit par agents | **100 %** |
| Plugin | Open source (Claude Code) |

---

# SYNTHÈSE

---

## Slide 18 — Trois visions, une convergence

| | Vasilopoulos | Debois | Shipper & Klaassen |
|---|---|---|---|
| **Approche** | Étude empirique | Cadre méthodologique | Pratique de terrain |
| **Le contexte compose** | Mesuré (chaque spec accélère les features adjacentes) | Théorisé (Context Flywheel) | Démontré (étape Compound) |
| **Le problème = le contexte** | "Explication répétée = spec à écrire" | "Échec d'éval = spec non écrite" | "Planifier enseigne au système" |
| **Partage incitatif** | 1-2h/semaine de maintenance | "Selfish reason to share" | Leçons dans le codebase |

---

## Slide 19 — Par où commencer ?

### Action 1 — Créer un CLAUDE.md
Conventions, patterns, commandes de build. 50 lignes suffisent pour le jour 1.

### Action 2 — Observer les explications répétées
Si vous expliquez la même chose deux fois à un agent, transformez-le en spec.

### Action 3 — Documenter une leçon après chaque session
10 minutes. C'est l'étape Compound. Le volant d'inertie démarre ici.

---

## Slide 20 — Conclusion

# Le contexte est un actif, pas une dépense.

L'ingénieur de demain ne sera pas celui qui écrit le meilleur code.
Ce sera celui qui structure le meilleur contexte.

**De la syntaxe → vers la sémantique**
**Du prompt → vers le système**
**De l'interaction → vers l'architecture**

---

## Sources principales

- Vasilopoulos, *Codified Context: Infrastructure for AI Agents in a Complex Codebase*, arXiv, février 2026
- Debois, *The Context Development Lifecycle*, Tessl, février 2026
- Shipper & Klaassen, *Compound Engineering: How Every Codes With Agents*, Every, décembre 2025

+ 31 fiches de veille complémentaires (mai 2025 — février 2026)
