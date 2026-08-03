---
themes: [economie-marche, politique-regulation, outils-plateformes]
source: "Mozilla"
---
# mozilla-state-of-open-source-ai-2026-07

## Veille

**Rapport récurrent de Mozilla**, *The state of open source AI*, **v1.0.1, juillet 2026**, introduit par une lettre de **Raffi Krikorian** (CTO). Sept sections, un site interactif et un rapport téléchargeable. **Thèse en titre de la section 1, et elle vaut pour tout le document** : *« The model layer has commoditized. Value accrues to the harness above it. »* **État capacitaire** : sur l'*Artificial Analysis Intelligence Index v4.1*, le meilleur modèle fermé marque **61** (Claude Opus 5), le meilleur ouvert **57** (**Kimi K3**), quatrième au général et devant trois des plus grands laboratoires fermés ; sur l'*Epoch Capabilities Index*, l'écart est de **6 points** (K3 à 156 contre GPT-5.6 Sol à 162), soit *« about one release cycle »*, **intervalles de confiance qui se chevauchent**. **Frontière en dents de scie** : l'ouvert mène en code frontend (K3 à 1 679 Elo sur LMArena Frontend Code Arena, six domaines sur sept), conteste le terrain agentique (88,3 contre 88,8 sur Terminal-Bench 2.1), et **cède sur le travail de connaissance professionnel** (Fable 5 devance K3 de 92 Elo sur GDPval-AA v2). **Bascule d'usage** : la part des tokens routés sur OpenRouter vers des modèles à poids ouverts est passée d'un niveau négligeable à un tiers fin 2025 puis à **une majorité mi-2026**, les **sept modèles les plus consommateurs étant tous à poids ouverts** — ⚠️ mais le rapport précise lui-même que *« by request count, closed US providers still lead »*, l'avance ouverte étant **un volume de tokens, concentré sur le codage et l'agentique**. **Le contraste central** : *« Open ships easy. Open deploys hard. »* — 79 % des développeurs qui ajoutent de l'IA utilisent des modèles ouverts contre 71 % pour les fermés, mais seules **53 % des équipes en modèle ouvert atteignent la production contre 63 %** ; et l'écart **se creuse avec la taille** (fermé 54 %→73 %, ouvert 53 %→57 %), ce qui *« rules out a resources explanation »*. La carte de maturité du stack (48 composants, 9 couches) montre deux colonnes systématiquement froides — **standardisation et *enterprise readiness*** —, l'« écart opérationnel ». **Section 5, la plus importante pour ce corpus** : *« The agentic harness is another user agent »*, et surtout *« The model is eating the harness »* — sur chaque modèle où les deux existent, le harnais du laboratoire l'emporte désormais, l'écart de **21,8 points s'étant comprimé à ~3** ; d'où la formule à retenir : *« A harness tuned tightly to one lab's weights… degrades on anyone else's model, so the tighter the tuning, the less swappable the weights underneath. **Lock-in arrives as a side effect of optimization.** »* ⚠️ **Réserve de lecture** : Mozilla est partie prenante, et le rapport est explicitement un **document de mobilisation** (*« We bet on open the first time. Open won. Together, we can do it again »*, appel final *« Build with us »*).

## Titre Article

The state of open source AI (v1.0.1, juillet 2026)

## Date

2026-07

## URL

https://stateofopensource.ai/

## Keywords

Mozilla, état de l'IA open source, poids ouverts, open weights, open source AI, définition OSI, code d'entraînement, documentation des données, commoditisation du modèle, harnais agentique, valeur en amont du modèle, Artificial Analysis Intelligence Index, Epoch Capabilities Index, Kimi K3, Claude Opus 5, GPT-5.6 Sol, Fable 5, Terminal-Bench, GDPval, LMArena, frontière en dents de scie, OpenRouter, part de tokens, volume vs requêtes, prix de l'inférence, 50x en 36 mois, LLMflation, adoption vs production, Mozilla SlashData, écart opérationnel, standardisation, enterprise readiness, carte du stack, souveraineté, 70 stratégies nationales, droits de sortie, exit rights, coût de sortie du cloud, rapatriement, Qwen, DeepSeek, Moonshot, Mistral, Zhipu, MiniMax, LangChain, MCP, A2A, Agentic AI Foundation, gouvernance des agents, surface d'écriture non résolue, lock-in par optimisation, contrôle à l'export, blackout de dix-neuf jours, irréversibilité d'une publication de poids, distillation, Kratsios, Greenblatt, Redwood Research, watchlist, Raffi Krikorian

