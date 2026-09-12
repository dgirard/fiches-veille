---
themes: [agents-codage-ia-skills, outils-plateformes, economie-marche]
source: "engineering.atspotify.com (Dimitri Mazmanov)"
---
# mazmanov-portal-spotify-shunt-claude-code-tokens-2026-09-03

## Veille

Billet d'ingénierie de **Spotify** publié le **3 septembre 2026** sur engineering.atspotify.com (~1 600 mots, neuf sections, deux manifestes YAML, quatre exemples de ligne de commande), signé **Dimitri Mazmanov**, Principal Product Manager. Il décrit un montage personnel destiné à sortir les tâches d'entrée-sortie du contexte de **Claude Code**. Prémisse posée d'entrée : *« Most of what an AI coding agent does for me isn't thinking. It's I/O »* — lire cinq fichiers pour répondre sur une seule méthode, produire un test calqué sur les vingt autres du répertoire. **(A) Les modes.** **Portal by Spotify** expose des *AiKA Modes*, agents déclaratifs sur runtime éphémère — instructions, modèle, température, outils **MCP** — comparés à *« AWS Lambda, but for agents »* ; deux modes publics, `bulk-reader` et `code-writer`, tournent ici sur **Gemini 2.5 Flash**. **(B) Le routage.** Un plugin Claude Code nommé `shunt` remplace des règles de `CLAUDE.md` jugées *« advisory, not enforced »* par trois couches : des hooks `PreToolUse` qui bloquent toute lecture au-delà de **350 lignes** (seuil réglable par `SHUNT_MIN_LINES`), deux scripts bash appelant la CLI Portal, deux skills qui donnent la syntaxe d'invocation. Le corpus part au modèle secondaire et **n'entre jamais dans le contexte de Claude**. **(C) Les mesures et leurs bornes.** Sur un monorepo Java, quatre scénarios, l'économie moyenne annoncée est de **~90 %** sur `bulk-read` ; l'auteur signale que le scénario `code-write` est *« harder to measure »*, et liste trois limites — édition non délégable, raisonnement non délégable, **10 à 30 secondes** de latence par appel. Prolonge les questions de budget de [[gupta-token-budget-wars-marginal-token-utility-2026-05-28]] et la délégation examinée dans [[willison-fable-judgement-delegation-subagents-2026-07-03]].

## Titre Article

Portal by Spotify cut my Claude Code token usage by 90%

## Date

2026-09-03

## URL

https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90

## Keywords

Portal by Spotify, AiKA Modes, shunt, plugin Claude Code, routage de modèles, modèle secondaire, délégation d'entrées-sorties, Gemini 2.5 Flash, bulk-reader, code-writer, hooks PreToolUse, blocage de lecture, seuil de lignes, SHUNT_MIN_LINES, skills, CLI Portal, runtime éphémère, agent déclaratif, MCP, budget de tokens, coût par développeur, tokens de sortie, contexte de l'agent, monorepo Java, latence de délégation, marketplace de plugins, spotify/portal-ai-plugins, Backstage, FinOps IA

## Authors

Dimitri Mazmanov (Principal Product Manager, Spotify), sur le blog d'ingénierie engineering.atspotify.com.

## Ton

**Profil** : retour d'expérience individuel publié sur un blog d'ingénierie d'entreprise, à la première personne, doublé d'une promotion assumée d'un produit interne. Public : utilisateurs avancés d'agents de codage et responsables de plateformes internes.

**Style** : le texte suit une progression de démonstration technique — problème chiffré, solution, architecture en couches numérotées, mesures, limites, mode d'emploi. Les artefacts sont donnés en clair : deux manifestes YAML complets, quatre invocations de ligne de commande, la variable d'environnement du seuil, les trois commandes d'installation. Les détails d'implémentation sont exposés plutôt que résumés, y compris les micro-décisions et leur raison — l'instruction *« output only the code »* est justifiée par les fences markdown que Claude devrait sinon parser, le fichier de référence obligatoire par le code hors contexte qu'un modèle produirait sans lui.

**Position épistémique** : le titre affiche un résultat chiffré, mais le corps le borne lui-même. Une section entière, *« What doesn't work »*, énumère ce que le montage ne fait pas : pas d'édition déléguée faute de numéros de ligne fiables, pas de raisonnement délégué — un bug de *thread-safety* manqué par le modèle secondaire, repéré par Claude —, et un surcoût de latence qui rend la délégation contre-productive sous le seuil. La mesure elle-même reste déclarative : quatre scénarios sur un monorepo Java, sans protocole publié, sans volumes absolus, sans comptabilisation du coût du modèle secondaire. La dernière section déplace explicitement l'enjeu du chiffre vers la réutilisabilité des modes, formulée comme *« they turn model routing from a systems engineering problem into a configuration problem »*.

