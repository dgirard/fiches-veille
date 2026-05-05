# aisi-uk-gpt55-cyber-capabilities-evaluation-2026-04-30
## Veille

Evaluation cybersecurite offensive GPT-5.5 par UK AISI — 95 taches CTF, cyber range 32 etapes, jailbreak universel — Blog AISI

## Titre Article

Our evaluation of OpenAI's GPT-5.5 cyber capabilities

## Date

2026-04-30

## URL

https://www.aisi.gov.uk/blog/our-evaluation-of-openais-gpt-5-5-cyber-capabilities

## Keywords

cybersecurite offensive, evaluation modele IA, GPT-5.5, AISI UK, capture-the-flag, cyber range, jailbreak universel, Mythos Preview, Opus 4.7, GPT-5.4, red teaming, safeguards, exploitation vulnerabilites, reverse engineering, cryptographie, autonomie long-horizon, SpecterOps, Crystal Peak Security, The Last Ones

## Authors

AI Safety Institute (AISI UK)

## Ton

**Profil** : Publication institutionnelle d'evaluation technique par l'agence gouvernementale britannique de securite de l'IA, registre technique-neutre, niveau avance.

**Description** : Le ton est celui d'un rapport d'evaluation gouvernemental : factuel, methodique et deliberement neutre. L'AISI presente ses resultats sans sensationnalisme, avec une rigueur statistique (intervalles de confiance, erreurs standard) qui ancre les conclusions dans la reproductibilite scientifique. L'autorite vient du mandat institutionnel — l'AISI est l'organisme officiel britannique charge d'evaluer la securite des modeles d'IA frontiere avant deploiement. Le texte equilibre transparence sur les capacites offensives croissantes et reconnaissance des efforts de mitigation d'OpenAI. Le public cible est triple : decideurs politiques, chercheurs en securite de l'IA, et communaute cybersecurite au sens large.

## Pense-betes

- L'AISI utilise une suite de 95 taches cyber etroites (narrow cyber tasks) au format CTF reparties en 4 niveaux de difficulte (basique, intermediaire, difficile, expert) testant reverse engineering, exploitation web et cryptographie
- Les taches basiques sont saturees (100%) par tous les modeles frontiere depuis au moins fevrier 2026 — la differentiation se fait desormais uniquement sur les taches expert
- Sur les taches expert (pass@1) : GPT-5.5 atteint 71,4% (+-8,0%), Mythos Preview 68,6% (+-8,7%), GPT-5.4 52,4% (+-9,8%), Opus 4.7 48,6% (+-10,0%) — GPT-5.5 est statistiquement comparable a Mythos mais nettement superieur a la generation precedente
- En pass@5 (meilleur sur 5 tentatives), GPT-5.5 obtient 90,5% (+-12,9%) sur les taches expert — le score le plus eleve jamais mesure par l'AISI
- Les taches avancees ont ete construites en collaboration avec Crystal Peak Security et Irregular, firmes specialisees en cybersecurite
- Token limits : 50M tokens par tentative pour les taches etroites, 100M pour les cyber ranges — la performance continue de croitre jusqu'a ces limites
- "The Last Ones" (TLO) : cyber range de 32 etapes simulant une attaque de reseau d'entreprise, construit avec SpecterOps, couvrant 4 sous-reseaux et environ 20 hotes, estime a 20 heures pour un expert humain
- GPT-5.5 a complete TLO de bout en bout dans 2 tentatives sur 10 — deuxieme modele a y parvenir. Mythos Preview (premier modele) l'avait reussi dans 3/10 tentatives
- Decouverte critique en safeguards : un jailbreak universel a ete identifie en 6 heures de red-teaming expert, permettant d'obtenir du contenu offensif sur toutes les requetes cyber malveillantes testees, y compris en mode agentique multi-tours
- OpenAI a mis a jour son stack de safeguards suite a cette decouverte, mais un probleme de configuration a empeche l'AISI de verifier l'efficacite de la version finale
- Conclusion structurante : les capacites cyber offensives emergent comme sous-produit des ameliorations generales en autonomie long-horizon, raisonnement et codage — impliquant des augmentations futures inevitables
- OpenAI a publie GPT-5.5 avec ses "safeguards les plus robustes a ce jour", et a lance un produit GPT-5.5-Cyber a acces restreint pour les professionnels de la cybersecurite defensive

## ResumeDe400mots

Dans cette evaluation pre-deploiement, l'AI Safety Institute du Royaume-Uni (AISI) documente les capacites cyberoffensives de GPT-5.5 d'OpenAI, utilisant sa suite standardisee de 95 taches au format capture-the-flag (CTF) reparties en quatre niveaux de difficulte, ainsi que des simulations d'attaque de bout en bout appelees "cyber ranges".

