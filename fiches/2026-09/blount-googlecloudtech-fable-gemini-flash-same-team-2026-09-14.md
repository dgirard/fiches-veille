---
themes: [outils-plateformes, agents-codage-ia-skills, economie-marche]
source: "X @GoogleCloudTech (Alan Blount)"
---
# blount-googlecloudtech-fable-gemini-flash-same-team-2026-09-14

## Veille

Article long publié le **14 septembre 2026** sur le compte X **@GoogleCloudTech** (~2 000 mots, quatre étapes, six blocs de commandes et de configuration), signé **Alan Blount**, Technical Solutions Consultant chez Google. Point de départ : une question anodine, confiée à un agent de recherche, facturée **38 $**. L'article propose de faire cohabiter **Claude Fable 5.1** et **Gemini 3.8 Flash** derrière la même API de **Gemini Enterprise Agent Platform** (anciennement Vertex AI). **(1) Configuration** : accès à Fable soumis à l'*Advanced AI Safety Addendum* de Google Cloud, qui impose un appel `setPublisherModelConfig` avec partage prompt-réponse activé pour Anthropic, sous peine d'un 403 ; Flash fonctionne dès l'activation. **(2) Benchmark maison** avec promptfoo pilotant opencode sur deux tâches : sur un état de branche git, Flash répond en **1,1 s** pour moins d'un dixième de cent quand Fable coûte **23 fois plus** ; sur une migration Postgres vers Spanner, Fable produit en **12 s** un DAG formel avec risques de dérive d'horloge et porte de rollback, là où Flash livre une séquence linéaire en 3 s. **(3) Usage** : *« asymmetric coordination »* — le modèle rapide en coordinateur de première ligne, le planificateur profond aux points de contrôle, un outil `ask_for_help` pour l'escalade, et une mise en garde contre les routeurs dynamiques : *« Keep it boring »*. **(4) ROI des tokens** : valeur du temps humain, des fonctionnalités livrées et des incidents évités, moins le coût des tokens et de la montée en compétence. Même geste de routage par frontière de tâche que [[mazmanov-portal-spotify-shunt-claude-code-tokens-2026-09-03]], dans le cadre FinOps posé par [[rafal-wenvision-tokenomics-foundation-finops-ia-2026-06-04]].

## Titre Article

Put Claude Fable 5.1 and Gemini 3.8 Flash on the same team

## Date

2026-09-14

## URL

https://x.com/GoogleCloudTech/status/2099507349828350285

## Keywords

routage de modèles, coordination asymétrique, tokenomics, ROI des tokens, Claude Fable 5.1, Gemini 3.8 Flash, Gemini Enterprise Agent Platform, Vertex AI, Model Garden, Advanced AI Safety Addendum, setPublisherModelConfig, partage prompt-réponse, opencode, promptfoo, benchmark maison, évaluations, sous-agents spécialisés, deep-thinker, worker, escalade ask_for_help, routeurs dynamiques, multi-armed bandits, frontière de tâche, migration Postgres Spanner, DAG, Google ADK, LangGraph, thinking level, quota, débit provisionné

## Authors

Alan Blount (Technical Solutions Consultant, Google Cloud, @zeroasterisk), publié sur le compte X @GoogleCloudTech.

## Ton

**Profil** : tutoriel d'ingénieur publié sur un compte éditorial de Google Cloud, à la première personne, qui promeut la plateforme de l'entreprise tout en en décrivant les frictions. Public : développeurs qui montent des agents de codage ou des services d'agents sur mesure, et responsables du coût d'inférence.

**Style** : progression en quatre étapes numérotées, chacune close par des artefacts exécutables — variables d'environnement, appels curl, réponses JSON attendues, codes d'erreur 409 et 403 avec leur message exact, fichiers `opencode.json` et `promptfooconfig.yaml`. L'humour d'auto-dérision (*« impossible things are easy, but easy things are hard »*, *« whew. We did it 🎉 »*) reconnaît la lourdeur du parcours d'activation. Les formules courtes servent de règles : *« That is a mistake »*, *« Keep it boring »*.

**Position épistémique** : l'auteur refuse d'emblée les classements publics (*« Twitter vibes and synthetic leaderboards »*) et pose sa propre comparaison comme *« one illustrative example »* à refaire sur ses tâches. Les mesures données (1,1 s, 23 fois, 12 s) portent sur deux tâches dans un conteneur propre, sans répétition ni protocole détaillé. Les taux d'escalade (85 à 90 % traités par le worker) et le seuil de 3 à 5 outils sont énoncés comme heuristiques, sans source. L'équation de ROI est explicitement présentée comme impossible à généraliser. Le texte est un contenu de plateforme : les modèles cités sont ceux que Google Cloud distribue, et le renvoi final pointe vers d'autres publications du même compte.

