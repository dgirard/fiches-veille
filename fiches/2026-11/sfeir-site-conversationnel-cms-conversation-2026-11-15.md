---
themes: [architecture-construction, transformation-adoption]
source: SFEIR
---
# sfeir-site-conversationnel-cms-conversation-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, tête d'une série de sept textes consacrés au passage de sfeir.com à un mode conversationnel, ouvert le **16 novembre 2026**. Le texte raconte **quatre versions** du site et ce que chacune a coûté. **(1)** **2021** : un CMS WordPress construit par un prestataire en environ **six mois** pour quelque **100 000 €** (ordres de grandeur internes). **(2)** **Printemps 2025** : reconstruction en pages générées sur Google Cloud Run en **une semaine** pour environ **1 000 €** ; toute modification passe par un agent (**Claude Code**). **(3)** **Printemps 2026** : une **base de connaissances** versionnée dans Git, une fiche par notion ; première version construite en une soirée le **1er avril 2026** (294 pages, 42 fiches), hébergement sur Cloudflare, mise en production fin mai. **(4)** **Automne 2026** : la conversation, sur une base de **363 fiches** et **2 053 sources** au 13 novembre ; trois semaines de construction, **1 157 échanges** en préversion. Le verdict est posé d'emblée : *« la conversation n'a été possible que parce qu'une base de connaissances l'a précédée »*. Le texte borne lui-même son périmètre : chiffres 2021-2025 non audités, site sans enjeu métier fort.

## Titre Article

Site conversationnel : comment sfeir.com est passé du CMS à la conversation

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/site-conversationnel-du-cms-a-la-conversation/

## Keywords

site conversationnel, CMS, WordPress, sortie de CMS, agent de code, Claude Code, base de connaissances, fiche par notion, Git, projection, Cloudflare, Google Cloud Run, réponse sourcée, préversion, Forward Deployed Engineer, matière vs outil, Web Platform, SFEIR

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : récit d'entreprise à la première personne du pluriel, publié par un cabinet sur son propre site, en tête d'une série. Public déclaré : DSI et direction générale, secondairement direction marketing.

**Style** : chronologique et sobre, quatre sous-parties datées, phrases courtes, chiffres placés en tête de paragraphe. Une figure résume les quatre versions selon quatre axes (qui met à jour, ce qui fait foi, ce que voit le visiteur, construction). Formule récurrente : le travail se déplace *« de l'outil vers la matière »*.

**Position épistémique** : le texte distingue explicitement la provenance de ses chiffres — ordres de grandeur internes non audités pour 2021 et 2025, dépôt Git (1 482 commits) et journaux de préversion pour 2026. Une section « limites de ce récit » précède la conclusion par rôle. Le texte renvoie à une offre maison (Sortie de CMS, Web Platform) en appel final.

## Pense-betes

- **Thèse de la série** : chaque version a déplacé le travail de l'outil vers la matière ; la conversation n'est possible qu'après la base de connaissances.
- **2021, un CMS** : WordPress, prestataire, ~6 mois, ~100 k€. L'outil garantit la forme, le marketing fournit le fond ; une page coûte cher, donc on en crée peu.
- **Printemps 2025, un agent** : pages générées, Google Cloud Run ; règle sans exception, *toute modification passe par un agent d'IA* (Claude Code). ~1 semaine, ~1 000 €. Limite : une définition reprise dans dix pages peut dériver de dix façons.
- **Printemps 2026, une base** : chaque notion a sa fiche versionnée dans Git, avec ses sources ; chaque page devient une projection. Premier commit 18 h 31, fusion 21 h 55 le 1er avril ; 294 pages dont 107 articles et 42 fiches. Puis durcissement : audit complet, **276 liens internes cassés** corrigés, mise en prod fin mai.
- **Automne 2026, la conversation** : 363 fiches, 2 053 sources, 384 articles au 13 novembre. La réponse rédigée ne s'appuie que sur les contenus publiés et cite ses sources ; la colonne de pages est composée par des règles écrites, un petit modèle de classification aide au tri.
- **Durées** : première couche conversationnelle en quelques heures ; conversation complète du 28 octobre au 16 novembre ; préversion de 1 157 échanges (29 octobre – 13 novembre).
- **Trois leçons** : une version coûte de moins en moins, mais la base a demandé **sept mois d'efforts continus** ; l'agent seul ne suffit pas (contrôles qui bloquent avant publication) ; un site institutionnel est un bon premier terrain (enjeu faible, erreur vite corrigée).
- **Limites déclarées** : chiffres 2021/2025 non audités ; transposition client = son propre travail de base ; hors périmètre, la conversation le dit et propose les pages proches.
- **Par rôle** : DSI — le premier chantier est l'état des contenus, le modèle vient ensuite ; marketing — de la production de pages à la tenue de la matière.

