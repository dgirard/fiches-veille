---
themes: [transformation-adoption, philosophie-societe, strategie-frameworks]
source: "felixrieseberg.com"
---
# rieseberg-how-to-be-more-ambitious-2026-10-13

## Veille

Billet de blog de **Felix Rieseberg** (fonction affichée : EM chez **Anthropic**, a dirigé l'ingénierie de Claude.ai, **Cowork** et Claude Code Desktop ; co-mainteneur d'**Electron**), publié le **13 octobre 2026** ; ~2 000 mots, 8 minutes. Il répond au mot d'ordre *« we're not ambitious enough »* par un tutoriel : l'ambition avec un modèle se décline en **quatre types**, **Speed**, **Altitude**, **Depth** et **Range**, la vitesse étant écartée comme acquise.

**(A) Altitude** : viser le résultat plutôt que la tâche, *« what's the goal beyond the goal? »* ; l'auteur est passé de « corrige ce crash » à « garde nos apps sans crash », ce qui a exigé d'outiller le modèle (rapports de crash, correspondance version ↔ commit, machines Windows, macOS, Linux). **(B) Depth** : travailler comme le meilleur professionnel du domaine (bases de données et modèles statistiques plutôt que tableaux markdown, objectifs déraisonnables, hypothèses vérifiées contre les données brutes, production de connaissance nouvelle, **juge extérieur** au modèle), avec un prompt type en quatre questions. **(C) Range** : convoquer d'autres disciplines, en remplaçant les noms par des verbes (Tom Kelley) et en composant une équipe, sans tomber dans le jeu de rôle : *« Don't ask the model to write like a short seller, ask it to do what a short seller does »*.

Un fil rouge illustre les trois axes : la revue trimestrielle (QBR) d'une entreprise fictive, Acme Inc. Une dernière partie rattache le problème à l'**auto-efficacité** (self-efficacy) : objectifs difficiles et précis (Locke et Latham), Dantzig, Bannister, le marathon sous deux heures de Sabastian Sawe, *The Inner Game of Tennis*.

Rapproche le billet de [[osmani-agentic-verification-2026-10-14]], qui traite aussi de la vérification hors du modèle.

## Titre Article

How to be more ambitious: A tutorial for humans with models

## Date

2026-10-13

## URL

https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/

## Keywords

ambition, usage des modèles, Speed, Altitude, Depth, Range, abstraction, objectif au-delà de l'objectif, revue trimestrielle, QBR, profondeur d'expertise, données brutes, juge extérieur, vérification, objectifs déraisonnables, pluridisciplinarité, noms en verbes, jeu de rôle, auto-efficacité, Claude

## Authors

Felix Rieseberg — EM chez Anthropic (fonction affichée), co-mainteneur d'Electron ; blog personnel felixrieseberg.com.

## Ton

