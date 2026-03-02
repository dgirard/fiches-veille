# Context Engineering — L'art de nourrir les agents IA
## Présentation 15 slides — ~30 minutes

---

## Slide 1 — Titre

# Context Engineering
### L'art de nourrir les agents IA

*Trois contributions majeures — une étude empirique, un cycle de vie, une méthodologie de terrain.*

---

## Slide 2 — Le paradoxe

# 80 % des prompts font moins de 100 mots

Vasilopoulos — 283 sessions, 2 801 prompts, 70 jours

Pas parce que les développeurs sont paresseux.
Parce que **tout le travail a été fait en amont**.

Le contexte est déjà là — chargé, structuré, prêt à être consommé.
L'infrastructure contextuelle = 24,2 % de la documentation totale.

---

## Slide 3 — Le goulot a changé

# Ce n'est plus le code. C'est le contexte.

> « Chaque session est un nouvel employé — sans mémoire musculaire ni conversations de couloir. »
> — Patrick Debois, inventeur du terme DevOps

Pendant des décennies : optimiser comment les humains écrivent du code.
Waterfall → Agile → DevOps → Platform Engineering.

Maintenant : **les agents écrivent le code.**
Le nouveau goulot = la qualité du contexte.

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
## Vasilopoulos : la preuve empirique

---

## Slide 5 — Trois tiers de mémoire

```
┌─────────────────────────────────────────────┐
│  TIER 3 — Cold Memory (Knowledge Base)      │
│  Savoir de référence, tiré quand nécessaire │
│  Spécifications détaillées, documentation   │
├─────────────────────────────────────────────┤
│  TIER 2 — Warm Memory (Experts de domaine)  │
│  Invoqués à la demande                      │
│  Faits codebase > instructions comportement │
├─────────────────────────────────────────────┤
│  TIER 1 — Hot Memory (Constitution)         │
│  Toujours chargé                            │
│  Conventions, patterns, tables de routage   │
└─────────────────────────────────────────────┘
```

Chaque tier = un type de mémoire, une fréquence d'accès.

**Principe : une constitution basique améliore l'output dès le jour 1.**

---

## Slide 6 — Ce que les données montrent

### L'étude : 283 sessions, 16 522 tours autonomes

- Le contrôle qualité et la correction domain-specific **dominent** les usages
- Plus de 50 % du contenu des agents spécialisés = **faits**, pas instructions
- Chaque sous-système documenté accélère **ses propres modifications ET les features adjacentes**
- Specs bien maintenues → résultats sans erreur là où les tentatives sans contexte **échouaient répétitivement**

### Le principal mode de défaillance :
**Les specs obsolètes.** Un contexte périmé induit activement en erreur.

**Coût de maintenance : 1-2 heures par semaine.**

---

# PARTIE 2 — LE CYCLE DE VIE
## Debois : le cadre méthodologique

---

## Slide 7 — Le CDLC en 4 phases

```
         ┌──────────┐
    ┌───→│ GÉNÉRER  │───┐
    │    └──────────┘   │
    │    Rendre          │
    │    l'implicite     ↓
┌──────────┐      ┌──────────┐
│ OBSERVER │      │ ÉVALUER  │
└──────────┘      └──────────┘
    ↑    Boucle          │
    │    feedback         │
    │    production       ↓
    │    ┌────────────┐  │
    └────│ DISTRIBUER │←─┘
         └────────────┘
```

**Context Development Lifecycle** — le contexte traité comme un artefact d'ingénierie.

---

## Slide 8 — Générer + Évaluer

### Générer : 3 niveaux de contexte

| Niveau | Contenu | Fourni ? |
|--------|---------|----------|
| **Technique** | Standards, patterns architecturaux | Souvent |
| **Projet** | Priorités, scope, timelines | Rarement |
| **Business** | Conformité, attentes client | Presque jamais |

**Le contexte pourrit et entre en conflit.**
Il ne suffit pas de documenter — il faut gérer fraîcheur et cohérence.

### Évaluer : le TDD du contexte

> « Un échec d'évaluation n'est pas un défaut de l'agent — c'est une spécification non écrite. »

Le problème est rarement le modèle. C'est le contexte incomplet.

---

## Slide 9 — Distribuer + Observer

### Distribuer — le contexte comme package

Versionné. Sécurisé. Audité.