## Authors

**Mozilla** — éditeur du rapport, avec une introduction signée **Raffi Krikorian**, *Chief Technology Officer*. Données issues de sources tierces créditées (Artificial Analysis, Epoch AI, OpenRouter, LMArena) et d'une **enquête propre menée avec SlashData** (*Mozilla / SlashData 2026 developer survey*, n = 1 410 sur la question des freins).

**Position à connaître avant de citer** : Mozilla n'est pas un observateur neutre du sujet qu'elle mesure. La lettre d'ouverture le revendique — *« Mozilla exists because one company tried to own the front door to the web, and an open community made sure it never could. We bet on open the first time. Open won. »* Le rapport est à la fois un travail de mesure sérieux et sourcé **et** une pièce de plaidoyer, refermée sur un appel à l'action et une inscription à MozFest.

## Ton

**Profil** : **rapport d'état sectoriel militant**, format web interactif (graphiques cliquables, cellules survolables) doublé d'un PDF. Registre analytique et chiffré dans le corps, **mobilisateur aux extrémités** — la lettre du CTO en ouverture, l'appel *« Build with us »* en clôture.

**Style** : chaque section porte un **titre-thèse en deux lignes** (*« Open ships easy. / Open deploys hard. »*, *« Open is a sovereignty choice. / Seventy governments are already treating it as one. »*), suivi d'une série de visualisations dont chacune est légendée par sa source **et par sa limite**. Cette discipline de légende est ce qui distingue le document d'un argumentaire : *« Scores use different scales and come mostly from vendor-run tests, so treat them as directional »*, *« with intermediate points interpolated »*, *« the confidence intervals overlap »*, *« Shares are of the top 20 only, not of all OpenRouter traffic »*.

**Deux gestes rhétoriques structurants** :

1. **L'ouverture par le cas marginal.** La lettre s'ouvre sur le te reo māori — une langue *« with no commercial market to speak of »* pour laquelle un diffuseur néo-zélandais construit des modèles de parole sous une licence qui garde les enregistrements chez les communautés — et sur un diagnostic de feuille de manioc rendu par un modèle tenant sur un téléphone, dans une zone blanche d'Afrique de l'Est. *« Neither project needed permission. And neither could have been rented from a frontier model. »* **On établit la valeur de l'ouvert par ce que le marché ne financera jamais, avant de parler de parts de marché.**
2. **La liste de réversibilité.** La section *watchlist* ne se contente pas de signaux : chacun est assorti d'un ***« Reverses if: »*** — la condition qui invaliderait la thèse. Rare et honnête dans un document de plaidoyer.

**Formules-marqueurs** : *« The model layer has commoditized »*, *« Open ships easy. Open deploys hard »*, *« Open weights are exit rights »*, *« You can switch off a model. You cannot switch off a copy already running on a machine you hold »*, *« the unsolved write surface »*, *« Lock-in arrives as a side effect of optimization »*, *« Commodity inputs surrender pricing power »*.

## Pense-betes

- **⭐⭐ La thèse à retenir, et elle est directement dans la ligne du corpus** : *« The model layer has commoditized. Value accrues to the harness above it. »* La justification tient en une phrase — *« Commodity inputs surrender pricing power »* — et en un constat : la majorité des charges de production tourne **bien en dessous du plafond de la frontière**.

- **La distinction terminologique, à tenir** : **open model** = poids téléchargeables, exécutables et modifiables sur du matériel qu'on contrôle. **Open weights** = paramètres sous licence permissive, **sans code d'entraînement ni documentation des données** — *« which describes most of what this report measures »*. **Open source AI** au sens **OSI** = exige en plus le code d'entraînement et assez d'information sur les données pour reconstruire le système. ⚠️ **Le rapport s'intitule « open source AI » mais mesure très majoritairement des poids ouverts.** Il le dit ; les reprises ne le diront pas.

