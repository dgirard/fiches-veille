---
themes: [transformation-adoption, economie-marche]
source: SFEIR
---
# sfeir-fde-101-kevin-bai-anthropic-2026-11-10

## Veille

Critique éditoriale **SFEIR AI** publiée sur sfeir.com le **10 novembre 2026**, l'une des neuf de la série consacrée à la playlist *forward deployed engineering* de l'**AI Engineer World's Fair 2026**. Elle porte sur le « FDE 101 » de **Kevin Bai** (Applied AI d'**Anthropic**, premier FDE de **Rippling**, ex-**Palantir**), 17 min 48, environ **87 700** vues, le talk le plus vu de la série. Trois apports. **(A)** Une grille à quatre cases croisant la technicité du produit et celle de l'acheteur : le FDE ne se justifie que pour une plateforme sur laquelle il faut développer, vendue à un acheteur non technique. **(B)** Le test du « dev shop » : une équipe qui écrit chaque application de zéro laisse *« 55 dépôts que personne ne voudra maintenir »* — *« you do not have an FDE function. You have a dev shop »*. **(C)** Une hypothèse : les plateformes devenant agentiques, la case « produit technique, acheteur non technique » s'étendrait à une grande partie du logiciel. Notes SFEIR : originalité **3/5**, qualité de l'information **3/5**. Rejoint la lecture produit du FDE de [[zhang-decagon-fde-produit-2026-08-11]].

## Titre Article

Kevin Bai (Anthropic) ramène le FDE à une question : qui achète quoi ?

## Date

2026-11-10

## URL

https://www.sfeir.com/articles/fde-101-kevin-bai-anthropic/

## Keywords

forward deployed engineering, FDE, FDE 101, Kevin Bai, Anthropic, Applied AI, Rippling, Palantir, Foundry, ontologie, AI Engineer World's Fair 2026, grille produit/acheteur, acheteur non technique, dev shop, développement à façon, plateforme, briques réutilisables, maintenance, valeur moyenne des contrats, plateformes agentiques, ESN, critique de talk

## Authors

SFEIR AI (voix éditoriale non signée), sfeir.com, site éditorial de SFEIR. Critique du talk de Kevin Bai (Anthropic).

## Ton

Critique de talk au format fixe de la série SFEIR : encadré (vidéo, orateur, durée, vues, deux notes sur 5), restitution par minutage, section « Pour une ESN », verdict argumenté, barème rappelé en pied. Registre journalistique sobre, phrases courtes, en français, citations en anglais traduites entre parenthèses. L'auteur distingue explicitement ce qui est utile (la grille, le test du « dev shop ») de ce qui relève de l'initiation, et signale les faiblesses de sourçage : chiffres de contrats *« de mémoire, avec des précautions de langage, sans date ni source »*, aucun propos sur la pratique d'Anthropic. Public visé : dirigeants d'ESN, comités de direction qui envisagent une équipe FDE, débutants sur le sujet.

## Pense-betes

- **Format** : 17 min 48, mis en ligne le 28 juillet 2026, ~87 700 vues au 10 novembre 2026 — devance de loin les huit autres talks de la playlist.
- **Orateur** : Kevin Bai, member of technical staff (Applied AI, Anthropic) ; premier FDE de Rippling (équipe montée à ~25 personnes en un an selon lui) ; ex-Palantir. Ne parle pas de son travail actuel.
- **Origine Palantir** : Foundry centralise les données et en tire une ontologie, mais le client ne sait qu'en faire → Palantir vend un résultat = plateforme + ingénieurs chez le client.
- **Grille (vers 4:18)** : axe technicité du produit × technicité de l'acheteur. GitHub, Datadog (produit complexe, acheteur technique) et Rippling, Jira, Slack (outil configurable, acheteur non technique) → pas de FDE. **Case FDE** : plateforme à développer vendue à un acheteur sans compétence logicielle (ex. pétrolier du Fortune 500). Métaphore du serveur de grand restaurant.
- **Valeur moyenne des contrats (vers 6:19, de mémoire)** : ~4 M$ Palantir, 1,2 M$ ServiceNow, ~600 000 $ Workday, aucun autre au-dessus de 500 000 $.
- **Test du « dev shop » (vers 8:19)** : une équipe FDE assemble des briques d'une plateforme commune ; sans elles, la maintenance mange la marge.
- **Deux questions avant de créer une équipe FDE (vers 9:20)** : vendez-vous du très technique à un acheteur qui ne l'est pas ? avez-vous une plateforme, ou la volonté d'en construire une ?
- **Hypothèse agentique (vers 11:21)** : plateformes agentiques → personnalisables → incompréhensibles pour une partie des clients → la case FDE s'étend. Exposée en une minute, sans exemple.
- **Questions de la salle** : application livrée à 60 % puis personnalisée sur 40 %, ou briques fines type DynamoDB ; deux FDE par projet pour éviter la concentration d'information ; ce qui se généralise remonte dans la plateforme, le FDE sert d'éclaireur. Définition : un ingénieur logiciel qu'on peut mettre devant un client.
- **Pour une ESN** : rebaptiser des consultants FDE ne suffit pas ; il faut livrer à partir de briques réutilisées d'une mission à l'autre.
- **Verdict SFEIR** : 3/5 et 3/5 — à voir en premier pour découvrir le sujet.

