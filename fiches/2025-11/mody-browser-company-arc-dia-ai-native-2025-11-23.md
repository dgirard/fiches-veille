# mody-browser-company-arc-dia-ai-native-2025-11-23
## Veille
The Browser Company - Arc Browser - Dia Browser - AI Native Product - Prompt Injection - Model Behavior

## Titre Article
From Arc to Dia: Lessons learned in building AI Browser

## Date
2025-11-23

## URL
https://www.youtube.com/live/cMSprbJ95jg?si=4HnxK8w1ELvSr4tz&t=20655

## Keywords
The Browser Company, Arc, Dia, AI Browser, Model Behavior, Prompt Injection, Jipa, Prototyping, Security, UX Design

## Authors
Samir Mody (Head of AI Engineering, The Browser Company)

## Ton
**Profil:** Product-Engineering | Design-Centric | Réflexif | Transparent

Le ton est celui d'une startup focalisée sur le produit et le design. Samir Mody partage une histoire d'évolution (de Arc à Dia) avec humilité ("we haven't achieved our vision yet"). Il insiste sur le "craft" (l'artisanat) du comportement des modèles et l'importance de l'itération rapide. Le discours mêle technique (Prompt Injection, Jipa) et philosophie produit (l'IA comme partenaire).

## Pense-betes
- **Transition Arc -> Dia** : Arc était une amélioration incrémentale. Dia est une refonte "AI Native" complète, construite pour la vitesse, la sécurité et l'IA.
- **Outils dans le produit ("Tools in Product")** : Ils ont intégré les outils de prototypage et d'édition de prompts *directement* dans la version "dogfood" du navigateur. Cela permet à toute l'entreprise (CEO, ops, designers) d'itérer sur l'IA avec leur propre contexte d'utilisation.
- **Jipa (technique d'optimisation)** : Utilisation d'une méthode appelée "Jipa" pour l'optimisation automatique des prompts (hill climbing) sans fine-tuning coûteux.
- **Model Behavior comme discipline** : Le comportement du modèle est un "craft" à part entière (ton, style, prise de décision). Une équipe "Model Behavior" s'est formée organiquement, incluant des non-ingénieurs (ex: stratégie & ops) qui étaient meilleurs pour prompter.
- **Sécurité AI (Prompt Injection)** : Le navigateur est un "lethal trifecta" (accès données privées + contenu non fiable + communication externe).
    - Les solutions techniques (tags XML, séparation instructions/données) ne suffisent pas.
    - **Solution UX** : Le design doit pallier les failles. Ex: Pour l'autofill ou l'envoi d'email, toujours une étape de confirmation explicite en "plain text" pour que l'utilisateur valide ce que l'IA va faire, contrant une injection invisible.

## RésuméDe400mots
Samir Mody, Head of AI Engineering chez The Browser Company, raconte la transition de leur produit phare **Arc** vers **Dia**, un nouveau navigateur conçu dès le départ comme "AI Native". Si Arc a repensé l'interface, Dia repense le moteur même de l'interaction web autour de l'IA.

Mody partage trois leçons clés de cette aventure :
1.  **Intégrer les outils d'itération dans le produit** : Au lieu d'outils développeurs séparés, ils ont intégré l'éditeur de prompts et les configurations de modèles directement dans le navigateur utilisé par l'équipe. Cela a permis à tous les employés (y compris le CEO et les équipes Ops) de prototyper des fonctionnalités IA avec leur propre contexte de navigation réel, accélérant massivement l'innovation et la pertinence des idées.
2.  **Le "Model Behavior" est un métier** : Définir comment l'IA se comporte (ton, décision, autonomie) est une nouvelle discipline. Chez The Browser Company, l'équipe "Model Behavior" s'est formée organiquement lorsqu'un membre de l'équipe Opérations (non-ingénieur) a réécrit les prompts pendant un week-end, améliorant drastiquement le produit. Cela prouve que le "prompt engineering" est autant une question de sensibilité produit que de technique. Ils utilisent aussi des techniques automatisées comme **Jipa** pour optimiser les prompts.
3.  **La sécurité est une propriété émergente du produit** : Le navigateur est exposé à un risque majeur : l'**injection de prompt** (un site web malveillant détournant l'IA du navigateur). Mody explique que les protections techniques seules (délimiteurs, instructions système) sont insuffisantes. La sécurité doit être intégrée dans l'UX. Par exemple, pour l'outil de remplissage de formulaire (Autofill), Dia impose une étape de confirmation où l'utilisateur voit exactement quelles données vont être insérées, empêchant l'IA d'exfiltrer des données secrètement à cause d'une instruction cachée dans la page web.

Il conclut en affirmant que construire un produit IA n'est pas juste une évolution technique, mais une transformation complète de la culture d'entreprise, du recrutement à la manière de collaborer.
