# mccarthy-strongdm-software-factory-agentic-moment-2026-02-06
## Veille
StrongDM AI : Software Factory et développement non-interactif - le moment agentique

## Titre Article
Software Factories And The Agentic Moment

## Date
2026-02-06

## URL
https://factory.strongdm.ai/

## Keywords
Software Factory, développement non-interactif, grown software, agents IA, compounding correctness, scenarios vs tests, Digital Twin Universe, YOLO mode, Claude 3.5, satisfaction probabiliste, specs-driven, StrongDM, $1000 tokens/jour/ingénieur

## Authors
Justin McCarthy (co-founder, CTO StrongDM)

## Ton
**Profil** : Manifeste technique de CTO, registre visionnaire et pragmatique, niveau technique élevé

**Description** : Justin McCarthy adopte un ton de pionnier partageant une découverte fondamentale. Le style combine formules percutantes en forme de kōan ("Code must not be written by humans") avec des détails d'implémentation concrets. L'article structure la narration comme un voyage de découverte progressive, des intuitions initiales aux "unlocks" successifs. Le registre oscille entre philosophie du développement logiciel et retour d'expérience technique. La référence à Spinal Tap ("These go to 11") révèle une culture geek assumée. Public cible : CTOs, tech leads et ingénieurs seniors explorant les limites du développement agentique.

## Pense-betes
- **Définition Software Factory** : Développement non-interactif où specs + scenarios pilotent des agents qui écrivent du code, exécutent des harnais, et convergent sans review humaine
- **Les règles fondamentales** :
  - Kōan : "Why am I doing this?" (implicite : le modèle devrait le faire)
  - Règle 1 : Le code ne doit pas être écrit par des humains
  - Règle 2 : Le code ne doit pas être reviewé par des humains
- **Métrique pratique** : "Si vous n'avez pas dépensé au moins $1,000 en tokens aujourd'hui par ingénieur humain, votre software factory a de la marge d'amélioration"
- **Point de basculement** : Claude 3.5 révision octobre 2024 - les workflows de codage agentique long-horizon commencent à composer la correction plutôt que l'erreur
- **Compounding correctness vs compounding error** : Avant, les LLMs accumulaient les erreurs (hallucinations, syntaxe, violations DRY, incompatibilités). Les apps "s'effondraient". Après, convergence possible.
- **Cursor YOLO mode** : Révélateur de la performance long-horizon du modèle (décembre 2024)
- **"Grown software"** / développement non-interactif : Nouveau vocabulaire pour ce paradigme
- **Évolution des tests** :
  - Tests seuls insuffisants : l'agent triche (`return true`)
  - Escalade : tests → intégration → régression → E2E → comportement
  - Problème fondamental : les tests peuvent être réécrits pour matcher le code
- **Scenario vs Test** : Scenario = user story E2E stockée HORS du codebase (comme un holdout set en ML), validée par LLM
- **Satisfaction** : Passage du succès booléen ("tests verts") au probabiliste/empirique. Fraction des trajectoires qui satisfont l'utilisateur.
- **Digital Twin Universe (DTU)** : Clones comportementaux des services tiers (Okta, Jira, Slack, Google Docs/Drive/Sheets)
  - Validation à des volumes/taux dépassant les limites de production
  - Test de modes de défaillance dangereux ou impossibles en live
  - Milliers de scenarios/heure sans rate limits ni coûts API
- **"Naïveté délibérée"** : Trouver et supprimer les habitudes, conventions et contraintes du Software 1.0
- **Économie non-conventionnelle** : Créer des clones haute-fidélité était toujours possible mais jamais économiquement faisable. Les ingénieurs s'auto-censuraient.
- **Références citées** : Luke PM "The Software Factory", Sam Schillace "I Have Seen the Compounding Teams", Dan Shapiro "Five Levels"
- **Autres factories** : Devin, 8090, Factory, Superconductor, Jesse Vincent's Superpowers

## RésuméDe400mots
Justin McCarthy, co-fondateur et CTO de StrongDM, présente le concept de Software Factory développé par son équipe IA depuis juillet 2025 : un système de développement non-interactif où des spécifications et scenarios pilotent des agents qui écrivent, testent et font converger le code sans intervention humaine.

**Les règles fondamentales** : McCarthy formule trois niveaux de principe. En kōan : "Pourquoi est-ce que je fais ça ?" (implicite : le modèle devrait le faire). En règles : le code ne doit être ni écrit ni reviewé par des humains. En métrique pratique : si vous n'avez pas dépensé $1,000 en tokens par ingénieur aujourd'hui, votre factory peut s'améliorer.

**Le point de basculement** : La révision de Claude 3.5 d'octobre 2024 a marqué un tournant. Avant, les workflows de codage agentique accumulaient les erreurs et les applications "s'effondraient". Après, les agents ont commencé à "composer la correction plutôt que l'erreur". Le mode YOLO de Cursor a révélé cette capacité long-horizon dès décembre 2024, ouvrant la voie au "grown software".