Sur les taches expert en pass@1, GPT-5.5 atteint un taux de reussite moyen de 71,4% (+-8,0% d'erreur standard), sensiblement equivalent a Mythos Preview d'Anthropic (68,6% +-8,7%) mais nettement superieur a GPT-5.4 (52,4%) et Opus 4.7 (48,6%). En pass@5, GPT-5.5 etablit un record avec 90,5% (+-12,9%), le score le plus eleve jamais mesure par l'AISI. Les taches basiques sont desormais saturees a 100% par tous les modeles frontiere depuis fevrier 2026, rendant seuls les niveaux superieurs discriminants.

L'evaluation inclut egalement "The Last Ones" (TLO), un cyber range de 32 etapes construit avec SpecterOps simulant une intrusion complete de reseau d'entreprise. Cette simulation couvre quatre sous-reseaux et une vingtaine de machines, et necessiterait environ 20 heures a un expert humain. GPT-5.5 a complete la chaine d'attaque de bout en bout dans 2 tentatives sur 10, devenant le deuxieme modele a accomplir cet exploit apres Mythos Preview (3/10). Les evaluations ont ete conduites avec des limites de 50 millions de tokens par tentative pour les taches etroites et 100 millions pour les cyber ranges, la performance continuant de progresser jusqu'a ces plafonds.

Concernant les garde-fous, l'AISI a identifie un jailbreak universel en six heures de red-teaming expert. Cette attaque a permis d'eliciter du contenu offensif sur l'integralite des requetes cyber malveillantes fournies par OpenAI, y compris dans des scenarios agentiques multi-tours. OpenAI a subsequemment mis a jour son stack de safeguards, bien qu'un probleme de configuration ait empeche l'AISI de verifier l'efficacite de la version finale deployee.

L'AISI conclut que la progression rapide des capacites cyber fait partie d'une tendance plus generale : les competences offensives emergent comme sous-produit des ameliorations en autonomie long-horizon, raisonnement et codage. Si cette hypothese est correcte, de nouvelles augmentations de capacites cyberoffensives sont a attendre des prochains modeles frontiere. OpenAI a repondu en deployant GPT-5.5 avec ses safeguards les plus robustes a ce jour et en lancant un produit GPT-5.5-Cyber a acces restreint destine aux professionnels de la cybersecurite defensive.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Predicat | Objet | Type Objet | Confiance | Temporalite | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| AISI UK | ORGANISATION | a_evalue | GPT-5.5 | TECHNOLOGIE | 0.99 | STATIQUE | declare_article |
| GPT-5.5 | TECHNOLOGIE | atteint | 71,4% pass@1 expert | CONCEPT | 0.97 | STATIQUE | declare_article |
| GPT-5.5 | TECHNOLOGIE | egale_statistiquement | Mythos Preview | TECHNOLOGIE | 0.92 | STATIQUE | declare_article |
| GPT-5.5 | TECHNOLOGIE | surpasse | GPT-5.4 | TECHNOLOGIE | 0.97 | STATIQUE | declare_article |
| GPT-5.5 | TECHNOLOGIE | surpasse | Opus 4.7 | TECHNOLOGIE | 0.95 | STATIQUE | declare_article |
| GPT-5.5 | TECHNOLOGIE | a_complete | The Last Ones (TLO) | EVENEMENT | 0.95 | STATIQUE | declare_article |
| SpecterOps | ORGANISATION | a_construit | The Last Ones (TLO) | EVENEMENT | 0.90 | STATIQUE | declare_article |
| Crystal Peak Security | ORGANISATION | collabore_avec | AISI UK | ORGANISATION | 0.88 | DYNAMIQUE | declare_article |
| Irregular | ORGANISATION | collabore_avec | AISI UK | ORGANISATION | 0.88 | DYNAMIQUE | declare_article |
| AISI UK | ORGANISATION | a_identifie | jailbreak universel | CONCEPT | 0.97 | STATIQUE | declare_article |
| jailbreak universel | CONCEPT | contourne | safeguards GPT-5.5 | TECHNOLOGIE | 0.95 | STATIQUE | declare_article |
| OpenAI | ORGANISATION | a_deploye | GPT-5.5-Cyber | TECHNOLOGIE | 0.90 | STATIQUE | declare_article |
| capacites cyber offensives | CONCEPT | emergent_de | ameliorations autonomie et raisonnement | CONCEPT | 0.85 | ATEMPOREL | infere |
| AISI UK | ORGANISATION | affirme_que | capacites cyber vont continuer a croitre | CONCEPT | 0.88 | ATEMPOREL | declare_article |

### Entites

| Entite | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| AISI UK | ORGANISATION | role | Institut de securite de l'IA du Royaume-Uni | AJOUT |
| GPT-5.5 | TECHNOLOGIE | score_expert_pass1 | 71,4% (+-8,0%) | AJOUT |
| GPT-5.5 | TECHNOLOGIE | score_expert_pass5 | 90,5% (+-12,9%) | AJOUT |
| Mythos Preview | TECHNOLOGIE | score_expert_pass1 | 68,6% (+-8,7%) | AJOUT |
| GPT-5.4 | TECHNOLOGIE | score_expert_pass1 | 52,4% (+-9,8%) | AJOUT |
| Opus 4.7 | TECHNOLOGIE | score_expert_pass1 | 48,6% (+-10,0%) | AJOUT |
| The Last Ones (TLO) | EVENEMENT | description | Cyber range 32 etapes, 4 sous-reseaux, ~20 hotes | AJOUT |
| SpecterOps | ORGANISATION | secteur | Cybersecurite offensive / Red team | AJOUT |
| Crystal Peak Security | ORGANISATION | secteur | Cybersecurite | AJOUT |
| Irregular | ORGANISATION | secteur | Cybersecurite | AJOUT |
| GPT-5.5-Cyber | TECHNOLOGIE | categorie | Produit IA a acces restreint pour cybersecurite defensive | AJOUT |
| OpenAI | ORGANISATION | secteur | IA / Modeles frontiere | MISE_A_JOUR |
