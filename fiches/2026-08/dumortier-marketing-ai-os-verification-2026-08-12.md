---
themes: [qualite-securite, architecture-construction, agents-codage-ia-skills, transformation-adoption]
source: "LinkedIn Pulse"
---
# dumortier-marketing-ai-os-verification-2026-08-12

## Veille

Retour d'expérience publié sur **LinkedIn Pulse** le **12 août 2026** par **Guillaume Dumortier**, dans sa newsletter *Growth Marketing Fit*, sous-titré *« Four layers, a lot of rebuilding, and the failure modes nobody warns you about »*, ~2 500 mots. L'objet : un système d'IA interne construit **dans Claude** pour une équipe marketing d'une soixantaine de personnes — une trentaine de **skills** contenu et vente, une douzaine de **modules de source de vérité**, **sept agents dont six n'existent que pour contrôler le travail plutôt que le produire**, un **plugin** pour ceux qui vivent dans un terminal, une **application navigateur** portant la même connaissance pour tous les autres, et une orchestration qui enchaîne trois ou quatre actifs en un *campaign bundle*. La thèse est posée tôt : la qualité d'une sortie IA n'est pas déterminée au moment de la génération, mais par ce que le système sait avant de commencer et par ce qui arrive au brouillon après — *« L'étape de génération au milieu est la partie facile. C'est aussi la seule que la plupart des équipes ont construite. »* D'où quatre couches : **Vérité** (presque personne ne la construit), **Production** (tout le monde), **Vérification** (presque personne), **Distribution interne** (*« là où les bons systèmes meurent de négligence »*). Deux mécanismes de défaillance portent l'article. **(A) Le « pass » nu d'un vérificateur en monde clos** : un vérificateur de faits adossé à la documentation produit reçoit un brouillon contenant une affirmation sur un autre produit, que ses sources ne couvraient pas — il rend un *« pass »*, non parce que l'affirmation était vraie mais parce que rien ne la contredisait. *« Il n'a pas seulement raté l'erreur, il l'a certifiée. »* Correctif : interdire le verdict nu et exiger que chaque rapport déclare sa **propre couverture** — combien d'affirmations vérifiées, combien appariées à des sources, lesquelles hors juridiction, lesquelles possédées par aucune source. *« "Je ne peux pas vérifier ceci" est devenu un résultat de première classe. »* **(B) La contradiction inter-actifs** : deux actifs peuvent être individuellement corrects, chacun traçable vers une vraie source, et se contredire — le communiqué dit une date, l'article de blog une autre, les deux passent, le bundle est inexpédiable. *« La vérification par actif ne peut pas attraper ça, par construction. »* Clausule de l'article : *« The generation is free. The trust is the product. »*

## Titre Article

I built a marketing AI operating system for a 60-person team. The most valuable thing in it is the part that refuses to write.

## Date

2026-08-12

## URL

https://www.linkedin.com/pulse/i-built-marketing-ai-operating-system-60-person-team-most-dumortier-3hbnc

## Keywords

Guillaume Dumortier, Growth Marketing Fit, LinkedIn Pulse, marketing AI OS, IA marketing, outil interne, Claude, skills, plugin, application navigateur, quatre couches, couche de vérité, truth layer, source of truth, propriétaire de document, versionnement, provenance, couche de production, couche de vérification, distribution interne, adoption interne, machine à confiance, dérive de faits, séparation faits/contenu, routage de skills, frontières de skill, contrat de sortie, ambiguïté, plan au lieu d'article, revue creuse, rubber-stamping, blanchiment de sortie, session fraîche, monde clos, closed-world, déclaration de couverture, interdiction du pass nu, affirmation invérifiable, résultat de première classe, campaign bundle, vérification inter-actifs, cohérence croisée, contradiction entre actifs, revue qui ne bloque jamais, deux interfaces, adoption suit la confiance, incertitude visible, contrôle déterministe, enforcement en code, tiret cadratin, asking nicely is not a control, échec silencieux, constante vide, suppression des chiffres, hallucination attribuée à tort, test de pipeline, lacune de validation, refus, teach the system to refuse, coût de vérification, staleness, propriété et provenance

## Authors

**Guillaume Dumortier** — auteur de la newsletter LinkedIn **Growth Marketing Fit** (~1 300 abonnés à la publication). Il écrit en **praticien-constructeur** : il a passé *« une longue partie de cette année »* à bâtir et exploiter le système décrit. La légende de l'illustration précise le socle technique — *« A custom-built Marketing AI OS within Claude »*. Publié le **12 août 2026**.

