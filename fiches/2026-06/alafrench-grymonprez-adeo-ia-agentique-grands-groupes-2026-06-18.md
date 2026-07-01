# alafrench-grymonprez-adeo-ia-agentique-grands-groupes-2026-06-18

## Veille

Entretien podcast « À la French » (chaîne tech francophone, enregistré au DevSummit) avec Mathieu Grymonprez, Global CDO du groupe Adeo (Leroy Merlin, Obramat, Weldom). Comment un groupe de retail familial centenaire embrasse la vague de l'IA agentique : culture vs structure, accountability, coût des tokens et FinOps, lock-in de l'intelligence d'entreprise, mémoire d'entreprise et orchestration d'agents. Domaine : transformation digitale, IA agentique, retail, stratégie SI.

## Titre Article

Comment l'IA agentique bouscule les Grands Groupes ? Partie 2/2 #DevSummit

## Date

2026-06-18

## URL

https://www.youtube.com/watch?v=p4yg2JCAw-s

## Keywords

IA agentique, transformation digitale, CDO, retail, Adeo, Leroy Merlin, Decathlon, accountability, make vs buy, coût des tokens, FinOps, lock-in, mémoire d'entreprise, orchestration d'agents, Claude Code, Vertex AI, context engineering, souveraineté, RFID end-to-end, ROI de l'IA

## Authors

Mathieu Grymonprez (Global CDO, groupe Adeo) — invité ; Jean-Baptiste Kempf, Steeve Morin, Mehdi Medjaoui (hôtes du podcast « À la French »)

## Ton

**Profil** : conversation à la première personne, registre oral et familier (podcast tech entre pairs), niveau technique élevé mais volontairement vulgarisé. Perspective de praticien-dirigeant qui « a mis les mains dedans ».

**Style** : récit d'expérience ponctué d'anecdotes (le crash brésilien de 2012, le premier firewall Check Point, le vrac de vis chez Leroy Merlin), d'humour récurrent (le running gag « Hermès » l'agent IA vs la maison de luxe ; « Allatoubon » sur les anglicismes ; les « vendeurs de pioches ») et de formules mémorables. Métaphores marquantes : « la confiance se gagne en gouttes, se perd en litres », « 4 jours d'ingénierie, 6 ans de surf », « payer pour voir », « je ne suis pas une chaîne de Markov », « quand ce n'est pas logique, c'est historique » (citation attribuée au directeur du Louvre), Boris Cyrulnik (« pour apprendre les maths à Paul, comprends d'abord comment Paul réfléchit »). **Autorité** : 26 ans dans la boîte, 8 ans CDO, parcours ingénieur réseau-sécurité → expat Brésil → stratégie groupe. **Public cible** : CDO, CTO, dirigeants tech de grands groupes en transformation.

## Pense-betes

