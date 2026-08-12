---
themes: [outils-plateformes, qualite-securite, transformation-adoption]
source: "Deep Research"
---
# chatgpt-claude-desktop-vs-web-deep-research-2026-08-12

## Veille

Rapport de recherche interne du **12 août 2026** (format **What ? — So What ? — Now What ?**, enquête menée les 11-12 août) sur une question apparemment banale : **les applications desktop de ChatGPT et de Claude sont-elles meilleures que leurs versions web ?** ⭐⭐ **La réponse tient en deux temps, et le second est le vrai sujet du rapport** : *oui, un consensus qualitatif solide et sourcé existe* — **et la quasi-totalité des chiffres qui circulent pour l'étayer ne résiste pas à la vérification**. **Le point de départ, incontestable** : desktop et web appellent **exactement les mêmes modèles cloud**, l'application n'étant qu'une interface du service. **Le gain se situe intégralement dans l'enveloppe applicative** — latence d'accès, stabilité en session longue, empreinte mémoire, intégrations système, fluidité du workflow. **Ce qui distingue réellement le desktop, confirmé** : côté OpenAI, raccourci global (Option/Alt + Espace), *companion window* toujours au premier plan, captures d'écran natives, et depuis juillet 2026 l'agentique **Codex/Work** intégrée dans l'app ; côté Anthropic, **Quick Entry** (macOS), **Desktop Extensions** (installer un serveur **MCP** local devient *« as simple as clicking a button »*), accès aux fichiers locaux, **Cowork** et **Computer Use** (permissions Accessibilité + enregistrement d'écran). Le web garde deux atouts confirmés : **multi-onglets/multi-fils** et **universalité sans client à installer**. ⭐⭐ **Le cœur du rapport est son audit critique (§1.5)** : sept affirmations chiffrées largement reprises sont classées **non confirmées** — le *cold start* « 2-3 s vs 8-12 s » (seule trace : un « loads in about 3 seconds » anecdotique sur Substack), la RAM « 200-700 Mo vs 1,2-2 Go » **attribuée à un « Alibaba Product Insights » dont les pages renvoient 404**, un *glitch rate* et une rétention de session introuvables, un « Claude +10-20 % end-to-end » attribué à **Skywork — qui avait en réalité benchmarké son propre agent Windows, pas Claude contre le web**, une source « Cosmo Edge » introuvable, des citations Zenken AI non confirmées, et **deux posts X non authentifiés** (aucune URL). **Le contre-signal est documenté avec la même rigueur** : Yuri Dvoinos décrit une app Claude Desktop qui *« makes me want to throw my laptop out the window »* — **68 % de CPU**, lag de saisie sur MacBook Pro — et le rapport rappelle que les deux apps sont des constructions **Electron + couches natives**, pas des applications natives. D'où sa formule : ***l'avantage desktop est une promesse d'implémentation, pas une loi de la nature.*** **Le « So What »** déplace la question : puisque le modèle est devenu le point commun, **l'interface devient le champ de bataille** — la fusion **Codex + ChatGPT du 9 juillet 2026** et le tandem **Cowork/Computer Use** racontent la même histoire, *« l'app desktop n'est plus un client de chat, c'est un runtime d'agents avec accès à la machine »*. Trois conséquences : le gain est **un gain de friction, pas de puissance** (réel seulement en usage intensif) ; pour les DSI, le desktop **déplace la frontière de confiance** — Computer Use exige des permissions système sensibles et la fusion Codex place exécution de code, navigateur et connecteurs dans *« one expanded trust boundary »*, quand le navigateur reste gouvernable par SSO/DLP/CASB ; et **pour qui publie, la fragilité des chiffres est l'information**. **Le « Now What »** livre des critères de bascule individuels, une checklist DSI (inventorier les permissions, désactiver Computer Use et Cowork par défaut, cadrer les extensions MCP autorisées, organiser la distribution et les mises à jour — **sur Linux, hors dépôt apt, Claude Desktop ne se met pas à jour seul**), et une consigne éditoriale : **ne citer que les verbatims et dates confirmés**, bannir les chiffres du tableau d'audit. ⭐ **Ironie relevée par le rapport** : le critique le plus virulent du desktop utilise Claude… **dans le navigateur d'OpenAI**, signe que les navigateurs IA pourraient devenir la **troisième voie** du duel.

