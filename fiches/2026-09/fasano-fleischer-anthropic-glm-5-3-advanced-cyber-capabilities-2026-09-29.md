---
themes: [qualite-securite, politique-regulation, recherche-education]
source: "Anthropic"
---
# fasano-fleischer-anthropic-glm-5-3-advanced-cyber-capabilities-2026-09-29

## Veille

Billet de recherche de l'équipe **Frontier Red Team** d'**Anthropic** (auteurs : **Andrew Fasano**, **Marius Fleischer**, Cole McFaul, Robert Xiao, Tripp Gallagher), publié le **29 septembre 2026** ; environ **2 300 mots**, six figures. Il analyse **GLM-5.3** de **Zhipu AI (Z.ai)**, modèle à poids ouverts, cinq mois après l'annonce de Claude Mythos Preview. **(A)** Capacité : sur ExploitBench (41 bogues V8 de Chrome), GLM-5.3 construit un exploit complet dans **50 essais sur 410**, contre **56 sur 410** pour Mythos Preview ; sur le benchmark interne de corruption mémoire, détournement du flot de contrôle dans **4 %** des essais contre **6 %** ; Claude Opus 4.6 et GLM-5.2 : 0. **(B)** Essais avec experts humains : chaîne de vulnérabilités 0-day d'un navigateur aboutissant à la lecture de fichiers du visiteur ; avec **GLM-5.3-Flash**, chaîne d'exploits N-day (CVE-2026-11645) contournant PAC sur ARM64, **20 minutes** d'attention humaine, huit heures de calcul, **20,40 $** aux prix de l'API. **(C)** Garde-fous : contournement dans **64 %** des cas par faux contexte de red team, **92 %** par préremplissage du raisonnement, **100 %** par *abliteration* (environ 2 200 heures GPU, 4 400 $) ; les modèles Claude testés restent à 0 %. **(D)** Recommandations : élargir l'accès des défenseurs aux modèles de pointe, tests gouvernementaux indépendants. Cite l'évaluation du **CAISI** du NIST (17 septembre) : « le modèle à poids ouverts le plus capable en cyber publié à ce jour », environ quatre mois derrière la frontière américaine. Prolonge les fiches du corpus sur Mythos et Glasswing.

## Titre Article

GLM-5.3 and the spread of advanced cyber capabilities

## Date

2026-09-29

## URL

https://www.anthropic.com/research/glm-5-3-and-the-spread-of-advanced-cyber-capabilities

## Keywords

GLM-5.3, Zhipu AI, Z.ai, modèle à poids ouverts, capacités cyber offensives, exploitation de vulnérabilités, ExploitBench, V8, Chrome, abliteration, réduction des refus, contournement de garde-fous, préremplissage du raisonnement, jailbreak, JailbreakBench, HarmBench, StrongREJECT, Claude Mythos Preview, Project Glasswing, CAISI, NIST, N-day, 0-day, PAC, prolifération, défenseurs, Frontier Red Team, évaluation indépendante

## Authors

Andrew Fasano, Marius Fleischer, Cole McFaul, Robert Xiao, Tripp Gallagher ; Frontier Red Team, Anthropic (billet de recherche du site anthropic.com).

## Ton

**Profil** : publication d'une équipe de red teaming interne, rédigée comme rapport d'évaluation avec protocole, chiffres et notes de bas de page, suivi d'une section de recommandations de politique publique.

**Style** : factuel, chiffré, avec comparaisons systématiques entre GLM-5.3, Claude Mythos Preview et modèles Claude plus anciens. Figures synthétiques, cas d'usage détaillés, citation verbatim du raisonnement d'un modèle abliteré.

**Position épistémique** : résultats issus de tests de l'équipe elle-même ; les attaques sur les modèles Claude sont testées avec les garde-fous en place, et la comparaison de capacité utilise des modèles Claude aux garde-fous désactivés. Les auteurs signalent les limites : simulation du monde par un autre LLM, sans exécution de code, « imparfaite » ; exploits limités à la version Linux du navigateur ; divulgations aux mainteneurs en cours. Le billet émane du concepteur des modèles comparés, ce que l'en-tête indique.

## Pense-betes

