---
themes: [outils-plateformes, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-gitlab-orbit-graphe-contexte-2026-10-29

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **29 octobre 2026**, jour de la disponibilité générale de **GitLab Orbit** pour les paliers Premium et Ultimate sur GitLab.com (~26 000 signes, neuf sections, 17 sources notées). Orbit fournit aux agents de code un graphe en lecture seule reliant le code à ses merge requests, pipelines, déploiements et vulnérabilités, filtré par les droits GitLab de l'utilisateur. Trois apports. **(A)** Une description du périmètre : deux couches (cycle de vie, code de la **branche par défaut** seulement), langage **GQL**, une vingtaine de langages dont HCL, pas de Dockerfiles ; branchement de **Claude Code**, Codex, Cursor par `glab orbit setup` (skill, hook, fichiers d'instructions modifiés) ou par serveur **MCP**. **(B)** Une relecture des chiffres : les gains « jusqu'à **45x** moins de retries, **4,5x** moins de tokens » viennent de tests internes sans méthodologie publiée ; le seul test client publié, celui de **Compare the Market** sur **79** merge requests, mesure **0,696** de couverture avec Orbit contre **0,658** sans contexte, pour une revue quatre fois plus chère. **(C)** Prix en *query packs* (**30 $** par utilisateur et par mois pour 1 000 requêtes), quatre points de sécurité (rôles, jetons hors SSO SAML, comptes de service, rétention de 30 jours) et des consignes par lecteur. Citation de l'équipe testeuse : *« more context isn't always better; precision matters as much as coverage »*. Rejoint les fiches du corpus sur le context engineering et les graphes de code servis en MCP.

## Titre Article

GitLab Orbit en disponibilité générale : ce que le graphe de contexte change pour vos agents IA

## Date

2026-10-29

## URL

https://www.sfeir.com/articles/gitlab-orbit-graphe-contexte-agents-ia/

## Keywords

GitLab Orbit, GitLab, graphe de contexte, graphe de propriétés, context engineering, agents de code, MCP, GQL, openCypher, branche par défaut, cycle de vie logiciel, merge requests, pipelines, vulnérabilités, Claude Code, Codex, Cursor, Agent Skills, glab, CLAUDE.md, AGENTS.md, Compare the Market, revue de code IA, RAG, Codebase-Memory, Tree-sitter, query packs, GitLab Credits, permissions, SSO SAML, jetons d'accès, Riftmap

## Authors

SFEIR AI, voix éditoriale du cabinet SFEIR, article non signé individuellement, publié sur sfeir.com.

## Ton

**Profil** : analyse de lancement produit pour DSI, CTO, RSSI et acheteurs, publiée sur le site d'un cabinet. Français technique, commandes et noms de fichiers cités, un tableau de résultats.

**Registre** : chaque chiffre est rattaché à sa source et à sa nature. Les gains de GitLab sont qualifiés de *« meilleurs cas »* et d'*« annonces d'éditeur »* tant qu'ils ne sont pas reproduits ; l'article relève que la même métrique (« 45x ») désigne tantôt des retries, tantôt des hallucinations selon le support. Le test de Compare the Market est restitué avec ses trois limites telles que l'équipe les pose.

**Posture** : l'article déplace la comparaison retenue par GitLab (Orbit contre RAG) vers celle qu'il juge décisive (Orbit contre absence de contexte), puis rapporte la recommandation de l'équipe testeuse, favorable à Orbit pour les cas complexes. Il reconnaît l'apport propre d'Orbit (couche cycle de vie sous permissions existantes). Clôture sur un critère d'évaluation : *« le coût du contexte par changement accepté plutôt que […] les tokens économisés »*.

## Pense-betes

