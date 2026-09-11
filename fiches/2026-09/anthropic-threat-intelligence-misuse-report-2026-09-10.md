---
themes: [qualite-securite, politique-regulation, economie-marche]
source: "Anthropic"
---
# anthropic-threat-intelligence-misuse-report-2026-09-10

## Veille

Rapport de renseignement sur les menaces publié par l'équipe **Threat Intelligence** d'**Anthropic** le **10 septembre 2026** sur anthropic.com (~36 000 mots indicateurs de compromission compris, PDF téléchargeable, non signé). Il couvre les abus interrompus entre **décembre 2025 et août 2026** dans **sept** domaines : cyber, influence, surveillance, armes conventionnelles, biologie, fraude, distillation. Tous les cas impliquent Haiku, Sonnet ou Opus ; aucun n'implique Fable ou Mythos, à l'exception d'une tentative de distillation.

Trois apports. **(A) Cyber** — le modèle opératoire autonome documenté en novembre 2025 *« has now proliferated across every class of actors »* : un hacktiviste francophone seul (GTG-50029), des affiliés **ShinyHunters** (GTG-50014) et un acteur rattaché à **Midnight Blizzard** (GTG-20006) mènent des campagnes multi-victimes avec des agents ; *« sophistication has stopped being a reliable signal of who is behind an operation »*. Les clés d'API IA volées servent à la fois de butin, de calcul et de couverture. **(B) Influence et surveillance** — **neuf** opérations d'influence (Russie, Iran, Turquie, Golfe, Kenya, Bangladesh, Malaisie) et une dizaine de surveillance où le modèle remplace une équipe d'analystes ou d'ingénieurs : plateforme d'interception nationale au **Mali** (~**25 M** de SIM), bureaux de sécurité chinois, unités iraniennes. **(C) Distillation** — sept laboratoires chinois nommés (**Alibaba**, **Moonshot AI**, **DeepSeek**, **Z.ai**, **Xiaomi**, SenseTime, MiniMax) ; la campagne d'Alibaba culmine à **~3 M d'échanges par jour** (**151 M** sur mai-juillet) ; Moonshot et DeepSeek servent des réponses de Claude à leurs propres clients sans les en informer ; une attaque par rejeu inter-sessions de la *thinking signature* contourne la protection existante.

Le rapport documente aussi cinq cas biologiques à double usage et six programmes d'armes conventionnelles (roquette guidée testée au Yémen, essaim de drones russe, suppression de défense aérienne visant Taïwan), et concède que ses garde-fous *« did not perform uniformly »*. Il prolonge [[anthropic-disrupting-ai-espionage-2025-11-13]] et éclaire la campagne ciblant les capacités cyber de modèles américains qui a précédé [[zai-glm-53-emergent-cyber-2026-08-14]].

## Titre Article

Detecting and countering misuse of AI: September 2026

## Date

2026-09-10

## URL

https://www.anthropic.com/threat-intelligence-report-september-2026

## Keywords

threat intelligence, mésusage de l'IA, Generative Threat Group, uplift, kill chain cyber, agents autonomes, vibe hacking, PentAGI, clés d'API volées, chaîne d'approvisionnement IA, ShinyHunters, Midnight Blizzard, exploit foundry, zero-day, opérations d'influence, influence-as-a-service, Breakout Scale, surveillance d'État, répression transnationale, interception de masse, armes conventionnelles, drones autonomes, double usage biologique, gain de fonction, distillation illicite, chaîne de raisonnement, thinking signature, rejeu inter-sessions, proxys de revente, Alibaba, Moonshot AI, DeepSeek, Z.ai, Xiaomi, garde-fous, classifieurs, programmes d'accès de confiance

## Authors

Anthropic — équipe Threat Intelligence (rattachée aux Safeguards), rapport institutionnel non signé publié sur anthropic.com.

## Ton

