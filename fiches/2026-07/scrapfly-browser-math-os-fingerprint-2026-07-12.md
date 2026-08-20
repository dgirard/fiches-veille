---
themes: [qualite-securite, architecture-construction, outils-plateformes]
source: "Scrapfly"
---
# scrapfly-browser-math-os-fingerprint-2026-07-12

## Veille

Article d'ingénierie publié le **12 juillet 2026** par **Scrapfly Engineering**, sur un canal de *fingerprinting* de navigateur peu connu : **les derniers bits d'un nombre flottant trahissent le système d'exploitation**. **Le mécanisme** : IEEE 754 définit comment un `double` est stocké, mais **n'exige pas** que `sin`, `cos`, `tanh` ou `exp` soient correctement arrondis ; chaque système livre donc une **libm** qui échange une fraction d'ULP contre de la vitesse, avec ses propres coefficients minimax, tables et constantes de réduction. Résultat, `Math.tanh(0.8)` rend **trois valeurs différentes** selon glibc (Linux), libsystem_m (macOS) et UCRT (Windows) — *« one tanh call on the right input is a per-OS signature. Claim macOS, return Linux math bits, and you have contradicted your own User-Agent. »* **Le tell est récent et daté précisément** : jusqu'à **Chrome 147**, V8 calculait `tanh` avec un portage **fdlibm** embarqué, identique partout et ne fuitant rien ; le commit V8 `c1486295ae5` l'a remplacé par `std::tanh`, livré dans V8 14.8.57 soit **Chrome 148** — 148, 149 et 150 fuient, 147 et antérieurs non. **Trois surfaces concentrent les fuites** : `Math.tanh` (le **seul** `Math.*` concerné, puisque V8 embarque et lie statiquement le reste), **toutes les fonctions trigonométriques CSS** (Blink appelle la libm hôte directement, après une réduction d'angle en degrés qui ne partage pas le code de `Math.sin`), et **Web Audio** (où le compresseur reste en scalaire libsystem_m tandis que la FFT et les étages vectoriels passent par **Accelerate**). **Quatre pièges** rendent la contre-mesure difficile : seule une partie des fonctions fuit — donc **spoofer les autres crée une incohérence détectable** ; JavaScript et CSS sont des chemins de code distincts ; **macOS embarque deux bibliothèques mathématiques qui divergent entre elles** (scalaire vs Accelerate, de 10 à 89 % des entrées selon la fonction : `cos(0)` rend `1.0` d'un côté, `0.9999999999999999` de l'autre) ; et l'**architecture fuit aussi** (FMA et propagation du signe des NaN diffèrent entre ARM et x86). **La parade rejetée et la parade retenue** : ajouter du bruit échoue deux fois — la valeur ne correspond à **aucun** OS réel, et la non-déterminisme par appel est lui-même un tell. La seule voie est la **reproduction bit à bit** : extraire les coefficients de la libm cible, les transcrire **en hexadécimal** (une transcription décimale arrondirait autrement), écrire chaque fusion multiplication-addition en `fma()` explicite et compiler avec `-ffp-contract=off` pour que le compilateur n'en invente ni n'en supprime aucune. **Divulgation à consigner** : l'éditeur indique en tête que *« the posts here are drafted with AI »*, les mécanismes, chiffres et code restant les siens.

## Titre Article

Your Browser Does Math Differently on Every OS, and Anti-Bot Systems Read the Bits

## Date

2026-07-12

## URL

https://scrapfly.dev/posts/browser-math-os-fingerprint/

## Keywords

fingerprinting, empreinte de navigateur, anti-bot, détection d'automatisation, IEEE 754, arrondi correct, ULP, unit in the last place, libm, glibc, libsystem_m, UCRT, ucrtbase, fdlibm, llvm-libc, dbl-64, V8, Blink, Chrome 148, commit V8, Math.tanh, fonctions trigonométriques CSS, réduction d'angle en degrés, Web Audio, DynamicsCompressor, Accelerate, vDSP, vvsin, vvtanh, FFT, biquad, Apple Silicon, ARM vs x86, FMA, fused multiply-add, propagation de NaN, WASM, coefficients minimax, tables d'exposants, constantes de réduction, reproduction bit à bit, transcription hexadécimale, ffp-contract, déterminisme, bruit comme contre-mesure, incohérence de spoofing, User-Agent contradictoire, surface de détection, agents navigateurs, Scrapfly

