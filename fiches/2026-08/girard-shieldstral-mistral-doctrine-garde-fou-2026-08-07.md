---
themes: [qualite-securite, politique-regulation, outils-plateformes]
source: "Didier Girard (X)"
---
# girard-shieldstral-mistral-doctrine-garde-fou-2026-08-07

## Veille

Note de veille de **Didier Girard** publiée sur **X** le **7 août 2026**, qui lit le lancement de **Shieldstral 1.0 3B** (Mistral AI, 4 août 2026) non comme une sortie produit mais comme **la mise en production d'une doctrine**. Point de départ : le **13 mai 2026**, devant la commission d'enquête de l'Assemblée nationale sur les vulnérabilités numériques, **Arthur Mensch** refusait tout droit de regard de Mistral sur l'usage final de ses modèles — *« nous n'avons pas la légitimité démocratique »* — en écartant explicitement la posture d'**Anthropic**. Moins de trois mois plus tard, Mistral publie un **modèle de modération**. L'auteur écarte la contradiction apparente : **Shieldstral ne porte aucune taxonomie du licite et de l'illicite**, il répond à une **question que l'utilisateur écrit**. **Le mécanisme est le cœur de la note** : un prompt en trois parties (contexte + sévérité / une seule question fermée / le contenu à juger), une réponse `yes` ou `no`, et la **softmax sur ces deux tokens** produit un score continu entre 0 et 1. **La politique de modération n'est pas dans les poids, elle est lue à l'inférence** — là où **Llama Guard 4** embarque la taxonomie MLCommons figée à l'entraînement, Shieldstral lit la vôtre en langage naturel, modifiable **sans réentraînement**. Le rapport technique (**arXiv:2607.25857**, 28 juillet 2026) chiffre le coût de ce choix : fine-tuning sur données publiques seules = **61,1 % de F1** en adaptabilité aux politiques ; **4,4 millions de paires contrastives** générées par LLM (même contenu réécrit pour violer une politique mais pas sa politique sœur) = **+23,3 points** ; **91,3 %** après fusion de trois checkpoints. Caractéristiques : **3,8 Md de paramètres réels** (le « 3B » du nom arrondit vers le bas), base **Ministral 3** + encodeur vision **Pixtral**, **12 langues**, **16 Go de VRAM en BF16**, **Apache 2.0**. Performance texte : **84,9 % de F1 moyen**, à égalité avec **GPT-OSS-Safeguard-20B** (sept fois plus gros), devant **Qwen3Guard-8B** (84,0) et loin devant **LlamaGuard-4-12B** (69,1). **Réserve posée par l'auteur lui-même** : *tous ces chiffres viennent de Mistral, sur des jeux de test que Mistral a sélectionnés, et aucune évaluation tierce n'existait au 6 août*. La thèse structurante est une **opposition de topologies** : chez **Anthropic**, le garde-fou vit **dans les poids** et l'éditeur arbitre qui y échappe (**Claude Fable 5** public avec mesures de sécurité / **Claude Mythos 5** sans, réservé aux cyberdéfenseurs approuvés du **Project Glasswing**, 9 juin 2026) ; chez **Mistral**, le garde-fou **sort du modèle** — composant séparé, ouvert, auto-hébergeable, dont la politique appartient au déployeur. Alignement client explicite (ministère des Armées, BNP Paribas, administrations françaises et luxembourgeoise). La note se termine sur un **revers en trois points documentés** : **auditabilité** (sortie binaire, aucune trace de raisonnement, alors que le déployeur hérite de la charge de justification en audit AI Act), **robustesse** (le premier chapitre du *Traité sur la tolérance* de Voltaire classé « appelle à la violence » par un testeur du fil Hacker News — confusion mention/adhésion), **disponibilité** (au 6 août : pas d'endpoint facturé sur La Plateforme, pas d'Ollama officiel). Trois règles de déploiement en clôture.

