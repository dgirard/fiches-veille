---
themes: [qualite-securite, outils-plateformes]
source: SFEIR
---
# sfeir-rea-android-apk-2026-10-19

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **19 octobre 2026** (~1 200 mots, cinq sources : README, documentation Android, SECURITY.md et DISCLAIMER.md de **REA**, plus une image Docker communautaire). Il décrit l'usage de REA, outil de rétro-ingénierie par agents, pour **auditer une APK** avant de l'autoriser dans un parc. **(A) Ce que REA lit** : le code via **JADX** headless (manifeste, classes, méthodes décompilées, références), les ressources via **Apktool** (manifeste décodé, chaînes, locales, version), les signatures v1 à v3.1 ; le pont est épinglé à **jadx-headless-mcp 0.7.1** avec empreinte SHA-256 et JDK 17+. **(B) L'audit type** tient en trois listes : permissions, SDK embarqués (analytics, publicité, suivi), domaines et points de terminaison, chaque trouvaille localisée dans l'archive. **(C) Confinement** : REA *« n'est pas un sandbox »* ; l'image psyb0t/docker-reverse-engineer-anything (18 octobre) illustre une posture lecture seule, `--cap-drop ALL`, réseau coupé. **(D) Limites** : code chiffré, chargé dynamiquement ou natif hors de portée ; une liste de domaines dit ce que l'application *peut* contacter, pas ce qu'elle contacte. Fait partie de la série SFEIR d'octobre 2026 sur REA.

## Titre Article

REA et Android : auditer une APK avec JADX et Apktool

## Date

2026-10-19

## URL

https://www.sfeir.com/articles/rea-android-apk/

## Keywords

REA, rétro-ingénierie par agents, Android, APK, JADX, jadx-headless-mcp, Apktool, adb, manifeste, permissions, SDK de tracking, analytics, signatures APK, MCP, analyse statique, analyse dynamique, émulateur, Docker, confinement, sandbox, RGPD, audit d'application mobile, obfuscation, AI Cyber

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Fiche technique en français, destinée aux équipes sécurité et aux DSI qui gèrent un parc de terminaux mobiles. Le registre est descriptif et précis : versions épinglées, prérequis, options de conteneur, chacun renvoyé à une source numérotée. L'article distingue soigneusement ce que l'outil lit (statique) de ce qu'il ne voit pas (dynamique, chiffré, natif) et consacre une section aux limites. La prudence est constante : l'image Docker communautaire est présentée comme *« jeune »* et *« confidentielle »*, illustrant une posture plutôt qu'une recommandation ; le cadre juridique est renvoyé au juriste du lecteur et au DISCLAIMER de REA. Une FAQ et un appel à l'offre AI Cyber de SFEIR terminent l'article, avec des renvois vers les autres pages du dossier REA.

## Pense-betes

- **Prérequis** : JADX headless + JDK complet, Linux, macOS ou Windows x64 ; Apktool fourni par l'utilisateur.
- **Trois cibles Android** dans le README : **code** (JADX : manifeste, classes, méthodes décompilées, références), **ressources** (Apktool : manifeste décodé, tables de chaînes, locales, version), **signatures** (signataires v1 à v3.1, empreintes, rotation de clé). Pilotage d'un appareil via **adb** = analyse dynamique, autre niveau de précaution.
- **Version épinglée** : **jadx-headless-mcp 0.7.1**, empreinte SHA-256 publiée à vérifier, JDK 17+ (compilateur compris). Le composant qui ouvre l'APK est un jar téléchargé : son intégrité se contrôle.
- **Audit avant mise en catalogue** : trois listes, **permissions**, **SDK embarqués** (analytics, pub, suivi), **domaines et endpoints** ; alimente les vérifications préalables et un contrôle RGPD.
- **Preuve** : chaque trouvaille arrive avec sa localisation dans l'archive.
- **Image psyb0t/docker-reverse-engineer-anything** (18 octobre 2026, non officielle) : OpenJDK 21, jadx-headless-mcp 0.7.1, Apktool 3.0.3, adb 34.0.5 ; mode MCP en lecture seule, `--cap-drop ALL`, `no-new-privileges`, endpoint sur `127.0.0.1:8080` derrière un jeton ; mode CLI avec `--network none`. Pas de Ghidra.
- **Limites** : code chiffré, chargé dynamiquement ou en bibliothèque native invisible ; obfuscation = noms illisibles ; pour savoir ce que l'application contacte, l'exécuter en émulateur isolé.
- **Droit** : *posséder un fichier ne donne pas toutes les permissions* (DISCLAIMER de REA) ; déployer une application ne vaut pas autorisation de la décompiler.

