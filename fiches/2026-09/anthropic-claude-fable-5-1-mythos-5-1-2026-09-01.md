---
themes: [economie-marche, qualite-securite, recherche-education]
source: "Anthropic"
---
# anthropic-claude-fable-5-1-mythos-5-1-2026-09-01

## Veille

Communication produit d'**Anthropic** publiée le **1er septembre 2026** sur anthropic.com (~4 000 mots, six sections, 22 témoignages de partenaires d'accès anticipé). Elle annonce **Claude Fable 5.1** (disponibilité générale) et **Claude Mythos 5.1** (accès vérifié) : *le même modèle, mais avec des niveaux de garde-fous différents*.

Trois apports. **(A) Économique** — le prix des lectures de cache baisse de **75 %** (**0,25 $/M tokens**), entrée et sortie restant à **10 $** et **50 $/M** : **~25 %** de coût en moins sur charge typique, **~45 %** sur charge fortement agentique. **(B) Scientifique** — Mythos 5.1 conçoit des *binders* protéiques avec un taux de succès de **~50 % sur 12 cibles** (contre 10-15 % usuels) et des affinités **10×** supérieures aux meilleures soumissions des compétitions Adaptyv Bio ; Fable 5.1 entraîne un réseau produisant une carte altimétrique d'**un tiers de Vénus** à 2-3 km de résolution depuis les radars **Magellan** ; sept modèles open source de génomique et de protéines sont accélérés jusqu'à **2,5×** par écriture de noyaux GPU, réduisant les coûts GPU de **30-60 %**. **(C) Garde-fous** — les classifieurs cyber déclenchent **60 %** d'interventions en moins par session, Fable 5.1 est désormais autorisé à *identifier* des vulnérabilités logicielles sans en développer les exploits, et les **Enterprise Frontier Safeguards** stockent les données chez le client ; pentest, génération d'exploits et scan binaire restent redirigés vers les modèles Opus.

Anthropic borne son propre audit d'alignement : couverture moindre du très long contexte, du multi-agent et des tâches impossibles. La topologie à deux niveaux prolonge celle de [[anthropic-claude-fable-5-mythos-5-2026-06-09]].

## Titre Article

Claude Fable 5.1 and Mythos 5.1

## Date

2026-09-01

## URL

https://www.anthropic.com/claude-fable-and-mythos-5-1

## Keywords

Claude Fable 5.1, Claude Mythos 5.1, modèle de fondation, lectures de cache, prix du cache, coût agentique, niveaux d'effort, Terminal-Bench-Science, Terminal-Bench 4.0, GDPval-AA, OSWorld 2.0, CursorBench, AutomationBench, Humanity's Last Exam, design de protéines, binders haute affinité, Adaptyv Bio, carte altimétrique de Vénus, Magellan, noyaux GPU, génomique, Evo 2, Enterprise Frontier Safeguards, zéro rétention de données, garde-fous cyber, faux positifs, identification de vulnérabilités, anti-distillation, Cyber Verification Program, Life Sciences Verification Program, EU AI Act, watermark, API de détection, Responsible Scaling Policy, Frontier Compliance Framework

## Authors

Anthropic — communication produit publiée sur anthropic.com, sans signature individuelle.

## Ton

Profil : communication corporate d'un laboratoire d'IA à la première personne du pluriel, registre technique-promotionnel discipliné, public cible développeurs, décideurs techniques et chercheurs. Trois traits distinguent ce texte de l'annonce produit standard. D'abord, la **réponse explicite aux critiques** : l'introduction énumère prix, rétention de données et garde-fous comme des retours clients auxquels la version répond, ce qui inscrit l'annonce dans une conversation plutôt que dans une proclamation. Ensuite, la **discipline métrologique** : les scores sont donnés en courbes coût/précision à cinq niveaux d'effort plutôt qu'en points isolés, les erreurs types sont publiées (±3,5-4,5 pts sur Terminal-Bench-Science), les écarts avec le classement public sont signalés et attribués au bruit, et une note précise que les garde-fous en production ont fait scorer zéro sur certaines tâches — donc que les chiffres publiés sous-estiment le modèle. Enfin, l'**auto-limitation** : la section alignement liste ce que l'audit ne couvre pas (très long contexte, multi-agent, tâches impossibles) et reconnaît que le modèle peut encore contourner approbations et classifieurs. Les 22 témoignages partenaires assurent la charge promotionnelle, chacun ancré sur un benchmark interne nommé et chiffré. La rhétorique dominante n'est pas la puissance brute mais la **précision** : garde-fous plus fins, coûts mieux ciblés, mesures mieux bornées.

