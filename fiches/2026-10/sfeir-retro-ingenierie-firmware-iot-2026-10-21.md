---
themes: [qualite-securite, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-retro-ingenierie-firmware-iot-2026-10-21

## Veille

Article **SFEIR AI** publié sur sfeir.com le **21 octobre 2026** (~6 500 signes, FAQ, cinq sources notées), dans la même série que la tribune sur la fin du code fermé. Point de départ : un article de **404 Media** du 20 octobre décrivant des TV connectées débarrassées de leurs publicités et des objets abandonnés remis en service avec des agents de code. L'article précise que rien n'établit que ces projets reposent sur **REA**, le serveur MCP de rétro-ingénierie devenu viral début octobre. Trois apports. **(A)** Ce que REA fait sur un firmware : il pilote **Binwalk 3.1.x** (inspection des régions) et **Unblob 26.6.x** (extraction), sans appareil, root, montage ni émulation, garde le bac à sable **Landlock** d'Unblob, puis passe les ELF extraits à **Ghidra**. **(B)** Deux usages d'entreprise : l'audit défensif d'un équipement avant branchement (identifiants codés en dur, clés, services ouverts, bibliothèques obsolètes), en lien avec le **Cyber Resilience Act**, et la continuité d'équipements sans support. **(C)** Deux risques : le firmware réécrit par IA, dont les bugs ont des conséquences physiques, et le passage de l'analyse statique à l'intervention sur l'appareil. Cadre juridique : directive (UE) **2016/943**, article **L151-3** du Code de commerce. Complète [[sfeir-fin-avantage-code-ferme-2026-10-21]].

## Titre Article

Firmware et objets connectés : la rétro-ingénierie par agents

## Date

2026-10-21

## URL

https://www.sfeir.com/articles/retro-ingenierie-firmware-iot/

## Keywords

rétro-ingénierie, firmware, IoT, objets connectés, REA, serveur MCP, Binwalk, Unblob, Ghidra, Landlock, extraction statique, audit de sécurité, identifiants codés en dur, Cyber Resilience Act, CRA, SBOM, continuité, obsolescence, préservation logicielle, secret d'affaires, directive 2016/943, L151-3, 404 Media, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Article pratique, registre de mise au point. Il commence par ramener l'attention médiatique à ses justes proportions : sur un firmware, REA fait « un travail plus modeste, qui sert surtout une équipe sécurité ». Les capacités de l'outil sont décrites d'après sa propre documentation (versions, prérequis, comportements en cas d'échec), sans extrapolation. Un avertissement explicite écarte la portée de conseil juridique. Les risques sont rendus concrets par des exemples physiques (surchauffe, porte ouverte, alarme muette). La FAQ reprend les questions attendues sur un ton factuel (« Rien ne l'établit »). Clôture sur l'offre AI Cyber de SFEIR. Public : équipes sécurité, responsables d'infrastructure et de parc d'équipements.

## Pense-betes

- Contexte : **404 Media** (20 oct. 2026, via Let's Data Science) — TV connectées « libérées » en un week-end, objets ressuscités, babyphone sans pub. **Aucun lien établi avec REA**.
- **REA** = serveur MCP de rétro-ingénierie. Sur firmware, il **ne réimplémente aucun extracteur** : **Binwalk 3.1.x** (régions) + **Unblob 26.6.x** (extraction), fournis par l'utilisateur ; jalon vérifié sous Linux x64.
- Pas d'appareil, pas de root, pas de montage, **pas d'émulation**, pas d'exécution des binaires extraits. Bac à sable **Landlock** d'Unblob conservé ; jamais de relance `--no-sandbox`.
- Sortie : carte de l'image (chargeur, noyau, systèmes de fichiers) → fichiers extraits → pseudocode via **Ghidra** des ELF choisis. Extracteur manquant signalé, résultats partiels conservés. L'interprétation reste à l'analyste.
- **Usage défensif** : auditer caméra, borne, automate, boîtier réseau avant branchement — identifiants en dur, clés privées, services ouverts, domaines contactés, bibliothèques obsolètes.
- **CRA** : obligations de signalement des fabricants depuis le **11 septembre 2026**.
- **Usage continuité** : équipement sans support ou fabricant disparu → documenter, isoler, préparer le remplacement ; le DISCLAIMER de REA cite la préservation logicielle.
- **Risque 1** : firmware régénéré par agent — Mike Nolan : *« so easy to recreate the functionality that you want »*, mais la maintenance reste lourde. Pas d'installation sans tests, revue, retour arrière.
- **Risque 2** : émulation / flashage modifient l'état de l'appareil ; autorisation d'inspecter ≠ autorisation d'intervenir. REA n'est pas un sandbox.
- Droit : démonter un produit acheté = obtention licite d'un secret d'affaires (directive **2016/943**, art. **L151-3**), sauf contrat contraire ; droit d'auteur, licences, MTP restent distincts.

## RésuméDe400mots

Cet article de SFEIR, publié le 21 octobre 2026, examine ce que la rétro-ingénierie par agents change pour les firmwares et les objets connectés. Il part d'un article de 404 Media du 20 octobre décrivant une vague de bricolage : des particuliers ont remplacé en un week-end le système de leur téléviseur connecté pour en retirer publicités et logiciels imposés, d'autres ont remis en service des objets abandonnés par leur fabricant. L'outil REA, serveur MCP de rétro-ingénierie devenu viral début octobre, a concentré l'attention, mais rien n'indique que ces projets l'aient utilisé.

Sur un firmware, REA fait un travail plus modeste. Il ne réimplémente aucun extracteur et pilote deux outils existants fournis par l'utilisateur : Binwalk pour inspecter les régions d'une image, Unblob pour l'extraction. Ce premier jalon, vérifié sous Linux x64, n'exige ni appareil, ni droits root, ni montage, ni émulation, ni exécution des programmes extraits. Le bac à sable Landlock d'Unblob reste actif et REA ne le désactive jamais en cas d'échec. L'agent obtient une carte de l'image, la liste des fichiers extraits, puis le pseudocode des binaires transmis à Ghidra ; l'interprétation reste celle de l'analyste.

SFEIR identifie deux usages sains pour une entreprise. Le premier est défensif : avant de brancher une caméra, une borne, un automate ou un boîtier réseau, extraire son firmware pour chercher identifiants codés en dur, clés embarquées, services ouverts par défaut, domaines contactés et bibliothèques obsolètes. Le Cyber Resilience Act, dont les obligations de signalement s'appliquent aux fabricants depuis le 11 septembre 2026, couvre ces produits. Le second usage relève de la continuité : documenter, isoler ou préparer le remplacement d'un équipement dont le fabricant a cessé le support ou disparu.

Deux risques sont soulignés. Un firmware réécrit par un agent peut contenir des défauts que son auteur ne sait pas diagnostiquer, avec des conséquences physiques ; Mike Nolan rappelle qu'il est devenu très facile de recréer une fonctionnalité, mais que la maintenance demande un travail considérable. Une entreprise n'installe donc pas un tel firmware sans tests, revue et plan de retour arrière. Ensuite, l'analyse change de nature quand on passe de l'extraction statique à l'émulation ou au flashage, qui peuvent modifier l'état d'un appareil ; REA n'est pas un bac à sable.

Sur le plan juridique, présenté sans valeur de conseil, démonter un produit acheté constitue un mode licite d'obtention d'un secret d'affaires selon la directive (UE) 2016/943 et l'article L151-3 du Code de commerce, sauf engagement contractuel contraire ; droit d'auteur, licences et mesures techniques restent des questions distinctes.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Firmware et objets connectés : la rétro-ingénierie par agents | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | est_instance_de | serveur MCP | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Binwalk | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Unblob | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Unblob | TECHNOLOGIE | utilise | Landlock | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| rétro-ingénierie par agents | METHODOLOGIE | s_applique_à | firmware | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| rétro-ingénierie par agents | METHODOLOGIE | permet | audit de sécurité d'un équipement avant branchement | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| rétro-ingénierie par agents | METHODOLOGIE | permet | continuité d'équipements sans support fabricant | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| Cyber Resilience Act | DOCUMENT | s_applique_à | objets connectés | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Mike Nolan | PERSONNE | affirme_que | il est devenu très facile de recréer une fonctionnalité, mais maintenir un logiciel reste un travail considérable | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | ne pas installer de firmware réécrit par IA sans tests, revue et plan de retour arrière | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | REA n'est pas un bac à sable : l'émulation et le flashage changent la nature de l'analyse | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| directive (UE) 2016/943 | DOCUMENT | affirme_que | démonter un produit acheté est un mode licite d'obtention d'un secret d'affaires, sauf contrat contraire | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| 404 Media | ORGANISATION | publie | 'Reverse-Engineer Anything' Is the New Wild West of AI | DOCUMENT | 0.88 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| REA | TECHNOLOGIE | capacité firmware | Pilote Binwalk et Unblob sous Linux x64, sans émulation ni exécution | AJOUT |
| Binwalk | TECHNOLOGIE | rôle | Inspection des régions d'une image firmware (3.1.x) | AJOUT |
| Unblob | TECHNOLOGIE | rôle | Extraction de firmware (26.6.x), bac à sable Landlock | AJOUT |
| rétro-ingénierie par agents | METHODOLOGIE | définition | Agent de code pilotant extracteurs et décompilateurs pour analyser un binaire ou un firmware | AJOUT |
| Cyber Resilience Act | DOCUMENT | jalon | Obligations de signalement des fabricants depuis le 11 septembre 2026 | AJOUT |
| Mike Nolan | PERSONNE | rôle | Chercheur en politique de l'open source, cité par 404 Media | AJOUT |
| directive (UE) 2016/943 | DOCUMENT | objet | Protection des secrets d'affaires (transposée art. L151-3 Code de commerce) | AJOUT |
