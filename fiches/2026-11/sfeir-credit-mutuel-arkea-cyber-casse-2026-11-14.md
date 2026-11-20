---
themes: [qualite-securite, politique-regulation]
source: SFEIR
---
# sfeir-credit-mutuel-arkea-cyber-casse-2026-11-14

## Veille

Article SFEIR AI publié sur sfeir.com le **14 novembre 2026** (~2 700 mots, 21 sources), consacré à l'attaque subie par **Crédit Mutuel Arkéa** entre le **1er et le 3 novembre 2026** : environ **100 M€** sortis du compte propre de la banque par virements instantanés, à partir d'éléments d'authentification récupérés chez un prestataire. Trois apports : (A) **ce qui est établi** — premier signal par l'enquêteur **ZachXBT** (106 M$ puis 133 M$ de retraits sur plateformes crypto), traçage **Bitquery** (126 M$ en 28 heures), communiqués d'Arkéa du 4 novembre, enquête du parquet de Paris, récit du président **Julien Carmona** le 12 novembre (*« C'est comme s'ils avaient obtenu un trousseau de clés »*), détection en deux jours, préjudice ≈ **1 % des fonds propres** ; (B) **ce qui relève de l'hypothèse** — le rôle de l'IA (conviction de Carmona, sans élément technique publié, sur fond de lettre **BCE SSM-2026-0301** du 7 juillet 2026), l'attribution (Lazarus écarté par ZachXBT), l'identité du prestataire ; (C) **quatre leçons** : identités non humaines des tiers, vitesse des paiements face aux fenêtres de détection humaines, patching et segmentation, communication de crise. L'article situe le cadre réglementaire (DORA, règlement 2024/886, transposition de NIS2) et termine par six actions. Rejoint les fiches du corpus sur [[Claude-Mythos-5]] et Project Glasswing.

## Titre Article

Cyber-casse chez Crédit Mutuel Arkéa : ce que 100 millions d'euros enseignent aux DSI et aux RSSI

## Date

2026-11-14

## URL

https://www.sfeir.com/articles/credit-mutuel-arkea-cyber-casse-lecons-dsi-rssi/

## Keywords

Crédit Mutuel Arkéa, cyberattaque, cyber-casse, prestataire compromis, risque tiers, identités non humaines, virement instantané, règlement 2024/886, vérification du bénéficiaire, crypto, USDC, ZachXBT, Bitquery, Julien Carmona, BCE, lettre SSM-2026-0301, DORA, NIS2, zero trust, patch management, segmentation, communication de crise, Claude Mythos Preview, Project Glasswing

## Authors

SFEIR AI (voix éditoriale de SFEIR), article publié sur sfeir.com, site éditorial du groupe SFEIR.

## Ton

Article d'analyse d'incident en français, à destination des DSI et RSSI, construit selon une séparation explicite entre faits établis et hypothèses. La chronologie est reconstituée heure par heure à partir de sources primaires (canal Telegram de ZachXBT, communiqués de la banque, Les Echos, AFP, lettre de la BCE) avec citations datées. Les écarts entre chiffres sont expliqués plutôt que tranchés (perte nette provisoire de la banque contre retraits bruts observés on-chain). Les affirmations du président de la banque sont rapportées comme telles, la thèse de l'IA étant qualifiée de « conviction, sans élément technique publié ». L'article écarte une lecture qu'il juge non soutenue par les éléments publics (le cloud public comme cause). La partie prescriptive s'appuie sur des précédents (SolarWinds, MOVEit, Snowflake, Bangladesh) et sur le texte de la BCE, et se termine par une liste d'actions.

## Pense-betes

