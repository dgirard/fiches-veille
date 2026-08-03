---
themes: [outils-plateformes, architecture-construction, agents-codage-ia-skills]
source: "Notion"
---
# notion-as-code-2026-08-03

## Veille

Page de documentation **Notion as Code**, publiée sur l'espace **Notion Ambassadors** et consultée le **3 août 2026**. Produit en **alpha sur liste d'attente**, avec un avertissement en tête : *« This product is under development so we recommend you try it out in a new workspace vs. your primary workspace »* et *« There may be breaking changes until we're fully launched »*. **Le principe est celui de l'infrastructure as code appliqué à un espace de travail documentaire** : *« Instead of having to make individual public API requests, you can describe the final state and we handle updating your workspace to match. »* Deux briques : un **SDK TypeScript** pour décrire l'état voulu, et un **endpoint d'API publique** `/v1/infra_as_code` pour le déployer. **Le mécanisme qui fait tout tenir est l'identifiant de ressource** : le script ne contient **aucun identifiant Notion**, seulement des *resource IDs* choisis par l'auteur ; le premier déploiement retourne une **table de correspondance** `resourceId → RecordPointer`, qu'on renvoie aux appels suivants pour que les mêmes enregistrements soient **mis à jour plutôt que recréés**. Trois propriétés en découlent, et ce sont les seules qui comptent : le script est **idempotent** (re-déploiement = mise à jour), il est **découplé de l'espace de travail** (plusieurs tables de correspondance permettent de déployer **le même script sur plusieurs espaces**), et il est **du code** — donc variables et boucles, l'exemple donné étant *« build 10 teams that all have a very similar structure and just need some nouns renamed »*. **L'API est asynchrone** : `POST /v1/infra_as_code` rend un `taskId` que l'on interroge via `GET /v1/async_tasks/{taskId}` jusqu'à `succeeded`. **Deux différences opérationnelles notables** : le produit exige des **jetons d'accès personnels** et non les jetons de bot habituels de l'API publique, et la **limite de débit est abaissée à 5 requêtes par minute** parce qu'un appel ne crée plus une entité mais un lot. ⚠️ **Point à consigner pour ce corpus** : la page est explicitement écrite pour un usage assisté — *« A typescript SDK for you **or your coding agent** to describe what you want »* —, et le chemin d'entrée recommandé est de cloner le SDK sur une branche expérimentale et de laisser *« either you or your favorite coding agent »* ouvrir le README. **Limites déclarées** : impossible de créer un nouvel espace, couverture partielle des primitives, et une page sans auteur ni date.

## Titre Article

How to use Notion as Code

## Date

2026-08-03

## URL

https://app.notion.com/p/notionambassadors/How-to-use-Notion-as-Code-3973139dbfef802eb77cfbe7cf08c12a

## Keywords

Notion as Code, infrastructure as code, IaC, état désiré, réconciliation, idempotence, SDK TypeScript, notion-sdk-js, branche expérimentale, API publique, infra_as_code, endpoint asynchrone, taskId, async_tasks, polling, resource ID, identifiant de ressource, RecordPointer, table de correspondance, mapping, existingResources, existingProperties, intents, déploiement multi-espaces, réutilisation de patterns, variables et boucles, jetons d'accès personnels, personal access token, limite de débit, 5 requêtes par minute, alpha, liste d'attente, breaking changes, agents de codage, coding agent, primitives supportées, feedback tracker, Notion Ambassadors

## Authors

**Notion** — documentation produit publiée sur l'espace public **Notion Ambassadors**. **Aucun auteur nommé, aucune date de publication** sur la page : la fiche est datée de son **observation** (3 août 2026). Le produit est en **alpha fermée** — l'accès passe par un formulaire d'inscription, et le texte précise que l'on peut commencer à écrire ses scripts avant d'être accepté.

Renvoi vers deux ressources externes : le dépôt **`makenotion/notion-sdk-js`** sur la branche **`EXPERIMENTAL__notion-as-code`**, et un **Feedback Tracker** pour les retours et anomalies.

## Ton

