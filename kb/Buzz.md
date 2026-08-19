# Buzz

> **Type** : TECHNOLOGIE | 35 relations | 7 fiches sources

## Attributs

- **architecture** : Relais Nostr écrit en Rust (Axum WS + REST) sous Apache 2.0, avec Postgres pour les événements et la recherche plein texte, Redis pour pub/sub, présence et saisie, stockage objet S3/MinIO pour les médias via Blossom, client desktop Tauri + React ; 127 event kinds, NIP-01, NIP-42, NIP-98, NIP-34
- **code source** : Ouvert : code, spécifications de protocole, vecteurs de test, sections sécurité et modèles formels publiés sur github.com/block/buzz ; site buzz.xyz
- **confidentialité** : Télémétrie et annulation en messages éphémères chiffrés, mémoire et comptabilité de coûts chiffrées mais durables ; le serveur ne voit que des métadonnées de routage. L'inférence peut être routée vers la machine d'un pair autorisé, le trafic modèle chiffré circulant directement entre eux
- **décentralisation** : L'ARCHITECTURE.md pose le relais comme source unique de vérité, sans échange pair-à-pair, sans gossip ni réplication : un relais autoritaire par communauté, donc un point de défaillance unique. La décentralisation revendiquée est une souveraineté organisationnelle (auto-hébergement + identité portable), pas une redondance réseau
- **définition** : Espace de travail auto-hébergeable de Block (21 juillet 2026, Apache-2.0) bâti sur Nostr, où humains et agents partagent les mêmes canaux ; chaque participant est une paire de clés, chaque événement est signé dans un journal append-only
- **identité des agents** : Chaque agent reçoit sa propre paire de clés ; son propriétaire signe une autorisation étroitement délimitée et l'agent signe son travail en son propre nom — « authorization does not erase authorship ». Révocation d'un agent sans remplacement de l'identité humaine, déconnexion en cascade si le propriétaire est retiré
- **interopérabilité** : Claude Code, Codex, goose et tout agent parlant Agent Client Protocol peuvent y travailler ; changer de modèle ou de harness préserve l'identité, les permissions et l'historique du projet
- **limites de sécurité** : Autorisation à la maille du canal et non par outil ou action ; agents lancés en --dangerously-skip-permissions hors bac à sable ; pas d'observabilité de l'activité des agents ; journal signé tamper-evident mais non tamper-resistant ; messages non chiffrés de bout en bout sur le relais hébergé
- **maturité** : Version 0.4.21 ou 0.4.22 au lancement selon les sources, puis 0.5.x ; dépôt créé le 6 mars 2026, premières releases publiques le 3 mai 2026, lancement public le 21 juillet 2026. Environ 25 900 étoiles GitHub à la mi-août 2026. Binaires Windows non signés, docs éparses, UI de forge Git précoce ; aucun prix publié pour l'hébergement géré
- **positionnement** : Présenté aux actionnaires comme un système interne de collaboration d'agents, de communication et de dépôts de code destiné à réduire les délais de coordination — cadrage productivité, complémentaire du cadrage ouverture protocolaire (Apache-2.0, Nostr, ACP) documenté ailleurs dans ce corpus
- **rôle** : Destination déclarée des enseignements de Berd : l'espace partagé humains+agents
- **statut** : Workspace humains+agents sur Nostr, en bêta au 18 août 2026
- **stockage Git** : Dépôts stockés en packfiles immuables adressés par contenu sur stockage objet, plus un pointeur de manifeste mutable avancé par compare-and-swap conditionnel qui constitue le point de commit ; protocole spécifié en TLA+ et model-checké, avec suite de conformité obligatoire par backend
- **vérification formelle** : Spécification d'isolation multi-tenant mécanisée en TLA+, propriétés d'autorisation vérifiées en Tamarin, protocole de stockage Git model-checké — niveau de formalisme inhabituel pour une version 0.x, mais portant sur l'identité et le stockage, non sur l'autorisation d'outil
- **équipes d'agents** : Les agents s'appellent entre eux : un SmartBee délègue un sous-ensemble à un WorkerBee, attend, relit et renvoie, sans relais humain. Chaque agent a un nom, une persona, une mémoire et sa propre présence dans le canal — un siège plutôt qu'une session

## Relations (comme sujet)

### affine