## Titre Article

Shieldstral : Mistral compile sa doctrine en 3,8 milliards de paramètres

## Date

2026-08-07

## URL

https://x.com/DidierGirard/status/2085622329720066233

## Keywords

Shieldstral, Shieldstral 1.0 3B, Mistral AI, Arthur Mensch, modèle de modération, classificateur de sécurité, classificateur multimodal, poids ouverts, open-weights, Apache 2.0, auto-hébergement, souveraineté, politique de modération, taxonomie de modération, politique à l'inférence, adaptabilité aux politiques, prompt en trois parties, question fermée, yes/no, softmax sur deux tokens, score continu, calibration de seuils, seuil 0,5, revue humaine, Llama Guard 4, LlamaGuard-4-12B, MLCommons, GPT-OSS-Safeguard-20B, Qwen3Guard-8B, F1, paires contrastives, données synthétiques, fusion de checkpoints, model merging, arXiv, rapport technique, Ministral 3, Pixtral, encodeur vision, 12 langues, 16 Go de VRAM, BF16, 3,8 milliards de paramètres, Anthropic, Claude Fable 5, Claude Mythos 5, Project Glasswing, garde-fou dans les poids, topologie du garde-fou, transfert de responsabilité, auditabilité, trace de raisonnement, AI Act, centre juridique, ministère des Armées, BNP Paribas, administration luxembourgeoise, SFEIR, Mistral-Microsoft, propriété d'architecture, faux positif, mention vs adhésion, Voltaire, Traité sur la tolérance, Hacker News, entrées obscurcies, arabe, indonésien, La Plateforme, Ollama, quantifications communautaires, checksum, injection de prompt, journalisation, The Decoder, Jonathan Kemper

## Authors

**Didier Girard** — auteur de la note, publiée sur son compte X. Écrit ici en **analyste de doctrine industrielle** plutôt qu'en testeur : il n'a pas déployé le modèle, il croise une **audition parlementaire** (Mensch, 13 mai), un **lancement produit** (Shieldstral, 4 août), un **rapport technique** (arXiv, 28 juillet) et un **contre-exemple concurrent** (Anthropic, 9 juin) pour montrer qu'ils forment une position cohérente. Deux marqueurs de posture : il **borne explicitement la valeur des chiffres** qu'il cite (aucune évaluation tierce) et il **termine par des règles opérationnelles** — l'analyse doit sortir avec sa traduction en décisions de déploiement.

Sources mobilisées et créditées dans le texte : **Mistral AI** (annonce, model card Hugging Face, docs) ; **Calvi, Sooriyarachchi, Pistilli, Lample et al.** (rapport technique arXiv:2607.25857) ; **Jonathan Kemper** (*The Decoder*, 5 août) ; le fil **Hacker News** du 4 août (471 points) ; l'audition d'**Arthur Mensch** ; l'annonce **Anthropic** du 9 juin ; l'analyse **SFEIR** de l'accord Mistral-Microsoft du 22 juillet.

## Ton

**Profil** : note d'analyse stratégique adossée à une lecture technique, format court et dense, publiée en fil. Ni compte rendu de lancement ni benchmark : une **démonstration de cohérence doctrinale**, suivie d'un audit des manques.

