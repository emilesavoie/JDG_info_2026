# Q3 - Officology (7 points)

**Objectif :** Implémenter un algorithme pour placer optimalement les éléments du bureau de Nocturna Solutions afin de maximiser le score de "Joie Totale".

## Contexte

Nocturna Solutions déménage et veut concevoir l'espace de travail parfait pour ses **7 consultants**. L'espace est une grille où certains emplacements sont bloqués par des murs. Votre mission est de déterminer les coordonnées $(x, y)$ de chaque élément pour créer l'environnement le plus productif et heureux possible.

## Instructions

- Lire la configuration de la pièce (dimensions et obstacles) depuis le fichier d'entrée (ou utiliser les paramètres par défaut fournis).
- Placer tous les éléments obligatoires dans la grille.
- Respecter toutes les contraintes strictes.
- Maximiser la fonction de score définie ci-dessous.
- Produire en sortie un fichier `output.txt` contenant la grille complétée.

## Format de Sortie

Votre programme doit générer un fichier nommé `output.txt`.
Ce fichier doit contenir la grille finale, respectant exactement les dimensions et la position des murs du fichier d'entrée `input_grid.txt`.
Les caractères doivent correspondre aux éléments placés (`C`, `M`, `R`, `P`) ou aux espaces vides (`.`).

## Spécifications Techniques

### 1. La Grille et les Distances

- L'espace est une grille 2D de dimensions $L \times H$.
- La distance entre deux points $(x_1, y_1)$ et $(x_2, y_2)$ est la **Distance de Manhattan** :
  $$d = |x_1 - x_2| + |y_1 - y_2|$$
- Pour les objets occupant plusieurs cases (Fauteuils), la distance est la plus courte distance vers n'importe quelle case de l'objet.

### 2. Éléments à placer

Vous disposez de l'inventaire suivant.

| Symbole | Élément            | Quantité Requise | Description                                                       |
| :-----: | ------------------ | :--------------: | ----------------------------------------------------------------- |
|   `C`   | Consultant         | **Exactement 7** | Les employés à satisfaire (1x1).                                  |
|   `M`   | Machine à Café     | **Exactement 1** | Le cœur du bureau (1x1).                                          |
|   `R`   | Fauteuil de Sieste | **Exactement 2** | **Taille 2x1**. Peut être placé horizontalement ou verticalement. |
|   `P`   | Plante             |   **Illimité**   | Décoration (1x1).                                                 |
|   `#`   | Mur                |      (Fixe)      | Case inutilisable (déjà présente).                                |
|   `.`   | Vide               |        -         | Espace de circulation.                                            |

## Contraintes Strictes (Hard Constraints)

_Si une seule de ces règles est violée, la solution est invalide (Score = 0)._

1. **Unicité** : Une case ne peut contenir qu'un seul élément (ou une seule partie d'élément).
2. **Murs** : Aucun élément ne peut être placé sur un mur (`#`).
3. **Inventaire** : Vous devez placer exactement 7 Consultants (`C`), 1 Machine à Café (`M`) et 2 Fauteuils (`R`).
4. **Intégrité des Fauteuils** : Chaque fauteuil doit occuper 2 cases adjacentes (horizontalement ou verticalement).
5. **Espace Vital** : Deux consultants ne peuvent pas être adjacents (ni orthogonalement, ni en diagonale).
6. **Accessibilité (Flood Fill)** : Il doit exister un chemin composé de cases vides (`.`) permettant de relier n'importe quel Consultant à :
   - La Machine à Café.
   - Les 2 Fauteuils de Sieste.
   - Tous les autres Consultants.
     _Note : Le chemin ne peut pas traverser les objets ou les murs, seulement les cases vides._

## Formule de Calcul de la Joie

Le score total est la somme des scores de joie individuels de chaque consultant.
$$Score_{Total} = \sum_{i=1}^{7} Joie(Consultant_i)$$

Pour un consultant donné, la joie est calculée ainsi :

### A. Facteur Caféine (Distance)

- Si la distance ($d$) vers la Machine à Café (`M`) est $\le 3$ cases : **0 point** (Trop proche/bruyant).
- Si la distance ($d$) est $> 3$ cases : **$15 - (d \times 2)$ points** (Minimum 0).

### B. Facteur Social (Bonus/Malus)

Pour _chaque_ autre consultant dans le bureau :

- Si distance $\le 2$ : **-10 points** (Trop de bruit/distraction).
- Si distance comprise entre 3 et 6 (inclus) : **+5 points** (Synergie d'équipe).
- Si distance $> 6$ : **0 point** (Trop loin pour collaborer).

### C. Facteur Environnement (+1 pt par plante)

- **+1 point** pour chaque Plante (`P`) située dans les 8 cases voisines (adjacentes et diagonales) du consultant.

### D. Facteur Bien-être (+5 pts)

- Si la distance vers le Fauteuil de Sieste (`R`) le plus proche est $\le 3$ cases : **+5 points**.
  _(Distance mesurée vers la case du fauteuil la plus proche)_.

## Ressources

- Vous pouvez utiliser n'importe quel langage de script (Python, JS, etc.).
- Un fichier `input_grid.txt` (vide avec murs) est fourni pour tester.
- **Script de validation** : Un script `validator.py` est fourni pour vérifier votre solution. NE MODIFIEZ PAS CE FICHIER. 
```
# Usage
python validator.py output.txt input_grid.txt
```

## Critères d'évaluation

| Critère                     | Points | Description                                                                           |
| --------------------------- | ------ | ------------------------------------------------------------------------------------- |
| **Validité de la solution** | 3      | Respect des contraintes strictes (Inventaire, Murs, Espace Vital, **Accessibilité**). |
| **Score de Joie**           | 3      | Performance de votre solution comparée à un seuil de référence.                       |
| **Qualité du Code**         | 1      | Clarté, découpage en fonctions, code auto-documenté.                                  |
| **Total**                   | **7**  |                                                                                       |

\* _Note : Le layout de bureau utilisé pour l'évaluation finale sera différent de celui fourni dans `input.txt`. Une solution hardcodée ne fonctionnera pas._
