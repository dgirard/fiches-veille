---
themes: [qualite-securite, outils-plateformes]
source: SFEIR
---
# sfeir-rea-ghidramcp-ida-pro-mcp-2026-10-20

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **20 octobre 2026**, mis à jour le 23 (~1 150 mots, sept sources : README des trois dépôts, grille tarifaire Hex-Rays, test de Jacar Systems, API GitHub). Il compare les trois serveurs MCP qui *« dominent la rétro-ingénierie par agents à l'automne 2026 »*. **(1) Architectures** : **REA** (morluto/rea, MIT) orchestre Hopper, Ghidra ou IDA et lit lui-même JavaScript/Electron, .NET, APK, firmware et sites web ; **GhidraMCP** (LaurieWired, Apache-2.0) branche un agent sur Ghidra et renomme dans le projet ; **ida-pro-mcp** (mrexodia, MIT) exige IDA Pro 8.3+, écrit dans la base et expose `py_eval`, son auteur recommandant le serveur officiel de **Hex-Rays**. **(2) Coût des moteurs** : Ghidra gratuit ; IDA Pro Essential à partir de **1 099 €/an**, Expert **4 999 €**, Ultimate **8 599 €** ; IDA Home et Free hors usage d'entreprise. **(3) Couverture** : pont mono-moteur plus léger pour du natif seul, REA quand la question traverse les couches. **(4) Gouvernance** : les trois écrivent ou exécutent ; REA 6.7.0 pèse 207 outils. Grille finale : GhidraMCP, serveur Hex-Rays ou REA selon licences et parc. Fait partie de la série SFEIR d'octobre 2026 sur REA.

## Titre Article

REA, GhidraMCP ou ida-pro-mcp : quel MCP de rétro-ingénierie choisir

## Date

2026-10-20

## URL

https://www.sfeir.com/articles/rea-ghidramcp-ida-pro-mcp/

## Keywords

REA, GhidraMCP, ida-pro-mcp, IDA MCP, Hex-Rays, IDA Pro, IDA Free, IDA Home, Ghidra, PyGhidra, Hopper, JEB, MCP, rétro-ingénierie par agents, décompilateur, orchestrateur, licence MIT, Apache-2.0, coût des licences, droits d'écriture, py_eval, profil compact, fenêtre de contexte, parc hétérogène, Electron, .NET, comparatif, étoiles GitHub

## Authors

SFEIR AI, voix éditoriale non signée de SFEIR, publiée sur sfeir.com (site éditorial du cabinet).

## Ton

Comparatif structuré en français, à l'usage d'une DSI qui choisit son outillage. Le texte avance par critères (architecture, coût, couverture, gouvernance) et se termine sur une grille de choix conditionnelle, sans désigner de gagnant unique : le choix *« dépend de votre parc et des licences que vous possédez déjà »*. Les prix sont datés (23 octobre 2026) et rattachés à la page tarifaire de l'éditeur ; les licences des projets sont précisées. L'article relativise lui-même un indicateur de popularité (*« La popularité ne départage pas grand-chose »*) et cite un testeur externe (Jacar Systems) pour l'arbitrage mono-moteur contre orchestrateur. Registre neutre, FAQ courte, renvoi à l'offre AI Cyber de SFEIR.

## Pense-betes

- **REA** (morluto/rea, **MIT**) : orchestrateur ; natif via Hopper, Ghidra ou IDA ; analyse lui-même JavaScript/Electron, .NET, APK via JADX, firmware via Binwalk ou Unblob, sites via Chrome ; une trentaine de types de cibles ; conclusions avec preuves et limitations.
- **GhidraMCP** (LaurieWired, **Apache-2.0**) : expose Ghidra au client MCP, analyse headless via **PyGhidra** ; **écrit** dans le projet (renommage automatique des méthodes et données).
- **ida-pro-mcp** (mrexodia, **MIT**) : IDA Pro **8.3+** (9 recommandée), pas d'IDA Free ; écrit dans la base (valeurs, types) ; **`py_eval`** exécute du Python arbitraire ; le README recommande désormais le serveur MCP officiel de **Hex-Rays**.
- **Prix Hex-Rays au 23 octobre 2026** : IDA Pro Essential dès **1 099 €/an**, Expert dès **4 999 €**, Ultimate dès **8 599 €** ; IDA Home **365 $** (usage individuel non commercial) ; IDA Free gratuit, x86/x64, décompilateurs cloud. Usage d'entreprise = IDA Pro. Ghidra gratuit ; Hopper commercial (macOS, Linux).
- **Licences** : REA n'en fournit aucune ; un pont open source n'ajoute aucun droit d'usage d'IDA Pro, Hopper ou JEB.
- **Couverture** (Javier Cañete Arroyo, Jacar Systems, REA 6.7.0) : avec IDA ou Ghidra déjà en place, un pont mono-moteur est plus léger ; REA prend l'avantage quand la question traverse les couches (renderer Electron → add-on natif).
- **Gouvernance** : les trois écrivent ou exécutent ; confinement obligatoire pour un binaire inconnu ; REA 6.7.0 = **207 outils**, liste de 3 158 352 octets, 219 211 en profil compact.
- **Étoiles GitHub au 23 octobre** : GhidraMCP **11 494**, ida-pro-mcp **13 103**, REA **369 860** (essentiel accumulé en octobre).
- **Grille SFEIR** : sans licence commerciale, natif seul → GhidraMCP ; IDA Pro en place et annotation de la base → serveur Hex-Rays (ou ida-pro-mcp en connaissance de cause) ; parc hétérogène et preuves en format unique → REA, profil compact, version épinglée.

