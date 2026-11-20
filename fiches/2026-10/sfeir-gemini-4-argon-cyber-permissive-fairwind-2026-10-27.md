---
themes: [qualite-securite, produits-services]
source: SFEIR
---
# sfeir-gemini-4-argon-cyber-permissive-fairwind-2026-10-27

## Veille

Article **SFEIR AI** publié sur sfeir.com le **27 octobre 2026** (~11 000 signes, un tableau comparatif, onze sources notées, majoritairement la documentation Google Cloud et DeepMind). Il décrit **gemini-4-argon-cyber-permissive**, variante de **Gemini 4 Argon** apparue le **13 octobre 2026** dans la documentation de **Gemini Enterprise Agent Platform**, qui ne bloque pas les tâches offensives ou à double usage et n'est accessible que sur liste, via le **Fairwind Program**. Trois apports. **(A)** Les écarts avec Argon public : raisonnement **HIGH** par défaut, pas de Computer Use, **pas de région eu**, **4 $ / 20 $** par million de tokens sans promotion, **aucune date de retrait garantie** (préavis minimal de **45 jours**). **(B)** Les chiffres, tous issus de Google : **85,8 %** en découverte de vulnérabilités contre 71,0 % pour Gemini 3.8 Flash Cyber, **70,9 %** en test d'intrusion boîte noire (benchmark Wiz), **68 %** sur CWE-bench v1 ; aucun score propre à la variante. **(C)** La logique d'accès : *moins le modèle refuse, plus l'entrée est filtrée* — conditions Fairwind (équipes cyber internes, MFA résistant au phishing, traçage, non-redistribution), plus de **650** partenaires, priorité aux États et infrastructures critiques. Prolonge [[sfeir-codemender-google-agent-faille-correctif-2026-10-26]].

## Titre Article

Gemini 4 Argon Cyber Permissive : Google retire les garde-fous et verrouille la porte

## Date

2026-10-27

## URL

https://www.sfeir.com/articles/gemini-4-argon-cyber-permissive-fairwind/

## Keywords

Gemini 4 Argon, Cyber Permissive, Fairwind Program, Google, Google DeepMind, Gemini Enterprise Agent Platform, Frontier Cyber Models, Gemini 3.8 Flash Cyber, Gemini 3.5 Flash Cyber, CodeMender, cyberdéfense, double usage, garde-fous, liste d'accès, MFA résistant au phishing, cycle de vie des modèles, préavis de retrait, tarification, tokens de raisonnement, région eu, RGPD, CWE-bench, Wiz, Scan for Good, Cyber Verification Program, Trusted Access for Cyber, SFEIR

## Authors

SFEIR AI — signature éditoriale de SFEIR, publiée sur sfeir.com (site éditorial de SFEIR).

## Ton

Article de décryptage produit, registre précis et documentaire. Il s'appuie presque entièrement sur la documentation officielle (pages modèle, cycle de vie, tarifs) et le signale, en précisant que tous les scores viennent de Google et qu'aucune évaluation indépendante n'existe. Le tableau comparatif et les montants exacts servent de base à des mises en garde pratiques (comparateurs qui recopient le tarif promotionnel, facturation des réponses longues échouées). Le titre oppose les deux mouvements, retrait des garde-fous et verrouillage de l'accès. La section RSSI adopte le registre de la check-list (éligibilité, localisation, contrôle d'accès). Clôture sur l'offre AI Cyber de SFEIR. Public : RSSI, responsables SOC, équipes de recherche de vulnérabilités.

## Pense-betes

- **13 octobre 2026** : `gemini-4-argon` ouvert aux clients payants ; même jour, `gemini-4-argon-cyber-permissive` pour la cyberdéfense, **sans blocage des tâches offensives / double usage**, sur liste d'accès (Fairwind ou équipe de compte).
- Annonce d'Argon (30 sept.) : *« we'll be releasing Argon without cyber guardrails »* pour les défenseurs de confiance.
- Gamme cyber en trois mois : **3.5 Flash Cyber** (21 juillet, avec CodeMender) → **3.8 Flash Cyber** (2 sept., GA sur liste le 16 sept.) → **Argon Cyber Permissive** (premier frontier).
- Écarts vs Argon public : raisonnement **HIGH** (vs MEDIUM) ; pas de Computer Use ; régions global/us **sans eu** ; **4 $ / 20 $** (4,40 / 22 $ sur us), exclu de la promo 50 % ; retrait garanti : Argon public ≥ 13 oct. 2027, Permissive **aucune date**, préavis ≥ **45 jours**.
- Usages cités : découverte de vulnérabilités, rétro-ingénierie, vérification d'exploit, génération de correctif. Classé **Frontier Cyber Model** (section 31 des Service Specific Terms).
- Un accès 3.8 Flash Cyber **ne se reporte pas** sur Argon : nouvelle demande.
- Scores (Google, Argon vs 3.8 Flash Cyber) : **85,8 % vs 71,0 %** (découverte, 20 langages) ; **70,9 % vs 58,2 %** (intrusion boîte noire, benchmark Wiz) ; **68 %** CWE-bench v1.
- Facture : tokens de raisonnement facturés en sortie ; dès le **13 nov. 2026**, réponses > 32K tokens facturées même en timeout → plafond de budget dès le premier jour.
- **Fairwind** : équipes internes cyber seulement, MFA anti-phishing, traçage par employé, interdiction de partager/revendre, double usage limité. Vérification par DeepMind ; **650+** partenaires ; priorité États, infrastructures critiques, grandes plateformes. Wiz l'utilise pour **Scan for Good**.
- RSSI : une ESN ou un éditeur moyen ne sont pas prioritaires ; l'accès reste interne (pas d'usage pour un client) ; régler RGPD avant dossier ; modèle remplaçable en 45 jours. Programmes équivalents : Cyber Verification Program (Anthropic), Trusted Access for Cyber (OpenAI).