## Ton

**Profil** : retour d'expérience d'ingénierie interne, à la première personne, publié en newsletter LinkedIn. Public borné dès l'introduction : *« Ce n'est pas un texte sur la question de savoir si l'IA écrit bien. Si c'est encore la question ouverte pour vous, ça ne prendra pas. C'est pour les gens déjà trois mois dedans, qui se demandent en silence pourquoi la chose marche magnifiquement en démo et continue de produire des sorties que personne ne fait assez confiance pour expédier. »* Registre praticien anti-démo, sec, sans vocabulaire de vendeur.

**Style** : la structure est fixe et répétée à chaque couche — six rubriques dans le même ordre, quatre fois : *What it is* → *Why nobody builds it* → *What I got wrong* → *The rule* → *How you'll know it's working* → *Do this week*. C'est un gabarit d'audit qu'on peut passer sur son propre système. Les critères de succès sont formulés en signaux observables plutôt qu'en métriques : *« Quelqu'un demande "d'où vient ce chiffre" et la réponse prend quatre secondes au lieu d'une expédition archéologique dans Slack »*, *« les gens arrêtent de vous demander quel outil utiliser pour quoi »*. Le texte ne prescrit jamais sans avoir d'abord raconté l'échec correspondant, détails ridicules assumés — les majuscules dans le prompt (*« ce qui est à peu près le moment où vous devriez commencer à soupçonner que vous avez le mauvais modèle du problème »*), la skill blog qui décrivait des articles au lieu de les écrire, *« à chaque fois »*, pendant des semaines. Chaque section se clôt sur un aphorisme, ce qui rend le texte facile à citer sans le mécanisme qui le fonde. La section *« ce dont je ne suis toujours pas sûr »* est placée avant la conclusion et non escamotée, avec une auto-critique : *« je fais actuellement un mélange et je ne pense pas que le mélange soit raisonné, je pense que c'est un compromis que je n'ai pas correctement examiné. »*

**Formules-marqueurs** :
- ***« I was building a trust machine, and I didn't know it »***
- ***« You cannot demo a truth layer. You can only demo what it prevents, which is nothing visible »***
- ***« Nothing that produces content is allowed to contain a fact. It has to ask »***
- ***« a skill's most important job is describing what it is not for »***
- ***« You do not get a bad review. You get a good review that is worthless »***
- ***« It didn't just miss the error, it certified it »***
- ***« An unverifiable claim is a finding, not a silence »***
- ***« If your review step has never blocked anything, it isn't a review step. It's decoration »***
- ***« adoption tracks trust, not capability »***
- ***« Never ask a model for something you can enforce in code »***
- ***« Traditional software crashes when it breaks. These systems keep going, confidently, at reduced quality »***
- ***« The generation is free. The trust is the product »***

**Position épistémique** : praticien en exploitation, non en démonstration. L'article ne nomme ni l'entreprise, ni les produits, ni les chiffres d'usage : aucun résultat n'est mesuré, aucune adoption quantifiée, aucun avant/après produit — ce que l'auteur revendique (*« Je vais vous dire ce qui a cassé, parce que les parties cassées sont la partie utile »*). Autorité forte sur les mécanismes de panne rencontrés ; aucune sur leur fréquence, leur coût ou leur généralité. Limites à garder : n=1, une seule pile, plusieurs correctifs généralisés par l'auteur sans démonstration, et un coût reconnu mais non chiffré.

## Pense-betes

- **Date / source** : **12 août 2026**, LinkedIn Pulse, newsletter *Growth Marketing Fit*, ~2 500 mots. Système bâti dans **Claude** pour une équipe marketing de ~60 personnes.
- **Cadrage clé** : *« Je croyais construire une machine à contenu. Je construisais une machine à confiance, et je ne le savais pas, donc j'ai dépensé mon effort initial exactement au mauvais endroit. »*

### Interdire le « pass » nu

Un vérificateur est un **système en monde clos** : il ne peut se prononcer que sur ce qu'on lui a fourni. Confronté à une affirmation qu'aucune de ses sources ne couvre, il ne trouve aucune contradiction et rend un verdict favorable indiscernable d'une vraie vérification. Le correctif est une contrainte de format :