- **Écart capacitaire, deux instruments concordants** : *Artificial Analysis Intelligence Index v4.1* (composite de neuf évaluations dont Terminal-Bench 2.1, Humanity's Last Exam, GPQA Diamond) → fermé 61 (Claude Opus 5) vs ouvert 57 (**Kimi K3**), quatrième sur 586 modèles, **3 des 11 modèles de tête à poids ouverts**. *Epoch Capabilities Index* → 156 (K3) vs 162 (GPT-5.6 Sol), **6 points ≈ un cycle de release**, avec **chevauchement des intervalles de confiance**. Et sur l'axe prix : K3 à **3,6 points du sommet pour environ le tiers du prix**.

- **⭐ La « frontière en dents de scie » — la nuance qui évite les généralités** : l'ouvert **mène** en code frontend (K3, 1 679 Elo, six domaines sur sept sur LMArena Frontend Code Arena) ; **conteste** l'agentique terminal (88,3 vs 88,8 sur Terminal-Bench 2.1 ; K3 gagne Program Bench, SpreadsheetBench 2 et BrowseComp, perd FrontierSWE 81,2 contre 86,6 pour Fable 5) ; **cède** sur le travail de connaissance professionnel (Fable 5 devance de **92 Elo** sur GDPval-AA v2, plus grand écart des benchmarks partagés, et Moonshot le concède). → *« Match the model to the job and you need the frontier for less than you think. »* ⚠️ Le rapport prévient : scores d'échelles différentes, **majoritairement issus de tests conduits par les vendeurs**, *« treat them as directional »*.

- **⚠️ Le chiffre le plus cité et le plus mal cité** : les poids ouverts sont passés d'une base négligeable à **un tiers** des tokens OpenRouter fin 2025 puis à **une majorité** mi-2026, et les **sept modèles de plus fort volume sont tous à poids ouverts** (72,4 % du volume du top 20 pour les rangs ouverts 1-10). **Mais le rapport précise** : *« By request count, closed US providers still lead. The open lead is a token-volume lead, concentrated in coding and agentic workloads »*, et les parts portent **sur le top 20 seulement**, pas sur tout le trafic. → **Une majorité de tokens n'est pas une majorité d'usages.**

- **⭐ Le vrai sujet du rapport : le déploiement, pas la capacité.** *« Open ships easy. Open deploys hard. »* Enquête Mozilla/SlashData 2026 : **79 %** des développeurs ajoutant de l'IA utilisent des modèles ouverts contre **71 %** de fermés, et **50 % utilisent les deux** (29 % ouvert seul, 21 % fermé seul) — les deux catégories sont **complémentaires**, pas rivales. Mais **53 % des équipes en ouvert atteignent la production contre 63 % en fermé**, et surtout l'écart **se creuse avec la taille de l'entreprise** : fermé **54 % → 73 %**, ouvert **53 % → 57 %**. → *« Scale rules out a resources explanation. Enterprises can buy their way through closed deployment. Open deployment waits on tooling that remains unfinished. »* Les freins nommés sont **opérationnels partout** : coût d'infrastructure, sécurité/conformité, maintenance, complexité de déploiement.

- **La carte du stack** (48 composants, 9 couches, 10 critères) confirme le même diagnostic par une autre voie : **deux colonnes systématiquement froides sur toutes les couches — standardisation et *enterprise readiness*** —, ce que le rapport appelle *« that repeating cold edge »*, l'écart opérationnel.

- **⭐⭐ Section 5, la plus importante ici — « The agentic harness is another user agent »** : l'analogie est celle du navigateur, *« code on the user's side negotiating with servers on their behalf »*, rejouée une couche plus haut. Le harnais = boucle d'orchestration + outils + mémoire + bacs à sable + modèle de permissions, et *« it is where production difficulty concentrates, and where the open-vs-closed, owner-vs-renter contest restarts »*. Cinq strates cartographiées : **Govern** (politique à état, registre et lignage, budget et révocation), **Surface** (AG-UI/A2UI, x402/AP2/UCP), **Action** (bacs à sable E2B/Daytona/Modal, **permission et identité — *« the unsolved write surface »***, éval et observabilité), **Reach** (MCP, A2A, mémoire), **Control** (LangGraph, CrewAI, AutoGen, LlamaIndex).
  ⭐ **« The unsolved write surface »** est la meilleure formule du rapport, et elle recoupe exactement le diagnostic de [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] : lire est résolu, écrire ne l'est pas.

- **⭐⭐ Le mécanisme de verrouillage, formulé mieux qu'ailleurs** : *« The model is eating the harness. »* Sur chaque modèle où le harnais du laboratoire et un harnais indépendant coexistent, **le premier gagne désormais**, et l'écart de **21,8 points s'est comprimé à ~3** au sommet. D'où : *« A harness tuned tightly to one lab's weights becomes a fitted component of that lab's product. It degrades on anyone else's model, so the tighter the tuning, the less swappable the weights underneath. **Lock-in arrives as a side effect of optimization.** »* → **Le verrouillage n'a pas besoin d'être une stratégie : il suffit d'optimiser.** À rapprocher de l'argument d'optionalité de [[dethlefsen-zed-anthropic-subscription-changes-2026-05-14]] et du contrat de portabilité de [[janakiram-agent-platform-portability-contract-2026-07-20]].

- **Traction de la couche harnais** : LangChain 126 000+ étoiles et **60 % de part développeur** ; **MCP** à **97 M de téléchargements SDK mensuels** et **10 000+ serveurs actifs** en un an, **+4 750 % en 16 mois**, donné à l'**Agentic AI Foundation** de la Linux Foundation en décembre 2025 (cf. [[openai-agentic-ai-foundation-linux-2025-12-09]]). ⚠️ Et l'écart de gouvernance : **~21 % seulement** des entreprises déclarent une gouvernance d'agents mature.

- **Économie** : l'inférence a chuté **50× en 36 mois** au niveau GPT-4 (contre 2,6× pour la bande passante à l'ère dotcom et 3,4× pour le calcul PC sur la même durée), le prix de frontière ayant chuté **112×** depuis les 45 $ de GPT-4. Sur OpenRouter (mai-sept. 2025), le fermé tenait **~80 % de l'usage et ~96 % du revenu** — à parité ~90 %, le fermé coûte **~6× plus par appel**, d'où une estimation de **~24,8 Md$ d'économies annuelles non réalisées** (étude Nagle-Yue pour la Linux Foundation). *« Where developers route by cost, they route to open weights. »*

