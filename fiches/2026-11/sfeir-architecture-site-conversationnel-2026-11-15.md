---
themes: [architecture-construction, outils-plateformes, qualite-securite]
source: SFEIR
---
# sfeir-architecture-site-conversationnel-2026-11-15

## Veille

Article éditorial **SFEIR AI** publié sur sfeir.com le **15 novembre 2026**, troisième volet de la série sur le site conversationnel de sfeir.com. Il décrit l'architecture en production : un site **Astro** statique (**1 626 URL**) servi par **Cloudflare Pages**, et un **Worker** sans adresse publique joint par liaison de service. **(1)** L'export de build : catalogue de **1 096 pages citables**, **7 132 passages**, lexique, empreinte de version. **(2)** Le chemin d'une question en six étapes : contrôles (Turnstile, quota sur empreinte d'IP salée), recherche hybride **bge-m3** + mots fusionnée par **RRF** (24 candidates), décision par **Clef-flash** (une intention sur sept, ≤ 1,8 s), colonne composée **par des règles écrites, sans modèle** (≤ 2,7 s), rédaction par **Llama 3.3 70B** (≤ 120 mots, température 0,2, premier mot ≤ 5 s), relances calculées sans modèle. **(3)** Un déploiement à deux portes de santé, justifié par un délai d'environ 90 secondes entre écriture et lecture dans Vectorize. Le principe : *« un seul modèle écrit, et seulement à la fin »*. L'article liste ce que l'architecture ne fait pas : hors corpus, mémoire de trois échanges, lenteur du premier fragment, aucune personnalisation.

## Titre Article

Architecture d'un site conversationnel : ce qui se passe entre la question et la réponse

## Date

2026-11-15

## URL

https://www.sfeir.com/articles/architecture-site-conversationnel/

## Keywords

architecture, site conversationnel, RAG, recherche hybride, Reciprocal Rank Fusion, RRF, bge-m3, Workers AI, Cloudflare Vectorize, Cloudflare Pages, Worker, liaison de service, Turnstile, Llama 3.3 70B, Clef-flash, classification d'intention, colonne par règles, cache KV, Durable Object, Analytics Engine, portes de santé, retour arrière, Astro, injection de prompt, SFEIR

## Authors

SFEIR AI, signature éditoriale collective de SFEIR, sur sfeir.com (site éditorial du cabinet).

## Ton

**Profil** : article d'architecture de production, écrit par le cabinet sur son propre système. Public déclaré : CTO et architectes, secondairement RSSI et DSI.

