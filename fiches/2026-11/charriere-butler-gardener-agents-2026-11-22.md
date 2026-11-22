---
themes: [architecture-construction, strategie-frameworks]
source: "X (@nichochar)"
---
# charriere-butler-gardener-agents-2026-11-22

## Veille

Article publié sur X le **22 novembre 2026** par **Nicholas Charriere** (@nichochar, Notion, ex-Mocha, Cruise, Pinterest), environ 1 300 mots, relayé par Harrison Chase. Il propose une typologie des agents en deux catégories : (A) les **butlers** (majordomes), attachés à une personne, généralistes et personnalisés ; (B) les **gardeners** (jardiniers), attachés à un lieu partagé qui survit à ses occupants — un dépôt de code, un CRM, le « cerveau » d'une entreprise. Test proposé : *« when a person leaves the company, does the agent leave with them? »*

L'auteur en tire trois thèses : (1) une application ne peut pas être un butler, et un butler ne doit pas jardiner ; (2) le pull request est le modèle de la frontière entre les deux, le gardener gardant le dernier mot sur ce qui entre dans le jardin ; (3) les protocoles agent-à-agent passeront de MCP en CRUD à des **messages d'intention** (lecture : « voici mon intention, donne-moi le contexte » ; écriture : « voici le changement sémantique visé »). Il reprend le « curator agent » de Harrison Chase et le « knowledge factory » de LangChain, et cite **Vercel Board** comme exemple d'espace de coordination d'essaims.

Le texte prolonge, côté entreprise, les fiches sur l'IA personnelle (Sarver, septembre 2026) et sur la mémoire d'agent partagée du lot SFEIR de novembre 2026.

## Titre Article

Butler agents and gardener agents

## Date

2026-11-22

## URL

https://x.com/nichochar/status/2124545461034033258

## Keywords

agents butler, agents gardener, agent majordome, agent jardinier, agent personnel, agent de lieu partagé, curator agent, knowledge factory, connaissance d'entreprise, cerveau d'entreprise, pull request, messages d'intention, protocoles agent-à-agent, MCP CRUD, essaims d'agents, bring your own agent, SaaS headless, revue de code automatisée, tarification au token, wiki auto-mis à jour

## Authors

Nicholas Charriere (@nichochar) — Notion ; précédemment Mocha (YC S23), Cruise, Pinterest.

## Ton