- Le **Make vs Buy** chez Adeo est « au moins à 70 % » de make : pas de différenciation compétitive en full buy.
- Toute transfo se gagne sur **deux terrains en même temps** : culture ET structure. Le même playbook (qui a porté la transfo digitale : cycle en V → agile, product, plateformes, tech radar, API, microservices) se rejoue avec l'IA.
- **Accountability** (responsabilité) reste humaine et liée aux organisations, jusqu'au legal : « je ne veux pas qu'un mec me dise c'est cassé en prod mais c'est pas de ma faute, c'est l'agent ».
- La **dette de documentation** (docs produit médiocres, docs process inexistantes) « va nous reclaquer à la figure très vite » : un agent ne peut pas lire une doc qui n'existe pas.
- Mathieu **ne parle jamais technique au board** : il parle expérience client, ROI, rentabilité, investissement.
- Il **ne demande même pas de budget supplémentaire** pour l'IA : les gains (compresser les tickets JIRA, les ops) financent le nouveau (« à flat »). Logique de **reuse** : le temps gagné est réinvesti au service du vendeur en magasin / du client.
- Pas de fantasme « virer tous les développeurs grâce à Claude Code » : il anticipe au contraire une **avalanche de demandes** — les projets en P10/P15 passent en P2 car « plus aucun projet ne coûte trop cher ».
- Sa grosse **« claque »** : Claude Code (recréer une VM sans avoir codé depuis longtemps), puis voir Karpathy et d'autres « shipper » davantage, puis son agent perso **« Hermes »** (à mémoire).
- **Coût des tokens** : confiant qu'il baissera comme l'a fait le FinOps cloud (muscle FinOps construit après les requêtes BigQuery à 30k). Leviers : puces d'inférence (TPU Google), modèles open source qui rattrapent (écart ~9 mois Chine/Anthropic), modèles distillés tournant sur laptop (Gemma 4, MoE 26 Mds / 4 Mds actifs, « conçu à Paris »). On n'a pas besoin d'un modèle frontière pour les ~300 produits digitaux du groupe.
- **Variation de modèles = vrai problème de prod** : à modèle changé, il faut retester (résultats différents) ; les fournisseurs requantisent / downgradent / routent vers de la capacité moindre. Ils ont arrêté d'upgrader quand c'était « good enough » (tri marketplace : 15 M produits → 7 M publiés, via OpenAI). On veut « être véloce, mais à ses termes ».
- **Conscience de la prod** : Google en a une que les startups (OpenAI, Anthropic) n'ont pas encore (ex. bug de limites Codex/Claude cramées en 1h au lieu d'une journée, reset à 17h).
- Sa **plus grande inquiétude** : le **lock-in de l'intelligence de l'entreprise** (config de la boîte dans un harnais agentique / « adeo.md » ; « refaire l'ERP de l'IA »). Parades : Kubernetes standard (pas de Cloud Functions propriétaires), test régulier des API chez d'autres hyperscalers, attention à la **gestion de la mémoire** (froide/chaude, context engineering, où c'est stocké, qui en est propriétaire).
- **Brique open source manquante** : l'**orchestration d'agents** (registry, cycle de vie, permissions « quel agent a le droit de faire quoi », partage de skills à l'échelle de la boîte). n8n / MCP n'en couvrent qu'une petite partie.
- **Mémoire d'entreprise** (« company brain ») : « quand ce n'est pas logique, c'est historique » — capturer le contexte des décisions. Ex. Leroy Merlin ne vend pas de matelas car la boîte est **pilotée au CA au mètre carré** (un lit prend trop de place pour ce qu'il rapporte) ; à mettre dans le company brain pour éviter qu'un futur chef de produit ne re-pitche l'idée.
- **RAG / contrôle d'accès** : difficile de savoir à quoi la personne qui pose la question a droit (plusieurs niveaux d'autorisation) — problème non résolu des chatbots d'entreprise.
- **Stack IA** : Vertex AI (GCP), sélection du modèle selon le besoin. Toujours regarder « la porte de sortie » (souveraineté).
- **Conseil à un autre CDO** : la transfo est **sur-mesure** (culture, capital disponible) ; identifier le **différentiel compétitif réel** dans l'expérience client. Si le board ne sait même pas l'exprimer → IT de base / maintenance en condition opérationnelle. S'il sait l'exprimer → tout miser, faire un truc complet end-to-end, créer le précédent. Comprendre la techno surtout « pour ne pas se faire enfler par les vendeurs et la hype ».
- **Décathlon RFID end-to-end** : succès car ils produisent une grande partie de leurs produits (puce intégrée en entrée de chaîne industrielle) jusqu'à la sécu en aval. Métrique simple : gain de temps sur toute la chaîne (humains + client) = ROI instantané. Adeo ne fabrique que la moitié → faire changer l'outil industriel de tous les fournisseurs est très compliqué.

## RésuméDe400mots

Deuxième partie d'un épisode du podcast « À la French » enregistré au DevSummit, cet entretien réunit Mathieu Grymonprez, Global CDO du groupe Adeo (Leroy Merlin, Obramat, Weldom), et les hôtes Jean-Baptiste Kempf (créateur de VLC), Steeve Morin et Mehdi Medjaoui. Mathieu, 26 ans dans la maison et 8 ans CDO, retrace un parcours d'ingénieur réseau-sécurité (premier firewall Check Point) devenu pilote de la « Digital Tech and Data » : après avoir résolu en urgence un crash de bases Oracle au Brésil (2012) puis refondu le SI local en six ans d'expatriation, il a rationalisé les 24 SI / sites / PIM du groupe en plateformes digitales (customer & commerce, supply chain, retail, corporate) appuyées sur un tech radar, des API documentées et des microservices (devenus « big products »).

Sa thèse : **toute transformation se gagne sur deux terrains simultanés, la culture et la structure**, et le playbook de la transfo digitale (cycle en V → agile, product, davantage de make que de buy) se rejoue avec l'IA. Côté culture : se reconfigurer pour embrasser la techno, garder un jugement critique et surtout l'**accountability** — la responsabilité reste humaine, « ce n'est pas la faute de l'agent ». Côté structure : combler la dette de documentation, gérer droits et permissions des agents. Mémoire de l'échec du « Retail Apocalypse » (Amazon, e-commerce négocié trop tard), le mot d'ordre est « on ne va pas se refaire avoir » : écouter sérieusement l'IA, mais avec les mêmes valeurs (pragmatisme, service client, marque leader). Si ChatGPT prépare mieux le panier que l'appli maison, « c'est mon problème ».

