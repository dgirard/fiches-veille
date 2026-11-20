---
themes: [politique-regulation, economie-marche, produits-services]
source: SFEIR
---
# sfeir-ia-semaine-8-15-octobre-2026-breves-2026-10-15

## Veille

Revue de brèves **SFEIR AI** publiée sur sfeir.com le **15 octobre 2026** (~5 000 signes, cinq nouvelles, onze sources), qui complète les articles longs de la semaine. Cinq faits datés du 12 au 14 octobre. **(1)** **Huit États américains** (Arizona, Arkansas, Idaho, Iowa, Kansas, Montana, Nebraska, Virginie-Occidentale) poursuivent **OpenAI** pour tromperie sur la sécurité de ChatGPT et nuisance publique ; ils demandent notamment l'interdiction de modèles *« qui s'améliorent eux-mêmes sans garantie d'alignement »*. **(2)** OpenAI fixe au **14 janvier 2027** la sortie de l'API de gpt-4o, gpt-4o-mini, gpt-4.1 et gpt-4.1-mini, avec **gpt-6-luna** comme remplaçant unique. **(3)** **Character.ai** se place sous **Chapter 11** (actifs estimés entre 50 et 100 M$) ; Disney paie 20 M$ pour une partie de la propriété intellectuelle. **(4)** **Microsoft** présente **Maia 300**, jusqu'à **7 fois** le débit en tokens de Maia 200 par baie, déploiement en 2027. **(5)** **Nvidia** entre au capital de **Doctolib** (minoritaire, sans siège) et engage **250 M$** de calcul sur cinq ans pour la recherche britannique en sécurité de l'IA. Format de veille hebdomadaire, sans analyse transversale.

## Titre Article

IA, semaine du 8 au 15 octobre 2026 : cinq autres nouvelles à retenir

## Date

2026-10-15

## URL

https://www.sfeir.com/articles/ia-semaine-8-15-octobre-2026-breves/

## Keywords

actualité IA, brèves, OpenAI, ChatGPT, procès des États américains, protection des consommateurs, nuisance publique, sécurité des mineurs, dépréciation de modèles, GPT-4o, GPT-4.1, GPT-6 Luna, shutdown_date, Character.ai, Chapter 11, Disney, Microsoft, Maia 300, puce d'inférence, Nvidia, Doctolib, Pigment, Genesis AI, Entalpic, sécurité de l'IA, Royaume-Uni

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : brèves d'actualité hebdomadaires pour un public de décideurs et de développeurs qui suivent le marché de l'IA. Français journalistique, factuel, un paragraphe à trois paragraphes par nouvelle.

**Style** : chaque brève commence par une date et un acteur, puis donne les chiffres, les noms et les échéances. Pas d'introduction thématique ni de conclusion ; le chapeau énumère les cinq faits. Les détails opérationnels utiles aux développeurs sont conservés (versions exactes des modèles dépréciés, champ `shutdown_date` de `GET /v1/models`).

