# law-ahrefs-content-engineering-claude-code-2026-04-28

## Veille
Billet du **blog Ahrefs** publié le **28 avril 2026** par **Ryan Law** (Director of Content Marketing, Ahrefs) décrivant un système de **content engineering** maison construit autour de **Claude Code** : un pipeline éditorial qui produit des **drafts prêts à publier en 6 à 12 minutes**. **Thèse-pivot** : ***« AI content is not, by default, good. This process works well because it mirrors our existing human editorial process »*** — la qualité ne vient pas du modèle mais de la **reproduction fidèle d'un processus éditorial humain** éprouvé sur des décennies. Architecture : **~23 skill files** correspondant chacun à une étape éditoriale (keyword research, topic gap analysis, structural outlining, research compilation, draft generation, formatting), **orchestrés par un skill principal `blog-pipeline`** qui les enchaîne pour produire un article complet. **Sept principes de conception** : (1) **mimer les workflows humains** en chaînant des skills adaptés de la documentation éditoriale Ahrefs existante ; (2) **sortir chaque étape séparément** pour le troubleshooting (*« if you get an article at the end of a ten minute run, and it's bad, it's hard to diagnose precisely where and why the process went wrong »* → sauvegarder les outputs intermédiaires) ; (3) **créer des cas de test** via le skill `skill-creator` d'Anthropic pour évaluer et améliorer les guidances ; (4) **brancher des sources de données de qualité** — le **Ahrefs MCP** (keyword metrics, parent topic, long-tail themes, SERP overviews, analyse concurrentielle), l'analyse concurrentielle et la doc produit ; (5) **front-loader la direction humaine** via des paramètres de contexte permettant le guidage éditorial ; (6) **construire des previews interactives** au format HTML pour la revue avant publication ; (7) **permettre la personnalisation** (chaque membre de l'équipe peut forker et modifier le système). **Volumétrie** : ~**15 articles publiés** et ~**30 articles mis à jour** via ce workflow ; développement démarré en **février 2026** (le processus antérieur d'**août 2025** demandait plusieurs jours et de l'intervention manuelle). **Caveats explicites** (anti-survente) : *« experience matters »* — le processus reflète des décennies d'expertise éditoriale ; la sélection de sujets se concentre sur du **contenu SEO informationnel** que l'auteur maîtrise bien ; Ahrefs **n'a aucun plan de "scaler" massivement le contenu** mais maintient une **bibliothèque evergreen**. Philosophie : automatiser *« the formulaic parts of work »* pour éliminer la corvée et libérer du temps pour la recherche, le thought leadership, les webinars et l'optimisation du système — **pas** remplacer l'effort humain. Référence canonique citée par Pasquale Pillitteri (*Opus 4.8 SEO workflow*) comme preuve terrain du gain « 6-12 min/draft ». Convergence directe avec la doctrine **skills-over-prompts** (Lattice, PROJ-AI), **systems around the model** (Dropbox/Okumura), et l'usage **HTML comme artefact de revue** (Shihipar).

## Titre Article
How I Do Content Engineering With Claude Code

## Date
2026-04-28

## URL
https://ahrefs.com/blog/how-i-do-content-engineering-with-claude-code/

## Keywords
content engineering, ingénierie de contenu, Claude Code, skill files, blog-pipeline, orchestration de skills, keyword research, topic gap analysis, structural outlining, research compilation, draft generation, formatting, draft prêt à publier en 6-12 minutes, 23 skill files, Ahrefs MCP, Model Context Protocol, parent topic, long-tail, SERP overview, analyse concurrentielle, skill-creator, cas de test, sauvegarde des outputs intermédiaires, troubleshooting de pipeline, front-loading direction humaine, preview HTML, fork et personnalisation, AI content is not by default good, mirror existing human editorial process, formulaic parts of work, bibliothèque evergreen, pas de scale massif, SEO informationnel, content marketing, workflow éditorial, automatisation éditoriale, Ryan Law, Ahrefs, systems around the model, skills over prompts

