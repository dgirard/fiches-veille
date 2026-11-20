---
themes: [qualite-securite, outils-plateformes]
source: SFEIR
---
# sfeir-rea-sandbox-confinement-2026-10-13

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **13 octobre 2026** (mis à jour le 19 octobre, ~11 000 signes, un schéma, sept sources). Il part de la politique de sécurité de **REA** : *« This is not a sandbox and does not protect against malicious processes already running as the same operating-system user »*. **(1) Ce que protège le pont** : jeton de capacité aléatoire par session, socket Unix réservé à l'utilisateur (TCP local authentifié sous Windows), projet **Ghidra** temporaire avec limites de ressources ; un programme tiers sans jeton est rejeté. **(2) Ce qu'il ne protège pas** : le moteur analyse la cible avec les droits de l'utilisateur (clés SSH, jetons cloud, dépôts), la capture à l'exécution lance la cible, et un binaire peut contenir des **injections de prompt** lues par l'agent (Crawford et McClure, arXiv, 29 mai 2026). **(3) Confiner** : VM ou conteneur jetable, lecture seule, sans dossier partagé ni secret, instantané restaurable ; avec un modèle hébergé la VM reste en ligne, d'où l'interdiction de lancer l'échantillon. La mise à jour du 19 octobre signale l'image communautaire `psyb0t/docker-reverse-engineer-anything` comme modèle de configuration. Volet sécurité de la série ouverte par [[sfeir-rea-trois-schemas-architecture-usage-2026-10-12]].

## Titre Article

REA n'est pas un sandbox : confiner l'analyse d'un binaire inconnu

## Date

2026-10-13

## URL

https://www.sfeir.com/articles/rea-sandbox-confinement/

## Keywords