| Le rapport doit énoncer | Pourquoi |
|---|---|
| Combien d'affirmations ont été **contrôlées** | dénominateur : sans lui, un « OK » ne veut rien dire |
| Combien ont été **effectivement appariées à une source** | c'est le vrai taux de couverture, toujours inférieur |
| Lesquelles **ne relevaient pas de sa juridiction** | sinon le juge déborde et le silence des autres passe pour un accord |
| Lesquelles **ne sont possédées par aucune source du système** | c'est le registre de risque réel de l'organisation |

*« Je ne peux pas vérifier ceci »* doit être un résultat de première classe, au même rang que « conforme » et « non conforme ». L'anti-pattern symétrique est plus dangereux que l'absence de contrôle : *« une bonne revue sans valeur est bien pire que pas de revue, parce qu'elle blanchit la sortie »* — quelqu'un en aval voit *reviewed: pass* et arrête de regarder. À croiser avec [[willison-fable-judgement-delegation-subagents-2026-07-03]].

### Le contrôle que la vérification par actif ne peut pas produire

Deux actifs d'une même campagne peuvent être chacun individuellement correct, chacun traçable vers une vraie source, chacun validé — et se contredire. Vérifier contre la couche de vérité et vérifier les actifs les uns contre les autres sont **deux contrôles différents** ; le premier ne peut pas produire le second. Diagnostic de l'auteur : *« si vous faites des campagnes multi-actifs et que vous ne vérifiez qu'un actif à la fois, vous avez ce bug en ce moment. »* Transposition hors marketing : une PR qui touche trois fichiers, un jeu de specs généré en lot, une doc et son code produits ensemble. La cohérence croisée est un contrôle de niveau bundle, jamais une somme de contrôles unitaires.

### La couche de vérité

Panne racontée : les faits produit vivaient **dans** la skill qui écrivait les articles, puis le même fait a dû exister dans la skill e-mail, la battlecard, la page web. *« En quelques semaines j'avais quatre versions légèrement différentes de notre date de lancement dans quatre fichiers différents, et la dérive était invisible parce que chaque fichier était individuellement plausible. »*

Règle : *« un document qui énonce des faits et un document qui produit du contenu sont deux documents différents, avec deux propriétaires différents »*, chacun versionné et daté. Rien de ce qui produit du contenu n'a le droit de contenir un fait — il doit le demander. Bénéfice : un fait change, on le change une fois, les 35 skills sont correctes le lendemain ; une affirmation est contestée, un seul endroit à regarder. Raison pour laquelle personne ne la construit : *« On ne peut pas faire la démo d'une couche de vérité. On ne peut faire la démo que de ce qu'elle empêche, c'est-à-dire rien de visible. »* Exercice proposé : ouvrir les cinq derniers actifs produits, surligner chaque affirmation factuelle, nommer pour chacune l'unique document qui la possède — *« celles auxquelles vous ne pouvez pas assigner de propriétaire sont votre véritable registre de risques. »* Prolonge [[vasilopoulos-codified-context-infrastructure-ai-agents-2026-02-24]].

### Deux leçons sur les skills

1. **Le contrat de sortie doit être paranoïaque sur l'ambiguïté.** Pendant des semaines, la skill « article de blog » écrivait **des descriptions d'articles** — des titres de section suivis d'une phrase expliquant ce que la section couvrirait, *« à chaque fois »* — et ça passait toutes les revues, la structure étant impeccable. Cause : une ligne ambiguë du gabarit (*« the post, under the flavour's own section headers »*), raisonnablement lue comme une demande de plan. Détail organisationnel plus important que le bug : personne ne l'a signalé, *« les gens supposent que l'outil a raison et qu'eux l'utilisent mal. »*
2. **Le travail le plus important d'une skill est de décrire ce à quoi elle ne sert pas.** Passé la trentaine de skills, le problème cesse d'être la qualité et devient le **routage** : deux skills qui traitent toutes deux plausiblement *« écris-moi quelque chose pour les commerciaux »* se disputent chaque requête, et le gagnant arbitraire produit le mauvais format. La moitié de chaque description est devenue une frontière explicite. À confronter à [[shihipar-claude-code-lessons-building-skills-2026-06-03]].

### Du prompt à la plomberie

