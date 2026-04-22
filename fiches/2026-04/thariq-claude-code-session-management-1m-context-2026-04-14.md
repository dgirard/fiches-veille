# thariq-claude-code-session-management-1m-context-2026-04-14

## Veille

Gestion de sessions Claude Code : fenêtre 1M tokens, compaction, rewind, subagents et pourriture de contexte

## Titre Article

Using Claude Code: Session Management & 1M Context

## Date

2026-04-14

## URL

https://x.com/trq212/status/2044548257058328723

## Keywords

Claude Code, gestion de sessions, fenêtre de contexte, 1 million de tokens, compaction, rewind, subagents, pourriture de contexte, context rot, pollution de contexte, bonnes pratiques, productivité agents de codage

## Authors

Thariq (@trq212)

## Ton

**Profil** : Perspective d'ingénieur Anthropic, registre technique pratique, niveau intermédiaire. Thariq écrit comme un praticien qui partage des enseignements tirés de conversations avec des utilisateurs.

**Description** : Le ton est celui d'un guide pratique conversationnel, direct et accessible. L'auteur s'appuie sur son expérience de terrain ("in my recent calls with Claude Code users") pour structurer des conseils concrets. Le style est didactique sans être condescendant, alternant entre explications de concepts (context rot, compaction) et recommandations actionnables (quand utiliser rewind vs compact vs clear). Les exemples sont concrets et tirés de cas d'usage réels (debugging, documentation, refactoring auth). Le public cible est constitué d'utilisateurs de Claude Code qui veulent optimiser leur workflow quotidien. Le ton reste nuancé, reconnaissant les zones grises et les compromis plutôt que d'imposer des règles rigides.

## Pense-betes

