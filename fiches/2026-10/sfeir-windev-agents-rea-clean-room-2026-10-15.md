---
themes: [architecture-construction, qualite-securite, politique-regulation]
source: SFEIR
---
# sfeir-windev-agents-rea-clean-room-2026-10-15

## Veille

Article **SFEIR AI** publié sur sfeir.com le **15 octobre 2026** (~5 500 signes, quatre sources), à la jonction de deux séries du cabinet : la migration **WinDev** et l'outil de rétro-ingénierie par agents **REA** (morluto/rea). Il traite le cas d'une application WinDev dont le **projet source a disparu** (prestataire parti avec les sources, poste effacé) et dont il ne reste que l'exécutable, la base **HFSQL** et les utilisateurs. L'article précise d'emblée qu'il ne constitue pas un conseil juridique. Trois apports. **(A)** Un état des lieux : au 15 octobre 2026, ni le README ni la documentation de REA ne citent WinDev parmi les cibles, et aucun retour public n'existe sur un exécutable WinDev ; on procède donc *« par preuve de concept »*, la base HFSQL restant *« la pièce la plus riche »*. **(B)** La **séparation clean-room** appliquée à des agents : un agent qui lit le pseudocode puis écrit la nouvelle application fusionne les deux rôles ; la documentation de REA exige *« A separate account or container »*, la spécification étant le seul objet qui franchit la frontière. **(C)** La preuve d'équivalence par **golden master inversé** alimenté par l'exécutable d'origine, et le **confinement** de l'analyse. Complète [[sfeir-rea-sandbox-confinement-2026-10-13]].

## Titre Article

Moderniser une application WinDev avec des agents : REA et méthode clean-room

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/moderniser-windev-agents-rea-clean-room/

## Keywords

WinDev, WLangage, application sans code source, rétro-ingénierie, rétro-documentation, REA, morluto/rea, Hopper, Ghidra, IDA, pseudocode, HFSQL, clean-room, séparation analyse et réécriture, conteneur, compte système séparé, spécification, golden master inversé, confinement, binaire non fiable, droits patrimoniaux, cession de droits, article L131-3 CPI, décompilation, CJUE Top System C-13/20, preuve de concept, Software Factory 10x

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article de cadrage pour DSI confrontées à un patrimoine WinDev sans sources, mêlant technique (rétro-ingénierie, isolation) et points juridiques. Français prudent, phrases courtes, FAQ finale.

