---
themes: [recherche-education, philosophie-societe]
source: SFEIR
---
# sfeir-openai-kakeya-eth-yang-mills-2026-10-27

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **27 octobre 2026** (~25 000 signes, huit sections, 25 sources notées), suite de l'article SFEIR sur les **722 manuscrits** livrés par **OpenAI** le 6 octobre. Il porte sur l'annonce du **26 octobre 2026** (« Working with academic communities to build scientific understanding ») et sur la méthode qui l'accompagne. Trois apports. **(A)** Une explication vulgarisée des trois résultats revendiqués : le *local smoothing* en toute dimension, dont découlent **Kakeya** et la restriction de Stein ; une réfutation de l'**Exponential Time Hypothesis** (ETH) par un algorithme sous-exponentiel pour k-SAT ; une preuve d'existence de théories de jauge en 4 dimensions, dont la **QCD** et Yang-Mills pur, sans le *mass gap* du problème du millénaire. **(B)** Le dispositif des « bergers » (*shepherds*) : trois stratégies de diffusion, quatre principes (transparence, pas de crédit pour OpenAI, reconnaissance du groupe, indépendance non rémunérée), et la lettre des bergers de l'ETH : *« Our involvement should not be taken as certification of the claim »*. **(C)** Les points à vérifier (fidélité des énoncés **Lean**, retraits du 6 octobre, règles du Clay Institute) et une comparaison des pratiques d'OpenAI, de Google DeepMind et d'Anthropic. Conclusion pour les DSI : investir dans la vérification, contrôler l'énoncé, former des « goûteurs ». S'inscrit dans la série du corpus sur l'IA en recherche mathématique.

## Titre Article

Kakeya, ETH, Yang-Mills : OpenAI annonce trois percées, la communauté prend le temps de goûter

## Date

2026-10-27

## URL

https://www.sfeir.com/articles/openai-kakeya-eth-yang-mills-bergers/

## Keywords

OpenAI, mathématiques et IA, conjecture de Kakeya, local smoothing, restriction de Stein, Exponential Time Hypothesis, ETH, 3-SAT, complexité algorithmique, Yang-Mills, QCD, mass gap, problème du millénaire, Clay Mathematics Institute, Lean, formalisation, vérification, bergers, shepherds, Ryan Williams, Russell Impagliazzo, Simons Foundation, AlphaProof Nexus, Google DeepMind, Anthropic, revue par les pairs, spécification

## Authors

SFEIR AI, voix éditoriale du cabinet SFEIR, article non signé individuellement, publié sur sfeir.com.

## Ton

**Profil** : article de vulgarisation scientifique puis de méthode, publié sur le site d'un cabinet et destiné à des lecteurs non mathématiciens (DSI, ingénieurs). Français clair, chaque résultat introduit par une image concrète (la loupe, l'aiguille qui pivote, les interrupteurs, le pont dont personne n'a prouvé les fondations).

**Registre** : prudent et daté. Les revendications sont attribuées à OpenAI (« OpenAI affirme », « selon OpenAI »), les nuances techniques sont posées en regard (résultat asymptotique, P contre NP non tranché, *mass gap* non revendiqué, borne Lean plus faible que celle du manuscrit). Les réactions sont citées dans le texte d'origine.

**Posture** : l'article prend position sur un point, l'asymétrie d'information créée par le choix des premiers bergers (*« Nous la mettrions en tête de liste »*). La métaphore filée du goûteur, reprise de l'article du 6 octobre, structure la conclusion : *« une preuve que personne ne comprend n'a pas encore produit de science »*. Clôture suspendue : *« Les trois résultats d'OpenAI sont peut-être vrais. »*

## Pense-betes