## Titre Article

ChatGPT Desktop & Claude Desktop vs versions web — Rapport « What ? — So What ? — Now What ? »

## Date

2026-08-12

## URL

*Aucune URL publique — rapport de recherche interne non publié au moment de la mise en fiche. Source archivée dans `raw-data/chatgpt-claude-desktop-vs-web-deep-research-2026-08-12.md` (le répertoire `docs/deep research/` est gitignoré).*

## Keywords

ChatGPT Desktop, Claude Desktop, version web, application desktop, app native, Electron, enveloppe applicative, latence d'accès, cold start, empreinte mémoire, RAM, session longue, glitch rate, rétention de session, benchmark indépendant, chiffre invérifiable, chiffre orphelin, audit de sources, vérification, sourçage, verbatim confirmé, honnêteté éditoriale, What So What Now What, raccourci global, Option Espace, Alt Espace, companion window, capture d'écran native, Quick Entry, Desktop Extensions, dxt, mcpb, serveur MCP local, Model Context Protocol, fichiers locaux, Cowork, Computer Use, permissions Accessibilité, enregistrement d'écran, runtime d'agents, agentique, Codex, fusion Codex ChatGPT, ChatGPT Classic, onglets Chat Work Code, GPT-5.6, multi-onglets, universalité du web, friction, gain de productivité, usage intensif, power user, DSI, gouvernance, frontière de confiance, trust boundary, SSO, DLP, CASB, MDM, mise à jour, beta Linux, dépôt apt, navigateur IA, troisième voie, Anthropic, OpenAI, Yuri Dvoinos, Skywork, Alibaba Product Insights, Cosmo Edge, Zenken AI, How-To Geek, TechSpot, PartnerInAI, Tech Times, mini-benchmark reproductible

## Authors

**Deep Research Veille Interne** — rapport non signé, produit par une enquête sourcée menée les **11-12 août 2026** et rendu le 12.

**Position d'énonciation** : le document est écrit **pour décider**, pas pour informer. Il s'adresse simultanément à trois lecteurs — l'utilisateur qui choisit son client, la DSI qui autorise ou non un déploiement, et l'auteur qui va publier sur le sujet — et donne à chacun une section d'actions. Sa singularité tient à ce qu'il **inclut l'audit de sa propre matière** : une section entière recense ce que l'enquête **n'a pas pu confirmer**, avec le motif de l'échec pour chaque affirmation.

⚠️ **Limite à porter avec le document** : la fiche enregistre **le statut de vérification tel que le rapport le déclare**, non une re-vérification indépendante. Deux nuances méritent d'être signalées à l'usage. (1) Les entrées de la chronologie antérieures à 2026 (app ChatGPT macOS de mai-juin 2024, *companion window* d'août 2024, Computer Use et Claude Desktop d'octobre 2024, renommage `.dxt` → `.mcpb`) correspondent à des annonces publiques largement documentées ; les entrées 2026 sont reprises telles que rapportées. (2) Le critère de « confirmation » appliqué est **l'existence et la lecture de la source**, pas son autorité : plusieurs sources classées confirmées sont des blogs de faible notoriété (PartnerInAI, MachineFriendly, explainx.ai, Titikey). **Confirmé y signifie « la page existe et dit cela », pas « c'est établi ».**

## Ton

**Profil** : rapport de décision en trois temps (**What / So What / Now What**), registre **analyste**, discipline de sourçage inhabituelle. Ni essai ni comparatif produit : un document qui sépare explicitement ce qui est établi, ce qui est interprété et ce qui est à faire.

