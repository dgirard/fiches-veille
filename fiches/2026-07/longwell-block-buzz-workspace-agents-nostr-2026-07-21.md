---
themes: [architecture-construction, outils-plateformes, agents-codage-ia-skills]
source: "Block Engineering"
---
# longwell-block-buzz-workspace-agents-nostr-2026-07-21

## Veille

Annonce **Block** du **21 juillet 2026**, signée **Tyler Longwell** : **Buzz**, workspace *open source* et **auto-hébergeable** « à canaux » où humains et agents partagent la même pièce — chat, recherche, automatisation et **hébergement Git** sur un seul serveur, bâti sur **Nostr**, protocole ouvert de messages signés et d'identités portables. Thèse d'ouverture : *« Models can do the work now. Teams still need somewhere to do it together. The bottleneck moved from intelligence to coordination. »* Trois pièces d'ingénierie. **(A) L'identité des agents.** Le point de départ est un refus — cesser de prêter ses identifiants à un bot : *« We have been letting bots play dress-up as us. It's weird. It's dangerous. »* Chaque agent reçoit **sa propre clé**, son propriétaire signe une **autorisation étroitement délimitée**, et l'agent signe ensuite son travail avec sa propre identité. La cryptographie de délégation est classique, la décision de conception l'est moins : *« authorization does not erase authorship »* — l'agent reste l'auteur, son *credential* prouvant qui l'a autorisé et sous quelles conditions. Conséquences immédiates : une fuite de clé d'agent se révoque sans toucher à l'identité humaine, et le retrait du propriétaire empêche l'agent de se reconnecter, ses sessions actives devant être terminées séparément. **(B) Git sur stockage objet.** Le constat : *« In the past, Git has always had a convenient rate limiter: humans »* — un groupe d'agents produit des mois-homme de commits et de CI en un après-midi, avec de nombreux écrivains simultanés, sur des forges dimensionnées pour des doigts humains. Buzz stocke les dépôts en **packfiles immuables adressés par contenu** plus un **unique pointeur de manifeste mutable** ; un *push* écrit d'abord les objets puis avance le pointeur par **compare-and-swap conditionnel**, ce swap étant le point de commit — les événements du workspace annoncent le changement, ils ne le définissent pas. Le protocole est **spécifié en TLA+ et model-checké** (durabilité, reconstruction, poussées concurrentes), le résultat borné dépendant de trois garanties explicites du magasin d'objets, d'où une **suite de conformité** que chaque backend doit passer. **(C) Interopérabilité et confidentialité.** Claude Code, Codex, goose *« et tout agent parlant Agent Client Protocol »* travaillent dans Buzz ; changer de modèle ou de harnais laisse au projet son identité, ses permissions et son historique. Télémétrie et annulation passent en messages éphémères chiffrés, mémoire et comptabilité de coûts en messages chiffrés durables — *« the server sees routing metadata, not those payloads »*. Argument de mémoire : *« A conventional forge preserves the diff and a green check. Buzz also preserves why the obvious fix was wrong. »* Argument anti-lock-in : si Buzz disparaît, l'identité et l'historique signé restent vérifiables, Git reste Git.

## Titre Article

Buzz!

## Date

2026-07-21

## URL

https://engineering.block.xyz/blog/buzz

## Keywords

Buzz, Block, workspace agentique, canal, channel-driven, auto-hébergeable, self-hostable, open source, Nostr, protocole ouvert, messages signés, identité portable, paire de clés, keypair, identité d'agent, clé par agent, autorisation déléguée, cryptographie de délégation, authorization does not erase authorship, authorship, paternité, révocation de clé, credentials partagés, usurpation d'identité, bot dress-up, périmètre d'autorisation, scope, sessions actives, Agent Client Protocol, ACP, Claude Code, Codex, goose, harness, portabilité de harness, orchestration multi-agents, agent frontier, swarm, agents bon marché, coordination, goulet d'étranglement, humain middleware, contexte partagé, mémoire de canal, canal éphémère, décision de merge signée, historique visible, chemins d'échec, forge Git, hébergement Git, Git sur stockage objet, packfile immuable, adressage par contenu, pointeur de manifeste, compare-and-swap, commit point, TLA+, model checking, vérification formelle, suite de conformité, garanties du magasin d'objets, appairage d'appareils, QR, code à six chiffres, messages éphémères chiffrés, métadonnées de routage, partage de GPU, inférence pair-à-pair, anti-lock-in, souveraineté de l'historique, Tyler Longwell, engineering.block.xyz, github.com/block/buzz

