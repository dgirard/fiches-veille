# voxtral-mistral-ai-speech-understanding-2025-07-15

## Veille
Voxtral — modèles open source de compréhension vocale de Mistral AI : transcription multilingue, Q&A audio, licence Apache 2.0 (mistral.ai)

## Titre Article
Voxtral | Mistral AI

## Date
2025-07-15

## URL
https://mistral.ai/news/voxtral

## Keywords
Voxtral, Mistral AI, compréhension vocale, open source, reconnaissance vocale, modèles de langage, transcription, multilingue, Q&A, résumé automatique, function-calling, IA, interface vocale, Apache 2.0, modèle 24B, Mini 3B

## Authors
Mistral AI

## Ton
**Profil :** Lancement produit technique | Institutionnel | Informatif-Promotionnel | Expert

Mistral AI adopte une voix d'annonce produit positionnant Voxtral comme une sortie open source majeure dans les modèles vocaux. L'accent sur la licence Apache 2.0 et les capacités multilingues s'adresse à la communauté open source. Le langage technique précis (modèle 24B, Mini 3B, function-calling, Q&A) démontre l'étendue des capacités. Le ton confiant et professionnel est typique d'une startup IA européenne se positionnant face à OpenAI/Google. La structure centrée capacités, avec détails de disponibilité, facilite l'adoption par les développeurs. Typique des lancements produits des laboratoires d'IA (style Anthropic, Cohere) visant une communauté de développeurs attachée à l'open source avec des capacités de niveau commercial.

## Pense-betes
- **2 tailles** : variante 24B (production), Mini 3B (local/edge), sous **licence Apache 2.0**
- **API accessible** + téléchargement open source
- **Comble le fossé** entre ASR open source à fort taux d'erreur et APIs propriétaires coûteuses
- **Précision état de l'art** + compréhension sémantique native à **moins de la moitié du prix** des solutions propriétaires
- **Contexte long** : jusqu'à **30-40 minutes d'audio** (30 min transcription, 40 min compréhension)
- **Q&A et résumé intégrés** : interrogation directe de l'audio sans chaîner ASR + LLM
- **Multilingue natif** : détection automatique de langue, **8+ langues** (anglais, espagnol, français, portugais, hindi, allemand, néerlandais, italien)
- **Function-calling depuis la voix** : intentions orales → commandes système actionnables
- **Voxtral Mini Transcribe** : **moins de la moitié du prix d'OpenAI Whisper**, et le surpasse
- **Voxtral Small égale ElevenLabs Scribe** pour **moins de la moitié du prix**
- **Benchmarks** : surpasse Whisper large-v3, compétitif avec GPT-4o mini Transcribe et Gemini 2.5 Flash
- **Roadmap** : segmentation des locuteurs, annotations audio (âge, émotion), timestamps au mot, reconnaissance audio non vocale

## RésuméDe400mots

Mistral AI dévoile **Voxtral**, une suite novatrice de modèles open source de compréhension vocale conçue pour révolutionner l'interaction humain-machine par la voix. Considérant la voix comme l'interface originelle de l'humanité, Voxtral vise à dépasser les limites des systèmes actuels, peu fiables ou propriétaires, en offrant des outils vocaux robustes, multilingues et profondément intelligents. Les modèles sont disponibles en **deux versions** : une variante 24B taillée pour les applications à l'échelle de la production, et une variante plus compacte de 3B, **Voxtral Mini**, adaptée aux déploiements locaux et en périphérie (edge). Les deux sont publiées sous la **licence permissive Apache 2.0** et accessibles via l'API de Mistral AI, avec **Voxtral Mini Transcribe**, optimisé pour la transcription, offrant une efficacité coût/latence inégalée.

**Architecture à deux niveaux et avantage de coût**

Voxtral se distingue en comblant le fossé entre les systèmes ASR open source à fort taux d'erreur et les APIs propriétaires coûteuses. Il offre une **précision état de l'art et une compréhension sémantique native** dans un cadre ouvert, à **moins de la moitié du prix** des solutions propriétaires comparables. Cette efficacité de coût rend l'intelligence vocale de haute qualité accessible et contrôlable à grande échelle pour un large éventail d'applications.

**Capacités avancées au-delà de la transcription**

Les modèles offrent plusieurs capacités avancées au-delà de la simple transcription. Ils supportent des **contextes audio longs**, jusqu'à **30 minutes pour la transcription et 40 minutes pour la compréhension**, permettant le traitement complet de conversations ou d'enregistrements étendus. Fonctionnalité marquante : le **Q&A et le résumé intégrés**, qui permettent d'interroger directement le contenu audio ou de générer des résumés structurés **sans chaîner des modèles ASR et de langage séparés**. Voxtral est nativement multilingue, avec détection automatique de langue et performances état de l'art sur de nombreuses langues largement utilisées : **anglais, espagnol, français, portugais, hindi, allemand, néerlandais, italien**. Il permet en outre le **function-calling directement depuis la voix**, traduisant les intentions orales de l'utilisateur en commandes système actionnables. Les modèles conservent les solides capacités de compréhension textuelle de leur socle, le modèle de langage Mistral Small 3.1.