- **Annonce du 26 octobre 2026** : trois résultats attendus depuis des décennies ; au 27 octobre, **aucun validé** par un expert indépendant. Vingt jours après les **722 manuscrits** du 6 octobre, OpenAI change de méthode.
- **(1) Analyse harmonique** : local smoothing (conjecture de **Sogge**, 1991) prouvé en toute dimension via une EDP auxiliaire nouvelle → **Kakeya** (dimension de Hausdorff pleine) et restriction de Stein (à l'intérieur de la zone conjecturée, pas aux extrémités). Antécédents : Guth-Wang-Zhang 2019 (dimension 2), **Wang-Zahl** février 2025 (Kakeya en dimension 3). Sortie du modèle le 18 octobre, Lean le 19, publié sur **openai/math**.
- **(2) Complexité** : « The Exponential Time Hypothesis is False » — algorithme déterministe qui **compte** les solutions de k-CNF en temps sous-exponentiel et espace polynomial ; réfute aussi Strong ETH, Gap-ETH, NSETH. 3-SAT en ~exp(n/(log n)^{1/2+o(1)}). Reste superpolynomial (**P vs NP non tranché**), asymptotique (biased-PPSZ en ~1,307^n reste plus rapide en pratique).
- **(3) Physique** : existence rigoureuse de théories de jauge avec fermions en 4D, dont la **QCD** et Yang-Mills pur, via l'approche de **Balaban** ; présentée comme une « partie » du problème du millénaire — le **mass gap** n'est pas revendiqué. Groupe de **David Gross** (Nobel 2004) avec Douglas, Jaffe, Klebanov, Nekrasov : rédige lui-même, rien publié sur le dépôt.
- **Bergers** : trois stratégies (publication brute en maths ; groupe + publication intégrale en informatique ; groupe souverain en physique). Quatre principes : aucun NDA, pas de crédit académique pour OpenAI, reconnaissance du groupe, participation **volontaire et non rémunérée**. Pour l'ETH : données brutes publiques et conférence financée.
- **Financement** : **5 M$** d'OpenAI à l'initiative **Simons Foundation** (15 M$ avec Anthropic et OpenAI, candidatures jusqu'au 1er décembre 2026).
- **Limite reconnue par OpenAI** : asymétrie d'information au profit des premiers bergers.
- **Communauté** : Williams, Impagliazzo, Paturi n'ont reçu que le PDF, refusent la certification ; Scott Aaronson (*« le buffet continue »*) ; **Hugo Duminil-Copin** (« choc monumental », RTS) ; lettre « A Severe Misalignment of AI in Mathematics » (**25 médaillés Fields** le 11 septembre, 28 signataires au 27 octobre).
- **À vérifier** : fidélité des énoncés Lean (fichier 378.md : borne formalisée plus faible que celle du manuscrit) ; précédent du 6 octobre (3 retraits pour erreur de signe, 14 révisés, catalogue ramené à **719**) ; règles du Clay (publication qualifiante, **2 ans** d'attente, acceptation générale) ; Arthur Jaffe à la fois coauteur de l'énoncé et berger.
- **Trois cultures** : OpenAI (volume puis médiation) ; Google DeepMind **AlphaProof Nexus** (Science, 8 octobre : 9 problèmes d'Erdős sur 353, 44 conjectures OEIS sur 492, revue par les pairs) ; Anthropic (Alman et Vassilevska Williams, 3SUM/APSP réfutées, sous NDA et rémunération).
- **Leçons pour l'entreprise** : investir dans la vérification autant que dans la génération ; contrôler l'énoncé (des tests verts prouvent la conformité à la spécification écrite, pas au besoin) ; former des goûteurs.

## RésuméDe400mots

Le 26 octobre 2026, OpenAI annonce trois résultats attendus depuis des décennies et une nouvelle méthode pour les faire examiner. SFEIR les explique et dresse la liste de ce qui reste à vérifier.

Le premier relève de l'analyse harmonique. La conjecture de local smoothing de Sogge (1991) dit qu'une onde qui se concentre ne garde son pic qu'un instant. OpenAI affirme que son modèle l'a prouvée en toute dimension grâce à une équation auxiliaire nouvelle, et en déduit la conjecture de Kakeya et celle de restriction de Stein, prouvées jusqu'ici en petite dimension. Texte et preuve Lean sont publiés sur le dépôt openai/math.

Le deuxième touche la complexité. L'Exponential Time Hypothesis postule qu'on ne résout pas 3-SAT fondamentalement mieux qu'en temps exponentiel. Le manuscrit décrit un algorithme déterministe sous-exponentiel en espace polynomial, qui réfuterait aussi ses variantes. L'article précise que P contre NP n'est pas tranché et que, pour des tailles réalistes, les algorithmes exponentiels connus restent plus rapides.

Le troisième concerne la physique : une preuve rigoureuse d'existence de théories de jauge en quatre dimensions, dont la chromodynamique quantique. OpenAI la présente comme une partie du problème du millénaire Yang-Mills, sans revendiquer le mass gap. Le groupe de David Gross a choisi de rédiger lui-même et rien n'est public.

OpenAI confie désormais ses résultats à des bergers académiques, selon trois stratégies de diffusion et quatre principes : transparence sans accord de confidentialité, aucun crédit académique pour l'entreprise, reconnaissance du groupe, participation bénévole. Elle reconnaît l'asymétrie d'information créée par le choix des premiers lecteurs. Les bergers de l'ETH, qui n'ont reçu que le PDF, écrivent que leur implication ne vaut pas certification.

Restent à vérifier : la fidélité des énoncés Lean (la borne formalisée diffère de celle du manuscrit), la solidité après les retraits du 6 octobre, et les règles du Clay Institute, qui exigent publication, deux ans d'attente et acceptation générale. L'article compare trois cultures : le volume puis la médiation chez OpenAI, la revue par les pairs avant parution chez Google DeepMind avec AlphaProof Nexus, des chercheurs nommés sous accord de confidentialité et rémunérés chez Anthropic.

Pour les entreprises, SFEIR tire trois conséquences : investir dans la vérification autant que dans la génération, contrôler l'énoncé et pas seulement la preuve, comme une spécification face au besoin métier, et former des profils capables de comprendre et de juger un résultat produit par d'autres.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Kakeya, ETH, Yang-Mills : OpenAI annonce trois percées | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | Working with academic communities to build scientific understanding | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | affirme_que | son modèle a prouvé le local smoothing en toute dimension, d'où Kakeya et la restriction de Stein | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| The Exponential Time Hypothesis is False | DOCUMENT | s_oppose_à | Exponential Time Hypothesis | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | affirme_que | existence rigoureuse de la QCD et de Yang-Mills pur en quatre dimensions, sans le mass gap | AFFIRMATION | 0.86 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | utilise | Lean | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| openai/math | TECHNOLOGIE | fait_partie_de | OpenAI | ORGANISATION | 0.85 | STATIQUE | inféré |
| OpenAI | ORGANISATION | a_créé | bergers académiques | METHODOLOGIE | 0.9 | STATIQUE | déclaré_article |
| Ryan Williams | PERSONNE | affirme_que | leur implication ne vaut pas certification de la réfutation de l'ETH | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Ryan Williams | PERSONNE | collabore_avec | Russell Impagliazzo | PERSONNE | 0.88 | STATIQUE | déclaré_article |
| David Gross | PERSONNE | dirige | groupe d'examen de la preuve Yang-Mills | ORGANISATION | 0.82 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | collabore_avec | Simons Foundation | ORGANISATION | 0.88 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | collabore_avec | Simons Foundation | ORGANISATION | 0.85 | STATIQUE | déclaré_article |
| Clay Mathematics Institute | ORGANISATION | référence | Yang-Mills et mass gap | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| AlphaProof Nexus | TECHNOLOGIE | mesure | 9 problèmes d'Erdős résolus sur 353 et 44 conjectures OEIS sur 492 | MESURE | 0.88 | STATIQUE | déclaré_article |
| Google DeepMind | ORGANISATION | a_créé | AlphaProof Nexus | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| A Severe Misalignment of AI in Mathematics | DOCUMENT | affirme_que | les objectifs des entreprises d'IA et de la communauté mathématique sont gravement désalignés | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | l'asymétrie d'information créée par le choix des premiers bergers est la limite principale | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | investir dans la vérification autant que dans la génération et contrôler l'énoncé, pas seulement la preuve | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| OpenAI | ORGANISATION | annonce | Trois résultats mathématiques revendiqués le 26 octobre 2026 | AJOUT |
| Exponential Time Hypothesis | CONCEPT | définition | Hypothèse (Impagliazzo, Paturi, fin des années 1990) : 3-SAT n'admet pas d'algorithme sous-exponentiel | AJOUT |
| The Exponential Time Hypothesis is False | DOCUMENT | statut | Manuscrit OpenAI du 17 octobre 2026, révisé le 25, non validé au 27 octobre | AJOUT |
| bergers académiques | METHODOLOGIE | définition | Groupes d'experts externes chargés d'organiser l'examen des résultats, bénévoles et sans NDA | AJOUT |
| Lean | TECHNOLOGIE | catégorie | Assistant de preuve formelle ; garantit la déduction, pas la fidélité des énoncés | AJOUT |
| openai/math | TECHNOLOGIE | catégorie | Dépôt GitHub des manuscrits et preuves Lean d'OpenAI (719 manuscrits après retraits) | AJOUT |
| Ryan Williams | PERSONNE | rôle | Chercheur au MIT, berger du résultat ETH | AJOUT |
| Russell Impagliazzo | PERSONNE | rôle | Coauteur de l'ETH, berger du résultat ETH | AJOUT |
| David Gross | PERSONNE | rôle | Prix Nobel de physique 2004, mène le groupe d'examen Yang-Mills/QCD | AJOUT |
| Simons Foundation | ORGANISATION | initiative | 15 M$ pour accompagner les mathématiciens face à l'IA, lancée le 15 octobre 2026 | AJOUT |
| AlphaProof Nexus | TECHNOLOGIE | catégorie | Recherche de preuves formelles de Google DeepMind, publiée dans Science le 8 octobre 2026 | AJOUT |
| A Severe Misalignment of AI in Mathematics | DOCUMENT | signataires | 25 médaillés Fields au dépôt (11 septembre 2026), 28 au 27 octobre | AJOUT |