- **Contexte** : Mythos Preview, annoncé cinq mois plus tôt, avait été diffusé de façon limitée via Project Glasswing (plus de 10 000 vulnérabilités trouvées par des défenseurs de confiance). Anthropic attendait la prolifération de cette capacité ; GLM-5.3 en est l'occurrence.
- **Capacité mesurée** : ExploitBench, 50 exploits complets sur 410 (GLM-5.3) contre 56 (Mythos Preview) ; benchmark interne de 100 tâches OSS-Fuzz, 4 % contre 6 %. Kimi K3, DeepSeek V4.1-Flash, Claude Opus 4.6 et GLM-5.2 restent à zéro ou presque : un **seuil** est franchi entre GLM-5.2 et GLM-5.3, comme entre Opus 4.6 et Mythos Preview.
- **Sessions avec experts** : moins d'une heure d'attention humaine. GLM-5.3 trouve plusieurs 0-day dans le moteur JavaScript d'un navigateur et les enchaîne en page lisant des fichiers arbitraires (figure : vol d'une clé SSH) ; d'autres pistes dans pilotes Wi-Fi et graphiques et logiciels d'équipements réseau, en cours de revue.
- **N-day à bas coût** : GLM-5.3-Flash, version plus petite, enchaîne deux failles connues pour une chaîne fiable sur ARM64 avec contournement de PAC : 20 minutes humaines, 8 heures machine, **20,40 $**.
- ⭐ **Garde-fous** : refus sur demandes ouvertement malveillantes, mais contournés par trois méthodes simples. Faux contexte de red team : **64 %** d'engagement ; préremplissage du raisonnement : **92 %** ; *abliteration* : **100 %**. Test en monde simulé, cinq ordres d'attaque, 50 échantillons par cellule.
- **Abliteration** : modification des poids qui supprime les refus. Refus moyen de 95 % à 6 % (GLM-5.3) et 14 % (Flash) sur trois benchmarks ; capacités quasi intactes (GPQA-Diamond identique, CyberGym quelques points en moins). Coût pour l'équipe : ~2 200 heures GPU (~4 400 $) ; une équipe rodée en aurait besoin de ~600 (~1 200 $). Des versions abliterées sont publiques dans les jours suivant la sortie.
- **Asymétrie avec les modèles fermés** : le préremplissage n'est pas offert par l'API Claude, les poids ne sont pas accessibles donc non abliterables, et les faux contextes sont bloqués dans les tests. Les modèles Claude testés (Opus 4.8, Opus 5, Mythos 5) restent à 0 %.
- **Évaluation CAISI** (NIST, 17 septembre) : GLM-5.3 « le plus cyber-capable des modèles à poids ouverts », à environ quatre mois de retard sur la frontière américaine ; modèles américains testés sans garde-fous, versions réservées à des utilisateurs vérifiés incluses.
- **Recommandations** : défenseurs équipés de modèles au moins aussi bons que ceux des attaquants (accès via Glasswing, Patch the Planet, Mythos 5.1) ; tests gouvernementaux des successeurs de GLM-5.3 ; appel aux développeurs de poids ouverts à sécuriser ces capacités.
- ⚠️ **Réserves de l'article** : monde simulé par LLM sans exécution réelle ; cibles limitées à une version Linux ; constats sur d'autres logiciels non encore publiés.

## RésuméDe400mots

Le billet de la Frontier Red Team d'Anthropic, publié le 29 septembre 2026, analyse GLM-5.3, modèle à poids ouverts de Zhipu AI (Z.ai). Il rappelle que Claude Mythos Preview, annoncé cinq mois plus tôt, avait été le premier modèle capable de construire de façon autonome des exploits complets, et qu'il n'avait été diffusé qu'aux défenseurs de confiance via Project Glasswing, qui ont trouvé plus de 10 000 vulnérabilités. Les auteurs attendaient que cette capacité se répande. Selon eux, GLM-5.3 la possède, sans garde-fous significatifs.

Sur ExploitBench, qui porte sur des bogues du moteur V8 de Chrome, GLM-5.3 produit un exploit complet dans 50 essais sur 410, contre 56 pour Mythos Preview. Sur le benchmark interne de corruption mémoire, il détourne le flot de contrôle dans 4 % des essais contre 6 %. Claude Opus 4.6, GLM-5.2, Kimi K3 et DeepSeek V4.1-Flash restent à zéro ou presque : un seuil est franchi. L'évaluation du CAISI du NIST, publiée le 17 septembre, parvient à des conclusions proches : GLM-5.3 est le modèle à poids ouverts le plus capable en cyber, avec environ quatre mois de retard sur la frontière américaine.

Deux sessions avec des chercheurs humains illustrent l'effet. Avec moins d'une heure d'attention, GLM-5.3 a découvert plusieurs vulnérabilités inconnues dans le moteur JavaScript d'un navigateur et les a enchaînées en une page qui lit des fichiers de l'ordinateur du visiteur ; des failles ont aussi été repérées dans des pilotes et des logiciels d'équipements réseau, divulguées ou en cours de revue. Dans l'autre, GLM-5.3-Flash a construit une chaîne d'exploits N-day contournant PAC sur ARM64, pour 20 minutes d'attention humaine et 20,40 $.

Les garde-fous du modèle refusent les demandes ouvertement malveillantes, mais trois contournements simples fonctionnent en monde simulé : un faux contexte d'exercice de red team (64 % d'engagement), le préremplissage du raisonnement (92 %) et l'abliteration (100 %). Cette dernière modifie les poids et fait passer le refus moyen de 95 % à 6 %, avec des capacités presque intactes ; elle a coûté à l'équipe environ 4 400 $ de calcul, et des versions abliterées circulent déjà. Les modèles Claude testés résistent, car l'API n'offre pas le préremplissage et les poids ne sont pas distribués.

