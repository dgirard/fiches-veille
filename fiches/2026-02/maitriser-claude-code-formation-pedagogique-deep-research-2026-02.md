# maitriser-claude-code-formation-pedagogique-deep-research-2026-02
## Veille
Formation complète Claude Code : 12 modules pédagogiques coding agentique - Deep Research

## Titre Article
Maîtriser Claude Code — Détail complet des 12 modules et ~60 leçons

## Date
2026-02

## URL
https://github.com/dgirard/fiches-veille/blob/main/docs/deep%20research/202602/Ma%C3%AEtriser%20Claude%20Code.md

## Keywords
Claude Code, coding agentique, formation pédagogique, pédagogie socratique, CLAUDE.md, MCP, Model Context Protocol, commandes slash, permissions, sandboxing, CI/CD, mode headless, subagents, skills, hooks, fenêtre de contexte, Git, workflow Explore-Plan-Code, Haiku, Sonnet, Opus, flashcards FSRS

## Authors
Deep Research Veille Interne

## Ton
**Profil** : Curriculum pédagogique structuré, registre didactique et interactif, niveau technique progressif (débutant à avancé)

**Description** : Document de formation complet conçu selon une méthode socratique en 5 étapes (hook, exploration guidée, dialogue, pratique active, flashcard FSRS). Le ton alterne entre celui d'un tuteur bienveillant qui pose des questions provocantes pour susciter la réflexion et celui d'un expert technique qui délivre des connaissances précises. Les analogies sont omniprésentes (architecte/briques, Airbus A380 pour chercher du pain, bureau de 200 000 post-its) pour ancrer les concepts abstraits. Le public cible est le développeur professionnel souhaitant passer du coding traditionnel à l'orchestration agentique.

## Pense-betes
- **Structure pédagogique** : 12 modules (A1-A12), ~60 leçons, 60 flashcards FSRS, durée estimée 3h-5h
- **Parcours A** couvre Claude Code de bout en bout : concepts → installation → conversations → commandes → mémoire → sécurité → contexte → Git → MCP → CI/CD → personnalisation → best practices
- **5 étapes par leçon** : Hook socratique (30s) → Exploration guidée (90s) → Dialogue socratique (60s) → Pratique active (60s) → Synthèse + Flashcard (30s)
- **Concepts fondamentaux** :
  - Coding agentique = le développeur décrit l'intention, l'agent explore/planifie/code/teste
  - Claude Code = agent terminal-first (pas un chatbot), peut lire/écrire fichiers, exécuter bash, gérer Git
  - Trois modèles : Haiku (rapide/économique), Sonnet (équilibré/défaut), Opus (intelligent/complexe)
- **Workflow recommandé Anthropic** : Explore → Plan → Code (mode Plan via Shift+Tab)
- **Système de mémoire à 4 niveaux** : Enterprise Policy > Project CLAUDE.md > Project Rules (.claude/rules/) > User CLAUDE.md
- **CLAUDE.md** : fichier versionné Git donnant le contexte permanent du projet, créé avec /init, à garder concis pour éviter le "fading memory"
- **Gestion du contexte** : fenêtre 200k tokens, /compact (résumer) vs /clear (effacer), /cost et /context pour surveiller
- **Sécurité multicouche** : 4 modes permission (Normal, Auto-accept edits, Plan, Bypass), sandbox OS (Seatbelt macOS, bubblewrap Linux), hooks PreToolUse, allow/deny dans settings.json
- **MCP** : standard ouvert pour connecter Claude Code à des outils externes (GitHub, Brave Search, Context7, Sentry, Playwright)
- **Mode headless** : flag -p pour usage non-interactif, intégration CI/CD via GitHub Actions, formats sortie text/json/stream-json
- **Skills vs commandes slash** : commandes = déclenchées manuellement (/commande), skills = activées automatiquement par Claude quand la description matche
- **Hooks** : scripts déterministes sur 11+ événements (PreToolUse, PostToolUse, Stop, Notification...), exit code 2 = bloquer
- **5 patterns professionnels** : Explore→Plan→Code→Test→Review, Context priming, Iterative refinement, Model surfing, Session hygiene
- **Paywall recommandé** : Modules A1-A4 gratuits (bases), A5-A12 Pro (expertise)

## RésuméDe400mots
Ce document constitue un curriculum pédagogique complet pour maîtriser Claude Code, l'outil CLI agentique d'Anthropic. Organisé en 12 modules (A1 à A12) totalisant environ 60 leçons, il suit une progression rigoureuse du concept fondamental jusqu'aux bonnes pratiques avancées, avec une durée estimée de 3 à 5 heures.

**Fondements (A1)** : Le coding agentique est un changement de paradigme où le développeur passe de l'écriture ligne par ligne à l'orchestration d'agents IA. Claude Code se distingue par son approche terminal-first et donne accès à trois modèles (Haiku, Sonnet, Opus) adaptés à différents niveaux de complexité.

**Prise en main (A2-A3)** : L'installation se fait en une commande (curl ou npm). Le workflow conversationnel repose sur des prompts spécifiques et contextualisés. Quatre règles d'or du prompting agentique : être spécifique, donner le contexte, préciser les contraintes, un objectif à la fois. Le workflow Explore → Plan → Code est recommandé par Anthropic pour les tâches complexes.

**Commandes et mémoire (A4-A5)** : Les commandes slash essentielles (/init, /clear, /compact, /cost, /model, /rewind) structurent le travail quotidien. Le système de mémoire hiérarchique à 4 niveaux (Enterprise Policy, CLAUDE.md projet, Project Rules, User CLAUDE.md) permet de partager et personnaliser le contexte. L'Auto Memory permet à Claude de s'écrire ses propres notes entre sessions.

**Sécurité et contexte (A6-A7)** : Quatre modes de permission (Normal, Auto-accept, Plan, Bypass) offrent un spectre contrôle-autonomie. Le sandbox OS (Seatbelt sur macOS, bubblewrap sur Linux) isole les commandes au niveau kernel. La fenêtre de contexte de 200 000 tokens nécessite une gestion active via /compact et /clear.

**Intégrations (A8-A10)** : Claude Code excelle en gestion Git (commits intelligents, résolution de conflits, PRs automatisées). Le MCP (Model Context Protocol) connecte Claude Code à des outils externes (GitHub, Brave Search, bases de données). Le mode headless (flag -p) permet l'intégration CI/CD via GitHub Actions avec contrôle budgétaire.

**Personnalisation avancée (A11-A12)** : Les commandes slash custom (.claude/commands/), les skills (SKILL.md détectées automatiquement), les subagents spécialisés et les hooks déterministes (11+ événements) permettent une automatisation poussée. Les cinq patterns professionnels (Explore→Plan→Code→Test→Review, Context priming, Iterative refinement, Model surfing, Session hygiene) constituent le socle de la maîtrise experte.

Chaque leçon intègre un hook socratique provocateur, une exploration guidée, un dialogue tuteur-apprenant, un exercice pratique et une flashcard FSRS pour la mémorisation espacée.
