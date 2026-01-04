# Q1 - Capture the Flag (9 points)

**Objectif :** Trouver jusqu’à **3 flags** du type **"FLAGXYZ"** dans l’application (environnement **docker-compose**) et fournir, pour chaque flag, une **méthode reproductible** pour l’obtenir.

## Contexte

Vous travaillez sur un environnement Docker Compose conçu comme un mini-CTF. L’évaluation porte autant sur la capacité à trouver les flags que sur la **qualité de la démarche** (où regarder, quelles actions effectuer, et pourquoi).

## Instructions

- Démarrer l’environnement Docker Compose.
- Trouver **3 flags**.
- Pour chaque flag, documenter une méthode claire et reproductible (étapes, outil utilisé, où se trouve l’information).

## Démarrage / Exécution

À l'aide de **docker compose**, allez au «root» du fichier et faites la commande suivante pour démarrer l'environnement :

```pwsh
docker compose up -d
```

Les ports utilisés sont écrits dans le **docker-compose.yml** pour commencer vos travaux.
(Par défaut, ouvrez simplement **localhost** dans le browser.)

## Ordinateurs ARM

Le setup est construit en mode **x86/x64 (Intel/AMD)**, vous devez utiliser **Rosetta** pour profiter pleinement des conteneurs sur les ordinateurs **Mac M1/M2**.

Si vous ne pouvez pas utiliser Rosetta, vous devez enlever l'image ctf-web-user, et certaines fonctionnalités pourraient ne pas fonctionner comme prévu / le problème pourrait être plus difficile. Mais c'est possible sans Rosetta.

## Ressources

- Outils développeur du navigateur (F12) : storage, network, console, etc...
- Fichier `docker-compose.yml` (ports et services exposés).

## Conseil(s)

- Regarder ses outils browsers, les données stockées, les messages, (F12), etc. Il est possible que les développeurs donnent trop d'informations sur leur environnement et leur fonctionnement ;)
- ctf-web-user utilise le domaine "ctf-web:3000" pour ses requêtes
- ctf-web-user utilise un navigateur "moderne" avec des requis normaux comme CORS

## Critères d'évaluation

Chaque **flag** vaut jusqu’à **3 points** selon la qualité de la démarche. Un flag sans justification vaut **0**.

| Critère               | Points | Description                                     |
| --------------------- | -----: | ----------------------------------------------- |
| **Flag #1 + méthode** |      3 | Flag trouvé + démarche reproductible et précise |
| **Flag #2 + méthode** |      3 | Flag trouvé + démarche reproductible et précise |
| **Flag #3 + méthode** |      3 | Flag trouvé + démarche reproductible et précise |
| **Total**             |  **9** |                                                 |

_Exemples de justifications invalides (0 points) :_

- J'ai décompilé les images docker et j'ai lu directement dans les fichiers de code de l'app... (faiblesse due au setup docker pour faire des CTF, ça ne passerait pas sur un environnement en "production")
- J'ai lu directement dans la **BD Postgres** du **docker-compose** (settings étant disponibles publiquement...)