REA, Reverse Engineer Anything, sandbox, bac à sable, confinement, binaire inconnu, SECURITY.md, pont authentifié, jeton de session, socket Unix, Ghidra, Hopper, IDA, capture à l'exécution, injection de prompt, GhidraMCP, VM jetable, conteneur, Docker, lecture seule, cap-drop, modèle local, modèle hébergé, approbation des outils, RSSI

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, publiée sur sfeir.com (site éditorial de l'ESN).

## Ton

**Profil** : note de sécurité destinée aux RSSI et aux équipes qui installent REA. Français technique, détails d'implémentation (descripteur privé, droits NTFS, options Docker) cités avec précision.

**Style** : ouverture sur la phrase du SECURITY.md, puis structure binaire « ce que le pont protège / le vrai risque », illustrée par un schéma à deux colonnes (« Protégé » / « Non protégé ») et un environnement jetable recommandé. Consignes à l'impératif (« ne se font jamais sur la machine principale », « coupez le réseau »). La mise à jour datée du 19 octobre est signalée dans le corps. FAQ de quatre questions.

**Position épistémique** : sources primaires du dépôt (SECURITY.md, README, DISCLAIMER) et un article arXiv sur les injections de prompt contre les agents de rétro-ingénierie. Les sources communautaires sont qualifiées comme telles : guide « écrit par un amateur », image Docker « non officielle, créée la veille », à prendre « comme modèle de configuration, pas comme une brique à déployer ». L'article rappelle que le confinement ne règle ni l'envoi de données au fournisseur du modèle ni le droit d'analyser la cible.

## Pense-betes

- **Phrase du SECURITY.md** : *« This is not a sandbox »* ; ouvrir un binaire non fiable le confie au moteur local avec les permissions de l'utilisateur.
- **Pont soigné** : jeton de capacité aléatoire par session, transmis par descripteur privé (pas en argument ni en variable d'environnement) ; socket Unix réservé à l'utilisateur (Linux, macOS) ; TCP local authentifié + répertoire NTFS restreint (Windows).
- **Sessions Ghidra** : projet temporaire isolé, répertoires privés, limites CPU/mémoire, suppression à la fermeture → limitent la persistance accidentelle, ne font pas de Ghidra un sandbox.
- **Non protégé** : processus malveillant déjà actif sous le compte ; fichier piégé exploitant une faille du moteur ; chaînes-instructions lues par l'agent ; capture runtime qui lance la cible.
- **Injection de prompt dans un binaire** : Crawford & McClure, arXiv:2605.30677 (29/05/2026), montage GhidraMCP — l'agent décrit un comportement qui n'est pas celui du programme. Parade pratique : garder l'approbation des outils active.
- **Règle** : statique sur binaire d'origine connue = poste de travail possible ; exécution, capture runtime ou binaire inconnu = **jamais sur la machine principale**.
- **Environnement jetable** : VM ou conteneur, FS en lecture seule, aucun dossier ni presse-papiers partagé, instantané restaurable, aucun secret d'entreprise.
- **Contrainte réseau** : modèle hébergé → VM en ligne → **ne jamais lancer l'échantillon** ; modèle local → couper le réseau.
- **Image Docker communautaire** (v0.1.1, 18/10/2026) : `--read-only`, `--cap-drop ALL`, `no-new-privileges`, endpoint sur 127.0.0.1 + jeton ; `--network none` seulement en CLI ; JADX, Apktool, adb mais pas Ghidra.
- **Hors périmètre du confinement** : données transmises au fournisseur du modèle ; droit d'analyser la cible (posséder un fichier ne donne pas permission de toute opération).
- **Chiffre de contexte** : 76 998 étoiles GitHub au 11/10/2026.

## RésuméDe400mots

L'article, signé SFEIR AI, s'adresse aux responsables sécurité qui envisagent d'installer REA (Reverse Engineer Anything), le serveur MCP qui donne à un agent de code les outils d'un rétro-ingénieur. Il part d'une phrase de la politique de sécurité du projet : REA n'est pas un bac à sable et ne protège pas contre les processus malveillants qui tournent déjà sous le même utilisateur. Ouvrir un binaire non fiable confie son analyse au moteur local avec les permissions de l'utilisateur.

Le texte décrit d'abord ce que REA protège. Le pont entre le serveur et les moteurs de décompilation (Hopper, Ghidra, IDA) est authentifié par un jeton aléatoire par session, transmis par un descripteur privé ; il passe par un socket Unix réservé à l'utilisateur, ou par un TCP local authentifié sous Windows. Les sessions Ghidra tournent dans un projet temporaire avec limites de ressources, supprimé à la fermeture. Un programme tiers sans jeton est rejeté.

Il décrit ensuite ce qui n'est pas protégé. Le moteur parse la cible avec les droits de l'utilisateur, à portée de ses clés SSH, jetons cloud et dépôts ; la capture à l'exécution lance la cible. Un second risque tient à l'agent : un binaire peut contenir des chaînes rédigées comme des instructions. Un article de Brian Crawford et Patrick McClure, déposé sur arXiv le 29 mai 2026, montre que de telles injections amènent un agent de rétro-ingénierie à décrire un comportement erroné. L'article recommande de garder l'approbation des outils active.

Pour confiner, la règle est simple : l'analyse statique d'un binaire d'origine connue peut se faire sur un poste de travail ; l'exécution, la capture et l'analyse d'un binaire inconnu jamais. Il faut alors une machine virtuelle ou un conteneur jetable, en lecture seule, sans dossier partagé ni secret, avec un instantané restaurable. Un modèle hébergé exige que la VM reste en ligne, ce qui interdit absolument de lancer l'échantillon ; un modèle local permet de couper le réseau. La mise à jour du 19 octobre signale une image Docker communautaire publiée la veille, configurée en lecture seule et sans capacités, à prendre comme modèle et non comme brique de production.

L'article conclut que le confinement protège le poste mais ne règle ni la question des données transmises au fournisseur du modèle ni celle du droit d'analyser la cible, renvoyées à d'autres volets de la série.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | REA n'est pas un sandbox : confiner l'analyse d'un binaire inconnu | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | affirme_que | This is not a sandbox and does not protect against malicious processes already running as the same operating-system user | CITATION | 0.95 | DYNAMIQUE | déclaré_article |
| pont authentifié par jeton | CONCEPT | fait_partie_de | REA | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| pont authentifié par jeton | CONCEPT | résout | accès d'un programme tiers au moteur d'analyse | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| injection de prompt | CONCEPT | s_applique_à | agents de rétro-ingénierie | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Brian Crawford | PERSONNE | a_créé | Investigating Detection and Obfuscation of Prompt Injection Attacks Against Software Reverse Engineering AI Agents | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| Investigating Detection and Obfuscation of Prompt Injection Attacks Against Software Reverse Engineering AI Agents | DOCUMENT | référence | GhidraMCP | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | analyser tout binaire inconnu dans une VM ou un conteneur jetable, en lecture seule et sans secret | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | ne jamais lancer l'échantillon quand la VM reste en ligne pour un modèle hébergé | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| docker-reverse-engineer-anything | TECHNOLOGIE | est_variante_de | REA | TECHNOLOGIE | 0.78 | DYNAMIQUE | inféré |
| docker-reverse-engineer-anything | TECHNOLOGIE | utilise | JADX | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le confinement ne règle ni les données transmises au fournisseur du modèle ni le droit d'analyser la cible | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | garder l'approbation des outils active et relire ce que l'agent veut exécuter | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | sécurité | Pas un sandbox : pont authentifié par jeton, analyse avec les droits de l'utilisateur | AJOUT |
| pont authentifié par jeton | CONCEPT | définition | Jeton de capacité par session + socket Unix réservé (TCP local authentifié sous Windows) | AJOUT |
| docker-reverse-engineer-anything | TECHNOLOGIE | statut | Image Docker communautaire non officielle (psyb0t), v0.1.1 du 18 octobre 2026 | AJOUT |
| Brian Crawford | PERSONNE | rôle | Co-auteur avec Patrick McClure d'un article arXiv sur les injections de prompt contre les agents de rétro-ingénierie | AJOUT |
| GhidraMCP | TECHNOLOGIE | catégorie | Pont MCP vers Ghidra, montage d'exemple de l'étude arXiv | AJOUT |