Profil : tutoriel d'un praticien qui travaille sur le produit dont il parle, adressé aux utilisateurs de modèles, non spécialistes compris. Le registre est familier et enjoué (*« I primarily use Claude (duh) »*, aliens qui menacent la Terre pour justifier l'équipe idéale), mais la structure est méthodique : une taxonomie en quatre types, puis pour chacun des techniques numérotées et des prompts reproductibles, sur un exemple unique filé (la QBR d'Acme Inc). L'auteur borne ses conseils : l'altitude convient mal aux projets créatifs, « Claude, go make money » ne fonctionne pas en 2026, l'auto-évaluation par le modèle reste à proscrire en octobre 2026. La dernière partie change de registre, passe à l'anecdote historique et sportive, et se termine par un appel aux lecteurs à partager leurs propres techniques.

## Pense-betes

- **Quatre types d'ambition** : Speed (même travail, moins de temps, écarté), Altitude (résultat plutôt que tâche), Depth (méthode d'expert), Range (plusieurs disciplines).
- **Altitude** : passer de « corrige ce crash » à « garde l'app sans crash » ; signe que c'est pertinent : le sujet donnerait lieu à des réunions. Prérequis : outiller le modèle (crash reports, version ↔ commit, machines des trois OS).
- **QBR en trois paliers** : expliquer ce qui a changé et pourquoi → trois décisions urgentes avec arguments pour/contre → concevoir mieux qu'un deck trimestriel, le prouver sur l'historique, le faire tourner en parallèle un trimestre.
- **Depth, cinq techniques** : instruments des meilleurs (pas seulement leur vocabulaire) ; objectif déraisonnable (200 ms au lieu de 5 s) ; tester les croyances sur les données brutes ; produire une connaissance nouvelle (simulation clients, signal de churn validé hors échantillon) ; juge extérieur, idéalement un outil exécutable.
- **Prompt Depth** : ce que ferait un pro → matériau le plus brut → méthodes et outils → ce qui prouverait le résultat hors de toi et moi → réécrire le prompt.
- **Range** : noms → verbes (la QBR = « faire croire à des gens pressés une histoire de cause à effet et décider dans l'incertitude, en 30 minutes ») ; équipe : analyste, journaliste, éditeur, motion/audio designer, red team (vendeur à découvert, juricomptable). Chercher des méthodes, pas des voix.
- **Condition commune** : un ordinateur où le modèle installe des logiciels + accès aux données (MCP ou autre).
- **Auto-efficacité** : croire possible (Dantzig), voir quelqu'un le faire (Bannister, Sawe), s'autoriser l'échec (*Inner Game of Tennis*, annonce de Linux).

## RésuméDe400mots

Felix Rieseberg, qui travaille sur Claude chez Anthropic, constate que les capacités des modèles progressent de façon inégale, « stupéfiantes dans certaines directions, insuffisantes dans d'autres » selon Terence Tao. Certains utilisateurs en tirent des résultats remarquables ; beaucoup se limitent à des questions simples. Au slogan « nous ne sommes pas assez ambitieux », il oppose un tutoriel.

Il distingue quatre types d'ambition. La vitesse, faire le même travail plus vite, est acquise et ne demande pas de créativité ; il la laisse de côté. Restent l'altitude, la profondeur et l'étendue.

L'altitude consiste à monter en abstraction : se demander quel est le but derrière le but. L'auteur est passé de demandes de correction de crashs à la consigne de garder ses applications sans crash, ce qui l'a obligé à donner au modèle les rapports de crash, la correspondance entre versions et commits et des machines Windows, macOS et Linux pour reproduire et vérifier. Sur l'exemple d'une revue trimestrielle chez Acme Inc, il gradue : expliquer ce qui a changé et pourquoi, dégager les trois décisions les plus urgentes avec leurs arguments, puis concevoir un dispositif plus efficace que le deck trimestriel, le valider sur l'historique et le faire tourner en parallèle. L'approche vaut pour les résultats visés, moins pour la création.

La profondeur consiste à exécuter la tâche comme le meilleur expert du domaine. Les modèles changent volontiers de vocabulaire sans changer de méthode : il faut exiger les instruments des meilleurs, fixer des objectifs déraisonnables en les présentant comme raisonnables, faire vérifier les hypothèses sur les données brutes, demander une connaissance nouvelle validée sur des données non vues, et surtout recourir à un juge extérieur, pas au modèle lui-même. Un prompt type demande au modèle ce que ferait un professionnel, de quel matériau brut il partirait, avec quelles méthodes, et ce qui prouverait le résultat, avant de réécrire la demande.

L'étendue consiste à convoquer d'autres disciplines, ce que les systèmes multi-agents rendent économique. Deux techniques : remplacer les noms par des verbes pour voir quels métiers sont concernés, et composer l'équipe idéale, red team comprise, en demandant au modèle de faire ce que fait chaque métier plutôt que d'en imiter le style. Toutes ces approches supposent un ordinateur et un accès aux données.

Rieseberg rattache enfin le problème à l'auto-efficacité : on accomplit davantage quand on croit la chose possible, quand on a vu quelqu'un la réussir, ou quand on s'autorise l'échec. Dans un monde où les capacités progressent par bonds, il appelle à partager d'autres techniques.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Felix Rieseberg | PERSONNE | travaille_chez | Anthropic | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Felix Rieseberg | PERSONNE | a_créé | Quatre types d'ambition | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| Altitude | CONCEPT | fait_partie_de | Quatre types d'ambition | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Depth | CONCEPT | fait_partie_de | Quatre types d'ambition | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Range | CONCEPT | fait_partie_de | Quatre types d'ambition | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Speed | CONCEPT | fait_partie_de | Quatre types d'ambition | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| Felix Rieseberg | PERSONNE | affirme_que | les modèles opèrent à des niveaux d'abstraction plus élevés à mesure qu'ils gagnent en capacité | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| Felix Rieseberg | PERSONNE | affirme_que | les modèles invités à agir en professionnels changent de vocabulaire sans changer de méthode | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| Felix Rieseberg | PERSONNE | recommande | un juge extérieur au modèle, idéalement un outil exécutable | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| Felix Rieseberg | PERSONNE | recommande | des objectifs déraisonnables présentés au modèle comme raisonnables | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Felix Rieseberg | PERSONNE | recommande | de demander au modèle ce que fait un métier plutôt que d'en imiter le style | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |
| Depth | CONCEPT | utilise | juge extérieur | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Range | CONCEPT | s_inspire_de | The Art of Innovation | DOCUMENT | 0.85 | STATIQUE | déclaré_article |
| Range | CONCEPT | utilise | systèmes multi-agents | TECHNOLOGIE | 0.80 | DYNAMIQUE | déclaré_article |
| Felix Rieseberg | PERSONNE | référence | Terence Tao | PERSONNE | 0.85 | STATIQUE | déclaré_article |
| Quatre types d'ambition | CONCEPT | est_basé_sur | Auto-efficacité | CONCEPT | 0.78 | ATEMPOREL | inféré |
| Locke et Latham | PERSONNE | affirme_que | des objectifs précis et difficiles donnent de meilleures performances que « faire de son mieux » | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |
| Felix Rieseberg | PERSONNE | utilise | Claude | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Felix Rieseberg | PERSONNE | rôle | EM chez Anthropic (Claude.ai, Cowork, Claude Code Desktop), co-mainteneur d'Electron | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| Quatre types d'ambition | CONCEPT | définition | Taxonomie de l'usage ambitieux des modèles : Speed, Altitude, Depth, Range | AJOUT |
| Altitude | CONCEPT | définition | Monter en abstraction : confier le résultat visé plutôt que la tâche | AJOUT |
| Depth | CONCEPT | définition | Exécuter la tâche avec les instruments et méthodes du meilleur expert du domaine | AJOUT |
| Range | CONCEPT | définition | Mobiliser plusieurs disciplines au-delà de celle que la tâche appelle en surface | AJOUT |
| Speed | CONCEPT | définition | Le même travail en moins de temps ; valeur économique établie de l'IA | AJOUT |
| Auto-efficacité | CONCEPT | définition | Croyance en ses capacités, corrélée à l'accomplissement (self-efficacy) | AJOUT |
| juge extérieur | CONCEPT | définition | Validation du résultat par un tiers ou un outil, jamais par le modèle lui-même | AJOUT |
| The Art of Innovation | DOCUMENT | auteur | Tom Kelley et Jonathan Littman ; technique « remplacer les noms par des verbes » | AJOUT |
| Claude | TECHNOLOGIE | catégorie | Modèle et assistant d'Anthropic | AJOUT |
| billet How to be more ambitious | DOCUMENT | catégorie | Billet de blog, felixrieseberg.com, 13 octobre 2026 | AJOUT |
