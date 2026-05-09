# TDD

> **Type** : METHODOLOGIE | 5 relations | 2 fiches sources

## Attributs

- **cycle** : Red → Green → Refactor, un test à la fois
- **description** : Test-Driven Development, pratique recommandée dans le workflow

## Relations (comme sujet)

### améliore

- [[kb/_entites-mineures#qualité-du-code\|qualité du code]] (CONCEPT) — 0.92, ATEMPOREL
  - [[fiches/2025-10/coding-agents-methodology-vincent-2025-10-05\|Méthodologie d'utilisation agents IA pour développement - Workflow multi-sessions - Blog Fsck]]

### est

- [[kb/_entites-mineures#outil-pas-religion\|outil pas religion]] (CONCEPT) — 0.96, ATEMPOREL
  - [[fiches/2022-12/eveillard-tdd-is-dead-long-live-testing-reponse-dhh-2022-12-07\|**Mathieu Eveillard** publie sur son blog personnel le **7 décembre 2022** (dernière mise à jour 17 mars 2025) une **contre-argumentation point à point** au célèbre essai de **David Heinemeier Hansson (DHH)** *"TDD is dead. Long live testing."* (RailsConf 2014). Article catégorisé **craft / best-of**, position d'**artisan logiciel** qui défend le **Test-Driven Development** sans dogmatisme. **Distinction-pivot** que DHH manque selon Eveillard : ***"Test-first"*** (écrire tous les tests avant le moindre code) vs ***"Test-Driven Development"*** (les tests me **guident** dans l'écriture du code, donc j'écris à chaque fois un peu de code *"en réaction"* à un nouveau test). DHH critique le *Test-first* en l'appelant TDD — confusion qui **cache une tout autre façon de programmer**. **Réponses point à point** : (1) *"TDD as hammer to beat down the nonbelievers"* — Eveillard concède le point déontologique mais redéfinit *"bon code"* : pas seulement absence de bugs mais **tests unitaires fins** documentant le comportement au plus bas niveau, co-localisés avec le code, **filet de sécurité** ; (2) *"Rebalance from unit to system"* — TDD **ne dit rien** des tests système et **ne dit pas** qu'il n'y a rien en dehors du TDD ; tests système ne **remplacent pas** unitaires (impôt sur le revenu en e2e n'a aucun sens) ; **pyramide de tests** — chaque type apporte sa pierre, unitaires pour feedback **millisecondes** + détection bug précoce ; (3) *"Horrendous monstrosities of architecture (service objects, command patterns)"* — Eveillard répond qu'il **ne connaît pas ces effets en programmation fonctionnelle**, donc l'effet est probablement dû à la **POO**, pas au TDD ; mais concède que trop d'injection de dépendances peut coupler test et implémentation. **Conclusion équilibrée** : *"Le TDD n'est pas une religion, c'est un outil"*. Le TDD se prête particulièrement bien au **code du domaine** (noyau fonctionnel d'un *bounded context*, *cœur de l'hexagone*) — moteur de calcul, règles de gestion fines, cas limites — ***"30% au plus de la codebase"***. Mention de la **Loi de l'Instrument** (si l'outil n'aide pas, c'est qu'on tombe dedans). **Pertinence dossier** : article **craft hors-corpus IA** mais à archiver pour positionner les débats actuels sur les coding agents (Beck *Augmented Coding Beyond Vibes* 2025-06-25, Vibe Coding vs TDD, Frizzo *writing muscle atrophy*) dans la lignée historique des débats craft autour du TDD. À mobiliser comme **fond de bibliothèque** pour formations.]]

### se_prête_à

- [[kb/_entites-mineures#code-du-domaine,-bounded-context,-cœur-hexagone\|code du domaine, bounded context, cœur hexagone]] (CONCEPT) — 0.94, ATEMPOREL
  - [[fiches/2022-12/eveillard-tdd-is-dead-long-live-testing-reponse-dhh-2022-12-07\|**Mathieu Eveillard** publie sur son blog personnel le **7 décembre 2022** (dernière mise à jour 17 mars 2025) une **contre-argumentation point à point** au célèbre essai de **David Heinemeier Hansson (DHH)** *"TDD is dead. Long live testing."* (RailsConf 2014). Article catégorisé **craft / best-of**, position d'**artisan logiciel** qui défend le **Test-Driven Development** sans dogmatisme. **Distinction-pivot** que DHH manque selon Eveillard : ***"Test-first"*** (écrire tous les tests avant le moindre code) vs ***"Test-Driven Development"*** (les tests me **guident** dans l'écriture du code, donc j'écris à chaque fois un peu de code *"en réaction"* à un nouveau test). DHH critique le *Test-first* en l'appelant TDD — confusion qui **cache une tout autre façon de programmer**. **Réponses point à point** : (1) *"TDD as hammer to beat down the nonbelievers"* — Eveillard concède le point déontologique mais redéfinit *"bon code"* : pas seulement absence de bugs mais **tests unitaires fins** documentant le comportement au plus bas niveau, co-localisés avec le code, **filet de sécurité** ; (2) *"Rebalance from unit to system"* — TDD **ne dit rien** des tests système et **ne dit pas** qu'il n'y a rien en dehors du TDD ; tests système ne **remplacent pas** unitaires (impôt sur le revenu en e2e n'a aucun sens) ; **pyramide de tests** — chaque type apporte sa pierre, unitaires pour feedback **millisecondes** + détection bug précoce ; (3) *"Horrendous monstrosities of architecture (service objects, command patterns)"* — Eveillard répond qu'il **ne connaît pas ces effets en programmation fonctionnelle**, donc l'effet est probablement dû à la **POO**, pas au TDD ; mais concède que trop d'injection de dépendances peut coupler test et implémentation. **Conclusion équilibrée** : *"Le TDD n'est pas une religion, c'est un outil"*. Le TDD se prête particulièrement bien au **code du domaine** (noyau fonctionnel d'un *bounded context*, *cœur de l'hexagone*) — moteur de calcul, règles de gestion fines, cas limites — ***"30% au plus de la codebase"***. Mention de la **Loi de l'Instrument** (si l'outil n'aide pas, c'est qu'on tombe dedans). **Pertinence dossier** : article **craft hors-corpus IA** mais à archiver pour positionner les débats actuels sur les coding agents (Beck *Augmented Coding Beyond Vibes* 2025-06-25, Vibe Coding vs TDD, Frizzo *writing muscle atrophy*) dans la lignée historique des débats craft autour du TDD. À mobiliser comme **fond de bibliothèque** pour formations.]]

## Relations (comme objet)

- [[kb/Kent-Beck\|Kent Beck]] **applique** → TDD — 0.98
- [[kb/Kent-Beck\|Kent Beck]] **a_créé** → TDD — 0.97

## Fiches sources

- [[fiches/2025-06/augmented-coding-beyond-vibes-kent-beck-2025-06-25\|Augmented Coding vs Vibe Coding - Kent Beck - B+ Tree - GenAI - TDD - Rust Python - Substack]]
- [[fiches/2025-10/coding-agents-methodology-vincent-2025-10-05\|Méthodologie d'utilisation agents IA pour développement - Workflow multi-sessions - Blog Fsck]]
