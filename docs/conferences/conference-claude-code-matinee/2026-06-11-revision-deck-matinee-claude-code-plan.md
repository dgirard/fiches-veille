# Plan — Révision du deck « Matinée Claude Code » (104 slides, 10/session)

Created: 2026-06-11

## Objectif et livrables

Réviser le deck existant `~/Downloads/matinee-claude-code-slides.html` (104 slides, design Sharp Artisan, 10 slides par session déjà respectés) en l'enrichissant des sources fournies, puis régénérer la conversion PowerPoint. Livrables (remplacement sur place) :

- `~/Downloads/matinee-claude-code-slides.html` — deck unique révisé, ~104 slides
- `~/Downloads/matinee-claude-code.pptx` — conversion régénérée (python-pptx 1.0.2 disponible)

## Sources et leur rôle

| Source | Rôle |
|---|---|
| `~/Downloads/Matinée Claude Code — Déroulé détaillé & Abstracts.docx` | **Structure autoritaire** : 10 sessions, arc POURQUOI→COMMENT→PREUVE→MÉTHODE→ÉCHELLE→ARGENT→CONTRÔLE→CONFIANCE→DÉMO→SUITE, messages-clés, plans minute par minute, transitions « bascule » |
| `~/Downloads/Session 5 - De l'artisanat à l'usine logicielle.md` | **Script autoritaire slide par slide** pour la session 5 (10 slides déjà spécifiés, règle « zéro JSON », climax sub-agents) |
| Rapport CCA-F (fourni dans la demande, à conserver avec ce plan) | **Source autoritaire** pour la session 8 certification : paliers Partner Network, 5 domaines/pondérations, format examen, profils praticien/théoricien, validité 6 mois, filières de préparation |
| `~/Downloads/prez/*.pptx` (20 fichiers) | Matière première par thème ; 15 déjà extraits en markdown dans `~/projects/ASpider/docs/matiere/extracted/`, ~5 nouveaux à extraire |
| Fiches veille (`~/projects/veille`, 292 fiches) | Chiffres et citations sourcées : Fable 5 (Stripe 50M lignes), Tokenomics Foundation (Goldman ×24), Salesforce (+151 % Effective Output, « removed all token limits »), Rafal (sandwich teams ~80 % de la chaîne, 3 gates), Compound Engineering (Klaassen definitive guide), Uber zero-trust agents, Shihipar skills, Wescale usine augmentée, Raiffeisen |

## Correspondance sessions ↔ sources

