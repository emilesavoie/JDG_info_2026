# Q1 - Serveur Backend (8 points)

**Objectif :** Exposer des endpoints **GET** (pour remplir des dropdowns) et un endpoint **POST** (pour randomiser des éléments) en s’appuyant sur des APIs externes, avec une gestion d’erreurs.

## Contexte

Votre équipe est mandatée pour concevoir et mettre en place un serveur backend capable de supporter une application qui aidera les utilisateurs à planifier leurs brosses (soirées bien arrosées).

Le backend doit agréger plusieurs APIs publiques (cocktails, repas, jeux, musique) afin de fournir des listes dynamiques pour un futur frontend.

L’objectif est de permettre à l’utilisateur de générer une planification générale d’une soirée (choix de cocktails, repas, jeux, playlists musicales) de façon interactive et personnalisée.

## Instructions

- Implémenter les **GET** nécessaires pour obtenir les options de chaque catégorie (ingrédients, catégories, genres, etc.).
- Implémenter un **POST** qui récupère les listes/choix et retourne des éléments randomisés.
- Tolérance aux erreurs : si une API externe est inaccessible, retourner **500** sans crash.

## Livrable attendu

On travaille avec **4 catégories d'items** :

- **Cocktails**
- **Repas**
- **Jeux vidéo**
- **Musique**

Pour **chaque catégorie**, vous devez exposer des routes permettant :

- **1 GET** qui retourne _tous les sous-éléments_ servant à remplir des dropdowns (ex: ingrédients, catégories, genres, etc.).
- **1 GET** qui retourne une _liste d'items filtrés_ en fonction d'un ou plusieurs sous-éléments/types fournis en paramètres (ex: ingrédients sélectionnés, catégorie de jeu sélectionnée, genre musical sélectionné).

Globalement, vous devez aussi exposer :

- **1 POST** qui reçoit les choix/critères (listes de sous-éléments sélectionnés) et retourne une **planification randomisée** :
  - **1 cocktail**
  - **1 repas**
  - **1 jeu vidéo**
  - **5 musiques**

```
# Exemple
- Un cocktail avec du [Gin] (ingrédient).
- Un repas avec du [Poulet] (ingrédient).
- Un jeu de style [Shooter] (catégorie).
- Une liste de 5 chansons de type [Rock] (genre).
```

## Codes HTTP attendus

Chaque route doit retourner le **bon code HTTP** en pair avec les données :

- **20X** si la requête réussit et retourne des données (ex: `200 OK`).
- **40X** si la requête est valide mais qu'**aucun élément n'est disponible** selon les critères (ex: `404 Not Found`).
- **50X** en cas d'erreur serveur, notamment si une **API externe est inaccessible / en erreur** (ex: `500 Internal Server Error`) — le serveur ne doit pas crash.

> Conseil: vous pouvez aussi utiliser `400 Bad Request` si les paramètres requis sont manquants/mal formés.

## Bonus (2 Points)

Le bonus peut uniquement porter votre note au maximum **100 %** de la valeur maximale de l'exercice :

- Implémenter une authentification basique :
  - Un **POST** `/login` avec `www-form-encoded` qui retourne un `SET_COOKIE` contenant le nom d'utilisateur en tant que chaîne.
  - La requête doit inclure `username` et `password` en tant que chaînes, validées à partir d'un tableau lu dans un fichier JSON.
  - Retourner un **401 Unauthorized** pour les **GET/POST** si l'utilisateur n'est pas authentifié (via `SET_COOKIE`).

## API à utiliser

- [The Cocktail DB](https://www.thecocktaildb.com/api.php)
- [The Meal DB](https://www.themealdb.com/api.php)
- [MMOBomb API](https://www.mmobomb.com/api)
- [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API#Application_rate_limiting_and_identification)
  - Veuillez lire les instructions pour respecter les restrictions (par exemple, chaîne user-agent).

**En cas de problèmes de connectivité avec les API externes :**

Écrire comment un support minimal pour cette API pourrait être implémenté.  
Hardcoder quelques options comme solution de secours.

## Contraintes techniques

- Vous devez utiliser les APIs listées ci-dessus pour obtenir les données.
- Respecter les limitations des API (ex: MusicBrainz : user-agent / rate limiting).
- Le stack doit être disponible pour les correcteurs afin d'exécuter l'application. Langages Tolérés:

  - **JavaScript/TypeScript/Node**
  - **Java** (Spécifiez le setup avec la version de Java installée, idéalement via SDKMAN).
  - **Rust**
  - **C#**
  - **Python**

- Pas besoin de réutiliser `./backend-example.py`; il sert uniquement à mettre en évidence les routes à implémenter avec un exemple de code.
- Bonus : si authentification implémentée, protéger vos routes via cookie et retourner **401** quand non authentifié.

## Client.py

Contient un exemple des appels qui pourraient être effectués pour tester votre API.  
Si vous implémentez le bonus, vous devez modifier `Client.py` pour supporter l'authentification.

## Critères d'évaluation

| Critère                       | Points | Description                                                                                                |
| ----------------------------- | -----: | ---------------------------------------------------------------------------------------------------------- |
| **GET - Options (dropdowns)** |      1 | 1 GET par catégorie pour retourner dynamiquement les sous-éléments (ingrédients, catégories, genres, etc.) |
| **GET - Items filtrés**       |      1 | 1 GET par catégorie pour retourner une liste d'items selon des paramètres (filtres)                        |
| **POST - Randomisation**      |      2 | 1 POST qui compose le résultat final (1 cocktail, 1 repas, 1 jeu, 5 musiques) à partir des choix reçus     |
| **Status HTTP + robustesse**  |      2 | 20X si OK, 40X si aucun résultat, 50X si erreur (API externe down => 500) sans crash                       |
| **Qualité du code**           |      2 | Code réutilisable/modulable (méthodes/classes), clarté, séparation des responsabilités, gestion d'erreurs  |
| **Bonus : Auth**              |   +2.0 | `/login` (form-encoded) + cookie + protection `401`                                                        |
| **Total**                     |  **8** | cap à 8 points                                                                                             |
