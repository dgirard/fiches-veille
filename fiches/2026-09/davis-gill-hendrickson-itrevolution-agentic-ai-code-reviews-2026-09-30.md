---
themes: [qualite-securite, agents-codage-ia-skills, strategie-frameworks]
source: "Enterprise Technology Leadership Journal"
---
# davis-gill-hendrickson-itrevolution-agentic-ai-code-reviews-2026-09-30

## Veille

Article collectif de sept auteurs (**Zach Davis**, **Michelle Gill**, **Elisabeth Hendrickson**, **Angie Jones**, **Sha Ma**, **Randy Shoup**, **James Wickett**), paru dans l'*Enterprise Technology Leadership Journal* d'**IT Revolution** (automne 2026, vol. 3, n° 2), sous licence CC BY-NC-SA. Environ **7 500 mots**, intitulé *« Toward a Pattern Language for Code Reviews in the Age of Agentic AI »*. **(A)** Cadrage : la revue de code est définie comme un examen par une entité non auteur menant à une action ; les études empiriques (Microsoft 2013, Mäntylä 2009, Beller 2014) montrent que la valeur tient surtout à la maintenabilité et au partage de connaissance, moins aux défauts fonctionnels. **(B)** Trois conditions pour sortir l'humain du chemin critique : validation déterministe maximale, revue **graduée par le risque**, **trace durable** de chaque décision d'agent ; *« no human in the loop »* est un choix de configuration, pas une valeur par défaut. **(C)** Neuf patrons composables, présentés comme une boîte à outils et non une échelle de maturité : petits changements, Shift Left, conception pour la vérification, pratiques d'ingénierie déterministes, ingénierie de contexte, boucle de qualité continue, revue LLM adverse, revues multi-agents, développement piloté par la spécification. **(D)** Trois études de cas : **Block**, **Cloudflare** (131 246 revues sur 48 095 PR en un mois, 1,2 constat par revue), **DryRun Security**. Prolonge les fiches du corpus sur l'ingénierie de contexte et la revue de code assistée.

## Titre Article

Agentic AI and Code Reviews: Toward a Pattern Language for Code Reviews in the Age of Agentic AI

## Date

2026-09-30

## URL

https://reader.itrevolution.com/download/agentic-ai-and-code-reviews?via=itrevolution

## Keywords

revue de code agentique, code review, langage de patrons, patron, revue adverse, revue multi-agents, boucle de qualité continue, shift left, vérification déterministe, revue graduée par le risque, ingénierie de contexte, AGENTS.md, développement piloté par la spécification, petits changements, PR empilées, piste d'audit, humain dans la boucle, Zero Trust, indépendance structurelle, Block, Cloudflare, OpenCode, DryRun Security, IT Revolution, dark software factory

## Authors

Zach Davis (LaunchDarkly), Michelle Gill (Engineered by AI), Elisabeth Hendrickson (Curious Duck), Angie Jones (Agentic AI Foundation), Sha Ma (Topogy), Randy Shoup (CircleCI), James Wickett (DryRun Security) ; article collectif, IT Revolution.

## Ton

**Profil** : papier de recherche-praticiens destiné aux dirigeants techniques, publié dans une revue éditoriale de l'écosystème DevOps. Les auteurs viennent d'éditeurs d'outils (LaunchDarkly, CircleCI, DryRun Security, Topogy) et de conseil ; la revue précise que des outils d'IA ont pu aider à la rédaction.