| # | Session | Sources principales | Effort attendu |
|---|---|---|---|
| 1 | Keynote — La tech bascule | **Rappeler l'arc narratif de la matinée** (visuel dédié dans l'intro) : `POURQUOI → COMMENT → PREUVE → MÉTHODE SFEIR → ÉCHELLE → ARGENT → CONTRÔLE → CONFIANCE → DÉMO → SUITE` ; BFM « Basculement », Impact_IA_Production_SI *(à extraire)*, Sharp Artisan ; fiches Fable 5, DORA 2025 | Moyen — chiffre choc + arc |
| 2 | SDLC AI | **Le cycle en 11 phases doit être expliqué et dessiné** (absent du deck actuel) : sdlc-v3 (vocabulaire, thèse, convictions), AG2R slide 8 (représentation visuelle de référence) ; appui : tokens-sdlc-v3, Foyer, Context Engineering v1/v2, fiches Rafal, Salesforce | **Fort** — refonte autour du cycle |
| 3 | Martignole (récit externe) | Déroulé uniquement — slides de cadre, liberté éditoriale de l'intervenant | **Faible** — ne pas surcharger |
| 4 | Sandwich Team & Compound | AG2R v1/v2/v3 *((3) à extraire)* ; fiches Compound Engineering (definitive guide, Every), Rafal (~80 % de la chaîne) | Moyen |
| 5 | Artisanat → usine | **Le md Session 5 fait foi** ; appui : fiches Shihipar skills, Wescale | Conformité stricte au script |
| 6 | Coûts / FinOps | tokenomics-finops-sdlc-50min *(à extraire)*, Token & Outcome *(à extraire)*, token-outcome-finops ; fiches Tokenomics Foundation, Rafal J+1, Salesforce ; coût ~6 $/jour/dev (rapport CCA-F) | Moyen-fort — nouveaux pptx du 09/06 |
| 7 | Gouvernance & sécurité | Fiches Uber zero-trust, Raiffeisen shift-left ; volet hooks/permissions du md Session 5 ; AG2R | Moyen |
| 8 | Certification CCA-F | **Rapport CCA-F fait foi** : Partner Network (Select ≥10 / Preferred ≥100 / Global Premier ≥1000 certifiés), 5 domaines pondérés (27/18/20/20/15 %), 60 q/120 min proctoré, 6 scénarios→4 tirés, praticien 850-985 vs théoricien <590, validité 6 mois, Partner Academy/ExamPro/Simpliaxis/Preporato, 99 USD/tentative | **Fort** — source nouvelle et riche |
| 9 | Démo live spec→PR | Déroulé (cadre, étapes, mapping étape↔session du matin, filet vidéo de secours) | Faible |
| 10 | Clôture — lundi matin | Déroulé (synthèse arc, 3 premiers pas, offre SFEIR) | Faible |

## Déroulé du travail

### Phase 1 — Extraction des nouveaux pptx (préparation)

- Identifier les pptx de `~/Downloads/prez/` absents de `~/projects/ASpider/docs/matiere/extracted/` : `20260609 - tokenomics-finops-sdlc-50min`, `Token & Outcome — FinOps agentique (1)`, `20260609-Impact_IA_sur_la_Production_de_SI-fond-clair`, `20260525 - AG2R (3)` (les doublons de taille identique, ex. `tokens-sdlc-v3 (3)` = `(1)`, sont ignorés)
- Les extraire en markdown via le script ASpider (`sfeir-content-engine/scripts/extract_matiere.py`) ou python-pptx directement

### Phase 2 — Audit d'écart session par session

