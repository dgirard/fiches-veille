---
themes: [qualite-securite, agents-codage-ia-skills, outils-plateformes]
source: "Sonatype"
---
# linskens-sonatype-securite-vitesse-ia-quatre-ans-2026-08-18

## Veille

Billet du blog de **Sonatype** signé **Aaron Linskens** (*technical writer*), publié le **18 août 2026**, ~1 300 mots : il restitue une étude de **Sonatype Research Labs** portant sur **49 mois** (juin 2022 — juin 2026) et sur une **cohorte fixe** d'applications d'entreprise, choix de méthode revendiqué pour isoler l'évolution du parc plutôt que celle du portefeuille clients. Résultat présenté comme une contradiction : on corrige plus vite et on accumule pourtant plus de risque. (A) **Le stock monte** — vulnérabilités *Critical* et *High* par application **×4,31** (de **14,14** en juin 2022 à **54,3** en 2026, encore **×3,91** hors applications légataires nouvellement prises en gestion), versions de composants nouvellement affectées à **46×** le rythme d'avant l'IA, création mensuelle d'applications **×4,84**. (B) **La remédiation progresse** — plus de la moitié des violations résolues le sont en moins d'un jour, l'âge médian des *Critical/High* non résolues passe de **228** à **126 jours** puis à **103** en mai 2026 ; sur les cohortes ayant eu douze mois, **52,6 %** sont résolues, **44,3 %** ouvertes, **3,1 %** en dérogation. (C) **Le point d'appui proposé est le choix du composant** : au moment où une dépendance vulnérable a été retenue, une version sensiblement moins risquée existait déjà dans **62,2 %** des cas sur **Maven**, **46,9 %** sur **npm**, **34,3 %** sur **PyPI** — écart que le texte attribue à un défaut d'information et non à une faute de développeur. Le billet énonce lui-même que l'IA n'est pas la cause unique de l'accélération, et se conclut sur **Sonatype Guide**, qui porte cette intelligence au point de sélection. Il prolonge côté chaîne d'approvisionnement ce que [[fiches/2026-08/staples-gitlab-when-code-is-abundant-2026-08-24]] pose en économie et [[fiches/2026-07/clinton-anthropic-secure-ai-native-sdlc-2026-07-21]] en cycle sécurisé.

## Titre Article

Securing Software at the Speed of AI: What Four Years of Data Reveal

## Date

2026-08-18

## URL

https://www.sonatype.com/blog/securing-software-at-the-speed-of-ai-what-four-years-of-data-reveal

## Keywords

chaîne d'approvisionnement logicielle, software supply chain, Sonatype Research Labs, cohorte fixe, étude longitudinale, vulnérabilités Critical et High, avis de vulnérabilité, versions de composants affectées, dépendances open source, sélection de composant, version moins risquée, âge médian des vulnérabilités, délai de remédiation, dérogation, Maven, npm, PyPI, prévention vs remédiation, assistant de codage IA, intelligence de composant, politique organisationnelle, Sonatype Guide, The AI-Era Software Assembly Line, ère IA

## Authors

Aaron Linskens, *technical writer* chez Sonatype, sur le blog de l'éditeur ; les chiffres sont produits par Sonatype Research Labs, non par l'auteur.

## Ton

Profil : billet de blog d'éditeur en restitution d'étude — format court, cinq intertitres, une liste de chiffres par section, ton mesuré et sans emphase, public cible responsables sécurité applicative, équipes plateforme et décideurs achat d'outillage. Le registre est celui du **compte rendu chiffré** : chaque affirmation est adossée à une mesure, les pourcentages sont donnés avec leur base (nombre de mois, périodes de comparaison, écosystèmes nommés séparément), et la méthode est exposée avant les résultats. Deux gestes de prudence sont explicites dans le texte, ce qui est peu fréquent dans ce format : la pluralité des causes est reconnue (*« AI alone did not cause this acceleration »*, avec quatre facteurs alternatifs nommés dont l'amélioration de la recherche de vulnérabilités elle-même), et l'écart mesuré sur le choix des versions est expressément retiré du registre de la faute (*« This should not be interpreted as developer failure »*). La rhétorique repose sur une **contradiction apparente** posée d'emblée puis tenue jusqu'au bout : remédiation plus rapide, risque accumulé plus élevé, d'où le déplacement proposé du curseur vers l'amont. La visée commerciale est assumée dans la dernière section, qui nomme le produit et le rattache au chiffre qui le motive. L'autorité tient à la position d'observatoire de l'éditeur — catalogue d'avis de vulnérabilité, parc d'applications instrumenté — et le billet renvoie au rapport complet, *The AI-Era Software Assembly Line*, pour les données sous-jacentes.

## Pense-betes