- **GA le 29 octobre 2026** : Premium et Ultimate, GitLab.com d'abord, Self-Managed et Dedicated « dans les semaines qui viennent » ; GitLab **19.5**. Thèse de GitLab : *« The model isn't the constraint. Context is. »*
- **Référence académique** : **Codebase-Memory** (Vogel et al., mars 2026, graphe Tree-sitter via MCP, 31 dépôts) — **10x** moins de tokens, 2,1x moins d'appels d'outils, qualité **83 %** contre 92 % pour l'explorateur fichier par fichier.
- **Graphe** : activé par groupe de premier niveau (Owner ou admin) ; couche **cycle de vie** (groupes, projets, MR, pipelines, work items, résultats de sécurité, mise à jour en minutes par capture de changements) ; couche **code** (fichiers, définitions, imports, appels) **sur la branche par défaut uniquement**. Requêtes en **GQL** (proche d'openCypher). Exemple partenaire : **34 M** d'entités, 7 minutes contre une demi-journée via l'API.
- **Couverture** : 12 langages en juin → ~20 dont **HCL** ; clés YAML de GitLab CI, Helm, ArgoCD, Compose sans références croisées ; **pas de Dockerfile** (confirmé le 22 octobre). Riftmap (concurrent) l'avait relevé le 12 juin.
- **Branchement** : agents Duo natifs ; `glab orbit setup` installe CLI + skill pour Claude Code, Codex, Duo, OpenCode, Pi ; écrit dans les fichiers d'instructions, ajoute un **hook** Claude Code (rappel d'`orbit grep`), autorise la skill dans `settings.json` ; avec `--project`, modifie `CLAUDE.md` et `AGENTS.md`. Conseil : passer ce changement par une MR. Serveur MCP pour les autres. Graphe local hors ligne gratuit (palier Free).
- **Chiffres GitLab** : « jusqu'à » 45x moins de retries (ou d'hallucinations selon le support), 4,5x moins de tokens, 11x plus rapide ; un billet du 13 octobre indique que 45x et 4,5x viennent d'essais séparés.
- **Compare the Market** (79 MR, MLflow sur Databricks) : couverture inline sans contexte **0,658** / Orbit **0,696** / RAG **0,577** ; coût illustratif **0,58 $** / **2,37 $** ; durée ≈ 44 s / 80,6 s / 90,8 s. Orbit + RAG n'améliore rien. Limites : test sur la bêta (graphe de code seul), métriques jugées par un LLM, échantillon réduit.
- **Prix** : query packs à **30 $** en crédits par utilisateur et par mois, **1 000** requêtes ajoutées à une réserve commune ; au-delà, 33 requêtes par crédit (~0,03 $). Question ouverte : 100 utilisateurs = 3 000 $/mois ? Bêta : **3 500** organisations, **280 000** requêtes (≈ 80 par organisation).
- **Sécurité** : aucune permission propre, chaque résultat revérifié ; Reporter sans données de sécurité ; jetons à granularité fine **non soumis au SSO SAML** ; pas d'accès admin/auditeur aux comptes de service ; graphe conservé **30 jours** après désactivation.
- **Positionnement** : apport propre = couche cycle de vie ; limite = ne voit que GitLab (code réparti GitLab/GitHub couvert en partie).

## RésuméDe400mots

Depuis le 29 octobre 2026, GitLab Orbit est en disponibilité générale pour les clients Premium et Ultimate, d'abord sur GitLab.com. L'outil donne aux agents de code un graphe qui relie le code aux merge requests, pipelines, déploiements et vulnérabilités, filtré par les droits GitLab de l'utilisateur. GitLab défend une thèse : la contrainte n'est plus le modèle mais le contexte. SFEIR la rapproche d'un travail académique sur les graphes de code servis en MCP, qui divise les tokens par dix au prix de neuf points de qualité.

Orbit construit, par groupe, un graphe en lecture seule à deux couches : le cycle de vie, mis à jour en quelques minutes, et le code, limité à la branche par défaut. Les agents l'interrogent dans un langage proche d'openCypher. La couverture s'est élargie depuis la bêta, jusqu'à Terraform, mais ne lit pas les Dockerfiles et ne relie pas les fichiers Helm entre eux. Les agents de GitLab l'utilisent nativement ; Claude Code, Codex et d'autres s'y branchent par une commande qui installe une skill et modifie les fichiers d'instructions des agents, ou par un serveur MCP. SFEIR conseille de faire passer ces modifications par une merge request.

Les gains annoncés, jusqu'à 45 fois moins de retries et 4,5 fois moins de tokens, viennent de tests internes sans jeu de tâches publié. Le seul test client public, celui de Compare the Market sur 79 merge requests, montre qu'Orbit dépasse nettement le RAG, mais ne gagne que moins de quatre points de couverture sur la configuration sans contexte, pour une revue quatre fois plus chère et presque deux fois plus lente. L'équipe recommande néanmoins un outil fondé sur l'arbre syntaxique pour les cas complexes et la seule lecture du diff pour les cas simples, et conclut que la précision du contexte compte autant que sa couverture.

