# forrestchang-andrej-karpathy-skills-claude-code-2026-01-27
## Veille
Guidelines Claude Code inspirées Karpathy - 4 principes anti-bloat

## Titre Article
Andrej Karpathy Skills for Claude Code

## Date
2026-01-27

## URL
https://github.com/forrestchang/andrej-karpathy-skills

## Keywords
Claude Code, Andrej Karpathy, skills, CLAUDE.md, principes codage IA, simplicité, modifications chirurgicales, prompt engineering, LLM limitations, bonnes pratiques développement

## Authors
forrestchang (GitHub), basé sur observations d'Andrej Karpathy

## Ton
**Profil** : Documentation technique concise, registre prescriptif et pratique, niveau technique intermédiaire

**Description** : Le README adopte un ton direct et pragmatique, structuré autour de problèmes observés et de solutions concrètes. Le style est celui d'une documentation open source bien écrite : sections claires, exemples d'installation copiables, principes numérotés. L'autorité repose sur la référence à Andrej Karpathy (figure respectée de l'IA) et sur l'observation empirique des comportements problématiques des LLMs. Le public cible est constitué de développeurs utilisant Claude Code et cherchant à améliorer la qualité des outputs.

## Pense-betes
- **3 456 stars** en quelques jours - signe d'un besoin réel dans la communauté Claude Code
- **Problèmes identifiés par Karpathy** :
  1. Hypothèses erronées sans vérification
  2. Sur-ingénierie et abstractions inutiles
  3. Modifications/suppressions de code non compris
- **Principe 1 - Think Before Coding** : Expliciter les hypothèses, poser des questions clarifiantes, présenter plusieurs approches en cas d'ambiguïté, s'arrêter quand confus
- **Principe 2 - Simplicity First** : Code minimal répondant uniquement à la demande, pas de features spéculatives, pas d'abstractions inutiles, pas de configurabilité non demandée. Test : "un ingénieur expérimenté trouverait-il ça over-engineered ?"
- **Principe 3 - Surgical Changes** : Modifier uniquement le code lié à la demande, préserver style et commentaires existants, ne pas supprimer du dead code préexistant sauf demande explicite
- **Principe 4 - Goal-Driven Execution** : Convertir tâches en critères de succès vérifiables. Ex: "add validation" → "write tests for invalid inputs, then make them pass"
- **Insight clé** : Les modèles excellent à "boucler jusqu'à atteindre un objectif spécifique" - définir des critères de succès plutôt que des instructions impératives
- **Installation** : Plugin Claude (`claude plugins add`) ou fichier CLAUDE.md par projet
- **Caveat important** : Pour changements triviaux (typos, one-liners évidents), appliquer du bon sens plutôt que la rigueur complète

## RésuméDe400mots
Ce dépôt GitHub propose un ensemble de guidelines pour Claude Code, inspirées des observations d'Andrej Karpathy sur les limitations des LLMs en développement logiciel. Avec plus de 3 400 stars en quelques jours, il répond manifestement à un besoin de la communauté.

**Problèmes identifiés** : Karpathy a observé que les modèles tendent à faire des hypothèses erronées sans vérification et à "partir dans une direction" sans valider leurs présupposés. Ils sur-compliquent souvent les solutions, créant des abstractions inutiles quand des approches simples suffiraient. Enfin, ils modifient ou suppriment parfois du code qu'ils ne comprennent pas entièrement, même sans rapport avec la tâche demandée.

**Quatre principes fondateurs** :

Le premier principe, "Think Before Coding", impose d'expliciter les hypothèses et de poser des questions clarifiantes plutôt que de deviner. En cas d'ambiguïté, présenter plusieurs approches viables. S'arrêter et reconnaître quand on est confus.

Le deuxième principe, "Simplicity First", prescrit d'écrire le code minimal répondant uniquement à ce qui est demandé. Éviter les features spéculatives, les abstractions inutiles, la configurabilité non sollicitée. Supprimer la gestion d'erreurs pour des scénarios impossibles. Le test : un ingénieur expérimenté considèrerait-il ce code comme over-engineered ?

Le troisième principe, "Surgical Changes", limite les modifications au code directement lié à la demande utilisateur. Préserver le style et les commentaires existants. Ne supprimer du code mort préexistant que sur demande explicite.

Le quatrième principe, "Goal-Driven Execution", convertit les tâches en critères de succès spécifiques et vérifiables. Plutôt que "ajouter de la validation", formuler "écrire des tests pour les inputs invalides, puis les faire passer". Utiliser des plans numérotés brefs avec étapes de vérification.

**Insight fondamental** : Les modèles excellent à "boucler jusqu'à atteindre des objectifs spécifiques". Plutôt que d'émettre des instructions impératives, définir des critères de succès clairs et laisser le système itérer vers ces objectifs.

**Installation et usage** : Le dépôt peut être installé comme plugin Claude (`claude plugins add`) ou téléchargé comme fichier CLAUDE.md par projet. Les guidelines sont conçues pour être fusionnées avec des règles spécifiques au projet.

**Indicateurs de succès** : Les diffs ne contiennent que les changements demandés, le code évite la complexité inutile dès la première tentative, des questions clarifiantes précèdent l'implémentation, les pull requests restent focalisées sans refactoring tangentiel.

**Caveat** : Ces guidelines privilégient la précision sur la vitesse. Pour les changements triviaux (typos, modifications one-liner évidentes), appliquer du bon sens plutôt que la rigueur complète.
