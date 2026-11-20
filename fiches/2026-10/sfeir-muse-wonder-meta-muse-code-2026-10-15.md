---
themes: [produits-services, economie-marche, politique-regulation]
source: SFEIR
---
# sfeir-muse-wonder-meta-muse-code-2026-10-15

## Veille

Article d'actualité **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** (~6 500 signes, un tableau, dix sources), consacré au lancement par **Meta**, le 12 octobre, de **Muse Wonder** et **Muse Wonder Full**, ses modèles destinés aux agents personnels et professionnels. Trois apports. **(A)** Les deux canaux : Muse Wonder est vendu à l'API (**4 $ / 20 $** le million de tokens en entrée / sortie) ; **Muse Wonder Full n'a pas d'API** et reste réservé aux abonnés **Muse Code** (50 $ et 200 $ par mois) ; les poids des deux sont fermés, seul **Muse Glimmer** (30 Md de paramètres, Apache 2.0) est ouvert. **(B)** Les mesures d'**Artificial Analysis** : Muse Wonder Full à **56** sur l'Intelligence Index v4.3 (Claude Opus 5.5 : 58), **1 857 Elo** sur GDPval-AA (Opus 5.5 : 1 866), 68 sur le Coding Agents Index, mais **30** sur AA-Omniscience contre 46 pour Opus 5.5. **(C)** La gouvernance des données : dans Muse Code, le **« Contributor mode »** est activé par défaut et entraîne les modèles sur les prompts et le code ; l'API fonctionne sans entraînement. L'article relève aussi que l'app Muse reste limitée aux États-Unis et au Canada. Suite de [[meta-muse-code-muse-spark-1-2-2026-08-05]].

## Titre Article

Muse Wonder : Meta rejoint la frontière et garde son meilleur modèle pour Muse Code

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/muse-wonder-meta-frontier-muse-code/

## Keywords

Muse Wonder, Muse Wonder Full, Meta, Muse Code, Muse Glimmer, Muse Spark 1.3, modèle frontier, poids fermés, Llama, API Meta, prix par million de tokens, abonnement, Active Memory, Active Focus, Artificial Analysis, Intelligence Index, GDPval-AA, Coding Agents Index, AA-Omniscience, Claude Opus 5.5, GPT-6 Astra, Gemini 4 Argon, Contributor mode, entraînement sur les données utilisateur, RGPD, AI Act, code de bonnes pratiques, Europe

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article d'actualité produit écrit pour une DSI, qui ramène l'annonce à trois questions pratiques : accès, performance mesurée, traitement des données. Français sobre, un tableau de scores, une section Europe.

**Style** : les fonctions mises en avant par Meta (Active Memory, Active Focus) sont décrites dans les termes de l'éditeur, puis suivies des chiffres annoncés et des réserves de la presse (Next, VentureBeat). Les résultats d'Artificial Analysis sont distingués des scores de concurrents rapportés par VentureBeat. La conclusion opérationnelle tient en deux phrases : Full est hors d'atteinte d'une chaîne d'agents faute d'API ; Wonder peut entrer dans un panel d'évaluation.

**Position épistémique** : attribution systématique des chiffres (Meta, Artificial Analysis, Next, VentureBeat). Les critiques sont celles de journalistes nommés (Alexandre Laurent sur Active Memory, Carl Franzen sur les comparaisons de code). Le texte signale ce qui manque : rapport de sécurité complet non publié, liste des pays de l'API non publiée.

## Pense-betes

