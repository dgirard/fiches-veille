---
themes: [qualite-securite, recherche-education, agents-codage-ia-skills]
source: SFEIR
---
# sfeir-ctf-crackmes-formation-retro-ingenierie-2026-10-16

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **16 octobre 2026** (~6 500 signes, quatre sources notées, avertissement « pas un conseil juridique »). Il propose les **crackmes** et les **CTF** comme terrain de formation à la rétro-ingénierie assistée par agents, depuis l'arrivée de **REA** en octobre 2026. Quatre apports. **(1)** Pourquoi les crackmes : petits, analysables avec l'autorisation de l'auteur, souvent pourvus d'un writeup qui sert de corrigé ; **crackmes.one** les présente comme *« made to be cracked »*. Un guide communautaire du dépôt REA propose une échelle de **six cibles**, du programme C écrit soi-même au malware en machine virtuelle. **(2)** Ce qu'on apprend : poser des questions courtes (« où le programme vérifie-t-il l'entrée ? ») et surtout **relire les preuves** — séparer ce que l'agent a observé de ce qu'il a déduit. **(3)** Les règles d'un entraînement sûr : machine virtuelle, instantanés, réseau coupé, REA n'étant *pas un bac à sable* ; pas d'agent en CTF sans autorisation explicite. **(4)** Enseigner le cadre : le DISCLAIMER de REA refuse le contournement de *« DRM, license checks, anti-cheat systems »*. S'inscrit dans la série SFEIR sur REA, aux côtés de l'article sur ses limites mesurées.

## Titre Article

CTF et crackmes : former ses équipes à la rétro-ingénierie assistée par agents

## Date

2026-10-16

## URL

https://www.sfeir.com/articles/ctf-formation-retro-ingenierie/

## Keywords

rétro-ingénierie, reverse engineering, crackmes, crackmes.one, CTF, capture the flag, formation, REA, agents de code, Ghidra, assembleur, keygen, writeup, patch, revue des preuves, observé vs déduit, machine virtuelle, isolation, sandbox, DRM, contrôle de licence, anti-cheat, cadre juridique, usages légitimes, SFEIR Institute

## Authors

SFEIR AI, voix éditoriale de SFEIR (ESN), article non signé individuellement, publié sur sfeir.com.

## Ton

Profil : article pédagogique d'une ESN, registre didactique et prudent, en français, public de responsables d'équipes sécurité et de formateurs. Le texte s'ouvre sur une citation de la FAQ de crackmes.one et définit chaque notion avant de l'utiliser (crackme, keygen, writeup). Il s'appuie presque entièrement sur des sources primaires citées verbatim en anglais : la FAQ du site, un guide communautaire du dépôt REA, les fichiers SECURITY.md et DISCLAIMER.md de l'outil. Un encadré initial précise que la page n'est pas un conseil juridique et renvoie à un juriste. La progression va de la technique (échelle des cibles, bonnes et mauvaises questions) à la sécurité (confinement), puis au cadre (frontière exercice / infraction). Le ton reste mesuré : les règles sont présentées comme celles des sources, et la FAQ répond aux questions de légalité et d'usage en CTF par des réponses brèves. Clôture sur les formations SFEIR Institute, « sans promesse de certification externe ».

## Pense-betes

- **Crackme** : petit programme cachant un contrôle (mot de passe, numéro de série) écrit pour être analysé. crackmes.one : *« all crackmes available on this website have been made to be cracked »* ; niveau 1 conseillé aux débutants.
- **Échelle des six cibles** (guide « New to RE with AI? », discussion n° 2412 du dépôt REA, 12 octobre 2026) : programme C écrit soi-même → crackmes et CTF d'entraînement → version sans symboles d'un petit outil open source (bzip2) → jeux open source et vieux programmes → sa propre application web ou une application Electron open source → malware, en VM uniquement.
- **Principe** : commencer petit, questions courtes sur un seul fichier, vérifier chaque réponse ; le source ou le writeup sert de corrigé.
- **Bonnes et mauvaises demandes** : « reconstruis tout » ou « passe la licence » → rien ; « où le programme vérifie-t-il l'entrée, explique simplement » → progrès.
- **Compétence centrale = la revue** : REA rend conclusions + preuves (fichier, adresse, instructions) + ce qu'il n'a pas établi ; l'apprenant exige l'assembleur qui justifie chaque réponse.
- **Keygen et patch** : keygen = réimplémentation de l'algorithme de validation avec writeup ; patcher pendant l'étude est admis, une solution réduite à un patch ne l'est en général pas.
- **Entraînement sûr** : VirtualBox, VMware ou Hyper-V, instantanés, réseau coupé ; archives protégées par le mot de passe « crackmes.one ». REA **n'est pas un bac à sable** (SECURITY.md).
- **Autres règles** : outils navigateur de REA uniquement sur ses propres pages ; en CTF en direct, pas d'agent sans mention explicite de l'organisateur.
- **Cadre** : crackmes.one interdit cracks commerciaux, contournements de DRM, triches, vrais malwares ; DISCLAIMER de REA cite CTF et enseignement comme usages légitimes.
- **Cible de fin de parcours** : piloter Ghidra par un agent, exiger une preuve par affirmation, savoir dire quand une demande sort du périmètre.

## RésuméDe400mots