## Authors
**Ryan Law** — Director of Content Marketing chez **Ahrefs**. Praticien senior du content marketing SEO ; le billet est un retour d'expérience personnel (*« How I do… »*) publié sur le **blog Ahrefs** (ahrefs.com/blog) le **28 avril 2026**.

## Ton
**Profil** : Billet de praticien (*how-I-do* / retour d'expérience), première personne du singulier (*« I »*), à destination des content marketers, SEO managers et éditeurs curieux d'industrialiser leur production avec l'IA. Registre **pragmatique-pédagogique**, niveau technique **moyen** (assume une familiarité avec SEO, MCP, Claude Code, skills, mais explique chaque étape).

**Style** : Prose de démonstration structurée par principes numérotés et étapes de workflow. Logique d'**éditeur-ingénieur** : on pose une thèse contre-intuitive (l'IA ne produit pas du bon contenu par défaut), on l'illustre par une architecture concrète (23 skills + `blog-pipeline`), on chiffre le résultat (6-12 min/draft, 15 publiés / 30 mis à jour), puis on désamorce explicitement les attentes de scale (caveats). Honnêteté forte : insistance répétée sur le fait que le système **reproduit** une expertise humaine plutôt que de la remplacer.

**Aphorismes-clés** :
- ***« AI content is not, by default, good. This process works well because it mirrors our existing human editorial process. »*** (thèse centrale).
- ***« If you get an article at the end of a ten minute run, and it's bad, it's hard to diagnose precisely where and why the process went wrong. »*** (justification du save-intermediate-outputs).
- *« Experience matters. »* (caveat anti-survente).

**Métaphores / cadres travaillés** :
- ***Content engineering*** — le contenu éditorial traité comme une chaîne de fabrication décomposée en étapes outillées et testables, et non comme un acte créatif monolithique.
- ***Mirror the human editorial process*** — le pipeline IA comme miroir d'un workflow humain existant : la qualité est portée par le processus, pas par le modèle.
- ***Save every step*** — l'observabilité du pipeline (outputs intermédiaires) comme condition du debugging, par analogie avec les logs d'un système logiciel.

