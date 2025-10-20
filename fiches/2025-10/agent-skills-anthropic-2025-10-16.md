# agent-skills-anthropic-2025-10-16

## Veille
Agent Skills d'Anthropic, compétences modulaires réutilisables, portabilité cross-product, Code Execution Tool - Anthropic

## Titre Article
Introducing Agent Skills

## Date
2025-10-16

## URL
https://www.anthropic.com/news/skills

## Keywords
Agent Skills, Claude, composable AI, portable skills, Code Execution Tool, skill-creator, API skills endpoint, Claude Code, workflow customization, specialist knowledge, executable code, minimal loading, chain of thought

## Authors
Anthropic (équipe produit)

## Pense-betes
- **Skills = dossiers** contenant instructions, scripts et ressources que Claude charge à la demande
- **Sélection automatique** : Claude scanne les skills disponibles et charge uniquement ce qui est nécessaire
- **Portable** : même format partout (Claude.ai, API, Claude Code)
- **Composable** : les skills se combinent automatiquement, Claude coordonne leur utilisation
- **Efficient** : charge uniquement le minimum nécessaire au moment opportun
- **Powerful** : peut inclure du code exécutable pour fiabilité (vs génération token)
- **skill-creator** : skill méta qui aide à créer d'autres skills de manière interactive
- Nécessite **Code Execution Tool** (beta) pour l'API
- Nouveau endpoint `/v1/skills` pour gestion programmatique
- Skills visibles dans la **chaîne de pensée** de Claude
- Marketplace `anthropics/skills` pour Claude Code
- Témoignages clients : Box, Notion, Canva, Rakuten (gains de temps massifs)
- Disponible pour Pro, Max, Team et Enterprise (admins doivent activer pour Team/Enterprise)

## RésuméDe400mots

Anthropic lance officiellement **Agent Skills**, un système permettant de doter Claude de compétences spécialisées réutilisables. Les Skills sont des dossiers contenant instructions, scripts et ressources que Claude charge dynamiquement selon les besoins de la tâche.

**Fonctionnement et Architecture**

Pendant son travail, Claude scanne automatiquement les skills disponibles pour identifier les correspondances pertinentes. Lorsqu'un skill correspond, il charge uniquement les informations et fichiers minimaux nécessaires, maintenant la rapidité tout en accédant à une expertise spécialisée. Cette approche "just-in-time loading" optimise l'utilisation des tokens.

**Quatre Caractéristiques Clés**

**Composable** : Les skills s'empilent ensemble. Claude identifie automatiquement quels skills sont nécessaires et coordonne leur utilisation simultanée sans intervention humaine.

**Portable** : Même format partout. Construire une fois, utiliser sur Claude.ai, Claude Code et l'API. Cette portabilité cross-product élimine la duplication d'efforts.

**Efficient** : Charge uniquement ce qui est nécessaire, quand c'est nécessaire. Pas de surcharge cognitive ou computationnelle.

**Powerful** : Les skills peuvent inclure du code exécutable pour les tâches où la programmation traditionnelle est plus fiable que la génération de tokens. Cette capacité hybride combine le meilleur des deux mondes.

**Déploiement Multi-Produit**

**Claude Apps** (Pro, Max, Team, Enterprise) : Skills activables dans les paramètres. Anthropic fournit des skills pour tâches communes (création documents Excel, PowerPoint, Word, PDF), des exemples personnalisables, et la possibilité de créer skills custom. Le **skill-creator** offre guidance interactive : Claude interroge sur le workflow, génère la structure de dossier, formate le fichier SKILL.md et regroupe les ressources. Aucune édition manuelle requise. Les skills apparaissent dans la chaîne de pensée visible de Claude.

**API** : Nouveau endpoint `/v1/skills` pour gestion programmatique des versions et du versioning. Nécessite le **Code Execution Tool** (beta) qui fournit l'environnement sécurisé d'exécution. Les développeurs peuvent créer skills custom pour étendre les capacités de Claude selon leurs cas d'usage spécifiques. Gestion via Claude Console.

**Claude Code** : Installation via plugins depuis la marketplace `anthropics/skills`. Claude charge automatiquement les skills pertinents. Partage via contrôle de version avec l'équipe. Installation manuelle possible via `~/.claude/skills`. Le Claude Agent SDK offre le même support pour construire des agents custom.

**Validation Clients**

**Box** (Yashodha Bhavnani, Head of AI) : Transformation de fichiers stockés en présentations, spreadsheets et documents Word suivant les standards organisationnels - économie de nombreuses heures.

**Notion** (MJ Felix, Product Manager) : Passage de questions à actions plus rapide, moins de manipulation de prompts sur tâches complexes, résultats plus prévisibles.

**Canva** (Anwar Haneef, GM & Head of Ecosystem) : Plans d'exploiter Skills pour personnaliser agents et intégrer Canva plus profondément dans workflows agentiques.

**Rakuten** (Yusuke Kaji, General Manager AI) : Traitement de multiples spreadsheets, détection d'anomalies critiques, génération de rapports selon procédures. Ce qui prenait une journée s'accomplit maintenant en une heure.

**Philosophie de Conception**

Anthropic conceptualise les Skills comme "matériaux d'onboarding personnalisés" permettant d'empaqueter l'expertise et transformer Claude en spécialiste des domaines importants pour l'utilisateur. Cette approche démocratise la customisation tout en maintenant portabilité et composabilité, évitant la fragmentation des écosystèmes d'extensions propriétaires.