Les règles de voix interdisaient les tirets cadratins, chaque prompt le disait, les testeurs en trouvaient quand même pendant des semaines : *« Je répétais la règle plus fort, ce qui est un correctif probabiliste à un problème dont la solution déterministe était juste là. »* Correctif : une fonction unique en sortie qui les supprime. Heuristique généralisable : *« si vous vous surprenez à répéter une instruction, c'est le signal de la sortir du prompt et de la mettre dans la plomberie »*, avec son corollaire — *« demander gentiment n'est pas un contrôle. »*

### La panne silencieuse

Une constante censée contenir un caractère marqueur invisible avait été vidée en chaîne vide. Aucun diff visible, aucune erreur. En aval, une étape de nettoyage s'est mise à matcher chaque chiffre de chaque prompt et à le supprimer : `« 7.1% across 6,000+ orgs, 2500 words »` arrivait au modèle sous la forme `« .% across ,+ orgs, words »`. Chaque statistique, date, compte de mots et numéro de section retirés silencieusement, pendant un nombre indéterminé de releases. C'était la raison réelle pour laquelle les chiffres cités revenaient faux — *« et j'avais passé des semaines à blâmer la tendance du modèle à inventer des chiffres. Il les inventait parce que je les avais supprimés. »*

Principe : *« Le logiciel traditionnel plante quand il casse. Ces systèmes continuent, avec assurance, à qualité réduite, et produisent quelque chose qui a l'air correct. »* Deux correctifs : tester **le pipeline** et pas seulement la sortie — un test dont l'unique fonction est d'affirmer que les chiffres survivent à un aller-retour dans l'assemblage du prompt ; et se rappeler que la validation a les mêmes trous que le système — un champ limité à 500 caractères est resté à 688 pendant deux releases parce que le script contrôlait toutes les autres limites sauf celle-là. Règle de diagnostic : avant d'accuser un modèle d'inventer un chiffre, vérifier que le chiffre lui est bien parvenu.

### La couche 4, distribution interne

*« C'est là que la plupart des projets IA internes meurent en silence. Pas d'un échec technique. D'être techniquement excellents et utilisés par quatre personnes. »* L'auteur avait construit pour lui d'abord — un plugin exigeant l'aisance en ligne de commande, ce qui décrivait six personnes sur soixante. Correctif : le même système bâti deux fois, même connaissance et mêmes contrôles, deux portes d'entrée — plugin pour les constructeurs, application navigateur pour les autres (catalogue, trois champs, un brouillon avec ses contrôles à côté sous forme de boutons).

Point le plus fin de la section : **l'adoption suit la confiance, pas la capacité**. L'outil a été davantage utilisé une fois que la sortie s'est mise à admettre ce dont elle n'était pas sûre — *« Un brouillon qui signale "cet exemple client est illustratif, trouvez-en un vrai avant publication" est utilisé. Un brouillon qui présente avec assurance un exemple client inventé est utilisé une fois, met quelqu'un dans l'embarras, et l'outil est mort par le bouche-à-oreille. »*

### Apprendre au système à refuser

La dernière brique adapte un actif à un autre segment de marché et connaît le segment que l'entreprise a décidé de ne pas poursuivre : sollicitée pour ce segment, elle décline et explique pourquoi. *« Même principe que la déclaration de couverture. Un système qui ne peut que dire oui vous tendra avec assurance la mauvaise chose pour toujours, et vous ne serez pas capable de faire la différence entre "c'est juste" et "c'était la seule réponse disponible". »* Le refus et l'aveu d'ignorance sont la même primitive : la capacité du système à borner son domaine de compétence.

### Les trois incertitudes laissées ouvertes

1. **Couche de vérité embarquée ou récupérée en direct ?** *« Les copies embarquées se périment sans que personne le remarque. Les fetch live sont lents et cassent quand quelqu'un renomme un dossier. »* L'auteur fait un mélange et le dit non raisonné.
2. **Le coût de vérification reste-t-il justifiable ?** Un actif entièrement contrôlé coûte *« plusieurs fois »* un brouillon brut : rentable pour du public, probablement pas pour une synthèse interne, *« et la frontière entre les deux est plus floue que mon système ne le prétend »*. Variable de gouvernance à instrumenter en premier : un niveau de vérification par criticité d'actif.
3. **Combien survit aux deux prochaines générations de modèles ?** Son pari, présenté comme tel : la couche de vérité et la discipline de couverture survivent, parce qu'elles *« résolvent un problème organisationnel de provenance et de propriété qui existerait même avec un modèle parfait. »*