**Position épistémique** : retour d'expérience d'opérateur (Ahrefs, éditeur SEO de référence) appuyé sur des chiffres modestes et vérifiables (15 + 30 articles), avec des **caveats explicites** qui renforcent la crédibilité (pas de promesse de scale massif, reconnaissance que l'expérience humaine reste le socle). Source promotionnelle (Ahrefs vend le MCP utilisé) mais cadrage prudent et reproductible.

**Autorité** : (a) **marque** Ahrefs (outil SEO de référence, donc légitimité métier) ; (b) **fonction** de Ryan Law (Director of Content Marketing) ; (c) **honnêteté** des limites (expérience requise, pas de scale) ; (d) **reproductibilité** (système forkable, étapes documentées) — devient la **référence terrain** citée par les workflows SEO 2026 (Pillitteri).

## Pense-betes

- **Date / source** : **28 avril 2026**, **blog Ahrefs** (ahrefs.com/blog). Auteur : **Ryan Law** (Director of Content Marketing, Ahrefs).
- **Thèse centrale (à retenir mot pour mot)** : ***« AI content is not, by default, good. This process works well because it mirrors our existing human editorial process. »***

### L'architecture du pipeline

- **~23 skill files**, un par étape éditoriale : keyword research, topic gap analysis, structural outlining, research compilation, draft generation, formatting.
- Orchestration par un skill maître **`blog-pipeline`** qui séquence les autres → article complet.
- **Ahrefs MCP** = source de vérité SEO live (keyword metrics, parent topic, long-tail, SERP overview, intent, analyse concurrentielle) au lieu d'hallucinations.

### Les 7 principes de conception

1. **Mimer les workflows humains** (skills adaptés de la doc éditoriale Ahrefs existante).
2. **Sortir chaque étape séparément** → troubleshooting (sauver les outputs intermédiaires).
3. **Créer des cas de test** via le `skill-creator` d'Anthropic.
4. **Brancher des sources de qualité** (Ahrefs MCP, concurrents, doc produit).
5. **Front-loader la direction humaine** (paramètres de contexte).
6. **Previews interactives en HTML** pour la revue avant publication.
7. **Forkable / personnalisable** par chaque membre de l'équipe.

### Chiffres & caveats

- **6 à 12 minutes** pour un draft prêt à publier (chiffre canonique repris partout).
- **~15 articles publiés**, **~30 mis à jour**. Dev démarré **février 2026** ; process antérieur (**août 2025**) = plusieurs jours + intervention manuelle.
- **Caveats explicites** : *« experience matters »* ; sujets = **SEO informationnel** maîtrisé ; **pas de plan de scale massif** → bibliothèque **evergreen**.
- Philosophie : automatiser *« the formulaic parts of work »* (corvée) → libérer du temps pour recherche / thought leadership / webinars / optimisation du système.

### À mobiliser en mission / présentation

- **Proof-point terrain** du gain de cycle éditorial : 6-12 min/draft, ancré sur des données live (MCP), avec garde-fou humain.
- Illustration directe de la doctrine **skills-over-prompts** + **systems around the model** (l'avantage = le pipeline orchestré, pas le modèle brut) — recoupe Lattice, PROJ-AI, Dropbox/Okumura.
- L'idée **save-every-step** = observabilité de pipeline agentique réutilisable comme pattern (cf. decision traces / debugging d'agents).

## RésuméDe400mots

Ryan Law, Director of Content Marketing chez Ahrefs, décrit dans ce billet du **28 avril 2026** le système de **content engineering** qu'il a construit autour de **Claude Code** pour produire des drafts d'articles prêts à publier en **6 à 12 minutes**. Sa thèse fondatrice désamorce d'emblée l'enthousiasme : *« AI content is not, by default, good. This process works well because it mirrors our existing human editorial process »*. Autrement dit, la qualité ne vient pas du modèle mais de la **reproduction fidèle d'un processus éditorial humain** déjà rodé.

Le système repose sur **environ 23 skill files**, chacun correspondant à une étape éditoriale précise : keyword research, topic gap analysis, structural outlining, research compilation, draft generation, formatting. Un skill maître, **`blog-pipeline`**, les enchaîne pour produire un article complet. Au cœur du dispositif, le **Ahrefs MCP** permet à Claude de tirer des **données SEO réelles** (keyword metrics, parent topic, thèmes long-tail, SERP overviews, intention de recherche, analyse concurrentielle) plutôt que d'inventer des chiffres.

Law dégage sept principes de conception : mimer les workflows humains existants ; sortir chaque étape séparément pour le troubleshooting (*« if you get an article at the end of a ten minute run, and it's bad, it's hard to diagnose precisely where and why the process went wrong »*) ; créer des cas de test via le `skill-creator` d'Anthropic ; brancher des sources de données de qualité ; front-loader la direction humaine via des paramètres de contexte ; construire des previews HTML interactives pour la revue ; et rendre le système forkable et personnalisable par chaque membre de l'équipe.

Les chiffres restent volontairement modestes : **~15 articles publiés** et **~30 mis à jour**, avec un développement démarré en **février 2026** (le processus antérieur, d'août 2025, demandait plusieurs jours et de l'intervention manuelle). Law assortit le tout de **caveats explicites** qui renforcent sa crédibilité : *« experience matters »* (le processus reflète des décennies d'expertise), la sélection de sujets se limite au **contenu SEO informationnel** bien maîtrisé, et Ahrefs **n'a aucun plan de scaler massivement** — il maintient une bibliothèque **evergreen**.

La philosophie d'ensemble est de n'automatiser que *« the formulaic parts of work »* — la corvée formulaïque — pour libérer du temps en faveur de la recherche, du thought leadership, des webinars et de l'optimisation du système, sans remplacer l'effort humain. Ce billet est devenu la **référence terrain** citée par les workflows SEO 2026 (notamment Pasquale Pillitteri), illustration concrète de la doctrine *skills-over-prompts* et *systems around the model* : l'avantage vient du pipeline orchestré, pas du modèle brut.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| Ryan Law | PERSONNE | travaille_chez | Ahrefs | ORGANISATION | 0.97 | DYNAMIQUE | déclaré_article |
| Ryan Law | PERSONNE | a_créé | pipeline de content engineering | METHODOLOGIE | 0.96 | STATIQUE | déclaré_article |
| pipeline de content engineering | METHODOLOGIE | est_basé_sur | Claude Code | TECHNOLOGIE | 0.96 | STATIQUE | déclaré_article |
| pipeline de content engineering | METHODOLOGIE | utilise | ~23 skill files | TECHNOLOGIE | 0.95 | STATIQUE | déclaré_article |
| blog-pipeline | TECHNOLOGIE | orchestre | les skill files éditoriaux | TECHNOLOGIE | 0.94 | STATIQUE | déclaré_article |
| pipeline de content engineering | METHODOLOGIE | produit | draft prêt à publier en 6-12 min | CONCEPT | 0.94 | STATIQUE | déclaré_article |
| pipeline de content engineering | METHODOLOGIE | interroge | Ahrefs MCP | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| Ahrefs MCP | TECHNOLOGIE | fournit | keyword data / parent topic / SERP overview | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| Ryan Law | PERSONNE | affirme_que | l'IA ne produit pas du bon contenu par défaut | CONCEPT | 0.95 | ATEMPOREL | déclaré_article |
| qualité du contenu IA | CONCEPT | provient_de | la reproduction du processus éditorial humain | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| sauvegarde des outputs intermédiaires | METHODOLOGIE | permet | le troubleshooting du pipeline | CONCEPT | 0.9 | ATEMPOREL | déclaré_article |
| skill-creator d'Anthropic | TECHNOLOGIE | génère | des cas de test pour les skills | CONCEPT | 0.88 | STATIQUE | déclaré_article |
| pipeline de content engineering | METHODOLOGIE | a_produit | ~15 articles publiés + ~30 mis à jour | CONCEPT | 0.92 | STATIQUE | déclaré_article |
| Ahrefs | ORGANISATION | refuse | de scaler massivement le contenu | CONCEPT | 0.9 | DYNAMIQUE | déclaré_article |
| previews HTML | TECHNOLOGIE | servent | la revue humaine avant publication | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| Ryan Law | PERSONNE | rôle | Director of Content Marketing, Ahrefs | AJOUT |
| Ahrefs | ORGANISATION | secteur | SEO / content marketing (outil de référence) | AJOUT |
| Claude Code | TECHNOLOGIE | catégorie | Agent de codage CLI (Anthropic) | AJOUT |
| blog-pipeline | TECHNOLOGIE | catégorie | Skill maître d'orchestration éditoriale | AJOUT |
| skill files | TECHNOLOGIE | quantité | ~23, un par étape éditoriale | AJOUT |
| Ahrefs MCP | TECHNOLOGIE | catégorie | Serveur MCP fournissant les données SEO live | AJOUT |
| content engineering | METHODOLOGIE | définition | Industrialisation du process éditorial via skills + MCP | AJOUT |
| draft prêt à publier | CONCEPT | métrique | 6 à 12 minutes par article | AJOUT |
| volumétrie | CONCEPT | valeur | ~15 publiés + ~30 mis à jour (dev démarré fév. 2026) | AJOUT |
| caveats | CONCEPT | contenu | experience matters ; SEO informationnel ; pas de scale massif | AJOUT |