**Style** : structure en **quatre mouvements** — le paradoxe apparent (Mensch refuse d'arbitrer / Mistral publie un modérateur) → le mécanisme qui le dissout (la politique s'écrit à l'inférence) → l'opposition de topologies (Anthropic vs Mistral) → le revers (la responsabilité arrive sans son outillage). Trois traits :

1. **L'ouverture par la contradiction apparente**, immédiatement désamorcée. Le texte pose un problème avant d'exposer un produit : c'est ce qui transforme un lancement en objet d'analyse.
2. **La réserve d'usage assumée à la première personne** — *« Je pose la réserve d'usage »*. Les chiffres sont cités **puis** relativisés dans le même paragraphe, sans les retirer de l'argument. Registre honnête plutôt que promotionnel.
3. **La symétrie du dernier tiers**. Après avoir défendu la cohérence du choix, l'auteur consacre autant de place à ce qui manque — auditabilité, robustesse, disponibilité — chacune illustrée par un fait vérifiable et non par une opinion.

**Formules-marqueurs** : *« Mistral compile sa doctrine en 3,8 milliards de paramètres »*, *« il répond à une question que vous écrivez »*, *« la politique de modération n'est pas apprise, elle sort des poids »*, *« deux endroits où loger le garde-fou »*, *« la responsabilité arrive sans son outillage »*, *« Mistral ne décidera pas ce qui est acceptable, il propose l'outil pour que vous le décidiez »*, *« Apache 2.0, 16 Go de VRAM, et la responsabilité livrée avec les poids »*.

**Position épistémique** : **favorable au choix architectural, sceptique sur son outillage**. L'auteur valide la cohérence doctrinale (« j'y vois la vraie cohérence du lancement ») tout en refusant les chiffres du constructeur comme preuve et en listant trois manques opérationnels. Le sourçage est dense pour un post social : sept sources créditées, dates précises, numéro d'arXiv.

## Pense-betes

- **L'idée centrale, à retenir seule** : la question n'est pas *« quel modèle modère le mieux ? »* mais ***« où loge le garde-fou ? »***. Deux réponses opposées, données à deux mois d'écart par deux éditeurs :
  | | **Anthropic** (9 juin 2026) | **Mistral** (4 août 2026) |
  |---|---|---|
  | Emplacement | **dans les poids** du modèle | **à côté** du modèle, composant séparé |
  | Qui définit la politique | l'éditeur | **le déployeur** |
  | Qui échappe au garde-fou | ceux que l'éditeur approuve (Project Glasswing) | question sans objet |
  | Modèle de distribution | Fable 5 public / Mythos 5 restreint | poids ouverts Apache 2.0 |
  → Ce n'est pas un désaccord technique, c'est un désaccord sur **qui a la légitimité d'arbitrer le licite**. Voir [[anthropic-claude-fable-5-mythos-5-2026-06-09]] pour le camp opposé et [[mensch-mistral-commission-enquete-vulnerabilites-numeriques-souverainete-ia-2026-05-13]] pour la position de Mensch en amont.

- **Le mécanisme, en trois lignes** : prompt = (1) contexte + niveau de sévérité, (2) **une seule question fermée** (« ce contenu appelle-t-il à la violence ? »), (3) le contenu à juger. Sortie = `yes` / `no`, et la **softmax sur ces deux tokens seulement** donne un **score continu entre 0 et 1**. Conséquence pratique : on obtient un scalaire seuillable, pas un verdict binaire — c'est ce qui rend la calibration possible (voir ci-dessous).

- **Ce qui est réellement nouveau** : la **politique n'est pas apprise**. Llama Guard 4 embarque la taxonomie MLCommons **figée à l'entraînement** ; Shieldstral lit la vôtre **en langage naturel à l'inférence**, et vous la changez **sans réentraîner**. Le modèle n'apprend pas *ce qui est interdit*, il apprend *à appliquer une règle qu'on lui donne*.

- **Le chiffre qui explique le reste** — l'adaptabilité ne vient pas de l'architecture mais des **données fabriquées pour l'enseigner** :
  | Étape | F1 « adaptabilité aux politiques » |
  |---|---|
  | Fine-tuning sur jeux publics seuls | **61,1 %** |
  | + 4,4 M de **paires contrastives** générées par LLM | **+23,3 pts** |
  | + fusion de trois checkpoints | **91,3 %** |
  → La **paire contrastive** est le vrai objet à retenir : *un même contenu réécrit pour violer une politique mais pas sa politique sœur*. C'est le seul signal qui force le modèle à lire la question plutôt qu'à reconnaître un thème. **Pattern transférable** à tout classificateur pilotable par consigne.

