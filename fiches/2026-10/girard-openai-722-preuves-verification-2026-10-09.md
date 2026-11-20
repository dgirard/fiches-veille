---
themes: [recherche-education, qualite-securite, philosophie-societe]
source: SFEIR
---
# girard-openai-722-preuves-verification-2026-10-09

## Veille

Article de **Didier Girard** publié sur sfeir.com le **9 octobre 2026** et mis à jour le **27 octobre** (~4 300 mots, trente-cinq sources). Il part du dépôt **openai/math** du **6 octobre 2026** : **722** manuscrits d'un modèle interne en **372** familles, tirés d'environ **4 000** problèmes ouverts, environ trois heures de calcul par résultat. Trois apports. **(A)** La vérification à l'épreuve : le **7 octobre**, OpenAI retire trois manuscrits pour une **erreur de signe** qui en invalidait deux autres et en révise **14** ; **300** résultats principaux sur 719 sont formalisés en **Lean** (~**42 %**) ; un utilisateur recompile la famille 003 avec Claude Code et deux noyaux, et note qu'une seule des **405** configurations Comparator active le second ; un préprint (Bastounis, Circelli, Hansen) soutient que Lean ne garantit pas l'argument en langage naturel, ce qu'illustre la famille 130. **(B)** Les réactions : Villani (*« au moins quatre siècles »*), LeCun (*« une nouvelle ère »*), Tao, l'AGMAI, et **Hugo Duminil-Copin**, dont le domaine est couvert par **3 500** pages de manuscrits contre **3 700** publiées dans sa carrière. **(C)** La transposition à l'entreprise, par le détour de **Galois** (quinze ans entre le rapport de Poisson et la publication) : spécifications exécutables relues par un humain, vérificateurs indépendants activés par défaut, changelog des retraits, et la règle de l'auteur — une confiance *« proportionnelle à ce qu'un tiers peut vérifier sans cette machine »*.

## Titre Article

722 preuves en un commit : ce que la publication mathématique d'OpenAI dit de l'avenir de la vérification

## Date

2026-10-09

## URL

https://www.sfeir.com/articles/openai-722-preuves-mathematiques-verification/

## Keywords

OpenAI, openai/math, preuves mathématiques, IA et mathématiques, vérification, vérification formelle, Lean, autoformalisation, Comparator, nanoda, erreur de signe, retrait de manuscrits, conjecture de Hodge, Unique Games, zêta, Navier-Stokes, AGMAI, Cédric Villani, Yann LeCun, Terence Tao, Hugo Duminil-Copin, François Charles, Évariste Galois, goulot de la vérification, spécification exécutable, revue de code, DORA 2025, créateur-vérificateur

## Authors

Didier Girard, SFEIR — publié sur sfeir.com, site éditorial de SFEIR.

## Ton

**Profil** : essai d'analyse signé, publié sur le site d'un cabinet, adressé aux DSI, CTO, lead devs, RSSI et achats qui déploient des agents. Français soutenu, première personne assumée sur deux jugements (*« Je lis ce retrait comme la meilleure nouvelle de la semaine »* ; *« Ma règle »*).

