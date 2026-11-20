---
themes: [qualite-securite, outils-plateformes, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-rea-deploiement-entreprise-2026-10-20

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **20 octobre 2026**, mis à jour le 23 (~1 250 mots, huit sources : registre npm, documentation de **REA**, tests d'Ishank Choudhary et de Javier Cañete Arroyo). Il pose les conditions d'un usage de REA en entreprise, l'outil s'étant *« répandu sur les postes de développeurs avant toute décision d'architecture »*. Quatre consignes. **(1) Épingler la version** : le paquet npm **rea-agents** est passé de **4.0.0 à 6.7.0** entre le 5 et le 18 octobre (33 versions au 23 octobre) ; bannir `@latest`, vérifier la provenance après le faux dépôt diffusant un trojan le 13 octobre. **(2) Isoler le profil d'agent** : REA s'enregistre par défaut dans `~/.claude.json` et `~/.claude/skills` ; profil séparé via `CLAUDE_CONFIG_DIR`, `--dry-run` obligatoire ; un profil n'est pas une frontière de sécurité. **(3) Conteneuriser** les cibles inconnues (*« This is not a sandbox »*). **(4) Gouverner outils et modèle** : **207 outils** et une liste de **3 158 352 octets** en 6.7.0, ramenée à **219 211** par le profil compact ; modèle choisi selon la sensibilité de la cible ; politique d'usage écrite. Fait partie de la série SFEIR d'octobre 2026 sur REA.

## Titre Article

Déployer REA en entreprise : versions, profils, conteneurs

## Date

2026-10-20

## URL

https://www.sfeir.com/articles/rea-entreprise-deploiement/

## Keywords

REA, rea-agents, npm, épinglage de version, @latest, chaîne d'approvisionnement, faux dépôt, trojan, MCP, Claude Code, CLAUDE_CONFIG_DIR, profil d'agent, skill, dry-run, conteneur, Docker, sandbox, clean-room, catalogue d'outils, profil compact, fenêtre de contexte, modèle local, politique d'usage, IDA Pro, Hopper, JEB, gouvernance DSI, AI Cyber

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Guide de gouvernance en français, à l'usage des DSI et des équipes sécurité. Le registre est prescriptif et sobre : quatre sections titrées par un verbe à l'infinitif (épingler, isoler, conteneuriser, gouverner), consignes à l'impératif, chaque fait daté et sourcé (versions npm, documentation d'installation, tests publics). Les chiffres sont présentés comme mesures d'un tiers à refaire sur sa propre version (*« Mesurez ces valeurs sur la version que vous épinglez »*). L'article signale les limites de ses propres recommandations, notamment qu'un profil séparé règle la découverte de l'outil mais pas l'accès au shell, aux fichiers et au réseau. Une mise à jour datée du 23 octobre est ajoutée en italique. FAQ et renvoi à l'offre AI Cyber de SFEIR en fin d'article.

## Pense-betes

- **Rythme de publication** : rea-agents **4.0.0 → 6.7.0** du 5 au 18 octobre 2026 ; 6.1.0, 6.2.0, 6.3.0 en moins de 24 h (9-10 octobre) ; **31** versions depuis juillet au 11 octobre (Choudhary), **33** au 23 octobre ; correctifs de sécurité limités à la dernière version publiée.
- **Épingler** : bannir `@latest` ; la commande de configuration épingle déjà la version installée dans l'enregistrement MCP → en faire une décision tracée et revue.
- **Provenance** : faux dépôt du 13 octobre distribuant un exécutable Windows détecté comme trojan ; sources officielles = morluto/rea, rea.tools, paquet npm rea-agents.
- **Profil d'agent** : par défaut, écriture dans `~/.claude.json` et skill sous `~/.claude/skills` → tous les projets peuvent l'appeler ; profil dédié via **`CLAUDE_CONFIG_DIR`** ; `--dry-run` *« returns a read-only plan with status planned »* ; la configuration réelle sauvegarde les fichiers modifiés.
- **Limite du profil** : il contrôle quelles sessions découvrent REA, pas l'accès au shell, aux fichiers ni au réseau ; séparation stricte (réécriture **clean-room**) = compte ou conteneur distinct.
- **Conteneur** : cible inconnue ou hostile en conteneur ou VM jetable ; construire sa propre image (lecture seule, capacités retirées, réseau coupé, jeton) plutôt que dépendre d'un dépôt de quelques jours.
- **Poids dans le contexte** : 6.4.0 = **170 outils**, 1 954 704 octets, profil compact −9 % (Choudhary) ; 6.7.0 = **207 outils**, **3 158 352 octets**, profil compact **219 211 octets** (< 7 %), installation **222 Mo**, **158 dépendances** (Cañete).
- **Modèle et licences** : résultats d'outils envoyés au fournisseur du modèle → modèle local pour un binaire sensible ; IDA Pro, Hopper, JEB sous leur propre licence, REA n'en fournit aucune.
- **Mise à jour du 23 octobre** : dernière version toujours 6.7.0 ; **369 860** étoiles selon l'API GitHub.

## RésuméDe400mots

L'article part d'un constat de rythme : entre le 5 et le 18 octobre 2026, le paquet npm rea-agents est passé de la version 4.0.0 à la 6.7.0, dont trois versions publiées en moins de vingt-quatre heures. REA, outil de rétro-ingénierie piloté par un agent, est né comme un outil individuel et s'est diffusé sur les postes de développeurs avant toute décision d'architecture. Une DSI qui veut l'autoriser doit d'abord le gouverner, selon quatre axes.

Le premier est l'épinglage de la version. Chaque version peut changer le catalogue d'outils, les contrats de sortie ou les prérequis, et les correctifs de sécurité ne visent que la dernière publiée. L'article recommande de bannir `@latest` en production et de faire de la version installée, que la commande de configuration épingle déjà, une décision tracée et revue. Il rappelle aussi l'épisode du faux dépôt du 13 octobre, qui distribuait un exécutable Windows détecté comme trojan, et les trois sources officielles de l'outil.

Le deuxième est l'isolement du profil d'agent. Par défaut, REA s'enregistre pour tout le client : pour Claude Code, dans `~/.claude.json` et sous `~/.claude/skills`, si bien que chaque projet peut l'appeler. Un profil séparé via `CLAUDE_CONFIG_DIR` le réserve aux analyses, et le mode `--dry-run` rend un plan relisable avant toute écriture. Ce profil ne constitue pas une frontière de sécurité : il règle la découverte de l'outil, pas l'accès au shell, aux fichiers et au réseau. Une séparation stricte, par exemple pour une réécriture en clean-room, exige un compte ou un conteneur distinct.

Le troisième est la conteneurisation. La politique de sécurité de REA écrit « This is not a sandbox » ; toute cible inconnue s'analyse dans un conteneur ou une machine virtuelle jetable, sur une image construite en interne selon les principes d'un projet communautaire récent (lecture seule, capacités retirées, réseau coupé, jeton).

Le quatrième est la gouvernance des outils et du modèle. En 6.7.0, REA expose 207 outils dont la liste pèse plus de 3 Mo, ramenée à environ 219 Ko par le profil compact ; ces valeurs sont à mesurer sur la version retenue. Les résultats d'outils partent chez le fournisseur du modèle, d'où un modèle local pour un binaire sensible. L'article recommande une politique d'usage écrite (qui, sur quelles cibles, avec quel modèle, quelle approbation) et rappelle que les moteurs commerciaux restent sous leur propre licence.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Déployer REA en entreprise | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| rea-agents | TECHNOLOGIE | fait_partie_de | REA | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | rea-agents passé de 4.0.0 à 6.7.0 entre le 5 et le 18 octobre 2026 | MESURE | 0.92 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | bannir @latest et épingler une version tracée de REA | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| CLAUDE_CONFIG_DIR | TECHNOLOGIE | permet | profil d'agent dédié aux analyses | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un profil d'agent séparé n'est pas une frontière de sécurité | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| clean-room | METHODOLOGIE | utilise | conteneur | TECHNOLOGIE | 0.8 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | analyser toute cible inconnue dans un conteneur ou une VM jetable | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Javier Cañete Arroyo | PERSONNE | mesure | REA 6.7.0 expose 207 outils, liste de 3 158 352 octets, 219 211 en profil compact | MESURE | 0.9 | STATIQUE | déclaré_article |
| Ishank Choudhary | PERSONNE | mesure | REA 6.4.0 expose 170 outils, profil compact ne retirant qu'environ 9 % | MESURE | 0.88 | STATIQUE | déclaré_article |
| profil compact | CONCEPT | réduit | poids du catalogue d'outils dans le contexte de l'agent | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | choisir le modèle selon la sensibilité de la cible, modèle local pour un binaire sensible | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | écrire une politique d'usage de REA (utilisateurs, cibles, modèle, approbation des outils) | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Javier Cañete Arroyo | PERSONNE | travaille_chez | Jacar Systems | ORGANISATION | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | catégorie | outil de rétro-ingénierie piloté par agent via MCP (morluto/rea), 6.7.0 au 18 octobre 2026 | AJOUT |
| rea-agents | TECHNOLOGIE | catégorie | paquet npm officiel de REA, 33 versions au 23 octobre 2026 | AJOUT |
| CLAUDE_CONFIG_DIR | TECHNOLOGIE | rôle | variable d'environnement de Claude Code isolant un profil d'agent | AJOUT |
| profil compact | CONCEPT | définition | catalogue d'outils réduit de REA pour limiter le poids dans le contexte | AJOUT |
| clean-room | METHODOLOGIE | définition | séparation entre analyse et réécriture, imposée par compte ou conteneur distinct | AJOUT |
| Javier Cañete Arroyo | PERSONNE | rôle | testeur de REA 6.7.0 (Jacar Systems, 19 octobre 2026) | AJOUT |
| Ishank Choudhary | PERSONNE | rôle | auteur d'un test de REA sur HackerNoon (14 octobre 2026) | AJOUT |