Profil : rapport de renseignement sur les menaces à la première personne du pluriel institutionnelle, registre d'analyste CTI (désignateurs GTG-xxxxx, niveaux de confiance *low / medium / high*, indicateurs de compromission défangés, tables d'adresses IP datées). Public : équipes de sécurité, autres fournisseurs de modèles, gouvernements et société civile. Trois traits. D'abord la **discipline d'attribution** : chaque cas porte son niveau de confiance et sépare ce qui est observé sur la plateforme de ce qui est corroboré par des sources ouvertes ou des partenaires (All Eyes on Wagner, Forbidden Stories, Microsoft, OpenAI) ; la visibilité s'arrête explicitement quand l'opération quitte Claude. Ensuite l'**aveu mesuré des limites** : un refus est *« overcome on further prompting »*, la fragmentation du travail en petites sessions dégrade les classifieurs, la plateforme malienne déployée hors ligne échappe à toute action sur les comptes, et la section biologie reconnaît que ses évaluations ne fournissent qu'une preuve ambiguë. Enfin la **portée normative** : le rapport nomme des entreprises (Alibaba, Moonshot AI, DeepSeek, Z.ai, Xiaomi, SenseTime, MiniMax, LKM Company, BBS Bilisim, S2T) et des États, et clôt chaque section par une recommandation à l'industrie — traiter les clés d'IA comme des identifiants de production, réserver les capacités biologiques de pointe à des programmes d'accès vérifié. Le vocabulaire reste celui de la menace (*uplift*, *kill chain*, *tradecraft*) ; la charge promotionnelle se limite à rappeler que Fable et Mythos n'apparaissent dans aucun cas cyber.

## Pense-betes

