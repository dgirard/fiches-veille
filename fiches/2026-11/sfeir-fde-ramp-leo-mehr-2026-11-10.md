---
themes: [transformation-adoption, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-fde-ramp-leo-mehr-2026-11-10

## Veille

Critique éditoriale **SFEIR AI** publiée sur sfeir.com le **10 novembre 2026**, dans la série de neuf retours sur la playlist *forward deployed engineering* de l'**AI Engineer World's Fair 2026**. Elle porte sur le talk de **Leo Mehr**, director of engineering chez **Ramp** au moment du talk (à la tête de Lumos Labs, chez **Lumos**, depuis août 2026), 14 min 04, **2 070** vues. Deux principes tirés de deux ans et demi de FDE (équipe passée de **2** à une **trentaine** d'ingénieurs). **(1)** Toujours cadrer : face au commercial qui exige un vendredi soir une intégration **SAP S/4HANA**, poser les questions (qui pousse l'urgence, qui utilisera, quel contournement, quels autres clients en profiteraient) ; contre-exemple d'une application Android livrée à un client tout iPhone. **(2)** Passer à l'échelle avec des tokens : découper le cycle d'une demande et confier chaque étape à des agents, en commençant par un **agent d'accueil** bâti sur les agents Notion (première réponse en quelques secondes, ~**20 %** de temps de cadrage gagné, estimation hésitante). Sans cadrage, l'usine à agents devient un *« token maxing slop cannon »*. Notes SFEIR : **3/5** et **4/5**. Même entreprise que [[orosz-salmon-klaric-ramp-inspect-coding-agent-2026-08-25]].

## Titre Article

Leo Mehr (Ramp) : sans cadrage, l'usine à agents devient un canon à slop

## Date

2026-11-10

## URL

https://www.sfeir.com/articles/fde-ramp-leo-mehr/

## Keywords

forward deployed engineering, FDE, Ramp, Leo Mehr, Lumos, AI Engineer World's Fair 2026, cadrage, qualification des demandes, SAP S/4HANA, avant-vente, agent d'accueil, intake agent, agents Notion, Slack, spécification, spec-driven development, évaluations, harnais, contexte, token maxing, slop cannon, AI slop, services IA, ESN, critique de talk

## Authors

SFEIR AI (voix éditoriale non signée), sfeir.com, site éditorial de SFEIR. Critique du talk de Leo Mehr (Ramp).

## Ton

Critique de talk au format fixe de la série SFEIR (encadré, minutages, « Pour une ESN », verdict noté). Registre concis et favorable : l'article salue *« quatorze minutes sans remplissage »*, des exemples honnêtes (l'application Android inutile) et une pratique reproductible, et qualifie le talk de *« meilleur rapport intérêt-durée de la série »*. Réserves : cadrer avant de construire n'a rien de neuf, l'outillage au-delà de l'accueil reste peu décrit et les 20 % sont une estimation. Public : responsables de flux de demandes clients, avant-vente d'ESN.

## Pense-betes

- **Format** : 14 min 04, mis en ligne le 28 juillet 2026, 2 070 vues.
- **FDE chez Ramp** : rattaché à l'ingénierie, aide à gagner les grands comptes en faisant fonctionner le produit et ses fonctions agentiques ; Leo Mehr dirige ~30 ingénieurs entre FDE, API développeurs et nouvelle activité de services IA. Il récuse le mème du FDE aboutissement de l'avant-vente technique.
- **Image (vers 2:02)** : dire oui à tout donne des chevaux avec des fusées aux pattes au lieu de Waymo.
- **Principe 1 — cadrer (vers 3:03)** : urgence portée par le client ou par l'objectif trimestriel du commercial ? qui utilisera ? contournement manuel ? développeurs côté client pour appeler l'API ? quels autres clients en profiteraient ?
- **Échec (vers 5:04)** : deux FDE apprennent iOS et Android pour un remboursement de frais mobile ; le client impose l'iPhone → moitié du travail inutile.
- **Principe 2 — tokens (vers 7:05)** : cycle découpé en contexte → cadrage → spécification → implémentation, chaque étape confiée à des agents.
- **Agent d'accueil** : canal Slack + formulaire Notion, qualité de demande variable ; V1 sur agents Notion = 2-3 questions, première réponse de heures/jours à secondes ; V2 (un petit pingouin) mène plusieurs tours jusqu'à rédiger une spécification ; ~20 % de temps de cadrage gagné.
- **Maillon faible (vers 10:10)** : passer d'une demande clarifiée à une spécification exploitable reste mal outillé ; les modèles frontières implémentent d'un coup une fonctionnalité moyenne à partir d'une bonne spec.
- **Prévision 6-12 mois** : le FDE de Ramp travaillera sur harnais, évaluations (grilles, retours humains) et contexte ; goût et jugement restent humains.
- **Conclusion (vers 12:11)** : usine à agents sans cadrage = slop cannon ; cadrage sans agents = dépassé par les concurrents nés avec eux.
- **Pour une ESN** : agent d'accueil transposable en avant-vente ; valeur des consultants dans la transformation demande clarifiée → spécification.

## RésuméDe400mots