## Pense-betes

- **Fable 5.1 et Mythos 5.1 sont le même modèle** : seuls les garde-fous diffèrent. Fable est en disponibilité générale ; Mythos passe par les programmes d'accès vérifié (CVP cyberdéfense, LSVP sciences du vivant, ce dernier monté avec le gouvernement américain).
- **La baisse de prix ne touche que le cache** : lectures de cache **−75 %** à **0,25 $/M tokens**. Entrée (**10 $/M**) et sortie (**50 $/M**) sont inchangées. Le gain réel dépend donc de la part du cache dans la charge — **~25 %** en typique, **~45 %** en fortement agentique. Un usage sans cache ne gagne rien.
- **Niveaux d'effort par défaut** : `high` dans [[claxton-anthropic-ai-native-sdlc-playbook-2026-08-21]] et Claude Code, `medium` dans Claude Cowork et sur claude.ai. À effort `low`/`medium`, Fable 5.1 égale ou dépasse Fable 5 à coût nettement inférieur — le levier d'économie le plus direct.
- **Benchmarks** : Terminal-Bench-Science 0.1 **52,6 %** (vs 24,7 % Fable 5, 29,0 % Opus 5, 22,4 % GPT-5.6 Sol) ; Terminal-Bench 4.0 **55,8 %** Fable / **60,9 %** Mythos ; GDPval-AA v2 **1853** ; CursorBench 3.2.0 **73,4 %** ; AutomationBench **31,4 %** (vs 17,1 %) ; HLE **60,9 %** sans outils.
- **L'écart Fable/Mythos sur Terminal-Bench mesure les garde-fous, pas la capacité** — Anthropic annonce que les nouveaux classifieurs devraient le réduire fortement.
- **Enterprise Frontier Safeguards (EFS)** : les données restent sur l'infrastructure cloud du client, la revue humaine est faite par le client. Déploiement progressif à partir de l'automne 2026 sur Claude Code, Claude Enterprise, la plateforme, Bedrock, Google Agent Platform et Microsoft Foundry. En attendant, zéro rétention pour les clients éligibles. Construit avec 100+ clients et les trois hyperscalers.
- **Ouverture cyber** : Fable 5.1 peut identifier des vulnérabilités, pas générer d'exploits. Restent redirigés vers Opus : pentest, génération d'exploits, scan de vulnérabilités sur binaire. Les garde-fous biologie se déclenchent **85 % moins** sur les questions médicales bénignes.
- **Anti-distillation** : les comptes API créés à partir du 1er septembre 2026 ne peuvent plus éditer manuellement le contexte antérieur de Claude en conservant la trace de son raisonnement. Les comptes existants sont épargnés pour l'instant, mais la règle s'appliquera à tous aux prochaines releases — à vérifier si une intégration custom dépend de ce mécanisme.
- **Conformité EU AI Act** : watermark numérique sur les sorties des modèles publiés après le 2 août 2026, invisible sans l'API de détection, sans information sur l'utilisateur. API de détection en préversion privée pour régulateurs, médias, chercheurs et entreprises soumises à la même obligation.
- **Science** : hit rate **~50 %** sur 12 cibles protéiques (10-15 % usuels), affinités **10×** meilleures sur trois cibles (EGFR, Nipah G, 15-PGDH) ; carte de Vénus publiée en Creative Commons avant les missions NASA VERITAS et ESA EnVision ; optimisations GPU annoncées comme prochainement open source.
- **Limites assumées de l'audit d'alignement** : peu de visibilité sur le travail très long contexte et le multi-agent, couverture insuffisante des tâches impossibles — précisément le terrain que documente [[mollick-agency-and-agents-twilight-factory-2026-08-31]].

