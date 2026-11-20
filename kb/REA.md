# REA

> **Type** : TECHNOLOGIE | 62 relations | 29 fiches sources

## Attributs

- **capacité firmware** : Pilote Binwalk et Unblob sous Linux x64, sans émulation ni exécution
- **capacités** : Récupération de sources JS (Wakaru), lecture des fusibles Electron, pilotage de décompilateurs natifs
- **catégorie** : outil open source de rétro-ingénierie par agents (morluto/rea)
- **couverture .NET** : Métadonnées, CIL, dépendances natives, comparaison de builds ; pas de C#, pas de single-file
- **définition** : Outil de rétro-ingénierie par agents pilotant Ghidra, avec preuves et limites de chaque conclusion
- **sources officielles** : github.com/morluto/rea, rea.tools, npm rea-agents
- **sécurité** : Pas un sandbox : pont authentifié par jeton, analyse avec les droits de l'utilisateur

## Relations (comme sujet)

### affirme_que

- « This is not a sandbox and does not protect against malicious processes already running as the same operating-system user » (CITATION) — 0.95, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-sandbox-confinement-2026-10-13\|REA n'est pas un sandbox : confiner l'analyse d'un binaire inconnu]]
- « A similar repository name or copied README does not establish that a download is official » (CITATION) — 0.92, STATIQUE
  - [[fiches/2026-10/sfeir-rea-faux-depots-supply-chain-2026-10-14\|Faux dépôts REA et cheval de Troie : le risque supply chain d'un outil viral]]
- « la décompilation et l'analyse assistée par IA peuvent être incomplètes ou fausses » (AFFIRMATION) — 0.90, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-evidence-sortie-agent-2026-10-15\|Lire une sortie REA : preuves, pseudocode et hallucinations]]

### concurrence

- [[kb/GhidraMCP\|GhidraMCP]] (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-ghidramcp-ida-pro-mcp-2026-10-20\|REA, GhidraMCP ou ida-pro-mcp : quel MCP de rétro-ingénierie choisir]]
  - [[fiches/2026-10/sfeir-rea-limites-2026-10-15\|Les limites réelles de REA : taille des sorties, coût, couverture]]
- [[kb/_entites-mineures#ida-pro-mcp\|ida-pro-mcp]] (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-ghidramcp-ida-pro-mcp-2026-10-20\|REA, GhidraMCP ou ida-pro-mcp : quel MCP de rétro-ingénierie choisir]]

### est_instance_de

- serveur MCP (TECHNOLOGIE) — 0.93, STATIQUE
  - [[fiches/2026-10/sfeir-retro-ingenierie-agents-securite-2026-10-16\|Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité]]
  - [[fiches/2026-10/sfeir-retro-ingenierie-firmware-iot-2026-10-21\|Firmware et objets connectés : la rétro-ingénierie par agents]]

### mesure

- « 25 793 étoiles GitHub en une journée (76 998 au 11 octobre 2026) » (MESURE) — 0.92, STATIQUE
  - [[fiches/2026-10/sfeir-fin-avantage-code-ferme-2026-10-21\|REA, ArtCraft et la fin de l'avantage du code fermé]]
- « 369 860 étoiles GitHub au 23 octobre 2026 » (MESURE) — 0.90, STATIQUE
  - [[fiches/2026-10/sfeir-legacy-sans-code-source-2026-10-16\|Applications legacy sans code source : comprendre avant de réécrire]]
  - [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
- « 369 860 étoiles GitHub le 23 octobre 2026 » (MESURE) — 0.90, STATIQUE
  - [[fiches/2026-10/sfeir-retro-ingenierie-agents-securite-2026-10-16\|Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité]]
- « 25 793 étoiles GitHub gagnées en une journée (11 octobre 2026) » (MESURE) — 0.86, STATIQUE
  - [[fiches/2026-10/sfeir-rea-faux-depots-supply-chain-2026-10-14\|Faux dépôts REA et cheval de Troie : le risque supply chain d'un outil viral]]
- « 207 outils MCP en version 6.7.0 » (MESURE) — 0.84, STATIQUE
  - [[fiches/2026-10/sfeir-retro-ingenierie-agents-securite-2026-10-16\|Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité]]

### observé_dans

- [[kb/_entites-mineures#Slack\|Slack]] (TECHNOLOGIE) — 0.85, STATIQUE
  - [[fiches/2026-10/sfeir-rea-application-electron-2026-10-15\|Ce qu'une analyse REA révèle d'une application Electron]]
- Hyper (TECHNOLOGIE) — 0.82, STATIQUE
  - [[fiches/2026-10/sfeir-rea-application-electron-2026-10-15\|Ce qu'une analyse REA révèle d'une application Electron]]

### permet

- [[kb/rétro-ingénierie-par-agents\|rétro-ingénierie par agents]] (METHODOLOGIE) — 0.93, DYNAMIQUE
  - [[fiches/2026-10/sfeir-clean-room-vs-reverse-engineering-2026-10-11\|Clean-room ou reverse engineering : méthode et risque juridique à l'ère des agents]]
  - [[fiches/2026-10/sfeir-decompilation-interoperabilite-dsi-2026-10-12\|Décompiler pour interopérer : l'article 6 de la directive expliqué à une DSI]]
  - [[fiches/2026-10/sfeir-fin-avantage-code-ferme-2026-10-21\|REA, ArtCraft et la fin de l'avantage du code fermé]]
  - [[fiches/2026-10/sfeir-retro-ingenierie-agents-securite-2026-10-16\|Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité]]
- analyse statique des métadonnées et du CIL sans exécution (CONCEPT) — 0.90, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-dotnet-2026-10-17\|Analyser des assemblies .NET avec REA]]
- reconstruction des canaux IPC et des add-ons natifs sans exécuter l'application (CONCEPT) — 0.90, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-application-electron-2026-10-15\|Ce qu'une analyse REA révèle d'une application Electron]]
- sortie en preuves (constat, localisation, limitations, inconnues) (CONCEPT) — 0.90, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
- comparaison de builds (CONCEPT) — 0.86, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-dotnet-2026-10-17\|Analyser des assemblies .NET avec REA]]
- [[kb/rétro-documentation\|rétro-documentation]] (METHODOLOGIE) — 0.86, ATEMPOREL
  - [[fiches/2026-10/sfeir-rea-dotnet-2026-10-17\|Analyser des assemblies .NET avec REA]]

### recommande

- « un compte ou un conteneur séparé pour l'environnement de réimplémentation » (AFFIRMATION) — 0.92, DYNAMIQUE
  - [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]
- « un compte ou un conteneur séparé pour l'équipe de réécriture » (AFFIRMATION) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-clean-room-vs-reverse-engineering-2026-10-11\|Clean-room ou reverse engineering : méthode et risque juridique à l'ère des agents]]

### réduit

- coût de la première lecture d'un binaire (CONCEPT) — 0.86, DYNAMIQUE
  - [[fiches/2026-10/sfeir-legacy-sans-code-source-2026-10-16\|Applications legacy sans code source : comprendre avant de réécrire]]

### s_applique_à

- [[kb/_entites-mineures#Electron\|Electron]] (TECHNOLOGIE) — 0.94, DYNAMIQUE
  - [[fiches/2026-10/sfeir-editeurs-logiciel-lisible-agents-2026-10-21\|Votre logiciel est lisible par n'importe quel agent : guide pour éditeurs]]
  - [[fiches/2026-10/sfeir-electron-asar-secrets-2026-10-21\|Applications Electron : secrets et logique métier exposés dans l'ASAR]]
  - [[fiches/2026-10/sfeir-obfuscation-code-agents-2026-10-16\|Obfuscation et protection du code à l'ère des agents]]
  - [[fiches/2026-10/sfeir-rea-application-electron-2026-10-15\|Ce qu'une analyse REA révèle d'une application Electron]]
  - [[fiches/2026-10/sfeir-rea-limites-2026-10-15\|Les limites réelles de REA : taille des sorties, coût, couverture]]
  - [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
- [[kb/_entites-mineures#.NET\|.NET]] (TECHNOLOGIE) — 0.92, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-dotnet-2026-10-17\|Analyser des assemblies .NET avec REA]]
- [[kb/_entites-mineures#analyse-de-malware\|analyse de malware]] (METHODOLOGIE) — 0.90, DYNAMIQUE
  - [[fiches/2026-10/sfeir-analyse-malware-agent-local-2026-10-14\|Analyser un malware en local avec un agent, sans l'exfiltrer]]
- [[kb/_entites-mineures#audit-d'application-mobile\|audit d'application mobile]] (METHODOLOGIE) — 0.90, ATEMPOREL
  - [[fiches/2026-10/sfeir-rea-android-apk-2026-10-19\|REA et Android : auditer une APK avec JADX et Apktool]]
- [[kb/Claude-Code\|Claude Code]] (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
- [[kb/_entites-mineures#Slack\|Slack]] (TECHNOLOGIE) — 0.88, STATIQUE
  - [[fiches/2026-10/sfeir-editeurs-logiciel-lisible-agents-2026-10-21\|Votre logiciel est lisible par n'importe quel agent : guide pour éditeurs]]
- [[kb/_entites-mineures#rétro-ingénierie\|rétro-ingénierie]] (CONCEPT) — 0.84, DYNAMIQUE
  - [[fiches/2026-10/sfeir-licence-retro-ingenierie-clauses-nulles-2026-10-13\|Clauses de licence et rétro-ingénierie : ce qui est nul en France]]
- SQLite (TECHNOLOGIE) — 0.80, DYNAMIQUE
  - [[fiches/2026-10/sfeir-formats-proprietaires-retro-documentation-2026-10-18\|Formats de fichiers propriétaires : rétro-documenter pour migrer les données]]
- [[kb/WinDev\|WinDev]] (TECHNOLOGIE) — 0.72, DYNAMIQUE
  - [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]

### utilise

- [[kb/_entites-mineures#Binwalk\|Binwalk]] (TECHNOLOGIE) — 0.95, DYNAMIQUE
  - [[fiches/2026-10/sfeir-retro-ingenierie-firmware-iot-2026-10-21\|Firmware et objets connectés : la rétro-ingénierie par agents]]
- [[kb/_entites-mineures#Ghidra\|Ghidra]] (TECHNOLOGIE) — 0.95, DYNAMIQUE
  - [[fiches/2026-10/sfeir-analyse-malware-agent-local-2026-10-14\|Analyser un malware en local avec un agent, sans l'exfiltrer]]
  - [[fiches/2026-10/sfeir-audit-binaire-fournisseur-2026-10-17\|Auditer un binaire fournisseur sans son code source]]
  - [[fiches/2026-10/sfeir-cra-sbom-binaire-2026-10-17\|Cyber Resilience Act et SBOM : inventorier un binaire livré sans inventaire]]
  - [[fiches/2026-10/sfeir-ctf-crackmes-formation-retro-ingenierie-2026-10-16\|CTF et crackmes : former ses équipes à la rétro-ingénierie assistée par agents]]
  - [[fiches/2026-10/sfeir-decompilation-interoperabilite-dsi-2026-10-12\|Décompiler pour interopérer : l'article 6 de la directive expliqué à une DSI]]
  - [[fiches/2026-10/sfeir-editeur-disparu-code-perdu-2026-10-19\|Éditeur disparu, code source perdu : plan de sauvetage d'une application critique]]
  - [[fiches/2026-10/sfeir-fin-avantage-code-ferme-2026-10-21\|REA, ArtCraft et la fin de l'avantage du code fermé]]
  - [[fiches/2026-10/sfeir-legacy-sans-code-source-2026-10-16\|Applications legacy sans code source : comprendre avant de réécrire]]
  - [[fiches/2026-10/sfeir-obfuscation-code-agents-2026-10-16\|Obfuscation et protection du code à l'ère des agents]]
  - [[fiches/2026-10/sfeir-rea-application-electron-2026-10-15\|Ce qu'une analyse REA révèle d'une application Electron]]
  - [[fiches/2026-10/sfeir-rea-dotnet-2026-10-17\|Analyser des assemblies .NET avec REA]]
  - [[fiches/2026-10/sfeir-rea-evidence-sortie-agent-2026-10-15\|Lire une sortie REA : preuves, pseudocode et hallucinations]]
  - [[fiches/2026-10/sfeir-rea-ghidramcp-ida-pro-mcp-2026-10-20\|REA, GhidraMCP ou ida-pro-mcp : quel MCP de rétro-ingénierie choisir]]
  - [[fiches/2026-10/sfeir-rea-limites-2026-10-15\|Les limites réelles de REA : taille des sorties, coût, couverture]]
  - [[fiches/2026-10/sfeir-rea-sandbox-confinement-2026-10-13\|REA n'est pas un sandbox : confiner l'analyse d'un binaire inconnu]]
  - [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
  - [[fiches/2026-10/sfeir-retro-ingenierie-agents-securite-2026-10-16\|Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité]]
  - [[fiches/2026-10/sfeir-retro-ingenierie-delphi-2026-10-17\|Applications Delphi : ce que Ghidra et les agents permettent]]
  - [[fiches/2026-10/sfeir-retro-ingenierie-firmware-iot-2026-10-21\|Firmware et objets connectés : la rétro-ingénierie par agents]]
  - [[fiches/2026-10/sfeir-retro-ingenierie-powerbuilder-nsdk-2026-10-20\|PowerBuilder et NSDK : état des lieux de la rétro-ingénierie par agents]]
  - [[fiches/2026-10/sfeir-retro-ingenierie-vb6-2026-10-18\|Rétro-ingénierie d'applications VB6 : peu de retours, un workflow possible]]
  - [[fiches/2026-10/sfeir-souverainete-audit-logiciel-2026-10-19\|Souveraineté : auditer le comportement d'un logiciel extra-européen]]
  - [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]
- [[kb/MCP\|MCP]] (TECHNOLOGIE) — 0.95, DYNAMIQUE
  - [[fiches/2026-10/sfeir-legacy-sans-code-source-2026-10-16\|Applications legacy sans code source : comprendre avant de réécrire]]
  - [[fiches/2026-10/sfeir-rea-android-apk-2026-10-19\|REA et Android : auditer une APK avec JADX et Apktool]]
  - [[fiches/2026-10/sfeir-rea-deploiement-entreprise-2026-10-20\|Déployer REA en entreprise : versions, profils, conteneurs]]
  - [[fiches/2026-10/sfeir-rea-faux-depots-supply-chain-2026-10-14\|Faux dépôts REA et cheval de Troie : le risque supply chain d'un outil viral]]
  - [[fiches/2026-10/sfeir-rea-limites-2026-10-15\|Les limites réelles de REA : taille des sorties, coût, couverture]]
  - [[fiches/2026-10/sfeir-rea-sandbox-confinement-2026-10-13\|REA n'est pas un sandbox : confiner l'analyse d'un binaire inconnu]]
  - [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
- [[kb/_entites-mineures#Unblob\|Unblob]] (TECHNOLOGIE) — 0.95, DYNAMIQUE
  - [[fiches/2026-10/sfeir-retro-ingenierie-firmware-iot-2026-10-21\|Firmware et objets connectés : la rétro-ingénierie par agents]]
- [[kb/_entites-mineures#JADX\|JADX]] (TECHNOLOGIE) — 0.94, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-android-apk-2026-10-19\|REA et Android : auditer une APK avec JADX et Apktool]]
  - [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
  - [[fiches/2026-10/sfeir-rgpd-verifier-telemetrie-application-2026-10-18\|RGPD : vérifier ce qu'une application envoie vraiment]]
- [[kb/_entites-mineures#agents-de-code\|agents de code]] (TECHNOLOGIE) — 0.93, DYNAMIQUE
  - [[fiches/2026-10/sfeir-fin-avantage-code-ferme-2026-10-21\|REA, ArtCraft et la fin de l'avantage du code fermé]]
- [[kb/_entites-mineures#Apktool\|Apktool]] (TECHNOLOGIE) — 0.92, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-android-apk-2026-10-19\|REA et Android : auditer une APK avec JADX et Apktool]]
- [[kb/_entites-mineures#IDA-Pro\|IDA Pro]] (TECHNOLOGIE) — 0.90, DYNAMIQUE
  - [[fiches/2026-10/sfeir-editeur-disparu-code-perdu-2026-10-19\|Éditeur disparu, code source perdu : plan de sauvetage d'une application critique]]
  - [[fiches/2026-10/sfeir-rea-ghidramcp-ida-pro-mcp-2026-10-20\|REA, GhidraMCP ou ida-pro-mcp : quel MCP de rétro-ingénierie choisir]]
- [[kb/_entites-mineures#jadx-headless-mcp\|jadx-headless-mcp]] (TECHNOLOGIE) — 0.90, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-android-apk-2026-10-19\|REA et Android : auditer une APK avec JADX et Apktool]]
- Hopper (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-editeur-disparu-code-perdu-2026-10-19\|Éditeur disparu, code source perdu : plan de sauvetage d'une application critique]]
  - [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]
- IDA (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-retro-ingenierie-agents-securite-2026-10-16\|Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité]]
  - [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]
- Node.js (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-application-electron-2026-10-15\|Ce qu'une analyse REA révèle d'une application Electron]]
- [[kb/_entites-mineures#Wakaru\|Wakaru]] (TECHNOLOGIE) — 0.88, DYNAMIQUE
  - [[fiches/2026-10/sfeir-obfuscation-code-agents-2026-10-16\|Obfuscation et protection du code à l'ère des agents]]
- [[kb/Claude-Code\|Claude Code]] (TECHNOLOGIE) — 0.85, DYNAMIQUE
  - [[fiches/2026-10/sfeir-rea-deploiement-entreprise-2026-10-20\|Déployer REA en entreprise : versions, profils, conteneurs]]
- [[kb/_entites-mineures#cargo-auditable\|cargo-auditable]] (TECHNOLOGIE) — 0.80, DYNAMIQUE
  - [[fiches/2026-10/sfeir-audit-binaire-fournisseur-2026-10-17\|Auditer un binaire fournisseur sans son code source]]
- [[kb/_entites-mineures#fuses-Electron\|fuses Electron]] (TECHNOLOGIE) — 0.80, DYNAMIQUE
  - [[fiches/2026-10/sfeir-electron-asar-secrets-2026-10-21\|Applications Electron : secrets et logique métier exposés dans l'ASAR]]

## Relations (comme objet)

- [[kb/faux-dépôt-rea-tools-rea\|faux dépôt rea-tools/rea]] **s_applique_à** → REA — 0.93
- [[kb/_entites-mineures#rea-agents\|rea-agents]] **fait_partie_de** → REA — 0.92
- [[kb/_entites-mineures#audit-de-binaire-fournisseur\|audit de binaire fournisseur]] **utilise** → REA — 0.92
- [[kb/Connor-Turland\|Connor Turland]] **utilise** → REA — 0.92
- [[kb/_entites-mineures#formation-à-la-rétro-ingénierie-assistée-par-agents\|formation à la rétro-ingénierie assistée par agents]] **utilise** → REA — 0.92
- [[kb/inventaire-de-binaire-par-agent\|inventaire de binaire par agent]] **utilise** → REA — 0.92
- [[kb/_entites-mineures#pont-authentifié-par-jeton\|pont authentifié par jeton]] **fait_partie_de** → REA — 0.90
- [[kb/_entites-mineures#revue-en-trois-états-(vu,-inféré,-inconnu)\|revue en trois états (vu, inféré, inconnu)]] **s_applique_à** → REA — 0.90
- [[kb/audit-de-télémétrie\|audit de télémétrie]] **utilise** → REA — 0.90
- [[kb/_entites-mineures#morluto\|morluto]] **a_créé** → REA — 0.88
- [[kb/profil-compact\|profil compact]] **fait_partie_de** → REA — 0.88
- [[kb/audit-de-comportement-logiciel\|audit de comportement logiciel]] **utilise** → REA — 0.88
- [[kb/rétro-documentation\|rétro-documentation]] **utilise** → REA — 0.88
- [[kb/rétro-documentation-de-format\|rétro-documentation de format]] **utilise** → REA — 0.82
- [[kb/docker-reverse-engineer-anything\|docker-reverse-engineer-anything]] **est_variante_de** → REA — 0.78

## Fiches sources

- [[fiches/2026-10/sfeir-audit-binaire-fournisseur-2026-10-17\|Auditer un binaire fournisseur sans son code source]]
- [[fiches/2026-10/sfeir-clean-room-vs-reverse-engineering-2026-10-11\|Clean-room ou reverse engineering : méthode et risque juridique à l'ère des agents]]
- [[fiches/2026-10/sfeir-cra-sbom-binaire-2026-10-17\|Cyber Resilience Act et SBOM : inventorier un binaire livré sans inventaire]]
- [[fiches/2026-10/sfeir-ctf-crackmes-formation-retro-ingenierie-2026-10-16\|CTF et crackmes : former ses équipes à la rétro-ingénierie assistée par agents]]
- [[fiches/2026-10/sfeir-decompilation-interoperabilite-dsi-2026-10-12\|Décompiler pour interopérer : l'article 6 de la directive expliqué à une DSI]]
- [[fiches/2026-10/sfeir-editeur-disparu-code-perdu-2026-10-19\|Éditeur disparu, code source perdu : plan de sauvetage d'une application critique]]
- [[fiches/2026-10/sfeir-editeurs-logiciel-lisible-agents-2026-10-21\|Votre logiciel est lisible par n'importe quel agent : guide pour éditeurs]]
- [[fiches/2026-10/sfeir-electron-asar-secrets-2026-10-21\|Applications Electron : secrets et logique métier exposés dans l'ASAR]]
- [[fiches/2026-10/sfeir-fin-avantage-code-ferme-2026-10-21\|REA, ArtCraft et la fin de l'avantage du code fermé]]
- [[fiches/2026-10/sfeir-formats-proprietaires-retro-documentation-2026-10-18\|Formats de fichiers propriétaires : rétro-documenter pour migrer les données]]
- [[fiches/2026-10/sfeir-legacy-sans-code-source-2026-10-16\|Applications legacy sans code source : comprendre avant de réécrire]]
- [[fiches/2026-10/sfeir-obfuscation-code-agents-2026-10-16\|Obfuscation et protection du code à l'ère des agents]]
- [[fiches/2026-10/sfeir-rea-android-apk-2026-10-19\|REA et Android : auditer une APK avec JADX et Apktool]]
- [[fiches/2026-10/sfeir-rea-application-electron-2026-10-15\|Ce qu'une analyse REA révèle d'une application Electron]]
- [[fiches/2026-10/sfeir-rea-deploiement-entreprise-2026-10-20\|Déployer REA en entreprise : versions, profils, conteneurs]]
- [[fiches/2026-10/sfeir-rea-dotnet-2026-10-17\|Analyser des assemblies .NET avec REA]]
- [[fiches/2026-10/sfeir-rea-evidence-sortie-agent-2026-10-15\|Lire une sortie REA : preuves, pseudocode et hallucinations]]
- [[fiches/2026-10/sfeir-rea-faux-depots-supply-chain-2026-10-14\|Faux dépôts REA et cheval de Troie : le risque supply chain d'un outil viral]]
- [[fiches/2026-10/sfeir-rea-ghidramcp-ida-pro-mcp-2026-10-20\|REA, GhidraMCP ou ida-pro-mcp : quel MCP de rétro-ingénierie choisir]]
- [[fiches/2026-10/sfeir-rea-limites-2026-10-15\|Les limites réelles de REA : taille des sorties, coût, couverture]]
- [[fiches/2026-10/sfeir-rea-sandbox-confinement-2026-10-13\|REA n'est pas un sandbox : confiner l'analyse d'un binaire inconnu]]
- [[fiches/2026-10/sfeir-rea-trois-schemas-architecture-usage-2026-10-12\|REA en trois schémas : architecture, fonctionnement et usage]]
- [[fiches/2026-10/sfeir-retro-ingenierie-agents-securite-2026-10-16\|Rétro-ingénierie par agents : ce que ça change pour les équipes sécurité]]
- [[fiches/2026-10/sfeir-retro-ingenierie-delphi-2026-10-17\|Applications Delphi : ce que Ghidra et les agents permettent]]
- [[fiches/2026-10/sfeir-retro-ingenierie-firmware-iot-2026-10-21\|Firmware et objets connectés : la rétro-ingénierie par agents]]
- [[fiches/2026-10/sfeir-retro-ingenierie-vb6-2026-10-18\|Rétro-ingénierie d'applications VB6 : peu de retours, un workflow possible]]
- [[fiches/2026-10/sfeir-rgpd-verifier-telemetrie-application-2026-10-18\|RGPD : vérifier ce qu'une application envoie vraiment]]
- [[fiches/2026-10/sfeir-souverainete-audit-logiciel-2026-10-19\|Souveraineté : auditer le comportement d'un logiciel extra-européen]]
- [[fiches/2026-10/sfeir-windev-agents-rea-clean-room-2026-10-15\|Moderniser une application WinDev avec des agents : REA et méthode clean-room]]