SFEIR AI publie le 10 novembre 2026 une critique du talk « How Forward Deployed Engineering is done at Ramp », donné à l'AI Engineer World's Fair 2026 par Leo Mehr, alors director of engineering chez Ramp, aujourd'hui à la tête de Lumos Labs chez Lumos, qu'il a cofondée. En deux ans et demi, l'équipe FDE de Ramp est passée de deux ingénieurs à une trentaine répartis entre FDE, API développeurs et services IA. Rattaché à l'ingénierie, le FDE y aide à gagner les grands comptes en faisant fonctionner le produit et ses fonctions agentiques.

Leo Mehr annonce deux principes et s'y tient en quatorze minutes. Le premier consiste à toujours cadrer. Scène type : un vendredi soir, un commercial exige une intégration SAP S/4HANA sans laquelle un client stratégique ne signera pas. Plutôt que d'accepter, il faut demander qui pousse l'urgence, qui utilisera l'intégration, s'il existe un contournement, si le client a des développeurs capables d'appeler l'API et quels autres clients en profiteraient. Contre-exemple vécu : deux FDE apprennent iOS et Android pour livrer une fonction mobile, avant de découvrir que le client impose l'iPhone à tous ses salariés.

Le second principe consiste à passer à l'échelle avec des tokens : découper le cycle d'une demande (contexte, cadrage, spécification, implémentation) et confier chaque étape à des agents. Ramp a commencé par l'accueil. Les équipes commerciales postent leurs blocages dans un canal Slack via un formulaire Notion ; un premier agent bâti sur les agents Notion posait deux ou trois questions, faisant passer la première réponse de plusieurs heures ou jours à quelques secondes. La version actuelle mène plusieurs tours jusqu'à rédiger une spécification. Leo Mehr estime, avec hésitation, le gain à 20 % du temps de cadrage.

La difficulté se situe au milieu : passer d'une demande clarifiée à une spécification exploitable reste mal outillé, alors que les modèles frontières implémentent une fonctionnalité moyenne d'un coup à partir d'une bonne spécification. Dans six à douze mois, le FDE travaillera surtout sur harnais, évaluations et contexte. La conclusion relie les deux principes : sans cadrage, une usine à agents devient un « token maxing slop cannon » ; sans agents, une équipe experte du cadrage sera dépassée.

Pour une ESN, l'agent d'accueil se transpose en avant-vente. Verdict : originalité 3/5, qualité de l'information 4/5.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | critique FDE Ramp Leo Mehr | DOCUMENT | 0.95 | STATIQUE | déclaré_article |
| critique FDE Ramp Leo Mehr | DOCUMENT | référence | AI Engineer World's Fair 2026 | EVENEMENT | 0.95 | STATIQUE | déclaré_article |
| Leo Mehr | PERSONNE | travaille_chez | Ramp | ORGANISATION | 0.85 | STATIQUE | déclaré_article |
| Leo Mehr | PERSONNE | travaille_chez | Lumos | ORGANISATION | 0.85 | DYNAMIQUE | déclaré_article |
| Ramp | ORGANISATION | utilise | Forward Deployed Engineering | METHODOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Leo Mehr | PERSONNE | recommande | toujours cadrer une demande avant de construire | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Ramp | ORGANISATION | a_créé | agent d'accueil des demandes FDE | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| agent d'accueil des demandes FDE | TECHNOLOGIE | utilise | Notion | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| agent d'accueil des demandes FDE | TECHNOLOGIE | réduit | délai de première réponse de plusieurs heures ou jours à quelques secondes | MESURE | 0.86 | STATIQUE | déclaré_article |
| agent d'accueil des demandes FDE | TECHNOLOGIE | améliore | environ 20 % du temps de cadrage (estimation) | MESURE | 0.72 | STATIQUE | déclaré_article |
| Leo Mehr | PERSONNE | affirme_que | "token maxing slop cannon" | CITATION | 0.9 | ATEMPOREL | déclaré_article |
| AI slop | CONCEPT | observé_dans | usine à agents sans cadrage | CONCEPT | 0.82 | ATEMPOREL | inféré |
| Leo Mehr | PERSONNE | affirme_que | passer d'une demande clarifiée à une spécification exploitable reste mal outillé | AFFIRMATION | 0.86 | DYNAMIQUE | déclaré_article |
| Leo Mehr | PERSONNE | prédit | dans 6 à 12 mois le FDE de Ramp travaillera surtout sur harnais, évaluations et contexte | AFFIRMATION | 0.84 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Leo Mehr | PERSONNE | rôle | Director of engineering chez Ramp au moment du talk ; dirige Lumos Labs chez Lumos depuis août 2026 | AJOUT |
| Ramp | ORGANISATION | équipe FDE | De 2 à ~30 ingénieurs (FDE, API développeurs, services IA) en deux ans et demi | AJOUT |
| agent d'accueil des demandes FDE | TECHNOLOGIE | définition | Agent Notion branché sur Slack qui pose les questions de cadrage puis rédige une spécification | AJOUT |
| critique FDE Ramp Leo Mehr | DOCUMENT | notes SFEIR | Originalité 3/5, qualité de l'information 4/5 | AJOUT |