- **Lancement** : 12 octobre 2026, Meta, premiers modèles frontier depuis la réorganisation de l'IA par Alexandr Wang (août 2025).
- **Muse Wonder** (`muse-wonder-1.0`) : API + Muse Code ; **4 $ entrée / 0,20 $ cache / 20 $ sortie** par million de tokens (tarif de Gemini 4 Argon après promotion).
- **Muse Wonder Full** : **pas d'API** ; Muse Code à 50 $/mois (Power Usage) et 200 $/mois (Maximum Usage) ; 42,99 €/mois en France (Next).
- **Commun** : 1 M de tokens de contexte, entrée texte/image/vidéo/audio, sortie texte, **poids fermés**. Ouvert : Muse Glimmer (30 Md, Apache 2.0).
- **Fonctions** : Active Memory (contexte entre conversations), Active Focus (reprise sur erreur, demande de précisions, consultation avant action importante). Chiffres Meta : mémoire 85,6 % vs 81,5 % (Opus 5.5), focus 54,2 % vs 45,8 %.
- **Artificial Analysis** :
  - Intelligence Index v4.3 : Opus 5.5 58, **Wonder Full 56**, Sonnet 5.5 56, GPT-6 Astra 53, Gemini 4 Argon 53, Wonder 52, Muse Spark 1.3 48
  - AA-Omniscience : Opus 5.5 46, GPT-6 Astra 43, Argon 42, **Wonder Full 30**, Wonder 25
  - GDPval-AA : Wonder Full 1 857 Elo, Opus 5.5 1 866, Sonnet 5.5 1 838
  - Coding Agents Index : Muse Code + Wonder Full 68 = Claude Code + Sonnet 5.5 ; Claude Code + Opus 5.5 66
  - coût d'évaluation : 4,52 $ (Wonder) vs 5,98 $ (Opus 5.5)
- **Données** : Contributor mode **actif par défaut** dans Muse Code (désactivation non rétroactive) ; API en mode Standard, sans entraînement.
- **Europe** : app Muse limitée aux États-Unis et au Canada ; Muse Code vendu en France ; Meta n'a pas signé le code de bonnes pratiques de l'AI Act (The Next Web).
- **Conseil DSI** : tester Muse Wonder sur ses tâches d'agent et sur des questions factuelles ; éviter Muse Code sur un dépôt client avec le réglage par défaut.

## RésuméDe400mots

L'article de SFEIR présente les deux modèles lancés par Meta le 12 octobre 2026, Muse Wonder et Muse Wonder Full, destinés aux agents personnels et professionnels dans le code, le droit, la finance et la santé.

Les deux modèles suivent des canaux distincts. Muse Wonder est disponible sur l'API de Meta à 4 dollars le million de tokens en entrée et 20 dollars en sortie, ainsi que dans Muse Code. Muse Wonder Full n'a pas d'API : il est réservé aux abonnements Muse Code à 50 et 200 dollars par mois. Les deux acceptent un million de tokens de contexte et des entrées multimodales ; leurs poids sont fermés, Meta ne citant comme modèle ouvert que Muse Glimmer, sous licence Apache 2.0. L'article rappelle que Meta s'était fait connaître par les poids ouverts de Llama.

Meta met en avant deux fonctions : Active Memory, qui conserve le contexte utile d'une conversation à l'autre, et Active Focus, qui maintient l'objectif sur les tâches complexes. L'éditeur annonce des scores supérieurs à Claude Opus 5.5 sur ses propres tests ; un journaliste de Next juge qu'Active Memory reprend une fonction déjà proposée par les concurrents.

Les mesures d'Artificial Analysis placent Muse Wonder Full à 56 points sur l'Intelligence Index, derrière Claude Opus 5.5 (58) et devant GPT-6 Astra et Gemini 4 Argon (53). Sur GDPval-AA, il obtient 1 857 points Elo, dans la marge d'erreur d'Opus 5.5 ; sur le Coding Agents Index, Muse Code animé par Wonder Full égale Claude Code avec Sonnet 5.5. Son point faible est la connaissance factuelle : 30 points sur AA-Omniscience contre 46 pour Opus 5.5. VentureBeat note que Meta a comparé ses concurrents avec des outils différents.

Sur les données, Muse Code active par défaut un mode Contributor qui utilise prompts et code pour entraîner les modèles ; la désactivation ne vaut que pour la suite. L'API n'entraîne pas sur les données. L'article en tire une conséquence pour les DSI : un développeur qui essaie Muse Code sur un dépôt client avec le réglage par défaut transmet ce code à Meta.