## Pense-betes

- **L'intuition de départ est un partage de charge, pas une optimisation de prompt.** Lire des fichiers et générer du code répétitif consomme des tokens sans mobiliser de raisonnement ; ces tâches partent à un modèle bon marché, le modèle principal garde les problèmes qui demandent du jugement.
- **Ce qui est économisé n'est pas seulement le prix, c'est l'occupation du contexte.** Le corpus lu est envoyé au modèle secondaire et ne rentre jamais dans la fenêtre de Claude ; une relance sur les mêmes fichiers ne recharge donc rien côté principal. Même mécanique que la délégation à des sous-agents dans [[willison-fable-judgement-delegation-subagents-2026-07-03]].
- **Un mode = un agent déclaratif** : nom, description, instructions, modèle, `visibility`, `resourceLimits`, `tags`. Runtime éphémère, rien de stocké côté serveur, aucune clé d'API à gérer. Résolution par nom, insensible à la casse, avec préséance perso → équipe → public : forker un mode public suffit à le surcharger sans configuration.
- **Les règles dans `CLAUDE.md` n'ont pas tenu.** Première version du routage : un bloc d'instructions que Claude lisait et suivait parfois. Deux défauts nommés — *advisory, not enforced*, et à recopier dans chaque projet. C'est l'argument qui fait passer aux hooks, portes dures indépendantes de la décision du modèle.
- **Le seuil est le paramètre de réglage central.** `check-file-size` bloque les `Read` au-delà de 350 lignes par défaut ; `check-bash-read` intercepte `cat`, `head`, `tail`, `less`, `more`. Les lectures ciblées (`offset`/`limit`) et les commandes pipées passent. Sous le seuil, la latence de délégation coûte plus qu'elle ne rapporte.
- **La dégradation gracieuse est le point d'architecture.** Trois couches : le hook bloque, le script exécute, la skill explique. Si Claude ignore la skill, le hook bloque quand même — le contrat n'est pas confié au modèle.
- **Deux instructions de mode font le gros du travail.** *Output only the code* évite les fences markdown et la prose que le principal devrait reparser ; un fichier de référence obligatoire pour `code-writer` évite du code hors contexte. Même logique de cadrage que les skills décrites dans [[shihipar-claude-code-lessons-building-skills-2026-06-03]].
- ⚠️ **Le chiffre du titre est auto-déclaré et non reproductible en l'état** : moyenne sur quatre scénarios d'un monorepo Java, sans protocole, sans volumes absolus, sans comparaison à un modèle principal utilisé avec des lectures ciblées. L'auteur admet que le scénario `code-write` est plus difficile à mesurer, et le coût du modèle secondaire n'est pas retranché.
- **Les trois limites revendiquées cadrent le périmètre** : pas d'édition déléguée (numéros de ligne du résumé non fiables), pas de raisonnement délégué (débogage, décisions d'architecture et code critique explicitement exclus du routage), latence de 10 à 30 s par aller-retour avec un plafond Portal à 30 s qui force à découper les grosses générations.
- **La conclusion opérationnelle porte sur les modes, pas sur le plugin** : réutilisables entre projets, partageables (les deux modes sont publics), composables (`doc-writer`, `reviewer`, `translator` cités comme extensions possibles) et découplés du routage — changer de modèle de travail ne change pas le plugin. Cette séparation empaquetage / exécution est celle que formalise [[google-agent-plugins-packaging-skills-mcp-2026-08-06]].
- **Installation** : `claude plugin marketplace add spotify/portal-ai-plugins`, puis les plugins `portal` (la CLI) et `shunt` (le routage), puis `/portal:setup` pour l'authentification contre une instance Portal. Le montage suppose donc une instance Portal avec le plugin AiKA activé — il n'est pas transposable tel quel hors d'une organisation qui l'exploite.
- **Les chiffres de cadrage viennent de l'extérieur du billet et ne sont pas sourcés** : coûts de codage IA dépassant le salaire moyen d'un développeur d'ici 2028, un quart des responsables d'ingénierie à 200-500 $ par développeur et par mois, certains au-delà de 2 000 $. À traiter comme ordre de grandeur, à rapprocher des mesures par équipe de [[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]].

