---
themes: [agents-codage-ia-skills, politique-regulation, philosophie-societe]
source: "The Register"
---
# claburn-register-linux-kernel-assisted-by-tag-2026-10-14

## Veille

Article de **Thomas Claburn** (*AI and software reporter*, **The Register**), publié le **14 octobre 2026** ; ~800 mots. Il rapporte l'abandon par la communauté du noyau **Linux** de l'obligation de déclarer l'usage d'outils d'IA dans les contributions.

**(A)** La décision : selon **Sasha Levin** (développeur du noyau, ingénieur chez **Nvidia**), *« The Maintainers Summit reached consensus to deprecate the Assisted-by Tag »*, avec retrait de la documentation qui l'exigeait. Le tag, proposé en **juillet 2025** et documenté en **janvier 2026**, demandait de signaler dans le message de commit tout *« advanced coding tool »*. **(B)** Le contexte : en un an, les agents produisent un code jugé acceptable ; **Greg Kroah-Hartman** déclarait en août que *« LLMs are good enough now »* pour trouver des bugs. Restent les inquiétudes sur les erreurs non vues, la responsabilité et la reproduction de code sous droit d'auteur ; **Claude** ajoute une mention de provenance par défaut, **Codex** non. **(C)** Le débat : **Jeff Layton** (**Red Hat**) avance trois raisons (règle non respectée, *« free advertising for proprietary LLM companies »*, utilité de la donnée non établie) ; **Laurent Pinchart** (**Ideas on Board**) défend la valeur d'une attente explicite même inapplicable. **(D)** La réponse de **Linus Torvalds** : par une analogie (interdire compilateurs et éditeurs), il rejette les règles *« you can't use tools for X »* ; seule compte la compréhension du code.

Prolonge [[torvalds-llm-outil-kernel-2026-07-14]], où Torvalds affirmait déjà que Linux n'est pas un projet anti-IA.

## Titre Article

Linux kernel devs drop obligatory confession of AI tool usage — Torvalds says contributors must understand their code, whatever tools they use

## Date

2026-10-14

## URL

https://www.theregister.com/ai-and-ml/2026/10/14/linux-kernel-devs-drop-obligatory-confession-of-ai-tool-usage/5303140

## Keywords

noyau Linux, Linux kernel, tag Assisted-by, déclaration d'usage de l'IA, divulgation, attribution, provenance du code, Maintainers Summit, mainteneurs, message de commit, LKML, code généré par IA, responsabilité, droit d'auteur, compréhension du code, open source, gouvernance de projet, Linus Torvalds

## Authors

Thomas Claburn — AI and software reporter, The Register.

## Ton

Profil : article d'actualité de presse technique, factuel et vivant, dans le style de The Register (titre ironique sur la « confession obligatoire », « lords of Linux », « penguin's kernel community »). Le texte expose la décision, retrace l'historique du tag, situe le contexte de qualité des agents, puis confronte les positions de Jeff Layton et Laurent Pinchart avant de citer longuement la réponse de Linus Torvalds, qui clôt l'article sans commentaire du journaliste. Les seuls apports propres de l'auteur sont deux paragraphes de contexte : la stigmatisation persistante de l'usage de l'IA et la différence de pratique d'attribution entre Claude et Codex.

## Pense-betes

- **Décision** : le Maintainers Summit déprécie le tag `Assisted-by` et retire la documentation qui l'exigeait (annonce de Sasha Levin sur la LKML).
- **Historique** : proposé en juillet 2025, documenté en janvier 2026 ; visait tout « advanced coding tool » utilisé pour un patch.
- **Contexte** : en un an, code des agents jugé de qualité acceptable pour le noyau ; Kroah-Hartman : les LLM sont des *pattern matchers*, le code est fait de motifs.
- **Pour l'abandon (Layton, Red Hat)** : règle non respectée ; publicité gratuite pour les éditeurs de LLM propriétaires ; utilité de la donnée non établie.
- **Contre (Pinchart)** : énoncer ce qu'on attend garde de la valeur, même si certains trichent ; demande un autre mécanisme de divulgation.
- **Torvalds** : règle ironique « pas de compilateur, pas d'éditeur » ; l'attente porte sur la compréhension, pas sur l'outil.
- **Pratiques divergentes** : Claude ajoute une provenance par défaut, Codex non.
- **Risques restants** : erreurs non vues, responsabilité, code sous droit d'auteur reproduit.
- Voisin de [[raymond-llm-coding-empowering-2026-07-08]].

## RésuméDe400mots

La communauté du noyau Linux renonce à demander aux contributeurs s'ils ont utilisé des outils d'IA. Sasha Levin, développeur du noyau et ingénieur chez Nvidia, a annoncé sur la liste de diffusion que le Maintainers Summit avait trouvé un consensus pour déprécier le tag Assisted-by et retirer la documentation qui l'exigeait. Cette règle demandait à quiconque utilisait un outil de codage avancé pour créer un patch de le signaler par ce tag dans le message de commit. Proposée en juillet 2025, elle avait été intégrée à la documentation en janvier 2026, peu après que Linus Torvalds s'était dit plutôt favorable au vibe coding comme porte d'entrée vers la programmation, tout en restant sceptique sur la maintenabilité.