- **La fiche technique, pour décider si ça tourne chez vous** : **3,8 Md de paramètres réels** (le « 3B » arrondit vers le bas), base **Ministral 3** + encodeur vision **Pixtral** (donc **multimodal** : texte et image), **12 langues**, **16 Go de VRAM en BF16**, **Apache 2.0**. C'est la classe « une carte grand public » — le dimensionnement fait partie de l'argument politique, pas seulement du produit.

- **Les benchmarks, avec leur réserve** : 84,9 % de F1 moyen texte, à égalité avec **GPT-OSS-Safeguard-20B** (×7 en taille), devant **Qwen3Guard-8B** (84,0), loin devant **LlamaGuard-4-12B** (69,1). **Tous ces chiffres viennent de Mistral, sur des jeux de test choisis par Mistral, sans évaluation tierce au 6 août 2026.** L'auteur pose lui-même la réserve — ne pas la perdre en citant le résultat.

- **Les trois règles de déploiement — le livrable actionnable de la note** :
  1. **Calibrer deux seuils** sur un jeu étiqueté **maison**, au lieu d'accepter le 0,5 par défaut : auto-approbation sous le premier, auto-rejet au-dessus du second, **revue humaine entre les deux**. (Le score continu existe pour ça.)
  2. **Journaliser la question de politique active à chaque décision** — c'est elle qui tiendra lieu de justification en audit, puisque le modèle n'en produit aucune.
  3. **Tester le couple mention/adhésion et vos langues réelles** avant mise en production.
  → Et une quatrième, séparée : **garder un détecteur dédié à l'injection de prompt**. *Shieldstral filtre du contenu, il ne protège pas un agent contre un document piégé.* Distinction à ne pas laisser s'effacer — cf. [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] et [[sfeir-anthropic-sdlc-ai-native-securise-2026-07-26]].

- **Le test Voltaire — le contre-exemple à citer** : sur le fil Hacker News, un utilisateur soumet le **premier chapitre du *Traité sur la tolérance*** avec la question « ce texte prône-t-il la violence contre un groupe protégé ? ». Réponse : **oui**. Le classificateur **confond mentionner la violence et y appeler** — le faux positif canonique du genre, obtenu sur l'un des textes fondateurs de la tolérance. Mistral reconnaît par ailleurs des faiblesses sur les **entrées obscurcies**, les **documents longs**, l'**arabe** et l'**indonésien**.

- **Le trou d'auditabilité, à évaluer avant tout usage réglementé** : la sortie est `yes`/`no` + un score, **aucune trace de raisonnement**. Or le déployeur hérite de la taxonomie, de la calibration **et** de la charge de justifier chaque décision en audit AI Act — **avec un score sec pour tout justificatif**. C'est le prix exact de la topologie « garde-fou hors du modèle » : la responsabilité est transférée, l'outillage de la responsabilité ne l'est pas.

- **La disponibilité au 6 août 2026 (état daté, à revérifier)** : pas d'endpoint facturé sur **La Plateforme**, pas d'entrée **Ollama** officielle, des **quantifications communautaires** publiées en 48 h qu'il faut vérifier au checksum. **L'auto-hébergement est la seule voie sérieuse** — cohérent avec le produit, mais l'usage est de fait réservé aux équipes qui savent héberger un modèle.

- **La lecture souveraineté** : un filtre qui tourne **sur site**, dont **la politique reste sur site**, documenté au regard de l'**AI Act** — c'est une case que les offres américaines laissent vide pour les clients que Mensch listait en audition (**ministère des Armées, BNP Paribas**, administrations **françaises** et **luxembourgeoise**). Se raccorde directement à la thèse de sfeir-mistral-microsoft-souverainete-strategie-industrielle-2026-07-22 : **la souveraineté se qualifie dépendance par dépendance, en propriété d'architecture** — un garde-fou open-weights *est* ce genre de propriété. À rapprocher aussi de mozilla-state-of-open-source-ai-2026-07 et deanwball-open-weights-decelerationnistes-kimi-2026-07-17 sur la place des poids ouverts dans le débat sûreté.

