# schopplich-toon-json-llm-token-optimization-2025-10-22

## Veille
Format de sérialisation TOON optimisé pour LLM réduisant les coûts de jetons de 30-60% - GitHub - Johann Schopplich

## Titre Article
TOON - Token-Oriented Object Notation: JSON for LLMs at half the token cost

## Date
2025-10-22

## URL
https://github.com/johannschopplich/toon

## Keywords
TOON, LLM, optimisation jetons, sérialisation données, JSON, YAML, CSV, TypeScript, API LLM, compression données, coût API, format données, architecture LLM

## Authors
Johann Schopplich (@johannschopplich)

## Pense-bêtes
- TOON réduit la consommation de jetons de 30-60% par rapport à JSON, jusqu'à 65% dans certains cas
- Format hybride fusionnant YAML (indentation hiérarchique) et CSV (format tabulaire)
- Précision de récupération : 86,6% (TOON) vs 83,2% (JSON) - meilleure compréhension par les LLM
- Syntaxe minimale : pas de guillemets, accolades réduites, indentation pour structure
- Métadonnées dans en-têtes d'arrays : `key[N]{field1,field2}:` pour validation explicite
- Projet créé le 22 octobre 2025, dernière activité 27 octobre 2025
- Cas d'usage : exports analytiques, listes GitHub, commandes e-commerce imbriquées
- Économies substantielles pour organisations avec volumes massifs de requêtes LLM
- Lisibilité supérieure à la compression binaire conventionnelle
- Alternative optimisée à JSON, YAML, CSV et XML pour contexte LLM

## RésuméDe400mots

TOON est un format de sérialisation de données innovant conçu spécifiquement pour optimiser les appels aux modèles de langage volumineux. Contrairement à JSON, qui requiert une syntaxe verbale avec guillemets et accolades répétitifs, TOON réduit drastiquement la consommation de jetons—ressource directement facturable dans les interactions avec les LLM. Le projet démontre des réductions comprises entre 30 et 60% de jetons comparé à JSON, avec certains scénarios atteignant jusqu'à 65% d'économies selon les données structurées.

L'architecture du format fusionne les concepts de YAML (indentation pour la hiérarchie) avec CSV (format tabulaire pour les données uniformes). Cette approche hybride s'avère particulièrement efficace pour les structures répétitives—collections d'objets identiques où chaque enregistrement partage les mêmes champs. Les syntaxes minimales éliminent les délimiteurs redondants, n'utilisant que des espaces pour indiquer l'imbrication et des virgules pour les séparations internes.

Techniquement, TOON encode les métadonnées critiques dans les en-têtes d'arrays : `key[N]{field1,field2}:` indique N éléments avec champs spécifiés. Cette approche explicite améliore la validation par les LLM et facilite l'analyse de structures complexes. Les benchmarks révèlent une précision de récupération de données de 86,6% versus 83,2% pour JSON, démontrant que la compacité ne sacrifie pas la compréhension du modèle.

Les cas d'usage s'étendent des exports de données analytiques aux listes de référentiels GitHub, en passant par les commandes de commerce électronique imbriquées. Pour les organisations gérant des volumes massifs de requêtes LLM, cette optimisation génère des économies substantielles aux coûts d'API, tandis que les développeurs bénéficient d'une syntaxe plus lisible qu'une compression binaire conventionnelle.

Le projet, créé le 22 octobre 2025 par Johann Schopplich, représente une réponse pragmatique à un problème économique concret : chaque jeton consommé dans une interaction LLM a un coût financier direct. En réduisant de moitié la verbosité de JSON tout en maintenant—voire améliorant—la compréhension par le modèle, TOON offre un avantage compétitif immédiat pour les applications intensives en IA.

L'innovation réside dans l'équilibre entre optimisation technique et lisibilité humaine. Contrairement aux formats de compression binaire qui deviennent opaques, TOON reste interprétable, facilitant le débogage et la maintenance. Cette caractéristique s'avère cruciale dans les environnements de production où la transparence des données échangées avec les LLM devient un enjeu de gouvernance et de conformité.
