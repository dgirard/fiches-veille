---
themes: [architecture-construction, outils-plateformes]
source: SFEIR
---
# sfeir-ecrire-moteurs-ia-schema-org-llms-txt-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, volet de la série sur le site conversationnel de sfeir.com consacré à l'écriture pour les moteurs et les assistants. Une page a *« au moins quatre lecteurs »* : la personne, Google, les robots des assistants, le chat du site. **(1)** Une notion, une fiche : **363 fiches**, une phrase de définition de référence, des alias, des titres à gabarit par collection en **60 caractères** au plus. **(2)** Un seul graphe **schema.org** JSON-LD par page, nœuds reliés par `@id` ; la relation `about` est calculée en inversant les `relatedArticles` des fiches (**305 fiches** en déclarent). Le build bloque un `@id` sans nœud ou deux blocs JSON-LD. **(3)** **llms.txt** publié (742 entrées, ~236 Ko) *« sans en attendre d'effet »* : position de **John Mueller** (17 juin 2025), étude **Ahrefs** (15 juin 2026 : 97 % des fichiers non lus en mai 2026). **(4)** Un robots.txt ouvert, qui répète ses exclusions dans les blocs des robots d'IA nommés (RFC 9309). **(5)** Des dates exactes, tirées du dernier commit. **(6)** L'étude **Pew** de juillet 2025 (8 % de clics avec résumé d'IA, 15 % sans), contestée par Google. L'article reconnaît ne publier aucune mesure du trafic venu des assistants.

## Titre Article

Écrire pour les moteurs et pour les IA : graphe schema.org, llms.txt et fiches de référence

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/ecrire-pour-moteurs-et-ia-schema-org-llms-txt/

## Keywords

GEO, generative engine optimization, SEO, schema.org, JSON-LD, @graph, @id, DefinedTerm, DefinedTermSet, about, données structurées, llms.txt, robots.txt, RFC 9309, robots d'IA, Google-Extended, plan du site, dateModified, fraîcheur, titres durables, résumés d'IA, AI Overviews, Pew Research Center, Ahrefs, John Mueller, Jeremy Howard, base de connaissances, SFEIR

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article de pratique éditoriale et technique, écrit par le cabinet sur son propre site. Public déclaré : équipes éditoriale et marketing, secondairement CTO et DSI.

**Style** : sobre, structuré par décisions (« ce que nous faisons », « ce que nous avons décidé de ne pas attendre »), une figure de graphe schema.org simplifié autour d'un article sur le FDE. Le texte refuse explicitement le registre des « astuces de GEO ». Exemples concrets de gabarits de titre et de types schema.org par collection.

**Position épistémique** : sept sources externes datées (Google Search Central, llmstxt.org, Search Engine Roundtable, Ahrefs, RFC 9309, Pew, The Register) ; la contestation de l'étude Pew par Google est mentionnée. Les attentes sont bornées : aucun gain de position garanti, aucun résultat enrichi garanti, llms.txt *« peut ne jamais être lu »*. Une section « ce que nous ne savons pas encore » assume l'absence de mesure du trafic issu des assistants.

## Pense-betes

- **Quatre lecteurs** d'une page : humain, Google, robots des assistants, chat du site. Ce sont les mêmes fiches et le même catalogue qui les servent.
- **Fiche de référence** : phrase de définition reprise telle quelle par page, chat et données structurées ; alias ; forme longue d'acronyme posée à la main ; FAQ si questions réelles ; 277 fiches sourcées, 2 053 sources.
- **Gabarits de titre** (≤ 60 caractères) : « X : définition et enjeux » (concept), « X : ce que c'est, à quoi ça sert » (technologie), « X : principes et mise en œuvre » (méthode).
- **Lien automatique** : première mention sur les pages de la base ; dans les articles, seulement 62 notions sans ambiguïté.
- **Graphe schema.org** : un seul `@graph` par page ; SFEIR et le site sous le même `@id` partout. Concept → DefinedTerm dans un DefinedTermSet ; technologie → SoftwareApplication ; méthode → HowTo ; personne → Person ; formations → Course ; offres d'emploi → JobPosting ; agences → LocalBusiness.
- **`about` calculé** : la fiche déclare ses articles, le build inverse. Article sans `about` = signalé. Renvois refermés dans le graphe par un nœud réduit à son identité.
- **llms.txt** : proposition de Jeremy Howard (3 septembre 2024). Google Search ne s'en sert pas (Mueller, 17 juin 2025 ; documentation actuelle). Ahrefs : 137 210 domaines, ~38 000 servent un llms.txt, 97 % jamais requêtés en mai 2026. Publié parce qu'il *ne coûte rien* dans un build existant.
- **robots.txt** : tout autorisé sauf l'API du chat et les liens `?q=`. Les robots d'OpenAI, Anthropic, Perplexity, Google-Extended, Applebot-Extended et Common Crawl sont nommés et répètent les exclusions, car un robot nommé dans son bloc n'obéit plus au bloc général. Contenus ouverts aux moteurs de réponse **et** à l'entraînement.
- **Dates vraies** : `lastmod` = dernier commit du fichier source, clone complet de l'historique ; `dateModified` réservé aux révisions de fond ; aucun compteur mouvant dans un titre.
- **Être cité ne fait pas venir** : Pew (juillet 2025) — 8 % de clics avec résumé d'IA contre 15 % sans, 1 % sur les liens du résumé.

