# osmani-how-write-good-spec-ai-agents-2026-01-13

## Veille
Addy Osmani - écrire specs pour agents IA, 5 principes, Plan Mode, PRD structuré, modularité

## Titre Article
How to write a good spec for AI agents

## Date
2026-01-13

## URL
https://addyosmani.com/blog/good-spec/

## Keywords
spec, spécifications, agents IA, Claude Code, Plan Mode, PRD, modularité, context window, sub-agents, testing, vibe coding, prompt engineering, SPEC.md

## Authors
Addy Osmani

## Ton
Profil : Article blog technique, registre pédagogique et prescriptif, perspective engineering leader (Google Chrome).
Style : Structure en 5 principes numérotés avec sous-sections détaillées. Utilise des exemples de code concrets et tableaux comparatifs. Équilibre théorie et mise en pratique. Références à études GitHub (2 500+ agents analysés). Mises en garde contre les pièges courants. Public cible : développeurs utilisant agents de codage IA, tech leads, architectes.

## Pense-betes
- **Problème central** : Specs massives causent surcharge de contexte et dégradation performance modèle
- **5 principes** pour specs efficaces :
  1. **Vision haut niveau d'abord** : brief concis, laisser l'IA élaborer les détails
  2. **Structure PRD professionnelle** : 6 domaines essentiels
  3. **Division modulaire** : éviter les prompts monolithiques
  4. **Auto-vérifications intégrées** : contraintes et expertise domaine
  5. **Test, itération, évolution** : specs comme documents vivants
- **Plan Mode** (Shift+Tab Claude Code) : exploration read-only avant génération code
- **SPEC.md** : fichier persistant pour cohérence cross-sessions
- **6 domaines PRD** : Commands, Testing, Project structure, Code style, Git workflow, Boundaries
- **Système 3 niveaux** : ✅ Always do, ⚠️ Ask first, 🚫 Never do
- **"Curse of instructions"** : performance IA dégradée avec trop d'instructions simultanées
- **Solution modularité** : SPEC_backend.md, SPEC_frontend.md séparés
- **Sub-agents/skills** : agents spécialisés par domaine
- **LLM-as-a-Judge** : second agent review pour style/architecture
- **Conformance testing** : suites YAML comme contrats
- **Pièges fréquents** : specs trop vagues (dominant), skip review humaine, confondre vibe coding et production
- **"Lethal trifecta"** : vitesse (hard to review) + non-déterminisme + coût (encourage shortcuts)
- **Métaphore** : Traiter agents comme "stagiaires compétents" - instructions claires, contexte pertinent, feedback actionnable
- **Outils mentionnés** : Claude Code, GitHub Spec Kit, Cursor, LangGraph, OpenAI Swarm, Chroma, Context7, MCP

## RésuméDe400mots
Addy Osmani publie un guide complet sur la rédaction de spécifications efficaces pour agents de codage IA, adressant le problème central que les specs massives causent une surcharge de contexte et dégradent les performances des modèles.

Le premier principe préconise de commencer par une vision haut niveau plutôt que de sur-ingénierer d'emblée. Utiliser le Plan Mode (Shift+Tab dans Claude Code) permet une exploration en lecture seule avant génération de code. L'agent élabore ensuite les détails dans un fichier SPEC.md persistant pour la cohérence entre sessions.

Le second principe structure les specs comme des PRD professionnels couvrant six domaines essentiels : commandes exécutables avec flags, procédures de test, structure projet explicite, exemples de code style, workflow git, et limites claires. Osmani propose un système de contraintes à trois niveaux : "Always do" (actions sûres), "Ask first" (changements à fort impact), "Never do" (arrêts durs comme commiter des secrets).

Le troisième principe divise le travail en tâches modulaires. La recherche révèle une "malédiction des instructions" où trop de consignes simultanées réduisent significativement l'adhérence du modèle. Les solutions incluent des fichiers spec séparés (SPEC_backend.md, SPEC_frontend.md), des sub-agents spécialisés, et des agents parallèles pour travaux non-chevauchants.

Le quatrième principe intègre des auto-vérifications. Le pattern "LLM-as-a-Judge" utilise un second agent pour vérifier l'adhérence au style et à l'architecture. Les tests de conformance en YAML servent de contrats indépendants du langage. L'expertise domaine doit être explicitement incluse : préférences, pièges spécifiques aux bibliothèques, formats attendus.

Le cinquième principe traite les specs comme documents vivants versionnés avec le code. Le cycle continu teste après chaque milestone, réinjecte les échecs dans le prompt suivant, et met à jour le document quand les hypothèses s'avèrent incomplètes.

Osmani met en garde contre les pièges fréquents : specs trop vagues (échec dominant selon l'étude GitHub), skip de la review humaine parce que les tests passent, et confusion entre "vibe coding" rapide et ingénierie de production. Il identifie une "triade létale" : vitesse (difficile à reviewer), non-déterminisme (outputs inconsistants), et coût (encourage les raccourcis).

La métaphore centrale compare les agents IA à des "stagiaires compétents" nécessitant instructions claires, contexte pertinent et feedback actionnable. Le succès dépend de l'équilibre entre specs complètes et fenêtres de contexte focalisées.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Addy Osmani | PERSONNE | a_publié | guide specs agents IA | CONCEPT | 0.98 | STATIQUE | déclaré_article |
| Addy Osmani | PERSONNE | travaille_chez | Google Chrome | ORGANISATION | 0.95 | DYNAMIQUE | inféré |
| specs massives | CONCEPT | causent | surcharge contexte | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Plan Mode | TECHNOLOGIE | permet | exploration read-only avant code | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| SPEC.md | TECHNOLOGIE | assure | cohérence cross-sessions | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| malédiction des instructions | CONCEPT | réduit | adhérence modèle | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| modularité specs | METHODOLOGIE | résout | surcharge contexte | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| LLM-as-a-Judge | METHODOLOGIE | vérifie | adhérence style et architecture | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| triade létale | CONCEPT | combine | vitesse, non-déterminisme, coût | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| vibe coding | METHODOLOGIE | s_oppose_à | ingénierie production | METHODOLOGIE | 0.83 | ATEMPOREL | déclaré_article |
| agents IA | CONCEPT | comparés_à | stagiaires compétents | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Addy Osmani | PERSONNE | rôle | Engineering Leader Google Chrome | AJOUT |
| Plan Mode | TECHNOLOGIE | activation | Shift+Tab dans Claude Code | AJOUT |
| SPEC.md | TECHNOLOGIE | catégorie | Fichier spécification persistant | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage IA CLI | AJOUT |
| LLM-as-a-Judge | METHODOLOGIE | définition | Second agent review style/architecture | AJOUT |
