# anthropic-claude-fable-5-mythos-5-2026-06-09

## Veille

Anthropic lance Claude Fable 5 (modèle de classe Mythos rendu sûr pour usage général) et Claude Mythos 5 (même modèle, garde-fous levés, réservé aux cyberdéfenseurs via Project Glasswing) : performances état de l'art en ingénierie logicielle, vision, mémoire long-contexte et sciences du vivant.

## Titre Article

Claude Fable 5 and Claude Mythos 5

## Date

2026-06-09

## URL

https://www.anthropic.com/news/claude-fable-5-mythos-5

## Keywords

Claude Fable 5, Claude Mythos 5, modèle de fondation, classe Mythos, agents autonomes, ingénierie logicielle, vision par ordinateur, mémoire persistante, sciences du vivant, design de protéines, cybersécurité, Project Glasswing, garde-fous, alignement, tarification tokens, Opus 4.8

## Authors

Anthropic

## Ton

Profil : communication corporate institutionnelle d'un laboratoire d'IA (perspective « nous » d'entreprise), registre technique-promotionnel maîtrisé, public cible développeurs, chercheurs et décideurs техniques. Le style équilibre l'annonce produit (records de benchmarks, témoignages clients) et un discours de responsabilité (garde-fous, classifieurs, system card, politique de rétention de données). L'autorité repose sur des résultats chiffrés, des évaluations partenaires (Cognition, Hebbia, GitHub, Cursor) et des cas d'usage concrets (migration Stripe, design de protéines). Métaphore récurrente du « modèle qui travaille de façon autonome plus longtemps que jamais ». Anthropic met en avant un double objectif explicite : déployer vite ET en sécurité, en assumant des garde-fous volontairement conservateurs (faux positifs < 5 % des sessions).

## Pense-betes

- **Deux modèles, un même socle** : Fable 5 = version grand public avec garde-fous ; Mythos 5 = même modèle, garde-fous levés, réservé aux cyberdéfenseurs/fournisseurs d'infrastructure via Project Glasswing (collaboration avec le gouvernement US).
- **Tarification** : 10 $/M tokens en entrée, 50 $/M tokens en sortie — moins de la moitié du prix de Claude Mythos Preview.
- **Disponibilité** : Fable 5 immédiatement sur l'API Claude et plans à la consommation ; déploiement sur les abonnements du 9 au 22 juin 2026 ; Mythos 5 restreint aux partenaires Glasswing + chercheurs en biologie (programme d'accès de confiance à venir).
- **Trois classifieurs de sécurité** : cybersécurité (0 conformité sur 30 techniques de jailbreak en test externe), biologie/chimie (repli sur Opus 4.8), anti-distillation (réplication non autorisée).
- **Nouvelle politique** : rétention des données 30 jours pour les modèles de classe Mythos (monitoring de sécurité).
- **Ingénierie** : Stripe a réalisé une migration d'un codebase Ruby de 50 M lignes en un jour (vs deux mois manuellement) ; score le plus élevé des modèles frontière sur FrontierCode (Cognition), même à effort moyen.
- **Vision** : état de l'art ; reconstruit le code d'une web app à partir de captures d'écran ; termine Pokémon FireRed avec un harnais vision seule.
- **Mémoire long-contexte** : focus sur des millions de tokens ; mémoire fichier persistante améliore les perfs 3× plus que pour Opus 4.8 (Slay the Spire).
- **Sciences du vivant** (Mythos 5) : design de protéines ~10× plus rapide ; hypothèses de biologie moléculaire préférées ~80 % du temps en aveugle vs modèles de classe Opus ; modèle de génomique 100× plus petit surpassant une publication récente de Science.
- **Garde-fous conservateurs** : se déclenchent en moyenne dans < 5 % des sessions, avec faux positifs assumés.

## RésuméDe400mots

Le 9 juin 2026, Anthropic annonce le lancement simultané de deux modèles. **Claude Fable 5** est un modèle de « classe Mythos » rendu sûr pour un usage général : ses capacités dépassent celles de tout modèle qu'Anthropic a rendu publiquement disponible, atteignant l'état de l'art sur la quasi-totalité des benchmarks testés. **Claude Mythos 5** est le même modèle sous-jacent, mais avec les garde-fous levés dans certains domaines ; il est réservé à un petit groupe de cyberdéfenseurs et fournisseurs d'infrastructure, déployé initialement via Project Glasswing (en collaboration avec le gouvernement américain) comme mise à niveau de Claude Mythos Preview. Mythos 5 possède les plus fortes capacités de cybersécurité de tous les modèles au monde.

