---
themes: [agents-codage-ia-skills, transformation-adoption, architecture-construction]
source: "martinfowler.com (Rachel's Ramblings)"
---
# laycock-thoughtworks-reviewing-all-this-code-2026-09-02

## Veille

Billet de **Rachel Laycock**, CTO de **Thoughtworks**, publié le **2 septembre 2026** sur *Rachel's Ramblings*, la section de martinfowler.com qu'elle tient, environ **8 000 caractères**. Le texte est une **réponse assumée** à [[houck-dx-what-are-code-reviews-for-2026-08-05]], après un désaccord public entre les deux auteurs sur un panel de **Code Remix** hébergé par **Moderne**. Laycock accepte le diagnostic chiffré de Houck (+**106 %** de lignes par diff chez **Meta**, +**64 %** de taille médiane de PR côté DX) et la liste des fonctions non-défectologiques de la revue, puis déplace la question : *« why are we waiting until code review to do all of those things? »* (A) Le principe directeur est le raccourcissement des boucles de rétroaction appris chez Thoughtworks — si un retour a de la valeur, ne pas le supprimer, le rapprocher de la décision qu'il informe. Chaque fonction attribuée à la revue est réaffectée en amont : exploration d'alternatives avant l'implémentation, transfert de connaissance par le **pair programming**, propriété collective par le **mob programming** et les sessions de design d'équipe, alignement architectural par le design commun puis les **fitness functions**, et automatisation de tout ce qui est déterministe — *« We really shouldn't still be arguing about whitespace in 2026. »* (B) La revue par exception remplace la revue systématique : changement architectural fondamental, frontière de sécurité sensible, rayon d'impact large, zone inconnue d'un système critique, ou simple déclaration d'inconfiance de l'équipe. (1) L'automatisation de la revue par un agent qui imite le relecteur humain est écartée comme *« automating the ceremony rather than questioning why the ceremony exists »*. (2) La dette cognitive de Houck est reconnue comme réelle, mais la PR obligatoire est jugée une défense faible : *« We need engineers to understand systems, not diffs. »*

## Titre Article

Maybe We Shouldn't Be Reviewing All This Code

## Date

2026-09-02

## URL

https://martinfowler.com/rachels-ramblings/code-review.html

## Keywords

revue de code, revue par exception, pull request, boucle de rétroaction courte, décaler le jugement à gauche, shift left, pair programming, mob programming, session de design d'équipe, trunk-based development, fitness functions, architecture évolutive, analyse statique, tests automatisés, scan de sécurité, cérémonie, goulot d'étranglement, rayon d'impact, frontière de sécurité, dette cognitive, dette d'intention, propriété collective, transfert de connaissance, comprendre les systèmes pas les diffs, Thoughtworks, Code Remix, Moderne

## Authors

Rachel Laycock, CTO de Thoughtworks, sur *Rachel's Ramblings* (martinfowler.com).

## Ton

Profil : billet de réponse court signé par une dirigeante technique, voix « je » pleinement assumée, registre argumentatif et personnel, niveau technique moyen, public cible responsables d'ingénierie et praticiens agiles. Le texte s'annonce comme tel dès l'ouverture — panel, désaccord, invitation de l'interlocuteur à écrire la réponse — et pose ses conditions de courtoisie avant d'attaquer : accord sur les faits, accord sur les finalités, désaccord sur le moyen. *« I think we mostly want the same things. I just don't think code review is the best way to get them. »* La concession est explicite et redoublée d'humour (*« Brian is lovely, by the way »*, *« But I'd be lying if I said I didn't want you to think I'm right by the end :) »*), tout comme l'aveu de position ancienne : l'autrice n'a jamais aimé la pull request au centre du processus, et le dit avec une digression assumée sur les conflits de merge. La construction est une réfutation point par point qui reprend la liste de son contradicteur et la réaffecte, avec une figure répétée jusqu'à l'auto-ironie (*« I won't repeat myself about pairing and team design sessions, oh wait... »*). La réserve est posée à sa place, sans mise en scène : la dette cognitive et d'intention est concédée comme *« a very real problem »*, seul le remède est contesté. Sont citables tels quels : *« If feedback is valuable, don't remove it. Move it closer to the decision it is informing »* ; *« We need engineers to understand systems, not diffs »* ; *« automating the ceremony rather than questioning why the ceremony exists »* ; et la clôture, *« perhaps the question isn't how we get the code reviewed faster. Perhaps it's why we're waiting until code review to have all the important conversations in the first place. »*