### Le plan « si vous démarrez lundi »

1. Écrire les **dix faits** que l'équipe répète le plus, avec un propriétaire et une date pour chacun — couche de vérité version zéro, *« ça prend un après-midi »*.
2. Prendre le meilleur prompt et en extraire chaque fait vers ce document ; faire en sorte que le prompt les demande.
3. Construire une étape de vérification qui tourne **en session fraîche**, ne voit que le brouillon et les sources, et doit dire ce qu'elle n'a pas pu contrôler.
4. Trouver ce qui est répété sans cesse dans les prompts et le déplacer dans le code.
5. Le montrer à quelqu'un de non technique et le regarder l'utiliser sans l'aider.

Test de référence à faire avant tout le reste : passer un actif **déjà expédié** au contrôle dans une session complètement fraîche, sans autre contexte que le brouillon et les sources. *« Ce qui revient est votre véritable ligne de base qualité. C'est généralement humiliant. La mienne l'était. »*

## RésuméDe400mots

Retour d'expérience publié sur **LinkedIn Pulse** le **12 août 2026** par **Guillaume Dumortier** (newsletter *Growth Marketing Fit*), sur un système d'IA marketing interne bâti **dans Claude** pour une équipe d'une soixantaine de personnes : une trentaine de skills, une douzaine de modules de vérité, **sept agents dont six ne font que contrôler**, un plugin terminal, une application navigateur, et une orchestration de campagnes multi-actifs.

**La thèse.** *« Je croyais construire une machine à contenu. Je construisais une machine à confiance. »* La qualité d'une sortie IA n'est pas déterminée à la génération, mais par **ce que le système sait avant** et **ce qui arrive au brouillon après**. La génération est la partie facile — et la seule que la plupart des équipes ont construite.

**Quatre couches.** *Vérité* : des documents de faits séparés de tout ce qui produit du contenu, chacun avec un propriétaire, versionné et daté. Laisser les faits dans les skills a produit **quatre versions d'une date de lancement dans quatre fichiers**, chacun individuellement plausible. *Production* : la skill blog écrivait pendant des semaines **des descriptions d'articles** au lieu d'articles, et passait toutes les revues, parce que la revue contrôlait la structure. Passé trente skills, le problème devient **le routage** — la moitié d'une description de skill doit énoncer ce à quoi elle ne sert pas. *Vérification* : la couche qui sépare une démo d'un système. *Distribution interne* : là où les projets meurent d'être excellents et utilisés par quatre personnes.

**Les deux pannes centrales.** Un vérificateur de faits reçoit une affirmation qu'aucune de ses sources ne couvre : il rend un « pass ». *« Il n'a pas seulement raté l'erreur, il l'a certifiée. »* Correctif : un vérificateur est un **système en monde clos** ; **il lui est interdit de renvoyer un « pass » nu** et il doit déclarer sa couverture — combien d'affirmations contrôlées, combien réellement appariées, lesquelles hors juridiction, lesquelles possédées par aucune source. *« Une affirmation invérifiable est un constat, pas un silence. »* Seconde panne : **deux actifs individuellement corrects peuvent se contredire** ; la vérification par actif ne peut pas l'attraper, par construction.

**Cinq règles transverses.** Ne jamais demander à un modèle ce qu'on peut imposer en code. Les **échecs silencieux** sont tout le risque — une constante vidée supprimait tous les chiffres de tous les prompts, et il accusait le modèle d'halluciner. Tester le pipeline, pas la sortie. Votre validation a les mêmes trous que votre système. **Apprendre au système à refuser.**

