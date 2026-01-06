# **RAPPORT D'ANALYSE STRATÉGIQUE : L'ACQUISITION DE MANUS PAR META PLATFORMS**

## **RÉSUMÉ EXÉCUTIF**

Le 29 décembre 2025, Meta Platforms a officialisé l'acquisition de la startup d'intelligence artificielle **Manus** (accessible via [**https://manus.im/**](https://manus.im/)), pour un montant estimé à plus de 2 milliards de dollars.1 Cette opération marque le passage stratégique de l'IA conversationnelle (chatbots) à l'IA agentique (agents autonomes).

Contrairement à certaines confusions initiales, cette acquisition ne concerne pas le fabricant de gants haptiques pour la VR (Manus VR), mais bien la société créatrice de l'agent généraliste capable d'opérer une machine virtuelle dans le cloud pour exécuter des tâches complexes.3

Manus, issue de l'écosystème chinois sous le nom de *Butterfly Effect* avant sa relocalisation à Singapour, a développé une architecture permettant l'exécution autonome de code et la navigation web, surpassant les standards de l'industrie (benchmarks GAIA).5 Ce rapport analyse les implications techniques de cette technologie de "machine virtuelle cloud", les enjeux géopolitiques ayant forcé la rupture avec les capitaux chinois, et la stratégie d'intégration de Meta.

## ---

**CHAPITRE 1 : ANATOMIE DE LA TRANSACTION ET IDENTITÉ DE LA CIBLE**

### **1.1. Les Dynamiques de l'Acquisition**

L'acquisition, conclue fin décembre 2025, représente la troisième plus grande opération de l'histoire de Meta, après WhatsApp et Scale AI.1 Bien que le montant exact reste confidentiel, les estimations convergent vers une fourchette de 2 à 3 milliards de dollars, incluant d'importants paquets de rétention pour les ingénieurs.8

Cette valorisation valide un modèle économique en hyper-croissance : au moment du rachat, Manus affichait un revenu récurrent annuel (ARR) d'environ 125 millions de dollars, atteint en seulement huit mois de commercialisation.10 La transaction s'est déroulée en un temps record d'une dizaine de jours, illustrant l'urgence pour Mark Zuckerberg de sécuriser une technologie "agentique" fonctionnelle face à Google et OpenAI.7

### **1.2. Profil de la Cible : De Monica à Manus.im**

Il est impératif de préciser l'identité numérique de l'entreprise acquise pour éviter toute confusion avec d'autres acteurs du secteur technologique.

* **Identité et Origine :** L'entreprise, juridiquement *Butterfly Effect Pte. Ltd.*, opère le service **Manus.im**. Elle a été fondée par Xiao Hong (surnommé "Red Xiao"), un entrepreneur de 33 ans issu de l'université de Huazhong, connu pour avoir créé des outils d'automatisation sur WeChat.12  
* **Le Pivot Produit :** Avant de lancer l'agent autonome Manus en mars 2025, l'entreprise avait rencontré un succès mondial avec **Monica.im**, une extension de navigateur agissant comme un copilote IA.12  
* **La Distinction Critique :** Meta n'a pas acquis de technologie matérielle (comme les gants de données de *Manus VR*), mais une "usine logicielle". Manus se définit non pas comme un assistant qui parle, mais comme un agent qui agit ("Fire and Forget"), capable de prendre le contrôle d'un navigateur pour accomplir des tâches réelles.2

## ---

**CHAPITRE 2 : ANALYSE TECHNIQUE — L'ARCHITECTURE DE L'AGENT AUTONOME**

L'acquisition de **Manus.im** par Meta ne vise pas à acquérir un nouveau LLM (Large Language Model), mais un **Système d'Exploitation Agentique (Agentic OS)**. Ce chapitre dissèque l'architecture logicielle qui permet à Manus de transformer des modèles de langage probabilistes en agents d'exécution déterministes.

### **2.1. Le Paradigme de la "Machine Virtuelle Cloud" (Cloud VM)**

La rupture fondamentale de Manus par rapport à ChatGPT ou Google Gemini réside dans son environnement d'exécution. Au lieu d'opérer dans une fenêtre de contexte textuelle, Manus instancie pour chaque tâche une **machine virtuelle (VM) basée sur Linux** dans le cloud.14

* **L'Approche "Computer Use" :** Xiao Hong, le fondateur, théorise que pour qu'une IA soit utile, elle doit avoir "son propre ordinateur".12 Manus déploie une sandbox sécurisée équipée d'un système de fichiers, d'un interpréteur Python, et surtout d'un navigateur complet (headless browser).  
* **La Stack Technique :** L'analyse des dépendances et des comportements de l'agent suggère l'utilisation intensive de frameworks d'automatisation comme **Playwright** ou de bibliothèques Python spécifiques comme **Browser Use**.16 Cela permet à l'agent non seulement de "lire" le web, mais d'interagir avec le DOM (Document Object Model) : cliquer sur des boutons, remplir des formulaires complexes, gérer les pop-ups et contourner les CAPTCHA basiques.  
* **Persistance et Asynchronisme :** Contrairement à un chatbot qui attend une réponse immédiate, l'architecture VM permet un fonctionnement asynchrone ("Fire and Forget"). L'utilisateur lance une requête complexe (« Trouve 50 prospects sur LinkedIn et mets-les dans un Excel »), ferme son ordinateur, et la VM de Manus continue de tourner dans le cloud pendant des heures si nécessaire, notifiant l'utilisateur une fois la tâche accomplie.1

### **2.2. Orchestration Multi-Modèles et Agnosticisme**

Manus n'est pas un modèle monolithique, mais un **orchestrateur**. Il agit comme une couche de gestion (middleware) au-dessus de plusieurs modèles de fondation tiers.

* **La Stratégie "Best-of-Breed" :** L'architecture de Manus route les tâches vers le modèle le plus approprié.  
  * **Raisonnement Complexe & Coding :** Pour la planification et l'écriture de code, Manus s'appuie fortement sur **Claude 3.5 Sonnet** (et potentiellement les versions beta de Sonnet 4/4.5) d'Anthropic, réputé pour ses capacités de codage supérieures.  
  * **Tâches Rapides & Contextes Longs :** Pour l'analyse de documents massifs ou des tâches moins critiques, il utilise des modèles comme **Qwen** (Alibaba) ou des versions distillées de Llama, optimisant ainsi le rapport performance/coût.  
* **Architecture Planificateur-Exécuteur :** Le système fonctionne sur une boucle de rétroaction stricte :  
  1. **Agent Planificateur :** Décompose l'objectif utilisateur en sous-tâches séquentielles (ex: 1\. Recherche Google, 2\. Scraping, 3\. Analyse Python, 4\. Génération PDF).  
  2. **Agent Exécuteur :** Prend le contrôle de la VM pour réaliser l'action.  
  3. **Agent Vérificateur (Critic) :** Analyse le résultat (ex: lit le message d'erreur d'exécution Python) et décide s'il faut réessayer ou passer à l'étape suivante. C'est cette boucle d'auto-correction qui permet à Manus d'écrire et de déployer des applications web fonctionnelles sans aide humaine.19

### **2.3. Performance Quantifiée : Analyse des Benchmarks GAIA**

La supériorité de Manus est objectivement mesurable via le benchmark **GAIA** (*General AI Assistant Benchmark*), conçu par Meta, Hugging Face et AutoGPT pour évaluer les capacités d'agents réels.16

| Niveau de Difficulté | Tâches Types | Score Manus | Score OpenAI (Deep Research) | Analyse Technique |
| :---- | :---- | :---- | :---- | :---- |
| **Niveau 1** | Recherche simple, extraction d'info unique. | **86,5 %** | 74,3 % | La navigation native via Playwright/Browser-Use offre une fiabilité supérieure au simple parsing HTML des LLM classiques.5 |
| **Niveau 2** | Raisonnement multi-étapes, combinaison d'outils. | **70,1 %** | 69,1 % | Égalité technique. Sur le raisonnement pur, les modèles d'OpenAI (o1/o3) restent très compétitifs face à l'assemblage de Manus.21 |
| **Niveau 3** | Tâches à long horizon (plusieurs heures), gestion d'erreurs, ambiguïté. | **57,7 %** | 47,6 % | **Le "Moat" (Avantage Compétitif).** L'écart de \+10 pts s'explique par la persistance de la VM et la gestion de l'état (state management). Là où un LLM "oublie" ou hallucine après 20 tours, la VM de Manus conserve les fichiers et l'historique d'exécution intacts. |

### **2.4. Le Goulot d'Étranglement Économique : La Crise du "Credit Burn"**

L'architecture de Manus présente un défaut majeur : son coût opérationnel exorbitant, qui a mené à une crise utilisateur majeure juste avant l'acquisition.

* **L'Intensité Computationnelle :** Une tâche "simple" pour un agent (ex: comparer 10 assurances) peut générer des centaines d'appels API (navigation, lecture, clic, retour arrière) et consommer des milliers de tokens d'entrée/sortie.  
* **La Controverse du "Credit Burn" :** En décembre 2025, les utilisateurs ont rapporté une consommation de crédits insoutenable (jusqu'à 1 000 crédits/jour) et une dégradation de la qualité. Pour préserver ses marges, Manus aurait supprimé le "High Effort Mode" (qui utilisait probablement les modèles de raisonnement les plus chers comme o1 ou Sonnet 3.5 Opus) au profit de modèles "Turbo" moins performants, entraînant des hallucinations et des boucles infinies.  
* **La Synergie Infrastructurelle :** C'est ici que l'acquisition prend tout son sens technique. Meta possède l'infrastructure (600 000+ GPU H100) pour absorber cette charge de calcul. En remplaçant les appels API coûteux vers Anthropic/OpenAI par des modèles internes **Llama 4** (ou versions futures) hébergés sur ses propres serveurs, Meta peut réduire le coût marginal de l'agent proche de zéro, rendant le modèle économique viable à l'échelle de WhatsApp.

## ---

**CHAPITRE 3 : GÉOPOLITIQUE ET "SINGAPORE-WASHING"**

Cette acquisition est un cas d'école des tensions technologiques sino-américaines et des stratégies de contournement mises en œuvre par les startups chinoises.

### **3.1. La Stratégie de Relocalisation**

Pour devenir "acquirable" par un géant américain, Manus a dû effacer ses origines chinoises. Fondée initialement à Pékin/Wuhan, la société a transféré son siège et sa propriété intellectuelle à Singapour en 2025.13  
Ce phénomène, qualifié de "Singapore-washing", permet aux entreprises technologiques de bénéficier des capitaux occidentaux (comme l'investissement de Benchmark Capital) tout en conservant une ingénierie d'origine chinoise.23

### **3.2. La Réponse Politique Américaine : Le Cas John Cornyn**

L'investissement initial de Benchmark Capital dans Manus a provoqué l'ire du sénateur républicain John Cornyn. Ce dernier a publiquement critiqué le financement américain d'une technologie pouvant renforcer un rival géopolitique.23  
Cette pression s'inscrit dans le cadre législatif du FIGHT China Act et du GUARD Act, visant à interdire les investissements US dans l'IA chinoise et à renforcer la recherche militaire américaine.26

### **3.3. La Muraille de Meta**

Pour valider l'accord, Meta a imposé une coupure nette :

* **Sortie des capitaux chinois :** Les investisseurs historiques comme Tencent et ZhenFund ont été totalement sortis du capital.27  
* **Fermeture en Chine :** Manus.im cessera toute opération en Chine continentale. Les données et les serveurs seront intégralement gérés hors de la juridiction chinoise.14

## ---

**CHAPITRE 4 : INTÉGRATION STRATÉGIQUE — WHATSAPP ET ORION**

L'acquisition vise à transformer les produits de Meta en plateformes de services transactionnels.

### **4.1. WhatsApp 2026 : Le Monopole de l'Agent**

Meta prépare une mise à jour majeure de ses conditions d'utilisation pour janvier 2026, interdisant les chatbots IA généralistes tiers sur WhatsApp Business.28

* **L'Objectif :** Éliminer la concurrence (ChatGPT, Copilot) sur sa propre plateforme.  
* **Le Rôle de Manus :** Manus deviendra le moteur exclusif de l'automatisation sur WhatsApp. Il permettra aux entreprises de gérer des flux complexes (réservations, devis, SAV) de manière totalement autonome, transformant l'application de messagerie en une "Super App" transactionnelle.28

### **4.2. Projet Orion : Le Cerveau des Lunettes AR**

Pour ses futures lunettes de réalité augmentée (Projet Orion, prévu vers 2027), Meta a besoin d'une IA capable d'agir sur le monde réel sans interface tactile.31

* **L'Intégration :** La capacité de Manus à naviguer sur le web et à interagir avec des API tierces permettra aux lunettes Orion d'exécuter des commandes vocales complexes (ex: "Achète ces chaussures en taille 42") en pilotant les processus d'achat en arrière-plan, concrétisant la vision d'un assistant "mains libres" véritablement utile.33

## ---

**CONCLUSION**

L'acquisition de **Manus (manus.im)** par Meta pour plus de 2 milliards de dollars est bien plus qu'une transaction financière. Elle entérine la supériorité de l'approche "machine virtuelle" pour les agents IA et marque une victoire du pragmatisme technologique sur les frontières géopolitiques, au prix d'une rupture totale avec les origines chinoises de la startup. Pour Meta, c'est la brique manquante pour transformer WhatsApp et ses futures lunettes AR en outils de productivité économique incontournables.

#### **Works cited**

1. Meta acquires AI startup Manus in milestone deal worth over $2 ..., accessed January 6, 2026, [https://www.businesstoday.in/technology/news/story/meta-acquires-ai-startup-manus-in-milestone-deal-worth-over-2-billion-508760-2025-12-31](https://www.businesstoday.in/technology/news/story/meta-acquires-ai-startup-manus-in-milestone-deal-worth-over-2-billion-508760-2025-12-31)  
2. Rachat de Manus par Meta : 2 milliards de dollars, accessed January 6, 2026, [https://equinoxal.fr/technologie/intelligence-artificielle/rachat-manus-ia-meta/](https://equinoxal.fr/technologie/intelligence-artificielle/rachat-manus-ia-meta/)  
3. Manus (AI agent) \- Wikipedia, accessed January 6, 2026, [https://en.wikipedia.org/wiki/Manus\_(AI\_agent)](https://en.wikipedia.org/wiki/Manus_\(AI_agent\))  
4. Manus se junta à Meta para a próxima era de inovação, accessed January 6, 2026, [https://manus.im/pt-br/blog/manus-joins-meta-for-next-era-of-innovation](https://manus.im/pt-br/blog/manus-joins-meta-for-next-era-of-innovation)  
5. Manus AI: Capabilities, GAIA Benchmark, Use Cases & More \- GoCodeo, accessed January 6, 2026, [https://www.gocodeo.com/post/manus-ai-capabilities](https://www.gocodeo.com/post/manus-ai-capabilities)  
6. Manus AI Statistics and Facts (2025) \- SEO.ai, accessed January 6, 2026, [https://seo.ai/blog/manus-ai-statistics-and-facts](https://seo.ai/blog/manus-ai-statistics-and-facts)  
7. Manus被Meta数十亿美元收购背后：创始人肖弘复盘至暗时刻, accessed January 6, 2026, [https://wallstreetcn.com/articles/3762295](https://wallstreetcn.com/articles/3762295)  
8. Meta pays $3 billion for Manus AI after startup cut all Chinese ties to clear regulatory hurdles, accessed January 6, 2026, [https://the-decoder.com/meta-pays-3-billion-for-manus-ai-after-startup-cut-all-chinese-ties-to-clear-regulatory-hurdles/](https://the-decoder.com/meta-pays-3-billion-for-manus-ai-after-startup-cut-all-chinese-ties-to-clear-regulatory-hurdles/)  
9. Meta kauft KI-Startup Manus AI für 2 Milliarden Dollar \- Notebookcheck.com News, accessed January 6, 2026, [https://www.notebookcheck.com/Meta-kauft-KI-Startup-Manus-AI-fuer-2-Milliarden-Dollar.1194070.0.html](https://www.notebookcheck.com/Meta-kauft-KI-Startup-Manus-AI-fuer-2-Milliarden-Dollar.1194070.0.html)  
10. Meta compra Manus AI: o movimento que muda a corrida dos Agentes de IA em 2026 | Blog, accessed January 6, 2026, [https://www.aleguimas.com.br/blog/meta-compra-manus-ai-o-movimento-que-muda-a-corrida-dos-agentes-de-ia-em-2026/](https://www.aleguimas.com.br/blog/meta-compra-manus-ai-o-movimento-que-muda-a-corrida-dos-agentes-de-ia-em-2026/)  
11. Meta buys startup Manus in latest move to advance its artificial intelligence efforts \- Delta Optimist, accessed January 6, 2026, [https://www.delta-optimist.com/the-mix/meta-buys-startup-manus-in-latest-move-to-advance-its-artificial-intelligence-efforts-11680488](https://www.delta-optimist.com/the-mix/meta-buys-startup-manus-in-latest-move-to-advance-its-artificial-intelligence-efforts-11680488)  
12. Meet Xiao Hong: CEO of Manus, Chinese AI firm acquired by Mark Zuckerberg’s Meta for $2 billion, accessed January 6, 2026, [https://www.financialexpress.com/life/technology-meet-xiao-hong-ceo-of-manus-chinese-ai-firm-bought-by-mark-zuckerbergs-meta-for-2-billion-4092361/](https://www.financialexpress.com/life/technology-meet-xiao-hong-ceo-of-manus-chinese-ai-firm-bought-by-mark-zuckerbergs-meta-for-2-billion-4092361/)  
13. Meta buys startup Manus in latest move to advance its artificial intelligence efforts | KSL.com, accessed January 6, 2026, [https://www.ksl.com/article/51424941/meta-buys-startup-manus-in-latest-move-to-advance-its-artificial-intelligence-efforts](https://www.ksl.com/article/51424941/meta-buys-startup-manus-in-latest-move-to-advance-its-artificial-intelligence-efforts)  
14. Meta buys AI startup Manus, makes clarification on its 'Chinese connection'; says: There will be no, accessed January 6, 2026, [https://timesofindia.indiatimes.com/technology/tech-news/meta-buys-ai-startup-manus-makes-clarification-on-its-chinese-connection-says-there-will-be-no-/articleshow/126283628.cms](https://timesofindia.indiatimes.com/technology/tech-news/meta-buys-ai-startup-manus-makes-clarification-on-its-chinese-connection-says-there-will-be-no-/articleshow/126283628.cms)  
15. Meta acquires Chinese-founded AI startup Manus for over $3 billion, accessed January 6, 2026, [https://gigazine.net/gsc\_news/en/20260105-meta-buys-ai-startup-manus/](https://gigazine.net/gsc_news/en/20260105-meta-buys-ai-startup-manus/)  
16. What is Manus AI? Benchmarks & How it Compares to Operator and Computer Use, accessed January 6, 2026, [https://www.helicone.ai/blog/manus-benchmark-operator-comparison](https://www.helicone.ai/blog/manus-benchmark-operator-comparison)  
17. ‘No continuing China-link’: Facebook-parent Meta clarifies after $2 billion Manus AI deal, accessed January 6, 2026, [https://timesofindia.indiatimes.com/technology/tech-news/no-continuing-china-link-facebook-parent-meta-clarifies-after-2-billion-manus-ai-deal/articleshow/126273605.cms](https://timesofindia.indiatimes.com/technology/tech-news/no-continuing-china-link-facebook-parent-meta-clarifies-after-2-billion-manus-ai-deal/articleshow/126273605.cms)  
18. The Meta-Manus Deal: How Flow Data Caught Institutions Selling the News 10 Days Early, accessed January 6, 2026, [https://www.exponential-tech.ai/post/meta-equity-flow-data](https://www.exponential-tech.ai/post/meta-equity-flow-data)  
19. Manus AI Statistics By Usage, Revenue and Facts (2025) \- ElectroIQ, accessed January 6, 2026, [https://electroiq.com/stats/manus-ai-statistics/](https://electroiq.com/stats/manus-ai-statistics/)  
20. Cornyn, Cruz Introduce Bill to Advance Defense Innovation & Artificial Intelligence, accessed January 6, 2026, [https://www.cornyn.senate.gov/news/cornyn-introduces-bill-to-advance-defense-innovation-artificial-intelligence/](https://www.cornyn.senate.gov/news/cornyn-introduces-bill-to-advance-defense-innovation-artificial-intelligence/)  
21. Meta acquires intelligent agent firm Manus, capping year of aggressive AI moves, accessed January 6, 2026, [https://www.hackdiversity.com/meta-acquires-intelligent-agent-firm-manus/](https://www.hackdiversity.com/meta-acquires-intelligent-agent-firm-manus/)  
22. Meta sube la apuesta en la IA y compra la ‘start-up’ china Manus por más de 2.000 millones de dólares, accessed January 6, 2026, [https://elpais.com/economia/2025-12-30/meta-sube-la-apuesta-en-la-ia-y-compra-la-start-up-china-manus-por-mas-de-2000-millones-de-dolares.html](https://elpais.com/economia/2025-12-30/meta-sube-la-apuesta-en-la-ia-y-compra-la-start-up-china-manus-por-mas-de-2000-millones-de-dolares.html)  
23. Meta just acquired a Chinese-founded AI startup for $2B. Here's why that matters, accessed January 6, 2026, [https://ca.news.yahoo.com/meta-just-acquired-chinese-founded-203638056.html](https://ca.news.yahoo.com/meta-just-acquired-chinese-founded-203638056.html)  
24. \#91: We are failing in AI literacy \- Hugging Face, accessed January 6, 2026, [https://huggingface.co/blog/Kseniase/fod91](https://huggingface.co/blog/Kseniase/fod91)  
25. What Is Manus? The AI agent that made Meta make a billion-dollar move \- ET Edge Insights, accessed January 6, 2026, [https://etedge-insights.com/technology/artificial-intelligence/what-is-manus-the-ai-agent-that-made-meta-make-a-billion-dollar-move/](https://etedge-insights.com/technology/artificial-intelligence/what-is-manus-the-ai-agent-that-made-meta-make-a-billion-dollar-move/)  
26. Cornyn, Cortez Masto, Colleagues Introduce Outbound Investment Legislation to Counter China, accessed January 6, 2026, [https://www.cornyn.senate.gov/news/cornyn-cortez-masto-colleagues-introduce-outbound-investment-legislation-to-counter-china/](https://www.cornyn.senate.gov/news/cornyn-cortez-masto-colleagues-introduce-outbound-investment-legislation-to-counter-china/)  
27. 20亿美金落袋？这位90后华人把公司卖给Meta，成了汪滔的同事 \- 智源社区, accessed January 6, 2026, [https://hub.baai.ac.cn/view/51561](https://hub.baai.ac.cn/view/51561)  
28. Meta Bans General-Purpose AI Chatbots on WhatsApp \- Azguards Technolabs, accessed January 6, 2026, [https://azguards.com/artificial-intelligence/what-metas-2026-whatsapp-chatbot-ban-means-for-businesses-explained/](https://azguards.com/artificial-intelligence/what-metas-2026-whatsapp-chatbot-ban-means-for-businesses-explained/)  
29. Meta is Removing Microsoft Copilot and ChatGPT From WhatsApp: Key Takeaways For IT Leaders \- UC Today, accessed January 6, 2026, [https://www.uctoday.com/unified-communications/meta-whatsapp-chatgpt-copilot-enterprise-impact/](https://www.uctoday.com/unified-communications/meta-whatsapp-chatgpt-copilot-enterprise-impact/)  
30. WhatsApp's 2026 AI Policy Explained \- Turn.io Learn, accessed January 6, 2026, [https://learn.turn.io/l/en/article/khmn56xu3a-whats-app-s-2026-ai-policy-explained](https://learn.turn.io/l/en/article/khmn56xu3a-whats-app-s-2026-ai-policy-explained)  
31. Meta plans Oakley-branded glasses, explores watches and earbuds \- The Business Times, accessed January 6, 2026, [https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/meta-plans-oakley-branded-glasses-explores-watches-and-earbuds](https://www.businesstimes.com.sg/companies-markets/telcos-media-tech/meta-plans-oakley-branded-glasses-explores-watches-and-earbuds)  
32. These Are the Biggest Rumors for the Next Generation of Meta Smart Glasses | Lifehacker, accessed January 6, 2026, [https://lifehacker.com/tech/biggest-rumors-for-next-generation-of-meta-smart-glasses](https://lifehacker.com/tech/biggest-rumors-for-next-generation-of-meta-smart-glasses)  
33. La paradoja de que Meta compre Manus: su mayor ventaja es no tener modelo propio, accessed January 6, 2026, [https://www.xataka.com/robotica-e-ia/paradoja-que-meta-compre-manus-su-mayor-ventaja-no-tener-modelo-propio](https://www.xataka.com/robotica-e-ia/paradoja-que-meta-compre-manus-su-mayor-ventaja-no-tener-modelo-propio)  
34. Meta Shares Insights Into Its Coming AR Glasses | Social Media Today, accessed January 6, 2026, [https://www.socialmediatoday.com/news/meta-previews-orion-ar-glasses/744422/](https://www.socialmediatoday.com/news/meta-previews-orion-ar-glasses/744422/)