**Profil** : documentation produit d'alpha, brève et opératoire. Ni annonce marketing ni article de fond — une page de prise en main doublée d'une **spécification d'API** (tableaux champ / type / description pour la requête et la réponse des deux endpoints).

**Style** : **avertissements d'abord, mécanisme ensuite**. La page s'ouvre sur trois mises en garde (produit en développement, changements cassants possibles, accès conditionné à une acceptation) avant la moindre explication de valeur. Le registre est celui d'une équipe qui livre tôt et le dit : émojis d'alerte 🚧 et ⚠️ en tête de section, renvoi vers un tracker d'anomalies, limites listées explicitement en clôture.

**Le geste rhétorique unique de la page** tient en une phrase, et c'est celle qui justifie l'existence du produit : *« Instead of having to make individual public API requests, you can describe the final state and we handle updating your workspace to match. »* Tout le reste en découle — la table de correspondance, l'idempotence, le multi-espaces.

**Trait notable** : l'agent de codage est mentionné **comme utilisateur de plein droit**, deux fois, sans emphase — *« for you or your coding agent »*, *« either you or your favorite coding agent can open the readme »*. Ce n'est pas une section « IA » ajoutée : c'est intégré à la description du produit comme une évidence.

**Formules-marqueurs** : *« describe the final state and we handle updating your workspace to match »*, *« this script doesn't have any IDs, but instead uses resource IDs »*, *« Since the script is not coupled to one workspace »*, *« this API is not a 1 request → 1 entity created or updated »*.

## Pense-betes

- **⭐ Ce que c'est, en une phrase** : de l'**infrastructure as code pour un espace de travail documentaire**. On décrit l'**état final voulu** en TypeScript, Notion **réconcilie** l'espace pour qu'il y corresponde. C'est le modèle Terraform, appliqué à des pages, bases et équipes plutôt qu'à des ressources cloud.

- **⭐⭐ Le mécanisme central — l'identifiant de ressource, et pourquoi il fait tout** : le script **ne contient aucun identifiant Notion**. Il utilise des `resourceId` choisis par l'auteur. Le premier déploiement retourne une **table de correspondance** `resourceId → RecordPointer`, que l'on renvoie ensuite via `existingResources` / `existingProperties`. Trois propriétés en découlent, et elles sont inséparables :
  1. **Idempotence** — re-déployer met à jour au lieu de recréer.
  2. **Découplage de l'espace de travail** — *« since the script is not coupled to one workspace, you can easily have multiple mappings… allowing you to use the same script to deploy many workspaces »* : **une table de correspondance par espace**, un seul script.
  3. **Programmabilité** — c'est du code, donc variables et boucles : *« build 10 teams that all have a very similar structure and just need some nouns renamed »*.
  → **L'indirection par identifiant logique est ce qui transforme un script d'API en descripteur d'état réutilisable.** C'est exactement le rôle des adresses de ressources dans un état Terraform.

- **Le contrat d'API, en deux temps (asynchrone)** : `POST /v1/infra_as_code` (champs `intents` — représentation JSON sérialisée du script —, `existingResources`, `existingProperties`) rend un `taskId` ; on interroge `GET /v1/async_tasks/{taskId}` jusqu'à `status: succeeded`, la réponse portant `createdRecordCounts`, `resourceIdToPointerMappings` et `resourceIdToPropertyIdMappings`. **Les deux tables de correspondance en sortie sont ce qu'il faut persister** — ce sont l'équivalent d'un fichier d'état.

- **Deux différences opérationnelles à connaître avant d'essayer** :
  - **Jetons d'accès personnels obligatoires**, et non les jetons de bot de l'API publique. ⚠️ Conséquence non discutée par la page : les actions sont attribuées à **une personne**, pas à une intégration — ce qui pose la même question de responsabilité que *« qui consomme, et pour le compte de qui »* dans [[girard-acp-deux-protocoles-un-sigle-2026-08-02]]. Un agent qui déploie avec le jeton personnel d'un administrateur agit **en son nom**.
  - **5 requêtes par minute**, *« since this API is not a 1 request → 1 entity created or updated »*. Le débit est abaissé parce qu'un appel est un lot.