**Style** : enquête en questions (« Qu'y a-t-il dans le dépôt ? », « Pourquoi trois manuscrits ont disparu en un jour », « Qui a recompilé les preuves ? »), puis panorama des réactions, long passage sur Duminil-Copin, métaphore filée de la cuisine et du goûteur (*« Lean ne dispense pas du goûteur »*), parallèle historique avec Galois et Poisson, et section entreprise par rôle. Chaque chiffre renvoie à un fichier du dépôt (README, history.md) ou à une source datée à l'heure près.

**Position épistémique** : l'article explique l'écart entre 722, 719, 372 et 377, marque le préprint Bastounis *et al.* comme non relu, signale qu'une recompilation unique ne vaut pas reproduction, borne le parallèle avec Galois (*« Le parallèle a ses limites »*) et relève l'incertitude sur le dénominateur (4 000 ou 8 000 problèmes, tentatives échouées comptées ou non). Il note aussi quelles recommandations de l'AGMAI OpenAI a suivies et lesquelles non.

## Pense-betes

- **Dépôt du 6 octobre** : billet « Sharing AI progress in mathematics » + github.com/openai/math (Apache 2.0) ; 722 manuscrits, 372 familles (numérotées jusqu'à 377, cinq vides), bibliothèque Lean, dix résumés de raisonnement. Presque chaque résultat vient d'un seul prompt à un seul agent.
- **Résultats mis en avant par Altman** : quasi-hypothèse de Riemann, Unique Games, un cas de la conjecture de Hodge, facteurs de groupes libres.
- **Retrait du 7 octobre** (history.md) : erreur de signe dans « Algebraicity of Weil classes on split abelian eightfolds », deux papiers dépendants tombent ; 14 révisions, 13 mises à jour de citations ; ancienne version archivée, rien supprimé en silence.
- **Recompilation indépendante** : davegoldblatt, famille 003 (ζ(s) ≠ 0 pour Re(s) > 7/8), Claude Code, Comparator du Lean FRO puis noyau nanoda ; une seule configuration sur 405 active le second noyau.
- **Limite de Lean** : Lean garantit que la preuve prouve l'énoncé, pas le choix de l'énoncé ; famille 130 = titre « pour tout n », preuve pour une sous-suite.
- **AGMAI** (IAS, neuf membres non rémunérés, dont François Charles, Gowers, Hairer, Witten) : recommandations du 29 septembre (nettoyer, déposer hors contrôle des labos, formaliser, financer la lecture humaine) ; OpenAI en suit une partie.
- **Duminil-Copin** (séminaire MIAM de la SMF, 8 octobre) : tout ce qu'il citait a été résolu, *« farming »*, doctorants *« en état de panique total »* ; dépôt arXiv « à la dernière seconde » le 5 octobre. Une preuve de θ(pc)=0 signée Anthropic (anthropics/formal-math) datait du 28 août.
- **Galois** : mémoire de 1831, rapport Lacroix-Poisson (*« ni assez clairs, ni assez développés »*), publication par Liouville en 1846.
- **Pour l'entreprise** : spécification exécutable relue (TLA+, tests de contrat), plusieurs vérificateurs actifs par défaut, changelog daté des retraits ; DORA 2025 et la revue de code comme goulot ; demander aux fournisseurs le coût par résultat utilisable, tentatives échouées comprises.
- **Règle de l'auteur** : la confiance accordée à une sortie de machine IA (modèle, harnais, contexte) doit être proportionnelle à ce qu'un tiers peut vérifier sans elle.

## RésuméDe400mots

Le 6 octobre 2026, OpenAI a déposé sur GitHub 722 manuscrits mathématiques produits par un modèle interne, regroupés en 372 familles et tirés d'une évaluation sur environ 4 000 problèmes ouverts. Chaque résultat a demandé en moyenne trois heures de calcul. Le lendemain, OpenAI retirait trois manuscrits : une erreur de signe dans l'un invalidait les deux autres, qui en dépendaient. Quatorze autres étaient révisés. Didier Girard part de cet épisode pour soutenir que, lorsque la machine génère à ce débit, la valeur se déplace vers la vérification.

L'article détaille ce que la vérification couvre. Environ 42 % des résultats principaux sont formalisés en Lean. Un utilisateur a recompilé l'une des preuves avec Claude Code et deux noyaux indépendants, en notant qu'une seule configuration sur 405 activait le second. Un préprint de Bastounis, Circelli et Hansen soutient qu'une preuve Lean issue d'une autoformalisation ne garantit pas l'argument en langage naturel ; le dépôt l'illustre avec une famille dont le titre promet plus que ce que la preuve établit.

Les réactions sont restituées : Cédric Villani parle du changement le plus radical depuis quatre siècles, Yann LeCun d'une nouvelle ère où la valeur se reporte sur les concepts et les définitions, Terence Tao de problèmes résolus par des prompteurs incapables de les exposer. Le groupe consultatif AGMAI avait recommandé de nettoyer, déposer hors du contrôle des labos, formaliser et financer la lecture humaine ; OpenAI n'en a suivi qu'une partie. Hugo Duminil-Copin, médaille Fields, décrit un domaine couvert en une nuit par 3 500 pages de manuscrits, presque autant qu'il en a écrit dans sa vie, et des doctorants en panique.

L'auteur rapproche la situation de celle de Galois, dont le mémoire de 1831 fut jugé illisible par Poisson et publié quinze ans plus tard : une démonstration n'existe qu'une fois comprise et transmise.

Pour l'entreprise, la leçon porte sur les agents de code. Le dépôt sépare spécification et implémentation, comme une suite de tests séparée du code ; mais un test vert sur une mauvaise spécification reste un risque. L'article recommande des spécifications exécutables relues par des humains, plusieurs vérificateurs indépendants activés par défaut et un changelog qui date chaque retrait. Il invite à demander aux fournisseurs le coût d'un résultat utilisable et pose une règle : la confiance accordée à une sortie de machine doit être proportionnelle à ce qu'un tiers peut vérifier sans elle.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Didier Girard | PERSONNE | travaille_chez | SFEIR | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | openai/math | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| openai/math | DOCUMENT | mesure | 722 manuscrits en 372 familles, ~3 h de calcul par résultat | MESURE | 0.93 | STATIQUE | déclaré_article |
| openai/math | DOCUMENT | mesure | 300 résultats principaux formalisés sur 719 (~42 %) | MESURE | 0.9 | STATIQUE | déclaré_article |
| openai/math | DOCUMENT | utilise | Lean | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | affirme_que | trois manuscrits retirés le 7 octobre pour une erreur de signe | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Navier-Stokes lost in translation | DOCUMENT | affirme_que | la vérification Lean d'une autoformalisation ne garantit pas la preuve en langage naturel | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Cédric Villani | PERSONNE | affirme_que | « le changement le plus radical en mathématiques depuis au moins quatre siècles » | CITATION | 0.9 | STATIQUE | déclaré_article |
| Yann LeCun | PERSONNE | prédit | la démonstration formelle automatisée reporte la valeur sur concepts, définitions et conjectures | AFFIRMATION | 0.88 | DYNAMIQUE | déclaré_article |
| AGMAI | ORGANISATION | recommande | déposer hors du contrôle des labos, formaliser et financer la lecture humaine | AFFIRMATION | 0.88 | STATIQUE | déclaré_article |
| Hugo Duminil-Copin | PERSONNE | mesure | 3 500 pages de manuscrits citant ses travaux contre 3 700 publiées dans sa carrière | MESURE | 0.86 | STATIQUE | déclaré_article |
| Hugo Duminil-Copin | PERSONNE | s_oppose_à | « cette version bulldozer… ne va pas fonctionner » | CITATION | 0.84 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | publie | anthropics/formal-math | DOCUMENT | 0.82 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | s_inspire_de | Évariste Galois | PERSONNE | 0.85 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | affirme_que | quand la machine génère à ce débit, la valeur se déplace de la génération vers la vérification | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | référence | DORA 2025 | DOCUMENT | 0.85 | STATIQUE | déclaré_article |
| Didier Girard | PERSONNE | recommande | spécifications exécutables relues, vérificateurs indépendants activés par défaut, changelog daté des retraits | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Didier Girard | PERSONNE | recommande | proportionner la confiance à ce qu'un tiers peut vérifier sans la machine IA | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Didier Girard | PERSONNE | rôle | Auteur, SFEIR | AJOUT |
| openai/math | DOCUMENT | définition | Dépôt public d'OpenAI (6 oct. 2026), manuscrits mathématiques d'un modèle interne, Apache 2.0 | AJOUT |
| Lean | TECHNOLOGIE | catégorie | Assistant de preuve formelle | AJOUT |
| AGMAI | ORGANISATION | définition | Advisory Group on Mathematics and AI, hébergé par l'IAS, neuf membres, indépendant des labos | AJOUT |
| Hugo Duminil-Copin | PERSONNE | rôle | Mathématicien, médaille Fields 2022 | AJOUT |
| Cédric Villani | PERSONNE | rôle | Mathématicien, médaille Fields | AJOUT |
| Yann LeCun | PERSONNE | rôle | Chercheur en IA | AJOUT |
| Évariste Galois | PERSONNE | rôle | Mathématicien (1811-1832), mémoire de 1831 publié en 1846 par Liouville | AJOUT |
| Navier-Stokes lost in translation | DOCUMENT | référence | Préprint arXiv:2610.08144 de Bastounis, Circelli et Hansen (6 oct. 2026), non relu | AJOUT |