- **Méta / la phrase à garder** : *« Mistral ne décidera pas ce qui est acceptable, il propose l'outil pour que vous le décidiez. »* C'est la doctrine, en une ligne — et la note montre qu'elle a un coût, pas seulement une vertu.

## RésuméDe400mots

Note de veille du **7 août 2026** qui lit **Shieldstral 1.0 3B** — le classificateur de sécurité multimodal publié par **Mistral AI** le 4 août sous **Apache 2.0** — comme la traduction en produit d'une position politique.

**Le paradoxe de départ.** Le 13 mai 2026, devant la commission d'enquête de l'Assemblée nationale sur les vulnérabilités numériques, **Arthur Mensch** refusait tout droit de regard de Mistral sur l'usage final de ses modèles : *« nous n'avons pas la légitimité démocratique »*, en écartant au passage la posture d'**Anthropic**. Moins de trois mois plus tard, Mistral publie un modèle de modération. L'auteur dissout la contradiction : **Shieldstral ne porte aucune taxonomie du licite et de l'illicite** — il répond à une question que le déployeur écrit.

**Le mécanisme.** Le prompt tient en trois parties : contexte et sévérité, **une seule question fermée**, le contenu à juger. Le modèle répond `yes` ou `no` et la **softmax sur ces deux tokens** donne un score continu. **La politique n'est donc pas apprise** : là où **Llama Guard 4** embarque la taxonomie MLCommons figée à l'entraînement, Shieldstral lit la vôtre en langage naturel **à l'inférence**, modifiable sans réentraînement. Le rapport technique (arXiv, 28 juillet) chiffre ce choix : **61,1 %** de F1 en adaptabilité avec les seuls jeux publics, **+23,3 points** grâce à **4,4 millions de paires contrastives** générées par LLM, **91,3 %** après fusion de trois checkpoints. L'objet est calibré pour tourner sur site : **3,8 Md de paramètres**, base **Ministral 3** et encodeur vision **Pixtral**, **12 langues**, **16 Go de VRAM**. Sur le texte, **84,9 %** de F1 moyen — à égalité avec **GPT-OSS-Safeguard-20B**, sept fois plus gros. Réserve posée par l'auteur : **chiffres du constructeur, jeux de test du constructeur, aucune évaluation tierce**.

**La thèse.** Deux endroits où loger le garde-fou. Chez **Anthropic** (9 juin), il vit **dans les poids** et l'éditeur arbitre qui y échappe — **Claude Fable 5** public, **Claude Mythos 5** réservé aux cyberdéfenseurs du **Project Glasswing**. Chez Mistral, il **sort du modèle** : composant séparé, ouvert, auto-hébergeable. Choix aligné sur des clients régaliens et bancaires, et sur une souveraineté qui se qualifie **dépendance par dépendance**.

