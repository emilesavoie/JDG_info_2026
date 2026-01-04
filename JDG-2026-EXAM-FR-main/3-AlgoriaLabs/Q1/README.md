# Q1 - Navigation dans les labyrinthes oniriques (6 points)

**Objectif :** Développer un algorithme de recherche de chemin pour naviguer dans des labyrinthes oniriques complexes avec portails de téléportation, zones d'accélération et obstacles temporels.

## Contexte

Le département *Dream Navigation*™ d'Algoria Labs étudie la navigation optimale dans des environnements oniriques où les lois physiques ne s'appliquent pas toujours. Ces labyrinthes contiennent des zones spéciales qui modifient le temps de parcours.

Dans ces mondes, les voyageurs rencontrent :

- **Portails de téléportation** : Transport instantané vers une autre position
- **Zones d'accélération** : Réduction du coût de déplacement temporel
- **Champs de ralentissement** : Augmentation du coût de déplacement temporel
- **Murs temporels** : Obstacles infranchissables
- **Terrain normal** : Déplacement standard

L'objectif est de trouver le chemin le plus rapide en exploitant ces anomalies tout en évitant les obstacles.

## Instructions

- Complétez le code Python fourni (`pathfinding_base.py`) pour implémenter votre algorithme de recherche de chemin. Le code de base inclut déjà quelques fonctions utilitaires pour vous aider.
- Tenez compte des différents types de terrain et de leurs effets sur le temps de parcours
- Testez votre code sur les grilles fournies (`dream_maze_X.txt`)
- **Limite de temps :** 10 secondes maximum pour trouver le chemin optimal
- **Format de sortie :** Chemin sous forme de coordonnées (x,y) et temps total de parcours

## Contraintes techniques

- **Navigation 8-directionnelle :** Déplacement possible dans les 8 directions (horizontal, vertical, diagonal)
- **Coûts variables selon le terrain :**
  - Terrain normal : 1.0 unité de temps
  - Zone d'accélération : 0.3 unité de temps
  - Champ de ralentissement : 3.0 unités de temps
  - Portail de téléportation : 0.1 unité de temps + téléportation
  - Mur temporal : infranchissable

\* _Remarque : l’unité de temps est dépensée **après** le déplacement, en fonction de la case d’arrivée (par exemple, un déplacement de `(0,0)` vers `(0,1)` sur un terrain normal coûte `1.0` unité de temps)._

- **Déplacement diagonal :** Coût × √2 (≈ 1.414) (distance euclidienne)
- **Gestion des portails :** Chaque portail a une destination fixe défini dans la grille
- Implémentation en Python avec le code de base fourni

## Types de terrain (symboles dans la grille)

| Symbole | Type                     | Effet                        |
| ------- | ------------------------ | ---------------------------- |
| `.`     | Terrain normal           | Coût standard                |
| `S`     | Point de départ          | Début du parcours            |
| `E`     | Point d'arrivée          | Objectif à atteindre         |
| `#`     | Mur temporal             | Infranchissable              |
| `>`     | Zone d'accélération      | Coût réduit (0.3x)           |
| `<`     | Champ de ralentissement  | Coût augmenté (3.0x)         |
| `P`     | Portail de téléportation | Téléportation + coût minimal |

## Ressources

- [Algorithmes de recherche de chemin](https://fr.wikipedia.org/wiki/Recherche_de_chemin)
- [Heuristiques pour la recherche de chemin](<https://en.wikipedia.org/wiki/Heuristic_(computer_science)>)
- Code de base Python : `pathfinding_base.py`
- Grilles de test : `dream_maze_X.txt`

## Critères d'évaluation

**Conditions d'échec automatique (0 point) :**

- Dépassement de la limite de temps de 10 secondes
- Chemin invalide (passage à travers des murs, coordonnées incorrectes)
- Absence de sortie ou format incorrect
- Algorithme qui ne termine pas ou plante

**Attribution des points selon les parcours réussits:**

| Parcours réussis                              | Points |
| --------------------------------------------- | ------ |
| **Solution invalide ou échec**                | 0      |
| **dream_maze_20x20 solution optimale**        | 1      |
| **dream_maze_50x50 solution optimale**        | 1      |
| **dream_maze_60x25 solution optimale**        | 1      |
| **dream_maze_portal_stuff solution optimale** | 1      |
| **dream_maze_200x200 solution optimale**      | 2      |
| **Total**                                     | **6**  |
