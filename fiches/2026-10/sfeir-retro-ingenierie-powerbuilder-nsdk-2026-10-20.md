---
themes: [architecture-construction, transformation-adoption]
source: SFEIR
---
# sfeir-retro-ingenierie-powerbuilder-nsdk-2026-10-20

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **20 octobre 2026** (~1 000 mots, quatre sources : annonce SAP-Appeon de 2016, note SAP 2624265, README de **REA**, site de **Nat System**). Il dresse un état des lieux de la rétro-ingénierie par agents sur deux ateliers de développement encore en production dans des applications de gestion : **PowerBuilder** et **NS-DK**. **(1) PowerBuilder** : depuis l'accord du 5 juillet 2016, **Appeon** en assure développement et support ; une note SAP de mars 2018 indique qu'Appeon ne maintient pas SAP PowerBuilder **12.6** et antérieures ; compilation en p-code ou en code machine ; outils tiers de décompilation du p-code *« sans maintenance claire »* ; REA ne cite pas PowerBuilder et ne verrait, via Ghidra, qu'un pseudocode sans le modèle d'objets (DataWindows, scripts d'événements). **(2) NS-DK et NatStar** : éditeur français toujours actif, offre de TMA ; aucun décompilateur public trouvé. **(3) Voie réaliste** : partir du comportement, des données et du golden master. L'article le dit sans détour : *« Nous n'avons trouvé, au 20 octobre 2026, aucun retour public de rétro-ingénierie par agents sur PowerBuilder ou NS-DK »*. Fait partie de la série SFEIR d'octobre 2026 sur la rétro-ingénierie par agents.

## Titre Article

PowerBuilder et NSDK : état des lieux de la rétro-ingénierie par agents

## Date

2026-10-20

## URL

https://www.sfeir.com/articles/retro-ingenierie-powerbuilder-nsdk/

## Keywords

PowerBuilder, Appeon, SAP, PowerBuilder 12.6, p-code, code machine, PBD, DataWindow, NS-DK, NSDK, NatStar, Nat System, Nat-Bot, NatJet, tierce maintenance applicative, rétro-ingénierie par agents, REA, Ghidra, décompilation, modernisation legacy, golden master, rétro-documentation, réécriture par briques, Software Factory, état des lieux

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

État des lieux en français, à destination des DSI qui exploitent des applications PowerBuilder ou NS-DK. Le registre est celui de l'**inventaire honnête** : l'article sépare ce qu'on sait, ce qui existe et ce qui manque, et consacre une section à *« Ce que nous ne savons pas »*. Il refuse explicitement de reprendre des chiffres non vérifiés à la source (offres de migration) et annonce une mise à jour si un retour vérifiable paraît. Les faits datés (accord SAP-Appeon, note SAP de 2018, site de Nat System consulté le 20 octobre 2026) sont sourcés. La recommandation est sobre : ne pas compter sur une décompilation par agent, partir de l'éditeur vivant quand il existe, puis du comportement et des données. FAQ et renvoi à la Software Factory de SFEIR en conclusion.

## Pense-betes

- **Accord SAP-Appeon, 5 juillet 2016** : Appeon prend en charge développement, vente et support de PowerBuilder.
- **Note SAP 2624265 (27 mars 2018)** : depuis juin 2017, Appeon distribue Appeon PowerBuilder 2017 ; Appeon *« cannot offer maintenance »* pour SAP PowerBuilder **12.6** et antérieures ; passage à Appeon = nouveau contrat → un parc en 12.6 ou avant n'a plus de support éditeur.
- **Compilation PowerBuilder** : **p-code** (interprété, garde une structure de haut niveau) ou **code machine** ; livraison en exécutable et bibliothèques PBD ou DLL ; distinction comparable à Visual Basic.
- **Décompilation** : outils tiers pour le p-code, sans maintenance claire ; aucun décompilateur publié par Appeon ; **REA ne cite pas PowerBuilder** ; via Ghidra, pseudocode générique sans modèle d'objets (fenêtres, DataWindows, scripts d'événements).
- **NS-DK / NatStar** (Nat System, éditeur français) : produits toujours présentés au 20 octobre 2026, avec Nat-Bot et NatJet ; offre de TMA pour *« pérenniser »* NatStar, Java et NS-DK ; formations. **L'éditeur est le premier interlocuteur.** Aucun décompilateur public, pas cité par REA.
- **Voie réaliste** : comportement et données ; écrans et cas limites décrits par les utilisateurs ; schéma et règles implicites de la base ; fichiers d'échange rétro-documentés ; **golden master** sur l'application qui tourne ; réécriture brique par brique.
- **Source partiel** : un agent lit des scripts exportés bien mieux qu'un binaire → partir du source, même incomplet.
- **Constat assumé** : aucun retour public de rétro-ingénierie par agents sur ces deux stacks au 20 octobre 2026 ; *« Une affirmation contraire mériterait sa source »*.

