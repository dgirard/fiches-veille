---
themes: [transformation-adoption, economie-marche, philosophie-societe]
source: "Anthropic Research"
---
# wilmers-anthropic-employment-changing-2026-10-16

## Veille

Rapport de l'équipe **Economics** d'**Anthropic**, signé **Nathan Wilmers**, **Regina Catipon**, **Maxim Massenkoff** et **Peter McCrory**, publié le **16 octobre 2026** sur le site Research (environ **4 500 mots**, huit figures, version PDF). Il étudie Anthropic comme indicateur avancé de l'organisation du travail sous IA, à partir de données internes (effectifs, télémétrie des agents, production, enquêtes, agendas, Slack, grilles d'entretien d'embauche) et de **17 entretiens**.

**(1)** Emploi : la part des juniors dans les départements techniques passe de **21 % à 14 %** depuis début 2025, celle des recrutements juniors de **27 % à 9 %**. **(2)** Agents : en août 2026, les sessions interactives pilotées par les employés totalisent **6 fois** plus d'heures que les humains. **(3)** Productivité : commits par ingénieur ×5 en six mois ; suivi de **192** adoptants contre **74** non-adoptants, sans écart de qualité mesurable entre code d'agent et code humain. **(4)** Goulot : les sessions passent **~80 %** du temps à attendre l'humain ; le *« meta-work »* passe de **10 % à 22 %** des sessions. **(5)** Embauche : l'autonomie et le jugement progressent dans les évaluations, l'expertise de domaine recule. **(6)** Trois leviers employeur : actionnariat salarié, système d'alerte précoce sur les métiers, redéploiement interne.

Les auteurs signalent que l'adoption des outils n'est pas aléatoire et que leurs mesures ne traitent pas le recul des embauches juniors. Le rapport prolonge [[anthropic-interviewer-ai-workforce-study-2025-12-04]] et la déclaration rapportée dans [[matsuda-amodei-entry-level-white-collar-2026-10-02]].

## Titre Article

How employment is changing at Anthropic

## Date

2026-10-16

## URL

https://www.anthropic.com/research/employment-at-anthropic

## Keywords

emploi, marché du travail, Anthropic, postes juniors, embauche junior, heures d'agents, agents IA, productivité, commits par ingénieur, adoption échelonnée, effets fixes, qualité du code, AI slop, goulot de l'attention humaine, meta-work, gestion d'agents, instructions permanentes, réunions, Slack, observabilité du travail humain, critères d'embauche, autonomie et jugement, redéploiement interne, mobilité interne, système d'alerte précoce, actionnariat salarié, automatisation médiocre, so-so automation, compromis d'après-guerre

## Authors

Nathan Wilmers, Regina Catipon, Maxim Massenkoff, Peter McCrory — équipe Economics d'Anthropic ; rapport publié sur anthropic.com/research.

## Ton

Profil : rapport d'économistes du travail, en anglais, à la première personne du pluriel, publié par l'entreprise étudiée sur ses propres données. Il s'adresse aux employeurs, aux décideurs publics et aux chercheurs.

Structure : constats clés en tête, puis quatre parties (demande de travail, productivité, goulots et processus, ce que peuvent faire les employeurs). Chaque partie alterne une figure chiffrée, sa note méthodologique et des verbatims d'employés anonymes.

Registre : descriptif et prudent sur les mesures. Les limites sont écrites dans le texte : adoption non aléatoire (biais de sélection), qualité du code mesurée par proxys, question d'enquête reformulée entre deux vagues, croissance commerciale qui confond les effets. Le ton devient normatif dans la dernière partie (*« Here we want to proceed carefully »*), qui mobilise l'histoire (chemins de fer, compromis syndical des années 1950) et la notion d'*« so-so automation »*.

Images : le baby-sitting (*« I need my juice box opened »*) pour la demande d'attention des agents, *« an army of Claudes »*. La conclusion reconnaît que les mesures proposées ne protègent pas ceux qui ne sont pas embauchés.

## Pense-betes