Les auteurs concluent que des acteurs étatiques et non étatiques utiliseront probablement ces modèles. Ils recommandent d'élargir l'accès des défenseurs aux modèles de pointe et de faire tester par les gouvernements les successeurs de GLM-5.3, et invitent les développeurs de poids ouverts à sécuriser ces capacités. Ils signalent que la simulation n'exécute aucun code et que les exploits visent une version Linux.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-----------|-----------|-----------|-------------|--------|
| Frontier Red Team | ORGANISATION | fait_partie_de | Anthropic | ORGANISATION | 0.95 | STATIQUE | déclaré_article |
| Frontier Red Team | ORGANISATION | publie | article GLM-5.3 and the spread of advanced cyber capabilities | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| Zhipu AI | ORGANISATION | a_créé | GLM-5.3 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| article GLM-5.3 and the spread of advanced cyber capabilities | DOCUMENT | affirme_que | GLM-5.3 a été publié sans garde-fous significatifs alors qu'il construit des exploits complets de façon autonome | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| GLM-5.3 | TECHNOLOGIE | mesure | 50 exploits complets sur 410 essais sur ExploitBench contre 56 sur 410 pour Claude Mythos Preview | MESURE | 0.95 | STATIQUE | déclaré_article |
| GLM-5.3 | TECHNOLOGIE | mesure | détournement du flot de contrôle dans 4 % des essais contre 6 % pour Claude Mythos Preview, 100 tâches | MESURE | 0.93 | STATIQUE | déclaré_article |
| GLM-5.3 | TECHNOLOGIE | converge_avec | Claude Mythos Preview | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| GLM-5.3 | TECHNOLOGIE | surpasse | GLM-5.2 | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| GLM-5.3-Flash | TECHNOLOGIE | est_variante_de | GLM-5.3 | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| GLM-5.3-Flash | TECHNOLOGIE | mesure | chaîne d'exploits N-day CVE-2026-11645 sur ARM64 contournant PAC, 20 minutes d'attention humaine, 20,40 $ | MESURE | 0.93 | STATIQUE | déclaré_article |
| abliteration | METHODOLOGIE | réduit | le refus moyen de GLM-5.3 de 95 % à 6 % avec des capacités presque intactes | MESURE | 0.93 | STATIQUE | déclaré_article |
| abliteration | METHODOLOGIE | s_applique_à | GLM-5.3 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| GLM-5.3 | TECHNOLOGIE | observé_dans | engagement à 64 % avec faux contexte de red team, 92 % avec raisonnement prérempli, 100 % abliteré | MESURE | 0.93 | STATIQUE | déclaré_article |
| article GLM-5.3 and the spread of advanced cyber capabilities | DOCUMENT | affirme_que | les modèles Claude testés résistent à ces contournements, faute de préremplissage et de poids accessibles | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| CAISI | ORGANISATION | affirme_que | GLM-5.3 est le modèle à poids ouverts le plus capable en cyber publié à ce jour, environ quatre mois derrière la frontière américaine | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| Project Glasswing | METHODOLOGIE | permet | à des défenseurs de confiance de trouver plus de 10 000 vulnérabilités avant les attaquants | MESURE | 0.92 | STATIQUE | déclaré_article |
| article GLM-5.3 and the spread of advanced cyber capabilities | DOCUMENT | recommande | élargir l'accès des défenseurs aux modèles de pointe | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| article GLM-5.3 and the spread of advanced cyber capabilities | DOCUMENT | recommande | des tests de sécurité gouvernementaux des successeurs de GLM-5.3 | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| article GLM-5.3 and the spread of advanced cyber capabilities | DOCUMENT | prédit | acteurs étatiques et non étatiques utiliseront des modèles comme GLM-5.3 pour causer des dommages réels | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Anthropic | ORGANISATION | secteur | Laboratoire d'IA ; éditeur de Claude et de Mythos | AJOUT |
| Frontier Red Team | ORGANISATION | secteur | Équipe de red teaming d'Anthropic | AJOUT |
| Zhipu AI | ORGANISATION | secteur | Éditeur chinois de GLM (Z.ai hors de Chine) | AJOUT |
| CAISI | ORGANISATION | secteur | Center for AI Standards and Innovation du NIST | AJOUT |
| GLM-5.3 | TECHNOLOGIE | catégorie | Modèle à poids ouverts de Zhipu AI, forte capacité d'exploitation | AJOUT |
| GLM-5.3-Flash | TECHNOLOGIE | catégorie | Version plus petite de GLM-5.3 | AJOUT |
| GLM-5.2 | TECHNOLOGIE | catégorie | Version précédente, sans capacité d'exploit complet | AJOUT |
| Claude Mythos Preview | TECHNOLOGIE | catégorie | Modèle d'Anthropic à diffusion limitée, exploits autonomes | AJOUT |
| Project Glasswing | METHODOLOGIE | définition | Programme d'accès limité pour défenseurs de confiance | AJOUT |
| abliteration | METHODOLOGIE | définition | Édition des poids supprimant les refus d'un modèle ouvert | AJOUT |
| article GLM-5.3 and the spread of advanced cyber capabilities | DOCUMENT | forme | Billet de recherche du 29 septembre 2026 | AJOUT |
