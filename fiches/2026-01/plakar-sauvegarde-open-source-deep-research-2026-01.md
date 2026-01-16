# plakar-sauvegarde-open-source-deep-research-2026-01

## Veille
Plakar - sauvegarde open source française, Kloset stockage immuable, Linux Foundation CNCF, 60x performances S3

## Titre Article
Plakar : la révolution française de la sauvegarde open source

## Date
2026-01-07

## URL
https://github.com/dgirard/fiches-veille/blob/main/docs/deep%20research/202601/Plakar%20_%20la%20r%C3%A9volution%20de%20la%20sauvegarde%20open%20source.md

## Keywords
Plakar, sauvegarde, backup, open source, Kloset, ptar, Linux Foundation, CNCF, chiffrement, déduplication, FastCDC, Restic, Borg, S3, immutable storage, France, souveraineté

## Authors
Deep Research Veille Interne

## Ton
Profil : Document de recherche technique approfondi, registre analytique et comparatif, perspective évaluation technologique.
Style : Structure encyclopédique avec architecture technique détaillée, matrices comparatives, benchmarks chiffrés. Équilibre factuel entre avantages et limitations. Citations d'audit cryptographique. Couverture médiatique multilingue analysée. Public cible : architectes infrastructure, DevOps, RSSI, décideurs IT évaluant solutions de sauvegarde.

## Pense-betes
- **Fondateurs** : Julien Mangeard (ex-CTO Veepee) + Gilles Chehade (créateur OpenSMTPD, contributeur OpenBSD)
- **Levée** : 3M$ en mai 2025, investisseurs Olivier Pomel (Datadog), Solomon Hykes (Docker)
- **Janvier 2026** : Rejoint Linux Foundation et CNCF - "standard ouvert pour la résilience"
- **Architecture 3 couches** : Storage Layer (immuable), Repository (compression/chiffrement), Snapshot (VFS, B+tree)
- **Kloset** : Moteur stockage immuable - chunks dédupliqués, compressés, chiffrés par hash contenu
- **FastCDC** : 8 149 MB/s vs 614 MB/s pour Rabin de Restic (13x plus rapide)
- **Audit crypto** : Jean-Philippe Aumasson (28 février 2025) - "conception cryptographiquement saine"
- **Algos post-audit** : Argon2id (256Mo, 4 iter), AES-256-GCM-SIV, AES-KW, BLAKE3
- **Format .ptar** : Archive immuable (27 juin 2025), remplace tar (1979), accès aléatoire, S3 natif
- **Performances S3** : 60x amélioration (14 min → 13 sec), uploads parallélisés
- **Déduplication** : 91,4% réduction stockage (327 Go → 28 Go pour 10 backups)
- **vs Restic** : Interface web intégrée, GC non-bloquant, FastCDC vs Rabin
- **vs Borg** : S3 natif (Borg nécessite SSH), courbe apprentissage plus simple
- **Licence ISC** : Style OpenBSD, permissive, engagement permanent open source
- **GitHub** : 1 400+ stars, 52 forks, 20 contributeurs, 5 967 commits
- **Enterprise beta** : AWS Marketplace depuis décembre 2025
- **Couverture FR** : Korben "atomise Restic et Borg", LMI, LinuxFr, Comptoir Open Source
- **Gap international** : Aucune couverture allemande, néerlandaise, japonaise identifiée

## RésuméDe400mots
Ce document de recherche analyse Plakar, startup française de sauvegarde open source fondée à Paris en septembre 2024 par Julien Mangeard (ex-CTO Veepee) et Gilles Chehade (créateur d'OpenSMTPD). Après une levée de 3 millions de dollars en mai 2025 auprès d'investisseurs prestigieux (Olivier Pomel de Datadog, Solomon Hykes de Docker), Plakar a rejoint la Linux Foundation et le CNCF en janvier 2026.

L'architecture repose sur trois couches : une couche de stockage immuable et parallélisée, une couche repository gérant compression et chiffrement locaux avec index pour déduplication, et une couche snapshot organisant les données via un système de fichiers virtuel soutenu par un arbre B+ personnalisé. Le moteur Kloset constitue le cœur technologique avec ses principes de stockage immuable, snapshots auto-descriptifs, connecteurs modulaires et auditabilité cryptographique.

L'algorithme FastCDC atteint 8 149 MB/s contre 614 MB/s pour le Rabin de Restic, soit 13x plus rapide. La cryptographie a été auditée par Jean-Philippe Aumasson en février 2025, concluant à une "conception cryptographiquement saine". Les algorithmes post-audit incluent Argon2id pour la dérivation de mot de passe (256 Mo de mémoire), AES-256-GCM-SIV résistant aux erreurs de nonce, et BLAKE3 pour le hachage.

Le format .ptar, annoncé en juin 2025, modernise tar (1979) avec accès aléatoire, support S3 natif et déduplication. Un test illustratif : archiver deux fois 8,8 Go produit 18 Go avec tar.gz contre 8,2 Go avec .ptar.

Les benchmarks revendiquent une amélioration de 60x sur S3 (14 minutes à 13 secondes) et une réduction de stockage de 91,4% via déduplication (327 Go → 28 Go pour 10 sauvegardes). Face à Restic (27k stars GitHub), Plakar offre une interface web intégrée et un garbage collection non-bloquant. Face à Borg, Plakar propose un support S3 natif (Borg nécessite SSH) et une courbe d'apprentissage plus simple.

La licence ISC (style OpenBSD) garantit un engagement permanent open source. La couverture médiatique française est enthousiaste (Korben : "atomise Restic et Borg"), mais l'absence de couverture internationale (Allemagne, Pays-Bas, Japon) reflète le caractère récent du projet.

Pour les organisations orientées S3/AWS et les équipes DevOps recherchant une solution française souveraine, Plakar mérite une évaluation sérieuse, avec une période de test recommandée sur des workloads non-critiques en attendant la maturation de l'écosystème.