## Pense-betes

- **Le cas fondateur est un mauvais ROI, pas une panne** : une question sans enjeu, un agent qui fouille chats et documents, la bonne réponse, 38 $. La tâche ne demandait pas de planification coûteuse. C'est la valeur marginale du token, discutée dans [[gupta-token-budget-wars-marginal-token-utility-2026-05-28]].
- **Deux formes de modèle, une seule surface d'API** : Fable 5.1 pour la planification autonome de classe Mythos, la fenêtre d'un million de tokens et la diligence multi-étapes ; Gemini 3.8 Flash pour la vitesse à **0,75 $ / 3,75 $** par million de tokens en entrée / sortie, avec niveau de réflexion réglable. Tout router sur l'un des deux est nommé comme l'erreur à éviter dans les deux sens : payer le tarif frontière pour lire des diffs, ou lancer un modèle rapide sur une migration irréversible sans plan.
- **Activer Fable sur Google Cloud est un parcours à étapes** : activer l'API, activer le modèle, remplir un formulaire d'usage, puis accepter l'Advanced AI Safety Addendum en appelant `setPublisherModelConfig` avec `dataSharingEnabledProvider: ANTHROPIC` au niveau du projet. Un 409 signifie que c'est déjà fait ; un 403 explicite indique l'étape manquante. Le nom de modèle dans l'URL s'écrit avec des tirets, `claude-fable-5-1`. Endpoint global recommandé, variantes multirégionales et régionales.
- **Le benchmark maison tient en deux fichiers** : opencode configuré avec les deux fournisseurs Vertex, promptfoo qui lance `opencode run --auto` avec chaque modèle sur les mêmes prompts, timeout de 60 s. La consigne : ne pas modifier les fichiers de la tâche entre les passes.
- **Les deux résultats se croisent** : sur l'état d'une branche de PR, Fable enchaîne des tours de méta-réflexion en réinspectant des hachages d'arbre inchangés (près de 6 s, 23 fois le coût) ; Flash déclenche les outils git et répond en 1,1 s. Sur la migration Postgres vers Spanner, Flash rend une séquence linéaire propre en 3 s ; Fable, en 12 s, un DAG complet avec risques de dérive d'horloge sur les doubles écritures, clés d'idempotence et porte de rollback réversible.
- **Pattern retenu, coordination asymétrique** : vitesse bon marché en première ligne, profondeur délibérée aux points de contrôle d'architecture. Dans un harnais de codage, des sous-agents nommés mappés sur des modèles distincts (`worker` sur Flash, `deep-thinker` sur Fable) ; le planificateur identifie la cause et découpe, les workers exécutent et rapportent, le planificateur vérifie et confirme ou réassigne. Deux familles de modèles se contrôlent l'une l'autre, rapprochement possible avec [[willison-fable-judgement-delegation-subagents-2026-07-03]].
- **Reformer le harnais selon le modèle** : 3 à 5 outils ciblés à schémas JSON stricts pour le modèle rapide, un catalogue de 50 outils créant confusion de paramètres et gaspillage de contexte ; documents d'architecture, schémas et guidelines pour Fable, mais sans droit d'écriture directe sur les fichiers.
- **Escalade « Ask for Help »** : toute requête démarre sur le worker rapide, doté d'un outil `ask_for_help(reason, failed_attempts, context)` ; il traite 85 à 90 % des demandes seul et n'escalade que sur ambiguïté, action irréversible ou deux échecs d'outil consécutifs.
- **Contre les routeurs « intelligents » automatiques** : mûrs en ML prédictif (bandits, ad tech, fraude) parce que les entrées sont bornées et le retour immédiat ; en agents multi-tours, le premier tour manque de signal, le succès ne se traduit pas en features apprenables, et les mauvais choix sont rejoués sur l'autre chemin, mangeant l'économie et ajoutant de la latence. Verdict : composer explicitement, router par frontière de tâche, laisser des assertions de code ou l'intention humaine gouverner les passages de main.
- ⚠️ **Les chiffres comparatifs reposent sur deux tâches en une passe**, sans variance ni protocole publié ; l'auteur le dit lui-même et renvoie chacun à ses propres évaluations.
- **L'équation de ROI** additionne temps humain économisé, fonctionnalités livrées plus vite, erreurs et pannes évitées, et retranche le coût des tokens et de la montée en compétence de l'équipe. L'auteur note qu'on pèse davantage sur ce calcul en faisant plus de travail, plus vite, qu'en économisant des tokens. Comparaison par équipe à lire avec [[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]].