- **⭐ Souveraineté — l'argument le mieux construit du rapport** : plus de **70 stratégies nationales** actives, et *« the strategic case for open is the ability to leave »*, adossé au précédent cloud (**90-120 k$ pour sortir un pétaoctet de S3**, 37signals passé de 3,2 M$ à moins d'1 M$, GEICO à 2,5× le plan, **80 % d'entreprises en rapatriement**). *« Closed model APIs reproduce the same trap… **Open weights are exit rights.** »*

- **⭐⭐ Le blackout de dix-neuf jours — le cas qui rend l'argument concret** : 9 juin, Anthropic livre Fable 5 et Mythos 5 → **12 juin, le Commerce applique des contrôles à l'export avec effet immédiat**, interdisant l'accès à *tout ressortissant étranger, aux États-Unis ou hors des États-Unis, y compris les propres employés d'Anthropic* ; la nationalité n'étant pas vérifiable en temps réel, **les deux modèles s'éteignent pour tout le monde** → 26 juin, restauration partielle de Mythos pour ~100 organisations américaines d'infrastructure critique → 30 juin, levée → 1er juillet, Fable 5 restauré, **dix-neuf jours après**. Puis **16 juillet**, Moonshot ouvre l'API de K3. **La leçon, en une phrase** : *« Access can be revoked and restored. A weight release cannot be withdrawn once the files are distributed… You can switch off a model. You cannot switch off a copy already running on a machine you hold. »* Cf. [[anthropic-claude-fable-5-mythos-5-2026-06-09]], [[arstechnica-ai-kill-switch-act-2026-07-23]] et [[sfeir-rapport-kill-switch-souverainete-2026-07-24]].