Au board, Mathieu ne parle jamais technique mais expérience client et ROI ; il ne demande même pas de budget IA, finançant le nouveau par les gains (compression des tickets JIRA), dans une logique de reuse au service du vendeur en magasin. Il n'anticipe pas la fin des développeurs mais une avalanche de demandes (les P10 deviennent P2). Sur les coûts, il est confiant : le FinOps des tokens suivra celui du cloud, porté par les puces d'inférence (TPU) et des modèles open source qui rattrapent (Gemma 4 sur laptop). Mais la variation des modèles est un vrai problème de prod (retests, requantisation, downgrade silencieux), et Google a une « conscience de la prod » que n'ont pas encore OpenAI ou Anthropic. Sa plus grande inquiétude : le **lock-in de l'intelligence d'entreprise** (harnais agentique, « adeo.md »), d'où l'attention au Kubernetes standard, à la portabilité des API et à la mémoire. Il pointe la brique open source manquante — l'orchestration d'agents (registry, cycle de vie, permissions, skills) — et la mémoire d'entreprise (« quand ce n'est pas logique, c'est historique »). Conseil final : la transfo est sur-mesure ; comprendre la techno surtout pour ne pas se faire « enfler » par les vendeurs de pioches.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Mathieu Grymonprez | PERSONNE | dirige | Digital Tech and Data Adeo | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Mathieu Grymonprez | PERSONNE | travaille_chez | Adeo | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Adeo | ORGANISATION | affirme_que | "On ne va pas se refaire avoir (après le Retail Apocalypse)" | CITATION | 0.88 | STATIQUE | déclaré_article |
| Transformation IA | METHODOLOGIE | est_basé_sur | culture et structure simultanées | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Accountability | CONCEPT | s_applique_à | organisations et humains | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Mathieu Grymonprez | PERSONNE | recommande | parler ROI et expérience client au board, jamais technique | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Claude Code | TECHNOLOGIE | améliore | productivité de développement | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| IA agentique | TECHNOLOGIE | permet | avalanche de projets jadis non prioritaires (P10 → P2) | AFFIRMATION | 0.88 | DYNAMIQUE | inféré |
| FinOps | METHODOLOGIE | s_applique_à | coût des tokens | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| Gemma 4 | TECHNOLOGIE | permet | inférence locale sur laptop (MoE 26 Mds / 4 Mds actifs) | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Variation de modèles | CONCEPT | s_oppose_à | stabilité de la production | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Kubernetes standard | TECHNOLOGIE | réduit | lock-in fournisseur | CONCEPT | 0.91 | ATEMPOREL | déclaré_article |
| Lock-in de l'intelligence d'entreprise | CONCEPT | s_oppose_à | autonomie du groupe | CONCEPT | 0.87 | ATEMPOREL | déclaré_article |
| Orchestration d'agents | METHODOLOGIE | affirme_que | "rien en open source ne marche bien pour ça" | CITATION | 0.86 | DYNAMIQUE | déclaré_article |
| Mémoire d'entreprise | CONCEPT | est_basé_sur | "quand ce n'est pas logique, c'est historique" | CITATION | 0.85 | ATEMPOREL | déclaré_article |
| Leroy Merlin | ORGANISATION | mesure | chiffre d'affaires au mètre carré | MESURE | 0.9 | ATEMPOREL | déclaré_article |
| Decathlon | ORGANISATION | utilise | RFID end-to-end (puce en entrée de chaîne industrielle) | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Google | ORGANISATION | surpasse | OpenAI et Anthropic sur la conscience de la prod | AFFIRMATION | 0.8 | DYNAMIQUE | déclaré_article |
| Vertex AI | TECHNOLOGIE | permet | sélection du modèle selon le besoin | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Mathieu Grymonprez | PERSONNE | recommande | comprendre la techno pour ne pas se faire enfler par les vendeurs | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Mathieu Grymonprez | PERSONNE | rôle | Global CDO groupe Adeo (Digital Tech & Data), 26 ans dans la boîte | AJOUT |
| Adeo | ORGANISATION | secteur | Retail bricolage / habitat (Leroy Merlin, Obramat, Weldom), actionnariat familial non coté | AJOUT |
| Leroy Merlin | ORGANISATION | particularité | Piloté au CA au mètre carré ; ne vend pas de matelas | AJOUT |
| Decathlon | ORGANISATION | particularité | Producteur d'une grande partie de ses produits → RFID end-to-end | AJOUT |
| À la French | TECHNOLOGIE | catégorie | Podcast tech francophone (hôtes : Kempf, Morin, Medjaoui) | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI | AJOUT |
| Hermes | TECHNOLOGIE | catégorie | Agent IA personnel à mémoire (running gag « Hermès ») | AJOUT |
| Vertex AI | TECHNOLOGIE | catégorie | Plateforme IA GCP (sélection multi-modèles) | AJOUT |
| Gemma 4 | TECHNOLOGIE | architecture | MoE 26 Mds params / ~4 Mds actifs, inférence locale | AJOUT |
| Accountability | CONCEPT | définition | Responsabilité humaine inaliénable face aux décisions des agents | AJOUT |
| Make vs Buy | CONCEPT | valeur | « au moins 70 % » de make chez Adeo | AJOUT |
| FinOps | METHODOLOGIE | application | Maîtrise de l'efficience du coût des tokens (analogie cloud) | AJOUT |
| Lock-in de l'intelligence d'entreprise | CONCEPT | risque | Configuration agentique (« adeo.md ») captive d'un fournisseur | AJOUT |
| Orchestration d'agents | METHODOLOGIE | manque | Brique open source absente (registry, cycle de vie, permissions, skills) | AJOUT |
| Mémoire d'entreprise | CONCEPT | enjeu | Capturer le contexte des décisions (cold/hot memory, context engineering) | AJOUT |
| Thomas Bouret | PERSONNE | rôle | Patron de Mathieu Grymonprez (a suivi 6 h de cours IA) | AJOUT |