## RésuméDe400mots

Alan Blount, Technical Solutions Consultant chez Google Cloud, publie le 14 septembre 2026 sur le compte X @GoogleCloudTech un tutoriel en quatre étapes pour faire travailler ensemble Claude Fable 5.1 et Gemini 3.8 Flash. Point de départ : une question anodine confiée à un agent qui a fouillé ses conversations et documents a coûté 38 dollars pour une réponse correcte mais sans enjeu.

Les deux modèles sont accessibles derrière la même API de Gemini Enterprise Agent Platform, le nouveau nom de Vertex AI, via Model Garden. Fable 5.1 apporte la planification autonome de classe Mythos, une fenêtre d'un million de tokens et une diligence multi-étapes ; Gemini 3.8 Flash apporte un raisonnement proche de la frontière à un tarif de 0,75 dollar par million de tokens en entrée et 3,75 en sortie, avec un niveau de réflexion réglable. Tout router sur un seul modèle est présenté comme une erreur.

La première étape détaille l'activation. Fable relève de l'Advanced AI Safety Addendum de Google Cloud : il faut activer le partage prompt-réponse pour Anthropic au niveau du projet par un appel à l'API setPublisherModelConfig, faute de quoi toute requête renvoie une erreur 403. Flash fonctionne dès que le modèle est activé.

La deuxième étape recommande de ne pas se fier aux classements publics et de comparer les modèles sur ses propres tâches, ici avec promptfoo pilotant l'agent opencode. Sur un résumé d'état de branche git, Flash répond en 1,1 seconde pour moins d'un dixième de cent, quand Fable multiplie les tours de réflexion et coûte 23 fois plus. Sur une migration Postgres vers Spanner, Flash livre une séquence linéaire en 3 secondes, Fable un graphe de dépendances formel en 12 secondes, avec risques de dérive d'horloge et porte de rollback.

La troisième étape décrit la coordination asymétrique : le modèle rapide en première ligne, le planificateur profond aux points de contrôle d'architecture. Dans un harnais de codage, cela se traduit par des sous-agents mappés sur des modèles distincts ; dans un service sur mesure, par un harnais adapté à chaque modèle, des évaluations automatisées et un outil d'escalade que le worker appelle sur ambiguïté, action irréversible ou double échec. Les routeurs dynamiques sont écartés au profit d'un routage explicite par frontière de tâche.