**Benchmarks compétitifs**

Les résultats de benchmark soulignent la performance supérieure de Voxtral. Il **surpasse globalement Whisper large-v3**, le modèle de transcription open source de référence, et dépasse GPT-4o mini Transcribe et Gemini 2.5 Flash sur diverses tâches. **Voxtral Small atteint l'état de l'art** sur l'anglais court et Mozilla Common Voice, démontrant de fortes capacités multilingues, et **égale ElevenLabs Scribe** pour les cas d'usage premium à un coût nettement réduit. **Voxtral Mini Transcribe surpasse OpenAI Whisper à moins de la moitié du prix**.

**Roadmap et vision**

Mistral AI prévoit d'introduire **segmentation des locuteurs, annotations audio (âge, émotion), timestamps au niveau du mot et reconnaissance d'audio non vocal**. L'entreprise étoffe son équipe audio et encourage les développeurs à intégrer Voxtral via téléchargement local sur Hugging Face, via l'API, ou en l'essayant dans le mode vocal de Le Chat, avec des fonctionnalités entreprise avancées : déploiement privé, fine-tuning spécifique au domaine et support d'intégration dédié.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Mistral AI | ORGANISATION | publie | Voxtral | TECHNOLOGIE | 0.99 | STATIQUE | déclaré_article |
| Voxtral | TECHNOLOGIE | est_basé_sur | Mistral Small 3.1 | TECHNOLOGIE | 0.97 | STATIQUE | déclaré_article |
| Voxtral | TECHNOLOGIE | utilise | licence Apache 2.0 | CONCEPT | 0.99 | STATIQUE | déclaré_article |
| Voxtral Small | TECHNOLOGIE | surpasse | Whisper large-v3 | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| Voxtral Small | TECHNOLOGIE | surpasse | GPT-4o mini Transcribe | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Voxtral Small | TECHNOLOGIE | surpasse | Gemini 2.5 Flash | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| Voxtral Small | TECHNOLOGIE | concurrence | ElevenLabs Scribe | TECHNOLOGIE | 0.93 | STATIQUE | déclaré_article |
| Voxtral Mini Transcribe | TECHNOLOGIE | surpasse | OpenAI Whisper | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| Voxtral | TECHNOLOGIE | permet | function-calling depuis la voix | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Voxtral | TECHNOLOGIE | permet | Q&A et résumé audio intégrés | CONCEPT | 0.97 | STATIQUE | déclaré_article |
| Voxtral | TECHNOLOGIE | observé_dans | Hugging Face | TECHNOLOGIE | 0.96 | DYNAMIQUE | déclaré_article |
| Le Chat | TECHNOLOGIE | utilise | Voxtral | TECHNOLOGIE | 0.95 | DYNAMIQUE | déclaré_article |
| Mistral AI | ORGANISATION | collabore_avec | Inworld | ORGANISATION | 0.88 | DYNAMIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Voxtral | TECHNOLOGIE | catégorie | Modèle de compréhension vocale open source | AJOUT |
| Voxtral | TECHNOLOGIE | variantes | Small (24B) et Mini (3B) | AJOUT |
| Voxtral | TECHNOLOGIE | licence | Apache 2.0 | AJOUT |
| Voxtral | TECHNOLOGIE | contexte audio maximal | 30 min (transcription), 40 min (compréhension) | AJOUT |
| Voxtral | TECHNOLOGIE | langues supportées | Anglais, espagnol, français, portugais, hindi, allemand, néerlandais, italien | AJOUT |
| Mistral Small 3.1 | TECHNOLOGIE | catégorie | Modèle de langage backbone | AJOUT |
| Mistral AI | ORGANISATION | secteur | IA / Open source | AJOUT |
| Le Chat | TECHNOLOGIE | catégorie | Assistant IA Mistral AI | AJOUT |
| Hugging Face | TECHNOLOGIE | catégorie | Plateforme de distribution de modèles | AJOUT |
| Whisper large-v3 | TECHNOLOGIE | catégorie | Modèle ASR open source (OpenAI) | AJOUT |
| ElevenLabs Scribe | TECHNOLOGIE | catégorie | Modèle de transcription propriétaire | AJOUT |
| Inworld | ORGANISATION | secteur | IA vocale / TTS | AJOUT |
