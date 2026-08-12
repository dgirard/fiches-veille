# Buzz

> **Type** : TECHNOLOGIE | 20 relations | 3 fiches sources

## Attributs

- **code source** : Ouvert : code, spécifications de protocole, vecteurs de test, sections sécurité et modèles formels publiés sur github.com/block/buzz ; site buzz.xyz
- **confidentialité** : Télémétrie et annulation en messages éphémères chiffrés, mémoire et comptabilité de coûts chiffrées mais durables ; le serveur ne voit que des métadonnées de routage. L'inférence peut être routée vers la machine d'un pair autorisé, le trafic modèle chiffré circulant directement entre eux
- **définition** : Espace de travail auto-hébergeable de Block (21 juillet 2026, Apache-2.0) bâti sur Nostr, où humains et agents partagent les mêmes canaux ; chaque participant est une paire de clés, chaque événement est signé dans un journal append-only
- **identité des agents** : Chaque agent reçoit sa propre paire de clés ; son propriétaire signe une autorisation étroitement délimitée et l'agent signe son travail en son propre nom — « authorization does not erase authorship ». Révocation d'un agent sans remplacement de l'identité humaine, déconnexion en cascade si le propriétaire est retiré
- **interopérabilité** : Claude Code, Codex, goose et tout agent parlant Agent Client Protocol peuvent y travailler ; changer de modèle ou de harness préserve l'identité, les permissions et l'historique du projet
- **positionnement** : Présenté aux actionnaires comme un système interne de collaboration d'agents, de communication et de dépôts de code destiné à réduire les délais de coordination — cadrage productivité, complémentaire du cadrage ouverture protocolaire (Apache-2.0, Nostr, ACP) documenté ailleurs dans ce corpus
- **stockage Git** : Dépôts stockés en packfiles immuables adressés par contenu sur stockage objet, plus un pointeur de manifeste mutable avancé par compare-and-swap conditionnel qui constitue le point de commit ; protocole spécifié en TLA+ et model-checké, avec suite de conformité obligatoire par backend

## Relations (comme sujet)

### affirme_que

- « l'autorisation n'efface pas la paternité : l'agent reste l'auteur, son credential prouve qui l'a autorisé et sous quelles conditions » (CITATION) — 0.96, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « la mise à jour du pointeur est le point de commit, les événements du workspace annonçant le changement sans le définir » (AFFIRMATION) — 0.95, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « une forge classique conserve le diff et une coche verte, là où Buzz conserve aussi pourquoi le correctif évident était faux » (CITATION) — 0.95, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

### concurrence

- [[kb/_entites-mineures#Slack\|Slack]] (TECHNOLOGIE) — 0.82, DYNAMIQUE
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

### est_instance_de

- [[kb/_entites-mineures#workspace-collaboratif-humains-agents-auto-hébergeable\|workspace collaboratif humains-agents auto-hébergeable]] (CONCEPT) — 0.95, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

### permet

- « à chaque agent d'avoir sa propre clé, son autorisation signée par son propriétaire et sa propre signature sur son travail » (AFFIRMATION) — 0.97, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « de brancher Goose, Claude Code et Codex par le même harnais » (AFFIRMATION) — 0.94, DYNAMIQUE
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- « de changer de modèle ou de harness sans que le projet perde son identité, ses permissions ou son historique » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
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

### utilise

- [[kb/_entites-mineures#Nostr\|Nostr]] (TECHNOLOGIE) — 0.97, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- « des packfiles immuables adressés par contenu sur stockage objet, plus un pointeur de manifeste mutable avancé par compare-and-swap conditionnel » (AFFIRMATION) — 0.96, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- [[kb/Agent-Client-Protocol\|Agent Client Protocol]] (TECHNOLOGIE) — 0.95, DYNAMIQUE
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- [[kb/Model-Context-Protocol\|Model Context Protocol]] (TECHNOLOGIE) — 0.93, ATEMPOREL
  - [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- « une suite de conformité que chaque backend de stockage objet doit passer, le résultat borné dépendant de trois garanties explicites » (AFFIRMATION) — 0.93, ATEMPOREL
  - [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]

## Relations (comme objet)

- [[kb/Block\|Block]] **publie** → Buzz — 0.98

## Fiches sources

- [[fiches/2026-08/girard-acp-deux-protocoles-un-sigle-2026-08-02\|ACP : deux protocoles, un sigle, zéro rapport]]
- [[fiches/2026-07/longwell-block-buzz-workspace-agents-nostr-2026-07-21\|Buzz!]]
- [[fiches/2026-08/paymentsdive-block-dorsey-pricing-ia-2026-08-06\|Block explores how to price AI]]
