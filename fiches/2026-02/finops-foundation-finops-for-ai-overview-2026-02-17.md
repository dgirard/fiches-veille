# finops-foundation-finops-for-ai-overview-2026-02-17

## Veille
Guide officiel FinOps Foundation pour l'IA : token economics, KPIs, caching, prompt optimization, sélection de modèle et extension des 14 capacités du Framework FinOps aux services GenAI - FinOps Foundation

## Titre Article
FinOps for AI Overview

## Date
2026-02-17

## URL
https://www.finops.org/wg/finops-for-ai-overview/

## Keywords
FinOps Foundation, token economics, cost per token, cost per inference, optimisation LLM, caching, prompt engineering, sélection de modèle, MMLU, Crawl Walk Run, KPIs FinOps IA, showback, unit economics, ROI IA, certification FinOps for AI

## Authors
FinOps Foundation — groupe de travail (Brent Eubanks/Wayfair, James Barney/MetLife, Eric Lam/Google, Adam Richter/AWS, Rahul Kalva/Wells Fargo, JJ Sharma/KPMG, Karl Hayberg/EY, et al.)

## Ton
**Profil** : Perspective d'organisme de standardisation (groupe de travail multi-entreprises), registre normatif et exhaustif, niveau praticien FinOps confirmé

**Description** : Document de référence collectif, co-écrit par un large groupe de travail représentant des entreprises majeures (Google, AWS, MetLife, Wells Fargo, Roche, Accenture, KPMG, EY…). Le ton est celui d'un standard sous licence CC BY 4.0 : neutre, structuré, vendor-agnostic, visant l'exhaustivité plutôt que la thèse. Chaque KPI est donné avec sa formule et un exemple chiffré ; chacune des 14 capacités du Framework FinOps est passée au crible « commun au cloud / différent pour l'IA ». La progressivité est encadrée par un modèle de maturité Crawl-Walk-Run. Le public cible : praticiens FinOps en poste, équipes Finance/Engineering/Data, et candidats à la certification *Certified FinOps for AI*.