## Authors

**Scrapfly Engineering** — équipe d'ingénierie de **Scrapfly**, fournisseur d'infrastructure de collecte web. Le texte annonce sa position d'intérêt sans détour : *« Scrapfly ships a browser that has to match a real one across hundreds of signals, and math is one of the harder ones. »* On lit donc un **attaquant du problème de détection**, qui documente le canal parce qu'il doit le neutraliser.

**Divulgation éditoriale explicite**, à consigner parce qu'elle est rare : *« A note on how these are written: the posts here are drafted with AI. That lets our engineers put research and findings out quickly and spend their effort on the technical substance instead of the prose. The mechanisms, the numbers, and the code are ours. »* La rédaction est assistée, les mesures et le code sont revendiqués par l'équipe.

## Ton

**Profil** : article d'ingénierie de très haute densité technique, registre *engineering blog* d'éditeur d'infrastructure. Douze minutes annoncées, aucune concession pédagogique : on entre par un extrait de console et on sort par du C avec des coefficients en hexadécimal.

**Style** : **la démonstration précède l'explication**. Le texte s'ouvre sur trois lignes à coller dans une console — `Math.tanh(0.8)` et ses trois sorties commentées par OS — avant d'expliquer pourquoi. Puis un tableau de mesures réelles sur trois machines physiques, avec la précision qui fait la différence entre une anecdote et un protocole : *« Measured over the DevTools protocol on Chrome 150: Linux (glibc), macOS 26 on Apple Silicon (libsystem_m), Windows 11 (ucrtbase.dll). »*

**Deux traits de méthode** :

1. **L'entrée-témoin est choisie, pas trouvée.** *« tanh(0.5) is one of the roughly three-in-four inputs where everyone agrees, which is exactly why it makes a useless probe. tanh(0.8) is one that separates all three at once. »* Le texte explique **comment on construit une sonde**, pas seulement qu'elle existe.
2. **L'ambiguïté est résolue expérimentalement, pas par lecture de code.** Face à deux bibliothèques Apple concurrentes : *« We resolved it by driving real Chrome on a real Mac over the debugging protocol and reading the exact double. »*

**Registre argumentatif** : celui de la **réfutation ordonnée**. La section « Four traps » démonte une par une les solutions évidentes — *« "Just reimplement the Mac functions" breaks on contact, for four reasons »* — et la section suivante écarte la contre-mesure la plus intuitive (le bruit) avant de proposer la sienne.

**Formules-marqueurs** : *« There is a quieter signal, and it lives in the last bits of a number »*, *« a detector needs no math, only a table »*, *« Claim macOS, return Linux math bits, and you have contradicted your own User-Agent »*, *« Pick the wrong library for a given call site and you land 1 ULP off on most inputs, worse than not spoofing »*, *« CSS is a tell everywhere »*.

## Pense-betes

- **Le principe, en une ligne** : IEEE 754 impose le **stockage** d'un `double`, pas l'**arrondi correct** des fonctions transcendantes. L'arrondi correct coûte cher, donc chaque système livre sa propre libm avec ses coefficients minimax, ses tables et ses constantes de réduction. **La différence d'arrondi est une signature.**

- **La sonde, à connaître** : `Math.tanh(0.8)` rend `0.6640367702678491` sur Linux (glibc), `0.664036770267849` sur macOS (libsystem_m) et `0.6640367702678489` sur Windows (UCRT) — **les trois diffèrent, sur 2 ULP d'écart**. Linux et macOS divergent sur environ **un quart de toutes les entrées**, généralement d'**1 ULP** ; Windows diverge des deux sur quelques pour cent. → *« A detector needs no math, only a table. »*

- **Le tell est daté au commit près, et c'est ce qui rend l'article utile** : jusqu'à **Chrome 147**, V8 calculait `tanh` avec un portage **fdlibm** embarqué — même bits partout, **aucune fuite**. Le commit V8 **`c1486295ae5`** l'a remplacé par `std::tanh`, qui lit la libm hôte ; livré dans **V8 14.8.57 = Chrome 148**. **148, 149, 150 fuient. 147 et antérieurs non.** → **Une régression de confidentialité introduite par un choix d'implémentation banal**, et une fenêtre de version précise pour dater une empreinte.