- **Chine, et la résolution « architecturale »** : Qwen a dépassé en février 2026 les huit organisations suivantes réunies en téléchargements Hugging Face ; les modèles chinois à poids ouverts sont passés de **moins de 2 %** des tokens OpenRouter fin 2024 à **plus de 45 %** du trafic hebdomadaire en avril 2026, **~61 %** parmi les dix plus utilisés. DeepSeek revendique 26 000+ comptes entreprise et figurait dans le stack de **58 % des nouvelles startups IA en 2025**, alors même qu'**au moins huit juridictions** ont restreint le service hébergé. → *« Enterprises ban the hosted app and adopt the weights anyway »* : **on interdit l'application, on adopte les poids.**

- **⚠️ L'affaire de distillation K3 / Fable, à manier avec les catégories du rapport lui-même** — qui distingue proprement trois niveaux : **confirmé** (divulgation Anthropic de février 2026 : ~24 000 comptes frauduleux, **plus de 16 M d'échanges**, dont **3,4 M attribués à Moonshot**, sur des modèles Claude antérieurs ; déclarations Kratsios le 22 juillet et Bessent le 21) ; **signal** (Greenblatt, Redwood Research : K3 s'auto-identifie comme Claude de façon statistiquement difficile à expliquer par le bruit — **limite** : il nomme un modèle *antérieur* à l'affaire, et l'auto-identification est un artefact connu d'entraînement sur du texte web) ; **preuve : absente** — *« No logs and no forensic package. Moonshot denies. »* Le rapport note que la publication des poids **rend désormais possible une forensique comportementale**. → **Ne jamais présenter l'allégation comme établie.**

- **La *watchlist*, et sa qualité méthodologique** : quatre familles de signaux (capacité/adoption, harnais, structure de marché, confiance/sûreté), chacune assortie de sa **condition d'invalidation** (*« Reverses if: the lab-harness lead widens, or a closed platform sets the permission standard first »*). **Poser à l'avance ce qui prouverait qu'on a tort** est ce qui sauve un document de plaidoyer.

- **⚠️ Réserve globale à porter en citation** : Mozilla mesure un sujet dont elle est militante. La rigueur des légendes et la présence des conditions de réversibilité rendent les données utilisables, mais **le cadrage** — commoditisation acquise, ouverture inéluctable, *« open won »* — est une thèse, pas un constat. Le rapport se termine sur *« Build with us »* et une inscription à MozFest.

- **Méta / à relier** : contexte capacitaire de K3 dans [[sfeir-kimi-k3-moonshot-frontier-open-weights-2026-07-16]] et [[deanwball-open-weights-decelerationnistes-kimi-2026-07-17]] ; blackout et export control dans [[anthropic-claude-fable-5-mythos-5-2026-06-09]] ; pression tarifaire concurrente dans [[sfeir-gpt56-sol-terra-luna-coding-agentique-pricing-2026-07-13]] ; couche harnais dans [[osmani-agent-harness-engineering-2026-04-19]] et [[skill-gibbs-hyperresearch-2026-08-03]] ; « unsolved write surface » à lire avec [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] ; souveraineté d'exécution dans [[sfeir-zml-llmd-docker-llm-inference-souveraine-2026-07-09]] et [[sfeir-airbus-scaleway-cloud-confiance-souverainete-2026-07-16]] ; économie du token dans [[tokenomics-foundation-linux-finops-token-economics-about-2026-06-03]].

## RésuméDe400mots

Rapport récurrent de **Mozilla**, *The state of open source AI* (v1.0.1, juillet 2026), introduit par son CTO **Raffi Krikorian**.