## Authors

**Tyler Longwell** — *« Building multi-player AI at Block »*, auteur unique et signataire à la première personne. Publié le **21 juillet 2026** sur le blog Block Engineering.

L'auteur a construit le prédécesseur du produit qu'il présente : *« I helped build Block's first Slack-integrated agent… I added enough glue to incorporate as a small adhesives business »*. L'argumentaire part d'une liste de questions restées sans réponse dans ce montage — *Does everyone get a bot? If people share one, whose credentials does it use?* (le sondage interne où *« everyone volunteered someone else »*), que faire quand une équipe veut changer de modèle ou de runtime. Note de clôture : *« We wrote this post in a Buzz channel with our team and our agents. We wrote Buzz there too. »*

## Ton

**Profil** : billet d'ingénierie de lancement produit, registre **praticien**, écrit à la première personne du singulier — rare pour une annonce d'entreprise. Public : ingénieurs plateforme et équipes qui orchestrent déjà plusieurs agents et en paient le coût de coordination.

**Style** : titres de sections en **calembours d'abeille** (*Hive to Survive*, *Headfirst into the Swarm*, *Bee Yourself*, *Git for the Hive Mind*, *Honey, I Saved the Context*) qui masquent une progression parfaitement sérieuse : problème vécu → substrat (Nostr) → identité → stockage → mémoire → gouvernance. Trois traits :

1. **L'humour comme accélérateur, pas comme remplissage.** *« a sufficiently ambitious toaster »*, *« alt-tabbing between them like a day trader »*, *« Connecting the two casually is how your cool new feature becomes an archaeological project »*. Chaque blague porte un argument technique.
2. **La formulation morale du problème d'identité.** *« The usual way to authorize an agent is to give it your credentials and hope it doesn't embarrass you. »* / *« If I see your face, I want to know it's you talking to me. »* Le texte ne traite pas l'identité d'agent comme une contrainte de conformité mais comme une **question de confiance sociale**.
3. **L'aveu d'immaturité, non négocié.** *« We're still very early in Buzz's life. There are rough edges and giant chasms between what we can see on the horizon and what exists today »* — placé **après** l'argumentaire, pas noyé dedans.

**Formules-marqueurs** : *« The bottleneck moved from intelligence to coordination »*, *« authorization does not erase authorship »*, *« We have been letting bots play dress-up as us »*, *« Nobody enjoyed being middleware »*, *« We put Git on object storage. On purpose! »*, *« Buzz also preserves why the obvious fix was wrong »*, *« it's 2026: software got cheap. Taste didn't »*, *« A protocol anyone can rebuild is a protocol nobody can lock you into »*, *« The room itself has become part of the team's intelligence »*.

**Position épistémique** : **affirmative sur le design, silencieuse sur les preuves**. Aucune mesure, aucun benchmark, aucun chiffre d'adoption — les affirmations de bénéfice (*« easier, faster, and more effective than any coordination tool or process we've used »*) sont des **témoignages d'usage interne**, pas des résultats. La seule preuve *formelle* du billet porte sur le **stockage Git** (TLA+), pas sur la productivité annoncée. C'est le complément exact du billet suivant de la série ([[patel-block-buzz-teams-tokens-benchmarks-2026-08-06]]), qui apporte les chiffres — et qui en tempère la promesse.

## Pense-betes

- **La phrase qui justifie l'existence de la catégorie** : ***« Models can do the work now. Teams still need somewhere to do it together. The bottleneck moved from intelligence to coordination. »*** À reprendre telle quelle pour argumenter un budget « plateforme agent » : la dépense marginale utile n'est plus dans le modèle, elle est dans la **pièce où le travail se fait**. Le symptôme diagnostique associé est plus opérationnel encore : *« Agents made individual work faster and teamwork slower »* — si vos équipes constatent exactement ça, le problème n'est pas votre choix de modèle.

