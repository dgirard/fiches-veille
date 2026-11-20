---
themes: [economie-marche, outils-plateformes]
source: SFEIR
---
# sfeir-api-claude-cache-effort-migrations-2026-11-16

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **16 novembre 2026** (~10 000 signes, huit sections, une source). Il restitue la vidéo « Building the Claude API for the Frontier » (chaîne YouTube de Claude, **12 novembre 2026**, 18 min 29), échange entre **Jake Dejno** (Claude Platform) et **Lucca Siaudzionis** (Platform Intelligence) d'Anthropic. Quatre apports. **(A)** L'effort et le system prompt se modifient désormais en cours de conversation **sans invalider le cache** (changement d'effort en bêta). **(B)** Le modèle fait office de version : en-têtes beta, bascules de retour, **un ou deux modèles de transition** avant dépréciation, et une revue du harnais à chaque migration. **(C)** Côté coûts, la première question posée aux clients porte sur le **taux de cache**, objectif **90 %**, puis sur l'*intelligence par token*. **(D)** **Mythos** et **Fable** partagent *« la même intelligence, les mêmes poids »* ; seuls les classifieurs diffèrent. L'article ajoute une lecture SFEIR (conditions d'accès comme risque fournisseur) et six recommandations. Rejoint, côté coût par tâche, [[walker-onlycfo-ai-tokenomics-2026-10-22]].

## Titre Article

Votre facture Claude est trop haute ? Anthropic vous dit par où commencer

## Date

2026-11-16

## URL

https://www.sfeir.com/articles/api-claude-frontiere-cache-effort-migrations/

## Keywords

API Claude, Messages API, prompt caching, taux de cache, effort, adaptive thinking, extended thinking, versioning, en-têtes beta, dépréciation, migration de modèle, harnais, intelligence par token, coût par tâche, Mythos, Fable, Cyber Verification Program, distillation, Claude Managed Agents, FinOps, Anthropic, SFEIR

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé publié sur sfeir.com, site éditorial du groupe.

## Ton

