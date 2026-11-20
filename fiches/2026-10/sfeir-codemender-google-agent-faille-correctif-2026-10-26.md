---
themes: [qualite-securite, outils-plateformes]
source: SFEIR
---
# sfeir-codemender-google-agent-faille-correctif-2026-10-26

## Veille

Article **SFEIR AI** publié sur sfeir.com le **26 octobre 2026** (~10 000 signes, huit sources notées : blog DeepMind, annonce Google Cloud, Help Net Security, The Register…). Il retrace le passage de **CodeMender** du projet de recherche **Google DeepMind** (octobre 2025, **72** correctifs soumis à des projets open source, dont un de **4,5 millions** de lignes) à la preview **Google Cloud** du **21 juillet 2026**. Trois apports. **(A)** Les deux portes d'accès : **Gemini Enterprise Agent Platform** et **AI Threat Defense**, où **Wiz** (racheté en mars 2026) orchestre CodeMender via ses agents Red Agent et Green Agent ; une version couplée à **Gemini 3.5 Flash Cyber** reste réservée. **(B)** La chaîne *chercher → prouver par un exploit en bac à sable → corriger (diff + modèle juge) → relecture humaine*, et le **mode proactif** qui ferme une classe de failles (annotations `-fbounds-safety` sur **libwebp**, qui auraient neutralisé **CVE-2023-4863**). **(C)** Quatre questions laissées au client : où tourne le modèle, qui confine l'agent, qui relit, quelle trace reste au regard du **Cyber Resilience Act**. Clôture sur l'offre AI Cyber. Fait suite à [[sfeir-bank-of-america-mythos-prestataires-correctifs-2026-10-26]].

## Titre Article

CodeMender : Google veut que l'agent qui trouve la faille écrive aussi le correctif

## Date

2026-10-26

## URL

https://www.sfeir.com/articles/codemender-google-agent-faille-correctif/

## Keywords

CodeMender, Google DeepMind, Google Cloud, Gemini Deep Think, Gemini Enterprise Agent Platform, AI Threat Defense, Wiz, Red Agent, Green Agent, Gemini 3.5 Flash Cyber, exploit, preuve par exploit, faux positifs, correctif automatique, LLM juge, revue humaine, mode proactif, -fbounds-safety, libwebp, CVE-2023-4863, fuzzing, Big Sleep, OSS-Fuzz, Cyber Resilience Act, AI Cyber, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Article de décryptage produit, registre explicatif. La première moitié restitue l'annonce de Google et le billet de DeepMind en citant leurs auteurs et leurs chiffres, sans reprendre les formules promotionnelles à son compte (les témoignages clients sont attribués). La partie centrale décompose le fonctionnement en quatre verbes (chercher, prouver, corriger, faire relire). L'article signale ce que l'annonce ne décrit pas (analyse réseau coupé, datation des passages) sous forme de questions ouvertes. La dernière section présente l'offre AI Cyber de SFEIR comme application du même principe au code interne. Public : RSSI, DSI, responsables d'ingénierie.

## Pense-betes