**L'adoption suit la confiance, pas la capacité** : une sortie qui admet ce dont elle n'est pas sûre est utilisée. Clausule : ***« The generation is free. The trust is the product. »***

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Guillaume Dumortier | PERSONNE | a_créé | Marketing AI OS | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Marketing AI OS | TECHNOLOGIE | utilise | Claude | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Marketing AI OS | TECHNOLOGIE | est_instance_de | système interne à quatre couches — vérité, production, vérification, distribution — servant une équipe marketing d'une soixantaine de personnes avec une trentaine de skills, une douzaine de modules de source de vérité et sept agents dont six ne font que contrôler | AFFIRMATION | 0.94 | STATIQUE | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | la qualité d'une sortie IA n'est pas déterminée au moment de la génération mais par ce que le système sait avant de commencer et ce qui arrive au brouillon après qu'il a fini | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | il croyait construire une machine à contenu alors qu'il construisait une machine à confiance, ce qui lui a fait dépenser son effort initial au mauvais endroit | CITATION | 0.95 | STATIQUE | déclaré_article |
| couche de vérité | CONCEPT | fait_partie_de | Marketing AI OS | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| couche de vérité | CONCEPT | réduit | la dérive factuelle : un fait modifié une seule fois rend correctes les trente-cinq skills dès le lendemain, et toute affirmation contestée n'a qu'un document propriétaire et qu'une personne à interroger | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | recommande | qu'un document qui énonce des faits et un document qui produit du contenu soient deux documents différents avec deux propriétaires différents, rien de ce qui produit du contenu n'ayant le droit de contenir un fait | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| vérification en monde clos | CONCEPT | s_applique_à | tout vérificateur automatique adossé à un corpus de sources fini, qui ne peut se prononcer que sur ce qu'on lui a fourni | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| vérification en monde clos | CONCEPT | observé_dans | un vérificateur de faits ayant rendu un « pass » sur une affirmation portant sur un produit que ses sources ne couvraient pas : rien ne la contredisait, donc il n'a trouvé aucun problème et a certifié l'erreur au lieu de la manquer | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| déclaration de couverture | CONCEPT | résout | la certification en monde clos : le vérificateur ne peut pas renvoyer un « pass » nu et doit énoncer combien d'affirmations il a contrôlées, combien il a réellement appariées à ses sources, lesquelles ne relevaient pas de sa juridiction et lesquelles ne sont possédées par aucune source du système | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | une affirmation invérifiable est un constat et non un silence, « je ne peux pas vérifier ceci » devant être un résultat de première classe | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | une bonne revue sans valeur est bien pire que pas de revue du tout, parce qu'elle blanchit la sortie et que quelqu'un en aval voit « reviewed: pass » et arrête de regarder | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| vérification inter-actifs | CONCEPT | résout | la contradiction entre actifs d'un même lot : deux actifs peuvent être individuellement corrects, traçables vers de vraies sources et validés, tout en se contredisant, ce que la vérification par actif ne peut pas attraper par construction | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | recommande | que chaque contrôle tourne comme un appel réellement séparé, sans mémoire de la rédaction du brouillon, différents contrôles possédant des juridictions disjointes et n'ayant pas le droit de noter le terrain des autres | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | le travail le plus important d'une skill est de décrire ce à quoi elle ne sert pas, le problème cessant d'être la qualité pour devenir le routage passé une trentaine de skills | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| ambiguïté du contrat de sortie | CONCEPT | observé_dans | une skill d'article de blog ayant produit pendant des semaines des descriptions d'articles au lieu d'articles, à cause d'une seule ligne ambiguë du gabarit, et passant toutes les revues parce que la revue contrôlait la structure | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| Guillaume Dumortier | PERSONNE | recommande | de ne jamais demander à un modèle ce qu'on peut imposer en code, la répétition d'une instruction dans les prompts étant le signal de la déplacer dans la plomberie — demander gentiment n'est pas un contrôle | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| échec silencieux | CONCEPT | observé_dans | une constante censée contenir un caractère marqueur invisible vidée en chaîne vide, faisant supprimer par une étape de nettoyage chaque chiffre de chaque prompt pendant un nombre indéterminé de releases, sans diff visible ni erreur | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | le logiciel traditionnel plante quand il casse alors que ces systèmes continuent avec assurance à qualité réduite et produisent quelque chose qui a l'air correct | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | recommande | de tester le pipeline et pas seulement la sortie, par exemple un test dont l'unique fonction est d'affirmer que les chiffres survivent à un aller-retour dans l'assemblage du prompt | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | l'adoption suit la confiance et non la capacité : un brouillon qui signale son incertitude est utilisé, un brouillon qui présente avec assurance un exemple inventé est utilisé une fois puis l'outil meurt par le bouche-à-oreille | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | recommande | de construire la seconde interface plus tôt que ce qui semble justifié et de rendre l'incertitude du système visible plutôt que de la cacher pour paraître plus impressionnant | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | recommande | d'apprendre au système à refuser, une étape déclinant explicitement une demande hors périmètre commercial, parce qu'un système qui ne peut que dire oui tendra avec assurance la mauvaise chose sans qu'on puisse distinguer « c'est juste » de « c'était la seule réponse disponible » | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | une étape de revue qui n'a jamais rien bloqué n'est pas une étape de revue mais de la décoration | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Guillaume Dumortier | PERSONNE | mesure | un actif entièrement vérifié coûte plusieurs fois le prix d'un brouillon brut, ce qui est justifié pour toute publication publique mais probablement pas pour une synthèse interne | MESURE | 0.85 | DYNAMIQUE | déclaré_article |
| Guillaume Dumortier | PERSONNE | prédit | que la couche de vérité et la discipline de couverture survivront aux deux prochaines générations de modèles, parce qu'elles ne compensent pas un raisonnement faible mais résolvent un problème organisationnel de provenance et de propriété qui existerait même avec un modèle parfait | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Guillaume Dumortier | PERSONNE | affirme_que | la génération est gratuite et que la confiance est le produit | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| déclaration de couverture | CONCEPT | s_applique_à | tout dispositif de LLM-juge hors marketing, notamment la revue de code automatisée et l'évaluation de sorties générées | AFFIRMATION | 0.85 | ATEMPOREL | inféré |
| Growth Marketing Fit | DOCUMENT | publie | Marketing AI OS | TECHNOLOGIE | 0.85 | STATIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Guillaume Dumortier | PERSONNE | rôle | Auteur de la newsletter LinkedIn *Growth Marketing Fit* ; a conçu et exploité un système d'IA marketing interne (« Marketing AI OS ») pour une équipe d'une soixantaine de personnes, dont il publie le journal de pannes en août 2026 | AJOUT |
| Marketing AI OS | TECHNOLOGIE | définition | Système d'IA marketing interne bâti dans Claude (2026) : quatre couches — vérité, production, vérification, distribution interne —, une trentaine de skills contenu et vente, une douzaine de modules de source de vérité, sept agents dont six ne font que contrôler, un plugin terminal et une application navigateur portant la même connaissance, plus une orchestration enchaînant trois ou quatre actifs en un *campaign bundle* | AJOUT |
| couche de vérité | CONCEPT | définition | Ensemble de documents décrivant ce que l'entreprise sait réellement — faits produit, positionnement, cibles et anti-cibles, règles de voix, preuves clients — tenu séparément de tout ce qui produit du contenu, chaque document ayant un propriétaire humain, une version et une date. Règle associée : rien de ce qui produit du contenu n'a le droit de contenir un fait, il doit le demander | AJOUT |
| vérification en monde clos | CONCEPT | définition | Propriété structurelle de tout vérificateur automatique : il ne peut se prononcer que sur ce que ses sources couvrent. Confronté à une affirmation hors couverture, il ne trouve aucune contradiction et rend un verdict favorable indiscernable d'une vraie vérification — il certifie l'erreur au lieu de la manquer | AJOUT |
| déclaration de couverture | CONCEPT | définition | Contrainte de format imposée à un vérificateur automatique : interdiction de renvoyer un « pass » nu, obligation de clore chaque rapport par le nombre d'affirmations contrôlées, le nombre réellement apparié à ses sources, celles hors de sa juridiction et celles possédées par aucune source du système. « Je ne peux pas vérifier ceci » devient un résultat de première classe | AJOUT |
| vérification inter-actifs | CONCEPT | définition | Contrôle de niveau lot lisant les actifs les uns contre les autres plutôt que contre la couche de vérité. Nécessaire parce que deux actifs individuellement corrects et traçables peuvent se contredire — une date dans le communiqué, une autre dans l'article de blog — rendant le lot inexpédiable, ce que la vérification par actif ne peut pas détecter par construction | AJOUT |
| échec silencieux | CONCEPT | définition | Classe de risque propre aux systèmes à base de LLM : contrairement au logiciel traditionnel qui plante, ils continuent avec assurance à qualité réduite et produisent une sortie plausible. Cas rapporté : une constante vidée faisait supprimer tous les chiffres de tous les prompts pendant plusieurs releases, panne longtemps imputée à tort à la tendance du modèle à inventer des chiffres | AJOUT |
| Growth Marketing Fit | DOCUMENT | rôle | Newsletter LinkedIn de Guillaume Dumortier (~1 300 abonnés en août 2026), support de publication du retour d'expérience sur le Marketing AI OS | AJOUT |
