---
themes: [agents-codage-ia-skills, architecture-construction, qualite-securite]
source: SFEIR
---
# sfeir-fde-factory-eno-reyes-2026-11-10

## Veille

Critique éditoriale **SFEIR AI** publiée sur sfeir.com le **10 novembre 2026**, dans la série de neuf retours sur la playlist *forward deployed engineering* de l'**AI Engineer World's Fair 2026**. Elle porte sur le talk d'ouverture du track, par **Eno Reyes**, cofondateur et CTO de **Factory** (agents **Droid**, ex-Hugging Face et Microsoft), 21 min 21, ~**6 200** vues. Trois apports. **(A)** Le refus des missions de modernisation au forfait : rentables, elles n'apprennent rien au produit ; les deployed engineers sont le fer de lance du produit chez les grands comptes. **(B)** L'usine logicielle, du signal au déploiement sans interruption humaine, *« built, not bought »*, sur un harnais d'agents indépendant des modèles. **(C)** Le code « prêt pour les agents » se mesure à la **densité de ses boucles de validation déterministes** (linters, typage, SAST, tests de bout en bout) ; Droid comblerait seul **30 à 40 %** des manques, et Factory mesure **15 à 20 %** d'autonomie sur son propre code. Notes SFEIR : **4/5** et **4/5**. Même orateur que [[reyes-factory-building-machine-software-2026-09-22]].

## Titre Article

Factory envoie ses FDE préparer le code des clients pour les agents

## Date

2026-11-10

## URL

https://www.sfeir.com/articles/fde-factory-eno-reyes/

## Keywords

forward deployed engineering, FDE, deployed engineer, Factory, Droid, Eno Reyes, AI Engineer World's Fair 2026, usine logicielle, software factory, signal au déploiement, built not bought, harnais d'agents, harness engineering, agent-ready codebase, boucles de validation déterministes, linters, typage, SAST, tests de bout en bout, récompense dense, modèle de maturité de l'autonomie, base de code exemplaire, Epcot, migration, modernisation legacy, air-gapped, ESN, critique de talk

## Authors

SFEIR AI (voix éditoriale non signée), sfeir.com, site éditorial de SFEIR. Critique du talk d'Eno Reyes (Factory).

## Ton

Critique de talk au format fixe de la série SFEIR (encadré, minutages, « Pour une ESN », verdict noté). Registre technique et favorable : l'article restitue une vision cohérente (usine, boucles de validation, analogie d'Epcot) et salue la franchise de l'orateur sur les limites de Factory. Il signale aussi que le rôle du FDE arrive tard, que le chiffre de **87 %** est présenté au conditionnel comme illustration et que les migrations de 30 à 50 millions de lignes sont citées sans client. Public : équipes qui préparent une base de code pour des agents, ESN de modernisation.

## Pense-betes