**Style** : structure gelée par le format, et exploitée à fond — le *What* est presque entièrement tabulaire (chronologie, verbatims, **audit des non-confirmés**), le *So What* est en quatre paragraphes à thèse, le *Now What* en quatre destinataires. Trois traits :

1. **⭐ L'audit du négatif comme section à part entière.** Consacrer un tableau à **ce que l'enquête n'a pas pu confirmer**, avec le motif de chaque échec (404, mauvaise attribution, source introuvable, tweet non authentifié), inverse la norme du rapport de veille, qui expose ce qu'il a trouvé et tait ce qu'il a manqué.
2. **La séparation stricte des statuts.** Chaque affirmation porte son étiquette : confirmée avec URL, non confirmée avec motif, interprétée dans le *So What*. La note finale verrouille : *« Toute affirmation chiffrée non listée comme "confirmée" doit être considérée comme non vérifiée. »*
3. **La transformation d'un manque en angle.** Le rapport ne se contente pas de constater que les chiffres manquent : il en fait une **recommandation éditoriale** (*« documenter leur invérifiabilité, c'est se différencier »*) puis une **proposition de travail** chiffrée en temps (un mini-benchmark maison de quelques heures).

**Formules-marqueurs** : *« la qualité du modèle est strictement identique des deux côtés »*, *« le gain se situe intégralement dans l'enveloppe applicative »*, *« l'app desktop n'est plus un client de chat, c'est un runtime d'agents avec accès à la machine »*, *« le gain de productivité est un gain de friction, pas de puissance »*, *« l'avantage desktop est une promesse d'implémentation, pas une loi de la nature »*, *« la fragilité des chiffres est l'information »*, *« mécanismes réels, métriques fragiles »*.

**Position épistémique** : **rigoureuse et bornée**. Le document ne prétend pas trancher ce qu'il n'a pas mesuré, refuse d'utiliser des chiffres qui l'arrangeraient, et retient le contre-exemple le plus défavorable à sa propre conclusion comme *« gage d'honnêteté éditoriale »*.

## Pense-betes

- **⭐⭐ Le fait de cadrage, à poser avant toute discussion** : **desktop et web appellent exactement le même modèle**. Aucune différence de qualité de réponse n'est en jeu. **Tout le débat porte sur l'enveloppe applicative** — accès, session, mémoire, intégrations, workflow. Toute affirmation du type « Claude est meilleur en desktop » qui ne précise pas *sur quelle dimension d'enveloppe* est une confusion de niveau.

- **⭐⭐ Le vrai livrable du rapport : le tableau de ce qui ne tient pas.** Sur une question grand public et trivialement mesurable, **aucun benchmark indépendant crédible n'existe**, et sept affirmations chiffrées largement reprises tombent :
  | Chiffre en circulation | Pourquoi il tombe |
  |---|---|
  | Cold start « 2-3 s vs 8-12 s » | aucun benchmark ; une seule trace anecdotique (« loads in about 3 seconds ») |
  | RAM « 200-700 Mo vs 1,2-2 Go » | attribué à « Alibaba Product Insights » — **pages en 404** |
  | Glitch rate 1,8 vs 4,2 · rétention 100 % vs 62 % | introuvables dans les sources accessibles |
  | Claude « +10-20 % end-to-end » (Skywork) | **mauvaise attribution** : Skywork benchmarkait son propre agent Windows |
  | Cosmo Edge (02/2026) · Zenken AI | sources introuvables / citations non confirmées |
  | Deux posts X très cités | **aucune URL x.com**, non authentifiés |
  → **Deux mécanismes de blanchiment de chiffre à savoir reconnaître** : (1) **l'attribution institutionnelle plausible** — un nom de marque + un mot comme « Product Insights » suffit à faire passer un chiffre, et personne ne clique ; (2) **le glissement de comparaison** — un benchmark réel existe, mais il ne mesurait pas ce qu'on lui fait dire. Ces deux motifs se retrouvent bien au-delà de ce sujet.