- **La carte des fuites — la partie la plus réutilisable** :
  | Opération | `Math.*` (JS) | CSS `calc()` | Web Audio |
  |---|---|---|---|
  | `sin cos tan` | V8 embarqué | **libm hôte** | Accelerate (FFT), scalaire dans le compresseur |
  | `asin acos atan atan2` | V8 embarqué | **libm hôte** | non utilisé |
  | `tanh` | **libm hôte** | — | non utilisé |
  | `exp`, `log*`, `pow` | V8 embarqué | **libm hôte** | scalaire dans le compresseur |
  | vecteur, FFT | — | — | **Accelerate (vDSP)** sur Mac |
  | `sqrt`, arithmétique | matériel | matériel | matériel |
  → **V8 route presque tout par sa propre math embarquée : JavaScript ne fuit qu'en un point, `Math.tanh`. CSS fuit partout. Web Audio touche trois bibliothèques dans un même graphe.**

- **WASM ne fuit pas l'OS** : pas d'opcode transcendant, `sin` vient de la libm que le module a embarquée, et l'arithmétique (`f64.sqrt`, `f64.mul`) est matérielle. **Son seul axe d'empreinte est ARM vs x86** (canonicalisation des NaN, quelques arrondis SIMD).

- **Les quatre pièges — la vraie leçon de conception, transposable bien au-delà du sujet** :
  1. **Seule une partie fuit.** Spoofer les fonctions qui **ne** fuitent pas crée une incohérence, et *« that asymmetry is itself checkable »*. → **Corriger trop est aussi détectable que corriger trop peu.**
  2. **JS et CSS sont des chemins distincts.** Les trigonométriques CSS réduisent l'angle **en degrés** puis appellent `std::sin` sur la valeur réduite — résultat différent d'un `sin()` en radians. L'équipe a reproduit *« the degree reduction and the radians-to-degrees step bit-for-bit, not just the leaf function »*.
  3. **macOS a deux bibliothèques mathématiques qui se contredisent.** Scalaire `libsystem_m` et vectorielles d'**Accelerate** divergent sur **10 à 89 %** des entrées selon la fonction. `cos(0)` : `1.0` en scalaire, `0.9999999999999999` en Accelerate. → *« "Reproduce Apple's math" is undefined until you know which library the browser calls, at which site. »* Réponse établie expérimentalement : scalaire pour `Math.tanh`, la trigo CSS et les transcendantes par échantillon du compresseur ; Accelerate pour la DSP Web Audio (FFT, math vectorielle, filtres biquad). **Se tromper de bibliothèque coûte 1 ULP sur la plupart des entrées — pire que ne rien faire.**
  4. **L'architecture fuit.** ARM et x86 diffèrent sur la fusion multiplication-addition et sur la propagation du signe des NaN ; une reproduction correcte sur le papier dérive si le compilateur fusionne d'un côté et pas de l'autre.

- **Pourquoi le bruit ne marche pas — argument généralisable à toute contre-mesure de fingerprinting** : *« Perturbing the output fails twice. A reference comparison sees a value that matches no real OS, and per-call randomness breaks determinism, which is its own tell. »* → **Une défense qui rend une valeur impossible est aussi identifiante qu'une valeur vraie.** La cible n'est pas « du bruit », c'est **la valeur exacte du système revendiqué**.

- **La parade retenue, et ses trois exigences** : (1) **récupérer** coefficients minimax, tables d'exposants et constantes de réduction dans la libm cible et les **transcrire en portable C** ; (2) **copier les motifs de bits en hexadécimal** — *« a decimal transcription would round differently »* ; (3) **écrire chaque fusion en `fma()` explicite** et compiler avec **`-ffp-contract=off`**, pour que les opérations fusionnées soient exactement celles qu'Apple fuse et que le résultat soit identique sur CPU avec et sans FMA, et **entre la machine ARM imitée et la flotte x86 qui exécute**. Quand la reproduction ne vaut pas l'effort : *« lift the original »* — l'UCRT Windows étant x86-64 et à code indépendant de la position.