## RésuméDe400mots

Le **1er septembre 2026**, Anthropic annonce **Claude Fable 5.1** et **Claude Mythos 5.1**, présentés comme les modèles les plus avancés pour le codage et le travail de connaissance. Les deux sont **le même modèle sous-jacent** ; seuls diffèrent les niveaux de garde-fous. Fable 5.1 est en disponibilité générale ; Mythos 5.1 n'est accessible que via des programmes d'accès de confiance, avec des garde-fous conçus pour la cybersécurité et les sciences du vivant.

L'annonce répond explicitement à trois retours clients. **Prix** : les lectures de cache baissent de 75 % à 0,25 $ par million de tokens, entrée et sortie restant à 10 $ et 50 $ ; le coût total baisse d'environ 25 % sur charge typique et jusqu'à 45 % sur charge fortement agentique. **Rétention de données** : les nouveaux *Enterprise Frontier Safeguards* stockent les données sur l'infrastructure du client, offrant la confidentialité d'un accord de rétention zéro tout en préservant la détection d'usages adverses ; déploiement par phases à partir de l'automne. **Garde-fous** : les classifieurs cyber produisent 60 % de faux positifs en moins, et Fable 5.1 est désormais autorisé à découvrir des vulnérabilités logicielles — sans développer d'exploits.

Sur les performances, Fable 5.1 atteint 52,6 % sur Terminal-Bench-Science 0.1 (contre 24,7 % pour Fable 5 et 29,0 % pour Opus 5), 55,8 % sur Terminal-Bench 4.0 (60,9 % pour Mythos 5.1), 1853 sur GDPval-AA v2, 73,4 % sur CursorBench 3.2.0 et 31,4 % sur AutomationBench. Les résultats sont présentés en courbes coût/précision à cinq niveaux d'effort ; à effort faible ou moyen, le modèle égale ou dépasse Fable 5 pour un coût bien moindre. Vingt-deux partenaires témoignent, dont Millennium, chez qui le modèle a diagnostiqué un crash survenant une fois sur un million que personne n'avait expliqué en quatre à cinq ans.

La section scientifique documente trois résultats. En **design moléculaire**, Mythos 5.1 atteint un taux de réussite de près de 50 % sur 12 cibles protéiques, avec des affinités dix fois supérieures aux meilleures soumissions d'Adaptyv Bio. En **modélisation**, Fable 5.1 a produit une carte altimétrique d'un tiers de Vénus à partir des radars Magellan, publiée sous licence Creative Commons. En **biologie computationnelle**, Mythos 5.1 a accéléré sept modèles open source jusqu'à 2,5× en écrivant des noyaux GPU, réduisant les coûts de 30 à 60 %.

