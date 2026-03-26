  
**RAPPORT D'ANALYSE**

**ALMIA**

La plateforme d'IA générative d'AG2R LA MONDIALE

*AG2R LA MONDIALE Intelligence Artificielle*

Mars 2026

*Recherche et synthèse multi-sources*  
**Table des matières**

*Note : Ce rapport a été constitué à partir d'une recherche approfondie sur les sources publiques disponibles : communiqués de presse, articles de presse spécialisée, interviews, posts LinkedIn, interventions en conférences et vidéos.*

# **1\. Synthèse exécutive**

Almia (acronyme d'AG2R LA MONDIALE Intelligence Artificielle) est la plateforme propriétaire d'intelligence artificielle générative développée par le groupe AG2R LA MONDIALE, acteur majeur de la protection sociale et patrimoniale en France avec plus de 15 millions d'assurés et 500 000 entreprises clientes.

Développée en interne à partir de début 2024, dévoilée en interne en avril 2024 et officialisée publiquement en novembre 2024, Almia s'inscrit dans une stratégie IA initiée dès 2023\. Elle est hébergée sur une infrastructure cloud sécurisée en France, via S3NS, la coentreprise entre Thales et Google Cloud. La plateforme repose sur le socle technique de Google Cloud Platform (GCP) tout en se revendiquant agnostique vis-à-vis des modèles de langage (LLM).

Fin 2025, Almia comptait 7 000 utilisateurs sur les 8300 collaborateurs du groupe, avec près de 1 300 assistants IA créés par les collaborateurs eux-mêmes. Le projet a valu à Pascal Martinez, membre du comité de direction en charge des SI et du digital, le titre de Stratège IT 2025 décerné par CIO Online.

# **2\. Fiche d'identité**

| Nom complet | Almia — AG2R LA MONDIALE Intelligence Artificielle |
| :---- | :---- |
| **Organisation** | AG2R LA MONDIALE — Groupe paritaire et mutualiste, \+115 ans d'existence |
| **Périmètre** | 15 millions d'assurés, 500 000 entreprises, \~15 000 collaborateurs |
| **Sponsor exécutif** | Pascal Martinez — Membre du Comité de Direction Groupe, SI et Digital |
| **Directeur Data & IA** | Ludovic Letort — Directeur Data & IA Factory |
| **Développement** | Interne, démarré en mars 2024 |
| **Lancement interne** | Avril 2024 (Almia Bot, auprès de « Champions IA » représentant les directions métiers du groupe) |
| **Annonce publique** | Novembre 2024 |
| **Ouverture à tous** | 20 janvier 2025 |
| **Infrastructure** | Cloud France — S3NS (Thales × Google Cloud), GCP |
| **Approche LLM** | Multi-LLM et agnostique (Microsoft, Google, etc.) |
| **Utilisateurs (fin 2025\)** | 7 000 utilisateurs actifs / 8 300 collaborateurs |
| **Assistants créés** | \~1 300 assistants développés par les collaborateurs |

# **3\. Contexte et genèse du projet**

## **3.1. AG2R LA MONDIALE : un groupe en pleine transformation**

AG2R LA MONDIALE est le fruit de nombreux rapprochements successifs, ce qui a conduit à un patrimoine applicatif considérable. En 2022, le groupe a lancé un programme de transformation SI majeur de 629 M€ sur 6 ans, visant à réduire le portefeuille de 1 300 à environ 400 applications, avec une orientation forte vers le SaaS. Pascal Martinez, arrivé cette même année après 7 ans chez Covea dont 4 en tant que DSI, pilote ce chantier de refonte massive qui concerne tant les back-offices que les applications clients.

## **3.2. L'IA classique : une histoire antérieure à la GenAI**

Le groupe utilisait déjà des formes classiques d'intelligence artificielle bien avant ChatGPT. Dès 2019, AG2R recherchait une solution pour traiter les 300 000 emails reçus annuellement sur le secteur santé. En 2022, le groupe a adopté la solution d'IA Classify de reciTAL pour la reconnaissance automatique de documents (RAD/LAD). L'IA était également employée pour la reconnaissance de notes d'honoraires manuscrites et l'entrée automatisée de données.

## **3.3. La réaction face à ChatGPT et la naissance d'Almia**

Lors du lancement de ChatGPT en novembre 2022, AG2R LA MONDIALE a adopté une posture prudente et décidé de bloquer l'accès aux outils d'IA générative publics (ChatGPT, etc.) afin de protéger les données clients. Le groupe a néanmoins rapidement perçu le potentiel de la technologie et défini trois règles fondamentales pour encadrer son usage :

* Garantir la cybersécurité et la confidentialité des données

* N’exposer aucun outil d'IA générative directement (frontal) à ses clients

* Déployer l'IA comme aide aux collaborateurs pour accroître leur performance, jamais pour les remplacer

C'est dans ce cadre qu'Almia a été conçu à partir de mars 2024, comme une interface sécurisée permettant d'interroger les LLM du marché sans exposer les données du groupe.

# **4\. Architecture technique et principes de sécurité**

## **4.1. Infrastructure cloud souveraine**

Almia repose sur une infrastructure cloud hébergée en France, s'appuyant sur S3NS, la coentreprise entre Thales et Google Cloud fondée en 2022\. S3NS a obtenu en décembre 2025 la qualification SecNumCloud 3.2 de l'ANSSI pour son offre PREMI3NS, attestant du plus haut niveau de sécurisation des données en France. AG2R LA MONDIALE figure parmi les premiers clients de S3NS avec l'offre « Contrôles locaux avec S3NS ».

## **4.2. Protection des données par vectorisation**

Le mécanisme de protection des données repose sur la vectorisation : les documents internes sont découpés en petites unités de sens avant d'être soumis aux LLM. Les textes d'origine restent stockés en local et ne sont jamais transmis. Seuls les vecteurs, inexploitables tels quels, sont envoyés aux modèles de langage. En retour, l'IA répond en langage intelligible. Ce procédé de RAG (Retrieval-Augmented Generation) permet de contextualiser les questions posées au bot avec les données propres d'AG2R LA MONDIALE.

## **4.3. Approche multi-LLM et agnostique**

Almia permet d'interroger plusieurs LLM du marché (Google Gemini, Microsoft, etc.) et n'est pas liée à un seul fournisseur. Le groupe peut ainsi utiliser le meilleur modèle pour chaque cas d'usage, avec le meilleur rapport qualité-prix, tout en suivant l'évolution très rapide du marché des LLM. La plateforme a également la capacité de connecter des SLM (Small Language Models) pour des usages spécifiques.

# **5\. Les quatre piliers de la plateforme Almia**

Almia n'est pas un simple chatbot : c'est une plateforme modulaire articulée autour de quatre composantes complémentaires.

## **5.1. Almia Bot — Le chatbot sécurisé**

Almia Bot est le point d'entrée principal de la plateforme, fonctionnant de manière similaire à un ChatGPT interne mais avec des garanties de sécurité essentielles en environnement professionnel. Il permet aux collaborateurs de poser des questions à différents LLM, avec la possibilité d'utiliser le RAG pour contextualiser les requêtes à partir des documents internes.

L'une des fonctionnalités clés est la possibilité pour chaque collaborateur de créer ses propres « assistants IA légers », alimentés avec ses données. Ces assistants peuvent rester privés ou être partagés avec d'autres collaborateurs, voire l'ensemble du groupe. Les assistants les plus performants et les plus utilisés sont candidats à l'intégration dans une marketplace interne, commentée et notée par les utilisateurs (système de pouces vers le haut/bas).

## **5.2. Almia Apps — Les applications métier industrialisées**

Almia Apps constitue le deuxième pan de la plateforme. Quand un assistant créé dans Almia Bot démontre une forte adoption et répond à un besoin métier précis, il peut être repris et industrialisé sous forme d'application web dédiée. Cette approche dépasse les limites architecturales du simple chatbot pour offrir des solutions métier complètes.

Exemples d'applications déployées :

* **Analyse des verbatims clients :** traitement de 100 000 à 150 000 retours clients par an pour identifier les irritants du parcours client

* **Génération de campagnes marketing :** l'utilisateur précise le canal (LinkedIn, email, radio), le persona visé (ex : boulangers 30-50 ans avec 20+ collaborateurs) et l'IA génère l'ensemble des assets : livre blanc, photos, textes

* **Analyse comparative des offres :** benchmark automatisé des produits du groupe versus la concurrence

* **Traitement documentaire :** reconnaissance et classification de 30% du million de documents reçus annuellement

* **Sélection des appels d'offres :** lecture préalable et analyse pour aider à décider de l'opportunité de répondre

## **5.3. Almia Dev — Les API pour développeurs**

Almia Dev met à disposition des développeurs informatiques et des équipes actuarielles (travaillant en Java et Python) toutes les possibilités de l'IA générative en matière de code : conception de programmes, analyse et optimisation de code, migration de langage, génération de cas de tests et documentation de code. Environ 80 développeurs testaient déjà GitHub Copilot depuis fin 2024\.

La plateforme expose également des API d'IA générative prêtes à l'emploi que les développeurs peuvent intégrer librement dans leurs applications métier. L'anonymisation automatique de documents est citée comme un exemple emblématique : un besoin fréquent dans l'assurance qui a été significativement amélioré grâce à l'IA générative.

## **5.4. Almia for Actuariat — Aide aux métiers de l'actuariat**

Almia intègre des fonctionnalités spécifiquement dédiées à la chaîne de développement informatique et aux métiers de l'actuariat, incluant la prévision des sinistres et l'aide au développement de modèles prédictifs.

## **5.5. Almia Agents — Des agents métiers pour renforcer l’efficacité opérationnelle**

Plus récemment Almia a commencé à déployer des agents IA orientés métiers basés sur la nouvelle stratégie du groupe “Esprit de conquête” introduite par le nouveau PDG, Fabrice Heyries, arrivé fin 2025\. Fort de la transformation amené par Almia depuis 2024, Fabrice Heyries a souhaité inscrire l’IA comme un levier technologique fondamental de sa nouvelle stratégie permettant de différencier AG2R LA MONDIALE sur son marché.

# **6\. Principaux cas d'usage déployés**

| Domaine | Description de l'usage |
| :---- | :---- |
| **Service client** | Aide aux conseillers pour construire plus rapidement la meilleure réponse ; synthèse automatique des échanges téléphoniques avec suggestion de la prochaine action |
| **Satisfaction client** | Analyse de 100 000 à 150 000 verbatims clients par an pour identifier les irritants du parcours et améliorer les processus |
| **Commercial** | Rédaction de comptes-rendus clients, analyse préalable des appels d'offres en protection sociale (contrats collectifs) |
| **Marketing** | Création de campagnes complètes avec assets multicanaux (LinkedIn, email, radio) ciblés par persona |
| **Documentation** | Traitement de 30% du million de documents reçus par an grâce à la reconnaissance de contenu ; anonymisation automatique |
| **RH / Recrutement** | Assistance au processus de recrutement et à la gestion des talents |
| **Développement IT** | Optimisation, documentation et migration de code ; GitHub Copilot pour \~80 développeurs |
| **Réunions** | Comptes-rendus automatiques de réunions internes |

# **7\. Stratégie de déploiement et conduite du changement**

## **7.1. Les « Champions de l'IA » : un modèle de diffusion par les pairs**

La stratégie de déploiement d'Almia s'appuie sur une communauté de « Champions de l'IA », un dispositif initié par Ludovic Letort, Directeur Data & IA Factory avec l’aide du cabinet de conseil en stratégie IA, WEnvision. Ces collaborateurs issus des différents métiers ont été les premiers à tester l'outil et à faire remonter les cas d'usage pertinents. Ils étaient une centaine au départ, chacun formant et accompagnant ensuite ses collègues sur l'outil, le prompting et les premiers cas d'usage.

## **7.2. Un prérequis de formation obligatoire**

La condition d'accès à Almia est d'avoir suivi trois formations obligatoires : une acculturation à l'IA, un module sur la sécurité et un module sur l'éthique. Cette approche garantit un usage responsable et éclairé de l'outil.

## **7.3. Chronologie de l'adoption**

La trajectoire d'adoption illustre une montée en puissance rapide et maîtrisée :

* **Début 2024 :** début du développement interne

* **Avril 2024 :** déploiement d'Almia Bot auprès des \~100 Champions IA

* **Fin 2024 :** franchissement de la barre des 2 000 utilisateurs

* **20 janvier 2025 :** ouverture à l'ensemble des collaborateurs éligibles

* **Mi-2025 :** 2 500 collaborateurs actifs (et déploiement en cours)

* **Fin 2025 :** 7 000 utilisateurs sur 8 300 collaborateurs, 1 300 assistants créés

# **8\. Gouvernance et conformité**

En parallèle du déploiement d’Almia, une gouvernance IA spécifique a été mise en place chez AG2R LA MONDIALE afin de sécuriser le déploiement de l’IA notamment générative. Un comité de gouvernance IA passe systématiquement en revue toutes les expérimentations d'IA lancées dans le groupe, qu'il s'agisse de solutions internes ou externes.

Ce comité est composé du Directeur IA, du DPO (Data Protection Officer), du RSSI (Responsable de la Sécurité des SI), de représentants de la DRH et des personnes en charge de la conformité RSE. Sa mission inclut la cartographie obligatoire de tous les usages d'IA pour vérifier leur conformité avec l'AI Act européen.

Les principes directeurs de la gouvernance sont clairs : respect des réglementations existantes et futures, usage éthique de l'IA, et utilisation comme appui et assistance aux collaborateurs — jamais comme substitut à l'expertise humaine. Aucune validation automatique n'est permise : un emailing ne partira jamais sans vérification par un collaborateur, et le conseiller peut toujours modifier les comptes-rendus générés par l'IA.

# **9\. Le partenariat technologique avec S3NS**

Le choix d'AG2R LA MONDIALE de s'appuyer sur S3NS est un élément différenciant majeur de la stratégie Almia. S3NS est une coentreprise de droit français créée en 2022, détenue majoritairement par Thales et bénéficiant de la technologie Google Cloud.

L'offre S3NS combine les services performants d'un hyperscaler avec une infrastructure ultra-sécurisée : opération exclusivement par des équipes françaises, infrastructure physiquement isolée en France avec 3 datacenters interconnectés en Île-de-France, et immunité contre les lois extraterritoriales non-européennes. Google n'a qu'un statut d'observateur sans droit de vote ni accès aux données.

En décembre 2025, S3NS a obtenu la qualification SecNumCloud 3.2 de l'ANSSI pour sa solution PREMI3NS, couvrant simultanément les couches IaaS, CaaS et PaaS — une première sur le marché français. AG2R LA MONDIALE fait partie de la quarantaine de clients de l'offre « Contrôles locaux avec S3NS ».

# **10\. Reconnaissance et retombées**

## **10.1. Pascal Martinez élu Stratège IT 2025**

Pascal Martinez a été désigné Stratège IT 2025 par les lecteurs de CIO Online (Le Monde Informatique), devançant Audrey Brayer (Pierre & Vacances Center Parcs) et Julien Nicolas (SNCF). Le déploiement d'Almia a été explicitement cité comme un facteur clé de cette reconnaissance, aux côtés du programme de transformation SI de 629 M€ sur 6 ans.

## **10.2. Programme de transformation IT global**

Almia s'inscrit dans un investissement IT massif. Le programme de modernisation des SI représente environ 150 M€ engagés en 2024, avec une trajectoire jusqu'en 2028\. La DSI, qui comptait environ 780 collaborateurs internes, a pratiquement doublé ses effectifs (principalement via des prestataires) pour mener cette transformation. L'objectif inclut le décommissionnement du mainframe et la migration vers le SaaS.

# **11\. Couverture médiatique et interventions publiques**

## **11.1. Articles de presse spécialisée**

* **Communiqué officiel (nov. 2024\) :** Newsroom AG2R LA MONDIALE — Annonce de lancement d'Almia

* **Alliancy (nov. 2024\) :** « AG2R La Mondiale lance sa propre IA pour améliorer l'expérience client »

* **L'Argus de l'Assurance (nov. 2024\) :** « AG2R La Mondiale présente sa solution d'IA générative »

* **La Revue du Digital (nov. 2024 puis avr. 2025\) :** Deux articles détaillés, dont « Usages multiples pour Almia » avec interview de Ludovic Letort

* **ActuIA (fév. 2025\) :** « GenAI et assurance : comment AG2R LA MONDIALE entend améliorer le quotidien de ses collaborateurs avec ALMIA »

* **Majorel Magazine (fév. 2025\) :** « Almia, l'IA génératrice d'efficacité des processus métiers » — Interview approfondie de Pascal Martinez

* **LeMagIT (2025) :** « Les quatre piliers de la stratégie GenAI d'AG2R La Mondiale » — Analyse détaillée de l'architecture

* **Cercle de l'Épargne (avr. 2025\) :** Interview de Pascal Martinez « L'intelligence artificielle au service de l'assurance — 3 questions »

* **IT for Business (avr. 2025\) :** « AG2R La Mondiale capitalise sur l'IA générative avec Almia »

* **Le Monde Informatique / CIO (déc. 2025\) :** « Pascal Martinez, élu Stratège IT 2025 : Nous intégrons peu à peu l'IA dans nos processus »

## **11.2. Interviews détaillées**

* **Républik IT (mai 2024\) :** Interview de Pascal Martinez sur la transformation d'AG2R, mention du lancement d'Almia et des tests avec les Champions IA

* **Républik IT (nov. 2024\) :** Interview approfondie « Nous vectorisons nos datas pour utiliser les IAG publiques » — Explication technique du fonctionnement d'Almia

* **News Assurances Pro — TEC (sept. 2024\) :** Vidéo de Pascal Martinez sur la feuille de route SI, en partenariat avec Cegedim Insurance Solutions

## **11.3. Conférences et interventions**

* **DIMS 2025 (IMA Digital Transformation) :** Session « La stratégie IA chez AG2R : ALMIA, un socle pour industrialiser l'IA » — partage autour de la stratégie d'industrialisation, des cas d'usage et de l'acculturation des collaborateurs

* **S3NS Summit (2025-2026) :** AG2R LA MONDIALE régulièrement cité comme client de référence de S3NS lors de leurs événements annuels

* **Séminaires internes AG2R :** Plénière annuelle de la DSID à Mons-en-Barœul (décembre 2025), présentation des avancées d'Almia aux équipes

* **Conférence IESAS × AG2R (déc. 2025\) :** Intervention sur la cybersécurité, en lien avec les enjeux de sécurisation de l'IA

* **Lancement plan « Esprit de conquête » :** Grande Halle de la Villette — Pascal Martinez y présente le rôle de l'IA dans la stratégie de conquête du groupe

## **11.4. Présence LinkedIn**

Les dirigeants d'AG2R LA MONDIALE sont actifs sur LinkedIn autour d'Almia :

* **Pascal Martinez :** posts réguliers sur les avancées d'Almia, son élection Stratège IT 2025, et le plan « Esprit de conquête »

* **Stéphane Lapierre :** posts sur les avancées de la solution Almia et les journées d'échanges IA avec Google

* **Ludovic Letort :** Directeur Data & IA Factory, profil Centralien, interventions sur la stratégie data et IA

* **Mickael Mikowsky :** Chef de projet IA en charge de la communauté Almia, posts sur l'IA comme sujet RH et le management dans l'ère de l'IA

## **11.5. Couverture internationale**

* **Qorus Global (nov. 2024\) :** « AG2R LA MONDIALE introduces Almia, its Gen AI platform to enhance customer and employee satisfaction » — Article en anglais pour l'industrie internationale de l'assurance

# **12\. Positionnement dans le paysage concurrentiel**

AG2R LA MONDIALE n'est pas le seul assureur français à avoir développé sa propre plateforme d'IA générative. AXA a lancé Secure GPT dans une démarche similaire. Cependant, Almia se distingue par plusieurs caractéristiques :

* Une approche multi-LLM et agnostique vis-à-vis des fournisseurs de modèles

* Un écosystème complet (Bot \+ Apps \+ Dev \+ Agents) plutôt qu'un simple chatbot

* Une stratégie de diffusion et de transformation notamment en s’appuyant sur un réseau dédié de pairs via les Champions IA

* L'adossement à S3NS / SecNumCloud pour la souveraineté des données

* Une marketplace interne d'assistants et d’agents pour et créés par les collaborateurs

* Une gouvernance IA formalisée et pilotée au plus haut niveau

Pascal Martinez lui-même reconnaît que les concurrents ne sont pas en reste dans cette course à l'IA, mais estime qu'Almia représente un atout compétitif significatif pour le groupe dans l’adoption de la technologie et son déploiement rapide à l’échelle de l’entreprise.

# **13\. Perspectives et feuille de route**

Plusieurs axes d'évolution se dessinent pour Almia :

* **Extension du périmètre utilisateurs :** poursuite du déploiement vers l'ensemble collaborateurs externes au groupe, au-delà des 7 000 utilisateurs actuels

* **Agents IA :** développement d'agents IA intégrés à la chaîne de valeur de l’entreprise

* **Produits IA :** la mise en oeuvre de nouvelle capacité Almia Apps pour répondre aux nouveaux besoins métiers en terme d’IA

* **Vertex AI sur S3NS :** au second semestre 2026, Vertex AI (plateforme IA de Google Cloud) rejoindra l'offre PREMI3NS de S3NS, ouvrant la voie à une IA de confiance souveraine

* **Intégration dans le programme de transformation :** les dernières années du programme SI (jusqu'en 2028\) se concentreront sur les migrations de données et décommissionnements, avec l'IA comme accélérateur

* **Conformité AI Act :** poursuite de la cartographie et de la mise en conformité de tous les usages IA avec la réglementation européenne

# **14\. Sources documentaires**

## **Sources principales**

1. Newsroom AG2R LA MONDIALE — Communiqué de presse officiel (novembre 2024\)

2. Alliancy — « AG2R La Mondiale lance sa propre IA pour améliorer l'expérience client » (novembre 2024\)

3. L'Argus de l'Assurance — « AG2R La Mondiale présente sa solution d'IA générative » (novembre 2024\)

4. La Revue du Digital — Deux articles (novembre 2024 et avril 2025\)

5. ActuIA — « GenAI et assurance : comment AG2R LA MONDIALE entend améliorer le quotidien de ses collaborateurs avec ALMIA » (février 2025\)

6. Majorel Magazine — Interview de Pascal Martinez (février 2025\)

7. Républik IT — Deux interviews de Pascal Martinez (mai et novembre 2024\)

8. LeMagIT — « Les quatre piliers de la stratégie GenAI d'AG2R La Mondiale » (2025)

9. Cercle de l'Épargne — Interview « L'intelligence artificielle au service de l'assurance — 3 questions » (avril 2025\)

10. Le Monde Informatique / CIO Online — « Pascal Martinez, élu Stratège IT 2025 » (décembre 2025\)

11. IT for Business — « AG2R La Mondiale capitalise sur l'IA générative avec Almia » (avril 2025\)

12. Qorus Global — Article en anglais (novembre 2024\)

13. DIMS 2025 (IMA Digital Transformation) — Session de conférence

14. News Assurances Pro — Vidéo TEC avec Pascal Martinez (septembre 2024\)

15. Profils LinkedIn : Pascal Martinez, Ludovic Letort, Stéphane Lapierre, Mickael Mikowsky