- **⭐ L'observation qui vaut au-delà du dossier** : ce qui manque ici est **mesurable en quelques heures** (chronométrer dix démarrages à froid, relever la RAM au moniteur d'activité, documenter machine et versions). Le rapport en fait sa recommandation différenciante. **Le trou n'est pas technique, il est d'effort** — sur un sujet où des dizaines d'articles citent des chiffres, personne n'a passé trois heures à les produire. C'est le genre de constat qui indique une opportunité de contenu, pas seulement une lacune.

- **⭐ La bascule de nature de l'objet — la meilleure idée du *So What*** : *« l'app desktop n'est plus un client de chat, c'est un runtime d'agents avec accès à la machine »*. La fusion **Codex + ChatGPT** (9 juillet 2026, onglets Chat / Work / Codex, l'ancienne app devenant « ChatGPT Classic ») et le tandem **Cowork / Computer Use** vont dans le même sens. **Conséquence de lecture** : comparer desktop et web sur la vitesse de lancement, c'est comparer les mauvaises grandeurs. La question réelle est *« qu'est-ce que ce client a le droit de faire sur ma machine ? »*.

- **⚠️⚠️ La conséquence DSI, à instruire avant tout déploiement** : le desktop **déplace la frontière de confiance**. Computer Use exige **Accessibilité + enregistrement d'écran** ; la fusion Codex place exécution de code, navigateur et connecteurs dans *« one expanded trust boundary »*. Le navigateur, lui, reste gouvernable par **SSO / DLP / CASB**. **Checklist reprise du rapport** : inventorier les permissions demandées ; **désactiver Computer Use et Cowork par défaut**, ouverture sur besoin justifié ; **cadrer la liste des extensions MCP autorisées** ; organiser distribution et mises à jour par MDM. ⚠️ **Point d'exploitation à ne pas rater : sur Linux (beta, 30 juin 2026), hors dépôt apt, Claude Desktop ne se met pas à jour tout seul.** À croiser avec [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] et [[sfeir-anthropic-sdlc-ai-native-securise-2026-07-26]].

- **La règle d'arbitrage individuelle, en une ligne** : **desktop si** vous invoquez l'IA plusieurs fois par heure **et** que vos workflows passent par des fichiers locaux, des captures ou des agents ; **web si** l'usage est occasionnel ou si vous vivez en multi-onglets. Le rapport reformule bien la question : *« pas lequel est le meilleur, mais à quelle fréquence et avec quelles intégrations travaillez-vous ? »*

- **Le gain est de friction, pas de puissance.** Quelques secondes par invocation × des dizaines d'invocations quotidiennes = gain réel, **mais borné aux usages intensifs**. Formulation utile pour désamorcer les attentes : personne ne devient plus intelligent en installant l'app.

- **⭐ Le contre-signal, à citer avec le reste** : **Yuri Dvoinos** — *« makes me want to throw my laptop out the window »*, **68 % de CPU** et lag de saisie sur MacBook Pro. Plus le rappel structurel : les deux apps sont **Electron + couches natives**. D'où la phrase à garder : ***« l'avantage desktop est une promesse d'implémentation, pas une loi de la nature »*** — il dépend de la version livrée, pas de la catégorie de produit.

- **⭐ La troisième voie, signalée en passant** : le critique le plus virulent du desktop **utilise Claude dans le navigateur d'OpenAI**. Si le débat se rejoue entre *client natif* et *navigateur IA*, la dichotomie desktop/web devient caduque. À suivre avec [[rafal-chatgpt-atlas-web-conversationnel-2025-10-22]] et [[mody-browser-company-arc-dia-ai-native-2025-11-23]].