Côté sûreté, Mythos 5.1 reste sous le palier de risque suivant de la Responsible Scaling Policy en biologie et dans la catégorie basse du Frontier Compliance Framework en cyber. L'audit d'alignement le trouve mieux aligné que Mythos 5, tout en reconnaissant une couverture limitée sur le long contexte, le multi-agent et les tâches impossibles.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Anthropic | ORGANISATION | publie | Claude Fable 5.1 | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Mythos 5.1 | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | est_variante_de | Claude Mythos 5.1 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | remplace | Claude Fable 5 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | remplace | Claude Mythos 5 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | utilise | Enterprise Frontier Safeguards | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Enterprise Frontier Safeguards | TECHNOLOGIE | permet | zéro rétention de données | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | réduit | coût des lectures de cache de 75 %, à 0,25 $/M tokens | MESURE | 0.96 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | réduit | coût total de ~25 % en charge typique et ~45 % en charge agentique | MESURE | 0.94 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | mesure | 52,6 % sur Terminal-Bench-Science 0.1 | MESURE | 0.95 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | mesure | 73,4 % sur CursorBench 3.2.0 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | mesure | 60,9 % sur Terminal-Bench 4.0 | MESURE | 0.93 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | surpasse | Claude Opus 5 | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | surpasse | GPT-5.6 Sol | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | permet | identification de vulnérabilités logicielles | CONCEPT | 0.93 | DYNAMIQUE | déclaré_article |
| garde-fous cyber | TECHNOLOGIE | réduit | 60 % d'interventions en moins par session dans Claude Code | MESURE | 0.92 | STATIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | mesure | taux de réussite de ~50 % sur 12 cibles de design de binders | MESURE | 0.90 | STATIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | surpasse | soumissions des compétitions Adaptyv Bio | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | a_créé | carte altimétrique de Vénus | DOCUMENT | 0.91 | STATIQUE | déclaré_article |
| carte altimétrique de Vénus | DOCUMENT | est_basé_sur | mission Magellan | EVENEMENT | 0.90 | STATIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | améliore | accélération jusqu'à 2,5× de sept modèles de deep learning | MESURE | 0.90 | STATIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | réduit | coûts GPU de 30-60 % sur analyses pangénomiques | MESURE | 0.88 | STATIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | fait_partie_de | Cyber Verification Program | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| Claude Mythos 5.1 | TECHNOLOGIE | fait_partie_de | Life Sciences Verification Program | CONCEPT | 0.90 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | collabore_avec | gouvernement américain | ORGANISATION | 0.90 | DYNAMIQUE | déclaré_article |
| Claude Security | TECHNOLOGIE | utilise | Claude Mythos 5.1 | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | Mythos 5.1 reste sous le palier de risque suivant de la Responsible Scaling Policy | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | l'audit d'alignement couvre mal le long contexte, le multi-agent et les tâches impossibles | AFFIRMATION | 0.90 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | utilise | mécanismes anti-distillation | TECHNOLOGIE | 0.91 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | utilise | watermark de contenu généré | TECHNOLOGIE | 0.90 | DYNAMIQUE | déclaré_article |
| watermark de contenu généré | TECHNOLOGIE | s_applique_à | EU AI Act | DOCUMENT | 0.92 | DYNAMIQUE | déclaré_article |
| Millennium | ORGANISATION | affirme_que | Fable 5.1 a diagnostiqué un crash inexpliqué depuis quatre à cinq ans | AFFIRMATION | 0.90 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Claude Fable 5.1 | TECHNOLOGIE | catégorie | Modèle de fondation, disponibilité générale, identifiant API claude-fable-5-1 | AJOUT |
| Claude Fable 5.1 | TECHNOLOGIE | tarification | 10 $/M entrée, 50 $/M sortie, 0,25 $/M lectures de cache | AJOUT |
| Claude Mythos 5.1 | TECHNOLOGIE | catégorie | Même modèle que Fable 5.1, garde-fous permissifs, accès vérifié | AJOUT |
| Claude Fable 5 | TECHNOLOGIE | statut | Remplacé par Fable 5.1 ; sert de référence de comparaison des benchmarks et des coûts | AJOUT |
| Claude Mythos 5 | TECHNOLOGIE | statut | Remplacé par Mythos 5.1 | AJOUT |
| Enterprise Frontier Safeguards | TECHNOLOGIE | nature | Données stockées sur le cloud du client, revue humaine côté client | AJOUT |
| Cyber Verification Program | CONCEPT | nature | Programme d'accès vérifié pour la cyberdéfense | AJOUT |
| Life Sciences Verification Program | CONCEPT | nature | Programme d'accès vérifié sciences du vivant, monté avec le gouvernement US | AJOUT |
| carte altimétrique de Vénus | DOCUMENT | statut | Publiée en Creative Commons, résolution 2-3 km sur un tiers de la planète | AJOUT |
| mécanismes anti-distillation | TECHNOLOGIE | portée | Édition du contexte antérieur bloquée pour les comptes API créés à partir du 2026-09-01 | AJOUT |
| watermark de contenu généré | TECHNOLOGIE | portée | Modèles publiés après le 2026-08-02, API de détection en préversion privée | AJOUT |
| Claude Security | TECHNOLOGIE | rôle | Scan de vulnérabilités et suggestion de correctifs, propulsé par Mythos 5.1 | AJOUT |
| Claude Opus 5 | TECHNOLOGIE | rôle | Modèle de repli pour les tâches cyber et biologie redirigées | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| Millennium | ORGANISATION | rôle | Partenaire d'accès anticipé, diagnostic d'un crash rare | AJOUT |