Article de restitution d'une source vidéo, en français, à destination des CTO, responsables de plateforme et équipes FinOps qui font tourner un produit sur Claude. Le registre est pratique : chaque section reprend un point de l'échange, avec appel de note systématique vers la source unique, puis en tire une conséquence opérationnelle. L'article distingue ce que disent les intervenants et ce que précise la description de la vidéo (statut bêta, Cyber Verification Program). Il assume un paragraphe d'analyse propre, signalé comme tel (« La vidéo ne s'attarde pas sur une conséquence »), sur les conditions d'accès décidées par le fournisseur. Les renvois internes (fiche prompt caching, coût par résultat, Fable 5.2 et Mythos 5.2) inscrivent le texte dans la série SFEIR sur l'économie des modèles. Conclusion en liste numérotée de six actions.

## Pense-betes

- **Source** : vidéo « Building the Claude API for the Frontier », 12 novembre 2026, Jake Dejno (Claude Platform) et Lucca Siaudzionis (Platform Intelligence), aucune annonce produit.
- **Messages API** = pierre angulaire (tours système/utilisateur/assistant + appels d'outils). Les réglages comme l'**effort** changent le comportement plus qu'un prompt : même modèle en effort haut et bas, *« deux modèles différents »*. Les valeurs par défaut reflètent le choix des équipes de recherche.
- **Effort et system prompt modifiables en cours de conversation sans casser le cache** ; avant, le changement invalidait le cache et annulait l'économie. Changement d'effort mid-conversation : **bêta**.
- **Deux chemins des fonctionnalités** : recherche → API (computer use né d'un progrès observé) ; clients → recherche (objectifs d'entraînement des *prochains* modèles). Un stock de fonctionnalités testées non lancées est réévalué à chaque modèle ; même conseil aux clients : **rejouer les prototypes qui échouaient de peu**.
- **Versioning** : nom du modèle + en-têtes beta + bascules de retour. Exemple : passage de l'extended thinking à l'**adaptive thinking** par défaut, avec retour possible un temps. Règle : **un ou deux modèles de transition**, puis dépréciation franche (un paramètre que les modèles ne savent plus honorer serait plus nuisible).
- **Chaque migration = revue du harnais** : un harnais conçu pour un modèle peut brider le suivant, *« dix fois plus capable »*.
- **Coûts** : premier levier, le **prompt caching** ; les commerciaux d'Anthropic demandent d'abord le **taux de cache**, objectif **90 %**. Deuxième levier : l'**intelligence par token** (vitesse d'atteinte du résultat) à côté du prix du token. Exemple : une tâche réservée à **Fable 5** passe désormais sur **Opus 5**.
- **Mythos / Fable** : mêmes poids, classifieurs différents ; Mythos réservé aux organisations vérifiées (Cyber Verification Program). Nouvelles protections **anti-distillation** sur le thinking ; une dizaine de variantes testées en interne par fonctionnalité.
- **Agents** : l'essentiel des fonctionnalités sert les flux agentiques ; **Claude Managed Agents** en bêta ; outils client (bash, éditeur) remplaçables.
- **Six recommandations SFEIR** : mesurer le taux de cache, régler l'effort par requête, piloter au coût par tâche réussie, migration = revue du harnais, rejouer les prototypes, anticiper les dépréciations.
- **À relier** : [[lancemartin-anthropic-prompt-auto-caching-claude-2026-02]] (mécanique du cache), [[anthropic-claude-fable-5-mythos-5-2026-06-09]] (séparation Fable/Mythos).

## RésuméDe400mots

L'article de SFEIR AI restitue « Building the Claude API for the Frontier », une vidéo de dix-huit minutes publiée le 12 novembre 2026 sur la chaîne officielle de Claude. Deux ingénieurs d'Anthropic, Jake Dejno (équipe Claude Platform) et Lucca Siaudzionis (équipe Platform Intelligence), y expliquent comment l'API évolue au rythme des modèles. La vidéo n'annonce aucun produit ; l'article en tire des conseils pour les CTO, responsables de plateforme et équipes FinOps.

La **Messages API** est présentée comme la pierre angulaire de la plateforme. Des réglages comme l'**effort** transforment le comportement du modèle au point qu'un même modèle en effort haut et en effort bas paraît être deux modèles différents. Deux évolutions sont détaillées : l'effort et le system prompt peuvent désormais changer en cours de conversation **sans invalider le cache de prompt**, ce qui rend rentable le passage en effort bas pour une étape simple d'un flux agentique. Le changement d'effort reste en bêta.

Les fonctionnalités naissent de deux chemins : des progrès observés par la recherche (le computer use) et des demandes clients, qui deviennent des objectifs d'entraînement pour les modèles suivants. Anthropic garde un stock de fonctionnalités non lancées qu'il réévalue à chaque modèle, et conseille aux clients de rejouer leurs prototypes abandonnés.

Sur le **versioning**, le modèle tient lieu de version, complété par des en-têtes beta et des bascules de retour. Le passage de l'extended thinking à l'adaptive thinking illustre la règle : un ou deux modèles de transition, puis une dépréciation franche. Chaque migration impose de réévaluer son harnais, qui peut devenir une limite pour un modèle plus capable.

Côté coûts, le premier conseil est le **prompt caching** : les équipes commerciales d'Anthropic demandent d'abord le taux de cache, avec un objectif de **90 %**. Le second est de suivre l'*intelligence par token* : un modèle plus cher peut coûter moins au total s'il atteint plus vite le résultat, et une tâche autrefois réservée à Fable 5 peut passer sur Opus 5, à vérifier par des évaluations propres.

Sur la sécurité, **Mythos** et **Fable** partagent les mêmes poids ; seuls les classifieurs diffèrent, Mythos étant réservé aux organisations vérifiées. Anthropic a déployé des protections anti-distillation sur le raisonnement. SFEIR ajoute que les conditions d'accès relèvent du risque fournisseur. La fin de l'échange porte sur les agents (Claude Managed Agents en bêta). L'article conclut par six recommandations, du taux de cache à l'anticipation des dépréciations.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Votre facture Claude est trop haute ? | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Votre facture Claude est trop haute ? | DOCUMENT | référence | Building the Claude API for the Frontier | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Jake Dejno | PERSONNE | 0.93 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | emploie | Lucca Siaudzionis | PERSONNE | 0.93 | DYNAMIQUE | déclaré_article |
| Messages API | TECHNOLOGIE | fait_partie_de | Claude Platform | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Messages API | TECHNOLOGIE | utilise | prompt caching | CONCEPT | 0.94 | DYNAMIQUE | déclaré_article |
| Messages API | TECHNOLOGIE | permet | changement d'effort sans perte de cache | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| adaptive thinking | TECHNOLOGIE | remplace | extended thinking | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | viser un taux de cache de 90 % | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | intelligence par token | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | chaque changement de modèle impose de réévaluer son harnais | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | un ou deux modèles de transition précèdent une dépréciation | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| Claude Mythos | TECHNOLOGIE | est_variante_de | Claude Fable | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Mythos | TECHNOLOGIE | utilise | Cyber Verification Program | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | protections anti-distillation | TECHNOLOGIE | 0.84 | STATIQUE | déclaré_article |
| Claude Managed Agents | TECHNOLOGIE | fait_partie_de | Claude Platform | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | piloter au coût par tâche réussie | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | les conditions d'accès aux modèles de frontière sont un risque fournisseur | AFFIRMATION | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle (groupe SFEIR) | AJOUT |
| Building the Claude API for the Frontier | DOCUMENT | format | Vidéo YouTube, chaîne Claude, 12 novembre 2026, 18 min 29 | AJOUT |
| Jake Dejno | PERSONNE | rôle | Ingénieur, équipe Claude Platform (Anthropic) | AJOUT |
| Lucca Siaudzionis | PERSONNE | rôle | Ingénieur, équipe Platform Intelligence (Anthropic) | AJOUT |
| Messages API | TECHNOLOGIE | rôle | Pierre angulaire de l'API Claude : tours système/utilisateur/assistant et appels d'outils | AJOUT |
| intelligence par token | CONCEPT | définition | Vitesse à laquelle un modèle atteint le résultat, suivie à côté du coût par token | AJOUT |
| adaptive thinking | TECHNOLOGIE | statut | Mode de raisonnement par défaut, successeur de l'extended thinking | AJOUT |
| Claude Mythos | TECHNOLOGIE | accès | Mêmes poids que Fable, réservé aux organisations vérifiées | AJOUT |
| Claude Managed Agents | TECHNOLOGIE | statut | Offre d'agents hébergés, en bêta | AJOUT |