**Le revers.** Trois manques documentés : **auditabilité** (sortie binaire, aucune trace de raisonnement, alors que le déployeur porte la justification en audit AI Act), **robustesse** (le *Traité sur la tolérance* de Voltaire classé « appelle à la violence » — confusion mention/adhésion), **disponibilité** (ni endpoint facturé ni Ollama officiel au 6 août). D'où trois règles : calibrer **deux** seuils sur un jeu maison, **journaliser la question de politique active**, tester mention/adhésion et vos langues — et garder un détecteur d'**injection de prompt** à part. *« Apache 2.0, 16 Go de VRAM, et la responsabilité livrée avec les poids. »*

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Mistral AI | ORGANISATION | publie | Shieldstral | TECHNOLOGIE | 0.98 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | Shieldstral met en production la doctrine défendue par Arthur Mensch devant la commission d'enquête de l'Assemblée nationale | AFFIRMATION | 0.96 | DYNAMIQUE | déclaré_article |
| Arthur Mensch | PERSONNE | affirme_que | un éditeur de modèles n'a pas la légitimité démocratique pour arbitrer l'usage final de ses modèles | CITATION | 0.96 | DYNAMIQUE | déclaré_article |
| Shieldstral | TECHNOLOGIE | permet | de lire une politique de modération en langage naturel au moment de l'inférence, sans réentraînement | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Shieldstral | TECHNOLOGIE | utilise | une softmax sur les deux tokens yes et no pour produire un score continu entre 0 et 1 | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Shieldstral | TECHNOLOGIE | est_basé_sur | Ministral 3 | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| Shieldstral | TECHNOLOGIE | utilise | Pixtral | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Shieldstral | TECHNOLOGIE | s_oppose_à | Llama Guard 4 | TECHNOLOGIE | 0.92 | ATEMPOREL | déclaré_article |
| Llama Guard 4 | TECHNOLOGIE | utilise | une taxonomie MLCommons figée à l'entraînement | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Mistral AI | ORGANISATION | mesure | 91,3 % de F1 en adaptabilité aux politiques, contre 61,1 % pour un fine-tuning sur jeux de données publics seuls | MESURE | 0.93 | STATIQUE | déclaré_article |
| paire contrastive | CONCEPT | améliore | l'adaptabilité d'un classificateur à une politique fournie à l'inférence, de 23,3 points de F1 | MESURE | 0.91 | ATEMPOREL | déclaré_article |
| Shieldstral | TECHNOLOGIE | surpasse | Qwen3Guard | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Shieldstral | TECHNOLOGIE | mesure | 84,9 % de F1 moyen sur le texte, à égalité avec GPT-OSS-Safeguard-20B pourtant sept fois plus gros | MESURE | 0.88 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | tous les chiffres publiés viennent de Mistral, sur des jeux de test sélectionnés par Mistral, sans aucune évaluation tierce au 6 août 2026 | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | Claude Mythos 5 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | s_oppose_à | l'idée que le déployeur définisse lui-même la politique de sûreté, en logeant le garde-fou dans les poids et en arbitrant qui y échappe | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| topologie du garde-fou | CONCEPT | s_applique_à | le choix d'architecture entre une sûreté logée dans les poids et une sûreté déportée dans un composant séparé | AFFIRMATION | 0.92 | ATEMPOREL | inféré |
| Shieldstral | TECHNOLOGIE | permet | un filtre de modération auto-hébergeable dont la politique reste sur site, documenté au regard de l'AI Act | AFFIRMATION | 0.91 | DYNAMIQUE | déclaré_article |
| Shieldstral | TECHNOLOGIE | s_applique_à | des secteurs régaliens et régulés : ministère des Armées, BNP Paribas, administrations françaises et luxembourgeoise | AFFIRMATION | 0.86 | DYNAMIQUE | inféré |
| Didier Girard | PERSONNE | affirme_que | le transfert de responsabilité vers le déployeur arrive sans son outillage : auditabilité, robustesse et disponibilité manquent | AFFIRMATION | 0.95 | DYNAMIQUE | déclaré_article |
| Shieldstral | TECHNOLOGIE | s_oppose_à | l'auditabilité d'une décision de modération, en ne produisant aucune trace de raisonnement | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Shieldstral | TECHNOLOGIE | observé_dans | un faux positif sur le premier chapitre du Traité sur la tolérance de Voltaire, classé comme appelant à la violence | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | recommande | calibrer deux seuils sur un jeu étiqueté maison — auto-approbation, revue humaine, auto-rejet — plutôt que d'accepter le 0,5 par défaut | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | journaliser la question de politique active à chaque décision, puisqu'elle tiendra lieu de justification en audit | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | Shieldstral filtre du contenu et ne protège pas un agent contre un document piégé : garder un détecteur dédié à l'injection de prompt | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Jonathan Kemper | PERSONNE | mesure | Shieldstral égale des modèles de sûreté bien plus gros sur le texte | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Shieldstral | TECHNOLOGIE | définition | Classificateur de sécurité multimodal de Mistral AI (4 août 2026), 3,8 Md de paramètres réels, poids ouverts Apache 2.0, base Ministral 3 + encodeur vision Pixtral, 12 langues, 16 Go de VRAM en BF16 ; la politique de modération est fournie en langage naturel à l'inférence, pas apprise dans les poids | AJOUT |
| Shieldstral | TECHNOLOGIE | limites | Sortie binaire yes/no sans trace de raisonnement (auditabilité) ; confusion mention/adhésion (faux positif sur Voltaire) ; faiblesses reconnues sur entrées obscurcies, documents longs, arabe et indonésien ; au 6 août 2026, ni endpoint facturé sur La Plateforme ni Ollama officiel | AJOUT |
| topologie du garde-fou | CONCEPT | définition | Choix d'architecture désignant l'endroit où réside la sûreté d'un système d'IA : dans les poids du modèle (l'éditeur définit la politique et arbitre les exemptions) ou dans un composant séparé et auto-hébergeable (le déployeur définit la politique et en porte la responsabilité) | AJOUT |
| paire contrastive | CONCEPT | définition | Donnée d'entraînement où un même contenu est réécrit pour violer une politique mais pas sa politique sœur ; force un classificateur à lire la consigne plutôt qu'à reconnaître un thème — 4,4 M de paires génèrent +23,3 points de F1 en adaptabilité chez Shieldstral | AJOUT |
| Mistral AI | ORGANISATION | positionnement | Assume de ne pas arbitrer le licite : livre un garde-fou ouvert, séparé et auto-hébergeable dont la politique appartient au déployeur — cohérence entre l'audition d'Arthur Mensch (13 mai 2026) et Shieldstral (4 août 2026) | MISE_A_JOUR |
| Arthur Mensch | PERSONNE | doctrine | Refuse à un éditeur de modèles la légitimité démocratique d'arbitrer l'usage final ; Shieldstral applique cette position en transférant la taxonomie au déployeur | MISE_A_JOUR |
| Anthropic | ORGANISATION | positionnement | Topologie inverse de celle de Mistral : garde-fou logé dans les poids, Claude Fable 5 public avec mesures de sécurité et Claude Mythos 5 sans, réservé aux cyberdéfenseurs approuvés du Project Glasswing | MISE_A_JOUR |
| Llama Guard 4 | TECHNOLOGIE | définition | Modèle de modération de Meta embarquant la taxonomie MLCommons figée à l'entraînement ; contre-modèle de Shieldstral, mesuré à 69,1 % de F1 texte dans les benchmarks Mistral | AJOUT |
| GPT-OSS-Safeguard | TECHNOLOGIE | positionnement | Modèle de sûreté à poids ouverts, version 20B mesurée à égalité avec Shieldstral (84,9 % de F1 texte) malgré une taille sept fois supérieure | AJOUT |
| Qwen3Guard | TECHNOLOGIE | positionnement | Modèle de sûreté concurrent, version 8B mesurée à 84,0 % de F1 texte dans les benchmarks Mistral | AJOUT |
| Ministral 3 | TECHNOLOGIE | rôle | Modèle de base de Shieldstral, complété par l'encodeur vision de Pixtral pour la modération multimodale | AJOUT |
| Didier Girard | PERSONNE | rôle | Auteur de la note ; lit un lancement produit comme la mise en production d'une doctrine, valide la cohérence architecturale mais refuse les chiffres du constructeur comme preuve et documente trois manques opérationnels | MISE_A_JOUR |
