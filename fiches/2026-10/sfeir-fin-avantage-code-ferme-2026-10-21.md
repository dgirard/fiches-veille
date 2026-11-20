---
themes: [qualite-securite, economie-marche, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-fin-avantage-code-ferme-2026-10-21

## Veille

Tribune **SFEIR AI** publiée sur sfeir.com le **21 octobre 2026** (~6 000 signes, quatre sections, FAQ, trois sources notées). Elle part de deux projets d'octobre 2026 : **REA** (*Reverse Engineer Anything*), dont le dépôt GitHub comptait **76 998** étoiles le 11 octobre (+**25 793** en une journée) puis ~**348 000** neuf jours plus tard, et **ArtCraft**, qui publie des réécritures en Rust de Photoshop, Premiere, Lightroom, Word, Excel et PowerPoint. Trois apports. **(A)** REA ne décompile rien lui-même : il branche un agent de code sur **Ghidra**, Hopper, IDA, JADX ; **Connor Turland** a reconstitué en une dizaine de minutes une logique de **Slack 4.52.171** — *« how much curiosity costs »*. **(B)** Ce qui ne protège plus : le secret de la logique côté client (minification, Electron, compilation native). Ce qui protège encore : données, utilisateurs, serveur, distribution, marque, vitesse d'exécution ; le droit d'auteur ne protège pas la fonctionnalité (arrêt **SAS Institute**, 2012). **(C)** Recommandations aux éditeurs : déplacer la valeur côté serveur, traiter le client comme du code public, jetons courts et révocables. Rejoint les fiches du corpus sur la sécurité des agents de code et l'économie du logiciel à l'ère agentique.

## Titre Article

REA, ArtCraft et la fin de l'avantage du code fermé

## Date

2026-10-21

## URL

https://www.sfeir.com/articles/fin-avantage-code-ferme/

## Keywords

rétro-ingénierie, REA, Reverse Engineer Anything, ArtCraft, clean-room, code fermé, logiciel propriétaire, moat logiciel, Ghidra, décompilation, Electron, ASAR, minification, obfuscation, logique côté serveur, droit d'auteur, SAS Institute, éditeurs de logiciels, agents de code, Rust, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Tribune à la première personne du pluriel (« nous pensons », « nous recommandons »), registre de conseil adressé aux éditeurs de logiciels et aux DSI. Le texte procède par constat daté et chiffré (étoiles GitHub, versions, délais), puis par une bipartition nette : « ce qui ne protège plus » / « ce qui protège toujours ». Il présente le renversement comme une bonne nouvelle « pour qui sait où se trouve sa valeur », sans dramatisation. Les limites des outils sont signalées (REA a manqué deux scripts de préchargement, sorties lourdes en contexte) et les revendications non auditées d'ArtCraft sont qualifiées comme telles. Les références juridiques sont posées avec prudence (« sous réserve de l'avis de votre juriste »). Le texte renvoie abondamment à d'autres pages SFEIR (hubs sécurité, legacy, clean-room) et se clôt sur l'offre AI Cyber. Public : éditeurs, RSSI, DSI portant des applications sans code source.

## Pense-betes

- **REA** (*Reverse Engineer Anything*) : **76 998** étoiles GitHub au 11 octobre 2026 (+**25 793** en un jour), ~**348 000** au 20 octobre selon Connor Turland.
- REA **orchestre** des moteurs existants (**Ghidra**, Hopper, IDA, JADX) + analyseurs JavaScript et .NET maison ; chaque conclusion revient **avec preuves et limites**.
- Test Turland sur **Slack 4.52.171** : ~10 min pour reconstituer la logique d'alerte Ne pas déranger (garde 2 s, cache 5 s derrière feature flag, liste d'avertissements en cache 1 h). Formule : ce qui change, c'est *« how much curiosity costs »*.
- **ArtCraft** : réécritures Rust de Photoshop (PhotoCraft, « clean-room » écrite avec Claude), Premiere, Lightroom, Word, Excel, PowerPoint. Revendication **non auditée**.
- Test **Ishank Choudhary** (Electron minifié) : REA restitue l'expression réelle d'un nom de canal dynamique ; mais manque **deux scripts de préchargement** et ses sorties pèsent lourd dans le contexte.
- **Ne protège plus** : secret de la logique côté client (règle de calcul, heuristique, clé embarquée → « considérez-la comme exposée »).
- **Protège toujours** : données, utilisateurs, serveur, distribution, marque, vitesse d'exécution — le savoir organisationnel derrière un paramètre ne se lit pas dans le binaire.
- Droit : le droit d'auteur protège code et ressources, **pas la fonctionnalité** (CJUE, **SAS Institute**, 2012) ; brevet, secret des affaires, contrat peuvent jouer ; en France certaines clauses anti-rétro-ingénierie sont nulles.
- **Recommandations** : logique sensible et secrets côté serveur ; client = code public ; **jetons courts, révocables** ; investir données / relation / rythme de livraison ; auditer son produit « avec les yeux d'un agent ».
- Effet miroir : équipes sécurité (analyste infatigable sur leurs binaires) et DSI à applications sans code source (rétro-documentation abordable).

## RésuméDe400mots

Cette tribune de SFEIR, publiée le 21 octobre 2026, tire les conséquences de deux projets apparus en octobre 2026 pour les éditeurs de logiciels. Le premier, **REA** (*Reverse Engineer Anything*), a connu une croissance fulgurante sur GitHub : 76 998 étoiles le 11 octobre après un gain de 25 793 en une journée, puis environ 348 000 neuf jours plus tard selon Connor Turland. Le second, **ArtCraft**, a publié des réécritures en Rust de Photoshop, Premiere et Lightroom, puis de Word, Excel et PowerPoint. Pour SFEIR, les deux disent la même chose : le code installé sur le poste du client est devenu lisible par n'importe quel agent.

REA ne décompile rien lui-même. Il branche un agent de code sur des moteurs établis (Ghidra, Hopper, IDA, JADX) et sur ses propres analyseurs JavaScript et .NET, et renvoie chaque conclusion avec ses preuves et ses limites. Le saut porte sur le coût : Connor Turland a reconstitué en une dizaine de minutes la logique d'alerte Ne pas déranger de Slack 4.52.171, jusqu'aux délais de garde et de cache. ArtCraft illustre l'étape suivante, de la compréhension à la réécriture ; sa revendication clean-room n'est pas auditée, mais une fonctionnalité visible se réimplémente désormais en quelques semaines. Un article de 404 Media décrit plus largement des téléviseurs débarrassés de leur publicité et des objets abandonnés remis en service.

Ce qui ne protège plus, selon l'article, c'est le secret de la logique côté client : minification, empaquetage Electron et compilation native ralentissaient un humain, pas un agent. Un test sur une application Electron minifiée montre REA restituant l'expression réelle d'un nom de canal construit dynamiquement. Les limites existent (deux scripts de préchargement manqués, sorties lourdes pour le contexte), mais elles reculent à chaque version et une stratégie produit ne peut pas parier dessus.

Ce qui protège toujours : les données, les utilisateurs, le serveur, la distribution, la marque et la vitesse d'exécution. Un agent lit qu'un cache dure une heure, pas l'incident qui a fixé ce délai. Sur le plan juridique, le droit d'auteur protège le code mais jamais la fonctionnalité, comme l'a jugé la Cour de justice dans l'arrêt SAS Institute de 2012 ; brevet, secret des affaires et contrat peuvent encore jouer.

SFEIR recommande donc de déplacer la valeur côté serveur (tarification, licences, heuristiques), de traiter le client comme du code public avec des jetons courts et révocables, d'investir dans la donnée, la relation et le rythme de livraison, et d'examiner son produit comme le ferait un agent tiers. Le même renversement profite aux équipes sécurité et aux DSI qui maintiennent des applications sans code source.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | REA, ArtCraft et la fin de l'avantage du code fermé | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | agents de code | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | permet | rétro-ingénierie par agents | METHODOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | mesure | 25 793 étoiles GitHub en une journée (76 998 au 11 octobre 2026) | MESURE | 0.92 | STATIQUE | déclaré_article |
| Connor Turland | PERSONNE | affirme_que | REA a reconstitué en ~10 minutes la logique d'alerte Ne pas déranger de Slack 4.52.171 | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| ArtCraft | ORGANISATION | a_créé | PhotoCraft | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| PhotoCraft | TECHNOLOGIE | utilise | Rust | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| PhotoCraft | TECHNOLOGIE | concurrence | Photoshop | TECHNOLOGIE | 0.8 | DYNAMIQUE | inféré |
| rétro-ingénierie par agents | METHODOLOGIE | réduit | protection par le secret de la logique côté client | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| arrêt SAS Institute | DOCUMENT | affirme_que | le droit d'auteur ne protège pas la fonctionnalité d'un programme | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | déplacer la logique sensible et les secrets côté serveur, traiter le client comme du code public | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | jetons courts obtenus à l'exécution et révocables | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | données, utilisateurs, serveur, distribution, marque et vitesse d'exécution protègent toujours un éditeur | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| clean-room | METHODOLOGIE | s_applique_à | réimplémentation de logiciels propriétaires | CONCEPT | 0.82 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| REA | TECHNOLOGIE | catégorie | Outil open source de rétro-ingénierie pilotée par agent (Reverse Engineer Anything) | AJOUT |
| ArtCraft | ORGANISATION | activité | Réécritures Rust d'applications Adobe et Microsoft Office | AJOUT |
| PhotoCraft | TECHNOLOGIE | catégorie | Réimplémentation revendiquée clean-room de Photoshop, écrite avec Claude | AJOUT |
| Connor Turland | PERSONNE | rôle | Auteur du test de REA sur Slack (atcyrus.com) | AJOUT |
| rétro-ingénierie par agents | METHODOLOGIE | définition | Agent de code pilotant des décompilateurs pour reconstituer la logique d'un binaire | AJOUT |
| arrêt SAS Institute | DOCUMENT | portée | CJUE 2012 : la fonctionnalité d'un programme n'est pas protégée par le droit d'auteur | AJOUT |
| clean-room | METHODOLOGIE | définition | Réimplémentation d'un comportement sans accès au code d'origine | AJOUT |
