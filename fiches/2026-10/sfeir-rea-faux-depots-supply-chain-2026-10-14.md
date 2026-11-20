---
themes: [qualite-securite, outils-plateformes]
source: SFEIR
---
# sfeir-rea-faux-depots-supply-chain-2026-10-14

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **14 octobre 2026** (~9 000 signes, un schéma, six sources), qui documente un incident de chaîne d'approvisionnement autour de **REA**. **(A) Les faits** : le 13 octobre 2026 à 00 h 42 UTC, l'issue **n° 2424** du dépôt officiel signale le faux dépôt `rea-tools/rea`, dont le nom imite le site rea.tools : README copié, section « Windows Standalone .exe / GUI », release « rea-agents: v6.3.0 » servant une archive de **82,6 Mo** téléchargée **172 fois**, classée **Trojan Wacatac** par Microsoft Defender et marquée par **8 moteurs sur 45** sur VirusTotal ; l'organisation avait été créée le 10 octobre. Deux jours plus tôt, le vrai dépôt gagnait **25 793 étoiles** en une journée. **(B) La réponse** : la PR **n° 2429**, fusionnée le jour même, ajoute dans le README et ses 19 traductions un encadré nommant les trois sources officielles — *« A similar repository name or copied README does not establish that a download is official »*. **(C) La méthode** généralisée à tout serveur **MCP** : cinq vérifications (propriétaire et date du dépôt, champ `repository` du paquet npm, `npm audit signatures`, version épinglée, aucun binaire hors sources officielles), dont la première et la dernière suffisaient ici. Troisième volet sécurité de la série ouverte par [[sfeir-rea-trois-schemas-architecture-usage-2026-10-12]].

## Titre Article

Faux dépôts REA et cheval de Troie : le risque supply chain d'un outil viral

## Date

2026-10-14

## URL

https://www.sfeir.com/articles/rea-faux-depots-supply-chain/

## Keywords

REA, Reverse Engineer Anything, faux dépôt, rea-tools, cheval de Troie, Wacatac, Microsoft Defender, VirusTotal, supply chain, chaîne d'approvisionnement, typosquatting, GitHub, npm, rea-agents, provenance npm, npm audit signatures, épinglage de version, serveur MCP, liste blanche, sources officielles, réponse à incident, SHA-256

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, publiée sur sfeir.com (site éditorial de l'ESN).

## Ton

**Profil** : récit d'incident suivi d'une procédure, destiné aux équipes sécurité et aux développeurs qui installent des serveurs MCP. Français factuel, horodatages UTC, empreinte SHA-256 et libellés de détection reproduits tels quels.

**Style** : chronologie serrée (signalement, PR en moins d'une demi-heure, fusion à 19 h 23 UTC), puis passage du cas particulier à la règle générale (« L'incident vaut pour tout serveur MCP »). Un schéma en cinq étapes met le faux dépôt en regard de la grille de vérification. Consignes de remédiation à l'impératif (« Ne lancez pas l'exécutable », « changez les secrets »). FAQ de quatre questions.

**Position épistémique** : sources primaires (issue et PR du dépôt, métadonnées npm, README). L'article reprend la retenue de la PR, qui évite de répéter l'URL malveillante ou d'affirmer un verdict, et s'interdit lui-même de citer les sites imitateurs « pour ne pas leur donner de visibilité ». Le nombre d'exécutions réelles est explicitement déclaré inconnu. Se termine sur l'offre AI Cyber du cabinet.

## Pense-betes