L'article de SFEIR présente les crackmes et les compétitions CTF comme le terrain le plus sûr pour former des équipes à la rétro-ingénierie assistée par agents. Le contexte est l'arrivée en octobre 2026 de REA, un outil qui donne à un agent de code les capacités d'un rétro-ingénieur. Un crackme est un petit programme qui cache un contrôle, mot de passe ou numéro de série, et qui est publié pour être analysé : la FAQ de crackmes.one le dit explicitement. L'analyse est donc autorisée par l'auteur, et le risque technique se maîtrise en confinant l'exécutable.

L'article s'appuie sur un guide communautaire publié dans les discussions du dépôt REA, qui propose une progression en six cibles : un programme C écrit soi-même, puis des crackmes et CTF d'entraînement, la version sans symboles d'un outil open source comme bzip2, des jeux et vieux programmes, sa propre application web ou une application Electron open source, et enfin un malware, uniquement en machine virtuelle. Le principe est de commencer petit, de poser des questions courtes sur un seul fichier et de vérifier chaque réponse, le code source ou le writeup publié servant de corrigé.

Ce que l'apprenant acquiert tient moins à l'outil qu'à la méthode. Demander à l'agent de reconstruire tout un programme ou de contourner une licence ne mène nulle part ; lui demander où le programme vérifie l'entrée, puis d'expliquer, fait progresser. La compétence centrale est la revue : REA rend ses conclusions avec leurs preuves et liste ce qu'il n'a pas établi, et l'apprenant apprend à réclamer l'assembleur justifiant chaque réponse pour séparer l'observé du déduit. Cette discipline sert ensuite sur du code d'entreprise sans corrigé. L'article précise aussi les usages admis sur crackmes.one : écrire un keygen avec son explication, patcher pendant l'étude, mais pas soumettre un simple patch.

Les règles de sécurité reprennent celles du site : exécution en machine virtuelle, instantanés, réseau coupé. REA n'ajoute aucune isolation, sa politique de sécurité indiquant qu'il n'est pas un bac à sable. Les outils navigateur ne visent que des pages que l'on possède, et en CTF en direct on s'abstient d'utiliser un agent sans autorisation explicite.

Enfin, l'article insiste sur l'enseignement du cadre. crackmes.one interdit les cracks de logiciels commerciaux et les contournements de DRM ; le DISCLAIMER de REA cite l'enseignement et les CTF comme usages légitimes et refuse d'aider à contourner les protections techniques. Une équipe formée doit comprendre pourquoi la même technique change de statut appliquée à un logiciel du commerce. Un avertissement rappelle que l'article n'est pas un conseil juridique.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | CTF et crackmes : former ses équipes à la rétro-ingénierie assistée par agents | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | former à la rétro-ingénierie par agents sur des crackmes et des CTF d'entraînement | AFFIRMATION | 0.92 | DYNAMIQUE | déclaré_article |
| crackmes.one | ORGANISATION | publie | crackmes | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| crackmes.one | ORGANISATION | affirme_que | all crackmes available on this website have been made to be cracked | CITATION | 0.93 | DYNAMIQUE | déclaré_article |
| crackmes | CONCEPT | permet | formation à la rétro-ingénierie assistée par agents | METHODOLOGIE | 0.88 | ATEMPOREL | déclaré_article |
| formation à la rétro-ingénierie assistée par agents | METHODOLOGIE | utilise | REA | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| formation à la rétro-ingénierie assistée par agents | METHODOLOGIE | est_basé_sur | New to RE with AI? | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | la compétence centrale est la revue des preuves, séparer l'observé du déduit | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| SECURITY.md de REA | DOCUMENT | affirme_que | REA n'est pas un bac à sable | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| crackmes.one | ORGANISATION | recommande | exécuter les crackmes en machine virtuelle, avec instantanés et réseau coupé | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| DISCLAIMER de REA | DOCUMENT | s_oppose_à | contournement de DRM, contrôles de licence et anti-cheat | CONCEPT | 0.88 | DYNAMIQUE | déclaré_article |
| crackmes.one | ORGANISATION | s_oppose_à | publication de cracks de logiciels commerciaux et de vrais malwares | CONCEPT | 0.86 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | ne pas utiliser d'agent en CTF sans autorisation explicite de l'organisateur | AFFIRMATION | 0.86 | ATEMPOREL | déclaré_article |
| SFEIR Institute | ORGANISATION | s_applique_à | formation à la rétro-ingénierie assistée par agents | METHODOLOGIE | 0.8 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| crackmes | CONCEPT | définition | Petits programmes cachant un contrôle, publiés pour être analysés | AJOUT |
| crackmes.one | ORGANISATION | rôle | Site d'hébergement de crackmes, niveaux de difficulté, règles d'usage | AJOUT |
| formation à la rétro-ingénierie assistée par agents | METHODOLOGIE | principe | Cibles graduées, questions courtes, vérification de chaque réponse par la preuve | AJOUT |
| REA | TECHNOLOGIE | catégorie | Outil de rétro-ingénierie piloté par agent (dépôt morluto/rea) | AJOUT |
| New to RE with AI? | DOCUMENT | publication | Guide communautaire, discussion n° 2412 du dépôt REA, 12 octobre 2026 | AJOUT |
| DISCLAIMER de REA | DOCUMENT | contenu | Usages légitimes (CTF, enseignement) et refus d'aider au contournement des protections | AJOUT |
| SECURITY.md de REA | DOCUMENT | contenu | Politique de sécurité de REA, absence d'isolation | AJOUT |