## Pense-betes
- **Token = unité fondamentale** de consommation des API LLM ; *« the meters, or elements of charge can be very different »* des métriques cloud classiques (écart entre tokens d'input utilisateur et tokens sémantiques facturés).
- **KPIs avec formules et exemples** :
  - **Cost Per Token** = Coût total / Tokens utilisés (ex : 2 500 $ / 1 M = 0,0025 $).
  - **Cost Per Inference** = Coûts inférence / Nb requêtes (ex : 5 000 $ / 100 000 = 0,05 $).
  - **Training Cost Efficiency** = Coût entraînement / métrique perf (ex : 10 000 $ / 95% = 105 $ par point).
  - **ROI** = (Bénéfices − Coûts) / Coûts × 100 (ex : 150%).
  - **LLM Model Choice Quality Score Alignment** : compare le MMLU minimal requis au MMLU du modèle utilisé → repère le gaspillage (ex : une analyse de sentiment exigeant MMLU 54 ne doit pas tourner sur GPT-4).
- **Optimisation tokens** : raccourcir les prompts en gardant la clarté ; **caching** des réponses répétées ; *« avoid using the most complex and expensive models for every task »* ; **model distillation** (versions plus petites de GPT-4/Claude pour la prod).
- **14 capacités du Framework FinOps** revisitées pour l'IA — les plus différenciées : Data Ingestion, **Allocation** (traçabilité des *multi-agent workloads*, absence de framework standard), Planning & Estimating (estimer les outputs réussis vs hallucinations), Forecasting (prédictibilité plus faible en Crawl/Walk), Budgeting, Benchmarking (per-token, peu de benchmarks externes), Unit Economics (cost-per-call, customer satisfaction per dollar), Rate Optimization (OpenAI Scale Tier), Cloud Sustainability (impact environnemental par requête).
- **Modèle de maturité Crawl → Walk → Run** : Crawl = prototypage *fail fast*, calculs manuels ; Walk = automatisation basique du tracking + anomalies ; Run = tracking & anomalies avancés, métriques financières intégrées, ne pas couper les coûts qui compromettent les exigences non-fonctionnelles.
- **8 modèles de pricing** : on-demand, reserved/CUD, provisioned capacity (OpenAI Scale Tier, Azure PTU), spot/batch, subscription, tiered, free/freemium, hybrid.
- **Showback** privilégié (visibilité sans facturation immédiate) comme outil de prise de conscience avant le chargeback.
- **Outils cités** : Langfuse, Langsmith, Prometheus, Grafana, OTEL ; natifs AWS/GCP/Azure (Bedrock, Vertex AI, Azure OpenAI) ; frameworks d'optimisation GGUF/ONNX/OpenVINO/TensorRT ; vector DBs (Kendra, OpenSearch, pgvector, Cosmos DB).
- **Note** : le document ne traite pas encore les **agents IA** comme catégorie distincte (seuls les *multi-agent workloads* sont évoqués sous Allocation) — d'où la valeur des compléments éditeurs (Finout, Orq.ai).
- **Écosystème** : certification *Certified FinOps for AI* ; conférence **FinOps X 2026** (8-11 juin, San Diego) ; licence CC BY 4.0.
- **Lien veille** : socle doctrinal officiel du cluster FinOps agentique — fondation que prolongent [[finout-finops-ai-agents-four-step-allocation-framework-2026-04-27]] (allocation), [[finout-cpo-guide-llm-rag-agents-agentic-token-multipliers-2025-11-02]] (multiplicateurs de tokens), [[orq-ai-finops-ai-agents-cost-per-outcome-hosseini-2026-04-15]] (cost per outcome). Recoupe Gupta (cost-per-token, marginal token utility) et le slot **Optimisation des coûts**.

## RésuméDe400mots
*FinOps for AI Overview* est le guide de référence de la FinOps Foundation, co-rédigé par un large groupe de travail (Google, AWS, MetLife, Wells Fargo, Roche, Accenture, KPMG, EY…) et publié sous licence CC BY 4.0. Il étend la discipline FinOps aux services d'IA générative en partant du token comme unité fondamentale de consommation, dont les « compteurs » diffèrent profondément des métriques cloud classiques.

Le document fournit une batterie de **KPIs avec formules et exemples chiffrés** : Cost Per Token (coût total / tokens), Cost Per Inference (coûts d'inférence / requêtes, ex : 0,05 $), Training Cost Efficiency (coût / point de précision), ROI ((bénéfices − coûts)/coûts × 100), et surtout le *LLM Model Choice Quality Score Alignment*, qui compare le score MMLU minimal requis par une tâche au MMLU du modèle réellement utilisé pour détecter le sur-dimensionnement (une analyse de sentiment à MMLU 54 ne devrait pas tourner sur GPT-4).

Côté **optimisation**, l'accent porte sur la réduction de tokens (raccourcir les prompts en gardant la clarté), le **caching** des réponses répétées, la **sélection de modèle** (*« éviter d'utiliser les modèles les plus complexes et chers pour chaque tâche »*) et la **model distillation** pour la production.

Le cœur structurel mappe les **14 capacités du Framework FinOps** sur le « commun au cloud » versus le « différent pour l'IA ». Les plus impactées : l'**Allocation** (traçabilité des *multi-agent workloads*, absence de framework standard), le Planning (estimer les outputs réussis et les séparer des hallucinations), le Forecasting (prédictibilité moindre en phases initiales), le Benchmarking (métriques per-token, rares benchmarks externes), les Unit Economics (cost-per-call, satisfaction client par dollar) et la Rate Optimization (pricing volatil type OpenAI Scale Tier).

La montée en maturité suit un modèle **Crawl → Walk → Run** : prototypage *fail fast* et calculs manuels au début ; automatisation basique du tracking et détection d'anomalies ensuite ; tracking avancé, métriques financières intégrées et vigilance à ne pas couper des coûts compromettant les exigences non-fonctionnelles en phase Run. Le document recense **huit modèles de pricing** (on-demand, reserved/CUD, provisioned — OpenAI Scale Tier, Azure PTU —, spot/batch, subscription, tiered, freemium, hybride) et privilégie le **showback** comme levier de prise de conscience avant le chargeback.

Limite notable : les **agents IA** ne sont pas encore traités comme catégorie distincte (seuls les *multi-agent workloads* affleurent sous l'Allocation), ce qui justifie les compléments d'éditeurs. Le guide s'accompagne d'une certification *Certified FinOps for AI* et renvoie à FinOps X 2026 (juin, San Diego).

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| FinOps Foundation | ORGANISATION | publie | FinOps for AI Overview | DOCUMENT | 0.98 | STATIQUE | déclaré_article |
| FinOps for AI Overview | DOCUMENT | étend | Framework FinOps aux services GenAI | METHODOLOGIE | 0.97 | ATEMPOREL | déclaré_article |
| token | CONCEPT | est | unité fondamentale de consommation LLM | CONCEPT | 0.97 | ATEMPOREL | déclaré_article |
| Cost Per Token | CONCEPT | est_défini_par | Coût total / tokens utilisés | CONCEPT | 0.96 | ATEMPOREL | déclaré_article |
| sélection de modèle | CONCEPT | réduit | coûts inutiles | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| MMLU | CONCEPT | sert_à | aligner capacité modèle et besoin tâche | CONCEPT | 0.92 | ATEMPOREL | déclaré_article |
| caching | METHODOLOGIE | réduit | consommation de tokens | CONCEPT | 0.93 | ATEMPOREL | déclaré_article |
| prompt engineering concis | METHODOLOGIE | réduit | tokens (15-25%) | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| Framework FinOps | METHODOLOGIE | comporte | 14 capacités revisitées pour l'IA | CONCEPT | 0.95 | STATIQUE | déclaré_article |
| modèle Crawl-Walk-Run | METHODOLOGIE | structure | maturité FinOps IA | CONCEPT | 0.94 | ATEMPOREL | déclaré_article |
| Allocation | CONCEPT | est_compliquée_par | multi-agent workloads | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| showback | METHODOLOGIE | favorise | prise de conscience des coûts | CONCEPT | 0.90 | ATEMPOREL | déclaré_article |
| FinOps Foundation | ORGANISATION | propose | certification Certified FinOps for AI | EVENEMENT | 0.92 | STATIQUE | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| FinOps for AI Overview | DOCUMENT | type | Guide de référence officiel (CC BY 4.0) | AJOUT |
| FinOps Foundation | ORGANISATION | secteur | Standardisation FinOps / Linux Foundation | AJOUT |
| token economics | CONCEPT | KPIs | Cost Per Token, Cost Per Inference, Training Cost Efficiency, ROI | AJOUT |
| MMLU | CONCEPT | usage | Benchmark d'alignement qualité-coût des modèles | AJOUT |
| modèle Crawl-Walk-Run | METHODOLOGIE | phases | Crawl (fail fast) → Walk (automation) → Run (intégré) | AJOUT |
| Framework FinOps | METHODOLOGIE | capacités | 14 capacités contrastées cloud vs IA | AJOUT |
| FinOps X 2026 | EVENEMENT | date | 8-11 juin 2026, San Diego | AJOUT |