- Relire le deck HTML existant session par session contre : déroulé (messages-clés, plan minute par minute, « Ce qu'on montre », transitions), script Session 5, rapport CCA-F, matière extraite
- Produire une liste de corrections par session : chiffres manquants ou périmés, messages-clés absents, slides à remplacer
- Contrainte invariante : **10 slides par session** — toute addition implique une suppression

### Phase 3 — Révision dans l'ordre de valeur

1. **S8 Certification** — source autoritaire nouvelle, refonte probable des 10 slides : pourquoi la certif compte pour un client, paliers partenariat, grille 5 domaines + pondérations, format et scénarios d'examen, profils de réussite (praticien vs théoricien), validité 6 mois et recertification, modèles/tarifs Claude, parcours de préparation, engagement SFEIR
2. **S2 SDLC AI** — refonte autour du **cycle en 11 phases**, aujourd'hui non expliqué dans le deck :
   - **Le dessin du cycle est obligatoire** (le visuel central de la session) : reproduire en SVG la frise du slide 8 AG2R — `0 SETUP → 1 DEFINE (gate) → 2 PLAN (gate) → 3 BUILD → 4 VERIFY → 5 REVIEW → 6 COMPOUND-1 → 7 SHIP (gate) → 8 OPS → 9 COMPOUND-2 → 10 DEPRECATION` — avec code visuel distinct pour les 3 gates humains (spec, plan, pull request), les 2 moments de capitalisation, et les phases exécutées par les agents
   - Poser le vocabulaire avant le dessin (sdlc-v3 slide 2) : un cycle = **une** unité de travail (pas un sprint, pas une release), quelques heures à quelques jours de construction + 7-14 jours d'observation, deux moments d'apprentissage
   - Porter la thèse (sdlc-v3 slide 3) : « le code est le sous-produit, l'actif est la connaissance » ; l'IA exécute, l'humain garde 3 gates inviolables, le système apprend (« le 100ᵉ cycle est meilleur que le 1ᵉʳ — par construction », fix iterations −30 % après 10 cycles)
   - Garder le message du déroulé : Context Engineering comme compétence centrale + bascule de rôle producteur → pilote d'agents
3. **S5 Artisanat→usine** — mise en conformité stricte avec le script : 4 propriétés de l'industrialisation (répétable, partagé, gouverné, auditable), climax sub-agents protégé (5 min), arborescence `.claude/` montrée en noms de fichiers, zéro JSON
4. **S6 Coûts** — intégrer les 2 pptx FinOps du 09/06 + doctrine Tokenomics Foundation (token = unité de mesure, coût par feature vs jour-homme)
5. **S1 Keynote / intro** — ajouter le rappel explicite de l'arc narratif de la matinée dans les slides d'ouverture (slide « programme en un coup d'œil » ou slide dédié) :
   - Visuel de l'arc : `POURQUOI → COMMENT → PREUVE → MÉTHODE SFEIR → ÉCHELLE → ARGENT → CONTRÔLE → CONFIANCE → DÉMO → SUITE`, chaque mot relié à sa session (1 Keynote, 2 SDLC AI, 3 Martignole, 4 Sandwich Team, 5 Artisanat→usine, 6 Coûts, 7 Gouvernance, 8 CCA-F, 9 Démo live, 10 Clôture)
   - Cet arc répond aux 3 questions du décideur posées par le déroulé : réel ? (PREUVE, DÉMO) · impact ? (COMMENT, MÉTHODE, ÉCHELLE) · contrôle ? (ARGENT, CONTRÔLE, CONFIANCE)
   - Réutilisable en clôture (S10) comme visuel de synthèse de l'arc parcouru
   - Enrichissement du reste de la keynote par les fiches et la matière extraite (chiffre choc à actualiser)
6. S4, S7 — enrichissement par les fiches et la matière extraite
7. S3, S9, S10 — retouches légères (S10 : reprendre le visuel de l'arc en synthèse de clôture)

### Phase 4 — Cohérence globale

- Arc narratif : chaque session se clôt sur sa « bascule » vers la suivante (formulations du déroulé)
- Numérotation des sessions et horaires visibles, gabarit unique Sharp Artisan, français partout
- Vérification du compte : 2 slides d'ouverture + 10×10 + clôture

### Phase 5 — Conversion et livraison

- Régénérer `matinee-claude-code.pptx` depuis le HTML révisé (python-pptx, même pipeline que la version du 11/06 15h29)
- Contrôle visuel des slides à fort enjeu (grilles CCA-F, **dessin du cycle 11 phases S2**, schéma orchestration S5, tableaux FinOps)
- Remplacement des deux fichiers dans `~/Downloads`

## Points de vigilance

- **Fidélité de conversion pptx** : les tableaux denses (paliers Partner Network, 5 domaines) doivent rester lisibles après conversion — simplifier côté HTML si besoin plutôt que de dégrader le pptx
- **Session 5, pièges explicites du script** : zéro JSON à l'écran, ne pas dérouler les 6 briques à plat, dire « gouvernable » et non « simple »
- **Session 3** : c'est le récit de l'intervenant externe — slides d'appui sobres seulement
- **Fichier HTML volumineux (~177 Ko)** : éditer par sections/sessions, jamais de réécriture intégrale en une passe
- **Dessin du cycle S2** : 11 étiquettes + 3 marqueurs de gates sur un seul slide — c'est dense. Privilégier une frise horizontale (comme AG2R) plutôt qu'un anneau ; vérifier la lisibilité après conversion pptx (le SVG sera probablement rastérisé ou simplifié)
