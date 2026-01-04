# Q1 - Deadlocks (5 points)

**Objectif :** Corriger/améliorer un programme C qui se bloque (deadlock) et expliquer clairement les changements apportés.

## Contexte

Vous avez devant vous le fichier `to_debug`, un problème écrit en C (sans le ++).  
Votre collègue a entamé une partie du travail, mais il n'arrive pas à identifier le problème avec son programme.  
Le programme semble s'arrêter sans raison apparente...

## Instructions

Pour exécuter le programme :

- Vous pouvez le lancer localement avec un compilateur de votre choix.
- Vous pouvez également utiliser un compilateur en ligne pour le tester.

### Commande pour lancer le programme (après compilation)

```bash
./a.out <nbProducteurs> <nbConsommateurs> <tailleTampon>
```

## Contraintes techniques

- Garder la solution en C (pas de C++).
- Viser une exécution reproductible et une amélioration observable (moins de blocages / meilleur comportement).

## Ressources

- Compilateur C en ligne : [OnlineGDB](https://www.onlinegdb.com/online_c_compiler)
- Concepts : producteur/consommateur, verrous (mutex), conditions (condvar), deadlocks.

## Critères d'évaluation

| Critère                          | Points | Description                                                                 |
| -------------------------------- | -----: | --------------------------------------------------------------------------- |
| **Explications et raisonnement** |    2.5 | Explication écrite des changements et du diagnostic                         |
| **Amélioration de l'exécution**  |    2.5 | Exécution améliorée vs initial (points partiels si des blocages persistent) |
| **Total**                        |  **5** |                                                                             |