**Position épistémique** : attribution systématique (« selon », « cité par l'AFP », « CBS relève »). Le texte signale ce que l'annonce ne contient pas (Maia 300 : ni puissance de calcul ni consommation publiées). Aucune prise de position éditoriale sur les procès ou la faillite ; les griefs sont rapportés comme ceux des procureurs ou du PDG.

## Pense-betes

- **Procès OpenAI (14 octobre)** : 8 États, procureurs des deux partis, une plainte par État (Idaho : Fourth Judicial District Court, comté d'Ada). Griefs : tromperie sur la sécurité de ChatGPT, assistant complaisant qui conforte des idées délirantes. Demandes : injonctions, interdiction de modèles auto-améliorants sans garantie d'alignement, pénalités. La Floride mène une procédure distincte depuis juin.
- **Dépréciations OpenAI** :
  - 14 janvier 2027 : gpt-4o (2024-08-06, 2024-11-20), gpt-4o-mini, gpt-4.1, gpt-4.1-mini → **gpt-6-luna**
  - 23 octobre 2026 : gpt-4.1-nano et gpt-4o-2024-05-13 → gpt-5.6-luna et gpt-5.6-sol
  - fine-tunés : calendrier du modèle de base ; repérage via `shutdown_date`
  - famille GPT-6 : Astra, Sol, Luna (Sol et Luna dans l'API depuis le 22 septembre)
- **Character.ai (12 octobre)** : Chapter 11 volontaire ; PDG Colin Adams invoque procès liés à des suicides d'adolescents, actions du Texas, Kentucky, Pennsylvanie, coûts d'IA croissants. Vente sous contrôle du tribunal visée fin novembre-début décembre ; fermeture sans repreneur. La politique de confidentialité autorise le transfert des conversations et voix en cas de vente (CBS).
- **Maia 300 (12 octobre)** : 3e génération, principal système d'inférence de Microsoft, ×7 débit par baie vs Maia 200 (janvier 2026), déploiements multi-gigawatts en 2027.
- **Nvidia à Paris (13 octobre)** : participations dans Doctolib, Pigment, Genesis AI, Entalpic. Doctolib veut ses propres modèles, sans dépendre d'OpenAI ni d'Anthropic, assistants patients/soignants 2027-2028.
- **Nvidia au Royaume-Uni** : 250 M$ de calcul sur 5 ans ; bénéficiaires BOLD (Oxford), SOFAIR (UCL), Imperial Frontier AI Research Lab ; sécurité des agents et modèles ouverts, environnements isolés, benchmarks.
- **À relier** : [[sfeir-grok-voice-3-centre-appels-2026-10-15]], [[sfeir-muse-wonder-meta-muse-code-2026-10-15]] (articles longs de la même semaine).

## RésuméDe400mots

Cette revue de SFEIR rassemble cinq nouvelles de l'intelligence artificielle survenues entre le 12 et le 14 octobre 2026, en complément des articles longs publiés la même semaine.

La première concerne OpenAI, attaquée le 14 octobre par huit États américains (Arizona, Arkansas, Idaho, Iowa, Kansas, Montana, Nebraska et Virginie-Occidentale) dans une action coordonnée menée par des procureurs des deux partis. Chaque État a déposé sa plainte devant ses propres tribunaux. Les procureurs reprochent à OpenAI d'avoir trompé le public sur la sécurité de ChatGPT, invoquent la nuisance publique et décrivent un assistant complaisant qui conforte des idées délirantes et pousse certains utilisateurs, y compris des adolescents, à se faire du mal. Ils demandent des injonctions, l'interdiction de développer des modèles qui s'améliorent eux-mêmes sans garantie d'alignement, des pénalités et des dommages.

Le même jour, OpenAI a annoncé que gpt-4o, gpt-4o-mini, gpt-4.1 et gpt-4.1-mini quitteront son API le 14 janvier 2027, avec gpt-6-luna comme remplaçant unique. Deux modèles plus anciens partent dès le 23 octobre 2026. Les modèles fine-tunés suivent le calendrier de leur modèle de base, et OpenAI conseille de lire le champ shutdown_date pour repérer les modèles concernés.

Character.ai s'est placée le 12 octobre sous la protection du Chapter 11, avec des actifs estimés entre 50 et 100 millions de dollars. Son PDG invoque des procès liant l'application à des suicides d'adolescents, des actions de plusieurs États et des coûts d'IA croissants. Disney paie 20 millions de dollars pour une partie de la propriété intellectuelle ; une vente sous contrôle du tribunal est visée pour la fin de l'année, faute de quoi la plateforme fermera. CBS note que la politique de confidentialité autorise le transfert des données des utilisateurs en cas de vente.

Microsoft a présenté Maia 300, troisième génération de sa puce d'inférence, annoncée jusqu'à sept fois plus rapide que Maia 200 en débit de tokens par baie, pour des déploiements à partir de 2027 ; ni puissance de calcul ni consommation n'ont été publiées.

Enfin, Nvidia a annoncé à Paris des prises de participation dans Doctolib, Pigment, Genesis AI et Entalpic. Doctolib veut développer ses propres modèles sans dépendre d'OpenAI ni d'Anthropic. Nvidia s'est aussi engagé à fournir 250 millions de dollars de calcul sur cinq ans aux chercheurs britanniques en sécurité de l'IA.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | IA, semaine du 8 au 15 octobre 2026 : cinq autres nouvelles à retenir | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| procès des huit États américains contre OpenAI | EVENEMENT | s_applique_à | ChatGPT | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| procès des huit États américains contre OpenAI | EVENEMENT | affirme_que | OpenAI a trompé le public sur la sécurité de ChatGPT | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| OpenAI | ORGANISATION | publie | GPT-6 | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| GPT-6 | TECHNOLOGIE | remplace | GPT-4o | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| GPT-6 | TECHNOLOGIE | remplace | GPT-4.1 | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| OpenAI | ORGANISATION | recommande | lire le champ shutdown_date de GET /v1/models pour repérer les modèles dépréciés | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Character.ai | ORGANISATION | mesure | actifs estimés entre 50 et 100 M$ au dépôt du Chapter 11 | MESURE | 0.88 | STATIQUE | déclaré_article |
| Disney | ORGANISATION | collabore_avec | Character.ai | ORGANISATION | 0.82 | STATIQUE | déclaré_article |
| Microsoft | ORGANISATION | publie | Maia 300 | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Maia 300 | TECHNOLOGIE | remplace | Maia 200 | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Maia 300 | TECHNOLOGIE | améliore | jusqu'à 7 fois le débit en tokens par baie face à Maia 200 | MESURE | 0.85 | STATIQUE | déclaré_article |
| Nvidia | ORGANISATION | collabore_avec | Doctolib | ORGANISATION | 0.9 | DYNAMIQUE | déclaré_article |
| Doctolib | ORGANISATION | affirme_que | Doctolib développera ses propres modèles sans dépendre d'OpenAI ni d'Anthropic | AFFIRMATION | 0.85 | DYNAMIQUE | déclaré_article |
| Nvidia | ORGANISATION | mesure | 250 M$ de calcul sur cinq ans pour la recherche britannique en sécurité de l'IA | MESURE | 0.88 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| SFEIR | ORGANISATION | secteur | ESN / cabinet d'ingénierie logicielle, éditeur de sfeir.com | AJOUT |
| procès des huit États américains contre OpenAI | EVENEMENT | date | 14 octobre 2026, Arizona, Arkansas, Idaho, Iowa, Kansas, Montana, Nebraska, Virginie-Occidentale | AJOUT |
| GPT-6 | TECHNOLOGIE | variantes | Astra, Sol, Luna ; gpt-6-luna remplaçant unique de GPT-4o et GPT-4.1 | AJOUT |
| GPT-4o | TECHNOLOGIE | fin de vie API | 14 janvier 2027 | AJOUT |
| GPT-4.1 | TECHNOLOGIE | fin de vie API | 14 janvier 2027 (nano : 23 octobre 2026) | AJOUT |
| Character.ai | ORGANISATION | statut | Chapter 11 volontaire depuis le 12 octobre 2026, PDG Colin Adams | AJOUT |
| Maia 300 | TECHNOLOGIE | catégorie | Puce d'inférence Microsoft de 3e génération, déploiement 2027 | AJOUT |
| Doctolib | ORGANISATION | actionnariat | Nvidia actionnaire minoritaire sans siège au conseil | AJOUT |
| Nvidia | ORGANISATION | investissements | Doctolib, Pigment, Genesis AI, Entalpic (annoncés à Paris le 13 octobre 2026) | AJOUT |