- **⭐ La mention des agents, intégrée sans emphase** : *« A typescript SDK for **you or your coding agent** to describe what you want in your Notion workspace »*, et le chemin recommandé consiste à cloner le SDK puis laisser *« either you or your favorite coding agent »* lire le README. → **Le produit est conçu en supposant qu'un agent l'utilisera**, et le SDK typé est précisément ce qui rend cela sûr : les types contraignent ce que l'agent peut décrire, et la réconciliation rend l'erreur corrigible par re-déploiement plutôt que par nettoyage manuel. **Un descripteur d'état typé est un bien meilleur outil pour un agent qu'une série d'appels d'API impératifs** — l'erreur y est rejouable, pas cumulative.

- **Limites déclarées** : ne peut que créer ou mettre à jour **dans un espace existant** (impossible de créer un espace) ; **toutes les entités ne sont pas couvertes** — se référer au fichier de définition de types du SDK, les primitives de haut niveau étant censées passer ; débit abaissé.

- **⚠️ Ce que la page ne dit pas, et qu'il faut avoir en tête** :
  - **Aucune mention de destruction.** L'API « crée ou met à jour ». Que devient un élément retiré du script ? Un vrai outil d'état sait supprimer ce qui n'est plus déclaré — ici, rien ne l'indique, ce qui suggère une réconciliation **additive** et donc une dérive possible entre le script et l'espace réel.
  - **Aucun mode « plan »** ni prévisualisation avant application. On déploie et on observe.
  - **Aucune gestion de la concurrence** : deux déploiements simultanés sur le même espace ne sont pas discutés.
  - **Aucun auteur, aucune date.** Pour une documentation d'alpha en évolution, c'est un manque qui rendra toute citation rapidement périmée — d'où la datation par observation dans cette fiche.

- **Angle « veille » — pourquoi c'est intéressant au-delà de Notion** : c'est un signal de plus de la **migration du modèle déclaratif hors de l'infrastructure**. Après le cloud, les espaces documentaires ; et le déclencheur assumé est l'agent de codage, qui a besoin d'un **format descriptible, typé et rejouable** plutôt que d'une séquence d'actions. À rapprocher de la logique « un fichier plutôt qu'une équipe » de [[isenberg-meng-to-google-design-md-design-team-in-a-file-2026-05-06]], et de la discipline de spécification versionnée de [[lassiege-usine-logicielle-heure-ia-2026-07-28]].

- **Méta / à relier** : question du jeton personnel et de l'action pour le compte d'autrui dans [[girard-acp-deux-protocoles-un-sigle-2026-08-02]] ; identité et périmètre d'action d'un agent dans [[uber-engineering-agent-identity-crisis-zero-trust-spire-2026-05-21]] et [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] ; artefacts déclaratifs pilotés par agent dans [[isenberg-meng-to-google-design-md-design-team-in-a-file-2026-05-06]].

## RésuméDe400mots

Documentation de **Notion as Code**, produit en **alpha fermée**, consultée le 3 août 2026 sur l'espace Notion Ambassadors — sans auteur ni date, avec un avertissement recommandant de l'essayer sur un espace de travail neuf et prévenant de changements cassants possibles.

**Le principe** est l'infrastructure as code appliquée à un espace documentaire : *« Instead of having to make individual public API requests, you can describe the final state and we handle updating your workspace to match. »* Deux briques : un **SDK TypeScript** pour décrire l'état voulu, et l'endpoint **`/v1/infra_as_code`** pour le déployer.

**Le mécanisme qui porte tout** est l'indirection par identifiant. Le script **ne contient aucun identifiant Notion** : il déclare des `resourceId` choisis par l'auteur. Le premier déploiement retourne une **table de correspondance** entre ces identifiants logiques et les enregistrements réellement créés ; renvoyée aux appels suivants, elle fait que les mêmes enregistrements sont **mis à jour plutôt que recréés**.