La quatrième étape pose une équation de ROI des tokens fondée sur la valeur produite plutôt que sur les grilles tarifaires.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Alan Blount | PERSONNE | travaille_chez | Google Cloud | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Google Cloud | ORGANISATION | publie | Gemini Enterprise Agent Platform | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Gemini Enterprise Agent Platform | TECHNOLOGIE | remplace | Vertex AI | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Gemini Enterprise Agent Platform | TECHNOLOGIE | utilise | Model Garden | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Model Garden | TECHNOLOGIE | permet | Claude Fable 5.1 | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Model Garden | TECHNOLOGIE | permet | Gemini 3.8 Flash | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | fait_partie_de | Advanced AI Safety Addendum | DOCUMENT | 0.92 | DYNAMIQUE | déclaré_article |
| Advanced AI Safety Addendum | DOCUMENT | utilise | setPublisherModelConfig | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Alan Blount | PERSONNE | mesure | une question anodine traitée par un agent de recherche a coûté 38 $ | MESURE | 0.93 | STATIQUE | déclaré_article |
| Gemini 3.8 Flash | TECHNOLOGIE | mesure | 0,75 $ par million de tokens en entrée, 3,75 $ en sortie | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | mesure | fenêtre de contexte d'un million de tokens | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| Alan Blount | PERSONNE | utilise | promptfoo | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| promptfoo | TECHNOLOGIE | utilise | opencode | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Gemini 3.8 Flash | TECHNOLOGIE | surpasse | Claude Fable 5.1 | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Gemini 3.8 Flash | TECHNOLOGIE | mesure | résumé d'état de branche git en 1,1 s pour moins d'un dixième de cent, Fable 5.1 près de 6 s et 23 fois plus cher | MESURE | 0.90 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | surpasse | Gemini 3.8 Flash | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | mesure | plan de migration Postgres vers Spanner en DAG formel en 12 s, contre une séquence linéaire en 3 s pour Flash | MESURE | 0.90 | STATIQUE | déclaré_article |
| Alan Blount | PERSONNE | recommande | coordination asymétrique | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| coordination asymétrique | CONCEPT | est_instance_de | routage de modèles | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| coordination asymétrique | CONCEPT | utilise | subagents | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| coordination asymétrique | CONCEPT | utilise | escalade Ask for Help | METHODOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| escalade Ask for Help | METHODOLOGIE | affirme_que | le worker rapide traite 85 à 90 % des requêtes et n'escalade que sur ambiguïté, action irréversible ou deux échecs d'outil consécutifs | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Alan Blount | PERSONNE | recommande | 3 à 5 outils à schémas JSON stricts pour le modèle rapide, un catalogue de 50 outils causant confusion de paramètres | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Alan Blount | PERSONNE | s_oppose_à | routeurs de modèles dynamiques | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| routeurs de modèles dynamiques | CONCEPT | affirme_que | signal insuffisant au premier tour, succès non traduisible en features, mauvais choix rejoués sur l'autre chemin | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Alan Blount | PERSONNE | affirme_que | "Keep it boring" | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Alan Blount | PERSONNE | recommande | ROI des tokens | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| ROI des tokens | CONCEPT | affirme_que | valeur du temps humain, des fonctionnalités livrées et des incidents évités, moins le coût des tokens et de la montée en compétence | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| coordination asymétrique | CONCEPT | s_applique_à | LangGraph | TECHNOLOGIE | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Alan Blount | PERSONNE | rôle | Technical Solutions Consultant chez Google Cloud (Vertex AI, LLMOps), @zeroasterisk ; auteur de l'article | AJOUT |
| Google Cloud | ORGANISATION | rôle | Éditeur du compte @GoogleCloudTech et de la plateforme qui distribue les modèles Google, Anthropic et xAI | AJOUT |
| Gemini Enterprise Agent Platform | TECHNOLOGIE | nature | Plateforme d'inférence et d'agents de Google Cloud, anciennement Vertex AI ; une authentification unique couvre Gemini et les modèles Anthropic | AJOUT |
| Vertex AI | TECHNOLOGIE | statut | Ancien nom de Gemini Enterprise Agent Platform ; endpoint aiplatform.googleapis.com conservé | MISE_A_JOUR |
| Model Garden | TECHNOLOGIE | nature | Catalogue de modèles managés de la plateforme, incluant Google, Anthropic, xAI et les modèles Hugging Face à déployer soi-même | AJOUT |
| Claude Fable 5.1 | TECHNOLOGIE | accès Google Cloud | Soumis à l'Advanced AI Safety Addendum : activation du modèle, formulaire d'usage, partage prompt-réponse activé par setPublisherModelConfig ; identifiant claude-fable-5-1 | AJOUT |
| Gemini 3.8 Flash | TECHNOLOGIE | profil | Raisonnement proche de la frontière, forte vélocité, 0,75 $ / 3,75 $ par million de tokens, thinkingLevel réglable ; utilisable dès activation | AJOUT |
| Advanced AI Safety Addendum | DOCUMENT | nature | Addendum contractuel Google Cloud conditionnant l'accès à certains modèles au partage prompt-réponse avec l'éditeur | AJOUT |
| setPublisherModelConfig | TECHNOLOGIE | usage | API v1beta1 fixant dataSharingEnabledProvider à ANTHROPIC au niveau projet ; 409 si déjà fait, 403 explicite sinon | AJOUT |
| promptfoo | TECHNOLOGIE | usage | Pilote des exécutions d'agent (provider exec) pour comparer deux modèles sur les mêmes tâches, timeout 60 s | AJOUT |
| opencode | TECHNOLOGIE | usage | Harnais de codage configuré avec deux fournisseurs Vertex et des sous-agents worker (Flash) et deep-thinker (Fable) | AJOUT |
| coordination asymétrique | CONCEPT | définition | Modèle rapide en première ligne pour l'exécution, planificateur profond aux points de contrôle d'architecture ; routage explicite par frontière de tâche | AJOUT |
| escalade Ask for Help | METHODOLOGIE | mécanisme | Outil ask_for_help(reason, failed_attempts, context) donné au worker ; escalade sur ambiguïté, action irréversible ou deux échecs consécutifs | AJOUT |
| routeurs de modèles dynamiques | CONCEPT | limite | Mûrs en ML prédictif (bandits, ad tech, fraude), fragiles en agents multi-tours ; écartés au profit d'une composition explicite | AJOUT |
| ROI des tokens | CONCEPT | formule | Temps humain économisé + fonctionnalités livrées + incidents évités − coût des tokens − coût de montée en compétence | AJOUT |
| subagents | TECHNOLOGIE | usage | Sous-agents nommés mappés sur des modèles distincts dans le harnais ; deux familles de modèles se contrôlent mutuellement | AJOUT |