## RésuméDe400mots

Ce volet de la série consacrée à sfeir.com décrit comment le site écrit pour ses lecteurs automatiques : le robot de Google, ceux des assistants d'IA et le chat du site lui-même. L'article écarte d'emblée les listes d'astuces d'optimisation pour moteurs génératifs et résume sa réponse en trois points : chaque notion est définie une fois dans une fiche, chaque page porte un seul graphe schema.org vérifié au build, et le fichier llms.txt est publié sans qu'on en attende d'effet.

La base de connaissances compte 363 fiches au 13 novembre 2026. Chaque fiche s'ouvre sur une phrase de définition de référence, reprise par la page, le chat et les données structurées. Elle porte des alias, la forme longue des acronymes posée à la main, des sections, une FAQ éventuelle et des sources. Les titres suivent un gabarit par type de fiche, en soixante caractères au plus.

Chaque page contient un unique bloc JSON-LD dont les nœuds se désignent par identifiant. Les fiches deviennent des DefinedTerm, SoftwareApplication, HowTo ou Person selon leur type. Le lien le plus utile, about, est calculé : la fiche déclare les articles qui la traitent et le build inverse la relation. Le build bloque les identifiants orphelins et les doubles blocs. L'article rappelle que Google dit se servir des données structurées pour comprendre une page, sans garantie de position.

Le fichier llms.txt, proposé par Jeremy Howard en 2024, liste 742 entrées. Il est publié parce qu'il ne coûte rien, mais l'article cite la position de Google, qui ne s'en sert pas, et une étude Ahrefs de juin 2026 selon laquelle 97 % de ces fichiers n'ont reçu aucune requête en mai 2026.

Le robots.txt autorise tout sauf l'API du chat et les liens portant une question, pour éviter qu'un texte arbitraire s'affiche sous le domaine. Les robots d'IA sont nommés et répètent ces exclusions, conformément au protocole d'exclusion. Les contenus sont ouverts aux moteurs de réponse comme à l'entraînement. Les dates du plan du site viennent du dernier commit de chaque fichier.

Enfin, l'article cite l'étude Pew de juillet 2025 : avec un résumé d'IA, les clics sur les résultats tombent de 15 % à 8 %. Être cité ne suffit pas ; la page doit mener l'acheteur ou le candidat à l'étape suivante. L'article reconnaît ne disposer d'aucune mesure propre du trafic issu des assistants.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article Écrire pour les moteurs et pour les IA | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | schema.org | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | JSON-LD | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | llms.txt | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Jeremy Howard | PERSONNE | a_créé | llms.txt | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| John Mueller | PERSONNE | affirme_que | aucun système d'IA n'utilise llms.txt (17 juin 2025) | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| John Mueller | PERSONNE | travaille_chez | Google | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| Ahrefs | ORGANISATION | mesure | 97 % des fichiers llms.txt sans aucune requête en mai 2026, sur 137 210 domaines | MESURE | 0.88 | STATIQUE | déclaré_article |
| Pew Research Center | ORGANISATION | mesure | 8 % de clics sur un résultat avec résumé d'IA contre 15 % sans (juillet 2025) | MESURE | 0.88 | STATIQUE | déclaré_article |
| Google | ORGANISATION | s_oppose_à | méthode de l'étude Pew sur les résumés d'IA | CONCEPT | 0.8 | STATIQUE | déclaré_article |
| graphe schema.org par page | METHODOLOGIE | utilise | DefinedTerm | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| graphe schema.org par page | METHODOLOGIE | fait_partie_de | sfeir.com | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | RFC 9309 | DOCUMENT | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | être cité par un assistant ne fait pas venir le visiteur | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | faire du graphe unique, des identifiants stables et des renvois refermés des contrôles de build | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | dater chaque fait mouvant dans sa phrase et bannir les compteurs mouvants des titres | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| llms.txt | TECHNOLOGIE | définition | Fichier Markdown à la racine d'un site présentant ses pages aux LLM (proposé le 3 septembre 2024) | AJOUT |
| graphe schema.org par page | METHODOLOGIE | principe | Un seul bloc JSON-LD @graph, nœuds reliés par @id, about calculé depuis les fiches | AJOUT |
| DefinedTerm | TECHNOLOGIE | rôle | Type schema.org d'une fiche de concept, rangée dans un DefinedTermSet | AJOUT |
| John Mueller | PERSONNE | rôle | Search Advocate, Google | AJOUT |
| Jeremy Howard | PERSONNE | rôle | Auteur de la proposition llms.txt | AJOUT |
| Pew Research Center | ORGANISATION | secteur | Institut de recherche et d'enquêtes | AJOUT |
