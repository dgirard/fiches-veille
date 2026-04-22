# trivedy-langchain-anatomy-agent-harness-2026-03-10

## Veille

Anatomie d'un harnais d'agent : Agent = Modèle + Harnais, composants fondamentaux et évolution des harnais LangChain

## Titre Article

The Anatomy of an Agent Harness

## Date

2026-03-10

## URL

https://blog.langchain.com/the-anatomy-of-an-agent-harness/

## Keywords

harnais d'agent, harness engineering, Agent = Modèle + Harnais, système de fichiers, sandbox, bash, exécution de code, mémoire, recherche, pourriture de contexte, compaction, exécution longue durée, Ralph Loop, planification, auto-vérification, co-évolution modèle-harnais, deepagents, LangChain, Terminal Bench

## Authors

Vivek Trivedy

## Ton

**Profil** : Perspective de développeur de framework, registre technique didactique, niveau intermédiaire à avancé. Vivek écrit comme un ingénieur qui décompose systématiquement un concept pour le rendre actionnable.

**Description** : Le ton est pédagogique et structuré, adoptant une démarche de dérivation logique : chaque composant du harnais est justifié en partant d'un comportement souhaité pour l'agent, puis en remontant vers la solution technique. L'article utilise un pattern récurrent "Behavior we want → Harness Design to help the model achieve this" qui rend la lecture progressive et compréhensible. Le style est technique mais accessible, avec des exemples concrets tirés de l'écosystème LangChain. L'auteur prend position sur l'avenir des harnais avec une vision nuancée : même si les modèles absorberont certaines fonctions du harnais, l'ingénierie de harnais restera utile car elle construit des systèmes autour de l'intelligence du modèle. Le public cible est constitué de développeurs construisant des agents IA.

## Pense-betes

- **Définition fondamentale** : Agent = Modèle + Harnais. "Si vous n'êtes pas le modèle, vous êtes le harnais." Le harnais = tout le code, la configuration et la logique d'exécution qui n'est pas le modèle lui-même
- **Composants du harnais** : prompts système, outils/Skills/MCP et leurs descriptions, infrastructure embarquée (filesystem, sandbox, navigateur), logique d'orchestration (subagents, handoffs, routage de modèles), hooks/middleware pour exécution déterministe (compaction, continuation, lint checks)
- **Système de fichiers** : primitive la plus fondamentale du harnais. Déverrouille : espace de travail, stockage incrémental, surface de collaboration multi-agents/humains. Git ajoute le versionnage
- **Bash + exécution de code** : outil généraliste plutôt que des outils pré-configurés pour chaque action. Le modèle conçoit ses propres outils à la volée via le code
- **Sandboxes** : environnements d'exécution sûrs et isolés. Déverrouillent la scalabilité (créés à la demande, détruits après). Les bons environnements incluent des outils par défaut (runtimes, CLI git, navigateurs)
- **Mémoire et recherche** : le filesystem comme primitive de mémoire (AGENTS.md chargé en contexte au démarrage). Web Search et MCP (ex: Context7) pour accéder aux connaissances au-delà du cutoff d'entraînement
- **Pourriture de contexte (Context Rot)** : dégradation de performance quand la fenêtre de contexte se remplit. Solutions : compaction (résumé intelligent), offloading des résultats d'outils, Skills comme progressive disclosure
- **Ralph Loop** : pattern de harnais qui intercepte la tentative de sortie du modèle via un hook et réinjecte le prompt original dans une fenêtre de contexte propre, forçant l'agent à continuer. Le filesystem permet cela car chaque itération part d'un contexte frais mais lit l'état de l'itération précédente
- **Auto-vérification** : hooks qui exécutent une suite de tests et boucle de retour vers le modèle en cas d'échec avec le message d'erreur
- **Co-évolution modèle-harnais** : les produits agents (Claude Code, Codex) sont post-entraînés avec modèle et harnais dans la boucle. Cela crée un overfitting (ex: changer la logique apply_patch dégrade la performance). Mais le meilleur harnais pour votre tâche n'est pas nécessairement celui avec lequel le modèle a été entraîné
- **Terminal Bench 2.0** : Opus 4.6 dans Claude Code score bien en dessous d'Opus 4.6 dans d'autres harnais. LangChain est passé du Top 30 au Top 5 en ne changeant que le harnais
- **Avenir** : certaines fonctions du harnais seront absorbées par les modèles, mais le harness engineering restera utile car il construit des systèmes autour de l'intelligence du modèle, pas seulement des patchs sur les déficiences
- **deepagents** : bibliothèque de LangChain pour améliorer la construction de harnais. Problèmes ouverts : orchestration de centaines d'agents en parallèle, agents analysant leurs propres traces, harnais assemblant dynamiquement les bons outils juste-à-temps

## RésuméDe400mots