**Style** : ouverture sur une citation de la documentation de REA, puis distinction nette entre deux situations (projet disponible : REA inutile ; projet perdu : objet de l'article). Les consignes de sécurité et de séparation sont citées en anglais depuis la documentation de l'outil, puis traduites en dispositif concret (un compte ou un conteneur par rôle).

**Position épistémique** : le texte marque systématiquement ce qui n'est pas connu (*« aucune source publique ne le dit »*, *« Toute promesse de résultat serait une invention »*) et date ses constats au 15 octobre 2026. L'avertissement juridique est posé en tête et répété dans la FAQ (renvoi au juriste). Les références juridiques (article L131-3 du CPI, arrêt CJUE Top System) sont citées avec leurs conditions.

## Pense-betes

- **Deux situations** : projet WinDev disponible → pas besoin de REA (export texte depuis la version 25, extraction des règles par IA) ; projet perdu → exécutable + base HFSQL + utilisateurs.
- **État des connaissances au 15 octobre 2026** : WinDev absent des cibles documentées de REA ; aucun retour public de rétro-ingénierie par agents sur un exécutable WinDev ; mode de compilation de l'atelier non documenté dans les sources.
- **Ce que REA fait** : pilote Hopper, Ghidra ou IDA ; renvoie pseudocode, assembleur, chaînes, symboles, références et limites.
- **Sources de règles sans décompiler** : écrans et données recoupés ; schéma HFSQL, contraintes implicites, valeurs réelles.
- **Livrable** : spécification relue par les utilisateurs + liste des zones non éclairées.
- **Clean-room par agents** : restreindre REA à un profil d'agent ne suffit pas (shell, fichiers, réseau restent accessibles, lancement par `npx`) → compte ou conteneur séparé pour l'analyse et pour la réécriture ; la spécification versionnée est le seul objet qui passe.
- **Propriété** : une application écrite par un prestataire n'appartient au client que si les droits ont été cédés par écrit (art. L131-3 CPI). La séparation garde un intérêt : elle force à écrire la spécification, qui nourrit les tests.
- **Décompilation** : CJUE Top System (C-13/20, 6 octobre 2021) — autorisée pour l'acquéreur légitime dans la mesure nécessaire à la correction d'erreurs, sous conditions contractuelles.
- **Équivalence** : golden master inversé (le LLM propose les entrées, l'exécutable d'origine fournit les sorties), bugs historiques compris jusqu'à décision métier.
- **Confinement** : REA analyse *« with that user's permissions »* → poste dédié pour un binaire interne, VM ou conteneur jetable pour un binaire incertain.
- **À relier** : [[sfeir-migration-windev-software-factory-10x-2026-10-15]].

## RésuméDe400mots

L'article de SFEIR traite d'un cas particulier de modernisation : l'application WinDev dont le projet source a disparu, parce qu'un prestataire est parti avec les sources, qu'un poste a été effacé ou que le projet est resté sur une version introuvable. Il ne reste alors que l'exécutable déployé, la base HFSQL et les utilisateurs. Le texte précise qu'il ne constitue pas un conseil juridique.

Lorsque le projet existe, l'outil de rétro-ingénierie REA n'est pas nécessaire : depuis sa version 25, l'atelier WinDev exporte le code en texte lisible, et le WLangage reste la meilleure source de vérité. Dans le cas contraire, la matière publique est mince : au 15 octobre 2026, REA ne cite pas WinDev parmi ses cibles et aucun retour de rétro-ingénierie par agents sur un exécutable WinDev n'a été publié. L'article recommande donc une preuve de concept sur un périmètre limité.

REA pilote des décompilateurs (Hopper, Ghidra, IDA) et renvoie pseudocode, chaînes et symboles, mais ce qu'ils tirent d'un exécutable WinDev reste à établir. Les écrans et les données permettent déjà de reconstituer une partie des règles ; la base HFSQL, avec son schéma, ses contraintes implicites et ses valeurs réelles, est la source la plus riche. Le livrable est une spécification relue par les utilisateurs, accompagnée de la liste des zones non éclairées.

Le texte applique ensuite la méthode clean-room aux agents : une équipe analyse et rédige une spécification sans code protégé, une autre réimplémente à partir de cette seule spécification. Si un même agent fait les deux, la barrière disparaît. La documentation de REA précise que limiter l'outil à un profil d'agent ne suffit pas et qu'un compte ou un conteneur distinct doit faire respecter la séparation. Pour sa propre application, la question de la contrefaçon se pose moins, à condition d'en détenir les droits patrimoniaux par une cession écrite ; la séparation conserve l'intérêt de forcer l'écriture de la spécification.

L'équivalence fonctionnelle se prouve grâce à l'exécutable d'origine, qui fournit les sorties de référence d'un golden master inversé ; la réécriture doit les reproduire, y compris les bugs historiques, jusqu'à décision du métier. Enfin, REA n'isolant pas l'analyse, tout binaire d'origine incertaine doit être ouvert dans une machine virtuelle ou un conteneur jetable. La FAQ aborde la récupération du source, la décompilation au regard de l'arrêt Top System de la CJUE et la sécurisation de la réécriture.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Moderniser une application WinDev avec des agents : REA et méthode clean-room | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Hopper | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | IDA | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | au 15 octobre 2026, REA ne documente pas WinDev parmi ses cibles | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | s_applique_à | WinDev | TECHNOLOGIE | 0.72 | DYNAMIQUE | inféré |
| clean-room | METHODOLOGIE | s_applique_à | rétro-ingénierie par agents | METHODOLOGIE | 0.9 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | recommande | un compte ou un conteneur séparé pour l'environnement de réimplémentation | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un même agent qui analyse puis réécrit fait disparaître la barrière clean-room | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | procéder par preuve de concept sur un périmètre fonctionnel limité | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| golden master | METHODOLOGIE | permet | prouver l'équivalence fonctionnelle à partir de l'exécutable d'origine | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| HFSQL | TECHNOLOGIE | permet | reconstitution des règles métier par le schéma et les valeurs réelles | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| arrêt CJUE Top System | DOCUMENT | affirme_que | l'acquéreur légitime peut décompiler dans la mesure nécessaire à la correction d'erreurs | AFFIRMATION | 0.86 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | vérifier la cession écrite des droits patrimoniaux (art. L131-3 CPI) avant de réécrire | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | ouvrir tout binaire d'origine incertaine en machine virtuelle ou conteneur jetable | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle, éditeur de sfeir.com | AJOUT |
| REA | TECHNOLOGIE | catégorie | outil open source de rétro-ingénierie par agents (morluto/rea) | AJOUT |
| WinDev | TECHNOLOGIE | cas traité | Application sans projet source : exécutable + base HFSQL | AJOUT |
| HFSQL | TECHNOLOGIE | rôle | Source la plus riche pour rétro-documenter les règles métier | AJOUT |
| clean-room | METHODOLOGIE | principe | Analyse et réimplémentation séparées, la spécification seule franchit la frontière | AJOUT |
| golden master | METHODOLOGIE | variante | Inversé : le LLM propose les entrées, l'exécutable d'origine fournit les sorties | AJOUT |
| arrêt CJUE Top System | DOCUMENT | référence | C-13/20, 6 octobre 2021, décompilation pour correction d'erreurs | AJOUT |