- **Le choix de conception à voler, même sans adopter Buzz** : ***« authorization does not erase authorship »***. Chaque agent a **sa clé** ; le propriétaire signe une **autorisation étroite** ; l'agent signe son travail **en son propre nom**, et son *credential* dit **qui l'a autorisé et sous quelles conditions**. Traduction en trois propriétés à exiger de toute plateforme d'agents en entreprise :
  1. **Révocation isolée** — la fuite d'une clé d'agent se révoque **sans reémettre l'identité humaine** ;
  2. **Attribution non ambiguë** — l'audit distingue « l'agent a fait X » de « la personne a fait X » ;
  3. **Retrait en cascade** — un propriétaire retiré rend ses agents inconnectables (+ terminaison des sessions actives si le risque est immédiat).
  **L'anti-pattern nommé est très répandu** : partager les identifiants d'un humain avec un bot. Vérifiez ce que fait *votre* intégration Slack/CI actuelle avant de juger celle des autres.

- **Git n'a plus son limiteur de débit — le constat est transposable à toute votre chaîne d'outillage.** *« In the past, Git has always had a convenient rate limiter: humans. We sleep, eat, attend meetings, and sometimes think before pushing. Agents remove those limits. »* Un groupe d'agents produit des **mois-homme de commits et de CI en un après-midi**. **À faire chez vous** : lister les systèmes dont le dimensionnement supposait implicitement une cadence humaine — forge, CI, revue, quotas d'API, alerting, revue sécurité — et regarder lequel casse en premier. C'est un exercice de capacité, pas de gouvernance.

- **La réponse technique, propre et copiable** : dépôts en **packfiles immuables adressés par contenu** + **un pointeur de manifeste mutable** ; un *push* écrit les objets d'abord, puis avance le pointeur par **compare-and-swap conditionnel**. **La règle qui rend le modèle sain** : *« That pointer update is the commit point. Workspace events announce the change; they do not define it. »* — l'événement de canal est une **notification**, jamais la source de vérité. Pattern généralisable à toute intégration event-driven sur un stockage objet.

- **Lire la garantie formelle avec sa clause de portée.** Le protocole est **spécifié en TLA+ et model-checké** (durabilité, reconstruction, poussées concurrentes) — mais *« the bounded result depends on three explicit object-store guarantees, so every backend must pass a conformance suite »*. Autrement dit : **la preuve vaut pour un magasin d'objets conforme**, et la conformité est déléguée à une suite de tests. Question à poser avant tout auto-hébergement : *mon S3-compatible passe-t-il la suite ?* Le billet ne nomme pas les trois garanties.

- **Interopérabilité — le point qui compte pour la stratégie d'outillage** : **Claude Code, Codex, goose, et tout agent parlant [[Agent-Client-Protocol]]** travaillent dans Buzz ; *« Change the model or harness and the project keeps its identity, permissions, and history. »* → l'identité et l'historique sont attachés au **projet**, pas au *harness*. Attention au sigle : c'est bien l'**Agent Client Protocol** (client ↔ agent), pas l'*Agentic Commerce Protocol* — cf. [[girard-acp-deux-protocoles-un-sigle-2026-08-02]]. Pour la brique ACP elle-même : [[agentclientprotocol-introduction-2026-08-02]].

- **La valeur réelle promise n'est pas le chat, c'est la mémoire des raisons.** *« Search auth refresh six months later and find the report, rejected fix, patch, review, and final call. A conventional forge preserves the diff and a green check. Buzz also preserves why the obvious fix was wrong. »* → **le rapprochement à faire** : c'est un argument de *context engineering* déguisé en argument de collaboration — le contexte partagé reste dans le canal **au lieu d'être compressé dans des prompts privés**. À relier à [[kb-context-engineering]] et à la thèse de la mémoire d'agent.