> « For the first time, there's a selfish reason to share knowledge. »

Partager le contexte améliore **ses propres** interactions avec les agents.

⚠️ Le contexte est aussi une **surface d'attaque** — même posture de sécurité que les dépendances.

### Observer — la boucle se ferme

Les agents révèlent les lacunes par leurs questions et choix inattendus.

⚠️ Fenêtres de contexte infinies ≠ solution.
Plus de contexte = plus de contradictions.
Le défi passe de la **curation** à la **gouvernance**.

---

# PARTIE 3 — LA PRATIQUE
## Shipper & Klaassen : l'inversion de la complexité

---

## Slide 10 — Compound Engineering

# Chaque feature rend la suivante *plus facile*

**Ingénierie traditionnelle :**
Feature → dette technique → complexité croissante → chaque ajout coûte plus cher

**Compound Engineering :**
Feature → boucle d'apprentissage → contexte enrichi → chaque ajout coûte moins cher

Le secret : une boucle documentée qui transforme chaque bug,
test échoué et insight en **investissement** pour les cycles suivants.

Estimation : 1 développeur bien outillé = 5 développeurs d'il y a quelques années.
Non pas en codant plus vite — en structurant mieux le contexte.

---

## Slide 11 — Plan-Work-Assess-Compound

```
┌──────────────────────────────────────────────┐
│                                              │
│   PLAN ████████████████████  40%             │
│   Recherche, planification, contexte         │
│                                              │
│   WORK █████                 10%             │
│   Exécution du plan                          │
│                                              │
│   ASSESS ██████████████████  40%             │
│   Évaluation multi-perspective               │
│                                              │
│   COMPOUND █████             10%             │
│   Leçons résumées et stockées                │
│                                              │
└──────────────────────────────────────────────┘
```

**80 % = Plan + Assess.** L'exécution = 10 %.

Le contexte mange le code.

La documentation n'est plus un coût — c'est le **carburant** de la productivité.

---

# SYNTHÈSE

---

## Slide 12 — Trois visions, une convergence

| | Vasilopoulos | Debois | Shipper & Klaassen |
|---|---|---|---|
| **Approche** | Étude empirique | Cadre méthodologique | Pratique de terrain |
| **Le contexte compose** | Mesuré : chaque spec accélère les features adjacentes | Théorisé : Context Flywheel | Démontré : étape Compound |
| **Le problème = le contexte** | "Explication répétée = spec à écrire" | "Échec d'éval = spec non écrite" | "Planifier enseigne au système" |
| **Partage incitatif** | 1-2h/semaine de maintenance | "Selfish reason to share" | Leçons dans le codebase, new hire = vétéran |

Trois chemins indépendants, mêmes conclusions.

---

## Slide 13 — Les 5 principes

### 1. Le goulot a changé
Ce n'est plus le code, c'est le contexte.

### 2. Le contexte est un artefact d'ingénierie
Il se conçoit, se teste, se versionne, se sécurise et se maintient.

### 3. Le contexte compose
Chaque investissement accélère les cycles suivants — la complexité devient décroissante.

### 4. Le problème est toujours le contexte, jamais l'agent
L'échec d'un agent est le symptôme d'une spécification absente.

### 5. Le partage est naturellement incitatif
Documenter le contexte sert directement celui qui le documente.

---

## Slide 14 — Le volant d'inertie

```
Documenter le contexte
    → Les agents produisent mieux
        → L'output enrichit le contexte
            → Le contexte compose et accélère
                → (boucle vertueuse)
```

**Coût d'entrée** : 1-2 heures par semaine

**Retour** : composé — la valeur s'accumule à chaque session

Le volant, une fois lancé, s'auto-alimente.

---

## Slide 15 — Conclusion

# Le contexte est un actif, pas une dépense.

L'ingénieur de demain ne sera pas celui qui écrit le meilleur code.
Ce sera celui qui structure le meilleur contexte.

**De la syntaxe → vers la sémantique**
**Du prompt → vers le système**
**De l'interaction → vers l'architecture**

---

## Sources

- Vasilopoulos, *Codified Context: Infrastructure for AI Agents in a Complex Codebase*, arXiv, février 2026
- Debois, *The Context Development Lifecycle*, Tessl, février 2026
- Shipper & Klaassen, *Compound Engineering: How Every Codes With Agents*, Every, décembre 2025