- **La contradiction est le résultat principal**, et elle est arithmétique avant d'être stratégique : la remédiation s'accélère (âge médian **228 → 126 → 103 jours**) pendant que le stock par application quadruple (**14,14 → 54,3** *Critical/High*). Corriger plus vite ne suffit pas quand le flux entrant croît plus vite que la capacité de traitement.
- **Le risque d'une application bouge sans que son code bouge.** Formulation directe du billet : une dépendance jugée acceptable hier peut recevoir demain une divulgation, devenir non maintenue, ou voir paraître une version plus sûre. Conséquence pour la veille interne : un inventaire figé n'est pas un état de sécurité, et l'absence de commit n'est pas l'absence d'événement.
- **Le chiffre le plus actionnable est celui de la version disponible** : au moment de la sélection, une version sensiblement moins risquée existait déjà dans **62,2 %** des cas sur **Maven**, **46,9 %** sur **npm**, **34,3 %** sur **PyPI**. L'écart entre écosystèmes est lui-même une donnée — il ordonne où la prévention rend le plus.
- **Deux causes distinctes derrière un même symptôme** : certaines vulnérabilités sont inévitables (l'écosystème n'offre pas d'option plus sûre), d'autres sont des **problèmes d'information** (celui qui choisit — humain ou assistant — n'a pas le bon contexte au moment de choisir). Seule la seconde classe est adressable par de l'outillage au point de sélection.
- **Le point de tension propre à l'IA**, tel que le billet le pose : un assistant peut recommander et introduire un composant en quelques secondes, mais *« a fast recommendation is not necessarily an informed one »* — il lui faut une intelligence **courante** sur le risque, les versions disponibles, la maintenance et la politique interne, que la connaissance figée dans les poids du modèle ne garantit pas.
- **Ce que le billet ne chiffre pas**, et qu'il faut demander au rapport complet avant de citer : l'**effectif de la cohorte** (aucun nombre d'applications), la **valeur du pic de janvier 2024** — alors que la baisse de **59 %** s'y réfère, quand la baisse de **45 %** part de 228 jours, donc de deux bases différentes —, et la **date de début de « l'ère IA »**, employée comme borne de comparaison sans être définie.
- **La honnêteté causale est portée par le texte lui-même** : quatre facteurs alternatifs à l'IA sont nommés pour l'expansion du paysage de vulnérabilités — meilleure recherche, meilleure divulgation, recherche de sécurité assistée par IA, évolution du comportement des attaquants. La position retenue est pragmatique : *« Organizations don't need to prove a single cause to confront the outcome. The scale itself is the problem. »*
- **À relier** : [[fiches/2026-08/claxton-anthropic-ai-native-sdlc-playbook-2026-08-21]] (la skill conseille, le hook contraint — ici la politique de composant est exactement ce qui gagne à devenir déterministe au moment du choix) et [[fiches/2026-07/sfeir-code-review-anneau-contraintes-2026-07-30]] (l'anneau de contraintes autour de l'agent, dont la sélection de dépendance est un maillon amont rarement instrumenté).

## RésuméDe400mots

Sonatype publie, sous la plume de son *technical writer* Aaron Linskens, la synthèse d'une étude longitudinale de ses laboratoires de recherche portant sur quarante-neuf mois, de juin 2022 à juin 2026. La méthode est annoncée d'emblée : une cohorte fixe d'applications suivies en continu, pour que les variations mesurées reflètent l'évolution du parc logiciel et non celle du portefeuille de clients. Le résultat central est présenté comme une contradiction : les organisations corrigent plus vite qu'avant, et leurs applications accumulent pourtant davantage de risque.

Quatre mesures cadrent le constat. Les vulnérabilités classées *Critical* et *High* par application ont été multipliées par 4,31, passant d'une moyenne de 14,14 en juin 2022 à 54,3 en 2026 ; l'effet ne tient pas au seul héritage, puisque l'exclusion des applications légataires récemment prises en gestion laisse un facteur 3,91. Les versions de composants nouvellement affectées progressent à quarante-six fois le rythme d'avant l'IA. L'âge médian des vulnérabilités a reculé de 59 % depuis son pic de janvier 2024. Enfin, la création mensuelle moyenne d'applications a été multipliée par 4,84, et avec elle les décisions de dépendance.

La progression de la remédiation est réelle : plus de la moitié des violations résolues le sont en moins d'une journée, et l'âge médian des *Critical/High* non résolues tombe de 228 à 126 jours, puis à 103 jours en mai 2026. Sur les cohortes disposant d'au moins douze mois pour agir, 52,6 % sont résolues, 44,3 % restent ouvertes et 3,1 % font l'objet d'une dérogation.

Le déplacement proposé porte sur l'amont. Les chercheurs ont examiné les dépendances vulnérables entrées dans les applications de la période et posé une question simple : au moment de la sélection, une version sensiblement moins risquée existait-elle déjà ? La réponse est oui dans 62,2 % des cas sur Maven, 46,9 % sur npm et 34,3 % sur PyPI. Le texte refuse d'y lire une faute de développeur : certaines vulnérabilités sont inévitables, d'autres relèvent d'un défaut d'information au moment du choix — un point qui devient sensible quand un assistant IA peut introduire un composant en quelques secondes sans disposer d'une intelligence à jour sur son risque et sur la politique de l'organisation.

Le billet reconnaît que l'IA n'est pas la cause unique de l'expansion du paysage de vulnérabilités et cite quatre facteurs concurrents. Il se conclut sur Sonatype Guide, qui porte cette intelligence au point de sélection, et renvoie au rapport complet, *The AI-Era Software Assembly Line*, pour les données sous-jacentes.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Sonatype | ORGANISATION | publie | Securing Software at the Speed of AI | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Aaron Linskens | PERSONNE | a_créé | Securing Software at the Speed of AI | DOCUMENT | 0.94 | STATIQUE | déclaré_article |
| Sonatype Research Labs | ORGANISATION | fait_partie_de | Sonatype | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Sonatype Research Labs | ORGANISATION | mesure | vulnérabilités Critical/High par application ×4,31 entre juin 2022 et juin 2026 | MESURE | 0.94 | STATIQUE | déclaré_article |
| Sonatype Research Labs | ORGANISATION | mesure | 14,14 vulnérabilités Critical/High par application en juin 2022, 54,3 en 2026 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Sonatype Research Labs | ORGANISATION | mesure | versions de composants nouvellement affectées à 46× le rythme d'avant l'IA | MESURE | 0.90 | STATIQUE | déclaré_article |
| Sonatype Research Labs | ORGANISATION | mesure | âge médian des Critical/High non résolues de 228 à 126 jours, puis 103 jours en mai 2026 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Sonatype Research Labs | ORGANISATION | mesure | création mensuelle moyenne d'applications d'entreprise ×4,84 | MESURE | 0.90 | STATIQUE | déclaré_article |
| Sonatype Research Labs | ORGANISATION | mesure | une version moins risquée était déjà disponible dans 62,2 % des cas sur Maven, 46,9 % sur npm, 34,3 % sur PyPI | MESURE | 0.93 | STATIQUE | déclaré_article |
| cohorte fixe d'applications | METHODOLOGIE | permet | isoler l'évolution du parc plutôt que celle du portefeuille clients | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Securing Software at the Speed of AI | DOCUMENT | affirme_que | la remédiation s'accélère alors que le risque accumulé par application augmente | AFFIRMATION | 0.94 | STATIQUE | déclaré_article |
| Securing Software at the Speed of AI | DOCUMENT | affirme_que | le profil de sécurité d'une application change sans que son code change | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Aaron Linskens | PERSONNE | affirme_que | l'IA n'est pas la cause unique de l'expansion du paysage de vulnérabilités | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Aaron Linskens | PERSONNE | affirme_que | l'écart de version relève d'un défaut d'information, pas d'une faute de développeur | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| sélection de composant | CONCEPT | réduit | travail de remédiation en aval | CONCEPT | 0.89 | ATEMPOREL | déclaré_article |
| Aaron Linskens | PERSONNE | recommande | déplacer la question du délai de correction vers le choix de la dépendance | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Sonatype Guide | TECHNOLOGIE | s_applique_à | point de sélection du composant, y compris dans les flux assistés par IA | CONCEPT | 0.91 | DYNAMIQUE | déclaré_article |
| assistants de codage IA | TECHNOLOGIE | utilise | intelligence courante sur le risque et la politique, non figée dans le modèle | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| The AI-Era Software Assembly Line | DOCUMENT | est_basé_sur | cohorte fixe d'applications | METHODOLOGIE | 0.89 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Sonatype | ORGANISATION | secteur | Éditeur de sécurité de la chaîne d'approvisionnement logicielle | AJOUT |
| Aaron Linskens | PERSONNE | rôle | Technical writer chez Sonatype, auteur du billet | AJOUT |
| Sonatype Research Labs | ORGANISATION | apport | Étude longitudinale sur 49 mois (juin 2022 — juin 2026) d'une cohorte fixe d'applications d'entreprise | AJOUT |
| Securing Software at the Speed of AI | DOCUMENT | format | Billet de blog ~1 300 mots restituant l'étude, publié le 18 août 2026 | AJOUT |
| The AI-Era Software Assembly Line | DOCUMENT | rôle | Rapport complet portant les données sous-jacentes, non reproduites dans le billet | AJOUT |
| cohorte fixe d'applications | METHODOLOGIE | définition | Même ensemble d'applications suivi en continu, pour que les variations reflètent le parc et non le portefeuille clients ; effectif non communiqué | AJOUT |
| sélection de composant | CONCEPT | rôle | Point d'appui amont : décider de la version avant que le risque n'entre dans l'application | AJOUT |
| Sonatype Guide | TECHNOLOGIE | fonction | Porte l'intelligence de composant (risque, versions plus sûres, politique) au moment du choix, y compris pour les assistants IA | AJOUT |
| Maven | TECHNOLOGIE | mesure | Version moins risquée déjà disponible dans 62,2 % des sélections vulnérables | AJOUT |
| npm | TECHNOLOGIE | mesure | Version moins risquée déjà disponible dans 46,9 % des sélections vulnérables | AJOUT |
| PyPI | TECHNOLOGIE | mesure | Version moins risquée déjà disponible dans 34,3 % des sélections vulnérables | AJOUT |
