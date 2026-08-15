# Knowledge Base — Souveraineté numérique (cloud, données, IA)

> 18 fiches | Période : Janvier 2026 — Août 2026 | Généré le 2026-08-15

## Vue d'ensemble

Cette KB thématique curée couvre la **souveraineté numérique** telle qu'elle se
joue en 2026 : non plus un slogan réglementaire, mais un **critère d'achat
discriminant** pour les industriels et grands groupes européens. Le fil rouge :
la dépendance se **contracte par étages** — infrastructure (cloud), plateforme,
puis **modèle et agent** — et le verrou se referme d'autant plus vite qu'on
monte dans la pile. Deux forces structurent le premier semestre. D'abord,
l'**immunité extraterritoriale** (le *Cloud Act* américain) qui départage un
« cloud de confiance » d'un cloud simplement performant, et pousse LVMH, France
Télévisions puis **Airbus** vers **Scaleway** (groupe iliad). Ensuite, la
**souveraineté de l'IA** : faire tourner des modèles sur des données
industrielles sensibles sans les exposer suppose de garder la chaîne complète
(calcul, entraînement, inférence) — et jusqu'au **silicium** (ZML/LLMD) — en
juridiction de confiance.

Position analytique récurrente (portée notamment par la voix cabinet SFEIR et
par plusieurs praticiens du corpus) : dépasser le **faux dilemme
« multi-cloud *ou* souverain »**. La bonne métrique n'est pas le drapeau du
fournisseur, mais la **réversibilité** qu'on se donne les moyens de bâtir (ex.
plateforme ALIX de France Télévisions déployée sur Scaleway *sans réécriture*).
Le débat traverse aussi l'**open source** (Plakar pour la sauvegarde, la charge
d'Ahmad Osman contre la captation de l'« ouvert » par Anthropic) et la
**puissance publique** (qualification SecNumCloud de l'ANSSI, audition de Mistral
AI devant la commission d'enquête de l'Assemblée nationale).

**L'été 2026 déplace le centre de gravité du corpus.** Trois basculements, tous
documentés entre le 16 juillet et le 11 août :

1. **La souveraineté devient une propriété d'architecture, pas un label** — et
   elle se décompose. L'accord Mistral ↔ Microsoft (21 juil.) oblige à
   distinguer **quatre souverainetés** (modèle, exécution, infrastructure,
   relation commerciale) dont « on peut en obtenir trois sur quatre, encore
   faut-il savoir laquelle manque » : un modèle européen exécutable *air-gapped*
   … sur l'infrastructure d'un hyperscaler américain.
2. **L'open-weights devient la porte de sortie — et un objet géopolitique.**
   Kimi K3 (Moonshot) fait entrer le frontier en poids ouverts et ajoute une
   colonne « réversibilité » à la grille de décision ; Xi Jinping en fait, à la
   WAIC, l'offre de la Chine au Sud global ; Dean W. Ball (OpenAI) y répond que
   les poids ouverts sont **intrinsèquement décélérationnistes** et prédit une
   *soft law* de FUD réglementaire visant les régulés. Le même artefact
   technique est lu comme émancipation d'un côté, comme menace de l'autre.
3. **Le risque bascule de la confidentialité vers la continuité.** L'*AI Kill
   Switch Act* (déposé le 23 juil.) et surtout le **précédent Anthropic** —
   Fable 5 / Mythos 5 coupés **19 jours** en juin 2026 — établissent qu'un
   « kill switch de fait » existe déjà. La question n'est plus seulement *qui
   peut lire mes données*, mais *qui peut éteindre mon modèle*.

**Contrepoint majeur, et tension centrale du corpus** : le 11 août, Mistral
lance l'**European Compute Unit** — engagements pluriannuels de cinq ans,
« *There is no getting out* » (Lacroix) — pour financer 200 MW fin 2027 et 1 GW
fin 2030. La souveraineté vendue **change de nature** : du poids ouvert
réversible au contrat sans porte de sortie. Le champion de la réversibilité
construit son propre verrou.

## Chronologie

