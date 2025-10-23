# gemini-cli-tos-privacy-google-2025-04-17

## Veille
Gemini CLI - Terms of Service - Privacy - Google - Data collection - Model training - Authentication

## Titre Article
Gemini CLI: Terms of Service and Privacy Notice

## Date
2025-04-17

## URL
https://github.com/google-gemini/gemini-cli/blob/main/docs/tos-privacy.md

## Keywords
Gemini CLI, Terms of Service, Privacy Notice, Google, Google Cloud, Gemini Code Assist, Gemini Developer API, Vertex AI GenAI API, data collection, model training, usage statistics, opt-out, authentication, API key

## Authors
Google / Gemini team

## Pense-betes
- **ToS/Privacy varient** selon méthode authentication et type de compte
- **4 méthodes d'authentication** : Google account avec Code Assist Individuals, Standard/Enterprise, Gemini API key avec Developer API, Vertex AI GenAI API
- **Individuals + API unpaid** : prompts/answers/code **collectés et utilisés** pour training
- **Standard/Enterprise + API paid + Vertex AI** : prompts/answers/code **NOT collected**, traités confidentiellement
- **Usage Statistics** : contrôle unique pour data collection optionnelle, scope varie selon type compte
- **Opt-out disponible** : possibilité de refuser Usage Statistics
- **Confidentialité différenciée** : gratuit = données collectées, payant/entreprise = confidentialité garantie

## RésuméDe400mots

La documentation Terms of Service et Privacy Notice du Gemini CLI (Command-Line Interface) révèle une structure complexe et hautement différenciée de politiques de confidentialité et d'utilisation des données, dépendant critiquement de la méthode d'authentification et du type de compte utilisé. Ce document est crucial car il détermine si les prompts, réponses et code associé de l'utilisateur seront collectés et potentiellement utilisés pour entraînement de modèles.

**Quatre Scénarios d'Authentification Distincts**

**Scénario 1 : Google account + Gemini Code Assist for Individuals**
Les utilisateurs sont soumis aux Google Terms of Service généraux et à une Privacy Notice spécifique Code Assist Individuals. Sous cet arrangement, **prompts, réponses et code associé sont collectés et peuvent être utilisés** pour améliorer les produits Google, incluant purposes de model training.

**Scénario 2 : Google account + Gemini Code Assist for Standard/Enterprise Users**
Application des Google Cloud Platform Terms of Service et Privacy Notice distinct pour Standard/Enterprise. **Crucially**, pour ces utilisateurs, **prompts, réponses et code sont traités comme confidentiels, ne sont pas collectés, et explicitement non utilisés** pour model training.

**Scénario 3 : Gemini API key + Gemini Developer API**
Les termes diffèrent selon service unpaid vs paid. Services **unpaid** : Gemini API Terms of Service for Unpaid Services s'appliquent, **permettant collection** de prompts/answers/code pour model improvement. Services **paid** : Gemini API Terms of Service for Paid Services gouvernent, **traitant inputs comme confidentiels** et prévenant collection pour model training.

**Scénario 4 : Gemini API key + Vertex AI GenAI API**
Soumis aux Google Cloud Platform Service Terms et Google Cloud Privacy Notice. Dans ce scénario, **prompts, réponses et code sont considérés confidentiels, ne sont pas collectés, et ne sont pas utilisés** pour model training.

**Usage Statistics : Contrôle Unifié, Scope Variable**

Le document adresse également "Usage Statistics", servant de contrôle unique pour toute data collection optionnelle dans Gemini CLI. Le scope des données collectées via ce paramètre **varie selon type de compte**. Pour individual Code Assist users et unpaid Developer API users, activer Usage Statistics **permet collection de telemetry anonyme PLUS prompts/answers/code** pour model improvement. Pour Standard/Enterprise Code Assist users et Vertex AI GenAI API users, ce paramètre contrôle **uniquement anonymous telemetry**, car leurs prompts et code ne sont jamais collectés. Paid Developer API users voient leurs prompts/responses **logged pour limited time** solely pour policy violation detection. **Tous les utilisateurs peuvent opt-out** de Usage Statistics collection.

Cette structure documentaire met en évidence une stratégie de monétisation claire : les services gratuits financent leur coût opérationnel via data collection pour model improvement, tandis que les services payants et entreprise garantissent confidentialité complète comme value proposition premium.
