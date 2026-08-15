---
themes: [outils-plateformes, agents-codage-ia-skills, economie-marche]
source: "graphify.net"
---
# graphify-net-annuaire-ia-coding-2026-08-06

## Veille

Site **graphify.net**, consulté le **6 août 2026**, maintenu par **Safi Shamsi** — le créateur de la skill open source graphify (cf. [[skill-shamsi-graphify-2026-08-06]]). Le domaine porte deux objets qu'il faut distinguer. **Le premier est une vitrine produit** : présentation de graphify, guides d'usage, référence CLI, et surtout une galerie de **100 dépôts GitHub tendance déjà graphifiés** — *« 100 repos, 854 079 nœuds, 1 932 930 arêtes »* — filtrables par langage et par taille de graphe, chacun avec sa prévisualisation et sa page de détail. **Le second, et c'est le plus intéressant pour une veille, est un annuaire éditorial** : *« 30 AI coding client guides »*, un répertoire de serveurs MCP comparés sur *« transport, runtime, client support, setup effort, and access risks »*, des comparaisons structurées entre outils (Cursor contre Codex), et un flux d'articles au ciblage manifestement longue traîne (*« GLM-5.2 Knowledge Graph for Developers »*, *« Trae Context Engineering for Agents »*, *« Symphony Knowledge Graph for Agent Memory »*, *« What Is Cowart? A Codex Plugin for Image Editing »*). Le site revendique une méthode — *« source-reviewed »*, *« aligned decision fields, official evidence, and explicit unknowns »* — et se décline en six langues. ⚠️ **Le point que cette fiche existe pour consigner** : le site est **factuellement décalé par rapport au produit qu'il présente**. Il annonce **« 3,7k+ GitHub Stars »** quand l'API GitHub en compte **103 187** le même jour, une **licence MIT** répétée trois fois quand le fichier `LICENSE` du dépôt est une **Apache 2.0**, et met en avant l'argument **« 71,5× de réduction de tokens »** qui appartient au README de la génération v1 et a disparu de la version courante. **Un site officiel qui affiche 3,7 % du nombre d'étoiles réel et se trompe de licence** est un signal en soi : la couche de communication n'a pas suivi le rythme du dépôt.

## Titre Article