## RésuméDe400mots

Cet article de SFEIR, publié le 27 octobre 2026, présente la variante cyber de Gemini 4 Argon que Google a rendue disponible le 13 octobre 2026, jour de l'ouverture d'Argon à ses clients payants. Baptisée gemini-4-argon-cyber-permissive, elle est destinée à la cyberdéfense et ne bloque pas les tâches offensives ou à double usage. Elle n'est accessible que sur liste, par le Fairwind Program ou l'équipe de compte Google. Google l'avait annoncé dès la présentation d'Argon, le 30 septembre : les défenseurs de confiance recevraient une version sans garde-fous cyber.

Cette variante complète une gamme construite en trois mois, après Gemini 3.5 Flash Cyber, lancé avec CodeMender en juillet, et Gemini 3.8 Flash Cyber, en septembre. Elle se distingue d'Argon public sur plusieurs points : raisonnement élevé par défaut, absence de Computer Use, absence de région européenne, prix de quatre dollars en entrée et vingt en sortie par million de tokens sans la promotion de lancement, et surtout aucune date de retrait garantie. Google promet seulement quarante-cinq jours de préavis, ce qui impose de construire des chaînes de recherche de vulnérabilités remplaçables rapidement.

Google cite quatre usages : découverte de vulnérabilités, rétro-ingénierie, vérification d'exploit et génération de correctif. Les scores publiés comparent Argon à 3.8 Flash Cyber, avec un net avantage en découverte de vulnérabilités et en test d'intrusion ; aucun score propre à la variante permissive ni aucune évaluation indépendante n'existe. L'article met en garde contre les comparateurs qui affichent le tarif promotionnel d'Argon public, et contre une facture alourdie par les tokens de raisonnement et par la facturation, à partir de novembre, des longues réponses interrompues.

La logique de Google est que la sélection à l'entrée remplace les refus du modèle. Les organisations admises dans Fairwind doivent réserver l'accès à leurs équipes de sécurité internes, authentifier chaque utilisateur avec une MFA résistante au phishing, tracer les usages, ne jamais redistribuer l'accès et limiter le double usage à des fins défensives. Google DeepMind vérifie chaque candidat ; le programme compte plus de six cent cinquante partenaires, avec priorité aux États, aux infrastructures critiques et aux grandes plateformes.

Pour les RSSI, l'article recommande de vérifier l'éligibilité, de traiter la question de la localisation avant de candidater, de se rabattre sinon sur CodeMender avec Argon public, et de mettre en place dès maintenant les contrôles d'accès exigés, que demandent aussi les programmes comparables d'Anthropic et d'OpenAI.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Gemini 4 Argon Cyber Permissive : Google retire les garde-fous et verrouille la porte | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Google | ORGANISATION | publie | Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | est_variante_de | Gemini 4 Argon | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | fait_partie_de | Fairwind Program | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | s_applique_à | cyberdéfense | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | mesure | 4 $ / 20 $ par million de tokens, sans promotion, sans date de retrait garantie | MESURE | 0.9 | DYNAMIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | surpasse | Gemini 3.8 Flash Cyber | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Gemini 4 Argon | TECHNOLOGIE | mesure | 85,8 % en découverte de vulnérabilités (vs 71,0 %), 70,9 % en intrusion boîte noire (vs 58,2 %) | MESURE | 0.86 | STATIQUE | déclaré_article |
| Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | remplace | garde-fous cyber du modèle | CONCEPT | 0.78 | DYNAMIQUE | inféré |
| Google | ORGANISATION | affirme_que | moins le modèle refuse, plus l'accès doit être filtré à l'entrée | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| Google DeepMind | ORGANISATION | dirige | Fairwind Program | METHODOLOGIE | 0.8 | DYNAMIQUE | inféré |
| Fairwind Program | METHODOLOGIE | mesure | plus de 650 partenaires | MESURE | 0.88 | DYNAMIQUE | déclaré_article |
| Wiz | ORGANISATION | utilise | Gemini 4 Argon | TECHNOLOGIE | 0.86 | DYNAMIQUE | déclaré_article |
| CodeMender | TECHNOLOGIE | utilise | Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | 0.82 | DYNAMIQUE | déclaré_article |
| Fairwind Program | METHODOLOGIE | converge_avec | Cyber Verification Program | METHODOLOGIE | 0.78 | DYNAMIQUE | inféré |
| SFEIR | ORGANISATION | recommande | construire des chaînes de recherche de vulnérabilités remplaçables en 45 jours (prompts, tests, format de sortie indépendants du modèle) | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | MFA résistant au phishing, journal d'usage par utilisateur et accès limité aux équipes sécurité avant toute candidature | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle | AJOUT |
| Gemini 4 Argon Cyber Permissive | TECHNOLOGIE | accès | Variante cyber sans garde-fous offensifs, sur liste Fairwind, régions global/us | AJOUT |
| Gemini 4 Argon | TECHNOLOGIE | sortie | Annoncé le 30 septembre 2026, ouvert aux clients payants le 13 octobre 2026 | AJOUT |
| Gemini 3.8 Flash Cyber | TECHNOLOGIE | sortie | Annoncé le 2 septembre 2026, GA sur liste d'accès le 16 septembre | AJOUT |
| Fairwind Program | METHODOLOGIE | définition | Programme Google d'accès vérifié aux modèles cyber frontier, lancé le 2 septembre 2026 | AJOUT |
| Cyber Verification Program | METHODOLOGIE | éditeur | Anthropic — accès aux usages cyber les moins bridés pour organisations vérifiées | AJOUT |
