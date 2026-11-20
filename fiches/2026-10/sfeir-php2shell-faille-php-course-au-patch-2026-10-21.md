---
themes: [qualite-securite, politique-regulation]
source: SFEIR
---
# sfeir-php2shell-faille-php-course-au-patch-2026-10-21

## Veille

Article d'actualité **SFEIR AI** publié sur sfeir.com le **21 octobre 2026**, jour de la publication des correctifs (~20 000 signes, frise, 18 sources notées : php.net, Sansec, Wiz, OpenAI, CERT-EU, CERT-FR, Cloudflare, The Record…). Il couvre **PHP2Shell** : deux RCE non authentifiées du moteur PHP, **CVE-2026-109618** et **CVE-2026-109619** (CVSS v4.0 **9.2**), corrigées en **8.5.12, 8.4.27, 8.3.36, 8.2.35**. Trois apports. **(A)** La chronologie : **Calif** (GPT-5.6 Sol, programme **Patch the Planet**) identifie les chemins le **1er août**, **Wiz Research** (Wiz Atlas, **Gemini 4 Argon**, GPT-5.6 Sol) le **19 août** ; fuite le 20 octobre, correctifs le 21 vers **13h30 UTC**. **(B)** Le mécanisme commun : une erreur fatale (dépassement de `memory_limit`) fait sauter PHP hors du code sans nettoyage, laissant un état que la requête suivante réutilise. **(C)** La « **Defender's Window** » d'OpenAI — deux mois laissés aux défenseurs — se referme à la publication du patch : *« a single researcher completed in a week what previously would have taken a world-class team months of work »* (Wiz). Liste d'actions immédiates (mise à jour, redémarrage des workers, mitigations partielles). Prolonge [[sfeir-gpt56-sol-terra-luna-coding-agentique-pricing-2026-07-13]] côté usage cyber des modèles frontier.

## Titre Article

PHP2Shell : l'IA a trouvé la faille avant les attaquants, la course au patch commence

## Date

2026-10-21

## URL

https://www.sfeir.com/articles/php2shell-faille-php-ia-course-au-patch/

## Keywords