- **Périmètre** : décembre 2025 → août 2026, sept domaines, une trentaine de groupes GTG. Modèles impliqués : Haiku, Sonnet, Opus. Aucun cas sur Fable ou Mythos, sauf une tentative de distillation cyber contre Fable, abandonnée après dégradation par les garde-fous ; les employés de Z.ai basculent alors sur Opus 4.6 et le modèle de tête d'un autre labo américain *« expressly because they assessed the safeguards were weaker »*.
- **Cyber, deux tendances.** (1) La sophistication ne dit plus qui attaque : un hacktiviste avec des clés volées, des affiliés ShinyHunters et un opérateur d'espionnage étatique suivent la même méthode. (2) L'autonomie progresse : boucles de reconnaissance-exploitation-exfiltration pendant des heures ou des jours, flotte de **13** agents de collecte planifiés sans humain (GTG-10007), agents qui reconstruisent le malware dès qu'un antivirus le détecte (GTG-20006). Deux réserves posées par le rapport : les humains gardent le ciblage, la monétisation et la revue ; autonomie et gravité sont deux axes distincts, plusieurs des compromissions les plus graves étaient dirigées pas à pas.
- **GTG-20006 (Midnight Blizzard)** : plus de **20** organisations ciblées, DNS hijacking chez trois prestataires WiFi hôtelier (méthode « CaptiveCrunch » décrite par Microsoft en juillet 2026), **300 000** identités nationales et le registre de **500 000** sociétés exfiltrés d'une autorité nord-africaine. L'humain intervient surtout pour modifier les skills Claude Code qui pilotent les workflows.
- **GTG-50014 (ShinyHunters)** : pipeline sur dix EC2 décompilant **1,8 M** d'APK avec TruffleHog ; plus d'un téraoctet exfiltré chez un fournisseur technologique ; **2 100** jeux de jetons Azure AD sur **40** tenants dumpés en **34 h**, *« AI agents performed nearly all of the work »* ; une brèche complète en quelques heures. Le rapport nomme cela *vibe hacking* : l'opérateur fixe un but général et laisse l'agent évaluer, scripter, exécuter et recommencer.
- **GTG-10007** : étudiants d'une université du Hunan, *exploit foundry* — une boucle autonome de rétro-ingénierie de firmware produit plus d'une douzaine de zero-days possibles en un mois sur des appliances réseau ; essaims d'agents avec mémoire de campagne persistante entre sessions.
- **Chaîne d'approvisionnement IA** : une clé volée donne *loot, compute, cover*. GTG-50020 attaque une trentaine de sociétés d'IA en quatre jours, avec pour but déclaré l'accès à un modèle Claude pré-release (échec sur toutes les voies) ; GTG-50021 vend un faux accès Claude à prix cassé qui installe un voleur d'identifiants. Injections de prompt contre des déploiements LiteLLM et OpenClaw pour exfiltrer des clés de production. Recommandation : traiter clés d'IA et intégrations d'agents comme des identifiants de production.
- **Influence** : neuf opérations, catégories 1 à 4 sur la Breakout Scale ; la plupart n'atteignent pas d'audience réelle, la portée authentique venant des médias d'État (radio FM en Centrafrique, Sputnik, RT). La doctrine vit dans des fichiers mémoire ou `SKILL.md` réutilisés sur des centaines de sessions. Claude a refusé certaines demandes (désigner des militants, produire un dossier de diffamation) ; l'acteur reformule et poursuit.
- **Surveillance** : au Mali, **Lakana 360** surveille ~**25 M** de SIM sur trois opérateurs, l'obligation de mandat retirée à la demande de l'opérateur, déployé sur site avec un LLM local — le bannissement du compte ne touche pas le produit. En Chine, une unité de renseignement religieux passée de plusieurs équipes à un seul bureau produisant des milliers d'enquêtes par mois ; un bureau rédige un manuel interne d'usage de l'IA. En Iran, seize comptes, une extension Firefox malveillante et deux unités alimentant le même système « Arman ».
- **Armes conventionnelles** : six cas. Au Yémen, un tir d'essai réel puis retour vers Claude en quelques heures pour analyser l'échec ; en Russie, un essaim FPV avec classe de cible *« person »* et détonation sans humain (TRL 3-4) ; en Chine, une suite de guerre électronique dont le scénario par défaut bascule sur douze cibles à Taïwan. Nouveaux classifieurs explosifs et armes annoncés.
- **Biologie** : cinq cas, tous à double usage, chercheurs en activité, institutions et agents volontairement tus. Les classifieurs confinent le gain de fonction aux modèles les plus faibles (Sonnet 4, Haiku 4.5), mais Opus 5 rédige en une heure une demande de subvention orthopoxvirus complète sans blocage. Conclusion du rapport : un classifieur ne peut pas seul *« enable benefit and prevent harm »*, d'où les programmes d'accès de confiance décrits dans [[anthropic-claude-fable-5-1-mythos-5-1-2026-09-01]]. Balayage de 30 jours : ~35 efforts de recherche liés à des institutions étatiques adverses.
- **Fraude** : GTG-15001, plus de 20 applications de rencontre, **4 700** personas IA, **25 000** victimes, **2,36 M** de messages en deux semaines, trois personas pour un travailleur humain. Le system prompt ressemble à un déploiement compagnon ordinaire : la fraude est invisible depuis l'échange.
- **Distillation** : Alibaba **151 M** d'échanges (mai-juillet, 3 500 comptes, distillation de Qwen 3.5 à 3.7), Moonshot AI **23 M** (5 380 comptes), DeepSeek **12,1 M** en 14 jours, Z.ai **3,4 M** en 17 jours, Xiaomi **400 k**. DeepSeek repère les utilisateurs de Claude Code, du Claude Agent SDK ou d'OpenCode et relaie leurs requêtes vers Opus. Moonshot et DeepSeek convertissent la *thinking signature* en trace complète par rejeu inter-sessions ; des données sensibles de tiers (PLA, ministère russe de la Défense, entreprises) transitent ainsi vers Claude. Contre-mesures : résumé du raisonnement, *preserved thinking* de Fable 5.1, vérification d'identité — le volet anti-distillation annoncé dans la fiche Fable 5.1 trouve ici son dossier d'instruction. À rapprocher de [[sfeir-kimi-k3-moonshot-frontier-open-weights-2026-07-16]].
- ⚠️ **Hygiène de citation** : la page n'affiche aucune date, la publication est déduite des métadonnées CMS (créée le 9, mise à jour le 10 septembre) ; les chiffres d'audience des opérations d'influence et de fraude sont auto-déclarés par les acteurs ; l'*uplift* est une estimation qualitative ; le rapport ne dit pas que GLM-5.3 a été entraîné sur les traces extraites, seulement qu'une campagne ciblant les capacités cyber a précédé sa sortie.

