---
themes: [produits-services, agents-codage-ia-skills, qualite-securite, economie-marche]
source: "Mistral AI"
---
# mistral-large-4-le-chonk-2026-10-06

## Veille

Billet de blog de **Mistral AI** (signé « By Mistral », 11 min de lecture), daté du **6 octobre 2026**, qui annonce la préversion publique de **Mistral Large 4** (ML4, surnommé « le Chonk » par l'éditeur) : un modèle multimodal natif de **1 000 milliards de paramètres dont 49 milliards actifs**, entraîné de zéro sur **3 800 GPU NVIDIA Grace Blackwell** dans les datacenters européens de Mistral. API de préversion disponible sur Mistral Studio ; **poids ouverts annoncés pour la fin du mois**.

**(1)** Cybersécurité : 82 % sur le test de reproduction puis correction d'une vulnérabilité de l'**Artificial Analysis Cyber Index** (le plus haut score cité), 93 % sur **Cybench** ; le billet indique que **Claude Opus 5.5** et **GPT-6 Astra** obtiennent un score proche de zéro sur ce test parce qu'ils refusent la tâche. **(2)** Code agentique : 61,7 % sur DeepSWE v1.1, 28,3 % sur Terminal-Bench 4, évaluation humaine Surge AI 3,74/5 (deuxième sur cinq, derrière Claude Opus 5 à 4,22). **(3)** Finance et droit : devant GPT-6 Astra selon vals.ai, premier des modèles ouverts sur le benchmark juridique de Harvey. **(4)** Entraînement par apprentissage par renforcement à grande échelle, financé par la série D de **3 milliards d'euros**. Tarif affiché : **1,36 $** (entrée) et **4,18 $** (sortie) par million de tokens.

Rapproche l'argument sur les refus en cybersécurité de [[fasano-fleischer-anthropic-glm-5-3-advanced-cyber-capabilities-2026-09-29]].

## Titre Article

Introducing Mistral Large 4

## Date

2026-10-06

## URL

https://mistral.ai/news/mistral-large-4/

## Keywords

Mistral Large 4, ML4, le Chonk, Mistral AI, poids ouverts, modèle MoE, multimodal, cybersécurité, souveraineté de l'IA, Europe, code agentique, DeepSWE, Terminal-Bench, Cybench, Artificial Analysis Cyber Index, apprentissage par renforcement, Mistral Forge, Harvey, vals.ai, robustesse aux injections de prompt, 160 langues, série D

## Authors

Mistral AI — éditeur de modèles d'IA ; billet de blog de l'entreprise (« By Mistral »).

## Ton

Profil : annonce produit d'éditeur à destination de décideurs techniques et d'entreprises, structurée par domaines de capacités (cybersécurité, code agentique, flux agentiques, multimodal, science et maths, travail de la connaissance, sécurité du modèle), avec onglets de benchmarks et quatre démonstrations interactives. Le texte alterne chiffres, comparaisons nommées et argumentaire de souveraineté (« Forged in Europe. Built for AI sovereignty »). Il emploie un surnom familier pour le modèle et précise le statut provisoire du produit : préversion, apprentissage par renforcement « toujours en cours », architecture, benchmarks supplémentaires et méthode de post-entraînement promis avec la publication des poids. Les évaluations citées combinent des tiers (Artificial Analysis, vals.ai, Surge AI, Lakera, HarveyAI) et des évaluations internes.

## Pense-betes

- **Modèle** : 1 000 Md de paramètres, 49 Md actifs, multimodal natif, hybride instruction et raisonnement ; plus de **160 langues**, dont toutes les langues officielles de l'UE. Entraîné avec l'environnement d'entraînement, de personnalisation et d'apprentissage par renforcement proposé aux clients via **Mistral Forge**, avec des entreprises de la finance, de l'industrie, de la logistique, de la pharmacie et du secteur public.
- **Calendrier** : préversion API aujourd'hui, poids avant la fin du mois. Avant cela, test en conditions réelles (red teaming) avec des responsables de la cybersécurité, des partenaires vérifiés et des autorités d'État, avec une modération réduite et des capacités cyber étendues.
- **Cybersécurité** : parmi les cinq premiers modèles de l'AA Cyber Index et en tête des modèles ouverts hors Chine ; 82 % sur reproduction plus correction de vulnérabilité, 93 % sur Cybench. Le billet explique que les refus des modèles fermés bloquent la recherche de vulnérabilités et la réponse à incident, et qu'un accès perdu en pleine crise est un risque ; il met en avant le déploiement privé ou sur site.
- **Code et agents** : 59,4 % sur SWE-Atlas-QnA, Coding Agent Index de 49,8 % devant DeepSeek V4 Pro 0813 et Qwen3.8 Max ; 59,9 % sur AutomationBench (657 workflows) ; 1 393 Elo sur AA-Briefcase.
- **Multimodal** : visuel et agentique combinés (imagerie satellite gigapixel, plans techniques) ; 42 % contre 41 % pour GPT-6 Astra sur Dense 200 (ancrage visuel).
- **Sécurité du modèle** : 93,3 % d'attaques repoussées sur le B3 de Lakera ; score KORA de 1,691 sur 2 ; taux de refus des requêtes malveillantes en cyber, selon le billet, plus élevé que pour tous les modèles ouverts comparés.
- **Apprentissage par renforcement** : bibliothèque d'environnements composables (sandboxes de code, recherche web, API), vérifications combinées (modèles de récompense, tests, juges LLM) ; avec 3 000 GPU, environ **33 milliards de tokens par jour**, dont ~16 milliards entraînables ; budgets de rollout de plusieurs millions de tokens.
- **Suite** : ML4 est présenté comme première étape de la feuille de route financée par la **série D de 3 Md€** et comme base d'une nouvelle génération de modèles spécialisés.
- ⚠️ **Portée** : préversion ; l'architecture détaillée et la méthode de post-entraînement ne sont pas publiées. Les comparaisons sont celles de Mistral, avec des choix de concurrents propres au billet, et plusieurs scores sont donnés sans le tableau complet dans le texte (graphiques à onglets).

## RésuméDe400mots

Mistral AI annonce le 6 octobre 2026 la préversion publique de Mistral Large 4, ou ML4, surnommé « le Chonk ». Le modèle compte 1 000 milliards de paramètres dont 49 milliards actifs, est multimodal de façon native et a été entraîné de zéro sur 3 800 GPU NVIDIA Grace Blackwell dans les datacenters européens de l'entreprise. L'API de préversion est disponible sur Mistral Studio ; les poids seront publiés avant la fin du mois, après une phase de test en conditions réelles avec des responsables de la cybersécurité, des partenaires vérifiés et des autorités d'État, qui accèdent à une version à modération réduite et capacités cyber étendues.

Mistral présente ML4 comme proche des meilleurs modèles ouverts du monde et nettement devant tout modèle ouvert américain ou européen, avec un état de l'art parmi les modèles ouverts en cybersécurité, finance et droit, et des résultats supérieurs à certains modèles fermés en ancrage visuel.

En cybersécurité, le modèle se classe dans les cinq premiers de l'Artificial Analysis Cyber Index et mène les modèles ouverts hors Chine. Sur le test de reproduction puis de correction d'une vulnérabilité, il obtient 82 %, le plus haut score cité, et 93 % sur Cybench. Le billet explique que Claude Opus 5.5 et GPT-6 Astra sont proches de zéro sur ce test parce qu'ils refusent la tâche, alors que défendre un logiciel commence souvent par prouver qu'une faille est réelle. Il en déduit l'intérêt de modèles ouverts, déployables en privé ou sur site, sous la politique de l'organisation.

En code agentique, ML4 atteint 61,7 % sur DeepSWE v1.1, 59,4 % sur SWE-Atlas-QnA et 28,3 % sur Terminal-Bench 4, soit 49,8 % à l'indice combiné, devant DeepSeek V4 Pro 0813 et Qwen3.8 Max. Une évaluation humaine en aveugle par Surge AI le place deuxième sur cinq (3,74), derrière Claude Opus 5 (4,22). En flux agentiques, il obtient 59,9 % sur AutomationBench et 1 393 Elo sur AA-Briefcase. Sur le travail de la connaissance, vals.ai le place devant GPT-6 Astra en finance et en droit, et il devance les autres modèles ouverts sur le benchmark juridique de Harvey. La section sécurité cite 93,3 % d'attaques repoussées sur le benchmark B3 de Lakera et un taux de refus des requêtes cyber malveillantes plus élevé que celui des modèles ouverts comparés.

Sur la méthode, Mistral décrit une bibliothèque d'apprentissage par renforcement composable, où sandboxes, recherche web, API et vérificateurs (modèles de récompense, tests, juges) se combinent. Avec 3 000 GPU, un entraînement produit environ 33 milliards de tokens par jour. ML4 est la première étape de la feuille de route financée par la série D de 3 milliards d'euros et servira de base à des modèles spécialisés. Le tarif est de 1,36 dollar par million de tokens en entrée et 4,18 dollars en sortie.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Mistral AI | ORGANISATION | publie | Mistral Large 4 | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | mesure | 1 000 milliards de paramètres dont 49 milliards actifs | MESURE | 0.97 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | utilise | GPU NVIDIA Grace Blackwell | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Mistral AI | ORGANISATION | recommande | déployer ML4 en privé ou sur site pour les opérations de sécurité | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | mesure | 82 % sur reproduction puis correction de vulnérabilité (AA Cyber Index) | MESURE | 0.95 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | mesure | 93 % sur Cybench | MESURE | 0.95 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | surpasse | Claude Opus 5.5 | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | surpasse | GPT-6 Astra | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | surpasse | DeepSeek V4 Pro | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Claude Opus 5 | TECHNOLOGIE | surpasse | Mistral Large 4 | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | mesure | 61,7 % sur DeepSWE v1.1 | MESURE | 0.95 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | mesure | 3,74 sur 5 à l'évaluation humaine Surge AI | MESURE | 0.93 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | mesure | 93,3 % d'attaques repoussées sur Lakera B3 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Mistral AI | ORGANISATION | affirme_que | les refus des modèles fermés bloquent la recherche de vulnérabilités et la réponse à incident | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | utilise | Mistral Forge | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | utilise | apprentissage par renforcement | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| série D de 3 Md€ | EVENEMENT | permet | la feuille de route de développement du modèle | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Mistral Large 4 | TECHNOLOGIE | permet | souveraineté de l'IA | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Mistral AI | ORGANISATION | secteur | Modèles d'IA, souveraineté, datacenters européens | AJOUT |
| Mistral Large 4 | TECHNOLOGIE | catégorie | Modèle MoE multimodal, 1 000 Md de paramètres (49 Md actifs), préversion le 6 octobre 2026, poids annoncés fin octobre ; 1,36 $ / 4,18 $ par million de tokens | AJOUT |
| GPU NVIDIA Grace Blackwell | TECHNOLOGIE | catégorie | Matériel d'entraînement de ML4 (3 800 GPU) | AJOUT |
| Claude Opus 5.5 | TECHNOLOGIE | catégorie | Modèle fermé comparé sur le test cyber | AJOUT |
| Claude Opus 5 | TECHNOLOGIE | catégorie | Modèle fermé en tête de l'évaluation humaine de code Surge AI (4,22) | AJOUT |
| GPT-6 Astra | TECHNOLOGIE | catégorie | Modèle fermé comparé en cyber, finance, droit et ancrage visuel | AJOUT |
| DeepSeek V4 Pro | TECHNOLOGIE | catégorie | Modèle ouvert comparé sur code et flux agentiques | AJOUT |
| Mistral Forge | TECHNOLOGIE | catégorie | Offre d'entraînement, personnalisation et environnement RL pour les clients de Mistral | AJOUT |
| apprentissage par renforcement | CONCEPT | définition | Post-entraînement sur les résultats des tentatives du modèle, à difficulté croissante | AJOUT |
| souveraineté de l'IA | CONCEPT | définition | Contrôle des clients sur déploiement, données et politiques, avec hébergement européen | AJOUT |
| série D de 3 Md€ | EVENEMENT | définition | Plus grande levée de fonds en capital d'une entreprise technologique européenne selon Mistral | AJOUT |