Profil : essai de positionnement à la première personne, registre conversationnel en anglais, publié sous forme d'article X, public cible bâtisseurs de produits IA et responsables produit SaaS. L'argument repose sur une métaphore filée (majordome / jardin, mauvaises herbes, terrain qui survit aux jardiniers) et sur des tests simples formulés en une phrase (« l'agent part-il avec la personne ? », « à qui répond-il : une personne ou un lieu ? »). L'auteur situe explicitement son point de vue (« I work at Notion, so this is the garden I think about the most ») et assume le statut de prédiction de ses thèses sur les protocoles. Le texte s'appuie sur des citations intégrées (Ali Spittel, Harrison Chase, annonce Vercel) plutôt que sur des données chiffrées ; aucune mesure n'est fournie. Il se termine sur une formule-slogan qui renverse la citation d'ouverture : *« bring your own agent to use my thing. It just has to ask my gardener first. »*

## Pense-betes

- **Point de départ** : citation d'Ali Spittel, *« i really don't want to use your agent, i want to use my agent to use your thing »*. Explication de l'auteur : un butler est attaché à une personne, il doit donc couvrir toutes ses applications — une application ne peut pas en être un.
- **Butlers** : OpenClaw, Grok Bot, Muse, Duet, Dot. Hypergénéralistes et hyperpersonnalisés ; mono-joueur, donc plus simples à construire. Catégorie revendiquée par les labs, qui subventionnent les abonnements individuels par rapport à l'API équipe.
- **Gardeners** : responsables d'un lieu partagé, horizon long (désherber, répartir l'attention dans le temps). Exemple côté code : un bot de revue comme **Greptile** ; les workflows partagés d'un dépôt (« factory ») sont des gardeners.
- **Le pull request comme frontière** : le butler déclare une intention de changement, le processus du jardin décide. C'est ce qui permet à dix agents de travailler sur un même dépôt.
- **Butlers shouldn't garden** : reprise de Harrison Chase — des agents poursuivant leurs propres buts rendent la connaissance partagée « unruly and full of contradictions ». Un gardener unique est plus efficace et plus fiable que dix butlers.
- **Levier composé** : un butler ne vaut que le jardin où il travaille (wiki périmé, base mal typée → mauvaises réponses quel que soit le modèle).
- **SaaS** : l'auteur ne croit pas au SaaS « headless » parcouru 24/7 par des butlers à grande échelle (10 → 1 000 butlers) ; le jardin doit rester découplé, protégé, autonome.
- **Achat** : butler = tokens par individu ; gardener = workflows à l'échelle, liés aux comptes entreprise, payés à la qualité du résultat et aux garanties sur les données.
- **Gardeners de connaissance (Notion)** : wiki qui se met à jour, agent qui valide le typage et la fraîcheur d'une base, skills de compte rendu de réunion qui évoluent. Question ouverte : comment protéger la base de butlers sur modèles bon marché qui la dégradent ?
- **Prédiction** : intent-based messages au lieu de MCP CRUD ; seul le gardener a le dernier mot. Exemple émergent : Vercel Board (forums, flux, canaux pour essaims). Voir [[mémoire d'agent]].

## RésuméDe400mots

Nicholas Charriere, qui travaille chez Notion, soutient que les agents IA se scindent en deux catégories qui se ressemblent techniquement — des boucles avec outils tendues vers un but — mais qui n'ont pas la même fonction. Les confondre produit la frustration résumée par Ali Spittel : les utilisateurs ne veulent pas de l'agent de chaque application, ils veulent que leur propre agent utilise ces applications.

La première catégorie est celle des butlers, des majordomes. Depuis OpenClaw, la catégorie a explosé (Grok Bot, Muse, Duet, Dot). Un butler sert une seule personne : il comprend ses tâches, retient ses préférences, s'adapte à son style. Une grande part du travail intellectuel relève de ce registre : on part d'un but, on le découpe en tâches et l'on produit un artefact (pull request, présentation, document) selon un processus privé et personnalisé. Les butlers sont mono-joueurs, ce qui les rend plus faciles à construire ; l'auteur estime que cette catégorie revient aux laboratoires, dont les abonnements individuels offrent des tokens plus subventionnés que leur API.

La seconde catégorie est celle des gardeners, des jardiniers. Ils ne sont pas attachés à une personne mais à un lieu partagé qui survit à ceux qui y travaillent : un dépôt de code, un CRM, la mémoire institutionnelle d'une entreprise. Le test proposé : quand une personne quitte l'entreprise, l'agent part-il avec elle ? Le jardinier reste avec le terrain.

Le code a pris de l'avance. Chaque développeur a son agent de codage configuré à sa façon — un butler — mais tous travaillent dans le même dépôt. Les agents responsables du dépôt, comme un bot de revue de code tel que Greptile, sont des gardeners. Le pull request incarne la frontière : le butler annonce ce qu'il veut changer, le processus du jardin décide.

D'où la règle : un butler ne doit pas jardiner. Citant Harrison Chase et son « curator agent », l'auteur juge que des agents poursuivant leurs propres objectifs rendent la connaissance partagée incohérente. Or un butler ne vaut que le jardin dans lequel il opère. L'auteur doute que les SaaS deviennent de simples back-ends parcourus en continu par des milliers de butlers ; il anticipe un jardin découplé, protégé et autonome, acheté à la qualité du résultat plutôt qu'au token.

Le prochain jardin est la connaissance d'entreprise : wikis qui se mettent à jour, agents qui valident les bases, skills de réunion évolutives. Charriere prédit que les protocoles agent-à-agent passeront d'API CRUD exposées via MCP à des messages d'intention, le jardinier gardant le dernier mot. Question finale : un agent répond-il à une personne ou à un lieu ?

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Nicholas Charriere | PERSONNE | publie | Butler agents and gardener agents | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Nicholas Charriere | PERSONNE | travaille_chez | Notion | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| agent butler | CONCEPT | est_variante_de | agents IA | TECHNOLOGIE | 0.88 | ATEMPOREL | inféré |
| agent gardener | CONCEPT | est_variante_de | agents IA | TECHNOLOGIE | 0.88 | ATEMPOREL | inféré |
| OpenClaw | TECHNOLOGIE | est_instance_de | agent butler | CONCEPT | 0.92 | DYNAMIQUE | déclaré_article |
| Greptile | TECHNOLOGIE | est_instance_de | agent gardener | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| curator agent | CONCEPT | est_variante_de | agent gardener | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Nicholas Charriere | PERSONNE | s_inspire_de | Harrison Chase | PERSONNE | 0.92 | STATIQUE | déclaré_article |
| Harrison Chase | PERSONNE | a_créé | knowledge factory | METHODOLOGIE | 0.85 | STATIQUE | déclaré_article |
| knowledge factory | METHODOLOGIE | utilise | curator agent | CONCEPT | 0.82 | ATEMPOREL | inféré |
| pull request | METHODOLOGIE | permet | coordination de plusieurs agents sur un même dépôt | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Nicholas Charriere | PERSONNE | affirme_que | un butler ne doit pas entretenir un espace partagé : un gardener unique est plus efficace et plus fiable | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Nicholas Charriere | PERSONNE | affirme_que | la catégorie des butlers revient aux laboratoires, dont les abonnements individuels subventionnent les tokens | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Nicholas Charriere | PERSONNE | prédit | les protocoles agent-à-agent passeront d'API CRUD exposées via MCP à des messages d'intention | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| messages d'intention | CONCEPT | remplace | MCP | TECHNOLOGIE | 0.75 | DYNAMIQUE | inféré |
| Nicholas Charriere | PERSONNE | s_oppose_à | SaaS headless parcouru par des butlers à grande échelle | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| agent gardener | CONCEPT | s_applique_à | connaissance d'entreprise | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Vercel | ORGANISATION | publie | Vercel Board | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Vercel Board | TECHNOLOGIE | permet | coordination d'essaims d'agents | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |
| Nicholas Charriere | PERSONNE | référence | Ali Spittel | PERSONNE | 0.90 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Nicholas Charriere | PERSONNE | rôle | Notion ; ex-Mocha (YC S23), Cruise, Pinterest | AJOUT |
| agent butler | CONCEPT | définition | Agent attaché à une personne, généraliste et personnalisé, mono-joueur (OpenClaw, Grok Bot, Muse, Duet, Dot) | AJOUT |
| agent gardener | CONCEPT | définition | Agent attaché à un lieu partagé qui survit à ses occupants (dépôt, CRM, connaissance d'entreprise) ; test : l'agent part-il avec la personne ? | AJOUT |
| curator agent | CONCEPT | définition | Terme de Harrison Chase pour l'agent d'arrière-plan qui maintient la connaissance d'une entreprise | AJOUT |
| messages d'intention | CONCEPT | définition | Lecture : « mon intention, donne-moi le contexte » ; écriture : « le changement sémantique visé » ; décision finale au gardener | AJOUT |
| Vercel Board | TECHNOLOGIE | catégorie | Message board sécurisé pour humains et agents, permissions, essaims (expérimental, novembre 2026) | AJOUT |
| Greptile | TECHNOLOGIE | catégorie | Bot de revue de code partagé à l'échelle du dépôt | AJOUT |
