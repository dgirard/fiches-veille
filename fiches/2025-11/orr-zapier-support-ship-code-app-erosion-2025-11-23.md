# orr-zapier-support-ship-code-app-erosion-2025-11-23
## Veille
Support technique autonome livrant du code - Résolution de l'érosion applicative - Zapier ingénierie
## Titre Article
Empowering Support to Ship Code: Solving App Erosion
## Date
2025-11-23
## URL
https://www.youtube.com/live/cMSprbJ95jg?si=4HnxK8w1ELvSr4tz
## Keywords
support technique, érosion applicative, Zapier, agents support, livraison code, automatisation support, intégrations API, maintenance continue
## Authors
Lisa Orr
## Ton
**Profil** : Leader ingénierie chez Zapier, perspective opérationnelle pragmatique, registre solution-oriented, présentation axée sur des problèmes réels

**Style** : Présentation pratique et directe, centrée sur la résolution de problèmes concrets. Ton professionnel mais accessible, utilisant des exemples tirés de l'expérience Zapier. L'autorité provient de la gestion d'intégrations à grande échelle. Public cible : leaders techniques, équipes support et développeurs confrontés à la maintenance d'intégrations complexes.
## Pense-betes
- **App Erosion** : 8000+ intégrations Zapier, 14 ans d'existence, APIs changeant constamment
- **Analogie Grand Canyon** : Érosion naturelle vs érosion applicative, jamais ne s'arrête
- **Backlog crisis** : Tickets arrivent plus vite qu'ils ne sont résolus
- **Experiment 1** : Support passe de triage à fixing bugs (guard rails, 4 apps cibles)
- **Experiment 2 - Scout** : Projet de codegen pour résoudre l'érosion
- **Pain points** : 50% du temps passé à rassembler le contexte
- **Solution architecture** : Context Analyzer → Diff Generator → Test Generator
- **Résultats** : 97% taux de réussite des MR, réduction temps de résolution de 72h à minutes
## RésuméDe400mots
Lisa Orr, leader ingénierie chez Zapier, présente comment l'entreprise combat "l'érosion applicative" en autonomisant les équipes support pour livrer du code. Utilisant l'analogie du Grand Canyon - où l'érosion naturelle crée de la beauté sur des millions d'années - elle contraste avec l'érosion applicative qui dégrade continuellement les 8000+ intégrations de Zapier depuis 14 ans.

Le problème est critique : les APIs tierces changent constamment, créant une **crise du backlog** où les tickets arrivent plus vite qu'ils ne sont résolus. Cela génère des problèmes de fiabilité, une mauvaise expérience client, et potentiellement du churn. Face à cette réalité, Zapier lance deux expériences parallèles il y a deux ans.

**Experiment 1** transforme le rôle du support : de simple triage vers la correction active de bugs. L'approche est prudente avec des garde-fous : focus sur 4 apps cibles, revue obligatoire par l'ingénierie, limitation aux corrections d'apps. La motivation est forte car l'érosion représente une source majeure de bugs, le support est avide d'apprendre (beaucoup veulent devenir ingénieurs), et certains membres aidaient déjà officieusement.

**Experiment 2 - Scout** utilise l'IA générative pour accélérer les corrections. Le processus commence par du "dog fooding" (Orr elle-même corrige des apps), l'observation des ingénieurs et du support, et l'identification des pain points. Découverte clé : **50% du temps est passé à rassembler le contexte** nécessaire pour comprendre le problème.

L'architecture de Scout comprend trois composants principaux :
1. **Context Analyzer** : Rassemble automatiquement tickets, logs d'erreurs, documentation API, code source
2. **Diff Generator** : Crée les corrections basées sur le contexte analysé
3. **Test Generator** : Génère des tests pour valider les corrections

Les résultats sont remarquables. Le **taux de succès des merge requests atteint 97%**, avec seulement 3% nécessitant des modifications mineures. Le temps de résolution passe de **72 heures à quelques minutes**. L'impact culturel est profond : le support se sent valorisé, l'ingénierie est libérée pour l'innovation, et la frontière entre les rôles s'estompe.

Orr souligne que cette transformation n'est pas qu'une optimisation technique mais une nécessité stratégique. Dans un écosystème où les intégrations sont centrales et l'érosion inévitable, la capacité de maintenance agile devient un avantage concurrentiel. L'autonomisation du support via l'IA représente une évolution organisationnelle fondamentale pour survivre dans un monde d'APIs en perpétuelle mutation.