- **Observation qui mérite d'être vérifiée ailleurs** : *« The agents also invent coordination we didn't script: recruiting each other, splitting work into side channels, handing tasks across contexts. »* **Anecdotique et non mesuré** — mais si c'est robuste, c'est un fait de conception majeur (la coordination émerge d'un substrat de messagerie ouvert, sans orchestrateur). À confronter aux résultats chiffrés du billet suivant, qui montrent au contraire que **la composition d'équipe ne paie pas sur les tâches courtes** : patel-block-buzz-teams-tokens-benchmarks-2026-08-06.

- **Confidentialité — ce qui est chiffré et ce qui ne l'est pas** : télémétrie live et annulation = **messages éphémères chiffrés** ; mémoire et enregistrements de coût = **chiffrés mais durables** ; le serveur voit *« routing metadata, not those payloads »*. Buzz peut router l'inférence vers **la machine d'un autre membre** (mutualisation de GPU) : Buzz présente les pairs autorisés, puis **le trafic modèle chiffré circule directement entre eux**. → Intéressant pour une équipe qui veut mutualiser du calcul local ; à instruire côté DLP, car la charge sort du périmètre serveur.

- **L'argument anti-lock-in, formulé de façon réutilisable** : *« If Buzz disappears, your identity and signed history still verify. Git remains Git and can be rehosted… A protocol anyone can rebuild is a protocol nobody can lock you into. »* Et la version gouvernance : *« Running the infrastructure shouldn't mean owning the identities, history, or work that passes through it. »* → **Critère d'achat transposable** : pour toute plateforme d'agents, demander ce qui **survit à la disparition du fournisseur** — identités, historique vérifiable, artefacts réhébergeables. Argument de vendeur, mais **testable** : Block publie code, specs de protocole, vecteurs de test, sections sécurité et modèles formels (github.com/block/buzz).

- **Contexte Block — à ne pas manquer.** Ce n'est pas un coup isolé : Block a déjà goose et le travail MCP-UI (block-goose-mcp-ui-future-agentic-interfaces-2025-08-25), et sa position sur la **monétisation de l'IA** est documentée par ailleurs (paymentsdive-block-dorsey-pricing-ia-2026-08-06). La formule d'auto-désignation du billet — *« That's what an intelligence company like Block needs »* — mérite d'être notée : **Block se qualifie d'*intelligence company***, pas d'entreprise de paiements.

- **Ce que le billet ne dit pas, et qu'il faut demander** : aucun chiffre (adoption, productivité, coût), aucune comparaison à Slack/Teams/forge existante, aucune discussion du **coût opérationnel** de l'auto-hébergement, ni du modèle de modération/gouvernance des canaux à l'échelle d'une entreprise. Les preuves formelles couvrent le **stockage**, pas les bénéfices annoncés.

## RésuméDe400mots

Billet d'ingénierie de **Block** signé **Tyler Longwell**, publié le **21 juillet 2026**, annonçant **Buzz** : un workspace *open source*, **auto-hébergeable** et organisé en canaux, où humains et agents travaillent dans la même pièce — messages, recherche, automatisation **et hébergement Git** sur un même serveur.

**Le point de départ est un échec vécu.** L'auteur a construit le premier agent Slack de Block ; il fonctionnait, mais laissait sans réponse des questions d'exploitation : chacun a-t-il son bot ? Si un bot est partagé, **de qui sont les identifiants** ? Que faire quand une équipe change de modèle ou de *runtime* ? D'où la thèse : *« Models can do the work now. Teams still need somewhere to do it together. The bottleneck moved from intelligence to coordination. »*

**Le substrat est Nostr** — protocole ouvert de messages signés et d'identités portables. Une identité est une **paire de clés**, chaque action est signée : la même identité envoie un message, autorise un agent, approuve un *workflow*, signe un commit, fusionne un changement. **Claude Code, Codex, goose et tout agent parlant Agent Client Protocol** travaillent dans Buzz ; changer de modèle ou de *harness* laisse au projet son identité, ses permissions et son historique.

**Le cœur du billet est l'identité des agents.** Plutôt que de prêter ses identifiants à un bot — *« We have been letting bots play dress-up as us »* —, chaque agent reçoit **sa propre clé**. Son propriétaire signe une **autorisation étroite** ; l'agent signe ensuite son travail **en son propre nom**. Le choix sémantique est explicite : ***« authorization does not erase authorship »***. La clé d'un agent compromis se révoque **sans toucher à l'identité humaine** ; retirer le propriétaire déconnecte l'agent.

**Deuxième pièce d'ingénierie : Git sur stockage objet.** Les agents suppriment le limiteur de débit qu'étaient les humains ; un groupe produit des mois-homme de commits en un après-midi. Buzz stocke les dépôts en **packfiles immuables adressés par contenu** plus **un pointeur de manifeste mutable**, avancé par **compare-and-swap conditionnel** — ce *swap* est le point de commit, les événements de canal l'annoncent sans le définir. Le protocole est **spécifié en TLA+** et model-checké ; le résultat dépend de **trois garanties du magasin d'objets**, d'où une **suite de conformité** par *backend*.

**La valeur promise est mnésique** : un canal éphémère par tâche agrège discussion, patchs, CI, revue et décision signée. *« A conventional forge preserves the diff and a green check. Buzz also preserves why the obvious fix was wrong. »*

**Et l'open source est argumenté** : *« it's 2026: software got cheap. Taste didn't. »* Si Buzz disparaît, identités et historique signé se vérifient toujours. Aucun chiffre, aucun benchmark : le billet est un exposé de design, pas une preuve d'effet.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Block | ORGANISATION | publie | Buzz | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Tyler Longwell | PERSONNE | travaille_chez | Block | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Tyler Longwell | PERSONNE | affirme_que | le goulet d'étranglement est passé de l'intelligence à la coordination : les modèles savent faire le travail, les équipes ont encore besoin d'un lieu pour le faire ensemble | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | Nostr | TECHNOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| Nostr | TECHNOLOGIE | permet | des identités portables sous forme de paires de clés et des actions signées, indépendantes du serveur qui les héberge | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | permet | à chaque agent d'avoir sa propre clé, son autorisation signée par son propriétaire et sa propre signature sur son travail | AFFIRMATION | 0.97 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | affirme_que | l'autorisation n'efface pas la paternité : l'agent reste l'auteur, son credential prouve qui l'a autorisé et sous quelles conditions | CITATION | 0.96 | ATEMPOREL | déclaré_article |
| identité déléguée d'agent | CONCEPT | résout | l'usage des identifiants d'un humain par un bot, et permet de révoquer un agent compromis sans remplacer l'identité humaine | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | Agent Client Protocol | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | s_applique_à | Claude Code, Codex et goose, ainsi qu'à tout agent parlant Agent Client Protocol | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | permet | de changer de modèle ou de harness sans que le projet perde son identité, ses permissions ou son historique | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Tyler Longwell | PERSONNE | affirme_que | les agents ont rendu le travail individuel plus rapide et le travail d'équipe plus lent, chaque passage de main exigeant un humain pour transporter le contexte | CITATION | 0.94 | DYNAMIQUE | déclaré_article |
| agents de codage | TECHNOLOGIE | s_oppose_à | le limiteur de débit humain sur lequel les forges Git étaient implicitement dimensionnées | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | des packfiles immuables adressés par contenu sur stockage objet, plus un pointeur de manifeste mutable avancé par compare-and-swap conditionnel | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | affirme_que | la mise à jour du pointeur est le point de commit, les événements du workspace annonçant le changement sans le définir | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | utilise | TLA+ | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| TLA+ | TECHNOLOGIE | permet | de model-checker la durabilité, la reconstruction et les poussées concurrentes du protocole de stockage Git de Buzz | AFFIRMATION | 0.94 | STATIQUE | déclaré_article |
| Buzz | TECHNOLOGIE | utilise | une suite de conformité que chaque backend de stockage objet doit passer, le résultat borné dépendant de trois garanties explicites | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | permet | de router les requêtes d'inférence d'un agent vers la machine d'un autre membre, le trafic chiffré circulant directement entre pairs autorisés | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | réduit | la compression du contexte partagé dans des prompts privés, en gardant discussion, patchs, CI, revue et décision de merge dans un même canal | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | affirme_que | une forge classique conserve le diff et une coche verte, là où Buzz conserve aussi pourquoi le correctif évident était faux | CITATION | 0.95 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | concurrence | Slack | TECHNOLOGIE | 0.82 | DYNAMIQUE | inféré |
| Block | ORGANISATION | affirme_que | une équipe doit contrôler ses propres identités d'agents, son historique et son travail, indépendamment de tout fournisseur ou plateforme | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | permet | à une identité et à un historique signé de rester vérifiables même si Buzz disparaît, un dépôt Git restant réhébergeable | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | affirme_que | en 2026 le logiciel est devenu bon marché mais pas le goût, les choix de design étant la partie difficile | CITATION | 0.92 | ATEMPOREL | déclaré_article |
| Buzz | TECHNOLOGIE | est_instance_de | workspace collaboratif humains-agents auto-hébergeable | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Block | ORGANISATION | publie | goose | TECHNOLOGIE | 0.9 | STATIQUE | généré_assistant |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Buzz | TECHNOLOGIE | définition | Workspace open source et auto-hébergeable organisé en canaux, publié par Block le 21 juillet 2026, où humains et agents partagent la même pièce : messages, recherche, automatisation et hébergement Git sur un seul serveur, bâti sur le protocole Nostr | AJOUT |
| Buzz | TECHNOLOGIE | identité des agents | Chaque agent reçoit sa propre paire de clés ; son propriétaire signe une autorisation étroitement délimitée et l'agent signe son travail en son propre nom — « authorization does not erase authorship ». Révocation d'un agent sans remplacement de l'identité humaine, déconnexion en cascade si le propriétaire est retiré | AJOUT |
| Buzz | TECHNOLOGIE | stockage Git | Dépôts stockés en packfiles immuables adressés par contenu sur stockage objet, plus un pointeur de manifeste mutable avancé par compare-and-swap conditionnel qui constitue le point de commit ; protocole spécifié en TLA+ et model-checké, avec suite de conformité obligatoire par backend | AJOUT |
| Buzz | TECHNOLOGIE | interopérabilité | Claude Code, Codex, goose et tout agent parlant Agent Client Protocol peuvent y travailler ; changer de modèle ou de harness préserve l'identité, les permissions et l'historique du projet | AJOUT |
| Buzz | TECHNOLOGIE | confidentialité | Télémétrie et annulation en messages éphémères chiffrés, mémoire et comptabilité de coûts chiffrées mais durables ; le serveur ne voit que des métadonnées de routage. L'inférence peut être routée vers la machine d'un pair autorisé, le trafic modèle chiffré circulant directement entre eux | AJOUT |
| Buzz | TECHNOLOGIE | code source | Ouvert : code, spécifications de protocole, vecteurs de test, sections sécurité et modèles formels publiés sur github.com/block/buzz ; site buzz.xyz | AJOUT |
| Nostr | TECHNOLOGIE | définition | Protocole ouvert de messages signés et d'identités portables, où une identité est une paire de clés ; sert de substrat à Buzz pour signer messages, autorisations d'agents, approbations de workflow, commits et merges avec la même identité | AJOUT |
| identité déléguée d'agent | CONCEPT | définition | Modèle d'autorisation où l'agent possède sa propre clé et signe son travail lui-même, tandis que le credential signé par son propriétaire atteste qui l'a autorisé et sous quelles conditions ; l'autorisation n'efface pas la paternité, ce qui rend la révocation et l'attribution indépendantes de l'identité humaine | AJOUT |
| TLA+ | TECHNOLOGIE | usage | Employé par Block pour spécifier et model-checker le protocole de stockage Git de Buzz : durabilité, reconstruction et poussées concurrentes, sous réserve de trois garanties explicites du magasin d'objets | AJOUT |
| Tyler Longwell | PERSONNE | rôle | Ingénieur chez Block, « Building multi-player AI » ; auteur du billet de lancement de Buzz et constructeur du premier agent intégré à Slack chez Block, dont les limites d'exploitation motivent Buzz | AJOUT |
| Block | ORGANISATION | positionnement | Se qualifie dans ce billet d'« intelligence company » et publie Buzz en open source, au motif qu'une équipe doit contrôler ses identités d'agents, son historique et son travail indépendamment de tout fournisseur | AJOUT |
| Agent Client Protocol | TECHNOLOGIE | rôle | Protocole d'interopérabilité client↔agent accepté par Buzz : tout agent qui le parle peut travailler dans le workspace, aux côtés de Claude Code, Codex et goose | MISE_A_JOUR |