- [[kb/_entites-mineures#forge-logicielle-souveraine\|forge logicielle souveraine]] (CONCEPT) — 0.84, DYNAMIQUE
  - [[fiches/2026-08/petersen-block-buzz-projects-forge-souveraine-2026-08-18\|Projects in Buzz]]

### affirme_que

- « l'autorisation n'efface pas la paternité : l'agent reste l'auteur, son credential prouve qui l'a autorisé et sous quelles conditions » (CITATION) — 0.96, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « la mise à jour du pointeur est le point de commit, les événements du workspace annonçant le changement sans le définir » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « une forge classique conserve le diff et une coche verte, là où Buzz conserve aussi pourquoi le correctif évident était faux » (CITATION) — 0.95, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

### concurrence

- Slack (TECHNOLOGIE) — 0.90, DYNAMIQUE
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- [[kb/GitHub-technologie\|GitHub]] (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]

### est_basé_sur

- [[kb/Berd\|Berd]] (TECHNOLOGIE) — 0.85, DYNAMIQUE
  - [[fiches/2026-08/block-berd-caractere-agents-open-source-2026-08-18\|Designing AI with character: what we learned building Berd]]

### est_instance_de

- workspace collaboratif humains-agents auto-hébergeable (CONCEPT) — 0.96, ATEMPOREL
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

### permet

- « à chaque agent d'avoir sa propre clé, son autorisation signée par son propriétaire et sa propre signature sur son travail » (AFFIRMATION) — 0.97, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « à des agents de se déléguer du travail entre eux et de s'escalader des questions sans qu'un humain relaie quoi que ce soit » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-08/patel-block-buzz-teams-tokens-benchmarks-2026-08-06\|Efficient Tokens & Effective Teams in Buzz]]
- « de brancher Goose, Claude Code et Codex par le même harnais » (AFFIRMATION) — 0.94, DYNAMIQUE
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- « une souveraineté organisationnelle par auto-hébergement et identité portable, et non une redondance réseau » (AFFIRMATION) — 0.94, ATEMPOREL
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
- « de changer de modèle ou de harness sans que le projet perde son identité, ses permissions ou son historique » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « de composer une équipe tri-fournisseurs : Claude Opus 5 en SmartBee, GPT-5.6 Terra en WorkerBee, un modèle local en QuickBee » (AFFIRMATION) — 0.93, DYNAMIQUE
  - [[fiches/2026-08/patel-block-buzz-teams-tokens-benchmarks-2026-08-06\|Efficient Tokens & Effective Teams in Buzz]]
- « à une identité et à un historique signé de rester vérifiables même si Buzz disparaît, un dépôt Git restant réhébergeable » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « de router les requêtes d'inférence d'un agent vers la machine d'un autre membre, le trafic chiffré circulant directement entre pairs autorisés » (AFFIRMATION) — 0.92, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « la collaboration entre agents, la communication et la gestion des dépôts de code, en réduisant les délais de coordination » (AFFIRMATION) — 0.90, DYNAMIQUE
  - [[fiches/2026-08/paymentsdive-block-dorsey-pricing-ia-2026-08-06\|Block explores how to price AI]]
- « un substrat multi-agent auto-hébergeable et auditable, sans dépendance SaaS tierce » (AFFIRMATION) — 0.90, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]

### réduit

- « la compression du contexte partagé dans des prompts privés, en gardant discussion, patchs, CI, revue et décision de merge dans un même canal » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

### s_applique_à

- « Claude Code, Codex et goose, ainsi qu'à tout agent parlant Agent Client Protocol » (AFFIRMATION) — 0.95, DYNAMIQUE
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « Claude Code, Codex, modèles ouverts et modèles locaux, avec leurs abonnements existants » (AFFIRMATION) — 0.94, DYNAMIQUE
  - [[fiches/2026-08/patel-block-buzz-teams-tokens-benchmarks-2026-08-06\|Efficient Tokens & Effective Teams in Buzz]]
- [[kb/_entites-mineures#travail-collaboratif-humains-agents\|travail collaboratif humains-agents]] (CONCEPT) — 0.94, ATEMPOREL
  - [[fiches/2026-08/block-berd-caractere-agents-open-source-2026-08-18\|Designing AI with character: what we learned building Berd]]

### s_oppose_à

- « la qualification de décentralisé au sens réseau : l'architecture officielle pose le relais comme source unique de vérité, sans échange pair-à-pair, sans gossip et sans réplication » (AFFIRMATION) — 0.96, ATEMPOREL
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
- « l'autorisation fine par outil : l'appartenance au canal reste l'unité de permission, un agent dans un canal pouvant faire ce que font les membres » (AFFIRMATION) — 0.95, DYNAMIQUE
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
- « l'observabilité de l'activité des agents : le workspace signale qu'un agent a reçu un message mais pas ce qu'il en fait, des agents ayant subi des kills OOM silencieux » (AFFIRMATION) — 0.92, DYNAMIQUE
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
- « un usage en production tant que l'autorisation fine par outil et l'observabilité des agents ne sont pas livrées » (AFFIRMATION) — 0.90, DYNAMIQUE
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]

### utilise

- [[kb/Nostr\|Nostr]] (TECHNOLOGIE) — 0.97, ATEMPOREL
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « des packfiles immuables adressés par contenu sur stockage objet, plus un pointeur de manifeste mutable avancé par compare-and-swap conditionnel » (AFFIRMATION) — 0.96, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- [[kb/Agent-Client-Protocol\|Agent Client Protocol]] (TECHNOLOGIE) — 0.95, DYNAMIQUE
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « un relais écrit en Rust avec Postgres pour les événements et la recherche, Redis pour la présence et le pub/sub, et un stockage objet S3 ou MinIO pour les médias » (AFFIRMATION) — 0.94, DYNAMIQUE
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
- [[kb/Model-Context-Protocol\|Model Context Protocol]] (TECHNOLOGIE) — 0.93, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- « un lancement en --dangerously-skip-permissions, hors bac à sable, sur la machine d'un humain » (AFFIRMATION) — 0.93, DYNAMIQUE
  - [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
- « une suite de conformité que chaque backend de stockage objet doit passer, le résultat borné dépendant de trois garanties explicites » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

## Relations (comme objet)

- [[kb/Buzz-Projects\|Buzz Projects]] **fait_partie_de** → Buzz — 0.98
- [[kb/Block\|Block]] **publie** → Buzz — 0.98

## Fiches sources

- [[fiches/2026-08/block-berd-caractere-agents-open-source-2026-08-18\|Designing AI with character: what we learned building Berd]]
- [[fiches/2026-08/buzz-block-panorama-deep-research-2026-08-12\|Buzz (buzz.xyz) — Rapport de recherche pour présentation]]
- [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- [[fiches/2026-08/patel-block-buzz-teams-tokens-benchmarks-2026-08-06\|Efficient Tokens & Effective Teams in Buzz]]
- [[fiches/2026-08/paymentsdive-block-dorsey-pricing-ia-2026-08-06\|Block explores how to price AI]]
- [[fiches/2026-08/petersen-block-buzz-projects-forge-souveraine-2026-08-18\|Projects in Buzz]]
