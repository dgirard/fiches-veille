---
themes: [outils-plateformes, architecture-construction]
source: SFEIR
---
# sfeir-retro-ingenierie-vb6-2026-10-18

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **18 octobre 2026** (~900 mots, quatre sources), fiche du cluster SFEIR sur le legacy sans code source, consacrée aux applications **Visual Basic 6**. Le titre annonce la couleur : *« peu de retours, un workflow possible »*. Point de départ : l'issue #4627 ouverte le 17 octobre sur le dépôt de **REA** pour demander la prise en charge de Visual Basic 3 (un programme d'astrologie des années 1990 au source perdu). Trois apports. **(A)** L'état de la couverture : au 18 octobre, REA ne cite ni VB5 ni VB6 ; il peut confier un exécutable VB6 (PE 32 bits) à **Ghidra** sans rien savoir des formulaires, contrôles ActiveX ou procédures événementielles, et SFEIR écrit n'avoir *« trouvé aucun retour public de rétro-ingénierie par agents sur une application VB6 »*. **(B)** La question préalable, **P-Code ou natif** : le P-Code garde des instructions de haut niveau, le natif ne laisse que du code machine ; **VB Decompiler** (DotFix Software) revendique près de **85 %** de code récupéré dans les deux cas, chiffre d'éditeur à prendre *« comme un ordre de grandeur »*. **(C)** Un workflow où le décompilateur spécialisé reste la référence et l'agent relit en masse, rapproche procédures et écrans, propose des règles et liste ce qu'il n'a pas compris. Texte parallèle à la fiche SFEIR sur Delphi.

## Titre Article

Rétro-ingénierie d'applications VB6 : peu de retours, un workflow possible

## Date

2026-10-18

## URL

https://www.sfeir.com/articles/retro-ingenierie-vb6/

## Keywords

Visual Basic 6, VB6, VB5, Visual Basic 3, P-Code, code natif x86, VBRUN300.DLL, format NE, exécutable 16 bits, PE 32 bits, rétro-ingénierie, décompilation, VB Decompiler, DotFix Software, ghidra-vb3, PyGhidra, Ghidra, REA, issue #4627, formulaires, contrôles ActiveX, procédures événementielles, rétro-documentation, legacy sans code source, golden master, bascule par briques, Software Factory

## Authors

SFEIR AI (voix éditoriale du cabinet), article non signé individuellement — sfeir.com, site éditorial de SFEIR.

## Ton

Profil : fiche technique d'une ESN, en français, adressée aux DSI qui maintiennent des applications VB6 sans source. Le registre est celui d'un état des lieux honnête sur un terrain peu documenté : le titre et le corps disent ce qui manque (aucun outillage dédié côté agents, aucun retour public trouvé, une proposition ouverte et non intégrée). Les chiffres d'éditeur sont rapportés avec leur provenance et ramenés à un ordre de grandeur. Le texte hiérarchise clairement les outils : le décompilateur spécialisé d'abord, l'agent ensuite pour la relecture et la synthèse. Le workflow se formule en impératifs ; la FAQ répond sans promesse (« jamais le projet d'origine à l'identique ») et renvoie le choix de la cible après la rétro-documentation. Conclusion sur l'offre Software Factory.

## Pense-betes