Les deux modèles sont tarifés à 10 $ par million de tokens en entrée et 50 $ en sortie, soit moins de la moitié du prix de Mythos Preview. Pour déployer rapidement et en sécurité, Fable 5 embarque des garde-fous (classifieurs) volontairement conservateurs : sur certains sujets, la requête reçoit la réponse d'Opus 4.8. Ils se déclenchent en moyenne dans moins de 5 % des sessions.

Côté capacités, **ingénierie logicielle** : Stripe rapporte que Fable 5 a « comprimé des mois d'ingénierie en jours », réalisant une migration d'un codebase Ruby de 50 millions de lignes en un jour (vs deux mois pour une équipe). Le modèle obtient le meilleur score des modèles frontière sur FrontierCode (Cognition). **Travail de connaissance** : meilleur score de tous les modèles sur le Finance Benchmark de Hebbia (raisonnement niveau senior). **Vision** : état de l'art ; reconstruit le code source d'une web app depuis des captures d'écran, termine Pokémon FireRed en vision seule. **Mémoire** : la mémoire fichier persistante améliore ses performances 3× plus que pour Opus 4.8.

**Sciences du vivant** : avec Mythos 5, les experts en design de protéines d'Anthropic ont accéléré le processus d'environ 10× ; 9 des 14 cibles protéiques ont donné des candidats forts. Mythos 5 est le premier modèle à produire des hypothèses scientifiques nouvelles et convaincantes, préférées ~80 % du temps en comparaison aveugle ; il a aussi mené des recherches de génomique autonomes, entraînant un modèle 100× plus petit qui surpasse une publication récente de Science. L'évaluation d'alignement automatisée situe le comportement désaligné de Mythos 5 à un niveau bas, similaire à Opus 4.8. Des témoignages clients (Cursor, GitHub, Vercel, EvolutionaryScale) confirment l'autonomie sur des tâches à long horizon et un raisonnement supérieur à Opus 4.8.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Anthropic | ORGANISATION | a_créé | Claude Fable 5 | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | a_créé | Claude Mythos 5 | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Fable 5 | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | est_variante_de | Claude Mythos 5 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | est_instance_de | classe Mythos | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | utilise | classifieurs de sécurité | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | utilise | Opus 4.8 | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | surpasse | Opus 4.8 | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Claude Mythos 5 | TECHNOLOGIE | remplace | Claude Mythos Preview | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Claude Mythos 5 | TECHNOLOGIE | fait_partie_de | Project Glasswing | EVENEMENT | 0.90 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | collabore_avec | gouvernement américain | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | mesure | meilleur score des modèles frontière sur FrontierCode | MESURE | 0.90 | STATIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | mesure | 10 $/M tokens entrée et 50 $/M tokens sortie | MESURE | 0.95 | STATIQUE | déclaré_article |
| Stripe | ORGANISATION | affirme_que | Fable 5 a migré un codebase Ruby de 50M lignes en un jour | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Claude Mythos 5 | TECHNOLOGIE | améliore | design de protéines accéléré ~10× | MESURE | 0.88 | STATIQUE | déclaré_article |
| Claude Mythos 5 | TECHNOLOGIE | surpasse | modèles spécialisés de design de protéines | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Claude Fable 5 | TECHNOLOGIE | permet | agents autonomes sur tâches à long horizon | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | recommande | rétention des données 30 jours pour la classe Mythos | CONCEPT | 0.85 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Claude Fable 5 | TECHNOLOGIE | catégorie | Modèle de fondation classe Mythos, usage général | AJOUT |
| Claude Fable 5 | TECHNOLOGIE | tarification | 10 $/M tokens entrée, 50 $/M tokens sortie | AJOUT |
| Claude Mythos 5 | TECHNOLOGIE | catégorie | Modèle classe Mythos, garde-fous levés, accès restreint | AJOUT |
| Claude Mythos 5 | TECHNOLOGIE | accès | Cyberdéfenseurs et fournisseurs d'infrastructure via Project Glasswing | AJOUT |
| classe Mythos | CONCEPT | définition | Famille de modèles Anthropic les plus capables | AJOUT |
| Project Glasswing | EVENEMENT | nature | Programme cyberdéfense Anthropic + gouvernement US | AJOUT |
| Opus 4.8 | TECHNOLOGIE | rôle | Modèle de repli pour requêtes filtrées par les garde-fous | AJOUT |
| Claude Mythos Preview | TECHNOLOGIE | statut | Remplacé par Mythos 5 | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| Stripe | ORGANISATION | rôle | Testeur précoce (migration Ruby 50M lignes) | AJOUT |