Selon l'article, l'attribution posait peu de question tant que le code généré était manifestement mauvais ; depuis un an environ, les agents produisent un code de qualité acceptable pour le noyau. En août, au Open Source Summit de la Linux Foundation en Corée du Sud, Greg Kroah-Hartman jugeait les LLM assez bons pour trouver des bugs, puisqu'ils reconnaissent des motifs et que le code n'est que motifs dans un format donné. Les inquiétudes demeurent : erreurs non détectées, responsabilité, reproduction de code protégé. Une stigmatisation persiste aussi envers ceux qui ne comprennent pas le code obtenu par prompt. Les éditeurs eux-mêmes divergent : Claude ajoute par défaut une mention de provenance, Codex non.

Jeff Layton, de Red Hat, avait justifié le retour en arrière par trois arguments : tout le monde ne respecte pas la règle, elle fait de la publicité gratuite aux éditeurs de LLM propriétaires, et l'intérêt de collecter cette information n'est pas établi. Laurent Pinchart, fondateur d'Ideas on Board, refuse de retirer le tag sans autre mécanisme de divulgation : il s'agit de dire ce que l'on attend, et le fait que certains trichent n'a jamais empêché de rejeter leurs contributions.

Linus Torvalds lui a répondu qu'il ne s'agissait pas d'attentes mais de blocages personnels. Il propose ironiquement d'interdire les compilateurs, au motif que seul l'assembleur prouverait la compréhension de la machine, puis les éditeurs pour les messages de commit, et qualifie ce type de règle d'absurde. Le projet ne fera pas de règles interdisant un outil pour une tâche. Son attente est que chacun fasse de son mieux et comprenne ce qu'il fait, ce qui dépend peu des outils ; et les personnes qu'il respecte ne fuient pas les outils nouveaux.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| The Register | ORGANISATION | publie | article Linux kernel devs drop obligatory confession | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| Thomas Claburn | PERSONNE | travaille_chez | The Register | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Maintainers Summit | EVENEMENT | s_oppose_à | Tag Assisted-by | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| Tag Assisted-by | CONCEPT | fait_partie_de | Linux | TECHNOLOGIE | 0.85 | STATIQUE | déclaré_article |
| Sasha Levin | PERSONNE | travaille_chez | Nvidia | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Sasha Levin | PERSONNE | affirme_que | le Maintainers Summit a trouvé un consensus pour déprécier le tag Assisted-by | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| Greg Kroah-Hartman | PERSONNE | affirme_que | les LLM sont assez bons pour trouver des bugs, le code n'étant que des motifs | AFFIRMATION | 0.90 | DYNAMIQUE | déclaré_article |
| Jeff Layton | PERSONNE | travaille_chez | Red Hat | ORGANISATION | 0.92 | DYNAMIQUE | déclaré_article |
| Jeff Layton | PERSONNE | s_oppose_à | Tag Assisted-by | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| Jeff Layton | PERSONNE | affirme_que | le tag fait de la publicité gratuite aux éditeurs de LLM propriétaires | AFFIRMATION | 0.90 | STATIQUE | déclaré_article |
| Laurent Pinchart | PERSONNE | a_créé | Ideas on Board | ORGANISATION | 0.90 | STATIQUE | déclaré_article |
| Laurent Pinchart | PERSONNE | soutient | Tag Assisted-by | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| Linus Torvalds | PERSONNE | s_oppose_à | Laurent Pinchart | PERSONNE | 0.85 | STATIQUE | déclaré_article |
| Linus Torvalds | PERSONNE | affirme_que | la compréhension du code par le contributeur dépend peu des outils qu'il utilise | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Linus Torvalds | PERSONNE | dirige | Linux | TECHNOLOGIE | 0.95 | DYNAMIQUE | généré_assistant |
| Claude Code | TECHNOLOGIE | utilise | Provenance du code | CONCEPT | 0.80 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Thomas Claburn | PERSONNE | rôle | AI and software reporter, The Register | AJOUT |
| The Register | ORGANISATION | secteur | Presse technique britannique | AJOUT |
| article Linux kernel devs drop obligatory confession | DOCUMENT | catégorie | Article The Register, 14 octobre 2026 | AJOUT |
| Tag Assisted-by | CONCEPT | définition | Mention obligatoire dans le message de commit de l'usage d'un outil de codage avancé ; proposée en juillet 2025, documentée en janvier 2026, dépréciée en octobre 2026 | AJOUT |
| Maintainers Summit | EVENEMENT | catégorie | Réunion annuelle des mainteneurs du noyau Linux | AJOUT |
| Sasha Levin | PERSONNE | rôle | Développeur du noyau Linux, ingénieur chez Nvidia | AJOUT |
| Greg Kroah-Hartman | PERSONNE | rôle | Mainteneur historique du noyau Linux | AJOUT |
| Jeff Layton | PERSONNE | rôle | Développeur du noyau Linux chez Red Hat | AJOUT |
| Laurent Pinchart | PERSONNE | rôle | Développeur du noyau Linux, fondateur d'Ideas on Board | AJOUT |
| Linus Torvalds | PERSONNE | rôle | Créateur et mainteneur principal du noyau Linux | AJOUT |
| Provenance du code | CONCEPT | définition | Mention de l'outil ou de l'agent ayant contribué à un code ou un commit | AJOUT |
| Linux | TECHNOLOGIE | catégorie | Noyau de système d'exploitation open source | AJOUT |
