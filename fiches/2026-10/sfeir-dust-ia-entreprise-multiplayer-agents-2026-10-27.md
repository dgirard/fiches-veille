---
themes: [produits-services, transformation-adoption, economie-marche]
source: SFEIR
---
# sfeir-dust-ia-entreprise-multiplayer-agents-2026-10-27

## Veille

Article **SFEIR AI** publié sur sfeir.com le **27 octobre 2026** (~13 000 signes, 19 sources notées : communiqué, billets Dust, The Next Web, French Tech Journal, Seedcamp, Wayback Machine). Portrait de **Dust**, société parisienne fondée en février 2023 par **Gabriel Hubert** (CEO) et **Stanislas Polu** (CTO, ex-OpenAI), qui a annoncé le **18 mai 2026** une Série B de **40 M$** (Abstract, **Sequoia**), pour plus de **60 M$** levés et plus de **3 000** organisations clientes revendiquées. Trois apports. **(A)** La thèse « **multiplayer** » : *« Most AI at work is still single-player »* — la valeur est dans des agents partagés ; brique technique : les **Skills** (janvier 2026) puis les *self-improving skills* (juillet), qui proposent des corrections d'instructions sans toucher aux poids. **(B)** Le tri entre vérifié et déclaratif : financements documentés, indicateurs d'usage revendiqués (300 000 agents, rétention nette 240 %), **Dust Index** du 7 octobre (65 % des messages vers des agents partagés). **(C)** Les limites : marché encombré, dépôt `dust-tt/dust` sous MIT en mai qui ne répond plus publiquement en octobre, SaaS sans auto-hébergement, aucune qualification SecNumCloud. SFEIR déclare son partenariat avec Google Cloud et Anthropic. Rejoint les fiches du corpus sur l'adoption collective des agents en entreprise.

## Titre Article

Dust ou l'IA d'entreprise qui se joue à plusieurs : ce que les DSI doivent en retenir

## Date

2026-10-27

## URL

https://www.sfeir.com/articles/dust-ia-entreprise-multiplayer-agents-dsi/

## Keywords

Dust, IA d'entreprise, agents partagés, multiplayer AI, single-player, Skills, self-improving skills, context engineering, AI Operators, Gabriel Hubert, Stanislas Polu, Série B, Sequoia, connecteurs MCP, tarification par crédits, Dust Index, Persona, Doctolib, Qonto, Mirakl, Spendesk, Mantu, réversibilité des modèles, SaaS, souveraineté, SecNumCloud, gouvernance des agents, coût par résultat, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Portrait d'entreprise à visée de conseil, registre d'enquête documentaire. L'article sépare explicitement « le vérifié et le déclaratif » et attribue chaque chiffre à sa source, en signalant les incohérences de la page tarifaire et l'écart entre le code présenté comme public et son état au 27 octobre. Il restitue la thèse des fondateurs en citations, rapporte la réserve de The Next Web (le discours multiplayer relève « autant du positionnement que du produit »), et situe Dust dans un marché concurrentiel. La position de SFEIR est déclarée (partenaire de Google Cloud et d'Anthropic) avant ses recommandations, formulées pour s'appliquer « que la DSI choisisse Dust ou non ». Public : DSI, directions métier, responsables de la transformation.

## Pense-betes

