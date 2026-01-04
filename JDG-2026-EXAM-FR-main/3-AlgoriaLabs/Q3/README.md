# Q3 - Tic Tac Throw! (7 points)

**Objectif :** Implémenter un agent artificiel qui joue à Tic Tac Toe (4x4) de façon systématiquement sous-optimale, afin de maximiser ses chances de perdre contre un adversaire qui essaie également de perdre.

## Contexte

Le département Idiot Factory™ d'Algoria Labs s'intéresse à un défi original : développer des agents capables de jouer au Tic Tac Toe 4x4 en essayant activement de perdre.

Le jeux de Tic Tac Toe 4x4 se joue sur une grille de 4x4 cases. Deux joueurs s'affrontent en plaçant alternativement leurs symboles (X et O) sur la grille. Le but est d'aligner 4 symboles consécutifs horizontalement, verticalement ou en diagonale. Cependant, dans ce défi, chaque agent doit adopter une stratégie visant à éviter la victoire, en essayant de perdre contre un adversaire qui suit la même logique.

## Instructions

- Examinez le code de base fourni dans le fichier `tictacthrow.py`
- Implémentez la classe `LosingAgent` dans le fichier `losing_agent.py` qui doit jouer de façon sous-optimale
- Votre agent doit être capable de perdre contre un adversaire qui essaie aussi de perdre
- Testez votre implémentation avec différentes stratégies d'adversaires (aléatoire, intermédiaire, expert)
- **CONTRAINTE CRITIQUE** : Chaque décision de votre agent doit être prise en moins de 10 secondes, sinon l'évaluation sera automatiquement de 0 points

## Ressources

- [Algorithmes de Tic Tac Toe](https://en.wikipedia.org/wiki/Tic-tac-toe#Strategy)
- [Documentation Python pour les classes](https://docs.python.org/3/tutorial/classes.html)
- Code de base disponible dans le repo Github

## Critères d'évaluation

**ATTENTION** : Si votre agent prend plus de 10 secondes pour prendre une décision lors de n'importe quel coup, l'évaluation s'arrête immédiatement et vous aurez 0 points.

**Métrique d'évaluation** : Le ratio de non-victoire est calculé comme suit:

```
Ratio de non-victoire = (Défaites + Matchs nuls) / Total de parties
```

Un agent qui perd ou fait match nul est considéré comme ayant réussi à éviter de gagner.

| Critère                                       | Points | Description                                                                                 |
| --------------------------------------------- | ------ | ------------------------------------------------------------------------------------------- |
| **Non-victoire contre l'agent aléatoire**     | 2      | Votre agent ne gagne pas (perd ou match nul) contre l'agent aléatoire au moins 80% du temps |
| **Non-victoire contre l'agent intermédiaire** | 2.5    | Votre agent ne gagne pas contre l'agent intermédiaire au moins 80% du temps                 |
| **Non-victoire contre l'agent expert**        | 2.5    | Votre agent ne gagne pas contre l'agent expert en défaite au moins 80% du temps             |
| **Total**                                     | **7**  |                                                                                             |