Orbit se vend en packs de requêtes partagés par l'organisation, à 30 dollars par utilisateur et par mois ; la règle de décompte reste à clarifier, et l'usage pendant la bêta était faible. Côté sécurité, Orbit ne crée aucune permission propre, mais quatre points sont à vérifier : rôles, jetons qui survivent à la session SAML, comptes de service trop larges, rétention de trente jours.

SFEIR recommande de profiter de l'essai de trente jours pour rejouer des tâches réelles avec et sans Orbit, même agent et même modèle, et de juger l'outil sur le coût du contexte par changement accepté.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | GitLab Orbit en disponibilité générale | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| GitLab | ORGANISATION | publie | GitLab Orbit | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| GitLab Orbit | TECHNOLOGIE | permet | graphe de contexte | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| GitLab Orbit | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| GitLab Orbit | TECHNOLOGIE | utilise | GQL | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| GitLab Orbit | TECHNOLOGIE | s_applique_à | Claude Code | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| GitLab Orbit | TECHNOLOGIE | est_instance_de | context engineering | METHODOLOGIE | 0.85 | ATEMPOREL | inféré |
| GitLab | ORGANISATION | affirme_que | jusqu'à 45 fois moins de retries et 4,5 fois moins de tokens avec Orbit | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Compare the Market | ORGANISATION | mesure | couverture inline 0,696 avec Orbit contre 0,658 sans contexte et 0,577 en RAG | MESURE | 0.92 | STATIQUE | déclaré_article |
| GitLab Orbit | TECHNOLOGIE | surpasse | RAG | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Compare the Market | ORGANISATION | affirme_que | more context isn't always better; precision matters as much as coverage | CITATION | 0.9 | ATEMPOREL | déclaré_article |
| Ryan Harvey | PERSONNE | travaille_chez | Compare the Market | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| Codebase-Memory | DOCUMENT | mesure | dix fois moins de tokens, qualité 83 % contre 92 % | MESURE | 0.88 | STATIQUE | déclaré_article |
| Codebase-Memory | DOCUMENT | utilise | Tree-sitter | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Riftmap | ORGANISATION | concurrence | GitLab | ORGANISATION | 0.8 | DYNAMIQUE | déclaré_article |
| GitLab Orbit | TECHNOLOGIE | concurrence | Augment Code Context Engine | TECHNOLOGIE | 0.75 | DYNAMIQUE | inféré |
| SFEIR | ORGANISATION | recommande | juger Orbit sur le coût du contexte par changement accepté, mesuré sur ses propres tâches | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | faire passer par une merge request les modifications de CLAUDE.md et AGENTS.md écrites par glab orbit setup | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| GitLab Orbit | TECHNOLOGIE | catégorie | Graphe de contexte en lecture seule pour agents (cycle de vie + code de la branche par défaut), GA le 29/10/2026 | AJOUT |
| GitLab Orbit | TECHNOLOGIE | prix | Query packs : 30 $ en crédits par utilisateur et par mois pour 1 000 requêtes | AJOUT |
| GitLab | ORGANISATION | secteur | Plateforme DevSecOps | AJOUT |
| graphe de contexte | CONCEPT | définition | Graphe reliant code, changements, pipelines, vulnérabilités et propriété, servi aux agents | AJOUT |
| GQL | TECHNOLOGIE | catégorie | Langage de requête de graphe en lecture seule, proche d'openCypher | AJOUT |
| Compare the Market | ORGANISATION | secteur | Comparateur britannique, seul test client publié d'Orbit (79 merge requests) | AJOUT |
| Ryan Harvey | PERSONNE | rôle | Responsable de l'ingénierie IA de Compare the Market | AJOUT |
| Codebase-Memory | DOCUMENT | référence | Vogel et al., arXiv:2603.27277, mars 2026 | AJOUT |
| Riftmap | ORGANISATION | secteur | Analyse d'impact entre dépôts, concurrent d'Orbit | AJOUT |