## RésuméDe400mots

L'article fait le point sur la rétro-ingénierie par agents appliquée à deux ateliers de développement qui font encore tourner des applications de gestion critiques : PowerBuilder et NS-DK. Son constat principal est un manque : au 20 octobre 2026, SFEIR n'a trouvé aucun retour public sur le sujet, et l'outil REA ne cite aucune de ces deux technologies parmi ses cibles.

Pour PowerBuilder, l'article rappelle l'accord du 5 juillet 2016 par lequel SAP confie à Appeon le développement, la vente et le support du produit. Une note SAP de mars 2018 précise que, depuis juin 2017, Appeon distribue une nouvelle génération du produit et ne peut assurer la maintenance de SAP PowerBuilder 12.6 et des versions antérieures ; passer à Appeon suppose un nouveau contrat. Un parc resté en 12.6 n'a donc plus de support éditeur. Techniquement, PowerBuilder compile soit en p-code interprété, qui conserve une structure de haut niveau, soit en code machine, livré en exécutable et bibliothèques PBD ou DLL. Des outils tiers existent pour décompiler le p-code, sans maintenance claire, et Appeon ne publie pas de décompilateur. Sur un build en code machine, REA peut confier le binaire à Ghidra, mais sans connaissance du modèle d'objets PowerBuilder (fenêtres, DataWindows, scripts d'événements), ce qui donne un pseudocode difficile à lire.

Pour NS-DK et NatStar, ateliers de l'éditeur français Nat System, la matière est encore plus mince. L'éditeur est vivant : son site présente toujours les deux produits et propose une offre de tierce maintenance applicative et des formations. L'article en conclut que l'éditeur reste le premier interlocuteur. Aucun décompilateur public n'a été trouvé, et l'article ne reprend aucun chiffre d'offre de migration qu'il n'a pas pu vérifier.

Pour une DSI, la recommandation est de ne pas compter sur une décompilation par agent et de partir du comportement et des données : description des écrans et cas limites par les utilisateurs, schéma et règles implicites de la base, rétro-documentation des fichiers d'échange, golden master produit par l'application d'origine tant qu'elle tourne, et réécriture brique par brique. Si un source PowerBuilder ou NS-DK subsiste, même incomplet, il vaut mieux partir de lui. Tout binaire analysé avec REA doit être confiné, et le cadre juridique de la décompilation validé. L'article annonce une mise à jour si un retour vérifiable paraît ou si REA ajoute ces cibles.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | PowerBuilder et NSDK : état des lieux de la rétro-ingénierie par agents | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Appeon | ORGANISATION | collabore_avec | SAP | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Appeon | ORGANISATION | publie | PowerBuilder | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| note SAP 2624265 | DOCUMENT | affirme_que | Appeon ne maintient pas SAP PowerBuilder 12.6 et antérieures | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Nat System | ORGANISATION | a_créé | NS-DK | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Nat System | ORGANISATION | a_créé | NatStar | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | aucun retour public de rétro-ingénierie par agents sur PowerBuilder ou NS-DK au 20 octobre 2026 | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le pseudocode Ghidra d'un build PowerBuilder ignore le modèle d'objets (DataWindows, scripts d'événements) | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | partir du comportement et des données plutôt que d'une décompilation par agent | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | consulter d'abord l'éditeur Nat System, toujours actif | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| golden master | METHODOLOGIE | s_applique_à | PowerBuilder | TECHNOLOGIE | 0.8 | ATEMPOREL | déclaré_article |
| rétro-documentation | METHODOLOGIE | s_applique_à | NS-DK | TECHNOLOGIE | 0.8 | ATEMPOREL | déclaré_article |
| p-code | CONCEPT | permet | conservation d'une structure de haut niveau dans le binaire | CONCEPT | 0.82 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| PowerBuilder | TECHNOLOGIE | statut | développé et supporté par Appeon depuis 2016 ; 12.6 et antérieures sans maintenance éditeur | AJOUT |
| Appeon | ORGANISATION | rôle | reprend développement, vente et support de PowerBuilder (accord SAP du 5 juillet 2016) | AJOUT |
| NS-DK | TECHNOLOGIE | catégorie | atelier de développement de Nat System, aucun décompilateur public connu | AJOUT |
| NatStar | TECHNOLOGIE | catégorie | atelier de développement de Nat System | AJOUT |
| Nat System | ORGANISATION | secteur | éditeur français, offre de TMA NatStar, Java et NS-DK | AJOUT |
| note SAP 2624265 | DOCUMENT | date | 27 mars 2018, migration vers Appeon PowerBuilder 2017 | AJOUT |
| p-code | CONCEPT | définition | code intermédiaire interprété par le moteur d'exécution, distinct du code machine | AJOUT |