### 2026 — La souveraineté devient un critère d'achat

- **Jan. 2026** — Guillaume Strubel décortique la qualification **SecNumCloud**
  de l'ANSSI : sécurité *et* immunité aux risques extraterritoriaux, montée des
  offres hybrides.
- **Jan. 2026** — **Plakar** : la sauvegarde open source française (stockage
  immuable Kloset, CNCF/Linux Foundation, ~60× les performances S3) — la
  souveraineté par la donnée archivée et la portabilité.
- **Jan. 2026** — Frédéric Simon : l'abandon de **SoGPT** (Société Générale) au
  profit de **Copilot** relance le « faux débat » build *vs* buy — la vraie
  bataille est le **capital IA** et la souveraineté européenne, pas l'outil.
- **Mars 2026** — **ALMIA (AG2R La Mondiale)** : plateforme d'IA générative
  interne d'un assureur régulé, bâtie sur le **cloud souverain S3NS** — adoption
  massive des collaborateurs, souveraineté par la plateforme.
- **Mai 2026** — Audition d'**Arthur Mensch (Mistral AI)** devant la commission
  d'enquête de l'Assemblée nationale sur les vulnérabilités numériques : la
  souveraineté IA portée au niveau politique et de la dépendance stratégique.
- **Juin 2026** — Sur **VivaTech**, le DSI de **LVMH** explique le choix de
  **Scaleway** : géopolitique de la tech, autonomie européenne, cloud hybride
  régionalisé (« on n'aime pas le mot souveraineté »).
- **Juin 2026** — Ahmad Osman, « **Anthropic's War on Opensource AI** » (1,7 M
  vues) : thèse à charge selon laquelle la « sécurité » serait convertie en
  mécanisme de fermeture — enjeu de souveraineté des **modèles ouverts**.
- **Juil. 2026** — **ZML / LLMD** (startup parisienne) : le « Docker des LLM »,
  souveraineté portée jusqu'au **silicium** (5 familles de puces, une base de
  code ; partenariat VSORA/Scaleway/Région Île-de-France).
- **16 juil. 2026** — **Airbus** retient **Scaleway** comme « **cloud de
  confiance** » après un appel d'offres à dix candidats : la gouvernance
  (immunité Cloud Act) l'emporte sur la seule performance — seuil de crédibilité
  franchi pour le cloud souverain européen.

### Été 2026 — Du cloud au modèle : réversibilité, kill switch, verrouillage

- **16 juil. 2026** — **Kimi K3** (Moonshot AI) : le frontier passe en
  **open-weights** (~2,8 T de paramètres annoncés, 1 M de contexte, prix cassés).
  La singularité décisive n'est pas un score, c'est la **réversibilité** — une
  API consommée redevient une **option** (self-host, portage, sortie de
  captivité). Spécifications et scores restent *vendor-stated*.
- **16-17 juil. 2026** — **WAIC 2026 / WAICO** : premier discours d'ouverture de
  **Xi Jinping** en personne, « quatre observations » dont la promotion de
  l'**open-source** ; naissance de **WAICO** (29 pays, siège Shanghai, aucune
  économie occidentale majeure). La Chine mise sur l'adhésion, les poids ouverts
  et des coûts d'inférence faibles pour offrir au **Sud global** une alternative
  à l'« America First » et aux contrôles à l'export.
- **17 juil. 2026** — **Dean W. Ball** (Head of Strategic Futures, OpenAI ;
  rédacteur d'*America's AI Action Plan*) prend le **contre-pied** : les poids
  ouverts sont **décélérationnistes** (ils dissuadent le capex), l'open-sourcing
  chinois est un sous-produit involontaire des contrôles à l'export, et la bonne
  stratégie américaine n'est pas d'interdire l'open source mais de fabriquer du
  **risque réglementaire** (soft law, FUD) pour que **les entreprises régulées
  reculent**.
- **20 juil. 2026** — **Janakiram MSV** : Bedrock AgentCore, Microsoft Foundry
  et Gemini Enterprise convergent sur **six primitives identiques**, mais
  **aucun contrat applicatif portable** n'existe pour les agents — on ne déplace
  pas un agent d'un cloud à l'autre (état, traces, identité restent chez le
  fournisseur). La souveraineté de l'**étage agent** est encore à écrire.
