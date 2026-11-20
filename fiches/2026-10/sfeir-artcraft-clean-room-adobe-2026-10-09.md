---
themes: [politique-regulation, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-artcraft-clean-room-adobe-2026-10-09

## Veille

Étude de cas **SFEIR AI** publiée sur sfeir.com le **9 octobre 2026** et mise à jour le **23 octobre** (~1 500 mots, sept sources), avec un avertissement : *« Ceci n'est pas un conseil juridique »*. Elle porte sur **ArtCraft**, organisation GitHub « storytold » attribuée par la presse à **Brandon Thomas**, qui publie depuis le **30 septembre 2026** des réécritures en **Rust** de la suite **Adobe** (PhotoCraft, FilmCraft, LightCraft…) écrites avec **Claude**, puis d'Excel, Pro Tools ou Figma. Trois apports. **(A)** Les faits : double licence MIT/Apache-2.0, applications en alpha, **71 629** étoiles sur PhotoCraft au 23 octobre ; promesse de parité ramenée à *« 99 % en quelques mois »*. **(B)** Ce que la revendication clean-room recouvre : format PSD écrit *« from Adobe's public specification »*, comparaison des rendus par un *« composite oracle »*, et l'arrêt **SAS Institute** (CJUE, **2012**) selon lequel fonctionnalité, langage et format de fichiers ne sont pas protégés. **(C)** Ce qui reste ouvert : aucune vérification indépendante (*« We also do not know whether the claimed 'clean-room process' stands up to scrutiny »*, Andres Guadamuz), une interface reprise à l'identique que la CJUE (**2010**) peut protéger, et la question non tranchée d'une salle blanche quand un modèle de langage écrit le code. Se lit avec les articles SFEIR des 11 et 12 octobre 2026 sur le clean-room et la décompilation.

## Titre Article

ArtCraft : des clones d'Adobe en clean-room revendiqué, ce que vaut l'argument

## Date

2026-10-09

## URL

https://www.sfeir.com/articles/artcraft-clean-room-adobe/

## Keywords

ArtCraft, storytold, PhotoCraft, Brandon Thomas, Adobe, Photoshop, réimplémentation clean-room, Rust, Claude Code, Claude Opus 5.5, rétro-ingénierie, droit d'auteur, CJUE, SAS Institute C-406/10, BSA C-393/09, interface graphique, trade dress, concurrence déloyale, parasitisme, spécification publique, composite oracle, séparation des rôles, traçabilité, open source

## Authors

SFEIR AI, voix éditoriale non signée — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : étude de cas juridique et technique publiée sur le site d'un cabinet, pour éditeurs de logiciels et DSI. Français sobre, encadré d'avertissement en ouverture (*« le conseil juridique n'est pas le métier de SFEIR »*), FAQ finale.

**Style** : quatre temps — faits vérifiables, ce que la revendication recouvre, ce qui reste ouvert, leçon pour un éditeur ou une DSI. Les faits sont datés et sourcés jusqu'au relevé de l'API GitHub ; les citations du README de PhotoCraft sont reproduites en anglais. Le texte distingue droit européen, droit américain (trade dress) et droit français (concurrence déloyale, parasitisme).

**Position épistémique** : l'article sépare ce qui est établi (dates, licences, étoiles, principe de l'arrêt SAS Institute) de ce qui repose sur le récit du développeur. Il relève le vocabulaire *« reverse engineer »* rapporté par Al Jazeera, signale que le soupçon de décompilation n'est établi par rien, et laisse la qualification au juge (*« Seul un juge pourrait trancher »*).

## Pense-betes

- **Chronologie storytold** : 30 septembre, cinq dépôts (PhotoCraft, FilmCraft, LightCraft, VectorCraft, PdfCraft) ; 1er octobre, DesignCraft et EffectCraft ; 7 octobre, GridCraft, DeckCraft, WordCraft, SoundCraft, CADCraft ; 9 octobre, FigCraft.
- **Auteur** : Brandon Thomas (Atlanta, ex-Storyteller.ai, ex-Square), motivé par les frais de résiliation d'Adobe. Code produit avec Claude Code et des agents, modèle Claude Opus 5.5 selon des relais.
- **Étoiles au 23 octobre** : PhotoCraft 71 629 ; PdfCraft 17 329 ; FilmCraft 15 832 ; WordCraft 15 641.
- **Définition clean-room** : une équipe décrit le comportement dans une spécification, une autre réécrit à partir de cette seule spécification sans voir le code d'origine.
- **Indices du README** : spécification publique du PSD, oracle de composition comparant les rendus à Photoshop → observation du comportement, pas lecture du code.
- **CJUE SAS Institute (C-406/10, 2 mai 2012)** : ni la fonctionnalité, ni le langage, ni le format des fichiers de données ne sont une forme d'expression protégée.
- **Interface** : *« If you know Photoshop, you already know PhotoCraft »* ; la CJUE (BSA, C-393/09, 2010) admet qu'une interface originale soit protégée par le droit d'auteur commun ; trade dress aux États-Unis ; parasitisme en France.
- **Question ouverte** : un modèle entraîné sur de vastes corpus a pu croiser des fragments protégés ; la séparation des rôles devient difficile à démontrer.
- **Leçon éditeur** : une fonctionnalité visible de l'extérieur se réimplémente en quelques semaines ; la protection du code reste, celle du comportement n'a jamais existé.
- **Leçon DSI** : spécification depuis le comportement observé, équipe de réécriture n'ayant jamais vu de code décompilé, journal de qui a vu quoi.
- **Statut** : aucune réaction publique d'Adobe trouvée, aucun audit indépendant au 23 octobre.

## RésuméDe400mots

Depuis le 30 septembre 2026, l'organisation GitHub storytold, qui signe ArtCraft, publie des réécritures en Rust d'applications Adobe : PhotoCraft pour Photoshop, FilmCraft, LightCraft, VectorCraft et PdfCraft, puis des équivalents d'Excel, de Pro Tools, d'outils de présentation, de CAO et de Figma. Le README de PhotoCraft se présente comme une réimplémentation clean-room open source, sous double licence MIT ou Apache-2.0. La presse attribue le projet à Brandon Thomas, ingénieur à Atlanta, qui dit avoir été motivé par les frais de résiliation d'Adobe. Le code a été écrit avec Claude et des agents. Les applications sont en alpha, mais PhotoCraft dépassait 71 000 étoiles le 23 octobre.

L'article de SFEIR, accompagné d'un avertissement selon lequel il ne constitue pas un conseil juridique, examine ce que vaut la revendication en droit européen. Une méthode clean-room sépare deux équipes : l'une décrit le comportement d'un logiciel, l'autre réécrit à partir de cette seule description. Le README donne deux indices compatibles avec cette démarche : le format PSD est implémenté à partir de la spécification publique d'Adobe, et un oracle compare les rendus de PhotoCraft à ceux de Photoshop. Or la Cour de justice de l'Union européenne a jugé en 2012, dans l'arrêt SAS Institute, que la fonctionnalité d'un programme, son langage et le format de ses fichiers ne sont pas protégés par le droit d'auteur. Si aucun code ni aucune ressource d'Adobe n'a été repris, la démarche s'appuie sur ce principe.

Plusieurs questions restent ouvertes. La revendication repose sur le récit du développeur, sans vérification indépendante ; le juriste Andres Guadamuz le souligne, et le développeur a lui-même employé le terme de rétro-ingénierie. L'interface, présentée comme identique à celle de Photoshop, peut être protégée si elle est originale, selon un arrêt de la CJUE de 2010, et une imitation trop proche peut relever du parasitisme en France ou du trade dress aux États-Unis. Enfin, personne n'a tranché ce que vaut une salle blanche quand un modèle de langage, entraîné sur de vastes corpus, écrit le code.

Pour un éditeur, l'article retient qu'une fonctionnalité visible de l'extérieur se réimplémente désormais en quelques semaines. Pour une DSI tentée de réécrire un outil tiers avec des agents, il recommande une spécification fondée sur le comportement observé, une équipe qui n'a jamais vu de code décompilé et un journal de qui a vu quoi.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | ArtCraft : des clones d'Adobe en clean-room revendiqué | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Brandon Thomas | PERSONNE | a_créé | ArtCraft | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| PhotoCraft | TECHNOLOGIE | fait_partie_de | ArtCraft | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| PhotoCraft | TECHNOLOGIE | concurrence | Adobe Photoshop | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| ArtCraft | TECHNOLOGIE | utilise | Rust | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| ArtCraft | TECHNOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| ArtCraft | TECHNOLOGIE | utilise | réimplémentation clean-room | METHODOLOGIE | 0.8 | STATIQUE | déclaré_article |
| PhotoCraft | TECHNOLOGIE | mesure | 71 629 étoiles GitHub au 23 octobre 2026 | MESURE | 0.9 | STATIQUE | déclaré_article |
| arrêt SAS Institute | DOCUMENT | affirme_que | ni la fonctionnalité, ni le langage, ni le format des fichiers ne sont protégés par le droit d'auteur | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| CJUE | ORGANISATION | publie | arrêt SAS Institute | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| arrêt BSA C-393/09 | DOCUMENT | affirme_que | une interface graphique originale peut être protégée par le droit d'auteur commun | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Andres Guadamuz | PERSONNE | affirme_que | « We also do not know whether the claimed 'clean-room process' stands up to scrutiny » | CITATION | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la séparation des rôles est difficile à démontrer quand un modèle de langage écrit le code | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | une fonctionnalité visible de l'extérieur se réimplémente désormais en quelques semaines | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | spécification depuis le comportement observé, équipe sans accès au code décompilé, journal de qui a vu quoi | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil, éditeur de sfeir.com | AJOUT |
| ArtCraft | TECHNOLOGIE | définition | Ensemble de réécritures en Rust d'applications Adobe et bureautiques (organisation GitHub storytold), MIT/Apache-2.0 | AJOUT |
| PhotoCraft | TECHNOLOGIE | définition | Réimplémentation de Photoshop revendiquée clean-room, alpha | AJOUT |
| Brandon Thomas | PERSONNE | rôle | Ingénieur à Atlanta, ex-Storyteller.ai et Square, identifié par la presse derrière ArtCraft | AJOUT |
| réimplémentation clean-room | METHODOLOGIE | définition | Une équipe spécifie le comportement, une autre réécrit sans voir le code d'origine | AJOUT |
| arrêt SAS Institute | DOCUMENT | référence | CJUE, 2 mai 2012, C-406/10 | AJOUT |
| arrêt BSA C-393/09 | DOCUMENT | référence | CJUE, 22 décembre 2010, protection d'une interface graphique originale | AJOUT |
| Andres Guadamuz | PERSONNE | rôle | Spécialiste de propriété intellectuelle, université du Sussex | AJOUT |
