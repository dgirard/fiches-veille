---
themes: [transformation-adoption, agents-codage-ia-skills, philosophie-societe]
source: "donnfelker.substack.com (Donn Felker)"
---
# felker-evaporation-software-engineering-agentic-builder-2026-09-14

## Veille

Essai de **Donn Felker** publié le **14 septembre 2026** sur son Substack (~4 400 mots, sous-titre *« Your identity was built on a bottleneck »*). L'auteur, responsable plateforme IA chez **Polygon** et anciennement chez **Tinder**, spécialiste Android pendant plus de dix ans, date sa bascule de **juillet 2025** par trois faits : un SaaS construit sans écrire une ligne, une migration de bibliothèque de threading chez Tinder ramenée de **6-8 heures** à **10 minutes** par un prompt de **2 000 mots**, et des non-techniciens (un CFO, un gérant de salle de sport) livrant des produits complets. **(A)** Il en tire un cadre psychologique — *occupational categorization*, *professional identity centrality* — pour expliquer l'anxiété des ingénieurs : *« It was never about coding, it's about the ability to execute »*. **(B)** Il propose une image de **pendule de levier** entre produit et ingénierie : l'IA déplace le levier initial vers le produit, la complexité et l'échelle le ramènent vers l'ingénierie, et chaque oscillation s'amortit à mesure que garde-fous et architecture sont codifiés. **(C)** Il décrit un rôle hybride, l'**agentic builder**, et un parcours en deux étapes (codifier son savoir en skills, passer d'une pensée de spécialiste à une pensée de système) avec un horizon affiché de **six mois**. Prolonge le passage à l'*agentic engineering* décrit dans [[karpathy-vibe-coding-agentic-engineering-software-3-0-2026-04-29]] et la chute des frontières entre métiers de [[sfeir-ia-frontieres-metiers-skill-based-organisation-2026-08-01]].

## Titre Article

The Evaporation of Software Engineering (and the Rise of the Agentic Builder)

## Date

2026-09-14

## URL

https://donnfelker.substack.com/p/the-evaporation-of-software-engineering

## Keywords

agentic builder, Agentic Product Engineer, identité professionnelle, catégorisation occupationnelle, centralité identitaire, pendule de levier, oscillation amortie, produit vs ingénierie, non-techniciens bâtisseurs, vibe coding, codification en skills, prompt réutilisable, migration de code, orchestrateur, pensée système, penser comme une entreprise, build vs buy, Not Invented Here, spécialisation, généraliste, guardrails, garde-fous agentiques, Destructive Command Guard, versionnement, observabilité, Claude Cowork, Base44, Tinder, Polygon, exécution

## Authors

Donn Felker (responsable plateforme IA chez Polygon, ex-Tinder, ex-co-animateur du podcast Fragmented), sur son Substack donnfelker.substack.com.

## Ton

**Profil** : essai personnel de carrière, à la première personne, adressé aux ingénieurs de plus de quarante ans qui partagent le parcours de l'auteur. Public : développeurs spécialisés, responsables produit, non-techniciens qui construisent avec des agents.

**Style** : récit à scènes — le bureau repoussé, la marche pour *« clear my head »*, le CFO qui ne sait pas où est son code — enchaîné à un exposé structuré par sous-titres et à une section finale d'instructions numérotées. Le texte convoque des notions de psychologie sociale (*occupational categorization*, *professional identity centrality*), des citations d'autorité (Heinlein, Tony Robbins), l'effet Dunning-Kruger, et deux analogies filées : le pendule amorti et l'entraîneur sportif. Le registre alterne l'aveu (*« I was dead wrong »*, *« I was in shock »*) et l'injonction (*« It's time to become an agentic builder »*).

**Position épistémique** : les preuves sont des anecdotes de première main, non chiffrées au-delà des deux mesures de la migration Tinder, et données comme représentatives. Les cas non-techniciens sont rapportés avec leur point de rupture (limite de session Cowork, Google Drive inadapté comme stockage), ce qui nourrit la thèse du pendule. L'horizon de six mois est asséné sans base. L'auteur nuance sur deux points : les spécialistes ne disparaissent pas entièrement, et chaque nouvelle version de modèle relance l'oscillation. La proportion **30 % construction / 70 % positionnement-marketing-vente** est posée comme principe, sans source.

## Pense-betes

- **Trois déclencheurs datés de juillet 2025** : un SaaS complet sans écrire de code ; un prompt de 2 000 mots — *« which we'd now call a Skill »* — qui exécute en 10 minutes une migration de bibliothèque de threading que chaque instance coûtait 6 à 8 heures à un ingénieur, répétée des centaines de fois dans la base de code de Tinder ; des non-techniciens qui livrent des produits. Le récit de bascule rejoint celui de [[cherny-sequoia-coding-is-solved-loops-printing-press-2026-05]].
- **Formule centrale** : *« Coding was just a gatekeeper. »* Ce qui sépare les rêveurs des faiseurs est la capacité d'exécution ; le code n'en était que le péage.
- **Le cadre identitaire** : la catégorisation occupationnelle compresse une personne en un rôle (*« Android Developer »*) ; la centralité identitaire professionnelle en fait le socle de la valeur perçue. D'où le double bind formulé : ne pas utiliser l'IA, c'est être distancé ; l'utiliser, c'est entraîner son remplaçant.
- **Le pendule de levier** : avant l'IA, l'ingénierie fixait le rythme et détenait le levier ; l'agent déplace le levier initial vers le produit (un MVP en un après-midi). La complexité, l'échelle et l'économie des systèmes le ramènent vers l'ingénierie, qui corrige, pose architecture et garde-fous, puis le rend au produit. Chaque retour est plus court — *damped oscillation* — mais une nouvelle version de modèle relance le mouvement.
- **Deux cas où le pendule revient** : un CFO qui a construit son outil financier dans une seule session Claude Cowork pendant **deux mois**, jusqu'à saturation de l'environnement, sans savoir où vit son code (retrouvé dans un dépôt GitHub privé) ; un photographe qui a branché Google Drive comme stockage de médias dans une application Base44, choix que l'agent a suivi sans objection et que les frais de transfert rendaient intenable. L'agent *« will follow your lead »*.
- **Analogie de l'entraîneur** : bouger suffit au début, puis on plafonne ou on se blesse ; l'ingénieur corrige la forme et fixe le programme, puis s'efface ; les visites suivantes sont plus courtes.
- **Le rôle qui émerge** : ni ingénieur ni produit, mais les deux — *« the engineer who thinks like a product person and the product person who thinks like an engineer »*. Côté ingénierie, le titre proposé est *Agentic Product Engineer*. Les purs spécialistes des deux extrêmes sont donnés comme exposés ; les spécialistes profonds subsistent mais avec des compétences hors de leur domaine. Cette cartographie des rôles peut se lire avec [[ng-ai-engineering-skills-map-2026-08-14]].
- **Parcours en deux étapes, commun aux deux profils** : (1) codifier son savoir en skills, templates et procédures exécutables par des humains ou des agents — *« you're making yourself scalable »*, passage d'opérateur à orchestrateur ; (2) passer de la pensée de spécialiste à la pensée de système, ce que l'auteur nomme complexité cognitive.
- **Pour l'ingénieur** : lâcher l'identité liée à un langage ou une plateforme (l'auteur n'a pas touché Android ni Kotlin depuis six mois), traiter chaque compétence comme une brique Lego, arbitrer build vs buy en tenant compte de la maintenance, penser ROI, acquisition, rétention. Position voisine de celle d'[[osmani-google-new-sdlc-vibe-coding-agentic-engineering-2026-05]] sur le passage à l'ingénierie agentique.
- **Pour le non-technicien** : demander à l'agent à chaque blocage, et exiger six choses qu'il ne sait pas demander seul — architecture maintenable, garde-fous, sauvegardes, contrôle de version, gouvernance, observabilité. Recommande d'installer un Destructive Command Guard.
- ⚠️ **Le délai de six mois est répété trois fois sans justification** ; il fonctionne comme un ressort rhétorique, pas comme une prévision étayée.
- **Premier geste conseillé** : lister ce qu'on fait manuellement et qu'on redoute, en choisir une chose, demander à Claude ou ChatGPT *« help me turn this into a skill »* et se laisser interviewer. Cinq minutes.

## RésuméDe400mots

Donn Felker, responsable de la plateforme IA chez Polygon, ancien de Tinder et spécialiste Android pendant dix ans, publie le 14 septembre 2026 un essai sur la disparition du génie logiciel tel qu'il l'a pratiqué. Il date sa prise de conscience de juillet 2025, par trois faits. Il a construit un SaaS complet sans écrire une ligne de code. Chez Tinder, un prompt de deux mille mots a exécuté en dix minutes une migration de bibliothèque de threading qui prenait six à huit heures par instance, sans erreur. Enfin, il a vu des non-techniciens livrer des produits réels : un directeur financier a bâti son outil d'opérations financières avec l'application Claude, un gérant de salle de sport sa plateforme de coaching. Sa conclusion : il ne s'agissait jamais de coder mais d'exécuter, le code n'était qu'un péage.

L'essai explique ensuite l'anxiété des ingénieurs par deux notions de psychologie sociale. La catégorisation occupationnelle résume une personne à son métier ; la centralité identitaire professionnelle fait de ce métier le socle de sa valeur. Quand le travail quotidien passe à un agent, l'identité vacille : être distancé ou entraîner son remplaçant.

Felker propose l'image d'un pendule de levier entre produit et ingénierie. L'agent déplace le levier initial vers le produit, qui obtient un prototype en un après-midi. Mais la complexité et l'échelle ramènent le levier vers l'ingénierie : un CFO bloqué après deux mois dans une même session Claude Cowork sans savoir où vit son code, un photographe dont l'application Base44 stockait ses médias sur Google Drive à un coût de transfert intenable. L'ingénieur corrige, pose architecture et garde-fous, puis rend la main. Chaque oscillation s'amortit, jusqu'à la prochaine version de modèle.

Le rôle qui se dessine au point d'équilibre est celui de l'agentic builder, hybride d'ingénieur et de responsable produit. Les purs spécialistes des deux extrêmes sont donnés comme menacés. Le parcours proposé comporte deux étapes : codifier son savoir en skills et procédures exécutables par des agents, ce qui rend l'individu scalable et le fait passer d'opérateur à orchestrateur ; puis adopter une pensée de système, business pour l'ingénieur, ingénierie pour le non-technicien, avec une liste de six exigences à formuler à l'agent : architecture, garde-fous, sauvegardes, versionnement, gouvernance, observabilité.

L'auteur fixe un horizon de six mois pour opérer la transition et conclut sur la figure du bâtisseur capable de lire un bilan comptable et une trace d'exécution.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Donn Felker | PERSONNE | travaille_chez | Polygon | ORGANISATION | 0.90 | DYNAMIQUE | inféré |
| Donn Felker | PERSONNE | travaille_chez | Tinder | ORGANISATION | 0.92 | STATIQUE | déclaré_article |
| Donn Felker | PERSONNE | affirme_que | "It was never about coding, it's about the ability to execute" | CITATION | 0.97 | ATEMPOREL | déclaré_article |
| Donn Felker | PERSONNE | affirme_que | "Coding was just a gatekeeper" | CITATION | 0.97 | ATEMPOREL | déclaré_article |
| Donn Felker | PERSONNE | mesure | migration de bibliothèque de threading chez Tinder ramenée de 6-8 heures à 10 minutes par un prompt de 2 000 mots, juillet 2025 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Donn Felker | PERSONNE | a_créé | agentic builder | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| agentic builder | CONCEPT | est_instance_de | rôle hybride ingénierie et produit | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| agentic builder | CONCEPT | remplace | spécialisation technique | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Donn Felker | PERSONNE | a_créé | pendule de levier | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| pendule de levier | CONCEPT | affirme_que | l'IA déplace le levier initial de l'ingénierie vers le produit, la complexité et l'échelle le ramènent vers l'ingénierie | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| pendule de levier | CONCEPT | est_basé_sur | oscillation amortie | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| identité professionnelle | CONCEPT | est_basé_sur | catégorisation occupationnelle | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| identité professionnelle | CONCEPT | est_basé_sur | centralité identitaire professionnelle | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| agents IA | TECHNOLOGIE | réduit | identité professionnelle | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| vibe coding | METHODOLOGIE | permet | prototype par non-technicien | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| vibe coding | METHODOLOGIE | observé_dans | Claude Cowork | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| vibe coding | METHODOLOGIE | observé_dans | Base44 | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Donn Felker | PERSONNE | affirme_que | le développement d'un produit logiciel a toujours représenté 30 % du problème, les 70 % restants étant positionnement, marketing et vente | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Donn Felker | PERSONNE | recommande | codification du savoir en skills | METHODOLOGIE | 0.95 | ATEMPOREL | déclaré_article |
| codification du savoir en skills | METHODOLOGIE | permet | passage d'opérateur à orchestrateur | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Donn Felker | PERSONNE | recommande | pensée système | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Donn Felker | PERSONNE | recommande | exiger de l'agent architecture maintenable, garde-fous, sauvegardes, contrôle de version, gouvernance et observabilité | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Donn Felker | PERSONNE | recommande | Destructive Command Guard | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Donn Felker | PERSONNE | prédit | six mois pour passer de spécialiste à agentic builder | AFFIRMATION | 0.90 | STATIQUE | déclaré_article |
| Donn Felker | PERSONNE | affirme_que | "The ability to stand where the pendulum stops" | CITATION | 0.95 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Donn Felker | PERSONNE | rôle | Responsable plateforme IA chez Polygon, ex-Tinder ; ex-spécialiste Android (Kotlin), ex-co-animateur du podcast Fragmented ; auteur de l'essai | AJOUT |
| Polygon | ORGANISATION | secteur | Blockchain / cryptomonnaies ; employeur actuel de l'auteur | AJOUT |
| Tinder | ORGANISATION | rôle | Terrain de la migration de threading pilotée par prompt en juillet 2025 | AJOUT |
| agentic builder | CONCEPT | définition | Rôle hybride qui combine acumen business et compétence d'ingénierie pour exécuter avec des agents ; variante côté ingénierie nommée Agentic Product Engineer | AJOUT |
| pendule de levier | CONCEPT | mécanisme | Levier initial vers le produit (prototype rapide), retour vers l'ingénierie sur complexité et échelle, oscillation amortie par codification des garde-fous, relancée à chaque nouveau modèle | AJOUT |
| identité professionnelle | CONCEPT | mécanisme | Catégorisation occupationnelle + centralité identitaire ; menacée quand le travail quotidien est délégué à un agent | AJOUT |
| vibe coding | METHODOLOGIE | limite | Suffit au MVP ; échoue sur la persistance de session, la localisation du code et les choix d'infrastructure à l'échelle | AJOUT |
| Claude Cowork | TECHNOLOGIE | rôle | Environnement dans lequel un CFO a construit et déployé son outil financier sur une session de deux mois, jusqu'à saturation | AJOUT |
| Base44 | TECHNOLOGIE | catégorie | Plateforme de vibe coding ; CRM et portail d'un studio photo, stockage Google Drive inadapté | AJOUT |
| codification du savoir en skills | METHODOLOGIE | étapes | Lister ce qu'on fait manuellement, en choisir une chose, demander à l'agent de la transformer en skill par interview, l'utiliser, répéter | AJOUT |
| Destructive Command Guard | TECHNOLOGIE | usage | Garde-fou empêchant un agent d'exécuter des commandes destructrices (ex. suppression d'une base de production) | AJOUT |
| agents IA | TECHNOLOGIE | effet | Délégation du travail quotidien de codage ; déplacement du levier produit/ingénierie | AJOUT |