## RésuméDe400mots

SFEIR AI publie le 10 novembre 2026 une critique du talk « Forward Deployed Engineering 101 » donné par Kevin Bai à l'AI Engineer World's Fair 2026. Avec près de 88 000 vues, c'est la vidéo la plus regardée des neuf que la chaîne AI Engineer consacre au forward deployed engineering. Kevin Bai travaille dans l'équipe Applied AI d'Anthropic, a été le premier FDE de Rippling et est passé par Palantir ; il ne dit rien de son travail chez Anthropic.

Le talk part de Palantir. Sa plateforme Foundry centralise les données d'une entreprise et en tire une ontologie, mais un dirigeant de la grande consommation demande ce que cela change à sa place en rayon. Palantir a donc vendu un résultat : la plateforme plus des ingénieurs qui construisent la solution chez le client.

Le cœur du propos est une grille à deux axes : technicité de ce que l'on vend, technicité de l'acheteur. GitHub ou Datadog vendent un produit complexe à des développeurs qui absorbent la complexité ; Rippling, Jira ou Slack vendent des outils configurables à des non-techniciens. Aucun n'a besoin de FDE. Il en faut quand une plateforme sur laquelle il faut développer est vendue à un acheteur sans compétence logicielle. Kevin Bai appuie l'intérêt économique du modèle sur des valeurs moyennes de contrat citées de mémoire (environ 4 M$ pour Palantir, 1,2 M$ pour ServiceNow).

Le passage jugé le plus utile répond à l'objection de la maintenance. Une équipe qui écrit chaque application de zéro laisse des dizaines de dépôts orphelins : ce n'est pas une fonction FDE mais un « dev shop », une société de développement à façon, éventuellement rentable sous un autre nom. Une équipe FDE assemble des briques d'une plateforme commune. D'où deux questions pour toute entreprise tentée : vend-elle du technique à un acheteur qui ne l'est pas, et a-t-elle une plateforme ou la volonté d'en bâtir une ?

L'hypothèse la plus neuve, selon SFEIR, est exposée en une minute : les plateformes devenant agentiques et donc personnalisables, la case du FDE s'étendrait à une grande partie du logiciel. Les questions de la salle précisent la pratique (deux FDE par projet, généralisation vers la plateforme, FDE éclaireur).

Pour une ESN, l'article retient que le titre ne se mérite pas en renommant des consultants. Verdict : originalité 3/5, qualité de l'information 3/5 ; talk recommandé en premier aux débutants.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | critique FDE 101 Kevin Bai | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| critique FDE 101 Kevin Bai | DOCUMENT | référence | AI Engineer World's Fair 2026 | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Kevin Bai | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.93 | DYNAMIQUE | déclaré_article |
| Kevin Bai | PERSONNE | affirme_que | le FDE se justifie pour une plateforme à développer vendue à un acheteur non technique | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Kevin Bai | PERSONNE | affirme_que | "you do not have an FDE function. You have a dev shop" | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| Forward Deployed Engineering | METHODOLOGIE | s_inspire_de | Palantir | ORGANISATION | 0.88 | STATIQUE | déclaré_article |
| Palantir | ORGANISATION | a_créé | Foundry | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Forward Deployed Engineering | METHODOLOGIE | utilise | plateforme commune | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| test du dev shop | CONCEPT | s_applique_à | Forward Deployed Engineering | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| Kevin Bai | PERSONNE | mesure | valeur moyenne des contrats ~4 M$ chez Palantir, 1,2 M$ chez ServiceNow | MESURE | 0.75 | STATIQUE | déclaré_article |
| Kevin Bai | PERSONNE | prédit | les plateformes agentiques étendent le besoin de FDE à une grande partie du logiciel | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | livrer à partir de briques réutilisées d'une mission à l'autre pour mériter le titre FDE | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Kevin Bai | PERSONNE | recommande | deux FDE par projet | AFFIRMATION | 0.8 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Kevin Bai | PERSONNE | rôle | Member of technical staff, Applied AI, Anthropic ; premier FDE de Rippling ; ex-Palantir | AJOUT |
| critique FDE 101 Kevin Bai | DOCUMENT | notes SFEIR | Originalité 3/5, qualité de l'information 3/5 | AJOUT |
| AI Engineer World's Fair 2026 | EVENEMENT | playlist | Neuf talks sur le forward deployed engineering, mis en ligne du 14 au 28 juillet 2026 | AJOUT |
| test du dev shop | CONCEPT | définition | Une équipe qui repart de zéro chez chaque client fait du développement à façon, pas du FDE | AJOUT |
| Forward Deployed Engineering | METHODOLOGIE | condition | Produit technique vendu à un acheteur non technique + plateforme réutilisable | AJOUT |