## RésuméDe400mots

Dimitri Mazmanov, Principal Product Manager chez Spotify, publie le 3 septembre 2026 sur le blog d'ingénierie de l'entreprise le récit d'un montage qui réduirait de 90 % sa consommation de tokens dans Claude Code. Son constat de départ : l'essentiel de ce qu'un agent de codage fait pour lui n'est pas du raisonnement mais de l'entrée-sortie — lire cinq fichiers pour répondre à une question sur une méthode, générer un fichier de test identique aux vingt voisins. Ce travail est envoyé à un modèle de pointe surqualifié, alors qu'un modèle bon marché le traiterait aussi bien.

La solution repose sur les AiKA Modes de Portal by Spotify : des agents déclaratifs exécutés sur un runtime éphémère, définis par des instructions, un modèle, des paramètres et des outils MCP, sans infrastructure ni clés d'API à gérer. L'auteur crée deux modes publics tournant sur Gemini 2.5 Flash. Le premier, bulk-reader, lit un lot de fichiers et répond en puces structurées. Le second, code-writer, génère du code à partir d'une spécification et d'un fichier de référence dont il doit reproduire les conventions.

Le routage est assuré par un plugin Claude Code appelé shunt, après l'échec d'une première version fondée sur des règles écrites dans CLAUDE.md, que le modèle pouvait ignorer et qu'il fallait recopier par projet. Le plugin empile trois couches. Des hooks PreToolUse bloquent les lectures de fichiers dépassant un seuil de lignes configurable, ainsi que les commandes cat, head ou tail sur de gros fichiers ; les lectures ciblées passent. Des scripts bash enveloppent les appels à la CLI Portal, construisent la requête et remontent l'usage de tokens. Des fichiers de skill indiquent à Claude quand et comment appeler ces scripts. Le corpus transite vers le modèle secondaire sans jamais entrer dans le contexte de Claude, qui ne voit pas non plus le code généré, écrit directement sur disque.

Les mesures sont présentées comme une moyenne d'environ 90 % d'économie sur quatre scénarios testés contre un monorepo Java, l'auteur reconnaissant que le scénario de génération se mesure mal. Une section détaille ce qui ne fonctionne pas : l'édition n'est pas délégable faute de numéros de ligne fiables, le raisonnement non plus — le modèle secondaire a manqué un bug de thread-safety que Claude a vu immédiatement —, et chaque délégation coûte dix à trente secondes de latence, ce qui la rend contre-productive sur les petits fichiers.

