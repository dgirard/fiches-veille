---
themes: [qualite-securite, strategie-frameworks, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-code-review-anneau-contraintes-2026-07-30

## Veille

Épisode « Phase 5 · Review » de la série SFEIR sur le SDLC augmenté, publié **le jour même** du post LinkedIn d'Addy Osmani qu'il traduit en spécification de phase. Thèse : **la qualité a changé d'adresse** — elle ne se lit plus dans le code (les agents en produisent plus que personne ne peut relire) mais dans **l'anneau de contraintes qui entoure l'agent**. L'anneau d'Osmani (sept dimensions — correction, sécurité, performance, accessibilité, maintenabilité, **efficience économique**, **compréhensibilité** — reliées par la règle de **back-pressure** : « on ne confie à une boucle que l'autonomie qu'on sait vérifier à faible coût et de façon fiable, pas un pouce de plus ») est redessiné, traduit et rattaché à la phase 5 du cycle SFEIR à 11 phases. Le corollaire structurant : **le goulot n'a jamais été la génération, c'est la vérification** — « la génération est une bouche large, la vérification un col étroit ; accélérer la bouche épaissit le tas au col ». **La décision de conception la plus intéressante est un choix d'architecture de cycle** : Review est délibérément **hors des trois gates humains** (Define, Plan, Ship), parce que faire porter le gate à Review reviendrait à mettre l'attention humaine — ressource finie — en point de contrôle d'une capacité de génération qui, elle, scale : « vous auriez bâti un pipeline dont le débit maximal est le nombre de diffs qu'un senior peut lire avant la fin de la journée ». D'où le partage : **Review instrumente, Ship décide** — Review livre un *faisceau de preuves opposable*, Ship décide sur les preuves, pas sur le diff intégral. Position située face à Monperrus (dont SFEIR retient le diagnostic — l'inspection humaine de chaque diff ne résiste pas à la vitesse agentique — mais refuse la conclusion : l'acceptation ne se délègue pas). Le piège nommé est **la validation circulaire** (l'agent qui écrit le code écrit les tests qui le valident : « vous avez construit un miroir, pas un anneau »), avec cinq contre-mesures reprises d'Anthropic (gates indépendants en fenêtres de contexte séparées, déterministe + agentique jamais l'un à la place de l'autre, mode ombre, tiering par risque, journalisation vers le SIEM) et l'avertissement de Compare the Market (**graphe AST ~70 % vs RAG vectoriel ~58 %**, le RAG faisant *pire que pas de contexte du tout*). Le prolongement propre au cabinet est **le cliquet** : « toute échappée devient une contrainte » — un défaut qui a franchi l'anneau se referme *dans l'anneau* (test, règle de lint, rubrique, garde-fou de harnais) au Compound-1, « le seul actif de la chaîne qui s'apprécie pendant que les modèles se déprécient » (mesure interne non auditable : **− 30 % d'itérations de correction après dix cycles**). Clôture par la reformulation de la question : « ce code est-il bon ? » est devenu insoluble ; reste **« qu'est-ce que mon système refuse de laisser passer ? »**

## Titre Article

Code review dans le SDLC augmenté : l'anneau de contraintes autour des agents

## Date

2026-07-30

## URL

https://www.sfeir.com/articles/sdlc-ai-review-anneau-contraintes/

## Keywords

anneau de contraintes, constraints around agents, phase Review, phase 5, SDLC augmenté, cycle SFEIR à 11 phases, gates humains, Define Plan Ship, Review instrumente Ship décide, faisceau de preuves opposable, back-pressure, autonomie ≤ vérifiabilité, vérifiabilité à faible coût, goulot de vérification, bouche large col étroit, plus de code que vous ne pouvez lire, Addy Osmani, harnais, harness engineering, Software Factories Light and Dark, usine sans lumière, lights-out factory, sept dimensions de contrainte, correction, tests de propriété, tests de mutation, oracle vert/rouge, sécurité, SAST, DAST, scan de dépendances, détection de secrets, performance, budget de performance, tests de charge, SLO, accessibilité, axe, contraste, navigation clavier, maintenabilité, couverture, complexité, rayon d'impact, frontières de composants, dette architecturale, efficience économique, budget tokens, coût par changement, FinOps token, TCO, CapEx OpEx, compréhensibilité, comprehension debt, dette de compréhension, journal de décision, decision log attaché à la PR, l'intention n'est pas perdue elle est jetée, Martin Monperrus, fin de la revue de code, fausse sécurité, du créateur au vérificateur, validation circulaire, circular validation, miroir, Augment Code, Paula Hingel, DORA 2025, débit vs stabilité, Anthropic, Jason Clinton, 80 % du code fusionné, gates indépendants, fenêtres de contexte séparées, déterministe et agentique, mode ombre, shadow mode, red team, base de code tiérée par le risque, échantillonnage pondéré par le risque, journalisation SIEM, 16 % à 54 %, un tiers des incidents, que ferions-nous tourner si scanner ne coûtait presque rien, Compare the Market, récupération de contexte, graphe de connaissance structurel, analyse AST, 70 % vs 58 %, 79 merge requests, RAG vectoriel, compréhension structurelle, appelants signatures hiérarchies, cliquet, ratchet, toute échappée devient une contrainte, un bug vu deux fois est un trou dans le système, Compound-1, capitalisation des leçons statiques, mémoire rechargée au Plan, − 30 % d'itérations de correction, dix cycles, où placer l'interrupteur, lumières éteintes, contrôle peu coûteux haute fréquence difficile à contourner immédiat non dérivant, boucles courtes, trois à dix étapes, accumulation de contexte, authentification facturation contrat d'API public, sortie d'exécution vs déclaration de l'agent, contraintes que le modèle ne peut pas discuter, qu'est-ce que mon système refuse de laisser passer

## Authors

SFEIR (voix éditoriale du cabinet, article non signé individuellement) — construit sur Addy Osmani (Google) ; cite Martin Monperrus, Paula Hingel (Augment Code), DORA/Google Cloud, Jason Clinton (Anthropic), l'équipe Engineering de Compare the Market

## Ton

**Profil** : article de doctrine à usage opérationnel, épisode d'une série numérotée (« Phase 5 · Review »). Public : directions d'ingénierie, architectes, RSSI qui outillent déjà des agents et cherchent où poser les contrôles. Registre professionnel dense, français soigné, zéro jargon non défini, aucun anglicisme laissé sans traduction (*back-pressure* et *comprehension debt* sont gardés mais glosés).

**Style** : la **formule-couperet** en fin de paragraphe est le moteur du texte, et elle est presque toujours une image concrète plutôt qu'une abstraction — « la génération est une bouche large, la vérification un col étroit ; accélérer la bouche épaissit le tas au col » ; « vous avez construit un miroir, pas un anneau de contraintes » ; « une usine sans lumière ne rembourse pas cette dette, elle la contracte à plein régime, tests au vert » ; « l'intention n'est pas perdue, elle est jetée » ; « une boucle qui s'étale cache ses erreurs dans les coins » ; « un anneau statique est un anneau qui fuit ». Architecture rhétorique en entonnoir : un schéma emprunté → sa traduction en tableau à deux colonnes (mécanisable / irréductiblement humain) → le mode d'échec nommé → le prolongement maison → cinq questions d'auto-diagnostic → une question de clôture qui remplace la question de départ. Deux marqueurs de rigueur inhabituels dans le genre : **chaque affirmation externe porte une note numérotée** avec une étiquette de statut (*Industrie · Anthropic*, *Mesuré · SFEIR*), et le schéma central est **explicitement crédité** (« Schéma SFEIR d'après le diagramme d'Addy Osmani, © Addy Osmani, redessiné, traduit et rattaché à la phase 5 »).

**Position épistémique** : assumée comme prescriptive, mais avec deux gestes de probité. Le premier est le **désaccord explicite et argumenté** avec Monperrus : SFEIR prend son diagnostic, refuse sa conclusion, et dit pourquoi (l'acceptation ne se délègue pas — c'est le gate Ship) plutôt que de l'ignorer ou de le caricaturer. Le second est la **réserve d'usage rappelée sur les chiffres d'Anthropic** (« les chiffres viennent d'Anthropic sur elle-même »), déjà posée dans la fiche du 26 juillet. La limite du texte est symétrique de sa force : **il est publié le jour même du post d'Osmani qu'il commente**, ce qui laisse peu de place à l'épreuve du temps ou à la contradiction — et son seul chiffre propre (− 30 % d'itérations après dix cycles) est first-party, non auditable, sans description de protocole ni de périmètre. Le CTA final (« Instrumenter votre phase Review avant d'ouvrir les vannes agentiques ») rappelle que la doctrine est aussi une offre.

## Pense-betes

- **Date / source** : **30 juillet 2026**, SFEIR, non signé (voix cabinet), tags `sdlc`, `ia-agentique`, `software-factory`, `harness-engineering`, `code-review`. Huit sources numérotées avec étiquettes de statut.
- **Nature** : **article de cadre**, non source primaire de résultats. Trois apports propres ; tout le reste est synthèse sourcée. Ne pas re-citer par cette fiche les chiffres d'Anthropic ou de Compare the Market — aller aux fiches sources.

### Les trois apports propres

1. **Review hors des gates humains**, avec le partage *« Review instrumente / Ship décide »*.
2. **Le rattachement du cliquet à Compound-1** comme phase qui en a explicitement la charge.
3. Le chiffre maison **− 30 %**.

### La grille dimension par dimension

Transposable telle quelle en spécification de phase Review : dimension → contrainte mécanisable → jugement humain résiduel.

| Dimension | Contrainte mécanisable | Jugement humain résiduel |
|---|---|---|
| Correction | unitaires, propriété, mutation, oracle vert/rouge | l'acceptation fonctionnelle |
| Sécurité | SAST/DAST, dépendances, secrets, revue agentique dédiée | l'arbitrage du risque résiduel |
| Performance | budget perf, charge, régression mesurée | la définition du SLO |
| Accessibilité | axe, contraste, clavier | l'expérience réellement vécue |
| Maintenabilité | couverture, complexité, rayon d'impact, frontières de composants | la dette architecturale assumée |
| Compréhensibilité | l'agent consigne ce qu'il a tenté **et ce qu'il a écarté**, journal de décision attaché à la PR | la reconstruction de l'intention |
| Efficience économique | budget tokens/compute par tâche, coût par changement | le TCO, l'arbitrage CapEx/OpEx |

Règle qui relie les sept : **back-pressure** — autonomie ≤ vérifiabilité à faible coût — dont le jugement résiduel est *où placer l'interrupteur*.

### L'argument d'architecture

Si Review portait le gate humain, *« le point de contrôle du système serait l'attention humaine, une ressource finie qui ne scale pas, face à une capacité de génération qui, elle, scale »* : le col ne s'élargirait jamais, et *« vous auriez bâti un pipeline dont le débit maximal est le nombre de diffs qu'un senior peut lire avant la fin de la journée »*. C'est ce qui justifie de **déplacer** le gate vers Ship plutôt que de supprimer l'humain. Distinction opératoire : Review a un **livrable** (un faisceau de preuves opposable), Ship a une **décision** — *« et cette décision se prend sur les preuves, pas sur le diff intégral »*.

### La dimension oubliée

La **compréhensibilité** est systématiquement omise *« parce qu'elle ne casse pas la CI »*. Le remède est le moins cher de la grille et le moins appliqué : demander à l'agent d'écrire ce qu'il a tenté et écarté, puisque *« la relecture d'une PR agentique est la première fois qu'un humain reconstruit le pourquoi »*. Formule à garder : *« l'intention n'est pas perdue, elle est jetée »*. C'est le garde-fou structurel que réclamait [[osmani-cognitive-surrender-comprehension-debt-2026-05-05]].

### La validation circulaire

L'agent écrit le code, le même agent écrit les tests, la CI est verte : *« un miroir, pas un anneau »*. Mesure du phénomène par DORA 2025 — adoption IA corrélée **positivement au débit** et **négativement à la stabilité** quand les fondations ne suivent pas. Question de diagnostic la plus rentable de l'article : *« vos tests sont-ils écrits par l'agent qui écrit le code ? »*

### Critère de qualification d'une boucle autonome

Le contrôle doit être **peu coûteux, à haute fréquence, difficile à contourner, immédiat et non dérivant**. Qualifient : oracle vert/rouge, porte de typage, tests de propriété, relecteur agentique doté d'une rubrique réelle. Corollaire : les boucles courtes se vérifient mieux que les longues — un agent tient 3 à 10 étapes et perd le fil au-delà d'une vingtaine ; *« une boucle qui s'étale cache ses erreurs dans les coins »*.

Où garder la lumière allumée : bugs subtils invisibles aux tests, rayons d'impact larges, décisions structurant un an de travail — nommément **authentification, facturation, contrat d'API public**. Avertissement de gouvernance : *« le vrai risque est de régler tous les interrupteurs pareil »* — tout éteint mène au démontage quatre mois plus tard, tout allumé à l'arrêt des livraisons.

### Le cliquet, prolongement propre à SFEIR

*« Toute échappée devient une contrainte »* : un défaut qui a franchi l'anneau ne se corrige pas seulement dans le code, il se **referme dans l'anneau** (test, règle de lint, rubrique de revue, garde-fou de harnais), au **Compound-1**, avec mémoire rechargée au Plan du cycle suivant. C'est le *ratchet principle* d'Osmani branché sur une phase du cycle qui en a la charge. Deux formules : *« une checklist s'écrit une fois et se périme, l'anneau s'épaissit à chaque cycle »* et *« un bug vu deux fois n'est pas un bug, c'est un trou dans le système »*. Argument d'investissement associé : l'anneau est *« le seul actif de la chaîne qui s'apprécie pendant que les modèles se déprécient »*.

### Le chiffre maison

**− 30 % d'itérations de correction après dix cycles**, étiqueté *Mesuré · SFEIR*, matière first-party 2026. Aucun protocole, périmètre, taille d'échantillon ni définition d'« itération de correction » n'est donné. C'est le seul chiffre propre de l'article et il soutient sa thèse la plus commercialement utile. Ne pas le réemployer sans le qualifier.

### L'efficience économique dans une grille de qualité

*« Un budget de tokens par tâche est une contrainte au même titre qu'un budget de performance, et il produit la même vertu, borner l'autonomie par le coût de la vérifier. »* Jonction FinOps ↔ qualité.

### Variance de citation à connaître

SFEIR référence Monperrus sous le titre *« The End of Code Review: How AI Agents Supersede Human Code Review »*. Le titre porté par le corpus (arXiv 2606.13175) est *« The End of Code Review: Coding Agents Supersede Human Inspection »*. Même papier, même date (11 juin 2026) ; c'est le libellé SFEIR qui dérive — utiliser le titre arXiv en citation formelle. SFEIR prend le diagnostic de [[monperrus-end-of-code-review-agents-supersede-2026-06-11]] et en refuse la conclusion.

### Sources citées absentes du corpus, candidates à l'ajout

Deux textes d'Osmani : *Set the constraints around your agents* (LinkedIn, **30 juillet 2026** — le diagramme d'origine) et surtout ***Software Factories, Light and Dark*** (addyosmani.com, juillet 2026), qui porte à lui seul trois des concepts structurants repris ici : le principe de back-pressure, la *comprehension debt* opérationnalisée, et la longueur exploitable des boucles. Également absent : *Code review à l'ère de l'IA : du créateur au vérificateur* (SFEIR, 1er avril 2026).

**Fait de veille à noter** : publication le jour même du post Osmani commenté.

## RésuméDe400mots

Cinquième épisode de la série SFEIR sur le SDLC augmenté, consacré à la phase Review, et publié le jour même du post LinkedIn d'Addy Osmani qu'il convertit en spécification de phase.

Le constat de départ : la qualité se lisait dans le code ; les agents en produisent désormais plus que personne ne peut relire. Elle a donc **changé d'adresse** — elle vit dans **l'anneau de contraintes** qui entoure l'agent, c'est-à-dire dans le harnais. Sept dimensions composent cet anneau (correction, sécurité, performance, accessibilité, maintenabilité, efficience économique, compréhensibilité), reliées par la règle de **back-pressure** : on ne confie à une boucle que l'autonomie qu'on sait vérifier à faible coût et de façon fiable. Le corollaire renverse l'intuition dominante : le goulot n'a jamais été la génération, c'est la vérification — « la génération est une bouche large, la vérification un col étroit ; accélérer la bouche épaissit le tas au col ».

D'où la décision d'architecture centrale : dans le cycle à onze phases, **Review n'est pas un gate humain**, et c'est délibéré. Les trois gates inviolables sont Define, Plan et Ship. Faire porter le gate à Review mettrait l'attention humaine — ressource finie — en point de contrôle d'une génération qui, elle, scale : le col ne s'élargirait jamais. **Review instrumente, Ship décide** ; Review produit un faisceau de preuves opposable, et la décision se prend sur les preuves, pas sur le diff intégral. SFEIR retient de Monperrus que l'inspection humaine de chaque diff ne résiste pas à la vitesse agentique, mais refuse sa conclusion : l'acceptation ne se délègue pas.

La traduction opérationnelle est un tableau dimension par dimension, séparant le mécanisable du jugement irréductiblement humain. La dimension systématiquement oubliée est **la compréhensibilité**, « parce qu'elle ne casse pas la CI » — d'où le remède le moins cher de la grille : faire consigner par l'agent ce qu'il a tenté et écarté, car « l'intention n'est pas perdue, elle est jetée ».

Le mode d'échec nommé est **la validation circulaire** : l'agent qui écrit le code écrit les tests qui le valident, la CI est verte, « vous avez construit un miroir, pas un anneau ». Cinq contre-mesures sont reprises d'Anthropic (gates indépendants, déterministe + agentique, mode ombre, tiering par risque, journalisation SIEM), et Compare the Market avertit qu'un relecteur bâti sur du RAG vectoriel dégrade la revue (~70 % pour un graphe AST contre ~58 %).

Le prolongement maison est **le cliquet**, rattaché à Compound-1 : toute échappée devient une contrainte. L'anneau s'épaissit à chaque cycle — « le seul actif de la chaîne qui s'apprécie pendant que les modèles se déprécient » (− 30 % d'itérations de correction après dix cycles, mesure interne). Reste une seule question : **qu'est-ce que mon système refuse de laisser passer ?**

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | affirme_que | la qualité logicielle ne se lit plus dans le code mais dans l'anneau de contraintes qui entoure l'agent | AFFIRMATION | 0.98 | ATEMPOREL | déclaré_article |
| anneau de contraintes | CONCEPT | est_basé_sur | Addy Osmani | PERSONNE | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affine | anneau de contraintes | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| anneau de contraintes | CONCEPT | fait_partie_de | cycle à 11 phases | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| back-pressure | CONCEPT | fait_partie_de | anneau de contraintes | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| Addy Osmani | PERSONNE | affirme_que | "on ne confie à une boucle que l'autonomie qu'on sait vérifier à faible coût et de façon fiable, pas un pouce de plus" | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le goulot n'a jamais été la génération mais la vérification : accélérer la génération ne fait qu'épaissir le tas au col de la vérification | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| phase Review (SDLC) | CONCEPT | fait_partie_de | cycle à 11 phases | METHODOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | "Review instrumente. Ship décide." — Review livre un faisceau de preuves opposable, Ship décide sur les preuves et non sur le diff intégral | CITATION | 0.97 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | placer le gate humain sur Review ferait de l'attention humaine le point de contrôle d'une génération qui scale, plafonnant le débit au nombre de diffs qu'un senior peut lire dans une journée | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | s_oppose_à | The End of Code Review: Coding Agents Supersede Human Inspection | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| Martin Monperrus | PERSONNE | affirme_que | le modèle hybride "l'agent écrit, l'humain relit" est intenable et générateur d'une fausse sécurité | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| validation circulaire | CONCEPT | est_instance_de | mode d'échec de la revue agentique | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Augment Code | ORGANISATION | référence | validation circulaire | CONCEPT | 0.94 | STATIQUE | déclaré_article |
| DORA 2025 | DOCUMENT | mesure | "l'adoption de l'IA est corrélée positivement au débit de livraison et négativement à la stabilité quand les fondations ne suivent pas" | MESURE | 0.93 | STATIQUE | déclaré_article |
| compréhensibilité | CONCEPT | réduit | comprehension debt | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| journal de décision | CONCEPT | permet | reconstruction de l'intention derrière une PR agentique | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | "l'intention n'est pas perdue, elle est jetée" | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| budget de tokens par tâche | CONCEPT | est_instance_de | contrainte de qualité au même titre qu'un budget de performance | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| cliquet de l'anneau | CONCEPT | est_basé_sur | ratchet principle | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| cliquet de l'anneau | CONCEPT | fait_partie_de | Compound-1 | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | toute échappée devient une contrainte : un défaut qui a franchi l'anneau se referme dans l'anneau sous forme de test, de règle de lint, de rubrique de revue ou de garde-fou de harnais | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | "l'anneau s'épaissit à chaque cycle, et c'est le seul actif de la chaîne qui s'apprécie pendant que les modèles se déprécient" | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | mesure | "− 30 % d'itérations de correction après dix cycles" (mesure interne first-party, protocole non publié) | MESURE | 0.78 | STATIQUE | déclaré_article |
| Compare the Market | ORGANISATION | mesure | "le graphe de connaissance structurel construit par analyse de l'AST place un commentaire en ligne pertinent dans environ 70 % des cas contre 58 % pour le RAG vectoriel, sur 79 merge requests" | MESURE | 0.92 | STATIQUE | déclaré_article |
| graphe de connaissance structurel | TECHNOLOGIE | surpasse | RAG vectoriel | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | qualifier une boucle pour l'autonomie sur cinq critères de contrôle — peu coûteux, à haute fréquence, difficile à contourner, immédiat et non dérivant | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| boucles courtes | CONCEPT | améliore | vérifiabilité d'un agent | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | garder la revue humaine sur l'authentification, la facturation et les contrats d'API publics, et réviser chaque interrupteur à chaque Compound | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | remplacer la question "ce code est-il bon ?" par "qu'est-ce que mon système refuse de laisser passer ?" | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| anneau de contraintes | CONCEPT | définition | Ensemble des sept dimensions de contrainte mécanisées autour d'un agent (correction, sécurité, performance, accessibilité, maintenabilité, efficience économique, compréhensibilité), reliées par la règle de back-pressure ; ne sort que la production qui franchit chaque porte | AJOUT |
| back-pressure | CONCEPT | définition | Règle qui relie les dimensions de l'anneau : autonomie ≤ vérifiabilité à faible coût — on ne confie à une boucle que l'autonomie qu'on sait vérifier de façon fiable et peu coûteuse | AJOUT |
| phase Review (SDLC) | CONCEPT | position | Phase 5 du cycle SFEIR, entre Verify et Compound-1, délibérément hors des trois gates humains (Define, Plan, Ship) ; livrable = un faisceau de preuves opposable, la décision revenant au gate Ship | AJOUT |
| validation circulaire | CONCEPT | définition | Mode d'échec où l'agent qui écrit le code écrit aussi les tests qui le valident : la CI est verte sans back-pressure réelle — « un miroir, pas un anneau de contraintes » | AJOUT |
| cliquet de l'anneau | CONCEPT | définition | Règle « toute échappée devient une contrainte » : un défaut ayant franchi l'anneau se referme dans l'anneau (test, lint, rubrique, garde-fou de harnais) au Compound-1, avec mémoire rechargée au Plan du cycle suivant | AJOUT |
| comprehension debt | CONCEPT | application | Dimension « compréhensibilité » de l'anneau : dette systématiquement omise parce qu'elle ne casse pas la CI ; remède peu coûteux = journal de décision de l'agent attaché à la PR | MISE_A_JOUR |
| Addy Osmani | PERSONNE | contribution | Auteur du diagramme de l'anneau de contraintes (LinkedIn, 30 juillet 2026) et de l'essai Software Factories, Light and Dark d'où viennent la back-pressure, la comprehension debt et la longueur exploitable des boucles | MISE_A_JOUR |
| Software Factories, Light and Dark | DOCUMENT | statut | Essai d'Addy Osmani (addyosmani.com, juillet 2026) — source des trois concepts structurants repris par SFEIR ; absent du corpus de veille, candidat d'ajout prioritaire | AJOUT |
| cycle à 11 phases | METHODOLOGIE | gates | Trois gates humains inviolables — Define (l'intention), Plan (l'architecture), Ship (l'acceptation avant livraison) ; Review en est délibérément exclue pour ne pas plafonner le débit sur l'attention humaine | MISE_A_JOUR |