- **La chronologie, à réutiliser telle quelle** (sources primaires selon le rapport) : **13 mai 2024** annonce app ChatGPT macOS · **25 juin 2024** disponibilité générale · **8 août 2024** companion window · **22 oct. 2024** Computer Use en public beta · **31 oct. 2024** Claude Desktop Mac et Windows · **juin → 11 sept. 2025** Desktop Extensions, `.dxt` renommé `.mcpb` · **12 janv. 2026** Cowork en research preview (macOS, plan Max) · **2 févr. 2026** app Codex · **30 juin 2026** Claude Desktop beta Linux · **7 juil. 2026** Cowork étendu au web, iOS, Android · **9 juil. 2026** fusion Codex + ChatGPT.

- **⚠️ Hygiène de citation propre à ce document** : la fiche enregistre **le statut de vérification déclaré par le rapport**, pas une contre-enquête. Et « confirmé » y veut dire **« la page existe et dit cela »**, pas « c'est établi » — plusieurs sources validées sont des blogs de faible notoriété. **Pour une publication, appliquer la règle du rapport** (ne citer que verbatims et dates confirmés, bannir le tableau §1.5) **et y ajouter un filtre d'autorité de source**.

- **Méta / à relier** : sur Cowork et l'adoption, [[cherny-steps-ai-adoption-2026-07-16]] ; sur Computer Use, [[cherny-sequoia-coding-is-solved-loops-printing-press-2026-05]] ; sur l'écart entre chiffres annoncés et gains mesurés dans l'IA de développement, [[dora-google-cloud-roi-ai-assisted-software-development-j-curve-2026-04-21]] et [[pragmatic-engineer-measure-ai-impact-dev-2025-09-16]] ; sur la couche MCP empaquetée pour installation en un clic, [[google-agent-plugins-packaging-skills-mcp-2026-08-06]] et [[agent-skills-anthropic-2025-10-16]].

## RésuméDe400mots

Rapport de recherche interne du **12 août 2026**, au format **What ? — So What ? — Now What ?**, sur une question simple : les applications desktop de ChatGPT et de Claude sont-elles meilleures que le web ?