- **20 juil. 2026** — **Delos Intelligence** (fact-check) : la souveraineté
  « 100 % Scaleway » annoncée était **en cours de finalisation** fin 2025, une
  partie du calcul restant sur Azure France — cas d'école de l'écart entre
  souveraineté *annoncée* et souveraineté *effective*.
- **21-22 juil. 2026** — **Mistral ↔ Microsoft** : partenariat de plusieurs
  milliards, compute Azure réservé en Europe, modèles Mistral dans Foundry et
  Copilot Studio, **Azure Local jusqu'au mode déconnecté (air-gapped)** — et
  **aucune prise de participation** (confirmé par Brad Smith). Lecture SFEIR :
  quatre souverainetés à distinguer, l'open-weights comme seul élément rendant
  la souveraineté **portable**, et un angle mort — la **lisibilité de la
  stratégie industrielle** de Mistral.
- **23-24 juil. 2026** — **AI Kill Switch Act** (section 2220F, 119ᵉ Congrès) :
  deux seuils **cumulatifs** (≥ 500 M$ de revenu IA *et* > 100 M$ de compute
  d'entraînement) qui couvrent peu de labs aujourd'hui, mais une **mécanique
  d'élargissement** (révision annuelle des seuils, clause affiliés, indexation
  au prix cloud) et un **effet domino** sur les clients ; sanctions jusqu'à
  20 M$/jour. Preuve opérationnelle du risque : **Fable 5 / Mythos 5 coupés
  19 jours** par Anthropic en juin 2026.
- **7 août 2026** — **Shieldstral 1.0 3B** (Mistral) : le garde-fou **sort des
  poids**. La politique de modération n'est plus figée à l'entraînement (Llama
  Guard 4 embarque la taxonomie MLCommons) mais **lue à l'inférence**, en
  langage naturel, modifiable sans réentraînement — composant ouvert
  (Apache 2.0), auto-hébergeable, dont la politique appartient au **déployeur**.
  Opposition de topologies avec Anthropic, où l'éditeur arbitre qui échappe au
  garde-fou (Project Glasswing).
- **11 août 2026** — **Mistral : 1 GW en 2030 et l'European Compute Unit**.
  Regional Endpoints en GA, Priority Tier avec SLA, coalition d'ancrage
  (Amadeus, ASML, Capgemini, CMA CGM) finançant 200 MW fin 2027 puis 1 GW fin
  2030. L'**ECU** est un contrat d'achat de capacité façon PPA électrique,
  visant **cinq ans d'engagement** : « *There is no getting out* ». Mistral se
  met par ailleurs à héberger des **modèles ouverts tiers** (GLM-5.2 de Z.ai,
  laboratoire chinois) — passage d'éditeur de modèles à **couche de
  distribution souveraine**.

## Fiches sources

### Cloud souverain & données (immunité extraterritoriale, réversibilité)