- **Incident** : issue **#2424**, 13/10/2026 00 h 42 UTC — faux dépôt `rea-tools/rea` imitant rea.tools.
- **Mode opératoire** : README officiel copié + section « Windows Standalone .exe / GUI » ; release « rea-agents: v6.3.0 » (numéro emprunté à une vraie version npm publiée trois jours plus tôt) ; archive `rea-x64.7z` de **82,6 Mo**, **172 téléchargements**.
- **Détection** : Defender `Trojan:Script/Wacatac.B!ml` (archive) et `Trojan:Win32/Wacatac.B!ml` (exécutable) ; VirusTotal **8/45** ; bac à sable : évitement (détection de débogueur, longues pauses, vérification d'interaction utilisateur).
- **Signal faible** : organisation créée le **10 octobre**, un seul dépôt. Contexte : le vrai dépôt avait gagné **25 793 étoiles** en un jour le 11/10.
- **Réponse du projet** : PR **#2429** proposée en moins de 30 min, fusionnée à 19 h 23 UTC ; encadré dans le README et ses **19 traductions** ; pas d'URL malveillante répétée, pas de verdict.
- **Sources officielles** : `github.com/morluto/rea`, `rea.tools`, npm `rea-agents` (ni `rea`, ni `rea-tools`, ni `rea-agent`) ; mainteneur npm unique `morluto` ; **6.5.0** (14/10) avec attestation de provenance npm. Pas d'exécutable Windows officiel : installation par `npx rea-agents setup`.
- **Cinq vérifications avant tout serveur MCP** : (1) propriétaire et date de création du dépôt ; (2) champ `repository` du paquet = dépôt consulté ; (3) `npm audit signatures` ; (4) version exacte épinglée, pas `@latest` ; (5) aucun binaire hors sources officielles.
- **Pour une équipe** : liste blanche des serveurs MCP autorisés (version + source), tenue par la sécurité, revue à chaque mise à jour.
- **Si copie suspecte téléchargée** : ne pas lancer ; sinon isoler le poste, comparer le SHA-256, conserver l'archive, changer les secrets, analyser en environnement confiné, signaler à GitHub.
- **Principe** : un serveur MCP s'exécute avec les droits du développeur → dépendance de premier rang.

## RésuméDe400mots

L'article, signé SFEIR AI, documente un incident de chaîne d'approvisionnement survenu autour de REA, le serveur MCP de rétro-ingénierie devenu viral en octobre 2026, et en tire une méthode de vérification valable pour tout serveur MCP.

Le 13 octobre 2026, un utilisateur ouvre l'issue n° 2424 sur le dépôt officiel pour signaler un imposteur : le dépôt `rea-tools/rea`, dont le nom imite le site officiel rea.tools. Ce faux dépôt copiait le README et ajoutait une section proposant un exécutable Windows autonome, publié sous une release intitulée d'après une vraie version du paquet npm. L'archive de 82,6 Mo avait été téléchargée 172 fois. Microsoft Defender la classait comme cheval de Troie Wacatac, huit moteurs sur 45 la signalaient sur VirusTotal, et l'analyse en bac à sable relevait des comportements d'évitement. L'organisation avait été créée le 10 octobre et ne contenait que ce dépôt. Le contexte explique l'attrait : deux jours plus tôt, le vrai dépôt gagnait 25 793 étoiles en une journée.

Le projet a répondu en moins de 24 heures. Une pull request proposée moins d'une demi-heure après le signalement, fusionnée le jour même, ajoute dans le README et ses 19 traductions un encadré qui nomme les trois sources officielles et précise qu'un nom similaire ou un README copié n'établit pas qu'un téléchargement est officiel. La PR évite volontairement de répéter l'URL malveillante.

Les sources officielles sont le dépôt `morluto/rea`, le site rea.tools et le paquet npm `rea-agents`, publié par un mainteneur unique et doté d'une attestation de provenance depuis la version 6.5.0. L'installation documentée passe par npx ; aucun exécutable Windows n'est distribué officiellement.

L'article généralise : un serveur MCP s'exécute sur le poste du développeur avec ses droits et fournit des outils à un agent, ce qui en fait une dépendance de premier rang. Il propose cinq vérifications avant installation : propriétaire et date de création du dépôt, concordance entre le paquet npm et le dépôt, contrôle des signatures, version exacte épinglée, refus de tout binaire non distribué par les sources officielles. Dans le cas présent, la première et la dernière suffisaient. À l'échelle d'une équipe, ces contrôles prennent la forme d'une liste blanche de serveurs MCP tenue par la sécurité.

En cas de téléchargement d'une copie suspecte, l'article recommande de ne pas l'exécuter, ou à défaut d'isoler le poste, de comparer l'empreinte, de changer les secrets accessibles et de signaler le dépôt à GitHub.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Faux dépôts REA et cheval de Troie : le risque supply chain d'un outil viral | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| faux dépôt rea-tools/rea | EVENEMENT | s_applique_à | REA | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| faux dépôt rea-tools/rea | EVENEMENT | est_instance_de | attaque supply chain | CONCEPT | 0.9 | STATIQUE | inféré |
| faux dépôt rea-tools/rea | EVENEMENT | mesure | archive de 82,6 Mo téléchargée 172 fois, détectée par 8 moteurs sur 45 sur VirusTotal | MESURE | 0.92 | STATIQUE | déclaré_article |
| Microsoft Defender | TECHNOLOGIE | observé_dans | faux dépôt rea-tools/rea | EVENEMENT | 0.86 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | mesure | 25 793 étoiles GitHub gagnées en une journée (11 octobre 2026) | MESURE | 0.86 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | affirme_que | A similar repository name or copied README does not establish that a download is official | CITATION | 0.92 | STATIQUE | déclaré_article |
| provenance npm | CONCEPT | s_applique_à | rea-agents | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| rea-agents | TECHNOLOGIE | fait_partie_de | REA | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un serveur MCP s'exécute avec les droits du développeur et constitue une dépendance de premier rang | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | cinq vérifications avant d'installer un serveur MCP : propriétaire et date, paquet npm, signatures, version épinglée, aucun binaire hors sources | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | une liste blanche de serveurs MCP autorisés tenue par la sécurité | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| épinglage de version | METHODOLOGIE | réduit | risque supply chain | CONCEPT | 0.84 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| faux dépôt rea-tools/rea | EVENEMENT | date | Signalé le 13 octobre 2026 (issue n° 2424), corrigé par la PR n° 2429 le même jour | AJOUT |
| rea-agents | TECHNOLOGIE | catégorie | Paquet npm officiel de REA, mainteneur unique morluto, provenance attestée depuis 6.5.0 | AJOUT |
| REA | TECHNOLOGIE | sources officielles | github.com/morluto/rea, rea.tools, npm rea-agents | AJOUT |
| épinglage de version | METHODOLOGIE | définition | Version exacte fixée dans l'enregistrement MCP plutôt que @latest | AJOUT |
| attaque supply chain | CONCEPT | variante | Nom proche, README copié, binaire ajouté, visant un projet devenu viral | AJOUT |
