# Q2 - Optimisation de l'empilage de blocs (15 points)

**Objectif :** Développer un algorithme pour maximiser la hauteur d'une tour de blocs, en respectant les contraintes de résistance, dimensions et fragilité.

## Contexte

Le département *To Infinity And Beyond*™ souhaite empiler des blocs de différentes dimensions pour construire des tours stables et compactes, prêtes à être expédiées dans l'espace. Le système actuel, basé sur un tri naïf, ne permet pas d'atteindre les hauteurs souhaitées.

Chaque bloc possède :

- Largeur (w), profondeur (d), hauteur (h)
- Poids (p)
- Résistance maximale (r) : poids total supporté au-dessus
- Type : fragile, standard ou robuste

L'objectif est de concevoir un algorithme efficace pour optimiser l'empilage tout en garantissant la stabilité et l'accessibilité.

## Instructions

- Implémentez un algorithme d'optimisation respectant toutes les contraintes (langue de programmation au choix).
- Testez votre code sur les fichiers `blocks_X.txt`
- **Limite de temps :** 30 secondes pour trouver la meilleure configuration
- **Format de sortie :** Votre programme peut afficher plusieurs solutions successives pendant les 30 secondes. La **dernière sortie dans la console** sera considérée comme votre solution finale, qu'elle soit valide ou non.
- **Sortie valide :** Doit contenir la hauteur totale de la tour et la liste ordonnée des ids de blocs utilisés (du bas vers le haut).

## Format du fichier blocks.txt

Les fichiers `blocks_X.txt` listent les données des blocs disponibles à empiler, avec un bloc par ligne. Chaque ligne du fichier contient les informations suivantes séparées par des espaces :

```
id poids résistance largeur profondeur hauteur type
```

**Description des champs :**

- `id` : Identifiant unique du bloc (entier)
- `poids` : Poids du bloc en unités (entier)
- `résistance` : Résistance maximale que peut supporter le bloc (entier)
- `largeur` : Largeur du bloc en unités (entier)
- `profondeur` : Profondeur du bloc en unités (entier)
- `hauteur` : Hauteur du bloc en unités (entier)
- `type` : Type de produit (`fragile`, `standard`, ou `robuste`)

**Exemple :**

```
20 2002 3000000 120 123 123 fragile
21 1500 2500000 115 118 110 standard
22 3000 5000000 140 145 150 robuste
```

## Contraintes techniques

- **Résistance mécanique :** Le poids cumulé des blocs placés au-dessus d'un bloc ne doit pas excéder sa résistance maximale
- **Dimensions strictement décroissantes :** Un bloc ne peut être posé que sur un bloc strictement plus large et plus profond : $w_{haut} < w_{bas}$ et $d_{haut} < d_{bas}$
- **Contrainte de fragilité :** Un bloc fragile doit toujours être au-dessus des blocs standard ou robustes
- Implémentation en langage de programmation au choix (Python, Java, C++, C#, etc.)

## Ressources

- [Algorithmes d'optimisation combinatoire](https://en.wikipedia.org/wiki/Combinatorial_optimization)
- [Programmation dynamique](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Algorithmes génétiques pour l'optimisation](https://en.wikipedia.org/wiki/Genetic_algorithm)

## Critères d'évaluation

**Conditions d'échec automatique (0 points):**

- Solution invalide (non-respect des contraintes)
- Dépassement du temps imparti (30 secondes) avant une première sortie
- Absence de sortie valide dans la console (hauteur totale + liste d'indices)
- Sortie valide hardcodée (on veut un algorithme, pas une solution pré-calculée)

Votre algorithme sera testé sur 5 ensembles de données (500 à 1M blocs). Chaque exécution vaut 1,2 point selon la hauteur atteinte :

| Hauteur atteinte                 | Points |
| -------------------------------- | ------ |
| Solution invalide ou échec       | 0      |
| ≥ 75% de la hauteur max possible | 0.4    |
| ≥ 90% de la hauteur max possible | 0.8    |
| 100% de la hauteur max possible  | 1.2    |

**Note :** Seule la dernière sortie affichée sera prise en compte. Vous pouvez donc afficher des sorties intermédiaires pendant votre recherche de solution.

Exemple de sortie valide :

```
Height: 1234
Blocks: 10 2893 3593 3152 2853 234 5763 9003 657 5360 2165 4915 409 9022 303 6002
```