- **Format** : 21 min 21, mis en ligne le 28 juillet 2026, ~6 200 vues ; ouvre le track FDE du World's Fair.
- **Refus (vers 3:03)** : pas de modernisation au forfait face aux devis des grands cabinets ; chiffre d'affaires sans apprentissage produit. Cible : un produit qui s'installe presque seul chez des clients de 45 000 personnes et des dizaines de milliers de bases de code.
- **Usine logicielle (vers 5:06)** : signaux (clients, bugs, Slack/Teams, décision d'un dirigeant) → tri humain → plans → code → revue, QA, sécurité, SAST, linters, types → production → surveillance → signaux. Objectif : boucle sans interruption humaine, humains concepteurs et mainteneurs de l'usine.
- **« We like to say this is built, not bought »** : harnais d'agents indépendant des modèles, traces et données détenues par le client, gouvernance centralisée ; déploiements sans réseau (finance, santé, public).
- **Rôle du deployed engineer (vers 8:11)** : modèle de maturité de l'autonomie, préparation du code, conception des workflows, récit du ROI de bout en bout (exemple conditionnel : −87 % de risque de bug après revue, QA et sécurité automatisées).
- **Code prêt pour les agents (vers 12:14)** : densité des boucles de validation déterministes ; analogie avec la récompense dense en entraînement. Règle : un problème formulable en vérifications se résout aujourd'hui avec l'IA. Migrations autonomes revendiquées de 30 à 50 M de lignes.
- **Epcot (vers 16:15)** : une base de code exemplaire trop en avance passe pour un parc d'attractions ; assez proche du quotidien, elle donne envie d'imiter.
- **Franchise** : ~15-20 % d'autonomie sur le code de Factory ; outil juridique interne quasi autonome ; scintillement du harnais terminal non vérifiable automatiquement.
- **Pour une ESN** : compter les boucles de validation d'un dépôt avant d'y lâcher un agent ; migration et mise en vérifiabilité relèvent du savoir-faire ESN.
- **Verdict** : 4/5 et 4/5 ; partie dense 11:14-19:18.

## RésuméDe400mots

SFEIR AI publie le 10 novembre 2026 une critique du talk « How Forward Deployed Engineering is done at Factory », qui ouvrait le track forward deployed engineering de l'AI Engineer World's Fair 2026. L'orateur, Eno Reyes, est cofondateur et CTO de Factory, éditeur des agents de développement Droid, après des passages chez Hugging Face et Microsoft.

Le talk commence par un refus. Quand un client demande à Factory de moderniser une base de code, devis de grands cabinets en main, Eno Reyes décline, même si Factory ferait le travail avec son produit : ce type de mission rapporte du chiffre d'affaires mais n'enseigne rien au produit. Les deployed engineers servent de fer de lance : ils rapportent ce que pensent les directions techniques et les ingénieurs des plus gros clients, pour que Droid s'installe ensuite presque seul chez des organisations de 45 000 personnes.

Eno Reyes décrit le développement comme une usine : des signaux entrent (clients, bugs, messages, décisions), sont triés en plans, traduits en code, passés par revue, QA, analyse de sécurité, linters et vérificateurs de types, puis déployés et surveillés. Factory vise une boucle sans interruption humaine, les humains concevant l'usine elle-même, qui « se construit, ne s'achète pas ». Factory en fournit les briques, dont un harnais d'agents indépendant des modèles, déployable sans réseau.

Le deployed engineer construit avec le client un modèle de maturité de l'autonomie, prépare le code, conçoit les workflows et raconte le retour sur investissement. La préparation du code est la partie que SFEIR juge la plus intéressante : un code prêt pour les agents se mesure à la densité de ses boucles de validation déterministes. Plus elles sont nombreuses, plus un agent travaille longtemps sans humain, comme un modèle a besoin d'une récompense dense. Droid comblerait seul 30 à 40 % des manques ; le reste exige de changer des habitudes.

Pour diffuser ces pratiques, Eno Reyes recommande une base de code exemplaire, ni trop en avance ni trop proche, en citant Epcot. Il admet environ 15 à 20 % d'autonomie sur le code de Factory. Pour une ESN, l'article retient un critère de chiffrage : compter les boucles de validation d'un dépôt. Verdict : originalité 4/5, qualité de l'information 4/5.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | critique FDE Factory Eno Reyes | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| critique FDE Factory Eno Reyes | DOCUMENT | référence | AI Engineer World's Fair 2026 | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Eno Reyes | PERSONNE | dirige | Factory | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Factory | ORGANISATION | a_créé | Droid | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Factory | ORGANISATION | utilise | Forward Deployed Engineering | METHODOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Factory | ORGANISATION | s_oppose_à | missions de modernisation au forfait | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Eno Reyes | PERSONNE | affirme_que | "We like to say this is built, not bought" | CITATION | 0.9 | ATEMPOREL | déclaré_article |
| Software Factory | METHODOLOGIE | utilise | Harness engineering | METHODOLOGIE | 0.82 | ATEMPOREL | déclaré_article |
| code prêt pour les agents | CONCEPT | est_basé_sur | boucles de validation déterministes | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| boucles de validation déterministes | CONCEPT | permet | autonomie longue des agents sans intervention humaine | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| boucles de validation déterministes | CONCEPT | s_inspire_de | récompense dense | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |
| Droid | TECHNOLOGIE | mesure | 30 à 40 % des manques de validation comblés seul | MESURE | 0.78 | STATIQUE | déclaré_article |
| Eno Reyes | PERSONNE | mesure | 15 à 20 % d'autonomie sur le code de Factory | MESURE | 0.8 | STATIQUE | déclaré_article |
| Eno Reyes | PERSONNE | recommande | une base de code exemplaire assez proche du quotidien des équipes (analogie Epcot) | AFFIRMATION | 0.84 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | compter les boucles de validation déterministes d'un dépôt avant d'y lâcher un agent | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Eno Reyes | PERSONNE | rôle | Cofondateur et CTO de Factory ; ex-Hugging Face et Microsoft | AJOUT |
| Factory | ORGANISATION | positionnement FDE | Deployed engineers fer de lance produit, refus des prestations de modernisation | AJOUT |
| Software Factory | METHODOLOGIE | définition (Factory) | Boucle du signal au déploiement sans interruption humaine ; « built, not bought » | AJOUT |
| code prêt pour les agents | CONCEPT | définition | Code mesuré par la densité de ses boucles de validation déterministes | AJOUT |
| boucles de validation déterministes | CONCEPT | composantes | Linters, typage, SAST, analyses de sécurité, tests de bout en bout | AJOUT |
| critique FDE Factory Eno Reyes | DOCUMENT | notes SFEIR | Originalité 4/5, qualité de l'information 4/5 | AJOUT |