- [[fiches/2026-07/sfeir-airbus-scaleway-cloud-confiance-souverainete-2026-07-16\|Airbus choisit Scaleway pour son « cloud de confiance » : la souveraineté à l'épreuve de l'industrie stratégique]]
- [[fiches/2026-06/lvmh-scaleway-souverainete-cloud-geopolitique-tech-vivatech-2026-06-11\|LVMH × Scaleway sur VivaTech : géopolitique de la tech, autonomie européenne et cloud hybride régionalisé]]
- [[fiches/2026-03/almia-ag2r-plateforme-ia-generative-deep-research-2026-03\|ALMIA (AG2R La Mondiale) : plateforme d'IA générative interne sur cloud souverain S3NS]]
- [[fiches/2026-01/strubel-secnumcloud-anssi-linkedin-2026-01-06\|SecNumCloud en (pas si) bref : qualification ANSSI, risques extraterritoriaux, offres hybrides]]
- [[fiches/2026-01/plakar-sauvegarde-open-source-deep-research-2026-01\|Plakar : la révolution française de la sauvegarde open source (Kloset, CNCF, ~60× S3)]]
- [[fiches/2026-07/delos-intelligence-fact-check-levee-2026-07-20\|Delos Intelligence (fact-check) : souveraineté « 100 % Scaleway » annoncée vs calcul encore partiellement sur Azure France]]

### Souveraineté de l'IA (modèles, inférence, silicium, politique)

- [[fiches/2026-08/nunez-mistral-gigawatt-compute-europeen-venturebeat-2026-08-11\|Mistral : 1 GW de compute européen en 2030 et l'European Compute Unit — « There is no getting out »]]
- [[fiches/2026-07/sfeir-mistral-microsoft-souverainete-strategie-industrielle-2026-07-22\|Mistral ↔ Microsoft : un accord souverain, une stratégie industrielle encore illisible (les quatre souverainetés)]]
- [[fiches/2026-08/girard-shieldstral-mistral-doctrine-garde-fou-2026-08-07\|Shieldstral : Mistral compile sa doctrine en 3,8 milliards de paramètres (le garde-fou sort des poids)]]
- [[fiches/2026-07/sfeir-zml-llmd-docker-llm-inference-souveraine-2026-07-09\|ZML/LLMD : et si le « Docker des LLM » était français ? (souveraineté du silicium à l'inférence)]]
- [[fiches/2026-05/mensch-mistral-commission-enquete-vulnerabilites-numeriques-souverainete-ia-2026-05-13\|Arthur Mensch (Mistral AI) devant la commission d'enquête sur les vulnérabilités numériques]]
- [[fiches/2026-01/simon-sogpt-copilot-faux-debat-souverainete-ia-2026-01-15\|SoGPT vs Copilot : le faux débat qui nous fait perdre la vraie bataille (capital IA, souveraineté européenne)]]

### Open-weights : réversibilité, géopolitique et contre-thèses

- [[fiches/2026-07/sfeir-kimi-k3-moonshot-frontier-open-weights-2026-07-16\|Kimi K3 de Moonshot AI : quand le frontier open-weights rattrape le propriétaire (la colonne « réversibilité »)]]
- [[fiches/2026-07/deanwball-open-weights-decelerationnistes-kimi-2026-07-17\|Dean W. Ball : les modèles à poids ouverts sont intrinsèquement décélérationnistes (contre-thèse OpenAI)]]
- [[fiches/2026-07/xi-waic2026-gouvernance-mondiale-ia-2026-07-17\|Xi Jinping à la WAIC 2026 : open-source, WAICO (29 pays) et offre au Sud global]]
- [[fiches/2026-06/osman-anthropic-war-on-opensource-ai-2026-06-12\|Anthropic's War on Opensource AI (Ahmad Osman) : sécurité comme mécanisme de fermeture]]

### Continuité de service & portabilité des agents

- [[fiches/2026-07/sfeir-rapport-kill-switch-souverainete-2026-07-24\|« AI Kill Switch Act » : seuils cumulatifs, mécanique d'élargissement et « so what » pour les entreprises européennes]]
- [[fiches/2026-07/janakiram-agent-platform-portability-contract-2026-07-20\|Les trois hyperscalers convergent sur la même architecture d'agents — et aucun contrat de portabilité n'existe]]

## Entités clés

### Organisations & institutions

- [[kb/Scaleway-organisation\|Scaleway]] — Filiale cloud et IA du groupe iliad ; « cloud de confiance » retenu par Airbus (face à 10 candidats), LVMH et France Télévisions
- [[kb/_entites-mineures#iliad\|iliad]] — Groupe télécoms/tech français, maison mère de Scaleway
- [[kb/_entites-mineures#Airbus\|Airbus]] — Groupe aéronautique et spatial ; retient Scaleway pour ses données/applications critiques (16 juil. 2026)
- [[kb/LVMH\|LVMH]] — Choix Scaleway (VivaTech 2026) : cloud hybride régionalisé, autonomie européenne
- [[kb/Mistral-AI\|Mistral AI]] — Champion IA européen ; audition parlementaire, accord Microsoft sans prise au capital, cap 1 GW en 2030, Shieldstral
- [[kb/Microsoft\|Microsoft]] — Partenaire industriel de Mistral (compute Azure en Europe, Azure Local air-gapped) et **locataire d'ancrage** de ses datacenters européens
- [[kb/SecNumCloud\|SecNumCloud]] — Qualification de sécurité cloud de l'**ANSSI** ; immunité extraterritoriale
- [[kb/Plakar-organisation\|Plakar]] — Éditeur français de sauvegarde open source (stockage immuable Kloset, CNCF)
- [[kb/Anthropic\|Anthropic]] — Cible de la charge « War on Opensource AI » ; auteur du précédent « kill switch de fait » (Fable 5 / Mythos 5, 19 jours)
- [[kb/Delos-Intelligence\|Delos Intelligence]] — Startup française d'IA générative B2B ; souveraineté Scaleway annoncée avant d'être effective
- [[kb/_entites-mineures#Société-Générale\|Société Générale]] — Abandon de SoGPT au profit de Copilot (débat build vs buy)
- ANSSI — Autorité française de cybersécurité, émettrice du référentiel SecNumCloud
- AG2R La Mondiale — Assureur régulé ; plateforme GenAI interne ALMIA sur cloud souverain
- Moonshot AI — Laboratoire chinois ; Kimi K3, frontier en poids ouverts (16 juil. 2026)
- WAICO — Organisation mondiale de coopération en IA, intergouvernementale, siège Shanghai, 29 pays signataires (16 juil. 2026)
- Amadeus, ASML, [[kb/Capgemini\|Capgemini]], CMA CGM — Coalition d'ancrage finançant les European Compute Units de Mistral

### Technologies & plateformes

- [[kb/Scaleway-technologie\|Scaleway (plateforme)]] — Cloud d'IA souverain européen : GPU, offre d'inférence, écosystème de modèles opérés sur le sol européen
- [[kb/_entites-mineures#S3NS\|S3NS]] — Cloud souverain (coentreprise Thales × Google Cloud) hébergeant la plateforme ALMIA d'AG2R
- [[kb/_entites-mineures#ALIX\|ALIX]] — Plateforme maison de France Télévisions déployée sur Scaleway *sans réécriture* — preuve de réversibilité en production
- [[kb/Plakar-technologie\|Plakar / Kloset]] — Stockage immuable open source, portabilité et immutabilité des sauvegardes
- [[kb/_entites-mineures#VSORA\|VSORA]] — Concepteur européen de puces IA (processeur Jotunn8) intégrant la couche ZML — souveraineté au niveau du silicium
- [[kb/Kimi-K3\|Kimi K3]] — Frontier open-weights de Moonshot AI ; transforme une dépendance API en **option** de self-host
- [[kb/Shieldstral\|Shieldstral]] — Modèle de modération Mistral (3,8 Md, Apache 2.0) dont la **politique est lue à l'inférence**, pas figée dans les poids
- [[kb/Microsoft-Foundry\|Microsoft Foundry]] / Azure Local — Distribution des modèles Mistral et exécution jusqu'au **mode déconnecté (air-gapped)**
- [[kb/Amazon-Bedrock-AgentCore\|Bedrock AgentCore]] — Plateforme d'agents AWS ; l'une des trois convergences sans contrat de portabilité
- [[kb/GLM-5.2\|GLM-5.2]] (Z.ai) — Modèle ouvert chinois hébergé par Mistral sous contrôles régionaux : le playbook *model garden* sur sol européen
- [[kb/GitHub-Copilot\|GitHub Copilot]] / [[kb/Microsoft-Copilot\|Microsoft Copilot]] — Solution « buy » retenue par Société Générale au détriment de SoGPT
- [[kb/AI-Kill-Switch-Act\|AI Kill Switch Act]] — Section 2220F, autorité DHS/CISA, seuils cumulatifs et sanctions jusqu'à 20 M$/jour
- Cloud Act — Loi extraterritoriale américaine ; critère discriminant qu'aucun hyperscaler US ne peut neutraliser
- European Compute Unit (ECU) — Créance fongible sur de la capacité Mistral, engagement cinq ans, sans sortie anticipée

### Personnes

- [[kb/Arthur-Mensch\|Arthur Mensch]] — Cofondateur et DG de Mistral AI ; auditionné par la commission d'enquête (mai 2026), refuse tout droit de regard sur l'usage final des modèles
- [[kb/Timothée-Lacroix\|Timothée Lacroix]] — Cofondateur et CTO de Mistral AI ; « *Tout l'intérêt des compute units, c'est d'avoir de l'engagement* » / « *There is no getting out* »
- [[kb/Damien-Lucas\|Damien Lucas]] — Directeur général de Scaleway ; situe l'accord Airbus sur le terrain de l'IA industrielle
- [[kb/Xi-Jinping\|Xi Jinping]] — Premier keynote WAIC en personne (17 juil. 2026) : open-source, WAICO et gouvernance multilatérale centrée Sud global
- [[kb/Janakiram-MSV\|Janakiram MSV]] — Analyste (The New Stack) ; « celui qui possèdera le *control plane* agent définira ce qu'est un agent »
- Dean W. Ball — Head of Strategic Futures, OpenAI ; thèse des poids ouverts « décélérationnistes » et de la *soft law* comme arme
- [[kb/_entites-mineures#Catherine-Jestin\|Catherine Jestin]] — EVP Digital d'Airbus ; protection des données critiques contre les législations étrangères
- [[kb/_entites-mineures#Steeve-Morin\|Steeve Morin]] — Fondateur de ZML (ex-VP Engineering de Zenly) ; souveraineté « model to metal »

## Concepts structurants

### La souveraineté par étages

```
Silicium / puces (ZML–LLMD, VSORA Jotunn8)
  → Infrastructure cloud (Scaleway, S3NS, SecNumCloud, Azure Local)
    → Plateforme / données (ALMIA, ALIX, Plakar/Kloset)
      → Modèle & poids (Mistral, Kimi K3, open weights, Shieldstral)
        → Agent & control plane (AgentCore, Foundry, Gemini Enterprise)
```
La dépendance se contracte à chaque étage ; **plus on monte, plus le verrou se
referme vite qu'on ne le défait**. Le contrat cloud sécurise le bas ; la partie
décisive — la réversibilité de l'IA sur les données — se joue en haut. L'été
2026 ajoute l'étage du dessus, le **control plane agent**, et y constate le
vide : six primitives convergentes chez les trois hyperscalers, **aucun contrat
applicatif portable**, aucun projet open source ne l'ayant revendiqué.

### Les quatre souverainetés (grille issue de l'accord Mistral × Microsoft)

| Souveraineté | Question qu'elle tranche | Ce qui la rend portable |
|---|---|---|
| **Modèle** | Qui possède et gouverne les poids ? | Licence open-weights |
| **Exécution** | Où tourne l'inférence, sous quel contrôle de clés ? | Mode déconnecté / air-gapped, chiffrement en mémoire |
| **Infrastructure** | Qui possède le fer et sous quelle juridiction ? | Immunité extraterritoriale (Cloud Act) |
| **Relation commerciale** | Qui peut interrompre le service, à quelles conditions ? | Absence d'engagement irréversible, clause de continuité |

On peut « en obtenir trois sur quatre — encore faut-il savoir laquelle manque ».
Corollaire : **la souveraineté est une propriété d'architecture, pas un label**,
et se qualifie **dépendance par dépendance**.

### Le critère qui tranche : l'immunité extraterritoriale (Cloud Act)

- Les hyperscalers US (Microsoft, Google, AWS) gardent une avance fonctionnelle
  qu'aucun européen n'égale « sur toute la ligne » — mais **aucun ne peut
  soustraire ses clients au Cloud Act**.
- Pour une PI valant des décennies de recherche (Airbus), le risque n'est pas
  théorique : il **conditionne** la décision.
- **Renversement de hiérarchie** (thèse Airbus/SFEIR) : *juridiction et immunité
  extraterritoriale d'abord, fonctionnalités ensuite* — inversion de l'ordre
  implicite des dix dernières années.

### Le faux dilemme « multi-cloud *ou* souverain »

- Le multicloud n'est pas un **repli** derrière « un unique drapeau tricolore »,
  mais une **doctrine** : chaque charge vit là où ses contraintes la placent, en
  conservant le **pouvoir d'en changer**.
- La souveraineté durable n'est **pas le contrat signé**, c'est la
  **réversibilité** qu'on bâtit (ALIX sur Scaleway sans réécriture).
- Nuance : pour la classe de données la plus sensible, placer chez un acteur
  **immunisé au Cloud Act** est un gain qu'aucun montage multicloud sur
  hyperscaler US ne procure.
- Traduction en règles de conception (SFEIR, juil. 2026) : **séparer le modèle
  du canal**, **concevoir pour sortir** (*Design to Exit* — l'open-weights rend
  la porte de sortie crédible), **router plutôt que parier** (portefeuille
  multi-LLM souverain).

### Continuité : du « qui peut me lire » au « qui peut m'éteindre »

- **Précédent opérationnel** : Anthropic coupe Fable 5 et Mythos 5 **19 jours**
  en juin 2026 — un « kill switch de fait » sans qu'aucune loi ne l'impose.
- **Cadre légal en formation** : l'*AI Kill Switch Act* (23 juil. 2026) confie
  au DHS via la **CISA** une autorité d'arrêt, sous **deux seuils cumulatifs**
  (≥ 500 M$ de revenu IA *et* > 100 M$ de compute d'entraînement). Peu de labs
  couverts aujourd'hui — la thèse « barrière très basse » est **inexacte au sens
  strict** — mais la **mécanique d'élargissement** (révision annuelle, clause
  affiliés, indexation au prix cloud) et l'**effet domino sur les clients**
  élargissent la portée réelle. Nuance importante : le red-teaming est **exclu**
  du déclenchement de l'autorité d'urgence.
- **Conséquences CTO** : architecture multi-modèles **réellement testée** (pas
  seulement documentée), clauses de continuité, cartographie d'exposition,
  options souveraines identifiées à l'avance.

### Open-weights : réversibilité, ou décélération ?

- **Thèse « réversibilité »** (Kimi K3, SFEIR) : un frontier en poids ouverts
  transforme une API consommée en **option**. La question change — non plus
  « quel est le meilleur modèle ? » mais « **quelle part de mon système suis-je
  prêt à rendre dépendante d'un fournisseur que je ne contrôle pas ?** ». Prix
  d'entrée : une infrastructure lourde (2,8 T de paramètres à héberger).
- **Thèse géopolitique** (Xi, WAIC) : l'open-source comme **offre au Sud
  global** — adhésion, coûts d'inférence faibles, WAICO et sièges à Shanghai,
  face à l'« America First » et aux contrôles à l'export.
- **Contre-thèse** (Dean W. Ball, OpenAI) : les poids ouverts sont
  **décélérationnistes** (ils dissuadent le capex), l'ouverture chinoise est un
  sous-produit des contrôles à l'export, et l'arme efficace n'est pas
  l'interdiction mais la **soft law** — assez de FUD réglementaire pour que les
  **entreprises régulées** reculent d'elles-mêmes. À lire comme le miroir exact
  de la thèse de réversibilité : le même artefact, lu comme risque.
- **Où le garde-fou vit-il ?** Deux topologies s'opposent : **dans les poids**
  (Anthropic — l'éditeur arbitre qui y échappe, cf. Project Glasswing) ou
  **hors des poids** (Shieldstral — politique lue à l'inférence, composant
  ouvert et auto-hébergeable, dont la politique appartient au déployeur). C'est
  une question de souveraineté, pas seulement de sécurité.

### Le retournement de l'été : quand le champion de la réversibilité vend du verrouillage

- L'**European Compute Unit** n'est pas un contrat cloud : c'est un **contrat
  d'achat de capacité à la manière d'un PPA électrique**, destiné à verrouiller
  la demande *avant* le déploiement du capital — cinq ans visés, « *There is no
  getting out* ».
- **L'arithmétique explique le mécanisme** : ~4 Md$ levés au total (PitchBook)
  face à ~38 Md$ de capex pour un datacenter d'un gigawatt (Epoch AI) et
  15-20 M$/MW hors puces (Goldman Sachs Research) ; les trois sites détaillés
  totalisent 77 MW.
- **Deux angles morts assumés** : les **GPU restent américains** (Nvidia), et
  Microsoft — locataire d'ancrage — est présenté comme ce qui *dé-risque* la
  construction, pas comme une dépendance.
- **La souveraineté devient une décision de configuration** : les documents
  Mistral mentionnent des « transferts limités et encadrés » vers des
  sous-traitants hors région ; interrogé, Lacroix désigne **les appels
  d'outils** (recherche web). Formulation la plus honnête du corpus : *« le
  contrôle régional complet est disponible, mais dès qu'un agent IA va chercher
  le web ouvert, la souveraineté devient une décision de configuration, pas un
  défaut »*.
- **Changement de rôle** : en hébergeant des modèles ouverts tiers (GLM-5.2 de
  Z.ai) sous ses propres contrôles régionaux, Mistral passe d'**éditeur de
  modèles** à **couche de distribution souveraine** — l'intermédiaire par lequel
  un régulé européen consomme un modèle chinois qu'il ne pourrait jamais appeler
  directement.

### Souveraineté & open source (débat ouvert)

- **Ouverture comme levier** : Plakar (sauvegarde), CNCF/Linux Foundation,
  interopérabilité native, technologies ouvertes réclamées par Airbus.
- **Charge critique** (Osman) : la « sécurité » invoquée par Anthropic serait
  convertie en mécanisme de **fermeture** des modèles — question de souveraineté
  des poids ouverts, distincte de la souveraineté de l'infrastructure.
- **Ce que les protocoles ouverts ne couvrent pas** (Janakiram) : MCP, A2A et
  OpenTelemetry standardisent l'interopérabilité, pas le **cycle de vie**.
  Trois questions de due diligence : **gouvernance** (fondation neutre vs
  vendor), **packaging** (même artefact sur deux clouds sans réécriture),
  **état** (mémoire exportable).

### Signaux clés

- **Airbus** : appel d'offres à **10 candidats** ouvert en janvier 2026 ;
  Scaleway retenu sur 3 critères, le juridique étant « le plus discriminant ».
- **Trois clients Scaleway** en quelques semaines : LVMH, France Télévisions,
  Airbus — bascule d'un « pis-aller réglementaire » vers un standard industriel.
- **SecNumCloud** : la qualification ANSSI comme socle d'immunité
  extraterritoriale et montée des offres hybrides.
- **ZML/LLMD** : 5 familles de puces depuis **une seule base de code** ;
  partenariat souverain VSORA × Scaleway × Région Île-de-France (VivaTech 2026).
- **Mistral × Microsoft** : partenariat de plusieurs milliards **sans prise de
  participation** — préserve la gouvernance de Mistral *et* minimise le risque
  antitrust (arbitrage réglementaire assumé, pas seulement technique).
- **Anthropic, juin 2026** : Fable 5 et Mythos 5 coupés **19 jours** — la preuve
  que le kill switch existe déjà, sans loi.
- **WAICO** : **29 pays** signataires, siège Shanghai, **aucune économie
  occidentale majeure** — l'écart de performance US-Chine réduit à **2,7 %**
  (Stanford HAI 2026).
- **Mistral, août 2026** : 77 MW documentés → **200 MW fin 2027** → **1 GW fin
  2030**, financés par des engagements clients de **cinq ans**.
- Métrique cardinale transverse : **réversibilité** > contrat signé. Mais l'été
  2026 montre qu'elle se **négocie à contre-courant** — le verrou décisif s'est
  déplacé de l'infrastructure vers le **modèle, l'agent et la durée
  d'engagement**.