**Style** : structuré en patrons à gabarit constant (problème, applicabilité, mécanisme, rôle de l'humain, liens avec les autres patrons), référencé à Christopher Alexander. Phrases générales et normatives, peu de chiffres hors du cas Cloudflare.

**Position épistémique** : proposition de cadre, non évaluée par la mesure. Les études de cas sont rédigées par ou avec les entreprises concernées ; seul Cloudflare donne des volumes. L'article nomme lui-même les limites de l'IA (jugement d'architecture, impact inter-systèmes, concurrence subtile, très gros changements). Deux auteurs dirigent des éditeurs de produits de revue ou de vérification, ce que la page des auteurs indique.

## Pense-betes

- **Définition de la revue de code** : examen du code par une entité non auteure, aboutissant à un jugement suivi d'une action (fusion, rejet, retour). Distingue la revue d'une lecture casuelle ; l'entité peut être un agent.
- **Valeur empirique** : la revue est sans doute surestimée comme détecteur de défauts et sous-estimée comme **triage de risque** ; la majorité des constats portent sur l'évolutivité (maintenabilité, style, partage).
- **Trois conditions** pour retirer l'humain du chemin critique : (1) déterministe d'abord (tests, analyse statique, politiques en code), l'agent ne traite que le résidu subjectif ; (2) revue **graduée** de « aucun humain » à autorisation explicite ; (3) **enregistrement inspectable** de ce qui a été évalué, sous quelles politiques, avec quelle confiance, par qui.
- **Placement dans le cycle** : en rédaction (retour rapide), avant fusion (politique, architecture, régressions), après fusion (dérives système), avant production (gouvernance de release).
- ⭐ **Boucle de qualité continue** : agent auteur et agent relecteur en cycle en six étapes (production, examen, retour structuré, correction, réévaluation, arrêt sur critère : passe propre, nombre max d'itérations ou risque résiduel acceptable). Le relecteur ne traite pas ce que les linters font ; il doit **vérifier que la correction a marché** et ne pas chercher de nouveaux problèmes une fois les anciens réglés.
- **Revue LLM adverse** : indépendance structurelle entre génération et évaluation. Trois formes : inter-modèles, inter-sessions (même modèle, contexte isolé, invite critique), invite adverse structurée. Analogies avec les GAN et le Zero Trust (vérification explicite, moindre privilège). Réserver aux chemins sensibles : coût et bruit.
- **Revues multi-agents** : spécialistes (sécurité, performance, conformité, standards, exactitude, exploitabilité), agent de triage, **coordinateur** (déduplication, sévérité, politique bloquant/consultatif), routage de contexte. Le coût croît avec le nombre de spécialistes ; la qualité du coordinateur conditionne la confiance.
- **Ingénierie de contexte** : l'agent a besoin de l'architecture, des contrats d'API, des incidents, des commentaires de revue passés, des compromis acceptés. Sans cela : constats bruyants et superficiels. Le rôle humain devient celui de **curateur**.
- **Spécification d'abord** : déplacer le point de contrôle de l'implémentation vers le plan ; l'humain relit l'intention, l'agent adverse vérifie la fidélité à la spécification.
- **Cloudflare** : orchestration en CI autour d'OpenCode, reviewers spécialisés et coordinateur, revue graduée, filtrage des lockfiles et artefacts générés, politique biaisée vers l'approbation, « break glass » humain, reprise des constats entre commits. **131 246 revues, 48 095 PR, 5 169 dépôts, 159 103 constats** (mars-avril 2026).
- **Block** : 3 500 ingénieurs, 90 % utilisant l'IA quotidiennement mi-2025 ; les PR d'agents restent en brouillon faute de propriété ; relecteurs maison bruyants puis outils commerciaux plus utiles ; PR empilées, revue adverse locale avant push.
- **DryRun** : faille d'isolation multi-locataire en bêta (2023) transformée en politique de code ; retour en trente secondes ; test d'exploitabilité.
- ⚠️ **Limites** : cadre non mesuré hors Cloudflare ; cas d'éditeurs décrivant leur propre pratique.

## RésuméDe400mots

L'article propose un langage de patrons pour la revue de code à l'ère des agents. Il part d'un constat : les agents accélèrent le volume de changements, les ingénieurs seniors reçoivent des dizaines de demandes de revue par jour, et la revue humaine exhaustive n'est plus tenable. La revue de code est définie comme l'examen du code par une entité qui n'en est pas l'auteur, aboutissant à un jugement suivi d'une action. Les études empiriques citées montrent que sa valeur tient autant à la maintenabilité, à la découverte d'alternatives et au partage de connaissance qu'à la détection de bugs ; elle serait surtout un mécanisme de triage du risque.

Pour retirer l'humain du chemin critique, trois conditions sont posées. Il faut déplacer un maximum de validation vers des contrôles déterministes, pour que les agents ne traitent que l'espace subjectif résiduel. La revue doit être graduée par le risque, de l'absence d'humain à l'autorisation explicite. Et chaque décision d'agent doit laisser une trace durable de ce qui a été évalué, sous quelles politiques, avec quelle confiance. Travailler sans humain dans la boucle est un choix de configuration justifié par le risque et la preuve.

Neuf patrons composent la boîte à outils : petits changements incrémentaux, Shift Left, conception pour la vérification, pratiques d'ingénierie déterministes, ingénierie de contexte, boucle de qualité continue, revue LLM adverse, revues multi-agents, développement piloté par la spécification. La boucle continue fait dialoguer un agent auteur et un agent relecteur jusqu'à un critère de convergence. La revue adverse apporte l'indépendance structurelle, par un autre modèle ou une session isolée. Les revues multi-agents répartissent le travail entre spécialistes, un agent de triage et un coordinateur. L'ingénierie de contexte conditionne le reste : sans elle, les constats sont bruyants.

Trois cas illustrent. Block, face à des PR d'agents laissées sans revue, est passé de relecteurs maison bruyants à des outils commerciaux, aux PR empilées, à la revue adverse locale et à la correction automatique en CI. Cloudflare a construit une orchestration en CI autour d'OpenCode : reviewers spécialisés, coordinateur, revue graduée, filtrage des fichiers bruyants, contournement humain, reprise des constats d'un commit à l'autre. Sur un mois, 131 246 revues couvrent 48 095 PR dans 5 169 dépôts, avec 1,2 constat par revue en moyenne. DryRun Security a fait d'une faille d'isolation entre locataires une politique vérifiée à chaque changement.

En conclusion, les auteurs présentent la transition comme une réorganisation des responsabilités : spécifications précises, vérification indépendante, pistes d'audit durables. La question directrice : si quelque chose n'allait pas, comment le saurait-on ?

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Zach Davis | PERSONNE | travaille_chez | LaunchDarkly | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| Randy Shoup | PERSONNE | travaille_chez | CircleCI | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| James Wickett | PERSONNE | dirige | DryRun Security | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| IT Revolution | ORGANISATION | publie | article Agentic AI and Code Reviews | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| article Agentic AI and Code Reviews | DOCUMENT | recommande | revue graduée par le risque, avec trace durable de chaque décision d'agent | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| article Agentic AI and Code Reviews | DOCUMENT | affirme_que | « No human in the loop » est un choix de configuration justifié par le risque et la preuve, non une valeur par défaut | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| revue adverse LLM | METHODOLOGIE | améliore | l'indépendance entre génération et évaluation, par un modèle ou une session distincts | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| revue adverse LLM | METHODOLOGIE | s_inspire_de | Zero Trust | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| boucle de qualité continue | METHODOLOGIE | utilise | revue adverse LLM | METHODOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |
| revues multi-agents | METHODOLOGIE | utilise | agent coordinateur | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| ingénierie de contexte | METHODOLOGIE | permet | des constats de revue moins bruyants et plus pertinents | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| développement piloté par la spécification | METHODOLOGIE | s_applique_à | la revue de l'intention avant l'écriture du code | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Cloudflare | ORGANISATION | a_créé | système de revue de code en CI | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| système de revue de code en CI | TECHNOLOGIE | utilise | OpenCode | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| système de revue de code en CI | TECHNOLOGIE | mesure | 131 246 revues sur 48 095 PR dans 5 169 dépôts, 159 103 constats, soit 1,2 par revue (mars-avril 2026) | MESURE | 0.95 | STATIQUE | déclaré_article |
| Block | ORGANISATION | utilise | revue adverse locale avant push | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Block | ORGANISATION | observé_dans | PR d'agents laissées en brouillon faute de propriété | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| DryRun Security | ORGANISATION | utilise | test d'exploitabilité | METHODOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| article Agentic AI and Code Reviews | DOCUMENT | référence | étude Microsoft sur la revue de code moderne | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| article Agentic AI and Code Reviews | DOCUMENT | affirme_que | « Generating code is cheap, but organizational attention is not. » | CITATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| IT Revolution | ORGANISATION | secteur | Éditeur DevOps, revue Enterprise Technology Leadership Journal | AJOUT |
| LaunchDarkly | ORGANISATION | secteur | Gestion de feature flags | AJOUT |
| CircleCI | ORGANISATION | secteur | Intégration continue | AJOUT |
| DryRun Security | ORGANISATION | secteur | Revue de sécurité contextuelle en pré-fusion | AJOUT |
| Cloudflare | ORGANISATION | secteur | Infrastructure réseau ; revue de code IA en CI | AJOUT |
| Block | ORGANISATION | secteur | Paiement ; 3 500 ingénieurs | AJOUT |
| Zach Davis | PERSONNE | rôle | Principal Engineer, LaunchDarkly | AJOUT |
| James Wickett | PERSONNE | rôle | CEO et cofondateur de DryRun Security | AJOUT |
| Randy Shoup | PERSONNE | rôle | SVP Engineering, CircleCI | AJOUT |
| article Agentic AI and Code Reviews | DOCUMENT | forme | Article collectif en neuf patrons, trois études de cas | AJOUT |
| revue adverse LLM | METHODOLOGIE | définition | Revue par un modèle ou une session indépendants de l'auteur | AJOUT |
| boucle de qualité continue | METHODOLOGIE | définition | Cycle agent auteur / agent relecteur jusqu'à convergence | AJOUT |
| revues multi-agents | METHODOLOGIE | définition | Spécialistes, triage et coordinateur | AJOUT |
| ingénierie de contexte | METHODOLOGIE | définition | Rendre architecture, précédents et politiques accessibles aux agents | AJOUT |
| développement piloté par la spécification | METHODOLOGIE | définition | Déplacer la revue de l'implémentation vers le plan | AJOUT |
| système de revue de code en CI | TECHNOLOGIE | catégorie | Orchestration multi-reviewers de Cloudflare | AJOUT |
| OpenCode | TECHNOLOGIE | catégorie | Agent de codage open source | AJOUT |
| Zero Trust | CONCEPT | définition | Aucun artefact ni contributeur n'est de confiance par défaut | AJOUT |
| agent coordinateur | CONCEPT | définition | Synthétise, dédoublonne et hiérarchise les constats des spécialistes | AJOUT |
| test d'exploitabilité | METHODOLOGIE | définition | Raisonner sur l'abus réel d'une faille dans son contexte | AJOUT |
| revue adverse locale avant push | METHODOLOGIE | définition | Agent adverse invoqué localement avant le push | AJOUT |
| étude Microsoft sur la revue de code moderne | DOCUMENT | référence | Bacchelli et Bird, ICSE 2013 | AJOUT |