- **Chronologie** : 27 octobre, indices d'intrusion chez un prestataire, connexion coupée ; 1er novembre (dimanche), début des virements ; 2 novembre, ZachXBT signale 106 M$ ; 3 novembre au matin, la banque constate les mouvements et coupe ses accès externes ; 4 novembre, ZachXBT nomme Arkéa, communiqués à 13 h et 17 h 30, enquête du parquet (OFAC) ; incident contenu le 4.
- **Mécanique** (Carmona) : logiciel d'éditeur tiers compromis ; éléments *« de nature à compromettre les systèmes d'authentification »* ; faux comptes et IBAN (dont au nom de Fortuneo) ; virements instantanés vers de vrais comptes ouverts par les fraudeurs dans d'autres banques européennes, puis plateformes crypto.
- **On-chain** : Bitquery, 126 M$ en 28 h, moitié convertie en ether en 4 h, partie en Monero ; 12 des 17 portefeuilles préparés depuis mai ; Tether gèle 1,14 M USDT, Circle aucun.
- **Bilan** : « de l'ordre d'une centaine de millions d'euros », 1 % des fonds propres, un trimestre de résultats ; clients interrompus 1 à 1,5 jour ; Fortuneo, CCF, AXA Banque, Euro-Information non touchés (segmentation).
- **Hypothèses** : IA (*« très probablement appuyé par des modèles IA de pointe »*) ; lettre BCE du 7 juillet 2026 sur les menaces cyber liées à l'IA, plan d'action dû le 31 octobre ; attribution inconnue, Lazarus écarté par ZachXBT ; prestataire non confirmé (éditeur français de conformité selon Les Echos).
- **Leçon 1** : inventorier les identités non humaines des tiers (comptes de service, clés d'API, certificats, jetons OAuth) ; révoquer par défaut ; zero trust.
- **Leçon 2** : la vérification du bénéficiaire ne détecte pas un vrai compte ouvert par un fraudeur ; plafonds et vélocité sur comptes propres, mise en attente automatique, alerte aux plateformes. Mythos Preview a aidé une banque Glasswing à bloquer un virement de 1,5 M$.
- **Leçon 3** : patching des logiciels tiers inscrit dans les contrats et SLA. **Leçon 4** : message factuel en quelques heures, même partiel.
- **Cadre** : DORA (17 janvier 2025) ; règlement (UE) 2024/886 (9 octobre 2025) ; projet de loi Résilience (NIS2, REC, DORA) examiné le 10 novembre, deux ans de retard.
- À relier : [[Claude-Mythos-5]] (Project Glasswing, IA en défense).

## RésuméDe400mots

L'article de SFEIR analyse la cyberattaque qui a coûté environ cent millions d'euros à Crédit Mutuel Arkéa pendant le week-end de la Toussaint 2026. Les attaquants ont utilisé des éléments d'authentification récupérés chez un prestataire, des IBAN créés pour l'occasion et la rapidité du virement instantané pour vider une partie du compte propre de la banque.

La partie consacrée aux faits établis reconstitue la chronologie. Le premier signal public vient de l'enquêteur blockchain ZachXBT, qui signale le 2 novembre des retraits massifs sur des plateformes crypto, puis nomme la banque le 4. La société Bitquery retrace environ 126 millions de dollars sortis en 28 heures, convertis en partie en ether puis en Monero. Arkéa confirme l'attaque le 4 novembre, précise que l'entrée s'est faite par la plateforme d'un prestataire et non par sa filiale Fortuneo, et le parquet de Paris ouvre une enquête. Le 12 novembre, le président Julien Carmona décrit un logiciel tiers compromis, de faux comptes construits pour passer les contrôles, deux jours avant la détection et un préjudice équivalent à un pour cent des fonds propres. Les avoirs des clients et les systèmes des partenaires n'ont pas été touchés.

L'article sépare ensuite les hypothèses. Le rôle de l'IA est une conviction du président, sans élément technique publié, même si la BCE avait demandé en juillet aux banques un plan face aux menaces cyber liées à l'IA. L'origine des attaquants reste inconnue, et l'identité du prestataire n'est pas confirmée. Les deux montants qui circulent mesurent des choses différentes.

Quatre leçons sont tirées. La surface d'attaque passe par les identités des tiers : il faut inventorier les secrets détenus par les prestataires et les révoquer dès qu'un tiers est compromis. La vitesse des paiements dépasse les fenêtres de détection humaines : il faut des contrôles automatiques dans le flux, y compris sur les comptes propres, et l'IA peut servir en défense. La correction rapide des failles et la segmentation des systèmes limitent l'exposition. La communication de crise doit être rapide, même partielle, puisque l'information circule sur la blockchain.

L'article rappelle le cadre réglementaire, DORA, le règlement sur les virements instantanés et la transposition française de NIS2 en retard, et note que ce scénario n'avait pas été anticipé par les stress tests. Il conclut par six actions pour les DSI et RSSI, de la cartographie des secrets des tiers à l'exercice de crise.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | Cyber-casse chez Crédit Mutuel Arkéa | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| cyberattaque de Crédit Mutuel Arkéa | EVENEMENT | observé_dans | Crédit Mutuel Arkéa | ORGANISATION | 0.97 | STATIQUE | déclaré_article |
| cyberattaque de Crédit Mutuel Arkéa | EVENEMENT | mesure | environ 100 M€, 1 % des fonds propres | MESURE | 0.92 | STATIQUE | déclaré_article |
| cyberattaque de Crédit Mutuel Arkéa | EVENEMENT | utilise | virement instantané | TECHNOLOGIE | 0.9 | STATIQUE | déclaré_article |
| cyberattaque de Crédit Mutuel Arkéa | EVENEMENT | est_instance_de | attaque par prestataire | CONCEPT | 0.9 | STATIQUE | déclaré_article |
| Julien Carmona | PERSONNE | dirige | Crédit Mutuel Arkéa | ORGANISATION | 0.95 | DYNAMIQUE | déclaré_article |
| Julien Carmona | PERSONNE | affirme_que | l'attaque a très probablement été appuyée par des modèles IA de pointe | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| ZachXBT | PERSONNE | mesure | 133 M$ de retraits sur plateformes crypto | MESURE | 0.88 | STATIQUE | déclaré_article |
| Bitquery | ORGANISATION | mesure | 126 M$ sortis en 28 heures | MESURE | 0.88 | STATIQUE | déclaré_article |
| ZachXBT | PERSONNE | s_oppose_à | attribution de l'attaque au Lazarus Group | AFFIRMATION | 0.85 | STATIQUE | déclaré_article |
| Claudia Buch | PERSONNE | publie | lettre BCE SSM-2026-0301 | DOCUMENT | 0.93 | STATIQUE | déclaré_article |
| lettre BCE SSM-2026-0301 | DOCUMENT | recommande | accélérer la gestion des vulnérabilités et des correctifs, y compris logiciels tiers | AFFIRMATION | 0.9 | STATIQUE | déclaré_article |
| règlement (UE) 2024/886 | DOCUMENT | s_applique_à | virement instantané | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| Claude Mythos Preview | TECHNOLOGIE | réduit | virement frauduleux de 1,5 M$ bloqué dans une banque Glasswing | MESURE | 0.8 | STATIQUE | déclaré_article |
| règlement DORA | DOCUMENT | s_applique_à | risque tiers | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | inventorier et révoquer les identités non humaines détenues par les prestataires | AFFIRMATION | 0.92 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | recommande | plafonds, vélocité et mise en attente automatique sur les comptes propres | AFFIRMATION | 0.9 | ATEMPOREL | déclaré_article |
| segmentation des systèmes d'information | METHODOLOGIE | réduit | propagation de l'attaque aux filiales et partenaires | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| cyberattaque de Crédit Mutuel Arkéa | EVENEMENT | date | 1er-3 novembre 2026, ~100 M€, entrée par un prestataire | AJOUT |
| Crédit Mutuel Arkéa | ORGANISATION | secteur | Banque (Brest), filiale Fortuneo | AJOUT |
| Julien Carmona | PERSONNE | rôle | Président de Crédit Mutuel Arkéa | AJOUT |
| ZachXBT | PERSONNE | rôle | Enquêteur blockchain indépendant | AJOUT |
| Bitquery | ORGANISATION | secteur | Analyse on-chain | AJOUT |
| lettre BCE SSM-2026-0301 | DOCUMENT | contenu | « Addressing AI-enabled cybersecurity threats », 7 juillet 2026, plan d'action dû le 31 octobre 2026 | AJOUT |
| Claudia Buch | PERSONNE | rôle | Présidente du conseil de surveillance de la BCE | AJOUT |
| règlement DORA | DOCUMENT | application | Digital Operational Resilience Act, en vigueur depuis le 17 janvier 2025 | AJOUT |
| identités non humaines | CONCEPT | définition | Comptes de service, clés d'API, certificats, jetons OAuth détenus par des tiers | AJOUT |
