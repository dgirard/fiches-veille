---
themes: [qualite-securite, politique-regulation]
source: SFEIR
---
# sfeir-divulgation-failles-ia-cadre-openai-2026-10-26

## Veille

Article **SFEIR AI** publié sur sfeir.com le **26 octobre 2026** (~11 000 signes, sept sources notées), consacré à la méthode plutôt qu'à la faille, dont le récit figure dans [[sfeir-php2shell-faille-php-course-au-patch-2026-10-21]]. Le **21 octobre 2026**, **OpenAI** a tiré de la coordination de **PHP2Shell** un cadre en **cinq étapes** pour répondre aux failles critiques trouvées par l'IA dans des logiciels très répandus, soumis à consultation. Trois apports. **(A)** Les étapes : valider et corriger en amont (des modèles frontier attaquent le correctif), laisser du temps aux organisations touchées, coordonner avec les acteurs publics (ONCD, **CISA**), préparer les mises à jour, publier sur le site **Patch the Planet** ; notification par vagues selon trois critères écrits, information graduée. **(B)** Ce que le cadre ajoute à la divulgation coordonnée (ISO/IEC **29147**/**30111**, politique **90+30** de Project Zero) : attaque du correctif, cercle élargi par vagues, État dans la boucle dès l'embargo. L'article relève que le secret a tenu jusqu'aux dernières **48 heures**, et que le billet ne nomme ni l'**ENISA** ni le CERT-FR alors que l'article 14 du **Cyber Resilience Act** impose une alerte sous **24 h**. **(C)** Quatre questions ouvertes, dont le **patch d'urgence par un tiers** via la faille elle-même.

## Titre Article

Failles trouvées par IA : le cadre de divulgation qu'OpenAI propose après PHP2Shell

## Date

2026-10-26

## URL

https://www.sfeir.com/articles/divulgation-failles-ia-cadre-openai-php2shell/

## Keywords

divulgation coordonnée, divulgation de vulnérabilités, PHP2Shell, OpenAI, Patch the Planet, Defender's Window, embargo, notification préalable, information graduée, CISA, ONCD, Super Intelligence Force, ISO/IEC 29147, ISO/IEC 30111, Project Zero, 90 jours, Cyber Resilience Act, article 14, ENISA, CERT-FR, patch d'urgence, Daybreak, php2shell-checker, skills Codex, inventaire, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Article d'analyse méthodologique, registre posé et comparatif. Il restitue le cadre d'OpenAI étape par étape en l'attribuant (« OpenAI décrit une coalition qu'elle dit avoir menée ») et signale que la paternité de la découverte reste partagée entre Calif et Wiz. La comparaison avec les normes de divulgation existantes est factuelle. L'angle européen est posé comme un complément (CRA, ENISA, CERT-FR absents du billet), sans polémique. La question du patch d'urgence par un tiers est désignée comme « la plus lourde pour une DSI ». Finale en cinq recommandations concrètes. Public : DSI, RSSI, responsables conformité.

## Pense-betes

- **21 octobre 2026** : en même temps que les correctifs PHP, OpenAI publie *« Patch the Planet: global response coordination as agents uncover critical vulnerabilities »* — cadre en cinq étapes, ouvert aux amendements.
- Rôles : **Calif** (GPT-5.6 Sol, Patch the Planet) et **Wiz** (Atlas, Gemini 4 Argon, GPT-5.6 Sol) découvreurs ; **mainteneurs PHP** écrivent et décident ; OpenAI, Wiz, **Cloudflare** = recherche, support, coordination.
- **Cinq étapes** : (1) valider/corriger en amont, **modèles frontier qui attaquent le correctif** ; (2) laisser du temps (backports, mitigations, règles WAF) ; (3) acteurs publics — Super Intelligence Force, **ONCD**, **CISA** ; (4) élargir le cercle aux distributeurs/hébergeurs ; (5) publier sur le site Patch the Planet avec mitigations et leurs limites.
- **Critères de notification** : rôle de protection, temps nécessaire pour agir, capacité à garder le secret. **Information graduée** (des IoC aux PoC). Calendrier réévalué en cas de fuite ou d'exploitation.
- Référence classique : ISO/IEC **29147** et **30111** ; Project Zero **90 + 30 jours**.
- Contrainte nouvelle (OpenAI) : le temps laissé manque si les capacités frontier ne sont pas très en avance sur celles largement diffusées. PHP2Shell : fuite des CVE le 20 octobre, secret tenu jusqu'aux **48 dernières heures**.
- **CRA art. 14** : depuis le 11 septembre 2026, notification des vulnérabilités activement exploitées, alerte précoce sous **24 h** via la plateforme unique **ENISA** — absents du billet d'OpenAI.
- **Questions ouvertes** : durée des fenêtres ; **patch d'urgence** par un gouvernement ou opérateur via la faille (balayage permanent d'internet évoqué) ; qui pré-notifier ; paquets sûrs par défaut et rétroportage.
- Outils : **php2shell-checker** (script + deux skills Codex) ; **1 Md$** d'accès subventionné à **Daybreak** pour les défenseurs de services essentiels.
- Pistes DSI : inventaire en minutes ; délai correctif → production en une journée ; dépendances = code à soi ; agents vérificateurs en lecture seule, périmètre limité ; répondre à la consultation (ou à l'ENISA).

## RésuméDe400mots

Cet article de SFEIR, publié le 26 octobre 2026, s'intéresse à la méthode de réponse aux failles critiques découvertes par l'IA, à partir de l'affaire PHP2Shell. Le 21 octobre, jour où l'équipe PHP publiait les correctifs de deux failles d'exécution de code à distance, OpenAI racontait les deux mois de coordination qui avaient précédé et en tirait un cadre en cinq étapes, soumis à la communauté sécurité.

OpenAI décrit une coalition qu'elle dit avoir menée : Calif a trouvé une faille avec GPT-5.6 Sol dans le programme Patch the Planet, Wiz a découvert et signalé les deux vulnérabilités de son côté, les mainteneurs de PHP ont écrit les correctifs et décidé de la publication, tandis qu'OpenAI, Wiz, Cloudflare et d'autres ont fourni recherche et coordination. L'entreprise nomme « Defender's Window » le délai gagné sur les attaquants et anticipe une forte hausse de découvertes comparables.

Les cinq étapes sont : valider et corriger en amont, y compris en faisant attaquer le correctif par des modèles de frontière ; laisser du temps aux distributeurs, hébergeurs et fournisseurs de sécurité ; coordonner avec les acteurs publics américains ; élargir le cercle pour préparer les mises à jour ; publier les consignes sur un site dédié. Le choix des organisations prévenues repose sur trois critères écrits, l'information transmise est graduée, et le calendrier se réévalue en cas de fuite ou d'exploitation.

Par rapport à la divulgation coordonnée classique, encadrée par les normes ISO et la politique de 90 jours de Google Project Zero, le cadre ajoute l'attaque du correctif par des modèles, un cercle élargi par vagues et la présence de l'État dès l'embargo. OpenAI reconnaît que le temps disponible se réduit si les capacités de frontière ne sont pas très en avance ; dans PHP2Shell, le secret n'a tenu que jusqu'aux dernières quarante-huit heures. Pour une organisation européenne, le cadre s'ajoute au Cyber Resilience Act, qui impose depuis septembre 2026 une alerte sous vingt-quatre heures via l'ENISA, institution que le billet ne cite pas.

OpenAI liste quatre questions ouvertes, dont celle d'un patch d'urgence réalisé par un tiers autorisé en exploitant la faille elle-même, jugée la plus lourde pour une DSI. Elle accompagne le cadre d'un vérificateur de version PHP sous forme de skills Codex et d'un milliard de dollars d'accès subventionné à sa suite Daybreak.

SFEIR en tire cinq pistes : tenir un inventaire interrogeable en minutes, raccourcir le délai entre correctif et production, traiter les dépendances comme son propre code, confiner les agents vérificateurs, et répondre à la consultation.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Failles trouvées par IA : le cadre de divulgation qu'OpenAI propose après PHP2Shell | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | a_créé | cadre de réponse en cinq étapes | METHODOLOGIE | 0.93 | STATIQUE | déclaré_article |
| cadre de réponse en cinq étapes | METHODOLOGIE | est_basé_sur | PHP2Shell | EVENEMENT | 0.9 | STATIQUE | déclaré_article |
| cadre de réponse en cinq étapes | METHODOLOGIE | affine | divulgation coordonnée | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| cadre de réponse en cinq étapes | METHODOLOGIE | utilise | notification préalable par vagues | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| cadre de réponse en cinq étapes | METHODOLOGIE | recommande | faire attaquer le correctif par des modèles frontier avant sa sortie | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| OpenAI | ORGANISATION | collabore_avec | CISA | ORGANISATION | 0.86 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | affirme_que | le temps laissé aux distributeurs manque si les capacités frontier ne sont pas très en avance sur celles largement diffusées | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| Google Project Zero | ORGANISATION | a_créé | politique de divulgation 90+30 jours | METHODOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Cyber Resilience Act | DOCUMENT | affirme_que | les fabricants notifient toute vulnérabilité activement exploitée avec alerte précoce sous 24 h via l'ENISA | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le billet d'OpenAI ne nomme ni l'ENISA ni les CSIRT nationaux | AFFIRMATION | 0.86 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | php2shell-checker | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| php2shell-checker | TECHNOLOGIE | utilise | Codex | TECHNOLOGIE | 0.84 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | Daybreak for Frontline Defenders | EVENEMENT | 0.84 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le patch d'urgence par un tiers via la faille est la question la plus lourde pour une DSI | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | inventaire interrogeable en minutes et redéploiement de toute une stack en une journée | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | faire tourner les agents vérificateurs en lecture seule dans un périmètre limité | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| cadre de réponse en cinq étapes | METHODOLOGIE | définition | Cadre OpenAI (21 octobre 2026) de réponse coordonnée aux failles trouvées par IA, en consultation | AJOUT |
| divulgation coordonnée | METHODOLOGIE | référence | ISO/IEC 29147 et 30111 ; découvreur, éditeur, coordinateur | AJOUT |
| PHP2Shell | EVENEMENT | description | Deux RCE du moteur PHP corrigées le 21 octobre 2026, cas fondateur du cadre | AJOUT |
| Cyber Resilience Act | DOCUMENT | article 14 | Notification des vulnérabilités exploitées depuis le 11 septembre 2026 | AJOUT |
| php2shell-checker | TECHNOLOGIE | catégorie | Vérificateur de version PHP d'OpenAI (script + deux skills Codex) | AJOUT |
| Daybreak for Frontline Defenders | EVENEMENT | montant | 1 Md$ d'accès subventionné à la suite Daybreak | AJOUT |