L'auteur conclut que l'économie de tokens n'est qu'un point de départ : l'intérêt réel des modes est de transformer le routage de modèles en problème de configuration plutôt que d'ingénierie système.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Dimitri Mazmanov | PERSONNE | travaille_chez | Spotify | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Dimitri Mazmanov | PERSONNE | a_créé | shunt | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Dimitri Mazmanov | PERSONNE | affirme_que | "Most of what an AI coding agent does for me isn't thinking. It's I/O" | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| Dimitri Mazmanov | PERSONNE | affirme_que | les coûts de codage IA dépasseront le salaire moyen d'un développeur d'ici 2028 | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Dimitri Mazmanov | PERSONNE | mesure | un quart des responsables d'ingénierie dépensent 200-500 $ par développeur et par mois en tokens | MESURE | 0.82 | STATIQUE | déclaré_article |
| Spotify | ORGANISATION | a_créé | Portal by Spotify | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Portal by Spotify | TECHNOLOGIE | permet | AiKA Modes | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| AiKA Modes | TECHNOLOGIE | est_instance_de | agent déclaratif sur runtime éphémère | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| AiKA Modes | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| AiKA Modes | TECHNOLOGIE | permet | routage de modèles | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| routage de modèles | CONCEPT | réduit | consommation de tokens du modèle principal | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| shunt | TECHNOLOGIE | fait_partie_de | Claude Code | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| shunt | TECHNOLOGIE | utilise | Portal by Spotify | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| shunt | TECHNOLOGIE | utilise | hooks | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| shunt | TECHNOLOGIE | remplace | règles de routage écrites dans CLAUDE.md | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| Dimitri Mazmanov | PERSONNE | affirme_que | "The rules were advisory, not enforced" | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| hooks | TECHNOLOGIE | permet | blocage des lectures au-delà de 350 lignes par défaut | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| bulk-reader | TECHNOLOGIE | est_instance_de | AiKA Modes | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| code-writer | TECHNOLOGIE | est_instance_de | AiKA Modes | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| bulk-reader | TECHNOLOGIE | utilise | Gemini 2.5 Flash | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| code-writer | TECHNOLOGIE | utilise | Gemini 2.5 Flash | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| shunt | TECHNOLOGIE | mesure | économie moyenne de ~90 % de tokens sur le scénario bulk-read, monorepo Java, quatre scénarios | MESURE | 0.85 | STATIQUE | déclaré_article |
| shunt | TECHNOLOGIE | réduit | occupation de la fenêtre de contexte du modèle principal | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Dimitri Mazmanov | PERSONNE | affirme_que | le gain sur le scénario code-write est difficile à mesurer en tokens | AFFIRMATION | 0.90 | STATIQUE | déclaré_article |
| routage de modèles | CONCEPT | s_oppose_à | délégation de l'édition de code et du raisonnement | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Gemini 2.5 Flash | TECHNOLOGIE | s_oppose_à | détection d'un bug de thread-safety trouvé par Claude Code | AFFIRMATION | 0.86 | STATIQUE | déclaré_article |
| shunt | TECHNOLOGIE | mesure | latence de 10 à 30 secondes par délégation, plafond Portal de 30 secondes | MESURE | 0.91 | STATIQUE | déclaré_article |
| Dimitri Mazmanov | PERSONNE | recommande | exclure du routage le débogage, les décisions d'architecture et le code critique | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Dimitri Mazmanov | PERSONNE | affirme_que | "They turn model routing from a systems engineering problem into a configuration problem" | CITATION | 0.93 | ATEMPOREL | déclaré_article |
| spotify/portal-ai-plugins | TECHNOLOGIE | publie | shunt | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Dimitri Mazmanov | PERSONNE | rôle | Principal Product Manager chez Spotify ; auteur du plugin shunt et du billet | AJOUT |
| Spotify | ORGANISATION | secteur | Streaming musical / Technologie ; publie son outillage agent interne sur engineering.atspotify.com | AJOUT |
| Portal by Spotify | TECHNOLOGIE | nature | Plateforme interne exposant des agents déclaratifs (AiKA Modes), une CLI et une API ; instance par organisation | AJOUT |
| AiKA Modes | TECHNOLOGIE | définition | Agent déclaratif sur runtime éphémère — instructions, modèle, température, outils MCP, visibilité publique ou privée ; résolution par nom avec préséance perso, équipe, public | AJOUT |
| shunt | TECHNOLOGIE | architecture | Plugin Claude Code à trois couches : hooks PreToolUse de blocage, scripts bash d'appel à la CLI Portal, skills d'invocation ; dégrade gracieusement si la skill est ignorée | AJOUT |
| bulk-reader | TECHNOLOGIE | rôle | Mode public lisant un lot de fichiers encadrés en balises XML et répondant en puces structurées ; le corpus n'entre pas dans le contexte de Claude | AJOUT |
| code-writer | TECHNOLOGIE | rôle | Mode public générant du code à partir d'une spécification et d'un fichier de référence obligatoire ; sortie écrite sur disque, jamais vue par Claude | AJOUT |
| hooks | TECHNOLOGIE | usage | check-file-size bloque les Read au-delà de 350 lignes (SHUNT_MIN_LINES) ; check-bash-read intercepte cat, head, tail, less, more ; lectures ciblées et commandes pipées exemptées | AJOUT |
| routage de modèles | CONCEPT | principe | Découple la décision de déléguer (le plugin) de la manière de répondre (le mode) ; changer de modèle de travail ne change pas le plugin | AJOUT |
| Gemini 2.5 Flash | TECHNOLOGIE | rôle | Modèle de travail des deux modes dans les exemples ; remplaçable par tout modèle configuré dans l'instance Portal | AJOUT |
| Claude Code | TECHNOLOGIE | rôle | Agent principal dont les lectures et générations volumineuses sont routées vers un modèle secondaire | AJOUT |
| spotify/portal-ai-plugins | TECHNOLOGIE | nature | Marketplace de plugins Claude Code distribuant portal (la CLI) et shunt (le routage) | AJOUT |
| MCP | TECHNOLOGIE | usage | Outils attachables à un mode Portal lors de sa définition | AJOUT |