- **Source** : rapport Economics d'Anthropic, 16 octobre 2026, 4 auteurs, données internes + 17 entretiens.
- **Revenu par employé** : à cinq ans, **2 à 4 fois** celui de Meta et Google au même stade.
- **Juniors** : part dans les départements techniques **21 % → 14 %** ; part des recrutements **27 % → 9 %** ; offres en forte baisse depuis décembre 2025. En avril 2026, un tiers des managers ML et un cinquième des managers SWE déclarent embaucher moins à cause de l'IA.
- **Composition** : part des départements techniques **61 % → 56 %** ; ratio ingénieurs / PM **~17 pour 1** ; commits des managers ×2 ; fonctions administratives restées légères.
- **Non-techniques qui codent** : sessions d'agents de code **2/mois (août 2025) → 90 (mai 2026)**.
- **Mobilité** : employés d'un an et plus **50 %** plus susceptibles de changer de département chaque mois en 2026 ; une équipe de rédaction produit est passée à l'écriture d'évals et de prompts.
- **Heures d'agents** : agents (autonomes + interactifs) > humains dès mars 2026 ; **6:1** en août sur les seules sessions interactives.
- **Productivité** : commits/ingénieur ×5 en six mois ; contrats, factures et ventes en hausse. Effets fixes personne × mois, traitement = 5 sessions agentiques dans le mois.
  - Qualité : même employé, même mois, même répertoire → pas d'écart de suppression ni de revert à 90 jours.
- **Difficulté** : après chaque sortie de modèle, la part des tâches au-delà du p90 de l'ancien modèle passe de **10 % à 13 %**.
- **Attention** : **~80 %** du temps de session = attente de l'humain ; lire toute la sortie des agents prendrait plus d'une **demi-semaine** même pour les non-techniques (0,75 mot/token, 250 mots/min).
- **Meta-work** : **10 % → 22 %** des sessions (specs multi-agents, revue croisée, monitoring) ; instructions permanentes **quelques centaines → 8 500** en un an.
- **Humain** : temps de réunion médian **+20 %** (+16 % chez les contributeurs individuels techniques) ; agents dans près de la moitié des canaux Slack publics, sans réduire les réponses humaines.
- **Embauche** : mention de l'usage créatif d'outils IA ×3 (technique) et ×4 (non technique) entre 2024 et 2026.
- **Attentes** : les employés estiment que l'IA fera **75 %** de leur travail en 2030, contre **28 %** pour les autres Américains.
- **Leviers** : actionnariat, alerte précoce par métier, redéploiement ; politique publique de reconversion et de revenu jugée nécessaire.
- ⚠️ **Portée** : données propres de l'entreprise, adoption non aléatoire ; les auteurs notent qu'aucun levier ne traite le recul des embauches juniors.

## RésuméDe400mots

