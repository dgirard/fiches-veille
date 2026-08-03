# Knowledge Base — Skills

> 2 fiches | Mise à jour : 2026-08-03 | KB thématique curée (alimentée par les fiches `fiche_type: skill`)

## Vue d'ensemble

Cette KB thématique recense les **skills** analysées dans la veille : des capacités réutilisables décrites par un fichier `SKILL.md` (skills Claude Code / agents de codage). Contrairement aux fiches d'articles, une fiche de skill capture un **fonctionnement réutilisable** — déclencheur, mécanisme, artefacts produits, anti-patterns — et non une opinion datée. Voir le format dédié dans `CLAUDE.md` § « Fiches de Skills (format spécial) ».

Les skills documentées ici déplacent l'effort de l'écriture de code vers la **conception et la mise à l'épreuve en amont** : nettoyer le vocabulaire métier, vérifier les hypothèses contre le code réel, et documenter les décisions au bon niveau de granularité. Elles s'inscrivent dans le mouvement plus large du *harness engineering* / *context engineering* (cf. `kb-context-engineering.md`).

## Catalogue des skills

| Skill | Auteur | Catégorie | Fonction en une phrase | Fiche |
|-------|--------|-----------|------------------------|-------|
| `grill-with-docs` | Matt Pocock | Conception amont (DDD) | Interview adversariale qui « cuisine » un plan d'archi contre le vocabulaire métier et les décisions documentées, et capture le tout dans `CONTEXT.md` + ADR au fil de l'eau | [skill-pocock-grill-with-docs-2026-06](fiches/2026-06/skill-pocock-grill-with-docs-2026-06.md) |
| `hyperresearch` (+ 16 skills d'étapes) | Jordan Gibbs | Deep research / harnais multi-étapes | Pipeline de recherche documentaire en 16 étapes adaptatif par paliers, où une skill-routeur invoque une skill par étape et où le rapport final ne peut plus être que retouché, jamais réécrit | [skill-gibbs-hyperresearch-2026-08-03](fiches/2026-08/skill-gibbs-hyperresearch-2026-08-03.md) |

## Concepts transverses

- **Skill-routeur et chargement différé** : une skill d'entrée qui ne contient **aucune** procédure et se borne à invoquer une skill par étape, chacune chargée fraîche au moment utile. Parade à un mode d'échec mesuré : dans un pipeline long, la procédure d'une étape tardive est **évincée par compaction** et l'orchestrateur la saute silencieusement (hyperresearch V7 → V8).
- **Verrouillage d'outils (*tool-locking*)** : restreindre l'allowlist d'un sous-agent (p. ex. `[Read, Edit]`) pour rendre un comportement **mécaniquement impossible** au lieu de le déconseiller par consigne — « patch, never regenerate ». Même famille que les hooks et les tests d'architecture : l'exécutable bat l'instruction.
- **Gates de vérification non négociables** : le style d'un livrable peut être paramétré, sa vérification non. Chez hyperresearch, les critiques reçoivent des *shims* de registre mais le vérificateur de citations et le gate d'expédition n'en reçoivent aucun.
- **Contenu récupéré = donnée, jamais instruction** : tout corps web servi sous clôture `<untrusted-source>`, frontière de confiance établie par **provenance** (les notes des sous-agents passent sans clôture) et non par inspection du contenu.
- **Conception en amont (DDD-flavored)** : forcer une conversation rigoureuse *avant* le code — nettoyer le vocabulaire, vérifier la cohérence avec l'existant, documenter les décisions.
- **Artefacts de documentation** : `CONTEXT.md` (glossaire métier pur, sans détail d'implémentation), ADR (`docs/adr/`, décision sous 3 critères : irréversible + surprenante + vrai arbitrage), `CONTEXT-MAP.md` (repos multi-domaines / bounded contexts).
- **Précision du langage** : signaler les conflits de terminologie, proposer un terme canonique, éprouver les relations métier par des cas limites.
- **Discipline documentaire** : capture *inline* (au fil de l'eau), création **paresseuse** des fichiers (« only when you have something to write »).
- **Anti-dérive** : prévenir les dérives de terminologie et les hypothèses non vérifiées qui coûtent cher plus tard.

## Liens

- Format des fiches de skills : `CLAUDE.md` § « Fiches de Skills (format spécial) »
- KB connexe : `kb-context-engineering.md` (harness engineering, skills/subagents, context engineering)