## RésuméDe400mots

L'article compare les trois serveurs MCP qui, selon SFEIR, dominent la rétro-ingénierie par agents à l'automne 2026 : REA, GhidraMCP et ida-pro-mcp. Le bon choix dépend du parc applicatif et des licences déjà détenues.

Les architectures diffèrent. REA, publié sous licence MIT, est un orchestrateur : il pilote Hopper, Ghidra ou IDA pour le code natif et analyse lui-même JavaScript et Electron, .NET, les APK via JADX, le firmware via Binwalk ou Unblob et les sites web via Chrome, chaque conclusion arrivant avec ses preuves et ses limites. GhidraMCP, de LaurieWired sous licence Apache-2.0, relie un agent à Ghidra, gratuit et open source, peut fonctionner sans interface via PyGhidra et écrit dans le projet en renommant méthodes et données. ida-pro-mcp, de mrexodia sous licence MIT, relie un agent à IDA Pro 8.3 ou plus récent, écrit dans la base et expose un outil qui exécute du Python arbitraire ; son README recommande désormais le serveur MCP officiel publié par Hex-Rays.

Le coût des moteurs pèse dans le choix. Ghidra est gratuit. La grille Hex-Rays consultée le 23 octobre 2026 affiche IDA Pro Essential à partir de 1 099 euros par an, Expert à partir de 4 999 et Ultimate à partir de 8 599 ; IDA Home et IDA Free ne couvrent pas un usage d'entreprise. REA ne fournit aucune licence : IDA Pro, Hopper et JEB doivent être acquis légalement, et un pont open source n'ajoute aucun droit.

Sur la couverture, un pont mono-moteur suffit et ajoute moins de surface si le besoin se limite au natif. Javier Cañete Arroyo, de Jacar Systems, estime après test de REA 6.7.0 que REA prend l'avantage quand la question traverse les couches, par exemple du renderer d'une application Electron vers un add-on natif. Sur un parc mixte, un point d'entrée unique apporte aussi un format de preuves commun.

Côté gouvernance, les trois outils écrivent ou exécutent quelque chose, ce qui impose le confinement pour un binaire inconnu. Le poids dans le contexte de l'agent diffère : REA 6.7.0 expose 207 outils, dont la liste dépasse 3 Mo et tombe à environ 219 Ko en profil compact. La popularité départage peu : 11 494 étoiles pour GhidraMCP, 13 103 pour ida-pro-mcp et 369 860 pour REA au 23 octobre.

La grille finale propose GhidraMCP sans licence commerciale et pour du natif seul, le serveur Hex-Rays avec une licence IDA Pro, et REA pour un parc hétérogène, avec profil compact et version épinglée.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | REA, GhidraMCP ou ida-pro-mcp : quel MCP de rétro-ingénierie choisir | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| REA | TECHNOLOGIE | concurrence | GhidraMCP | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | concurrence | ida-pro-mcp | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| REA | TECHNOLOGIE | utilise | IDA Pro | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| GhidraMCP | TECHNOLOGIE | utilise | Ghidra | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| LaurieWired | PERSONNE | a_créé | GhidraMCP | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| ida-pro-mcp | TECHNOLOGIE | utilise | IDA Pro | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| mrexodia | PERSONNE | a_créé | ida-pro-mcp | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| mrexodia | PERSONNE | recommande | IDA MCP | TECHNOLOGIE | 0.85 | DYNAMIQUE | déclaré_article |
| Hex-Rays | ORGANISATION | publie | IDA MCP | TECHNOLOGIE | 0.88 | DYNAMIQUE | déclaré_article |
| Hex-Rays | ORGANISATION | a_créé | IDA Pro | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | IDA Pro Essential à partir de 1 099 € par an au 23 octobre 2026 | MESURE | 0.9 | STATIQUE | déclaré_article |
| Javier Cañete Arroyo | PERSONNE | affirme_que | REA vaut son coût quand l'analyse traverse les couches (renderer Electron vers add-on natif) | AFFIRMATION | 0.86 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | mesure | 11 494 étoiles GhidraMCP, 13 103 ida-pro-mcp, 369 860 REA au 23 octobre 2026 | MESURE | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | GhidraMCP sans licence commerciale, IDA MCP avec IDA Pro, REA pour un parc hétérogène | AFFIRMATION | 0.9 | DYNAMIQUE | déclaré_article |
| GhidraMCP | TECHNOLOGIE | utilise | MCP | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| REA | TECHNOLOGIE | catégorie | orchestrateur MCP de rétro-ingénierie multi-moteurs, licence MIT | AJOUT |
| GhidraMCP | TECHNOLOGIE | catégorie | serveur MCP pour Ghidra (LaurieWired, Apache-2.0), écrit dans le projet | AJOUT |
| ida-pro-mcp | TECHNOLOGIE | catégorie | serveur MCP pour IDA Pro 8.3+ (mrexodia, MIT), outil py_eval | AJOUT |
| IDA MCP | TECHNOLOGIE | catégorie | serveur MCP officiel de Hex-Rays | AJOUT |
| IDA Pro | TECHNOLOGIE | prix | Essential dès 1 099 €/an, Expert dès 4 999 €, Ultimate dès 8 599 € (23 octobre 2026) | AJOUT |
| Ghidra | TECHNOLOGIE | licence | désassembleur-décompilateur gratuit et open source | AJOUT |
| Hex-Rays | ORGANISATION | produit | éditeur d'IDA Pro | AJOUT |