Graphify — Knowledge Graphs for AI Coding Assistants (site graphify.net : vitrine, annuaire d'outils et galerie de dépôts graphifiés)

## Date

2026-08-06

## URL

https://graphify.net/

## Keywords

graphify.net, annuaire d'outils IA, directory, guides clients IA, comparaison d'outils, Cursor vs Codex, serveurs MCP, répertoire MCP, transport, runtime, effort de mise en place, risques d'accès, agent skills, dépôts graphifiés, galerie de graphes, nœuds, arêtes, communautés, GitHub Trending, tree-sitter, Leiden, god nodes, graphe interactif, contenu longue traîne, référencement, marketing de contenu, source-reviewed, evidence, unknowns explicites, multilingue, Safi Shamsi, Graphify Labs, incohérence de licence, étoiles périmées, réduction de tokens, v1 contre v8, graphify.com, plateforme commerciale

## Authors

**Safi Shamsi** — mainteneur déclaré en pied de page (*« © 2026 Graphify. Built in the open. Maintained by Safi Shamsi »*), également créateur de la skill graphify et fondateur de **Graphify Labs** (Y Combinator S26). Le site est donc une **propriété officielle du projet**, non un site tiers.

**Trois propriétés distinctes à ne pas confondre** :
- **`github.com/Graphify-Labs/graphify`** — le code de la skill open source.
- **`graphify.com`** — la **plateforme commerciale** (couche continue, en liste d'attente), qui est le `homepage` déclaré du dépôt.
- **`graphify.net`** — le présent site : vitrine, annuaire éditorial et galerie de graphes.

## Ton

**Profil** : site hybride, moitié documentation produit, moitié **média de comparaison**. Registre neutre, structuré, orienté décision — le vocabulaire est celui d'un comparateur (*« aligned decision fields »*, *« official evidence »*, *« explicit unknowns »*, *« setup effort »*, *« access risks »*), pas celui d'une page de vente.

**Style** : la page d'accueil enchaîne des blocs autonomes, chacun avec son titre-fonction et son appel à l'action — *« Choose an AI coding client with evidence »*, *« Find MCP servers for real development work »*, *« Explore Graphified trending repositories »*. Chaque bloc pourrait vivre seul, ce qui est la signature d'un site conçu pour être **atteint par recherche** plutôt que parcouru depuis l'accueil.

**Le trait le plus révélateur est la revendication de méthode.** Le site ne dit pas « les meilleurs outils » mais *« source-reviewed »*, et promet de rendre visibles les **inconnues explicites** avant une décision de changement d'outillage. C'est une posture de comparateur sérieux — et elle rend d'autant plus visible le décalage factuel du site sur son propre produit.

**Le flux d'articles trahit une stratégie de référencement assumée** : les titres suivent un gabarit répété appliqué à chaque outil nouvellement visible (*« <Outil> Knowledge Graph for Developers »*, *« <Outil> Context Engineering for Agents »*, *« <Outil> Large Codebase Context »*). Le contenu est une matrice sujet × outil, produite au rythme des sorties du marché.

## Pense-betes

- **Ce que c'est** : la propriété éditoriale de graphify, distincte du dépôt de code et de la plateforme commerciale `graphify.com`. Trois choses y cohabitent — une vitrine, un annuaire d'outils, une galerie de graphes.

- **⭐ L'annuaire est la partie qui a de la valeur pour une veille**, indépendamment du produit qu'il promeut :
  - **30 guides de clients de codage IA**, comparés sur *« workflow, agents, pricing, security, and delivery fit »*.
  - Un **répertoire de serveurs MCP** avec des critères inhabituellement bien choisis : *« transport, runtime, client support, setup effort, and access risks »* — **le dernier surtout**, rarement traité ailleurs, alors qu'un serveur MCP est une dépendance exécutable.
  - Des **comparaisons deux à deux** (Cursor contre Codex) sur champs alignés.
  → **Grille réutilisable** : transport, runtime, clients supportés, effort d'installation, risques d'accès. C'est à peu près la bonne liste pour arbitrer un serveur MCP, et elle recoupe l'avertissement de Hugo Lassiège — *« tout skill, MCP, code repris depuis l'extérieur doit être scruté »* ([[lassiege-usine-logicielle-heure-ia-2026-07-28]]).

- **⭐ La galerie de dépôts graphifiés est une démonstration à l'échelle** : **100 dépôts** de GitHub Trending, **854 079 nœuds**, **1 932 930 arêtes**, filtrables par langage (24 langages proposés) et par taille de graphe, avec pour chacun le triplet nœuds / arêtes / communautés. Deux exemples relevés : `addyosmani/agent-skills` et un thème GTK à 165 nœuds et 34 communautés. → **Montrer l'outil tourner sur des dépôts que le lecteur connaît** est une démonstration plus convaincante qu'un argumentaire, et cela produit au passage un **jeu de données public** de graphes de code comparables.

- **⚠️⚠️ Le décalage factuel entre le site et son propre produit — le vrai apport de cette fiche.** Trois écarts vérifiés le même jour :
  | Point | Ce que dit le site | Ce que dit la source |
  |---|---|---|
  | Étoiles GitHub | **« 3,7k+ »** | **103 187** (API GitHub) |
  | Licence | **« MIT »** (trois fois : carte de statistiques, corps de texte, lien de pied de page) | **Apache 2.0** (fichier `LICENSE`, branche v8) |
  | Argument principal | **« 71,5× de réduction de tokens »** | Absent du README v8, qui met en avant LOCOMO et LongMemEval |
  → **Le site décrit la génération v1 du produit.** Il présente graphify comme *« created for AI coding assistants such as Claude Code, OpenAI Codex and OpenCode »* alors que la version courante en revendique une vingtaine. **Ne jamais citer graphify.net comme source de fait sur graphify** : aller au dépôt, branche `v8`.

- **⚠️ L'erreur de licence est la plus sérieuse.** MIT et Apache 2.0 ne portent pas les mêmes obligations — la seconde impose la mention des modifications et emporte une concession expresse de brevets. Un site officiel qui annonce la mauvaise licence induit en erreur sur des points juridiquement opérants. À signaler à l'auteur plutôt qu'à répercuter.

- **Le décalage sur les étoiles a une lecture utile** : un facteur **28** entre l'affichage et la réalité indique que le site a été construit tôt puis laissé en l'état pendant que le dépôt explosait. Cela **corrobore** la trajectoire de croissance côté dépôt tout en montrant qu'aucune des deux façades n'est tenue à jour au même rythme.

- **La stratégie de contenu, à observer pour elle-même** : le site produit une matrice **sujet × outil** (graphe de connaissance, context engineering, grands dépôts, mémoire d'agent) appliquée à chaque outil qui apparaît sur le marché — GLM-5.2, Trae, Symphony, Cowart, Codex. → **Un éditeur d'outil qui construit l'annuaire de sa propre catégorie** occupe la requête d'évaluation avant que le concurrent n'y arrive. C'est le même mouvement que Cloudflare occupant l'espace de noms de l'identité agentique dans [[cloudflare-wallets-agentic-commerce-2026-08-04]] : on ne normalise pas la sémantique, on s'installe en amont de la décision.

- **⚠️ Conflit d'intérêts structurel à garder en tête** : le site compare des outils de codage IA **et** promeut l'outil de son propre auteur, référencé parmi les *« Featured Agent Skills »* aux côtés de Superpowers et des skills Anthropic. La revendication *« source-reviewed »* ne neutralise pas cette position. **Utilisable comme point d'entrée, pas comme arbitre.**

- **Multilingue** : six langues servies (anglais, chinois simplifié, chinois traditionnel de Hong Kong et de Taïwan, coréen, vietnamien) — un ciblage asiatique marqué, cohérent avec le README du dépôt disponible en 33 langues.

- **Méta / à relier** : fiche jumelle sur le produit lui-même, [[skill-shamsi-graphify-2026-08-06]] ; grille d'évaluation des serveurs MCP à rapprocher de la vigilance sur les dépendances agentiques de [[lassiege-usine-logicielle-heure-ia-2026-07-28]] ; stratégie d'occupation de la couche d'évaluation à comparer à [[cloudflare-wallets-agentic-commerce-2026-08-04]] ; annuaires et comparateurs d'outils agentiques dans [[janakiram-agent-platform-portability-contract-2026-07-20]].

## RésuméDe400mots

Site **graphify.net**, consulté le 6 août 2026, propriété officielle de **Safi Shamsi**, créateur de la skill open source graphify. Le domaine porte trois choses distinctes de la plateforme commerciale `graphify.com` et du dépôt GitHub.

**Une vitrine produit**, d'abord : présentation de graphify, guides d'usage, référence de la CLI, pages sur tree-sitter et le clustering de Leiden.

**Une galerie de démonstration**, ensuite, et c'est la partie la plus convaincante : **100 dépôts de GitHub Trending déjà graphifiés**, totalisant **854 079 nœuds et 1 932 930 arêtes**, filtrables par langage et par taille, chacun affichant son compte de nœuds, d'arêtes et de communautés, avec prévisualisation du graphe et page de détail. Montrer l'outil tourner sur des dépôts connus vaut mieux qu'un argumentaire, et produit au passage un jeu de données public de graphes comparables.

**Un annuaire éditorial**, enfin, qui a de la valeur indépendamment du produit qu'il promeut : **30 guides de clients de codage IA** comparés sur le workflow, les agents, le prix, la sécurité et l'adéquation à la livraison ; un **répertoire de serveurs MCP** évalués sur le transport, le runtime, les clients supportés, l'effort d'installation et **les risques d'accès** ; des comparaisons deux à deux sur champs alignés. Le site revendique une méthode — *« source-reviewed »*, preuves officielles, inconnues explicites — et se décline en six langues.

⚠️ **Cette fiche existe surtout pour consigner un décalage.** Le même jour, le site annonce **« 3,7k+ étoiles GitHub »** quand l'API en compte **103 187** ; il déclare **trois fois** une licence **MIT** quand le fichier `LICENSE` du dépôt est une **Apache 2.0** ; et il met en avant l'argument **« 71,5× de réduction de tokens »**, qui appartient au README de la génération v1 et a disparu de la version courante au profit de benchmarks LOCOMO et LongMemEval. Le site décrit donc un produit d'il y a plusieurs générations.

**L'erreur de licence est la plus sérieuse** : MIT et Apache 2.0 n'emportent pas les mêmes obligations, notamment sur les brevets et la mention des modifications.

Reste une observation stratégique : **un éditeur d'outil qui construit l'annuaire de sa propre catégorie** occupe la requête d'évaluation avant ses concurrents. La revendication de neutralité ne supprime pas le conflit d'intérêts — graphify figure parmi les skills mises en avant du site. Point d'entrée utile, arbitre non.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Safi Shamsi | PERSONNE | publie | graphify.net | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| graphify.net | TECHNOLOGIE | permet | de comparer des clients de codage IA et des serveurs MCP sur champs alignés | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| graphify.net | TECHNOLOGIE | recommande | d'évaluer un serveur MCP sur son transport, son runtime, ses clients supportés, son effort de mise en place et ses risques d'accès | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| graphify.net | TECHNOLOGIE | mesure | 100 dépôts graphifiés totalisant 854 079 nœuds et 1 932 930 arêtes | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| graphify.net | TECHNOLOGIE | référence | graphify | METHODOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| graphify.net | TECHNOLOGIE | affirme_que | graphify est publié sous licence MIT | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| fichier LICENSE de graphify | DOCUMENT | s_oppose_à | l'annonce d'une licence MIT sur graphify.net, en portant une Apache 2.0 | AFFIRMATION | 0.95 | STATIQUE | inféré |
| graphify.net | TECHNOLOGIE | mesure | 3 700 étoiles GitHub pour graphify, contre 103 187 relevées le même jour | MESURE | 0.93 | DYNAMIQUE | inféré |
| site officiel d'un projet | CONCEPT | s_oppose_à | la fraîcheur de son dépôt, quand la communication ne suit pas le rythme du code | AFFIRMATION | 0.85 | ATEMPOREL | inféré |
| graphify.net | TECHNOLOGIE | s_applique_à | une matrice de contenu sujet par outil, produite au rythme des sorties du marché | AFFIRMATION | 0.88 | DYNAMIQUE | inféré |
| éditeur d'outil construisant l'annuaire de sa catégorie | CONCEPT | permet | d'occuper la requête d'évaluation avant ses concurrents | AFFIRMATION | 0.85 | ATEMPOREL | inféré |
| graphify.net | TECHNOLOGIE | s_oppose_à | sa propre revendication de neutralité, en mettant en avant la skill de son auteur | AFFIRMATION | 0.85 | DYNAMIQUE | inféré |
| graphify.net | TECHNOLOGIE | est_variante_de | graphify.net | TECHNOLOGIE | 0.9 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| graphify.net | TECHNOLOGIE | définition | Propriété éditoriale officielle du projet graphify : vitrine produit, annuaire comparatif de clients de codage IA et de serveurs MCP, et galerie de 100 dépôts publics déjà graphifiés | AJOUT |
| graphify.net | TECHNOLOGIE | fiabilité | Décalé de plusieurs générations sur son propre produit au 6 août 2026 : 3 700 étoiles annoncées contre 103 187 réelles, licence MIT annoncée contre Apache 2.0 effective, argument de réduction de tokens hérité de la version v1 | AJOUT |
| Safi Shamsi | PERSONNE | rôle | Créateur de graphify et de Graphify Labs ; maintient également le site d'annuaire graphify.net, distinct de la plateforme commerciale graphify.com | MISE_A_JOUR |
| grille d'évaluation d'un serveur MCP | CONCEPT | définition | Cinq critères de décision proposés par graphify.net : transport, runtime, clients supportés, effort de mise en place et risques d'accès | AJOUT |
| annuaire d'outils tenu par un éditeur | CONCEPT | définition | Position où le fournisseur d'un outil édite le comparateur de sa propre catégorie, occupant la requête d'évaluation tout en y figurant comme option | AJOUT |
| graphify | METHODOLOGIE | catégorie | Skill open source présentée par le site, distincte du site lui-même | AJOUT |