## Pense-betes

- **Le désaccord porte sur le moyen, pas sur la fin.** Laycock accepte les chiffres et la liste de Houck — la revue sert aussi au partage de connaissance, à la formation des juniors, à la propriété collective et à la diffusion de la compréhension architecturale — et n'en tire pas la conclusion qu'il faut préserver la revue, mais qu'il faut arrêter d'attendre la revue pour faire tout cela. La thèse tient dans une inversion de calendrier, pas dans une contestation des données.
- **Le principe importé : raccourcir la boucle, pas supprimer le retour.** *« If feedback is valuable, don't remove it. Move it closer to the decision it is informing. »* Table de réaffectation fonction par fonction : explorer des alternatives → avant l'implémentation, pas après ; transfert de connaissance → pair programming, parce que raisonner à côté de quelqu'un enseigne davantage que lire sa solution finie ; apprentissage des juniors → travailler avec des seniors *pendant* qu'ils réfléchissent ; propriété collective → organisation d'équipe, mob programming, sessions de design au tableau ; alignement architectural → design commun puis **fitness functions** encodant les contraintes ; formatage, linting, sécurité connue et tout ce qui est testable déterministiquement → automatisation.
- **La « revue par exception » est le dispositif de sortie proposé**, et il est borné explicitement : changement architectural fondamental (possiblement revu en équipe après une session de design), franchissement d'une frontière de sécurité sensible, changement à large rayon d'impact, partie inconnue d'un système critique, ou déclaration d'une équipe qui dit ne pas être confiante. La distinction est entre *« exactly the places where human judgment is valuable »* et l'exigence d'inspection humaine de tout changement au titre de la cérémonie historique de production de confiance.
- ⚠️ **L'argument anti-goulot est indépendant de l'argument pédagogique** et se suffit à lui-même : si un agent produit dix fois plus de code mais que chaque ligne finit en file d'attente devant un ingénieur senior, on n'a pas créé une organisation dix fois plus rapide, on a créé un backlog et un nouveau goulot. C'est le même mécanisme que le coût par changement accepté de [[staples-gitlab-when-code-is-abundant-2026-08-24]] : lever une contrainte expose la suivante.
- **La revue IA imitant le relecteur humain est explicitement refusée** — non parce qu'elle marcherait mal, mais parce qu'elle préserve un processus dont on n'a pas réinterrogé la raison d'être : *« That's automating the ceremony rather than questioning why the ceremony exists. »* À noter pour l'usage : cette réserve vise la substitution à l'identique, pas la participation d'agents aux boucles amont, que le texte admet (contester des designs, tester des hypothèses, vérifier en continu), en maintenant que la pensée vient d'humains expérimentés.
- **Ce qui est concédé, et ce qui est renvoyé** : la dette cognitive et d'intention est qualifiée de *« very real problem »* ; c'est la PR obligatoire comme défense qui est contestée. La contre-proposition n'est pas un dispositif unique mais une liste — design collaboratif, pairing, bonnes frontières, architecture exécutable, responsabilité opérationnelle partagée — assortie de l'aveu qu'il faudra probablement des pratiques non encore inventées.
- **Le diagnostic de fond, à retenir hors du débat** : des années à empiler sur la revue de code un nombre extraordinaire de responsabilités — porte qualité, contrôle sécurité, revue d'architecture, mécanisme de mentorat, système de partage de connaissance, modèle de propriété. Cela tenait tant que les humains ne pouvaient produire du code qu'à une certaine vitesse ; c'est cette contrainte qui disparaît, et l'empilement avec elle.
- **À relier** : [[monperrus-end-of-code-review-agents-supersede-2026-06-11]] (la même conclusion sur l'inspection humaine, atteinte par l'automatisation plutôt que par le déplacement à gauche) et [[boeckeler-harness-engineering-coding-agents-2026-04-02]] (l'outillage de vérification amont, côté Thoughtworks également).

## RésuméDe400mots

Rachel Laycock, CTO de Thoughtworks, publie le 2 septembre 2026 sur martinfowler.com une réponse à l'édition d'Engineering Enablement signée Brian Houck un mois plus tôt. Les deux auteurs se sont opposés publiquement sur un panel de Code Remix hébergé par Moderne, et Houck l'a encouragée à écrire ce texte. Le désaccord est circonscrit d'emblée : ils veulent la même chose, elle ne pense pas que la revue de code soit le meilleur moyen de l'obtenir.

Elle accepte le constat. L'IA produit plus de code que les humains ne peuvent raisonnablement revoir, et les chiffres de Houck — 106 % d'augmentation des lignes significatives par diff chez Meta, 64 % de taille médiane de pull request chez DX — sont repris tels quels. Elle partage aussi son inquiétude : automatiser la revue risque de perdre tout le reste, car la revue n'a jamais servi qu'à trouver des bugs. Sa question est ailleurs : pourquoi attendre la revue pour faire tout cela ?

Elle n'a jamais aimé voir la pull request au centre du processus. Construire quelque chose, le finir, l'emballer, le lancer par-dessus la clôture, puis avoir la conversation importante sur la justesse de ce qu'on a construit lui paraît un ordre inversé. Le principe qu'elle oppose est celui appris tôt chez Thoughtworks : si un retour a de la valeur, ne pas le supprimer, mais le rapprocher de la décision qu'il informe.

Suit une réaffectation systématique. Explorer des alternatives se fait avant d'en implémenter une. Le transfert de connaissance passe par le pairing, qui enseigne davantage que la lecture d'une solution achevée. L'apprentissage des juniors suppose de travailler avec des seniors pendant qu'ils réfléchissent. La propriété collective vient de l'organisation des équipes, du mob programming et des sessions de design au tableau. L'alignement architectural naît du design commun, puis des fitness functions. Le formatage, le linting, la sécurité connue et le déterministe s'automatisent.

Reste la revue par exception : changement architectural fondamental, frontière de sécurité sensible, large rayon d'impact, zone inconnue d'un système critique, ou équipe qui se déclare peu confiante. C'est différent d'exiger l'inspection de chaque changement au nom de la cérémonie. Elle écarte aussi l'agent IA qui imiterait le relecteur humain : cela automatise la cérémonie au lieu d'interroger sa raison d'être.

Elle concède un point : la dette cognitive et d'intention décrite par Houck est un vrai problème. Mais la PR obligatoire en est une défense faible. Il faut du design collaboratif, du pairing, de bonnes frontières, de l'architecture exécutable et de la responsabilité opérationnelle partagée — parce que les ingénieurs doivent comprendre des systèmes, pas des diffs.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Rachel Laycock | PERSONNE | a_créé | Maybe We Shouldn't Be Reviewing All This Code | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Rachel Laycock | PERSONNE | dirige | Thoughtworks | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Maybe We Shouldn't Be Reviewing All This Code | DOCUMENT | s_oppose_à | What are code reviews even for? | DOCUMENT | 0.96 | STATIQUE | déclaré_article |
| Rachel Laycock | PERSONNE | affirme_que | le problème n'est pas que l'IA ait cassé la revue de code, mais qu'on utilisait la revue pour résoudre les mauvais problèmes | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| boucle de rétroaction courte | CONCEPT | recommande | ne pas supprimer un retour de valeur, mais le rapprocher de la décision qu'il informe | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| pair programming | METHODOLOGIE | remplace | la revue de code comme mécanisme de transfert de connaissance | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| pair programming | METHODOLOGIE | surpasse | la lecture d'une solution achevée pour apprendre le raisonnement d'un ingénieur expérimenté | AFFIRMATION | 0.91 | ATEMPOREL | déclaré_article |
| mob programming | METHODOLOGIE | permet | propriété collective par construction, au lieu d'une notification de l'équipe après coup | AFFIRMATION | 0.89 | ATEMPOREL | déclaré_article |
| session de design d'équipe | METHODOLOGIE | permet | explorer les alternatives avant l'implémentation plutôt qu'après | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| fitness functions | METHODOLOGIE | permet | encoder les contraintes architecturales importantes après un design commun | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| analyse statique | TECHNOLOGIE | s_applique_à | formatage, linting, problèmes de sécurité connus et tout ce qui est testable déterministiquement | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| revue par exception | METHODOLOGIE | s_applique_à | changement architectural fondamental, frontière de sécurité sensible, large rayon d'impact, zone inconnue d'un système critique, inconfiance déclarée de l'équipe | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| revue par exception | METHODOLOGIE | s_oppose_à | exiger l'inspection humaine de chaque changement au titre de la cérémonie historique de production de confiance | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Rachel Laycock | PERSONNE | prédit | un agent produisant dix fois plus de code devant une file de revue senior ne crée pas une organisation dix fois plus rapide mais un backlog et un nouveau goulot | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| revue de code par agent imitant le relecteur humain | METHODOLOGIE | s_oppose_à | interroger la raison d'être de la cérémonie plutôt que l'automatiser à l'identique | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| agents IA | TECHNOLOGIE | permet | participer aux boucles amont en contestant des designs, testant des hypothèses et vérifiant en continu, la pensée restant humaine | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Rachel Laycock | PERSONNE | soutient | la dette cognitive et d'intention est un problème réel | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| pull request | METHODOLOGIE | réduit | faiblement la dette cognitive et d'intention lorsqu'elle est rendue obligatoire, contre l'usage qui lui est prêté | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Rachel Laycock | PERSONNE | affirme_que | il faut que les ingénieurs comprennent des systèmes, pas des diffs | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| revue de code | METHODOLOGIE | est_instance_de | empilement de responsabilités — porte qualité, contrôle sécurité, revue d'architecture, mentorat, partage de connaissance, modèle de propriété | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| abondance du code générée par l'IA | CONCEPT | s_oppose_à | la contrainte de vitesse humaine qui rendait cet empilement tenable | AFFIRMATION | 0.90 | ATEMPOREL | inféré |
| Code Remix | EVENEMENT | observé_dans | le désaccord public entre Rachel Laycock et Brian Houck, à l'origine du billet | AFFIRMATION | 0.90 | STATIQUE | déclaré_article |
| Moderne | ORGANISATION | publie | Code Remix | EVENEMENT | 0.88 | STATIQUE | déclaré_article |
| Rachel Laycock | PERSONNE | recommande | maintenir la compréhension humaine par design collaboratif, pairing, bonnes frontières, architecture exécutable et responsabilité opérationnelle partagée | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Rachel Laycock | PERSONNE | rôle | CTO de Thoughtworks, autrice de la section *Rachel's Ramblings* sur martinfowler.com | AJOUT |
| Thoughtworks | ORGANISATION | apport | Cabinet dont l'autrice tire les principes invoqués : boucles de rétroaction courtes, pair programming, trunk-based development, fitness functions | MISE_A_JOUR |
| Maybe We Shouldn't Be Reviewing All This Code | DOCUMENT | format | Billet d'environ 8 000 caractères publié le 2 septembre 2026, réponse explicite à l'édition d'Engineering Enablement de Brian Houck du 5 août | AJOUT |
| revue par exception | METHODOLOGIE | définition | Réserver la revue humaine aux classes de changement où le jugement humain apporte, au lieu d'inspecter systématiquement chaque changement | AJOUT |
| pair programming | METHODOLOGIE | rôle | Substitut proposé à la revue pour le transfert de connaissance et l'apprentissage des juniors, parce qu'il opère pendant le raisonnement et non après | MISE_A_JOUR |
| mob programming | METHODOLOGIE | rôle | Dispositif de propriété collective, avec les sessions de design d'équipe au tableau, en amont de l'écriture ou de l'instruction donnée à l'agent | AJOUT |
| fitness functions | METHODOLOGIE | rôle | Encodage exécutable des contraintes architecturales, posé après un design collectif plutôt que vérifié en revue | AJOUT |
| pull request | METHODOLOGIE | critique | Contestée comme centre du processus de développement : construire, finir, emballer et transmettre avant d'avoir la conversation importante | AJOUT |
| dette cognitive et dette d'intention | CONCEPT | statut | Concédée comme problème réel, mais dont la pull request obligatoire est jugée une défense faible | MISE_A_JOUR |
| Brian Houck | PERSONNE | rôle | Contradicteur nommé, rattaché à DX ; auteur du texte auquel ce billet répond | MISE_A_JOUR |
| Code Remix | EVENEMENT | nature | Panel hébergé par Moderne où Laycock et Houck se sont publiquement opposés | AJOUT |
| Moderne | ORGANISATION | rôle | Hôte du panel Code Remix ; éditeur cité sans autre développement | AJOUT |