En Europe, l'application Muse reste limitée aux États-Unis et au Canada, Muse Code est déjà vendu en France, et Meta n'a pas signé le code de bonnes pratiques de l'AI Act. L'article conclut que Muse Wonder Full ne peut pas entrer dans une chaîne d'agents faute d'API, que Muse Wonder peut être évalué sur des tâches réelles, et que le rapport de sécurité complet n'est pas encore publié.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Muse Wonder : Meta rejoint la frontière et garde son meilleur modèle pour Muse Code | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Meta | ORGANISATION | publie | Muse Wonder | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Meta | ORGANISATION | publie | Muse Wonder Full | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Muse Wonder Full | TECHNOLOGIE | fait_partie_de | Muse Code | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Muse Wonder | TECHNOLOGIE | remplace | Muse Spark 1.3 | TECHNOLOGIE | 0.8 | DYNAMIQUE | inféré |
| Artificial Analysis | ORGANISATION | mesure | Muse Wonder Full à 56 points sur l'Intelligence Index v4.3 contre 58 pour Claude Opus 5.5 | MESURE | 0.92 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | Muse Wonder Full à 1 857 Elo sur GDPval-AA contre 1 866 pour Claude Opus 5.5 | MESURE | 0.9 | STATIQUE | déclaré_article |
| Artificial Analysis | ORGANISATION | mesure | Muse Wonder Full à 30 sur AA-Omniscience contre 46 pour Claude Opus 5.5 | MESURE | 0.9 | STATIQUE | déclaré_article |
| Muse Wonder Full | TECHNOLOGIE | surpasse | GPT-6 Astra | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Muse Wonder Full | TECHNOLOGIE | surpasse | Gemini 4 Argon | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Muse Wonder Full | TECHNOLOGIE | concurrence | Claude Opus 5.5 | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Muse Code | TECHNOLOGIE | concurrence | Claude Code | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Muse Code | TECHNOLOGIE | utilise | Contributor mode | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Contributor mode | CONCEPT | permet | entraînement des modèles de Meta sur les prompts et le code des utilisateurs | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Muse Wonder | TECHNOLOGIE | utilise | Active Memory | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Meta | ORGANISATION | publie | Muse Glimmer | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Carl Franzen | PERSONNE | s_oppose_à | comparaisons de code de Meta menées avec des outils différents selon les modèles | CONCEPT | 0.82 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | tester Muse Wonder sur ses tâches d'agent et sur des questions factuelles | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle, éditeur de sfeir.com | AJOUT |
| Meta | ORGANISATION | stratégie modèles | Poids fermés pour Muse Wonder ; Muse Glimmer seul modèle ouvert cité | AJOUT |
| Muse Wonder | TECHNOLOGIE | prix | API 4 $ / 0,20 $ cache / 20 $ par million de tokens ; 52 points Intelligence Index | AJOUT |
| Muse Wonder Full | TECHNOLOGIE | accès | Sans API, réservé aux abonnés Muse Code (50 $ et 200 $/mois) | AJOUT |
| Muse Code | TECHNOLOGIE | catégorie | Outil de développement agentique de Meta, vendu en France (42,99 €/mois) | AJOUT |
| Muse Glimmer | TECHNOLOGIE | licence | 30 Md de paramètres, Apache 2.0 | AJOUT |
| Contributor mode | CONCEPT | défaut | Activé par défaut dans Muse Code, désactivation non rétroactive | AJOUT |
| Active Memory | CONCEPT | définition | Mémoire du contexte utilisateur entre conversations (Meta) | AJOUT |
| Artificial Analysis | ORGANISATION | rôle | Évaluateur indépendant ; Intelligence Index, GDPval-AA, AA-Omniscience | AJOUT |
| Carl Franzen | PERSONNE | support | Journaliste, VentureBeat | AJOUT |