**Trois propriétés en découlent.** Le script devient **idempotent**. Il devient **découplé de l'espace de travail** — plusieurs tables de correspondance permettent de déployer **le même script sur plusieurs espaces**. Et comme c'est du code, il admet variables et boucles : l'exemple donné est de construire dix équipes de structure identique en ne changeant que quelques noms.

**Le contrat d'API est asynchrone** : un `POST` rend un `taskId`, que l'on interroge jusqu'à complétion ; la réponse porte les tables de correspondance à persister — l'équivalent d'un fichier d'état.

**Deux différences opérationnelles** : le produit exige des **jetons d'accès personnels** et non les jetons de bot habituels, ce qui attribue les actions à une personne plutôt qu'à une intégration ; et la **limite de débit tombe à 5 requêtes par minute**, un appel étant désormais un lot et non une entité.

**Le produit suppose l'agent.** Le SDK est présenté comme fait *« for you or your coding agent »*, et le chemin de prise en main consiste à laisser un agent lire le README du SDK. Un descripteur d'état typé est en effet un meilleur outil pour un agent qu'une série d'appels impératifs : l'erreur y est rejouable plutôt que cumulative.

⚠️ **Ce qui manque** : aucune mention de suppression des éléments retirés du script, aucun mode de prévisualisation avant application, rien sur la concurrence, et aucune date sur une documentation appelée à bouger.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Notion | ORGANISATION | publie | Notion as Code | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Notion as Code | TECHNOLOGIE | permet | de décrire l'état final voulu d'un espace de travail et de laisser la plateforme le réconcilier | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| Notion as Code | TECHNOLOGIE | est_instance_de | infrastructure as code | CONCEPT | 0.92 | ATEMPOREL | inféré |
| identifiant de ressource logique | CONCEPT | permet | de rendre un script idempotent et déployable sur plusieurs espaces de travail | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| table de correspondance resourceId vers enregistrement | CONCEPT | permet | de mettre à jour les enregistrements existants au lieu d'en créer de nouveaux | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Notion as Code | TECHNOLOGIE | utilise | un SDK TypeScript | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Notion as Code | TECHNOLOGIE | s_applique_à | les agents de codage, désignés comme utilisateurs du SDK au même titre que les humains | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Notion as Code | TECHNOLOGIE | utilise | des jetons d'accès personnels plutôt que des jetons de bot de l'API publique | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| endpoint infra_as_code | TECHNOLOGIE | s_oppose_à | le modèle une requête pour une entité, d'où une limite de débit abaissée à cinq requêtes par minute | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Notion as Code | TECHNOLOGIE | réduit | le nombre d'appels d'API nécessaires pour construire des structures répétitives, grâce aux variables et aux boucles | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| description d'état typée | CONCEPT | surpasse | une séquence d'appels impératifs pour un agent, l'erreur devenant rejouable plutôt que cumulative | AFFIRMATION | 0.82 | ATEMPOREL | inféré |
| Notion as Code | TECHNOLOGIE | affirme_que | le produit est en développement, sujet à des changements cassants, et limité à la création ou mise à jour dans un espace existant | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Notion as Code | TECHNOLOGIE | définition | Infrastructure as code appliquée à un espace de travail Notion : un SDK TypeScript décrit l'état final voulu, un endpoint asynchrone réconcilie l'espace pour y correspondre, une table de correspondance rendant l'opération idempotente et rejouable sur plusieurs espaces | AJOUT |
| How to use Notion as Code | DOCUMENT | référence | Documentation d'alpha publiée sur l'espace Notion Ambassadors, sans auteur ni date ; observée le 3 août 2026 | AJOUT |
| identifiant de ressource logique | CONCEPT | définition | Identifiant choisi par l'auteur d'un script déclaratif, distinct de l'identifiant réel de la plateforme, et relié à lui par une table de correspondance produite au premier déploiement | AJOUT |
| Notion | ORGANISATION | évolution produit | Ouvre en alpha un modèle déclaratif de construction d'espace de travail, explicitement conçu pour être piloté par un agent de codage autant que par un humain | MISE_A_JOUR |