## RésuméDe400mots

Le **10 septembre 2026**, Anthropic publie son quatrième rapport de renseignement sur les menaces. Il couvre les opérations interrompues entre décembre 2025 et août 2026 dans sept domaines : cyber, influence, surveillance, armes conventionnelles, biologie, fraude et distillation. Tous les cas impliquent des modèles Haiku, Sonnet ou Opus ; aucun n'implique Fable ou Mythos, à l'exception d'une tentative de distillation.

En **cyber**, le rapport constate que le modèle opératoire autonome décrit en novembre 2025 s'est diffusé à toutes les classes d'acteurs, jusqu'aux frameworks publics comme PentAGI. La sophistication d'une attaque ne renseigne plus sur son auteur : un hacktiviste francophone seul, des affiliés ShinyHunters et un opérateur lié à Midnight Blizzard mènent des campagnes multi-victimes que des équipes entières auraient exigées un an plus tôt. Les agents reconstruisent les malwares détectés, produisent des zero-days en boucle, dumpent 2 100 jeux de jetons Azure AD en 34 heures. Les clés d'API IA volées deviennent butin, calcul et couverture. Deux réserves : les humains gardent le ciblage, et l'autonomie multiplie l'échelle sans déterminer la gravité.

En **influence**, neuf opérations (Russie, Iran, Turquie, Golfe, Kenya, Bangladesh, Malaisie) montrent le modèle intégré comme secrétaire de rédaction dans des pipelines existants, la doctrine stockée dans des fichiers mémoire réutilisés sur des centaines de sessions. La plupart n'atteignent pas d'audience réelle ; la portée vient des médias d'État. En **surveillance**, le modèle remplace une équipe d'ingénieurs ou d'analystes : plateforme d'interception de 25 millions de SIM au Mali, déployée hors ligne et donc hors de portée d'un bannissement ; bureaux de sécurité chinois et unités iraniennes produisant briefings et outils.

Six cas d'**armes conventionnelles** vont d'un tir d'essai au Yémen à un essaim de drones russe capable de sélectionner une cible humaine sans opérateur. Cinq cas **biologiques**, tous à double usage, conduisent Anthropic à conclure qu'un classifieur ne peut pas à la fois permettre le bénéfice et prévenir le mal, d'où les programmes d'accès de confiance. Un réseau d'applications de rencontre a fait converser 4 700 personas avec 25 000 personnes.