- **Issue REA #4627** (17 octobre 2026) : prise en charge de **VB3** ; REA rejette les exécutables Windows **16 bits (NE)** et n'analyse pas le p-code VB3 interprété par **VBRUN300.DLL** — un désassembleur natif *ne montre que l'interpréteur*. Proposition : inspection NE + branchement de **ghidra-vb3** (script PyGhidra, mai 2026). Non intégré.
- **VB6 dans REA** : absent du README au 18 octobre 2026. Exécutable VB6 = PE 32 bits → Ghidra possible, sans connaissance des formulaires, contrôles ActiveX, procédures événementielles.
- **Aucun retour public** de rétro-ingénierie par agents sur du VB6 trouvé par SFEIR.
- **P-Code vs natif** : P-Code = bytecode exécuté par la VM de la bibliothèque d'exécution, instructions de haut niveau plus faciles à remonter ; natif x86 = code machine + appels au runtime.
- **VB Decompiler** (DotFix Software) : VB5/VB6, P-Code et natif ; revendique **~85 %** du code récupéré (P-Code typique) et **jusqu'à 85 %** en natif ; reste = analyse et correction humaines. Chiffre éditeur.
- **Hiérarchie** : décompilateur qui connaît le format VB (formulaires, contrôles, tables d'objets) > décompilateur générique piloté par agent. Rôle de l'agent : relecture en masse, procédures ↔ écrans, règles métier, liste des incompris.
- **Workflow** : identifier le mode de compilation de chaque exécutable/composant → P-Code : décompilateur spécialisé puis agent ; natif : décompilateur spécialisé + Ghidra via REA (trace des preuves) → lecture disciplinée (règle inférée ≠ règle lue) → analyse des fichiers de données → réécriture : règles relues par les utilisateurs, **golden master** alimenté par l'exécutable d'origine, bascule par briques.
- Livrable utile = **une spécification**, pas le projet d'origine à l'identique. Cible choisie après la rétro-documentation.

## RésuméDe400mots

Cet article de SFEIR, publié le 18 octobre 2026, fait le point sur la rétro-ingénierie des applications Visual Basic 6 dont le code source a disparu, et sur ce que les agents y apportent. Il part d'une demande déposée la veille sur le dépôt de l'outil REA : la prise en charge de Visual Basic 3, pour retrouver la logique d'un programme des années 1990. Pour SFEIR, cette demande révèle un angle mort : les applications Visual Basic encore en production n'ont pas d'outillage dédié côté agents.

Au 18 octobre 2026, REA ne mentionne ni VB5 ni VB6 parmi ses cibles. La demande sur VB3 concerne une génération plus ancienne, en exécutables 16 bits que REA rejette, et dont le code est interprété par une bibliothèque d'exécution : un désassembleur natif ne montre alors que l'interpréteur. Un exécutable VB6 est un binaire Windows 32 bits que REA peut confier à Ghidra, mais sans rien comprendre des formulaires, des contrôles ActiveX ou des procédures événementielles. SFEIR indique n'avoir trouvé aucun retour public de rétro-ingénierie par agents sur une application VB6.

La première question à poser est le mode de compilation. Visual Basic 6 compile soit en P-Code, un bytecode qui conserve des instructions de haut niveau, soit en code natif x86, qui ne laisse que du code machine. Les deux se décompilent en partie : l'éditeur de VB Decompiler revendique la récupération de près de 85 % du code dans les deux cas, chiffre que l'article invite à lire comme un ordre de grandeur.

Sur VB6, un décompilateur qui connaît le format des projets Visual Basic fait mieux qu'un décompilateur générique piloté par un agent. L'agent garde un rôle de relecture en masse : rapprocher les procédures des écrans, proposer des règles métier, lister ce qu'il n'a pas compris.

Le workflow proposé commence par l'identification du mode de compilation de chaque exécutable. En P-Code, la sortie d'un décompilateur spécialisé est confiée à l'agent ; en natif, on combine ce décompilateur et Ghidra, piloté via REA pour garder une trace des preuves. La sortie se lit en distinguant règle inférée et règle lue, les fichiers de données sont analysés à part, puis la réécriture suit : règles relues par les utilisateurs, golden master alimenté par l'exécutable d'origine, bascule par briques. Le livrable utile reste une spécification, et le choix de la cible vient après.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Rétro-ingénierie d'applications VB6 : peu de retours, un workflow possible | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | REA ne cite ni VB5 ni VB6 parmi ses cibles documentées au 18 octobre 2026 | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | aucun retour public de rétro-ingénierie par agents sur une application VB6 n'a été trouvé | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| Visual Basic 6 | TECHNOLOGIE | utilise | P-Code | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| VB Decompiler | TECHNOLOGIE | s_applique_à | Visual Basic 6 | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| DotFix Software | ORGANISATION | a_créé | VB Decompiler | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| DotFix Software | ORGANISATION | mesure | près de 85 % du code récupéré en P-Code comme en natif (revendication éditeur) | MESURE | 0.78 | DYNAMIQUE | déclaré_article |
| VB Decompiler | TECHNOLOGIE | surpasse | décompilateur générique piloté par un agent sur VB6 | CONCEPT | 0.8 | DYNAMIQUE | déclaré_article |
| ghidra-vb3 | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| ghidra-vb3 | TECHNOLOGIE | s_applique_à | Visual Basic 3 | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | identifier le mode de compilation (P-Code ou natif) de chaque exécutable avant toute estimation | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | s_applique_à | Visual Basic 6 | TECHNOLOGIE | 0.86 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | utilise | golden master | METHODOLOGIE | 0.8 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | choisir la cible de migration après la rétro-documentation, pas avant | AFFIRMATION | 0.84 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Visual Basic 6 | TECHNOLOGIE | catégorie | Environnement Microsoft compilant en P-Code ou en code natif x86 | AJOUT |
| P-Code | CONCEPT | définition | Bytecode VB exécuté par la machine virtuelle de la bibliothèque d'exécution | AJOUT |
| VB Decompiler | TECHNOLOGIE | catégorie | Décompilateur spécialisé VB5/VB6, P-Code et natif (DotFix Software) | AJOUT |
| DotFix Software | ORGANISATION | rôle | Éditeur de VB Decompiler | AJOUT |
| ghidra-vb3 | TECHNOLOGIE | catégorie | Script PyGhidra de désassemblage du p-code Visual Basic 3 (mai 2026) | AJOUT |
| REA | TECHNOLOGIE | catégorie | Serveur MCP de rétro-ingénierie (Reverse Engineer Anything) | AJOUT |
| rétro-documentation | METHODOLOGIE | définition | Reconstitution de la documentation d'une application à partir de ses binaires | AJOUT |