- **Dust** : immatriculée à Paris en **février 2023** ; **Gabriel Hubert** (CEO, ex-Stripe, ex-CPO d'Alan) et **Stanislas Polu** (CTO, ex-Stripe, ex-OpenAI, équipe Greg Brockman). Cofondateurs de Totems (racheté par Stripe en 2014).
- Financement : seed **5 M€** (Sequoia, 2023), Série A **16 M$** (2024, 1 M$ d'ARR), Série B **40 M$** (mai 2026, Abstract + Sequoia, avec Snowflake Ventures et Datadog). Valorisation et CA non publiés.
- Produit : agents sans code connectés aux outils (100+ sources selon le communiqué, 70+ connecteurs MCP selon la page produit) ; **20+ modèles** au choix par agent (OpenAI, Anthropic, Google, Mistral, DeepSeek) ; SOC 2 Type II, RGPD, hébergement UE ou US.
- Tarif par **crédits** depuis le 23 juin 2026 : sièges Free / Pro (30/mois) / Max (150/mois) ; Enterprise ajoute SCIM, audit, single-tenant.
- **Multiplayer** : le goulot passe de la génération à la coordination. **Skills** (26 janv. 2026) = instructions + connaissances + outils partagés ; **self-improving skills** (7 juil.) = propositions de correction validées par le responsable, poids inchangés.
- « **AI Operators** » : profils Ops, Support, Marketing, Sales qui construisent les agents de leurs équipes.
- Déclaratif : 300 000+ agents, adoption mensuelle > 90 %, rétention nette **240 %** en 2025 ; The Next Web : 41 000 MAU en avril 2026.
- Cas : Persona (11 départements, 300+ agents), Doctolib (3 000 salariés), Qonto (≥ 50 000 h/an), Mirakl (30 % de créateurs), Spendesk (90 % d'adoption en six mois).
- **Dust Index** (7 oct.) : 65 % des messages vers des agents utilisés par plusieurs personnes ; 1,8 % des agents (≥ 50 utilisateurs) = 43,3 % des messages.
- Code : `dust-tt/dust` MIT (1 364 étoiles) en mai ; ne répond plus publiquement en octobre. Alternatives auto-hébergées : Onyx, Dify, Flowise, AnythingLLM.
- Recommandations SFEIR : relais par équipe ; publication d'agent = acte de gouvernance (cas 1Password) ; réversibilité des modèles par contrat ; mesurer le coût à l'unité de travail ; démarrer par 2-3 processus transverses, mesure à 30 et 90 jours.

## RésuméDe400mots

Cet article de SFEIR, publié le 27 octobre 2026, dresse le portrait de Dust, plateforme française d'agents d'entreprise, et en tire des leçons pour les DSI. Le 18 mai 2026, Dust a annoncé une Série B de quarante millions de dollars co-menée par Abstract et Sequoia, portant le total levé au-delà de soixante millions, et revendique plus de trois mille organisations clientes.

La société a été immatriculée à Paris en février 2023 par Gabriel Hubert et Stanislas Polu, rencontrés à Stanford, cofondateurs d'une société rachetée par Stripe, puis passés respectivement par l'assureur Alan et par OpenAI. Leur conviction : les modèles sont capables de transformer l'économie mais restent sous-déployés faute de couche produit.

Dust permet aux équipes métier de construire sans code des agents connectés aux connaissances et aux outils de l'entreprise, en choisissant le modèle agent par agent parmi une vingtaine de fournisseurs. La plateforme est passée en juin 2026 à une tarification par crédits. Sa thèse est celle d'une IA « multiplayer » : l'usage individuel enferme les gains, alors que des agents partagés font passer le goulot de la génération à la coordination. Les Skills, lancées en janvier 2026, mutualisent instructions, connaissances et outils entre agents ; depuis juillet, la plateforme propose des corrections de skills à partir des erreurs récurrentes, que le responsable accepte ou rejette, sans modifier les poids du modèle.

L'article distingue le vérifié du déclaratif. Les levées de fonds sont documentées ; les indicateurs d'usage (trois cent mille agents, rétention nette de 240 %) sont des revendications. Les études de cas de Persona, Doctolib, Qonto, Mirakl et Spendesk illustrent l'adoption, et le premier Dust Index indique que 65 % des messages vont à des agents utilisés par plusieurs personnes.

Dust évolue dans un marché encombré, face aux offres entreprise des éditeurs de modèles, aux agents intégrés des suites bureautiques et à d'autres plateformes. Son dépôt de code, présenté comme public sous licence MIT en mai, ne répond plus publiquement en octobre ; le produit est un SaaS sans auto-hébergement, et aucune qualification SecNumCloud n'est annoncée, les appels d'inférence passant majoritairement par des fournisseurs américains.

SFEIR, qui se déclare partenaire de Google Cloud et d'Anthropic, retient quatre leçons : le facteur limitant est organisationnel et passe par des relais dans chaque équipe ; publier un agent partagé est un acte de gouvernance ; la réversibilité des modèles doit être contractuelle ; le coût se mesure à l'unité de travail. L'article recommande de commencer par deux ou trois processus transverses et de mesurer à trente puis quatre-vingt-dix jours.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Dust ou l'IA d'entreprise qui se joue à plusieurs : ce que les DSI doivent en retenir | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Gabriel Hubert | PERSONNE | dirige | Dust | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Stanislas Polu | PERSONNE | travaille_chez | Dust | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Gabriel Hubert | PERSONNE | a_créé | Dust | ORGANISATION | 0.93 | STATIQUE | déclaré_article |
| Sequoia | ORGANISATION | collabore_avec | Dust | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| Dust | ORGANISATION | mesure | Série B de 40 M$ (mai 2026), plus de 60 M$ levés au total | MESURE | 0.93 | STATIQUE | déclaré_article |
| Dust | ORGANISATION | affirme_que | l'IA en entreprise reste single-player et la valeur est dans des agents partagés entre équipes | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| Dust | ORGANISATION | a_créé | Dust Skills | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Dust Skills | TECHNOLOGIE | permet | mutualisation d'instructions, connaissances et outils entre agents | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| Dust Skills | TECHNOLOGIE | s_applique_à | context engineering | METHODOLOGIE | 0.8 | ATEMPOREL | inféré |
| Dust | ORGANISATION | utilise | MCP | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| Dust | ORGANISATION | publie | Dust Index | DOCUMENT | 0.9 | STATIQUE | déclaré_article |
| Dust Index | DOCUMENT | mesure | 65 % des messages envoyés à des agents utilisés par plus d'une personne | MESURE | 0.88 | STATIQUE | déclaré_article |
| Dust | ORGANISATION | mesure | 300 000 agents déployés et rétention nette de 240 % en 2025 (déclaratif) | MESURE | 0.78 | STATIQUE | déclaré_article |
| Dust | ORGANISATION | concurrence | Microsoft 365 Copilot | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| Dust | ORGANISATION | concurrence | Glean | ORGANISATION | 0.8 | DYNAMIQUE | déclaré_article |
| Mantu | ORGANISATION | collabore_avec | Dust | ORGANISATION | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | le facteur limitant de l'adoption des agents partagés est organisationnel | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | traiter la publication d'un agent partagé comme un acte de gouvernance (propriétaire, maintenance, tests) | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | exiger contractuellement la réversibilité des modèles et mesurer le coût à l'unité de travail | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle ; partenaire Google Cloud et Anthropic | AJOUT |
| Dust | ORGANISATION | profil | Plateforme française d'agents d'entreprise (Paris, 2023), 3 000+ clients revendiqués | AJOUT |
| Gabriel Hubert | PERSONNE | rôle | CEO et cofondateur de Dust | AJOUT |
| Stanislas Polu | PERSONNE | rôle | CTO et cofondateur de Dust, ex-OpenAI | AJOUT |
| Dust Skills | TECHNOLOGIE | définition | Paquets réutilisables d'instructions, connaissances et outils ; auto-amélioration proposée depuis juillet 2026 | AJOUT |
| Dust Index | DOCUMENT | date | Premier index d'usage publié le 7 octobre 2026 | AJOUT |
| multiplayer AI | CONCEPT | définition | Agents partagés entre humains et équipes plutôt qu'assistants individuels | AJOUT |