- **Fenêtre de contexte 1M tokens** : tout ce que le modèle peut "voir" en même temps (system prompt, conversation, tool calls, outputs, fichiers lus). Épée à double tranchant : plus d'autonomie mais risque de pollution de contexte
- **Context rot** : dégradation de performance quand le contexte grandit, l'attention se dilue sur trop de tokens. Pour le modèle 1M, commence à apparaître vers ~300-400k tokens, mais dépend fortement de la tâche
- **Compaction** : résumé automatique de la conversation quand on approche la fin de la fenêtre. Peut être déclenché manuellement. Lossy par nature (on fait confiance au modèle pour décider quoi garder)
- **5 options à chaque tour** : Continue, /rewind (esc esc), /clear, /compact, subagents. Le plus naturel est de continuer, mais les 4 autres existent pour gérer le contexte
- **Règle d'or** : nouvelle tâche = nouvelle session. Zone grise pour les tâches liées (ex: documentation d'une feature qu'on vient d'implémenter)
- **Rewind = le meilleur réflexe** : "If I had to pick one habit that signals good context management, it's rewind." Double-tap Esc pour revenir à un message précédent et re-prompter avec ce qu'on a appris, plutôt que corriger en accumulant du contexte
- **"Summarize from here"** : faire résumer par Claude ses apprentissages comme un message de handoff de son futur soi vers son passé
- **Compact vs Clear** : /compact = résumé automatique (lossy mais exhaustif), /clear = résumé manuel (plus de travail mais contexte exactement ce qu'on veut). On peut guider compact : "/compact focus on the auth refactor, drop the test debugging"
- **Mauvaises compactions** : se produisent quand le modèle ne peut pas prédire la direction du travail. Particulièrement problématique car le modèle est à son point le moins intelligent (context rot) au moment de compacter. Avec 1M tokens, on a plus de temps pour /compact proactivement
- **Subagents = gestion de contexte** : déléguer un bloc de travail à un agent avec son propre contexte propre. Test mental : "aurai-je besoin de ce résultat intermédiaire ou juste de la conclusion ?" Exemples : vérifier un résultat, lire un autre codebase, écrire la doc
- **Claude Code appellera automatiquement des subagents**, mais on peut lui demander explicitement de le faire pour des cas spécifiques

## RésuméDe400mots

Thariq, ingénieur chez Anthropic, partage un guide pratique sur la gestion de sessions dans Claude Code avec la fenêtre de contexte d'un million de tokens. Ses observations viennent de conversations récentes avec des utilisateurs de Claude Code.

La **fenêtre de contexte** est tout ce que le modèle peut voir simultanément : prompt système, conversation, appels d'outils et fichiers lus. La **pourriture de contexte** (context rot) désigne la dégradation de performance quand le contexte grandit, l'attention se diluant sur trop de tokens. Pour le modèle 1M, cette dégradation commence typiquement vers 300-400k tokens, selon la tâche. La **compaction** est le mécanisme de résumé qui remplace l'historique par une synthèse quand on approche la limite.

À chaque fin de tour, l'utilisateur a cinq options : continuer dans la même session, **rewind** (revenir à un message précédent), **/clear** (session propre), **/compact** (résumer et continuer), ou **subagents** (déléguer avec un contexte propre). La règle générale est de démarrer une nouvelle session pour chaque nouvelle tâche, avec une zone grise pour les tâches liées.

Le **rewind** est identifié comme le meilleur réflexe de gestion de contexte. Plutôt que de corriger en accumulant du bruit ("ça n'a pas marché, essaie X"), il vaut mieux revenir au point juste après les lectures de fichiers et re-prompter avec les enseignements : "N'utilise pas l'approche A, le module foo ne l'expose pas — va directement à B." La fonction "summarize from here" permet de créer un message de handoff, comme un message du futur soi de Claude vers son passé.

La différence entre **/compact** et **/clear** est significative. Compact est automatique et potentiellement plus exhaustif mais lossy — on fait confiance au modèle pour décider quoi garder. Clear demande à l'utilisateur de formuler ce qui compte et repart propre. On peut guider compact avec des instructions spécifiques. Les mauvaises compactions surviennent quand le modèle ne peut pas anticiper la direction du travail, ce qui est particulièrement problématique car il est à son point de moindre intelligence au moment de compacter.

Les **subagents** sont un outil de gestion de contexte pour les blocs de travail générant beaucoup d'output intermédiaire. Le test mental : "aurai-je besoin de cet output ou juste de la conclusion ?" On peut demander explicitement à Claude de déléguer à un subagent pour vérifier un résultat, lire un autre codebase, ou écrire de la documentation. L'auteur conclut que ces mécanismes seront à terme gérés automatiquement par Claude, mais pour l'instant la gestion de sessions reste une compétence clé de l'utilisateur.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Thariq | PERSONNE | a_écrit | Guide gestion sessions Claude Code 1M | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Thariq | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.90 | DYNAMIQUE | inféré |
| Claude Code | TECHNOLOGIE | possède | Fenêtre de contexte de 1 million de tokens | CONCEPT | 0.98 | DYNAMIQUE | déclaré_article |
| Context rot | CONCEPT | dégrade | Performance du modèle | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Context rot | CONCEPT | apparaît_vers | 300-400k tokens | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Compaction | CONCEPT | résume | Historique de conversation | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Rewind | CONCEPT | est_recommandé_comme | Meilleur réflexe de gestion de contexte | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Subagents | CONCEPT | offre | Contexte propre isolé | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Compact | CONCEPT | s_oppose_à | Clear | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Mauvaise compaction | CONCEPT | est_causée_par | Imprévisibilité de la direction du travail | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Thariq | PERSONNE | rôle | Ingénieur Anthropic, expert Claude Code | AJOUT |
| Claude Code | TECHNOLOGIE | fenêtre_contexte | 1 million de tokens | MISE_A_JOUR |
| Context rot | CONCEPT | définition | Dégradation de performance quand le contexte grandit, attention diluée sur trop de tokens | MISE_A_JOUR |
| Compaction | CONCEPT | définition | Résumé automatique de la conversation remplaçant l'historique | MISE_A_JOUR |
| Rewind | CONCEPT | définition | Retour à un message précédent en supprimant les messages suivants du contexte (double Esc) | AJOUT |
| Subagents | CONCEPT | définition | Agents délégués avec leur propre fenêtre de contexte propre | MISE_A_JOUR |