- **Ce que l'article implique pour les agents qui naviguent** — non dit par le texte, mais direct : un agent qui pilote un navigateur pour lire le web franchit exactement ces contrôles. Les harnais qui **escaladent vers le navigateur réel de l'utilisateur** plutôt que d'imiter un navigateur (cf. la voie navigateur de [[skill-gibbs-hyperresearch-2026-08-03]], qui pilote le Chrome authentifié et pose comme frontière dure que *« CAPTCHAs, 2FA, and logins are never solved automatically »*) contournent le problème par construction : **il n'y a rien à falsifier quand le navigateur est authentiquement celui qu'il prétend être.** Deux stratégies opposées face au même mur.

- **Cadre d'usage** : l'article documente une technique de **contournement de détection**, écrite par un fournisseur de collecte web. Il est utilisable en défense (comprendre ce que son anti-bot lit réellement, et savoir qu'un signal `Math.tanh` isolé date le navigateur autant qu'il identifie l'OS) comme en contournement. **Rien dans le texte ne traite du consentement des sites collectés**, ni des conditions d'utilisation — c'est hors de son périmètre déclaré.

- **Rédaction assistée par IA, déclarée** : *« the posts here are drafted with AI… The mechanisms, the numbers, and the code are ours. »* Divulgation honnête et rare ; à mentionner si l'on cite le texte comme source primaire. Les mesures sont assorties de leur protocole (protocole DevTools, trois machines nommées avec leurs versions), ce qui les rend contrôlables indépendamment de la façon dont la prose a été produite.

- **Méta / à relier** : côté agents pilotant un navigateur, [[skill-gibbs-hyperresearch-2026-08-03]] (voie navigateur, escalade, frontière CAPTCHA) ; côté surface d'attaque et contenu web traité comme donnée hostile, [[valente-zalewski-beyond-zero-enterprise-security-ai-era-2026-07-20]] ; côté navigateurs IA et automatisation, [[mody-browser-company-arc-dia-ai-native-2025-11-23]], perplexity-chrome-integration-browser-ai-search-2025-10-22 et mcp-replaces-browser-logrocket-2025-09-15.

## RésuméDe400mots

Article de **Scrapfly Engineering** (12 juillet 2026) sur un canal de *fingerprinting* logé **dans les derniers bits d'un nombre**.

**Le mécanisme.** IEEE 754 définit le stockage d'un `double` mais **n'exige pas** l'arrondi correct des fonctions transcendantes. L'arrondi correct étant coûteux, chaque plateforme livre une **libm** avec ses propres coefficients minimax, tables et constantes. Conséquence : `Math.tanh(0.8)` rend trois valeurs distinctes selon glibc, libsystem_m et UCRT. Linux et macOS divergent sur environ un quart des entrées, généralement d'**1 ULP**. *« A detector needs no math, only a table. »* Et l'incohérence est immédiatement exploitable : annoncer macOS en rendant les bits de Linux **contredit son propre User-Agent**.

**Le tell est récent et daté.** Jusqu'à **Chrome 147**, V8 calculait `tanh` avec un fdlibm embarqué, identique partout. Le commit `c1486295ae5` l'a remplacé par `std::tanh`, qui lit la libm hôte, livré avec **Chrome 148**.

**Trois surfaces fuient.** `Math.tanh` est le **seul** `Math.*` concerné — V8 embarque et lie statiquement tout le reste. Les **sept fonctions trigonométriques CSS** fuient toutes, Blink appelant la libm hôte après une réduction d'angle en degrés qui ne partage pas le code de `Math.sin`. Et **Web Audio** touche trois bibliothèques dans un même graphe : Accelerate pour la FFT et les étages vectoriels, scalaire libsystem_m pour les transcendantes du compresseur. WASM, lui, ne fuit pas l'OS — seulement l'architecture.

**Quatre pièges** rendent la contre-mesure difficile : seule une partie des fonctions fuit, donc **spoofer les autres crée une asymétrie détectable** ; JavaScript et CSS sont des chemins de code séparés ; **macOS embarque deux bibliothèques mathématiques qui divergent entre elles** de 10 à 89 % selon la fonction, si bien que « reproduire la math d'Apple » n'a pas de sens tant qu'on ignore laquelle est appelée à quel site ; et ARM et x86 diffèrent sur la fusion multiplication-addition et la propagation des NaN.

**Le bruit ne marche pas** : il produit une valeur qui ne correspond à **aucun** OS réel, et sa non-déterminisme est elle-même un signal. La seule voie est la **reproduction bit à bit** — coefficients extraits de la libm cible et transcrits en hexadécimal, chaque fusion écrite en `fma()` explicite, compilation avec `-ffp-contract=off`.

L'éditeur déclare que ses billets sont **rédigés avec l'aide de l'IA**, les mécanismes, chiffres et code restant les siens.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Scrapfly | ORGANISATION | publie | Your Browser Does Math Differently on Every OS | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| IEEE 754 | CONCEPT | s_applique_à | le stockage d'un double, sans exiger l'arrondi correct des fonctions transcendantes | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| libm de plateforme | TECHNOLOGIE | permet | d'identifier le système d'exploitation d'un navigateur par la différence d'arrondi d'une fonction transcendante | AFFIRMATION | 0.96 | ATEMPOREL | déclaré_article |
| Math.tanh | TECHNOLOGIE | mesure | trois valeurs distinctes sur glibc, libsystem_m et UCRT pour l'entrée 0.8 | MESURE | 0.95 | DYNAMIQUE | déclaré_article |
| Chrome 148 | TECHNOLOGIE | remplace | le calcul embarqué de tanh par un appel à la libm hôte, introduisant la fuite | AFFIRMATION | 0.94 | STATIQUE | déclaré_article |
| fonctions trigonométriques CSS | TECHNOLOGIE | s_oppose_à | les fonctions Math de JavaScript, dont elles ne partagent pas le chemin de code | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| Web Audio | TECHNOLOGIE | utilise | trois bibliothèques mathématiques distinctes dans un même graphe audio sur macOS | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Accelerate | TECHNOLOGIE | s_oppose_à | libsystem_m scalaire, les deux divergeant sur 10 à 89 % des entrées selon la fonction | MESURE | 0.92 | ATEMPOREL | déclaré_article |
| spoofing partiel d'une empreinte | CONCEPT | s_oppose_à | la cohérence de l'empreinte, l'asymétrie créée étant elle-même vérifiable | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| ajout de bruit | CONCEPT | s_oppose_à | la dissimulation d'une empreinte, en produisant une valeur ne correspondant à aucun système réel | AFFIRMATION | 0.95 | ATEMPOREL | déclaré_article |
| Scrapfly | ORGANISATION | recommande | de reproduire bit à bit l'algorithme de la libm cible plutôt que de perturber sa sortie | AFFIRMATION | 0.94 | ATEMPOREL | déclaré_article |
| transcription hexadécimale des coefficients | CONCEPT | résout | l'erreur d'arrondi qu'introduirait une transcription décimale | AFFIRMATION | 0.93 | ATEMPOREL | déclaré_article |
| option de compilation ffp-contract=off | TECHNOLOGIE | permet | de rendre déterministes les fusions multiplication-addition entre architectures | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| WebAssembly | TECHNOLOGIE | réduit | la surface d'empreinte, n'exposant que la distinction ARM contre x86 | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| Scrapfly | ORGANISATION | affirme_que | ses billets sont rédigés avec l'aide de l'IA, les mécanismes, chiffres et code restant les siens | CITATION | 0.95 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| empreinte mathématique de navigateur | CONCEPT | définition | Canal de fingerprinting exploitant le fait que les fonctions transcendantes ne sont pas correctement arrondies : la différence d'arrondi entre bibliothèques mathématiques identifie le système d'exploitation réel | AJOUT |
| Your Browser Does Math Differently on Every OS | DOCUMENT | référence | Article Scrapfly Engineering du 12 juillet 2026 cartographiant les fuites d'OS via Math.tanh, la trigonométrie CSS et Web Audio, et détaillant la reproduction bit à bit comme seule contre-mesure | AJOUT |
| Scrapfly | ORGANISATION | positionnement | Fournisseur d'infrastructure de collecte web ; livre un navigateur devant correspondre à un vrai sur des centaines de signaux — position d'attaquant du problème de détection | AJOUT |
| ULP | CONCEPT | définition | Unit in the last place : plus petit écart représentable entre deux flottants voisins, unité dans laquelle se mesurent les divergences entre bibliothèques mathématiques | AJOUT |
| cohérence d'empreinte | CONCEPT | définition | Exigence selon laquelle une empreinte falsifiée doit l'être sur toutes les surfaces liées et sur aucune autre — corriger trop est aussi détectable que corriger trop peu | AJOUT |