- **Octobre 2025** : CodeMender présenté par **Raluca Ada Popa** et **Four Flynn** (DeepMind) ; raisonne avec **Gemini Deep Think** + analyse statique/dynamique, fuzzing, tests différentiels, solveurs SMT ; outil de critique LLM comparant code d'origine et modifié. Prolonge **Big Sleep** et **OSS-Fuzz**.
- **72 correctifs** en six mois à des projets open source (jusqu'à **4,5 M** de lignes), « modest-compute run », acceptés par les mainteneurs.
- **21 juillet 2026** : preview Google Cloud (Michael Gerstenhaber, Clemens Viernickel). Accès : **Gemini Enterprise Agent Platform** ou **AI Threat Defense** orchestré par **Wiz** (Red Agent = tests d'intrusion, Green Agent = correctifs). Version **Gemini 3.5 Flash Cyber** réservée à gouvernements et partenaires.
- Langages : C/C++, Go, Java, Python, Ruby, Rust, TypeScript. Modèles tiers annoncés d'ici fin d'année. Témoins : Salesforce, Robinhood, Palo Alto Networks.
- **Chaîne** : chercher (classes de failles, gravité) → **prouver** (exploit exécuté en bac à sable géré par le client — réponse aux faux positifs) → corriger (diff + **second modèle juge**, conventions du client) → **relecture humaine** de chaque patch.
- Exploitation : trafic via le VPC client, pas de conservation du code ; CI/CD ou CLI (VS Code, Antigravity).
- **Mode proactif** : réécrire pour fermer une famille de failles. Exemple **libwebp** + `-fbounds-safety` (Clang) → aurait rendu inexploitable **CVE-2023-4863** (zero-click iOS).
- Reste à charge : **où tourne le modèle** (pas de mode réseau coupé décrit) ; **qui confine** l'agent qui exécute des exploits ; **qui relit** (goulot de revue) ; **quelle trace** — harnais mis à jour en continu, un scan de juillet ne vaut plus en octobre ; CRA.
- Offre **AI Cyber** : pas de faille sans preuve, test qui échoue + correctif, legacy d'abord, registre daté par passage, réécriture (Rust) d'un module à bugs mémoire récurrents.

## RésuméDe400mots

Cet article de SFEIR, publié le 26 octobre 2026, présente CodeMender, l'agent de Google qui cherche les failles d'un dépôt, construit un exploit pour prouver qu'elles sont réelles, puis écrit le correctif. Google Cloud l'a ouvert en preview le 21 juillet 2026.

En octobre 2025, CodeMender n'était qu'un projet de recherche de Google DeepMind, présenté par Raluca Ada Popa et Four Flynn. Il raisonnait avec Gemini Deep Think et s'appuyait sur les outils classiques d'analyse de programme : analyse statique et dynamique, fuzzing, tests différentiels, solveurs SMT, ainsi qu'un outil de critique fondé sur un LLM pour repérer les régressions. En six mois, l'équipe avait soumis soixante-douze correctifs à des projets open source, acceptés par les mainteneurs.

La preview de 2026 offre deux portes : Gemini Enterprise Agent Platform, avec les modèles Gemini, et AI Threat Defense, la plateforme de sécurité de Google, où Wiz, racheté en mars 2026, orchestre CodeMender avec ses propres agents de test d'intrusion et de correction. Une version couplée à Gemini 3.5 Flash Cyber reste réservée à quelques gouvernements et partenaires. L'agent couvre sept langages et Robinhood affirme qu'il a trouvé des failles critiques manquées par ses autres outils.

Le fonctionnement enchaîne des filtres : chercher des classes de failles et les classer, prouver chaque hypothèse par un exploit exécuté dans un bac à sable géré par le client, générer un correctif vérifié par un second modèle juge, puis le soumettre à la relecture d'un développeur. Les données transitent par le VPC du client et le code n'est pas conservé.

DeepMind avait aussi conçu un mode proactif : réécrire du code pour qu'une famille entière de failles ne soit plus exploitable. Sur libwebp, des annotations de vérification de bornes auraient rendu inexploitable la faille CVE-2023-4863. Pour une DSI, l'article juge ce mode plus important : il ferme toutes les portes du même type, y compris celles non encore trouvées.

SFEIR souligne ce qui reste à la charge du client. Les correctifs de 2025 portaient sur de l'open source déjà très relu, alors que le code interne n'a pas ce public. L'annonce laisse ouvertes quatre questions : où tourne le modèle, qui confine un agent qui exécute du code d'attaque, qui relit quand l'agent produit plus vite que l'équipe, et comment dater chaque analyse alors que le harnais évolue en continu et que le Cyber Resilience Act impose de documenter les vulnérabilités. L'article présente enfin l'offre AI Cyber de SFEIR, fondée sur le même principe de preuve, appliquée au legacy et au code sous-traité.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | CodeMender : Google veut que l'agent qui trouve la faille écrive aussi le correctif | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Google DeepMind | ORGANISATION | a_créé | CodeMender | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Google Cloud | ORGANISATION | publie | CodeMender | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | utilise | Gemini Deep Think | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | utilise | fuzzing | METHODOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | s_inspire_de | Big Sleep | TECHNOLOGIE | 0.82 | STATIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | mesure | 72 correctifs soumis en six mois à des projets open source (jusqu'à 4,5 M de lignes) | MESURE | 0.92 | STATIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | fait_partie_de | AI Threat Defense | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Wiz | ORGANISATION | utilise | CodeMender | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| Wiz | ORGANISATION | fait_partie_de | Google | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | utilise | preuve par exploit | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| preuve par exploit | METHODOLOGIE | réduit | faux positifs de l'analyse statique | CONCEPT | 0.86 | ATEMPOREL | déclaré_article |
| CodeMender | TECHNOLOGIE | utilise | LLM juge | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | permet | fermeture proactive d'une classe de failles | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Google DeepMind | ORGANISATION | affirme_que | des annotations -fbounds-safety sur libwebp auraient rendu CVE-2023-4863 inexploitable | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Gemini 3.5 Flash Cyber | TECHNOLOGIE | est_variante_de | Gemini | TECHNOLOGIE | 0.82 | STATIQUE | inféré |
| SFEIR | ORGANISATION | affirme_que | quand l'agent produit des correctifs plus vite que l'équipe ne les relit, la revue devient le goulot | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | dater et consigner chaque passage d'analyse dans un registre, et relancer à chaque génération de modèle | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| CodeMender | TECHNOLOGIE | catégorie | Agent de sécurité du code : cherche, prouve par exploit, corrige ; preview Google Cloud 21 juillet 2026 | AJOUT |
| Google DeepMind | ORGANISATION | rôle | Créateur de CodeMender (recherche, octobre 2025) | AJOUT |
| AI Threat Defense | TECHNOLOGIE | catégorie | Plateforme de sécurité Google orchestrée par Wiz | AJOUT |
| Wiz | ORGANISATION | statut | Racheté par Google (finalisé en mars 2026) | AJOUT |
| preuve par exploit | METHODOLOGIE | définition | Une faille ne compte que si un exploit exécuté en bac à sable la démontre | AJOUT |
| Gemini 3.5 Flash Cyber | TECHNOLOGIE | accès | Réservé à des gouvernements et partenaires de confiance | AJOUT |