Vivek Trivedy de LangChain propose une définition structurée du harnais d'agent : Agent = Modèle + Harnais. Le harnais englobe tout le code, la configuration et la logique d'exécution qui n'est pas le modèle lui-même, incluant prompts système, outils et MCP, infrastructure embarquée, logique d'orchestration et hooks déterministes.

L'article dérive chaque composant du harnais à partir des comportements souhaités que les modèles ne peuvent pas fournir nativement. Le **système de fichiers** est identifié comme la primitive la plus fondamentale : il offre un espace de travail, un stockage incrémental, et une surface de collaboration entre agents et humains. **Bash et l'exécution de code** fournissent un outil généraliste permettant au modèle de concevoir ses propres outils à la volée. Les **sandboxes** offrent des environnements d'exécution sûrs et scalables avec des outils par défaut pré-installés.

Pour la **mémoire**, le filesystem sert de primitive centrale via des fichiers standards comme AGENTS.md, chargés en contexte au démarrage et mis à jour entre sessions. La recherche web et les outils MCP (comme Context7) donnent accès aux connaissances au-delà du cutoff d'entraînement.

L'article identifie la **pourriture de contexte** (Context Rot) comme un défi majeur : les performances se dégradent quand la fenêtre de contexte se remplit. Les solutions incluent la compaction (résumé intelligent du contexte), l'offloading des résultats d'outils volumineux vers le filesystem, et les Skills comme mécanisme de progressive disclosure.

Pour l'**exécution longue durée**, les primitives précédentes se composent. Le **Ralph Loop** est un pattern qui intercepte la tentative de sortie du modèle et réinjecte le prompt dans un contexte propre, forçant la continuation du travail. La planification et l'auto-vérification (tests + boucle de correction) maintiennent l'agent sur la bonne trajectoire.

L'article explore la **co-évolution modèle-harnais** : les produits agents comme Claude Code et Codex sont post-entraînés avec leur harnais, créant un couplage (changer la logique d'un outil peut dégrader la performance). Cependant, le meilleur harnais pour une tâche n'est pas nécessairement celui d'entraînement — LangChain est passé du Top 30 au Top 5 sur Terminal Bench 2.0 en ne changeant que le harnais.

En conclusion, même si certaines fonctions du harnais seront absorbées par les modèles, le harness engineering restera pertinent car il construit des systèmes autour de l'intelligence du modèle. LangChain développe deepagents et explore l'orchestration massive d'agents, l'auto-analyse de traces, et l'assemblage dynamique de contexte juste-à-temps.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Vivek Trivedy | PERSONNE | a_écrit | The Anatomy of an Agent Harness | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Vivek Trivedy | PERSONNE | travaille_chez | LangChain | ORGANISATION | 0.95 | DYNAMIQUE | inféré |
| LangChain | ORGANISATION | développe | deepagents | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| LangChain | ORGANISATION | a_amélioré | Score Terminal Bench 2.0 de Top 30 à Top 5 | EVENEMENT | 0.92 | STATIQUE | déclaré_article |
| Harnais d'agent | CONCEPT | se_définit_comme | Tout sauf le modèle dans un agent | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| Système de fichiers | CONCEPT | est | Primitive la plus fondamentale du harnais | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Ralph Loop | METHODOLOGIE | intercepte | Tentative de sortie du modèle | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Context Rot | CONCEPT | dégrade | Performance de l'agent | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Compaction | CONCEPT | combat | Context Rot | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | est_post-entraîné_avec | Harnais dans la boucle | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Codex | TECHNOLOGIE | est_post-entraîné_avec | Harnais dans la boucle | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Opus 4.6 | TECHNOLOGIE | score_différemment_dans | Différents harnais | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Vivek Trivedy | PERSONNE | rôle | Auteur chez LangChain | AJOUT |
| LangChain | ORGANISATION | secteur | Framework IA / Agents | MISE_A_JOUR |
| deepagents | TECHNOLOGIE | catégorie | Bibliothèque de construction de harnais LangChain | AJOUT |
| Ralph Loop | METHODOLOGIE | définition | Pattern de harnais réinjectant le prompt dans un contexte propre pour forcer la continuation | AJOUT |
| Context Rot | CONCEPT | définition | Dégradation de performance de l'agent quand la fenêtre de contexte se remplit | AJOUT |
| Terminal Bench 2.0 | TECHNOLOGIE | catégorie | Benchmark pour agents de codage | AJOUT |
| Opus 4.6 | TECHNOLOGIE | catégorie | Modèle de langage Anthropic | AJOUT |
| Skills | CONCEPT | définition | Primitive de harnais pour progressive disclosure protégeant contre la pourriture de contexte | MISE_A_JOUR |
| Context7 | TECHNOLOGIE | catégorie | Outil MCP pour accès aux connaissances à jour | AJOUT |