## RésuméDe400mots

L'article décrit comment REA, un outil de rétro-ingénierie piloté par un agent, sert à auditer une application Android avant de l'autoriser dans un parc de terminaux gérés. Pour une APK, REA demande JADX en mode headless et un JDK complet, sous Linux, macOS ou Windows x64. L'agent reçoit en retour les déclarations du manifeste, les classes, les méthodes décompilées et leurs références, de quoi répondre à la question d'une équipe sécurité : quelles données l'application touche, et vers quels serveurs elle peut les envoyer.

Le README de REA distingue trois cibles Android. Le code passe par JADX headless. Les ressources passent par un lanceur Apktool fourni par l'utilisateur, qui décode manifeste, tables de chaînes, locales et informations de version. Les signatures sont lues par un outil statique (signataires v1 à v3.1, empreintes, rotation de clé). Un appareil ou un émulateur peut aussi être piloté via adb, ce qui relève de l'analyse dynamique. La documentation épingle la version du pont, jadx-headless-mcp 0.7.1, dont l'empreinte SHA-256 doit être vérifiée, avec un JDK 17 ou plus récent.

L'audit défensif type tient en trois listes : permissions demandées, bibliothèques embarquées (notamment SDK d'analytics, de publicité ou de suivi) et domaines ou points de terminaison présents dans le code et les ressources. Ces listes nourrissent les vérifications préalables au déploiement et un contrôle de conformité au RGPD. Chaque trouvaille est accompagnée de sa localisation dans l'archive, ce qui permet de la vérifier.

REA n'isole rien lui-même : sa politique de sécurité précise qu'il n'est pas un sandbox et que l'analyse est déléguée au moteur local avec les droits de l'utilisateur. Une image Docker communautaire publiée le 18 octobre 2026 illustre une posture de confinement (lecture seule, aucune capacité Linux, jeton, réseau coupé en mode ligne de commande) ; l'article la présente comme un exemple, non comme une recommandation.

Les limites sont posées : la décompilation statique ne voit ni le code chiffré, ni le code chargé depuis le réseau, ni les bibliothèques natives, et l'obfuscation dégrade la lisibilité. Une liste de domaines dit ce que l'application peut contacter, pas ce qu'elle contacte ; il faut l'exécuter en émulateur isolé pour observer le trafic. Côté droit, l'autorisation d'inspecter un artefact n'emporte pas celle de le décompiler ou d'intercepter ses échanges ; l'article renvoie au juriste et au cadre européen.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | REA et Android : auditer une APK | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | JADX | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Apktool | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | jadx-headless-mcp | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.85 | DYNAMIQUE | inféré |
| REA | TECHNOLOGIE | s_applique_à | audit d'application mobile | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| audit d'application mobile | METHODOLOGIE | utilise | analyse statique | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| audit d'application mobile | METHODOLOGIE | s_applique_à | conformité RGPD | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |
| SECURITY.md de REA | DOCUMENT | affirme_que | REA n'est pas un sandbox et délègue l'analyse au moteur local avec les droits de l'utilisateur | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| docker-reverse-engineer-anything | TECHNOLOGIE | utilise | jadx-headless-mcp | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| docker-reverse-engineer-anything | TECHNOLOGIE | utilise | Docker | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | une liste de domaines tirée du code dit ce que l'application peut contacter, pas ce qu'elle contacte | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | vérifier l'empreinte SHA-256 du jar jadx-headless-mcp avant usage | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | exécuter l'APK en émulateur isolé pour observer le trafic réel | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| obfuscation | CONCEPT | réduit | lisibilité du code décompilé | CONCEPT | 0.8 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea) | AJOUT |
| JADX | TECHNOLOGIE | catégorie | décompilateur Android (DEX vers Java), utilisé en mode headless | AJOUT |
| Apktool | TECHNOLOGIE | catégorie | décodage des ressources et du manifeste d'une APK | AJOUT |
| jadx-headless-mcp | TECHNOLOGIE | version | 0.7.1, empreinte SHA-256 épinglée par REA, JDK 17+ | AJOUT |
| docker-reverse-engineer-anything | TECHNOLOGIE | origine | image communautaire non officielle de psyb0t, 18 octobre 2026 | AJOUT |
| audit d'application mobile | METHODOLOGIE | contenu | permissions, SDK embarqués, domaines et endpoints | AJOUT |