Le 16 octobre 2026, quatre économistes de l'équipe Economics d'Anthropic publient un rapport sur la transformation du travail dans l'entreprise. Ils la considèrent comme un indicateur avancé, parce qu'elle a reconstruit ses flux de travail autour de l'IA. Le rapport s'appuie sur des données internes (effectifs, télémétrie des agents, production, enquêtes, agendas, Slack, grilles d'entretien) et sur dix-sept entretiens.

Anthropic croît vite mais embauche moins par dollar de revenu que Meta ou Google au même âge. Les postes juniors techniques reculent : leur part dans les départements techniques passe de 21 % à 14 % depuis début 2025, et celle des recrutements de 27 % à 9 %. Les départements techniques pèsent moins dans l'effectif, tandis que les non-techniciens se mettent à coder : leurs sessions d'agents de code passent de 2 à 90 par mois. Les fonctions administratives restent légères et la mobilité interne progresse de moitié.

Depuis mars 2026, les heures d'agents dépassent les heures humaines ; en août, les seules sessions interactives des employés représentent six fois le temps humain. Les commits par ingénieur ont été multipliés par cinq en six mois, et juristes, comptables et commerciaux produisent davantage. En comparant 192 ingénieurs qui adoptent les agents à 74 qui ne les adoptent pas, les auteurs observent une hausse nette après adoption, tout en reconnaissant que l'adoption n'est pas aléatoire. Le code produit par agent n'est ni plus supprimé ni plus souvent annulé que le code écrit à la main par le même employé.

L'attention humaine devient le goulot. Environ 80 % du temps de session des agents se passe à attendre une réponse, et lire toute leur production occuperait plus d'une demi-semaine, même pour les non-techniciens. Les employés y répondent par du « meta-work » : instructions permanentes, spécifications multi-agents, revues croisées, tableaux de bord. Cette part passe de 10 % à 22 % des sessions. Le temps de réunion augmente de 20 %, et le travail doit rester visible pour que les agents disposent du contexte.

À l'embauche, les évaluateurs mentionnent trois à quatre fois plus souvent l'usage créatif de l'IA, et valorisent l'autonomie et le jugement plus que l'expertise de domaine ou l'exécution.

Les auteurs retiennent trois leviers : l'actionnariat salarié, qui partage les gains de l'adoption ; un système d'alerte précoce sur les métiers exposés ; le redéploiement interne, qui pousse à créer des tâches plutôt qu'à automatiser à la marge. Ils reconnaissent qu'aucun ne protège ceux qui ne sont pas embauchés et appellent une politique publique de reconversion et de soutien au revenu.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Anthropic | ORGANISATION | publie | rapport How employment is changing at Anthropic | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Nathan Wilmers | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Maxim Massenkoff | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Peter McCrory | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Regina Catipon | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | mesure | part des recrutements juniors techniques passée de 27 % à 9 % depuis début 2025 | MESURE | 0.95 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | mesure | heures des agents interactifs six fois supérieures aux heures humaines en août 2026 | MESURE | 0.93 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | mesure | commits par ingénieur multipliés par cinq en six mois | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| Agents de codage | TECHNOLOGIE | améliore | production de code des ingénieurs adoptants, sans écart de suppression ou de revert à 90 jours | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | mesure | environ 80 % du temps de session des agents passé à attendre une entrée humaine | MESURE | 0.90 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | affirme_que | l'attention humaine est le goulot de la production des agents | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Meta-work | METHODOLOGIE | observé_dans | Anthropic | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | mesure | meta-work passé de 10 % à 22 % des sessions Claude interactives entre l'automne 2025 et le printemps 2026 | MESURE | 0.90 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | affirme_que | les évaluations d'embauche valorisent davantage l'autonomie et le jugement que l'expertise de domaine | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | affirme_que | le besoin de contexte des agents exige l'observabilité du travail et des décisions humaines | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | recommande | Actionnariat salarié | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | recommande | Système d'alerte précoce sur les métiers | METHODOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | recommande | Redéploiement interne | METHODOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Redéploiement interne | METHODOLOGIE | réduit | So-so automation | CONCEPT | 0.78 | ATEMPOREL | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | s_inspire_de | Compromis syndical d'après-guerre | CONCEPT | 0.80 | STATIQUE | déclaré_article |
| rapport How employment is changing at Anthropic | DOCUMENT | affirme_que | les protections des salariés en place ne bénéficient pas aux juniors non embauchés et doivent s'accompagner d'une politique publique | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| rapport How employment is changing at Anthropic | DOCUMENT | nature | Rapport de l'équipe Economics d'Anthropic, 16 octobre 2026, données internes + 17 entretiens | AJOUT |
| Anthropic | ORGANISATION | effectif | Taille triplée en un an ; revenu par employé 2 à 4 fois celui de Meta et Google au même âge (oct. 2026) | MISE_A_JOUR |
| Nathan Wilmers | PERSONNE | rôle | Économiste, équipe Economics d'Anthropic | AJOUT |
| Regina Catipon | PERSONNE | rôle | Chercheuse, équipe Economics d'Anthropic | AJOUT |
| Maxim Massenkoff | PERSONNE | rôle | Économiste, équipe Economics d'Anthropic | AJOUT |
| Peter McCrory | PERSONNE | rôle | Économiste, équipe Economics d'Anthropic | AJOUT |
| Meta-work | METHODOLOGIE | définition | Travail consacré à outiller et superviser les agents (skills, specs, revues, monitoring) plutôt qu'à la tâche elle-même | AJOUT |
| Système d'alerte précoce sur les métiers | METHODOLOGIE | définition | Suivi par métier de la demande et de la productivité, lu au regard des capacités et usages de l'IA | AJOUT |
| Redéploiement interne | METHODOLOGIE | définition | Réaffectation des employés vers des postes moins exposés à l'automatisation | AJOUT |
| Actionnariat salarié | CONCEPT | définition | Participation financière des employés, présentée comme mécanisme de partage des gains de l'adoption | AJOUT |
| So-so automation | CONCEPT | définition | Automatisation qui remplace des travailleurs pour un gain de productivité minime | AJOUT |
| Compromis syndical d'après-guerre | CONCEPT | définition | Accord des années 1950 (UAW, USW) : réorganisation du travail contre hausses salariales indexées sur la productivité | AJOUT |
| Agents de codage | TECHNOLOGIE | catégorie | Agents IA qui écrivent et modifient du code | AJOUT |