## RésuméDe400mots

SFEIR ouvre une série de sept articles sur la transformation de son site, sfeir.com, dont la page d'accueil devient une conversation le 16 novembre 2026 : le visiteur pose une question, le site répond à partir de ses propres contenus et affiche les pages utiles. Le premier texte raconte quatre versions successives et soutient une thèse unique : chaque version a déplacé le travail de l'outil vers la matière, et la conversation n'a été possible que parce qu'une base de connaissances l'a précédée.

En 2021, le site tournait sur WordPress, construit par un prestataire en six mois environ pour quelque 100 000 euros, selon des chiffres internes. Chaque modification passait par le back-office. Le modèle garantissait la forme, mais une page coûtant cher, on en créait peu.

Au printemps 2025, le site est reconstruit en pages générées, déployées sur Google Cloud Run, en une semaine pour environ 1 000 euros. Une règle gouverne le projet : toute modification passe par un agent d'IA, Claude Code ; l'humain demande, l'agent écrit et commite. La limite apparaît vite : le contenu vit dans les pages, et une définition reprise dix fois peut dériver dix fois.

Au printemps 2026, le contenu s'appuie sur une base de connaissances : une fiche par notion, versionnée dans Git, avec ses sources, chaque page devenant une projection de cette matière. La première version complète est construite en une soirée, le 1er avril, avec 294 pages dont 42 fiches ; le site passe sur Cloudflare. Plusieurs semaines de durcissement suivent, dont la correction de 276 liens internes cassés, avant une mise en production fin mai.

À l'automne 2026, la base compte 363 fiches et 2 053 sources, le site 384 articles. Elle est jugée assez solide pour être interrogée. La réponse rédigée ne s'appuie que sur les contenus publiés et cite ses sources ; la colonne de pages voisine est composée par des règles écrites, aidées par un petit modèle de classification. La couche conversationnelle a demandé trois semaines, et 1 157 échanges ont été testés en préversion.

L'article en tire trois enseignements : le coût de construction baisse à chaque version, mais la base a exigé sept mois d'effort continu ; l'agent seul ne suffit pas sans contrôles bloquants ; le site institutionnel est un terrain d'essai peu risqué pour une organisation. Il signale ses limites : chiffres anciens non audités, site sans enjeu métier fort, conversation bornée au contenu de la base.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article Site conversationnel du CMS à la conversation | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | a_créé | sfeir.com | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | base de connaissances sfeir.com | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | Claude Code | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | Cloudflare | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | remplace | WordPress | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| site conversationnel | CONCEPT | est_basé_sur | base de connaissances sfeir.com | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la conversation n'a été possible que parce qu'une base de connaissances l'a précédée | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| base de connaissances sfeir.com | TECHNOLOGIE | mesure | 363 fiches et 2 053 sources au 13 novembre 2026 | MESURE | 0.92 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | CMS 2021 : ~6 mois et ~100 k€ ; agent 2025 : ~1 semaine et ~1 000 € | MESURE | 0.85 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | mesure | 1 157 échanges en préversion du 29 octobre au 13 novembre 2026 | MESURE | 0.9 | STATIQUE | déclaré_article |
| fiche par notion | METHODOLOGIE | résout | dérive des définitions répétées dans les pages | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | commencer par l'état des contenus avant le choix du modèle | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| site conversationnel | CONCEPT | s_applique_à | site institutionnel comme terrain d'essai des agents | CONCEPT | 0.82 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet de conseil et d'ingénierie | AJOUT |
| sfeir.com | TECHNOLOGIE | historique | WordPress (2021) → pages générées par agent (2025) → base de connaissances (2026) → conversation (16/11/2026) | AJOUT |
| base de connaissances sfeir.com | TECHNOLOGIE | volume | 42 fiches au 1er avril 2026, 363 au 13 novembre 2026 | AJOUT |
| site conversationnel | CONCEPT | définition | Site dont l'accueil répond aux questions à partir de ses contenus, avec sources et pages utiles | AJOUT |
| fiche par notion | METHODOLOGIE | principe | Une définition unique versionnée dans Git, les pages en sont des projections | AJOUT |