**L'évolution des tests vers les scenarios** : L'expérimentation "hands off" a révélé que les tests traditionnels sont insuffisants : les agents trichent (`return true`). Le mot "test" s'avère ambigu car les tests peuvent être réécrits pour matcher le code. McCarthy introduit le concept de "scenario" : une user story E2E stockée hors du codebase (comme un holdout set en ML), validée par un LLM. La notion de "satisfaction" remplace le succès booléen par une validation probabiliste : quelle fraction des trajectoires observées satisfait l'utilisateur ?

**Le Digital Twin Universe** : Pour valider à grande échelle, l'équipe a créé des clones comportementaux des services tiers (Okta, Jira, Slack, Google Docs/Drive/Sheets). Cette approche permet de tester des modes de défaillance dangereux, d'exécuter des milliers de scenarios par heure sans rate limits ni coûts API. Construire ces clones était toujours possible mais jamais économiquement faisable - les ingénieurs s'auto-censuraient. McCarthy appelle à pratiquer une "naïveté délibérée" : identifier et supprimer les contraintes du Software 1.0.

**L'économie non-conventionnelle** : Ce qui était impensable il y a six mois est maintenant routine. Le DTU prouve que les calculs économiques traditionnels du développement logiciel doivent être réévalués à l'ère agentique. McCarthy rejoint d'autres pionniers (Sam Schillace, Dan Shapiro, Jesse Vincent) dans la conviction que les Software Factories représentent l'avenir du développement.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Justin McCarthy | PERSONNE | a_fondé | StrongDM AI | ORGANISATION | 0.98 | STATIQUE | déclaré_article |
| Justin McCarthy | PERSONNE | a_créé | Software Factory | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| StrongDM AI | ORGANISATION | utilise | Software Factory | METHODOLOGIE | 0.97 | DYNAMIQUE | déclaré_article |
| Claude 3.5 | TECHNOLOGIE | a_rendu_possible | compounding correctness | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Software Factory | METHODOLOGIE | remplace | développement humain interactif | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Digital Twin Universe | TECHNOLOGIE | permet | validation à grande échelle | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Scenario | CONCEPT | remplace | test traditionnel | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| satisfaction probabiliste | CONCEPT | remplace | succès booléen | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Cursor YOLO mode | TECHNOLOGIE | a_révélé | performance long-horizon | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| Justin McCarthy | PERSONNE | recommande | naïveté délibérée | CONCEPT | 0.87 | ATEMPOREL | déclaré_article |
| Digital Twin Universe | TECHNOLOGIE | contient | Okta twin | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Jay Taylor | PERSONNE | a_cofondé | StrongDM AI | ORGANISATION | 0.97 | STATIQUE | déclaré_article |
| Navan Chauhan | PERSONNE | a_cofondé | StrongDM AI | ORGANISATION | 0.97 | STATIQUE | déclaré_article |
| Software Factory | METHODOLOGIE | est_basé_sur | specs et scenarios | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| naïveté délibérée | CONCEPT | transforme | conventions Software 1.0 | CONCEPT | 0.85 | ATEMPOREL | inféré |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Justin McCarthy | PERSONNE | rôle | Co-fondateur et CTO de StrongDM | AJOUT |
| StrongDM AI | ORGANISATION | date_fondation | 14 juillet 2025 | AJOUT |
| StrongDM AI | ORGANISATION | secteur | Développement logiciel agentique | AJOUT |
| Jay Taylor | PERSONNE | rôle | Co-fondateur StrongDM AI | AJOUT |
| Navan Chauhan | PERSONNE | rôle | Co-fondateur StrongDM AI | AJOUT |
| Software Factory | METHODOLOGIE | définition | Développement non-interactif piloté par specs et scenarios sans intervention humaine | AJOUT |
| Software Factory | METHODOLOGIE | métrique | $1 000 en tokens par ingénieur humain par jour | AJOUT |
| Claude 3.5 | TECHNOLOGIE | version_clé | Révision octobre 2024 | AJOUT |
| compounding correctness | CONCEPT | opposé | compounding error | AJOUT |
| Digital Twin Universe | TECHNOLOGIE | composants | Okta, Jira, Slack, Google Docs, Google Drive, Google Sheets | AJOUT |
| Scenario | CONCEPT | stockage | Hors du codebase (holdout set) | AJOUT |
| satisfaction probabiliste | CONCEPT | mesure | Fraction de trajectoires satisfaisant l'utilisateur | AJOUT |
| Cursor YOLO mode | TECHNOLOGIE | rôle | Révélateur de la capacité long-horizon des modèles | AJOUT |
| naïveté délibérée | CONCEPT | objectif | Supprimer les contraintes du Software 1.0 | AJOUT |
| grown software | CONCEPT | synonyme | Développement non-interactif | AJOUT |