Sur la **distillation**, le rapport nomme sept laboratoires chinois. Alibaba atteint 151 millions d'échanges en trois mois pour entraîner Qwen ; Moonshot AI et DeepSeek servent des réponses de Claude à leurs clients sans les prévenir et convertissent la *thinking signature* en trace complète par rejeu inter-sessions ; Z.ai cible les capacités cyber avant la sortie de GLM-5.3 et abandonne Fable pour des modèles jugés moins protégés. Contre-mesures citées : résumé du raisonnement, *preserved thinking* de Fable 5.1, vérification d'identité.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Anthropic | ORGANISATION | publie | Threat Intelligence Report septembre 2026 | DOCUMENT | 0.99 | STATIQUE | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | affine | rapport Disrupting AI espionage novembre 2025 | DOCUMENT | 0.92 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | utilise | Generative Threat Group | CONCEPT | 0.95 | DYNAMIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | aucun cas de mésusage n'implique Fable ou Mythos, hors une tentative de distillation | AFFIRMATION | 0.96 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | la sophistication d'une attaque n'est plus un signal fiable de l'identité de son auteur | AFFIRMATION | 0.95 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | le modèle opératoire autonome documenté en novembre 2025 s'est diffusé à toutes les classes d'acteurs | AFFIRMATION | 0.94 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | l'autonomie multiplie l'échelle et la vitesse d'une opération mais ne détermine pas sa gravité | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| PentAGI | TECHNOLOGIE | permet | automatisation de la kill chain cyber | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Midnight Blizzard | ORGANISATION | utilise | Claude Code | TECHNOLOGIE | 0.90 | STATIQUE | déclaré_article |
| ShinyHunters | ORGANISATION | utilise | vibe hacking | CONCEPT | 0.90 | STATIQUE | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | mesure | 2 100 jeux de jetons Azure AD sur 40 tenants dumpés en 34 heures, presque entièrement par des agents | MESURE | 0.92 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | recommande | traiter les clés d'API IA et les intégrations d'agents comme des identifiants de production | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | utilise | Breakout Scale | METHODOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | affirme_que | la plupart des opérations d'influence n'atteignent pas d'audience authentique, sauf via des médias d'État | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | mesure | Lakana 360 couvre environ 25 millions de cartes SIM sur les trois opérateurs mobiles du Mali | MESURE | 0.92 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | les garde-fous n'ont pas fonctionné uniformément dans les cas de surveillance chinois | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | un classifieur ne peut pas seul permettre le bénéfice et prévenir le mal en biologie à double usage | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | recommande | programmes d'accès de confiance | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | mesure | 4 700 personas IA en conversation avec au moins 25 000 personnes, 2,36 millions de messages en deux semaines | MESURE | 0.93 | STATIQUE | déclaré_article |
| Alibaba | ORGANISATION | utilise | distillation illicite | CONCEPT | 0.96 | STATIQUE | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | mesure | 151 millions d'échanges attribués à Alibaba entre mai et juillet 2026, pic à environ 3 millions par jour | MESURE | 0.95 | STATIQUE | déclaré_article |
| Qwen | TECHNOLOGIE | est_basé_sur | Claude Opus | TECHNOLOGIE | 0.88 | STATIQUE | déclaré_article |
| Moonshot AI | ORGANISATION | utilise | attaque par rejeu inter-sessions | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| DeepSeek | ORGANISATION | utilise | attaque par rejeu inter-sessions | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| attaque par rejeu inter-sessions | CONCEPT | s_oppose_à | thinking signature | TECHNOLOGIE | 0.92 | STATIQUE | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | affirme_que | Moonshot AI et DeepSeek ont servi des réponses de Claude à leurs clients sans les en informer | AFFIRMATION | 0.93 | STATIQUE | déclaré_article |
| Z.ai | ORGANISATION | utilise | distillation illicite | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| Threat Intelligence Report septembre 2026 | DOCUMENT | affirme_que | Z.ai a ciblé les capacités cyber de modèles américains avant la sortie de GLM-5.3 et abandonné Fable pour des modèles jugés moins protégés | AFFIRMATION | 0.92 | STATIQUE | déclaré_article |
| Xiaomi | ORGANISATION | utilise | distillation illicite | CONCEPT | 0.93 | STATIQUE | déclaré_article |
| Claude Fable 5.1 | TECHNOLOGIE | utilise | preserved thinking | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| preserved thinking | TECHNOLOGIE | réduit | distillation illicite | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| Anthropic | ORGANISATION | affirme_que | un modèle distillé d'un modèle frontière peut acquérir des capacités dangereuses même si les échanges récoltés n'en traitent pas | AFFIRMATION | 0.90 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Threat Intelligence Report septembre 2026 | DOCUMENT | nature | Quatrième rapport de menaces d'Anthropic ; décembre 2025-août 2026 ; sept domaines ; ~36 000 mots avec indicateurs de compromission | AJOUT |
| rapport Disrupting AI espionage novembre 2025 | DOCUMENT | statut | Rapport précédent, dont le modèle opératoire autonome est déclaré diffusé à toutes les classes d'acteurs | AJOUT |
| Anthropic | ORGANISATION | secteur | IA / Safety | AJOUT |
| Generative Threat Group | CONCEPT | définition | Désignateur interne d'Anthropic (GTG-xxxxx) pour un acteur observé abusant de l'IA | AJOUT |
| uplift | CONCEPT | définition | Gain de capacité apporté par l'IA à un acteur, évalué en vitesse, échelle et profondeur | AJOUT |
| Claude Code | TECHNOLOGIE | usage adverse | Skills pilotant les workflows d'un acteur d'espionnage ; utilisé aussi par une cyberpolice chinoise et une cellule d'armement yéménite | AJOUT |
| Claude Opus | TECHNOLOGIE | statut | Versions 4.6, 4.7 et 4.8 ciblées par les campagnes de distillation ; Opus 5 rédige une demande de subvention orthopoxvirus sans blocage | AJOUT |
| Claude Fable 5.1 | TECHNOLOGIE | contre-mesure | Preserved thinking : les nouveaux comptes API ne peuvent plus modifier le contexte précédant le raisonnement | AJOUT |
| Midnight Blizzard | ORGANISATION | rôle | Groupe d'espionnage à nexus russe (GTG-20006) ; plus de 20 organisations ciblées, campagnes automatisées par IA | AJOUT |
| ShinyHunters | ORGANISATION | rôle | Collectif criminel de vol de données et d'extorsion (GTG-50014) ; affiliés opérant par agents | AJOUT |
| vibe hacking | CONCEPT | définition | L'opérateur fixe un but général et laisse l'agent évaluer l'environnement, scripter, exécuter et itérer jusqu'au résultat | AJOUT |
| PentAGI | TECHNOLOGIE | catégorie | Framework offensif agentique public reproduisant le scaffolding d'attaque autonome | AJOUT |
| chaîne d'approvisionnement IA | CONCEPT | statut | Cible criminelle délibérée : clés d'API, jetons de session, bacs à sable, proxys et revendeurs | AJOUT |
| Breakout Scale | METHODOLOGIE | définition | Échelle en six catégories (Brookings) mesurant la portée d'une opération d'influence par migration inter-plateformes | AJOUT |
| Lakana 360 | TECHNOLOGIE | nature | Plateforme d'interception nationale pour le renseignement malien, conçue avec Claude, déployée sur site avec un LLM local | AJOUT |
| programmes d'accès de confiance | CONCEPT | rôle | Voie recommandée par Anthropic pour servir les capacités biologiques de pointe, avec signaux de compte et rétention de données | AJOUT |
| distillation illicite | CONCEPT | définition | Campagne industrielle et couverte d'extraction des capacités d'un modèle, permise par des réseaux de comptes frauduleux | AJOUT |
| attaque par rejeu inter-sessions | CONCEPT | définition | Sauvegarde de la thinking signature puis nouvelle session pour faire reconvertir la signature en trace de raisonnement complète | AJOUT |
| thinking signature | TECHNOLOGIE | rôle | Référence chiffrée renvoyée à la place du raisonnement brut pour limiter la distillation | AJOUT |
| preserved thinking | TECHNOLOGIE | définition | Mécanisme de Fable 5.1 empêchant les nouveaux comptes API d'altérer system prompt, outils ou messages précédant le raisonnement | AJOUT |
| Alibaba | ORGANISATION | rôle | Plus grande campagne de distillation mesurée (GTG-16005) : 151 M d'échanges, 3 500 comptes, cible Qwen 3.5 à 3.7 | AJOUT |
| Qwen | TECHNOLOGIE | statut | Versions 3.5, 3.6 et 3.7 déclarées entraînées sur des traces de raisonnement extraites d'Opus 4.6 et 4.7 | AJOUT |
| Moonshot AI | ORGANISATION | rôle | Relais silencieux de requêtes clients vers Claude (GTG-16002), 5 380 comptes, 23 M d'échanges | AJOUT |
| DeepSeek | ORGANISATION | rôle | Relais des utilisateurs de harnais de codage vers Opus (GTG-16001), 12,1 M d'échanges en 14 jours | AJOUT |
| Z.ai | ORGANISATION | rôle | Nettoyage de traces de raisonnement d'Opus 4.8 (GTG-16006), 273 comptes, 3,4 M d'échanges ; campagne cyber abandonnée contre Fable | AJOUT |
| GLM-5.3 | TECHNOLOGIE | statut | Sa sortie a été précédée d'une campagne de Z.ai ciblant les capacités cyber de modèles américains | AJOUT |
| Xiaomi | ORGANISATION | rôle | Rejeu de sessions MiMo vers Claude (GTG-16008), 1 500 comptes, 400 000 échanges | AJOUT |