**Style** : technique et séquentiel, numéroté étape par étape, avec délais maximaux chiffrés à chaque étage et deux figures (chemin d'une question, topologie de production). Les consignes du modèle de rédaction sont restituées presque mot pour mot. Un exemple de correction concret par règle (« assurance qualité » qui ouvrait la page du secteur assurance, rangé parmi les faux amis).

**Position épistémique** : les choix sont justifiés par leurs contreparties (« le revers : chaque cas que la colonne traite mal demande une règle de plus »). Une section « ce que cette architecture ne fait pas » précède les conseils par rôle. Trois sources externes : l'article RRF de SIGIR 2009 et deux pages de documentation Cloudflare consultées le 14 novembre 2026. Le RSSI est averti que le risque d'injection est contenu, pas supprimé.

## Pense-betes

- **Socle statique** : Astro génère les pages au build, Cloudflare Pages les sert ; aucun serveur d'application ni base de données à la lecture. La matière : 363 fiches YAML, 384 articles Markdown.
- **Export par build** : catalogue (1 096 entrées citables), 7 132 passages, lexique, empreinte. Vectorize mis à jour en deux temps (ajouts avant, suppressions après). L'agent ne lit que ce que le build a publié.
- **Étape 1, contrôles** : origine, Turnstile, quota par visiteur sur empreinte d'IP salée et renouvelée chaque jour ; e-mails et numéros masqués avant toute étape.
- **Étape 2, recherche** : vecteur 1 024 dimensions (bge-m3) + recherche par mots, fusion RRF, 24 candidates. Les mots rattrapent acronymes, noms propres, codes de formation.
- **Étape 3, décision** : Clef-flash choisit une intention sur sept et trie ; 1,8 s, sinon l'ordre de recherche s'applique.
- **Étape 4, colonne** : *aucun modèle n'écrit la colonne*. Ce que la question nomme passe en tête, puis achat, appels à l'action, information. Chaque correction de règle laisse un test.
- **Étape 5, rédaction** : Llama 3.3 70B, trois derniers échanges, passages transmis comme données. Consignes : uniquement les passages, phrase fixe si rien (*« Je n'ai pas cette information dans les contenus publiés sur sfeir.com. »*), 120 mots, aucun lien. Sources converties en 1 à 4 pages du catalogue.
- **Cache** : première question complète gardée 7 jours dans KV ; la clé porte la version du contenu, pas de purge.
- **Mesure** : une ligne par échange, gardée trois mois ; jamais la réponse, l'IP, le navigateur ni un identifiant.
- **Pourquoi le modèle n'écrit que la fin** : liens (pas d'invention), délai (colonne avant texte), réversibilité (modèle = paramètre de déploiement, second fournisseur prévu).
- **Déploiement** : une commande (GitLab ou poste) ; porte 1 avec retour arrière automatique, porte 2 sous dix minutes vérifiant la même empreinte dans site, catalogue, passages.
- **Limites** : premier fragment > 2,5 s quatre fois sur dix fin octobre ; pas de compte, de cookie ni de personnalisation.

## RésuméDe400mots

Troisième article de la série sur sfeir.com, ce texte décrit l'architecture du site conversationnel ouvert le 16 novembre 2026. Le principe : des règles écrites choisissent les pages montrées, un petit modèle de classification aide à les trier, et un seul modèle rédige le dernier paragraphe, à partir des seuls contenus publiés.

Le site reste statique : Astro génère 1 626 URL, servies par Cloudflare Pages sans serveur d'application. À chaque build, un export prépare la matière de l'agent : un catalogue de 1 096 pages citables, 7 132 passages, un lexique et une empreinte de version. Les index Cloudflare Vectorize se mettent à jour en deux temps, et l'agent ne lit que ce que le build a déployé.

Une question suit six étapes. Les contrôles d'entrée vérifient l'origine, le test anti-robot Turnstile et un quota calculé sur une empreinte d'IP jamais stockée ; e-mails et numéros sont masqués. La recherche combine un vecteur bge-m3 et une recherche par mots, fusionnés par Reciprocal Rank Fusion, pour 24 candidates. Le modèle Clef-flash choisit une intention parmi sept en 1,8 seconde au plus. La colonne de pages est ensuite composée par des règles écrites et testées, sans modèle, et s'affiche en 2,7 secondes au plus. Llama 3.3 70B rédige enfin une réponse de 120 mots maximum, à température basse, avec des consignes qui interdisent d'attribuer à SFEIR ce qui n'est pas dans les passages. Si le premier mot tarde plus de 5 secondes, l'échange se termine sur la colonne. Trois relances sont calculées sans modèle.

Un cache de sept jours, dont la clé porte la version du contenu, évite les appels répétés. La mesure garde une ligne par échange pendant trois mois, sans IP ni réponse rédigée.

L'article justifie le choix de limiter le modèle à la fin par trois raisons : les liens ne peuvent pas être inventés, la colonne arrive avant le texte, et le modèle reste remplaçable. Le revers est qu'un cas mal traité demande une règle de plus.

En production, le domaine reste chez son registraire ; Pages relaie les appels /api/ vers un Worker sans adresse publique. Le déploiement comporte deux portes de santé, car Vectorize met environ quatre-vingt-dix secondes à rendre visible une écriture.

Les limites sont listées : réponses bornées au corpus, mémoire de trois échanges, latence du modèle, aucune personnalisation, risque d'injection contenu mais non supprimé.

## GrapheDeConnaissance

### Triples

| Sujet | Type Sujet | Prédicat | Objet | Type Objet | Confiance | Temporalité | Source |
|-------|-----------|----------|-------|-----------|-----------|-------------|--------|
| SFEIR | ORGANISATION | publie | article Architecture d'un site conversationnel | DOCUMENT | 0.97 | STATIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | Astro | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| sfeir.com | TECHNOLOGIE | utilise | Cloudflare Pages | TECHNOLOGIE | 0.94 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | fait_partie_de | sfeir.com | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Cloudflare Workers | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Cloudflare Vectorize | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | bge-m3 | TECHNOLOGIE | 0.92 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Reciprocal Rank Fusion | METHODOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Clef-flash | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Llama 3.3 70B | TECHNOLOGIE | 0.93 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | utilise | Cloudflare Turnstile | TECHNOLOGIE | 0.9 | DYNAMIQUE | déclaré_article |
| colonne composée par des règles | METHODOLOGIE | résout | liens inventés par le modèle | CONCEPT | 0.88 | ATEMPOREL | déclaré_article |
| SFEIR | ORGANISATION | affirme_que | un seul modèle écrit, et seulement à la fin, à partir des passages publiés | AFFIRMATION | 0.93 | DYNAMIQUE | déclaré_article |
| agent conversationnel sfeir.com | TECHNOLOGIE | mesure | colonne ≤ 2,7 s, premier mot ≤ 5 s, réponse ≤ 120 mots | MESURE | 0.9 | STATIQUE | déclaré_article |
| deux portes de santé | METHODOLOGIE | résout | réponse fondée sur un contenu retiré | CONCEPT | 0.85 | ATEMPOREL | déclaré_article |
| Cloudflare Vectorize | TECHNOLOGIE | mesure | environ 90 secondes entre écriture et lecture lors des essais | MESURE | 0.82 | STATIQUE | déclaré_article |
| Reciprocal Rank Fusion | METHODOLOGIE | est_basé_sur | Reciprocal Rank Fusion outperforms Condorcet (SIGIR 2009) | DOCUMENT | 0.88 | STATIQUE | déclaré_article |
| SFEIR | ORGANISATION | recommande | commencer par l'export (catalogue, passages, empreinte) avant de choisir un modèle | AFFIRMATION | 0.88 | ATEMPOREL | déclaré_article |

### Entités

| Entité | Type | Attribut | Valeur | Action |
|--------|------|----------|--------|--------|
| agent conversationnel sfeir.com | TECHNOLOGIE | architecture | Worker sans URL publique : contrôles, recherche, décision, colonne, rédaction, cache, mesure | AJOUT |
| colonne composée par des règles | METHODOLOGIE | principe | Blocs et ordre choisis par des règles écrites et testées, aucun modèle | AJOUT |
| deux portes de santé | METHODOLOGIE | fonctionnement | Porte 1 avec retour arrière automatique ; porte 2 vérifiant la même empreinte sous dix minutes | AJOUT |
| Clef-flash | TECHNOLOGIE | rôle | Petit modèle de classification d'intention (7 intentions) sur Workers AI | AJOUT |
| Llama 3.3 70B | TECHNOLOGIE | rôle | Modèle de rédaction, température 0,2, sur Workers AI | AJOUT |
| Reciprocal Rank Fusion | METHODOLOGIE | définition | Fusion de classements par rang réciproque (Cormack, Clarke, Büttcher, 2009) | AJOUT |
