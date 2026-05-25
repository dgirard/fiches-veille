# uber-engineering-agent-identity-crisis-zero-trust-spire-2026-05-21

## Veille

Article d'ingénierie publié sur le blog d'**Uber** par six ingénieurs (Matt Mathew, Prasad Borole, Meng Huang, Sergey Burykin, Gaurav Goel, Bayard Walsh) le **21 mai 2026**, exposant la **doctrine d'identité et de contrôle d'accès des agents IA** déployée en production chez Uber pour plusieurs milliers d'agents internes. **Thèse-pivot** : les modèles d'identité existants (humains + workloads) ne décrivent pas l'**agency** — *« an agent is best defined as an entity that is authorized to act for or in the place of another »* — et perdent la **provenance** à travers les hops d'un workflow agentique. **Deux problèmes opérationnels identifiés** : (1) ***« Current Identity Model Doesn't Describe Agency »*** — la délégation est le mode par défaut, les workflows sont compositionnels (agents qui appellent agents qui appellent tools), le comportement est dynamique (plans évoluent selon résultats intermédiaires) ; (2) ***« Original Provenance Isn't Effectively Carried Forward Across Agents to Systems »*** — *« Execution context (originating user, intermediate agents) is dropped across agent hops. »* **Architecture proposée** comme extension de la Zero Trust Architecture Uber : **Agent Registry** (source of truth des mappings agent↔workload) + **AI Agent Mesh** (data plane inter-agents) + **STS (Security Token Service)** (émission JWT scopés courts) + **MCP Gateway** (policy enforcement point pour invocation d'outils) + **AI Gateway** (médiation appels LLM externes avec guardrails) + **SPIRE** (provider de workload credentials). **Mécanique cryptographique** : workloads récupèrent des **SVID (SPIFFE Verifiable IDs)** signés cryptographiquement depuis SPIRE → SDK demande JWT au STS via identité workload → STS vérifie l'autorisation agent contre Agent Registry → token court (TTL en minutes) émis pour **destination single-hop spécifique** (claim `Audience` ciblé). **Doctrine pivot** : ***« Single-hop, short-lived tokens. Every JWT minted by the STS is intended for a single hop, with a specific Audience claim and a short time-to-live in the order of minutes. »*** **Préservation de la chaîne d'acteurs** : exemple multi-hop avec on-call engineer `user1` → Oncall Agent (Workload-1) → Investigation Agent (Workload-2) → MCP Gateway ; le JWT final transporte l'**actor chain `[user1, oncall-agent, investigation-agent]`** vérifiable, permettant des décisions d'accès tool-level basées sur l'**historique complet de la requête**. **Standardisation** : **Standardized A2A (Agent-to-Agent) Client** qui automatise les échanges STS et la propagation de l'actor chain — *« the secure path is also the easiest path for developers to implement A2A calls »* — migration phasée des agents legacy. **Métriques production** : ***« P99 latency for the STS Token Exchange API is consistently below 40 milliseconds »***, milliers d'agents internes adoptés, dashboard d'observabilité temps réel traçant les sessions multi-agents. **Vision long terme — three-layer framework** : (1) Identity & Trust Foundation (identité agent vérifiable + delegation chains), (2) Dynamic Access Control (permissions context-based + human-in-the-loop), (3) Unified Enforcement Plane (politique centralisée observable). **Alignement standards** : IETF **WIMSE** working group + draft `draft-klrc-aiagent-auth-01` *AI Agent Authentication and Authorization*, basé conceptuellement sur **OAuth 2.0 Token Exchange (RFC 8693)** et **SPIFFE/SPIRE** (graduated CNCF). Première publication de référence d'un hyperscaler non-AI-lab (logistique/mobilité) qui industrialise la sécurité des agents au niveau infrastructure, comblant le gap doctrinal entre les frameworks de skills/harness (Vincent, Lattice, PROJ-AI) et les questions d'identité enterprise grade.

## Titre Article

Solving the Identity Crisis for AI Agents

## Date

2026-05-21

## URL

https://www.uber.com/us/en/blog/solving-the-agent-identity-crisis/

## Keywords

Uber Engineering, AI agent identity, agent identity crisis, agency definition, agent-as-delegate, multi-hop workflow, actor chain, provenance preservation, Zero Trust Architecture, Agent Registry, AI Agent Mesh, Security Token Service STS, MCP Gateway, AI Gateway, MCP tool invocation, SPIRE workload identity, SPIFFE Verifiable IDs SVID, JWT short-lived tokens, audience claim, single-hop tokens, per-hop token exchange, OAuth 2.0 Token Exchange RFC 8693, A2A protocol agent-to-agent, Standardized A2A Client, BaseAgentProtocolClient, IETF WIMSE working group, draft-klrc-aiagent-auth-01, AI Agent Authentication and Authorization, on-call engineer agent, Oncall Agent, Investigation Agent, Monitoring Agent, audit trail, fine-grained access policy, policy enforcement point, data redaction AI Guard, secure-by-default, P99 latency 40ms, identity trust foundation, dynamic access control, unified enforcement plane, three-layer framework, agent observability, audit governance, agent provenance, delegation chain, cryptographically signed workload credentials, SPIFFE CNCF graduated, agent-to-workload mapping, Uber internal agents, thousands of agents production, agent infrastructure security, agent mesh, secure path easiest path, legacy agent migration phased refactoring, identity model limitations, downstream systems policy, contextual attribution

## Authors

**Matt Mathew** (Sr Staff Engineer), **Prasad Borole** (Staff Software Engineer), **Meng Huang** (Engineering Manager), **Sergey Burykin** (Sr Software Engineer), **Gaurav Goel** (Software Engineer II), **Bayard Walsh** (Software Engineer I). Tous chez **Uber**, équipe Security/Identity infrastructure responsable du déploiement de l'architecture d'identité agentique en production. Composition d'équipe représentative : un Engineering Manager, un Staff senior cadre, un Staff IC architecte, deux SWE séniors/intermédiaires, un SWE I — pattern classique d'une équipe Uber qui livre une plateforme transverse mission-critical.

## Ton

**Profil** : Article d'ingénierie corporate technique-explicative, registre *engineering blog d'hyperscaler*. Format canonique Uber Engineering : exposition didactique d'une solution déployée en production, narration *problem-first* (deux problèmes identifiés et nommés), schémas d'architecture (Figures 1-4 mentionnées), exemple-walkthrough multi-hop concret, métriques de validation, vision long terme. Pas de marketing déguisé, pas d'hyperbole — registre **operational engineering memo** destiné à un public d'ingénieurs sécurité, d'architectes plateforme, et de tech leads.

**Style** : Voix ingénieur-architecte plurielle (six co-auteurs), registre **anglo-saxon-corporate-precise** caractéristique d'Uber Eng :
1. **Définitions axiomatiques courtes** — *« An agent is best defined as an entity that is authorized to act for or in the place of another. »* Une définition qui tient en 18 mots et qui structure tout le reste du document. Mode *propositional*.
2. **Énumération orthogonale des contraintes** — *« Delegation is the default mode... Workflows are compositional... Behavior is dynamic »* — trois propriétés mutually exclusive, collectively exhaustive, qui justifient le besoin d'un nouveau modèle d'identité.
3. **Pattern problème → composant → mécanisme → exemple → métrique** — chaque couche est introduite par le problème qu'elle résout, puis spécifiée par son rôle, puis détaillée par sa mécanique (tokens, claims, audience), puis instanciée par un walkthrough, puis validée par une mesure. Pédagogie *zoom-in zoom-out* maîtrisée.
4. **Précision lexicale** — *« short-lived tokens », « single-hop », « specific Audience claim », « time-to-live in the order of minutes », « cryptographically signed »* — vocabulaire dense en termes techniques précis, sans paraphrase.

**Métaphores et formules-clés** :
- ***« An agent is best defined as an entity that is authorized to act for or in the place of another »*** — la **définition fondatrice de l'agency** par Uber, qui pose la délégation comme propriété axiomatique de l'agent.
- ***« Execution context (originating user, intermediate agents) is dropped across agent hops »*** — formule de cadrage du problème de provenance, courte et opérante.
- ***« Single-hop, short-lived tokens »*** — slogan-doctrine de la solution, équivalent fonctionnel du *« least privilege »* en Zero Trust classique mais adapté au régime agentique.
- ***« The secure path is also the easiest path for developers to implement A2A calls »*** — doctrine d'adoption : sécurité par défaut sans friction développeur (parallèle direct avec le *« paved road »* SRE classique).
- ***« P99 latency for the STS Token Exchange API is consistently below 40 milliseconds »*** — la formule-métrique qui clôt le débat *« cette architecture est-elle viable à l'échelle Uber ? »* — réponse : oui, et avec marge.

**Position épistémique** : Les auteurs parlent en **opérateurs en production** (milliers d'agents internes, P99 mesurée, dashboard d'observabilité existant). Ils ne théorisent pas — ils **documentent une solution livrée**. Le ton est confiant mais non triomphaliste, avec reconnaissance explicite que le travail continue (*« long-term vision »*, *« phased refactoring »* des agents legacy).

**Autorité construite par** : (a) la **traction production** (chiffres concrets — P99 <40ms, milliers d'agents), (b) la **profondeur architecturale** (six composants nommés, mécanique cryptographique exposée), (c) l'**alignement standards** (SPIFFE/SPIRE CNCF graduated, RFC 8693, IETF WIMSE), (d) la **composition d'équipe** (six co-auteurs sur le post — signal qu'il s'agit d'une plateforme transverse mature, pas d'un POC), (e) le **timing** (publié alors que la conversation industrie sur la sécurité agent est encore émergente — Uber prend une position de référence).

**Public et impact attendu** : Article calibré pour les **architectes plateforme et security engineers** des grandes entreprises qui commencent à déployer des agents IA en interne. Public secondaire : la communauté CNCF/SPIFFE, les contributeurs des drafts IETF WIMSE, les éditeurs MCP/gateway. Effet attendu : devenir une **référence canonique** dans la doctrine de sécurité agentique 2026, à côté des publications d'Anthropic sur les MCP, de Stripe sur Toolshed, et de Cloudflare sur l'edge.

## Pense-betes

- **Source** : blog Uber Engineering (uber.com/blog), publication officielle. Article du **21 mai 2026** — 2 jours avant la date de consultation 2026-05-23.

- **Auteurs (six co-auteurs)** :
  - **Matt Mathew** — Sr Staff Engineer
  - **Prasad Borole** — Staff Software Engineer
  - **Meng Huang** — Engineering Manager
  - **Sergey Burykin** — Sr Software Engineer
  - **Gaurav Goel** — Software Engineer II
  - **Bayard Walsh** — Software Engineer I
  - Équipe Security/Identity infrastructure Uber, responsable de l'architecture agent identity production.

- **Thèse-pivot épistémologique** : ***« An agent is best defined as an entity that is authorized to act for or in the place of another. »*** Cette définition pose la **délégation** comme propriété axiomatique de l'agent — ce qui change tout du modèle d'identité classique (humain ou workload, mais jamais *for someone else*).

- **Deux problèmes opérationnels nommés** :
  1. **Current Identity Model Doesn't Describe Agency** — les frameworks d'identité existants couvrent les humains et les workloads, mais ne modélisent pas l'**acting on behalf of** comme mode par défaut. Conséquences :
     - **Delegation is the default mode** — agents work on behalf of others
     - **Workflows are compositional** — agents call other agents, tools, and systems
     - **Behavior is dynamic** — plans evolve based on intermediate results
  2. **Original Provenance Isn't Effectively Carried Forward Across Agents to Systems** — *« Execution context (originating user, intermediate agents) is dropped across agent hops. »* Conséquences :
     - **Audit trails incomplets**
     - **Application incohérente** des politiques d'accès fine-grained
     - Pas de capacité à raisonner sur la chaîne complète d'acteurs ayant initié une requête

- **Architecture — six composants nommés** :
  | Composant | Rôle |
  |-----------|------|
  | **Agent Registry** | Source of truth pour les mappings agent↔workload |
  | **AI Agent Mesh** | Data plane pour la communication inter-agents |
  | **STS (Security Token Service)** | Émet des JWT courts et scopés (audience-specific) |
  | **MCP Gateway** | Policy enforcement point pour l'invocation d'outils (MCP tools) |
  | **AI Gateway** | Médiation des appels aux modèles IA externes + guardrails de sécurité (AI Guard pour redaction) |
  | **SPIRE** | Provider de credentials workload (extension de l'infra Zero Trust existante Uber) |

- **Mécanique cryptographique end-to-end** :
  1. Workloads récupèrent des **SPIFFE Verifiable IDs (SVIDs)** **cryptographiquement signés** depuis SPIRE.
  2. Le SDK demande des **JWT** au STS en utilisant l'identité workload (le SVID).
  3. Le STS **vérifie l'autorisation de l'agent** contre l'Agent Registry.
  4. **Short-lived tokens** émis pour une **destination single-hop spécifique** (claim `Audience` ciblé, TTL **en minutes**).
  5. Le token transporte la **chaîne complète des acteurs** participants (l'actor chain).

- **Doctrine *single-hop, short-lived* (formule canonique)** :
  > *« Single-hop, short-lived tokens. Every JWT minted by the STS is intended for a single hop, with a specific Audience claim and a short time-to-live in the order of minutes. »*

  Conséquences opérationnelles :
  - **Vol de token = blast radius minimal** (TTL minutes, audience unique)
  - **Pas de bearer token réutilisable cross-services** — contraste fort avec OAuth classique
  - **Chaque hop demande un nouveau token** — overhead réseau compensé par latency <40ms

- **Walkthrough multi-hop canonique (exemple article — Figure 4)** :
  1. **user1** (on-call engineer) initie une session avec **Oncall Agent**
  2. **Oncall Agent** contacte le STS, présente son identité SPIRE (Workload-1), demande un JWT pour **Investigation Agent**
  3. Oncall Agent envoie le JWT à **Investigation Agent** (Workload-2)
  4. **Investigation Agent** effectue un **token exchange** avec le STS pour obtenir une audience **MCP Gateway**
  5. **MCP Gateway** reçoit le JWT avec l'**actor chain `[user1, oncall-agent, investigation-agent]`** — décision d'accès tool-level basée sur l'historique complet

- **Standardized A2A Client (SDK)** :
  - Implémentation du **A2A protocol** (Agent-to-Agent, standard émergent référencé sur GitHub).
  - **Automatise** les échanges STS, la construction de l'actor chain, et la propagation cross-hop.
  - Doctrine d'adoption : ***« the secure path is also the easiest path for developers to implement A2A calls »*** — sécurité-par-défaut.
  - Code montré : classe `BaseAgentProtocolClient` avec méthodes async (authentication context building + agent calling).
  - Migration phasée des agents legacy via refactoring.

- **Standards externes alignés (à connaître)** :
  | Standard | Rôle |
  |----------|------|
  | **SPIFFE / SPIRE** | Framework d'identité workload — projet **CNCF graduated** |
  | **OAuth 2.0 Token Exchange (RFC 8693)** | Base conceptuelle du per-hop token exchange |
  | **IETF WIMSE working group** | Workload Identity in Multi-System Environments — drafts pour identité agent |
  | **draft-klrc-aiagent-auth-01** | Draft IETF *« AI Agent Authentication and Authorization »* |
  | **A2A Protocol** | Agent-to-Agent standard (référence GitHub) |

- **Métriques production (à retenir)** :
  - ***« P99 latency for the STS Token Exchange API is consistently below 40 milliseconds »***
  - **Milliers d'agents internes** adoptés
  - Dashboard d'observabilité temps réel traçant les sessions multi-agents
  - Spikes occasionnels mais consistent <40ms en P99

- **Features sécurité dérivées** :
  - **Per-hop token exchange** — tokens valides uniquement pour une destination spécifique
  - **Actor chain preservation** — visibilité complète du lignage à travers tous les systèmes
  - **Policy enforcement tool-level** — décisions basées sur l'historique complet de la requête
  - **Data redaction via AI Guard** — informations sensibles filtrées au passage par l'AI Gateway

- **Vision long terme — Three-Layer Framework** (architecture cible) :
  1. **Identity & Trust Foundation** — identité agent vérifiable + delegation chains
  2. **Dynamic Access Control** — permissions context-based + human-in-the-loop options + workflow authorization
  3. **Unified Enforcement Plane** — décisions de politique + observabilité + audit + governance unifiés

  ***« Long-term vision is a cohesive architecture where identity, risk, and policy work together seamlessly. »***

- **Pourquoi cet article est important (positionnement)** :
  - **Première publication de référence d'un hyperscaler non-AI-lab** (Uber = logistique/mobilité) qui industrialise la sécurité agent au niveau infrastructure.
  - **Comble le gap doctrinal** entre les frameworks de skills/harness (Vincent *Superpowers*, Lattice, PROJ-AI, Wescale Usine Logicielle Augmentée) qui parlent de productivité, et les **questions d'identité enterprise grade** qui n'avaient pas de doctrine publique.
  - **Aligne sur les standards émergents** (SPIFFE/SPIRE déjà adopté, IETF WIMSE en cours) plutôt que d'inventer un protocole propriétaire — pattern *cathedral and bazaar* classique d'Uber Eng.
  - **Devient une référence pour les RSSI / CISO** confrontés au déploiement d'agents en interne.

- **Articulation dossier veille** :
  - **Famille immédiate (infrastructure agent enterprise)** :
    - **Stripe Minions (Gray 2026-02-09 et 2026-02-19)** — fiche [gray-stripe-minions-coding-agents-part1-2026-02-09] et [gray-stripe-minions-coding-agents-part2-2026-02-19] : 1000-1300+ PRs/semaine autonomes, **Toolshed ~500 MCP tools**, devboxes isolés. Stripe et Uber convergent sur l'**industrialisation des agents internes** — Stripe focus sur les coding agents et le toolshed MCP, Uber focus sur l'**identity layer** qui rend ces déploiements gouvernables.
    - **Levie *Building for trillions of agents*** (fiche [levie-building-trillions-agents-software-2026-03-07]) — Aaron Levie (Box) : *« logiciel API-first pour agents, infrastructure agentique, modèles économiques »*. Levie prédit ; Uber **livre**.
    - **Thoughtworks AI/works™** (fiche [thoughtworks-aiworks-agentic-development-platform-2026-05-12]) — Control Plane avec *« active guardrails + end-to-end lineage »*. Uber est l'**implémentation production** de ce que Thoughtworks vend comme produit.
  - **Famille MCP / outils** :
    - **Anthropic 2026 Agentic Coding Trends Report** (fiche [anthropic-agentic-coding-trends-report-2026-02]) — démocratisation et supervision.
    - **Cloudflare Markdown for Agents** (fiche [martinho-allen-cloudflare-markdown-for-agents-2026-02-12]) — conversion HTML→Markdown en edge. Cloudflare et Uber adressent deux dimensions distinctes de l'infra agent : data shape (Cloudflare) vs identity (Uber).
  - **Famille harness / agent architecture** :
    - **Trivedy *Anatomy of an Agent Harness*** (fiche [trivedy-langchain-anatomy-agent-harness-2026-03-10]) — Agent=Modèle+Harnais. Uber complète : Harnais inclut désormais une **identity layer dédiée**, hop-aware.
    - **Osmani *Agent Harness Engineering*** (fiche [osmani-agent-harness-engineering-2026-04-19]) — Uber est un exemple opérationnel de ce que Osmani théorise.
    - **Seale *Semantic Agent: (Model+Harness) + (Ontology+Data)*** (fiche [seale-semantic-agent-model-harness-ontology-data-2026-04-17]) — Uber ajoute une troisième dimension : *(Identity + Provenance)*.
  - **Famille zero trust / sécurité plateforme** :
    - **Sierra AI-native interview** (fiches [sierra-ai-native-interview-iyengar-asemanfar-wang-2026-04-22] et [taylor-sierra-ai-native-interview-engineering-hiring-2026-04-20]) — recrute pour les forces. Profil ingénieur Uber visé : Plan/Build/Review avec compétence sécurité agent.
  - **Famille souveraineté / défense / risque** :
    - **Mensch / Mistral devant commission Assemblée nationale** (fiche [mensch-mistral-commission-enquete-vulnerabilites-numeriques-souverainete-ia-2026-05-13]) — *« sécurité économique »* + *« cyber : capacités offensives linéaires »*. Uber montre **comment** sécuriser opérationnellement ; Mensch montre **pourquoi** c'est stratégique pour la souveraineté.
    - **AISI UK GPT-5.5 cyber capabilities** (fiche [aisi-uk-gpt55-cyber-capabilities-evaluation-2026-04-30]) — modèles capables de découvrir vulnérabilités. La défense passe par des architectures comme celle d'Uber.
    - **Sun *Permanent Underclass*** (fiche [sun-nyt-silicon-valley-permanent-underclass-2026-04-30]) — déplacement travail → capital. Uber illustre la couche d'infrastructure *« capital »* qui rend possible l'automatisation à l'échelle.

- **Points faibles / questions ouvertes** :
  - **Pas de détails sur le coût** de l'architecture (combien de serveurs STS, combien de QPS, combien d'auteurs JWT/jour).
  - **Pas de chiffres sur les pertes de productivité développeurs** dues à la migration des agents legacy (combien de PRs de refactoring ? quelle durée totale ?).
  - **Position vs. solutions vendor** (Auth0, Okta, ForgeRock) non discutée — Uber a choisi de construire en interne sur SPIRE plutôt que d'acheter, mais sans expliciter le raisonnement build-vs-buy.
  - **Pas de discussion sur les failure modes** — que se passe-t-il si le STS est en panne ? Quel mode dégradé ? Quel circuit breaker ?
  - **Privacy / GDPR / données personnelles** dans l'actor chain — pas évoqué (un on-call engineer peut être nommément traçable dans tous les hops).
  - **Pas de discussion** sur les attaques par confusion de delegation chain ou par injection d'un faux maillon.
  - **L'A2A protocol** est cité comme dépendance externe — mais le draft IETF n'est pas encore un standard. Risque : adoption précoce sur un protocole qui peut évoluer.

- **Vocabulaire uber-eng à retenir** : *agency (définition Uber)*, *single-hop short-lived tokens*, *actor chain*, *agent registry*, *AI agent mesh*, *secure path = easiest path*, *per-hop token exchange*, *provenance preservation*, *MCP gateway as policy enforcement point*, *AI gateway as redaction layer*, *three-layer framework (identity / access / enforcement)*.

- **À mobiliser pour** :
  - Présentations dirigeants CISO/RSSI sur la sécurité des agents en entreprise (référence canonique).
  - Doctrine d'architecture pour les clients industriels qui déploient des agents internes (≥ 100 agents en flotte).
  - Comparaison build-vs-buy pour solutions IAM agentiques.
  - Argumentaire en faveur de SPIFFE/SPIRE comme **standard de facto** pour l'identité workload (CNCF graduated + adopté par Uber).
  - Référence dans tout document de plan plateforme agent enterprise (control plane, identity layer, observability).
  - Convergence avec la doctrine **Usine Logicielle Augmentée** Wescale et **AI/works™** Thoughtworks sur la nécessité d'un *« control plane »* mature.

## RésuméDe400mots

Six ingénieurs d'**Uber** (Matt Mathew et al.) publient le 21 mai 2026 sur le blog Uber Engineering un article exposant l'architecture d'**identité et de contrôle d'accès pour agents IA** déployée en production chez Uber pour des **milliers d'agents internes**. **Thèse-pivot** : ***« an agent is best defined as an entity that is authorized to act for or in the place of another »***, ce qui rend caduc le modèle d'identité classique humain+workload.

**Deux problèmes nommés** : (1) ***« Current Identity Model Doesn't Describe Agency »*** — la délégation est le mode par défaut, les workflows sont compositionnels, le comportement dynamique ; (2) ***« Original Provenance Isn't Effectively Carried Forward Across Agents to Systems »*** — *« Execution context is dropped across agent hops »* — créant des trous d'audit et empêchant l'application cohérente des politiques d'accès fine-grained.

**Architecture** comme extension de la Zero Trust Architecture Uber : **Agent Registry** (source of truth agent↔workload) + **AI Agent Mesh** (data plane inter-agents) + **STS (Security Token Service)** (émission JWT courts scopés) + **MCP Gateway** (policy enforcement pour tools) + **AI Gateway** (médiation LLM + redaction via AI Guard) + **SPIRE** (provider credentials workload).

**Mécanique** : workloads récupèrent des **SPIFFE Verifiable IDs (SVIDs)** cryptographiquement signés depuis SPIRE → SDK demande JWT au STS → STS vérifie l'autorisation contre Agent Registry → **token court (TTL en minutes) émis pour destination single-hop spécifique** (claim `Audience`). **Doctrine canonique** : ***« Single-hop, short-lived tokens. Every JWT minted by the STS is intended for a single hop, with a specific Audience claim and a short time-to-live in the order of minutes. »***

**Walkthrough multi-hop** : un on-call engineer `user1` → Oncall Agent → Investigation Agent → MCP Gateway. Le JWT final transporte l'**actor chain `[user1, oncall-agent, investigation-agent]`** vérifiable — décisions d'accès tool-level basées sur **l'historique complet** de la requête.

**Standardisation** : un **Standardized A2A (Agent-to-Agent) Client** SDK automatise les échanges STS et la propagation de l'actor chain — ***« the secure path is also the easiest path for developers to implement A2A calls »***. Migration phasée des agents legacy.

**Métriques production** : ***« P99 latency for the STS Token Exchange API is consistently below 40 milliseconds »***, milliers d'agents internes adoptés, observabilité temps réel.

**Vision long terme — three-layer framework** : (1) Identity & Trust Foundation, (2) Dynamic Access Control, (3) Unified Enforcement Plane.

**Standards externes** : SPIFFE/SPIRE (CNCF graduated), OAuth 2.0 Token Exchange (RFC 8693), IETF WIMSE working group, draft `draft-klrc-aiagent-auth-01`, A2A protocol.

**Importance** : première publication de référence d'un hyperscaler non-AI-lab qui industrialise la **sécurité agent au niveau infrastructure**, comblant le gap doctrinal entre les frameworks de skills/harness (productivité) et les questions d'**identité enterprise grade** (gouvernabilité). Devient une référence canonique pour les architectes plateforme, security engineers, et CISO confrontés au déploiement d'agents en interne.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Uber | ORGANISATION | a_déployé | architecture identité agent IA | TECHNOLOGIE | 0.98 | DYNAMIQUE | déclaré_article |
| Matt Mathew | PERSONNE | est_Sr_Staff_Engineer_chez | Uber | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Prasad Borole | PERSONNE | est_Staff_Software_Engineer_chez | Uber | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Meng Huang | PERSONNE | est_Engineering_Manager_chez | Uber | ORGANISATION | 0.98 | DYNAMIQUE | déclaré_article |
| Uber | ORGANISATION | définit_agent_comme | entité autorisée à agir pour ou à la place d'un autre | CONCEPT | 0.99 | ATEMPOREL | déclaré_article |
| modèle d'identité classique | CONCEPT | ne_décrit_pas | l'agency | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| workflows agentiques | CONCEPT | sont | compositionnels (agents appellent agents et tools) | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| comportement agentique | CONCEPT | est | dynamique (plans évoluent selon résultats intermédiaires) | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| contexte d'exécution | CONCEPT | est_perdu_à_travers | les hops d'agents | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| perte de provenance | CONCEPT | empêche | application cohérente de politiques fine-grained | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| architecture Uber | TECHNOLOGIE | étend | Zero Trust Architecture | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Agent Registry | TECHNOLOGIE | est | source of truth pour mappings agent↔workload | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| AI Agent Mesh | TECHNOLOGIE | est | data plane pour communication inter-agents | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| STS (Security Token Service) | TECHNOLOGIE | émet | JWT short-lived scopés single-hop | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| MCP Gateway | TECHNOLOGIE | est | policy enforcement point pour invocation outils | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| AI Gateway | TECHNOLOGIE | médiation | appels LLM externes avec guardrails | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| AI Gateway | TECHNOLOGIE | inclut | AI Guard pour data redaction | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| SPIRE | TECHNOLOGIE | fournit | workload credentials signés | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| SPIFFE | TECHNOLOGIE | définit | Verifiable IDs (SVIDs) | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| workloads Uber | TECHNOLOGIE | récupèrent | SVIDs depuis SPIRE | CONCEPT | 0.97 | DYNAMIQUE | déclaré_article |
| SDK Uber | TECHNOLOGIE | demande_JWT_à | STS | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| STS | TECHNOLOGIE | vérifie_autorisation_contre | Agent Registry | TECHNOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| JWT Uber | TECHNOLOGIE | est_émis_pour | destination single-hop spécifique | CONCEPT | 0.98 | ATEMPOREL | déclaré_article |
| JWT Uber | TECHNOLOGIE | a_TTL | minutes (short-lived) | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| JWT Uber | TECHNOLOGIE | contient | actor chain vérifiable | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| actor chain | CONCEPT | permet | décisions accès tool-level basées sur historique requête | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Standardized A2A Client | TECHNOLOGIE | automatise | échanges STS et propagation actor chain | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Standardized A2A Client | TECHNOLOGIE | implémente | A2A protocol | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Uber | ORGANISATION | recommande | secure path = easiest path | METHODOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| architecture Uber | TECHNOLOGIE | est_basée_sur | OAuth 2.0 Token Exchange (RFC 8693) | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Uber | ORGANISATION | aligne_sur | IETF WIMSE working group drafts | EVENEMENT | 0.96 | DYNAMIQUE | déclaré_article |
| draft-klrc-aiagent-auth-01 | EVENEMENT | spécifie | AI Agent Authentication and Authorization | CONCEPT | 0.94 | DYNAMIQUE | déclaré_article |
| STS Token Exchange API | TECHNOLOGIE | a_P99_latency | <40 millisecondes | CONCEPT | 0.98 | DYNAMIQUE | déclaré_article |
| Uber | ORGANISATION | exploite | milliers d'agents internes adoptés | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Uber | ORGANISATION | dispose_de | dashboard observabilité temps réel sessions multi-agents | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Uber | ORGANISATION | prédit | three-layer framework (identity, access, enforcement) | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Uber | ORGANISATION | migre | agents legacy via refactoring phasé | METHODOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| SPIFFE/SPIRE | TECHNOLOGIE | est_graduated_à | CNCF | ORGANISATION | 0.97 | STATIQUE | inféré |
| article Uber | EVENEMENT | est | première publication référence hyperscaler non-AI-lab sur identity agent | CONCEPT | 0.93 | STATIQUE | inféré |
| identity layer Uber | CONCEPT | comble | gap entre frameworks skills/harness et identity enterprise | CONCEPT | 0.92 | ATEMPOREL | inféré |
| Uber on-call engineer | PERSONNE | initie_session_avec | Oncall Agent | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Oncall Agent | TECHNOLOGIE | appelle | Investigation Agent | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Investigation Agent | TECHNOLOGIE | appelle | MCP Gateway | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| MCP Gateway | TECHNOLOGIE | reçoit | actor chain [user1, oncall-agent, investigation-agent] | CONCEPT | 0.97 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Uber Engineering | ORGANISATION | catégorie | Équipe d'ingénierie Uber, publie blog technique sur uber.com/blog, déploie infrastructure agent identity en production pour milliers d'agents internes | AJOUT |
| Matt Mathew | PERSONNE | rôle | Sr Staff Engineer chez Uber, co-auteur principal de l'article *Solving the Identity Crisis for AI Agents* (2026-05-21) | AJOUT |
| Prasad Borole | PERSONNE | rôle | Staff Software Engineer chez Uber, co-auteur | AJOUT |
| Meng Huang | PERSONNE | rôle | Engineering Manager chez Uber, responsable équipe Security/Identity infrastructure agent | AJOUT |
| Sergey Burykin | PERSONNE | rôle | Sr Software Engineer chez Uber, co-auteur | AJOUT |
| Gaurav Goel | PERSONNE | rôle | Software Engineer II chez Uber, co-auteur | AJOUT |
| Bayard Walsh | PERSONNE | rôle | Software Engineer I chez Uber, co-auteur | AJOUT |
| agency (définition Uber) | CONCEPT | définition | *« An entity that is authorized to act for or in the place of another »* — définition fondatrice qui pose la délégation comme propriété axiomatique de l'agent IA | AJOUT |
| Agent Registry | TECHNOLOGIE | catégorie | Source of truth Uber pour les mappings agent↔workload — utilisé par STS pour vérifier l'autorisation des agents | AJOUT |
| AI Agent Mesh | TECHNOLOGIE | catégorie | Data plane Uber pour la communication inter-agents — couche réseau cohérente pour l'orchestration agentique | AJOUT |
| STS (Security Token Service) | TECHNOLOGIE | catégorie | Service Uber d'émission de JWT short-lived, audience-scoped, single-hop — TTL en minutes, P99 latency <40ms | AJOUT |
| MCP Gateway | TECHNOLOGIE | catégorie | Policy enforcement point Uber pour l'invocation des MCP tools — décisions d'accès tool-level basées sur l'actor chain complète | AJOUT |
| AI Gateway | TECHNOLOGIE | catégorie | Médiateur Uber des appels LLM externes avec guardrails de sécurité — inclut AI Guard pour la redaction de données sensibles | AJOUT |
| SPIRE | TECHNOLOGIE | catégorie | Provider de credentials workload (CNCF graduated), implémentation de référence du standard SPIFFE — utilisé par Uber pour émettre des SVIDs aux workloads | AJOUT |
| SPIFFE Verifiable IDs (SVID) | TECHNOLOGIE | catégorie | Identités workload cryptographiquement signées définies par le standard SPIFFE, récupérées depuis SPIRE et utilisées comme base pour les JWT STS | AJOUT |
| Standardized A2A Client | TECHNOLOGIE | catégorie | SDK Uber implémentant l'A2A protocol, automatise les échanges STS et la propagation de l'actor chain — pattern *secure path = easiest path* | AJOUT |
| A2A Protocol | TECHNOLOGIE | catégorie | Agent-to-Agent standard émergent (référencé sur GitHub) pour les communications inter-agents | AJOUT |
| actor chain | CONCEPT | définition | Liste vérifiable de tous les participants à une requête multi-hop (user + agents intermédiaires) transportée dans le JWT — permet des décisions d'accès tool-level basées sur l'historique complet | AJOUT |
| single-hop short-lived tokens | METHODOLOGIE | définition | Doctrine canonique Uber : *« Every JWT minted by the STS is intended for a single hop, with a specific Audience claim and a short time-to-live in the order of minutes »* — blast radius minimal en cas de vol | AJOUT |
| OAuth 2.0 Token Exchange (RFC 8693) | TECHNOLOGIE | catégorie | Standard IETF pour l'échange de tokens entre services — base conceptuelle du per-hop token exchange Uber | AJOUT |
| IETF WIMSE working group | EVENEMENT | catégorie | Workload Identity in Multi-System Environments — groupe de travail IETF émergent sur l'identité workload et agent | AJOUT |
| draft-klrc-aiagent-auth-01 | EVENEMENT | catégorie | Draft IETF *AI Agent Authentication and Authorization* — spécification émergente alignée par Uber | AJOUT |
| three-layer framework (Uber) | METHODOLOGIE | définition | Vision long terme Uber : (1) Identity & Trust Foundation, (2) Dynamic Access Control, (3) Unified Enforcement Plane — architecture cible cohérente identity + risk + policy | AJOUT |
| Zero Trust Architecture | METHODOLOGIE | catégorie | Doctrine sécurité Uber (et industrie) — chaque requête vérifiée indépendamment, pas de confiance implicite — étendue par l'architecture agent identity | AJOUT |
| AI Guard | TECHNOLOGIE | catégorie | Composant Uber au sein de l'AI Gateway pour la redaction des données sensibles avant envoi aux LLM externes | AJOUT |