**La thèse** ouvre la première section : *« The model layer has commoditized. Value accrues to the harness above it. »* Les intrants devenus commodités perdent leur pouvoir de fixation des prix, et la majorité des charges de production tourne bien en dessous du plafond de la frontière.

**L'état capacitaire.** Sur l'Artificial Analysis Intelligence Index, le meilleur modèle fermé marque 61 (Claude Opus 5), le meilleur ouvert 57 (**Kimi K3**), quatrième au général ; sur l'Epoch Capabilities Index l'écart vaut **six points, « environ un cycle de release »**, intervalles de confiance chevauchants. La frontière est **en dents de scie** : l'ouvert mène en code frontend, conteste l'agentique terminal, et cède nettement sur le travail de connaissance professionnel.

**La bascule d'usage.** La part des tokens routés sur OpenRouter vers des poids ouverts est passée d'un niveau négligeable à une majorité mi-2026, les sept modèles les plus consommateurs étant tous ouverts — mais le rapport précise que **par nombre de requêtes les fournisseurs fermés mènent encore**, l'avance ouverte étant un volume de tokens concentré sur le codage et l'agentique.

**Le vrai sujet est ailleurs** : *« Open ships easy. Open deploys hard. »* 79 % des développeurs utilisent des modèles ouverts contre 71 % de fermés, la moitié utilisant les deux ; mais seules **53 % des équipes en ouvert atteignent la production contre 63 %**, et l'écart **se creuse avec la taille de l'entreprise**, ce qui exclut une explication par les moyens. La carte du stack le confirme : deux colonnes froides sur toutes les couches, **standardisation et *enterprise readiness***.

**Le harnais est la nouvelle frontière.** *« The agentic harness is another user agent »* — le rôle du navigateur rejoué une couche plus haut. Et le mécanisme de verrouillage y est formulé avec précision : le harnais d'un laboratoire, ajusté à ses propres poids, se dégrade sur ceux des autres, donc *« the tighter the tuning, the less swappable the weights underneath. **Lock-in arrives as a side effect of optimization.** »*

**La souveraineté** est traitée comme un droit de sortie, illustré par le **blackout de dix-neuf jours** de Fable 5 sur contrôle à l'export : *« You can switch off a model. You cannot switch off a copy already running on a machine you hold. »*