**What.** Oui, un consensus qualitatif existe chez les power users et les reviewers — **mais il ne porte jamais sur le modèle** : desktop et web appellent exactement la même intelligence cloud. Le gain est **entièrement dans l'enveloppe applicative** : latence d'accès, stabilité en session longue, empreinte mémoire, intégrations système. Ce qui distingue réellement le desktop, confirmé : côté OpenAI, raccourci global, *companion window* au premier plan, captures natives, et depuis juillet 2026 l'agentique **Codex/Work** dans l'app ; côté Anthropic, **Quick Entry**, **Desktop Extensions** (un serveur MCP local s'installe *« en cliquant un bouton »*), fichiers locaux, **Cowork** et **Computer Use**. Le web garde le multi-onglets et l'universalité sans installation.

**L'audit critique est le cœur du document.** Sept affirmations chiffrées largement reprises sont classées **non confirmées** : le cold start « 2-3 s vs 8-12 s » (aucun benchmark), la RAM « 200-700 Mo vs 1,2-2 Go » attribuée à un « Alibaba Product Insights » **dont les pages renvoient 404**, un glitch rate et une rétention de session introuvables, un « Claude +10-20 % » attribué à **Skywork qui benchmarkait en réalité son propre agent Windows**, deux sources introuvables et **deux posts X non authentifiés**. Le contre-signal est retenu avec la même rigueur : Yuri Dvoinos, **68 % de CPU** et *« makes me want to throw my laptop out the window »*, plus le rappel que les deux apps sont des **Electron + couches natives**. D'où : *« l'avantage desktop est une promesse d'implémentation, pas une loi de la nature. »*

**So What.** Le modèle étant devenu le point commun, **l'interface devient le champ de bataille** : *« l'app desktop n'est plus un client de chat, c'est un runtime d'agents avec accès à la machine »*. Le gain est **un gain de friction, pas de puissance**, réel seulement en usage intensif. Pour les DSI, le desktop **déplace la frontière de confiance** — permissions Accessibilité et enregistrement d'écran, *« one expanded trust boundary »* après la fusion Codex — quand le navigateur reste gouvernable par SSO/DLP/CASB. Et pour qui publie, **la fragilité des chiffres est l'information**.

**Now What.** Desktop si l'IA est invoquée plusieurs fois par heure et que les workflows passent par fichiers, captures ou agents ; web sinon. Côté DSI : inventorier les permissions, désactiver Computer Use et Cowork par défaut, cadrer les extensions MCP, gérer les mises à jour (**sur Linux hors apt, pas de mise à jour automatique**). Côté publication : ne citer que verbatims et dates confirmés, et produire son propre mini-benchmark reproductible — quelques heures pour des chiffres enfin citables.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Deep Research Veille Interne | ORGANISATION | affirme_que | les applications desktop et web de ChatGPT et Claude appellent exactement les mêmes modèles cloud, toute la différence tenant à l'enveloppe applicative | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Deep Research Veille Interne | ORGANISATION | affirme_que | le consensus qualitatif en faveur du desktop est solide et sourcé, alors que la quasi-totalité des chiffres qui l'étayent ne résiste pas à la vérification | AFFIRMATION | 0.96 | DYNAMIQUE | déclaré_article |
| chiffre orphelin | CONCEPT | observé_dans | sept affirmations chiffrées sur les applications desktop, toutes non confirmées : pages en 404, sources introuvables, benchmark mal attribué, posts non authentifiés | AFFIRMATION | 0.9 | DYNAMIQUE | inféré |
| Deep Research Veille Interne | ORGANISATION | s_oppose_à | la reprise des benchmarks chiffrés attribués à Alibaba Product Insights, Skywork, Cosmo Edge et Zenken AI sur ce sujet | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| Skywork | ORGANISATION | mesure | son propre agent Windows, et non Claude Desktop contre la version web | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| ChatGPT Desktop | TECHNOLOGIE | permet | un raccourci global, une companion window au premier plan et des captures d'écran natives | AFFIRMATION | 0.94 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | la fusion de Codex et ChatGPT en une application desktop unifiée le 9 juillet 2026, l'ancienne app devenant ChatGPT Classic | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Claude Desktop | TECHNOLOGIE | utilise | Desktop Extensions | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Desktop Extensions | TECHNOLOGIE | permet | d'installer un serveur MCP local en cliquant un bouton | CITATION | 0.92 | DYNAMIQUE | déclaré_article |
| Desktop Extensions | TECHNOLOGIE | utilise | Model Context Protocol | TECHNOLOGIE | 0.93 | ATEMPOREL | déclaré_article |
| Claude Desktop | TECHNOLOGIE | utilise | Cowork | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Desktop | TECHNOLOGIE | utilise | Computer Use | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Computer Use | TECHNOLOGIE | utilise | les permissions système d'Accessibilité et d'enregistrement d'écran | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Deep Research Veille Interne | ORGANISATION | affirme_que | l'application desktop n'est plus un client de chat mais un runtime d'agents avec accès à la machine | CITATION | 0.95 | DYNAMIQUE | déclaré_article |
| frontière de confiance | CONCEPT | s_applique_à | l'arbitrage entre un client desktop qui obtient des permissions système et un navigateur gouvernable par SSO, DLP et CASB | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| ChatGPT Desktop | TECHNOLOGIE | s_oppose_à | la gouvernance d'entreprise, en réunissant exécution de code, navigateur et connecteurs dans une frontière de confiance élargie | AFFIRMATION | 0.87 | DYNAMIQUE | déclaré_article |
| Deep Research Veille Interne | ORGANISATION | recommande | de désactiver Computer Use et Cowork par défaut, de cadrer les extensions MCP autorisées et d'organiser les mises à jour par MDM avant tout déploiement desktop | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Claude Desktop | TECHNOLOGIE | observé_dans | une beta Linux qui ne se met pas à jour automatiquement hors dépôt apt | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Deep Research Veille Interne | ORGANISATION | affirme_que | le gain du desktop est un gain de friction et non de puissance, réel uniquement pour les usages intensifs | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Yuri Dvoinos | PERSONNE | s_oppose_à | l'avantage attribué à Claude Desktop, en rapportant 68 % de CPU consommés et un lag de saisie sur MacBook Pro | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| Claude Desktop | TECHNOLOGIE | utilise | Electron | TECHNOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| Deep Research Veille Interne | ORGANISATION | affirme_que | l'avantage du desktop est une promesse d'implémentation et non une loi de la nature | CITATION | 0.94 | ATEMPOREL | déclaré_article |
| Deep Research Veille Interne | ORGANISATION | recommande | de ne citer que les verbatims et dates confirmés, et de produire un mini-benchmark maison reproductible plutôt que de reprendre des chiffres invérifiables | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| navigateur IA | TECHNOLOGIE | concurrence | l'opposition entre application desktop et version web, comme troisième voie | AFFIRMATION | 0.82 | DYNAMIQUE | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| chiffre orphelin | CONCEPT | définition | Donnée chiffrée largement reprise dont la source ne résiste pas à la vérification : soit attribuée à une institution au nom plausible dont la page renvoie une erreur, soit issue d'un benchmark réel mais portant sur une autre comparaison que celle qu'on lui prête | AJOUT |
| frontière de confiance | CONCEPT | définition | Périmètre des permissions qu'un client obtient sur la machine de l'utilisateur ; un client desktop doté d'accès aux fichiers, à l'écran et à l'exécution de code élargit ce périmètre là où un navigateur reste gouvernable par SSO, DLP et CASB | AJOUT |
| Claude Desktop | TECHNOLOGIE | définition | Client de bureau d'Anthropic (Mac et Windows depuis le 31 octobre 2024, beta Linux le 30 juin 2026) : Quick Entry sur macOS, Desktop Extensions pour installer un serveur MCP local en un clic, accès aux fichiers locaux, onglets Chat / Cowork / Code. Construction Electron plus couches natives | AJOUT |
| ChatGPT Desktop | TECHNOLOGIE | définition | Client de bureau d'OpenAI (macOS annoncé le 13 mai 2024, disponible le 25 juin) : raccourci global Option/Alt + Espace, companion window au premier plan, captures d'écran natives ; fusionné avec Codex le 9 juillet 2026 en une app à onglets Chat / Work / Codex, l'ancienne version devenant ChatGPT Classic | AJOUT |
| Cowork | TECHNOLOGIE | définition | Capacité agentique d'Anthropic lancée en research preview le 12 janvier 2026 (macOS, plan Max), étendue au web, iOS et Android le 7 juillet 2026 ; à désactiver par défaut en contexte d'entreprise | AJOUT |
| Computer Use | TECHNOLOGIE | rôle | Capacité de pilotage de la machine par le modèle, en public beta depuis le 22 octobre 2024 ; exige les permissions système d'Accessibilité et d'enregistrement d'écran, ce qui en fait un point de décision de gouvernance | MISE_A_JOUR |
| Desktop Extensions | TECHNOLOGIE | définition | Format d'empaquetage d'Anthropic pour installer un serveur MCP local depuis le client de bureau sans configuration manuelle ; extension `.dxt` renommée `.mcpb` le 11 septembre 2025 | AJOUT |
| Deep Research Veille Interne | ORGANISATION | rôle | Auteur du rapport ; applique un format What / So What / Now What et consacre une section entière à l'audit de ce que l'enquête n'a pas pu confirmer, motif par motif | MISE_A_JOUR |
| navigateur IA | TECHNOLOGIE | positionnement | Troisième terme possible du duel desktop/web : le critique le plus virulent de Claude Desktop utilise Claude dans le navigateur d'OpenAI, ce qui déplace la question du client natif vers la surface de navigation | AJOUT |