PHP2Shell, CVE-2026-109618, CVE-2026-109619, PHP, RCE, exécution de code à distance, sécurité mémoire, memory_limit, longjmp, mod_php, PHP-FPM, Defender's Window, Patch the Planet, divulgation coordonnée, GPT-5.6 Sol, Gemini 4 Argon, Wiz, Calif, Sansec, WAF, Cloudflare, CERT-FR, patch management, dette de versions, AISecOps, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Article d'alerte rédigé à chaud, registre journalistique et opérationnel. La chronologie est horodatée à la minute (UTC) et chaque fait renvoie à une source numérotée ; les estimations sont signalées comme telles (« c'est une estimation, mais elle décrit le problème »). Le texte vulgarise le mécanisme technique par une image (l'employé interrompu qui part sans ranger) avant de détailler les CVE. Il donne place à des voix contrastées : l'enthousiasme de Wiz et d'OpenAI, le discours plus mesuré de Calif (modèles accessibles à tous, poids de l'expertise humaine), la prudence de watchTowr. La partie « À faire aujourd'hui » adopte le registre de la consigne (listes d'actions, paramètres php.ini exacts). La section « point de vue de SFEIR » conclut sur la double face de l'IA en sécurité et sur l'industrialisation du patch d'urgence. Public : DSI, RSSI, équipes d'exploitation PHP.

## Pense-betes

- **Correctifs** du 21 octobre 2026 : PHP **8.5.12, 8.4.27, 8.3.36, 8.2.35** ; deux CVE notées **9.2** (CVSS v4.0). Bug présent depuis **14 ans** selon Greg Brockman.
- **Chronologie** : Calif 1er août (GPT-5.6 Sol, Patch the Planet) → signalement 11 août ; Wiz 19 août → RCE Drupal 20, WordPress 21, rapports 24 août ; accusé PHP 21 sept. ; divulgation visée le 22 oct., **fuite le 20** ; patchs ~13h30 UTC le 21.
- Coalition pilotée deux mois par **OpenAI** avec la « Super Intelligence Force » de la Maison Blanche, ONCD, **CISA** et partenaires internationaux.
- **Mécanisme** : `memory_limit` dépassé → `longjmp` sans nettoyage. 109618 = données à moitié initialisées (multipart) ; 109619 = état libéré mais réutilisé par la requête suivante du même worker (`session.upload_progress`, backtraces PHP 8.5).
- Exploits démontrés : images Docker officielles WordPress, Drupal, Joomla ; Magento 2.4.9 + dix applications (Sansec). Risque max sur **mod_php** : attaque avant tout code applicatif.
- Exposition : depuis PHP **5.4** ; PHP = **69,3 %** des sites à langage connu (W3Techs) ; ~**36 %** des sites WordPress sous PHP < 8.2 (16 % en 7.4). PHP 8.2 en fin de support le **31/12/2026**.
- **Cloudflare** : règles WAF dès 3h02 UTC ; Dane Knecht : *« This is a STOPGAP only »*.
- **Calif** (via The Next Web) : modèles grand public, sans harnais ; la connaissance de l'historique PHP a pesé autant que le modèle.
- À faire : mettre à jour, **redémarrer les workers**, isoler ≤ 8.1, mitigations partielles (`session.upload_progress.enabled=0`, `fatal_error_backtraces=0`, `post_max_size` bas, filtrage multipart) — aucune ne rend sûr.
- Thèse SFEIR : la fenêtre divulgation → exploitation se compte **en heures** ; le cycle mensuel de patch ne suffit plus pour l'exposé internet ; IA à intégrer dans la boucle de défense (AISecOps).

## RésuméDe400mots

Publié par SFEIR le 21 octobre 2026, jour de la sortie des correctifs, cet article décrit l'affaire **PHP2Shell** : deux vulnérabilités du moteur PHP, CVE-2026-109618 et CVE-2026-109619, notées 9.2 en CVSS v4.0, qui permettent une exécution de code à distance sans authentification. Le projet PHP a publié en urgence les versions 8.5.12, 8.4.27, 8.3.36 et 8.2.35. Selon Greg Brockman, président d'OpenAI, le code fautif existait depuis quatorze ans.

La chronologie, reconstituée d'après Sansec, Wiz, Tenable et le CERT-EU, commence le 1er août, quand Calif, travaillant avec GPT-5.6 Sol dans le programme Patch the Planet d'OpenAI, identifie plusieurs chemins d'exécution. Wiz Research trouve le problème indépendamment le 19 août avec Wiz Atlas, Gemini 4 Argon et GPT-5.6 Sol. OpenAI coordonne pendant deux mois une coalition de mainteneurs et de fournisseurs, avec l'ONCD et la CISA. Une fuite le 20 octobre précipite la publication ; Cloudflare déploie des règles WAF dès la nuit et observe des attaques à 7h43 UTC.

Les deux failles partagent une racine : lorsqu'une requête dépasse `memory_limit`, PHP sort brutalement du code en cours sans nettoyer. La première exploite des données à moitié initialisées, la seconde un état libéré que la requête suivante du même worker réutilise. Wiz et Sansec ont démontré des RCE sur WordPress, Drupal, Joomla, Magento et une dizaine d'autres applications ; une application irréprochable reste vulnérable si l'interpréteur l'est. L'exposition remonte à PHP 5.4, et une part importante du parc tourne sur des versions non maintenues.

OpenAI parle de « Defender's Window » : l'IA aurait trouvé ces failles avant les attaquants, laissant deux mois aux défenseurs. Wiz affirme qu'un chercheur a fait en une semaine le travail de mois d'une équipe de pointe. Calif nuance : sa découverte s'est faite avec des modèles accessibles à tous, et l'expertise de l'historique de PHP a autant compté. L'accélération vaut aussi pour l'attaquant : des preuves de concept générées avec l'IA circulaient, sans exploitation réussie confirmée le jour même.

L'article en tire des conséquences : la fenêtre entre divulgation et exploitation se mesure en heures, le cycle mensuel de patch ne suffit plus pour les composants exposés, la dette de versions devient un risque immédiat, et le WAF n'est qu'un palliatif. Il liste les actions du jour (mise à jour, redémarrage des workers, isolement des versions anciennes, mitigations partielles, surveillance) et recommande d'intégrer l'IA dans la boucle de défense.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | PHP2Shell : l'IA a trouvé la faille avant les attaquants, la course au patch commence | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| PHP2Shell | EVENEMENT | s_applique_à | PHP | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| PHP2Shell | EVENEMENT | mesure | deux CVE notées 9.2 en CVSS v4.0, RCE non authentifiée | MESURE | 0.95 | STATIQUE | déclaré_article |
| Calif | ORGANISATION | utilise | GPT-5.6 Sol | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Wiz | ORGANISATION | utilise | Gemini 4 Argon | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Wiz | ORGANISATION | utilise | GPT-5.6 Sol | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Calif | ORGANISATION | fait_partie_de | Patch the Planet | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | a_créé | Patch the Planet | METHODOLOGIE | 0.9 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | collabore_avec | CISA | ORGANISATION | 0.86 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | affirme_que | l'IA frontier a trouvé ces failles avant les attaquants, ouvrant une Defender's Window de deux mois | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Wiz | ORGANISATION | affirme_que | un seul chercheur a fait en une semaine le travail de plusieurs mois d'une équipe de premier plan | CITATION | 0.9 | STATIQUE | déclaré_article |
| Calif | ORGANISATION | affirme_que | la découverte initiale s'est faite avec des modèles grand public, l'expertise de PHP ayant autant pesé | AFFIRMATION | 0.82 | STATIQUE | déclaré_article |
| Cloudflare | ORGANISATION | publie | règles WAF PHP2Shell | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | prédit | les découvertes de vulnérabilités similaires vont fortement augmenter dans les mois à venir | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la fenêtre entre divulgation et exploitation se compte en heures ; le cycle mensuel de patch ne suffit plus | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | AISecOps | METHODOLOGIE | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | mettre à jour PHP et redémarrer tous les workers le jour même | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| PHP2Shell | EVENEMENT | description | Deux RCE du moteur PHP (CVE-2026-109618/109619) corrigées le 21 octobre 2026 | AJOUT |
| PHP | TECHNOLOGIE | catégorie | Langage serveur, 69,3 % des sites à langage connu (W3Techs) | AJOUT |
| Calif | ORGANISATION | rôle | Premier découvreur (1er août 2026) | AJOUT |
| Wiz | ORGANISATION | rôle | Découvreur indépendant (19 août 2026), outil Wiz Atlas | AJOUT |
| Patch the Planet | METHODOLOGIE | définition | Programme OpenAI de découverte et coordination de correctifs par agents | AJOUT |
| Gemini 4 Argon | TECHNOLOGIE | rôle | Modèle Google crédité par Wiz pour découverte, exploit et validation du patch | AJOUT |
| GPT-5.6 Sol | TECHNOLOGIE | rôle | Modèle OpenAI utilisé par Calif et Wiz | AJOUT |
| AISecOps | METHODOLOGIE | définition | Le modèle qui trouve la faille sert aussi à détecter et valider le correctif | AJOUT |