⚠️ Mozilla milite pour ce qu'elle mesure. Les légendes sont scrupuleuses et la *watchlist* énonce ses propres conditions d'invalidation ; le cadrage reste une thèse.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Mozilla | ORGANISATION | publie | The state of open source AI | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| Raffi Krikorian | PERSONNE | travaille_chez | Mozilla | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Mozilla | ORGANISATION | affirme_que | la couche modèle s'est commoditisée et la valeur remonte vers le harnais agentique | CITATION | 0.96 | DYNAMIQUE | déclaré_article |
| harnais agentique | CONCEPT | est_instance_de | un user agent, au sens où le navigateur l'était pour le web ouvert | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| harnais ajusté aux poids d'un laboratoire | CONCEPT | réduit | l'interchangeabilité des poids sous-jacents — le verrouillage arrive comme effet de bord de l'optimisation | CITATION | 0.95 | DYNAMIQUE | déclaré_article |
| Kimi K3 | TECHNOLOGIE | mesure | 57 sur l'Artificial Analysis Intelligence Index v4.1, contre 61 pour le meilleur modèle fermé | MESURE | 0.93 | STATIQUE | déclaré_article |
| Kimi K3 | TECHNOLOGIE | concurrence | Claude Opus 5 | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| open-weights | CONCEPT | mesure | une majorité des tokens routés sur OpenRouter mi-2026, avec les sept plus forts volumes | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| Mozilla | ORGANISATION | affirme_que | l'avance des poids ouverts est un volume de tokens et non un nombre de requêtes, concentré sur le codage et l'agentique | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| modèles ouverts | TECHNOLOGIE | s_oppose_à | leur propre mise en production, seules 53 % des équipes y parvenant contre 63 % en fermé | MESURE | 0.92 | DYNAMIQUE | déclaré_article |
| écart opérationnel | CONCEPT | observé_dans | la standardisation et l'enterprise readiness, colonnes systématiquement faibles de toutes les couches du stack ouvert | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| poids ouverts | TECHNOLOGIE | permet | un droit de sortie, là où une API propriétaire reproduit le piège du verrouillage cloud | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| contrôle à l'export | CONCEPT | s_oppose_à | la disponibilité d'un modèle fermé, éteint dix-neuf jours pour tous ses utilisateurs | AFFIRMATION | 0.94 | STATIQUE | déclaré_article |
| publication de poids | CONCEPT | s_oppose_à | la révocabilité d'un accès, une copie distribuée ne pouvant être retirée | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| permission et identité des agents | CONCEPT | est_instance_de | la surface d'écriture non résolue du stack agentique | CITATION | 0.93 | DYNAMIQUE | déclaré_article |
| Model Context Protocol | TECHNOLOGIE | mesure | 97 M de téléchargements SDK mensuels et plus de 10 000 serveurs actifs en un an | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| gouvernance des agents | CONCEPT | s_oppose_à | le rythme d'adoption, seules ~21 % des entreprises déclarant une gouvernance mature | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| prix de l'inférence | CONCEPT | réduit | d'un facteur 50 en 36 mois à performance de classe GPT-4 | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| modèles fermés | TECHNOLOGIE | mesure | environ 80 % de l'usage et 96 % du revenu sur OpenRouter, à un coût par appel environ six fois supérieur à parité | MESURE | 0.88 | STATIQUE | déclaré_article |
| entreprises | ORGANISATION | utilise | les poids ouverts chinois en auto-hébergement, tout en interdisant le service hébergé correspondant | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Michael Kratsios | PERSONNE | affirme_que | Kimi K3 aurait été entraîné par extraction covert à grande échelle depuis Fable 5 | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Moonshot AI | ORGANISATION | s_oppose_à | l'allégation d'extraction covert, qu'elle dément | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| Mozilla | ORGANISATION | affirme_que | aucun journal ni dossier forensique n'étaye l'allégation de distillation, que Moonshot dément | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Mozilla | ORGANISATION | recommande | de suivre quatre familles de signaux assorties chacune de sa condition d'invalidation | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| open-weights | CONCEPT | s_oppose_à | open source AI au sens OSI, qui exige en plus le code d'entraînement et la documentation des données | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| The state of open source AI | DOCUMENT | référence | Rapport récurrent de Mozilla, v1.0.1, juillet 2026 ; sept sections, données Artificial Analysis, Epoch AI, OpenRouter, LMArena et enquête Mozilla/SlashData 2026 | AJOUT |
| Mozilla | ORGANISATION | positionnement | Éditrice d'un état des lieux annuel de l'IA ouverte, à la fois travail de mesure sourcé et pièce de plaidoyer — partie prenante du sujet mesuré | MISE_A_JOUR |
| Raffi Krikorian | PERSONNE | rôle | Chief Technology Officer de Mozilla, auteur de la lettre d'ouverture du rapport | AJOUT |
| open-weights | CONCEPT | définition | Paramètres publiés sous licence permissive, sans code d'entraînement ni documentation des données — distincts de l'open source AI au sens OSI | AJOUT |
| écart opérationnel | CONCEPT | définition | Retard structurel du stack ouvert sur la standardisation et la préparation entreprise, qui explique que l'adoption dépasse l'ouvert mais que la mise en production reste derrière | AJOUT |
| verrouillage par optimisation | CONCEPT | définition | Mécanisme par lequel un harnais ajusté finement aux poids d'un laboratoire se dégrade sur les autres modèles, rendant les poids d'autant moins interchangeables que l'ajustement est bon | AJOUT |
| surface d'écriture non résolue | CONCEPT | définition | Couche permission et identité du stack agentique, désignée comme le point non résolu : lire est outillé, écrire ne l'est pas | AJOUT |
| droit de sortie | CONCEPT | définition | Capacité de quitter un fournisseur sans réécrire son système ; argument central en faveur des poids ouverts, adossé au coût constaté des sorties de cloud | AJOUT |
