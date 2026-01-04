# Q3 - Requêtes SQL (5 points)

**Objectif :** Pour le schéma que vous avez proposé à la question 2, écrivez les requêtes SQL dans les fichiers correspondants `REQUEST_X.sql`.

## Instructions

- Complétez les fichiers `REQUEST_1.sql` à `REQUEST_5.sql` dans ce répertoire
- Utilisez le langage MySQL si possible
- Basez-vous sur votre schéma de la question 2.2
- Optimisez les requêtes pour les performances
- Commentez les requêtes complexes

## Requêtes à implémenter

### 1. REQUEST_1.sql

Récupérer la liste des utilisateurs qui ont plus de 3 plans d'intervention actifs.

### 2. REQUEST_2.sql

Récupérer la liste de tous les profils d'un utilisateur donné (id utilisateur = 42) avec son nombre de plans d'intervention en attente.

### 3. REQUEST_3.sql

Récupérer toutes les recommandations non actives pour un plan donné (id plan = 30).

### 4. REQUEST_4.sql

Récupérer l'historique des actions dans les logs pour un utilisateur donné (id utilisateur = 42) sur ses plans et recommandations, triés en ordre décroissant selon leur date de création.

### 5. REQUEST_5.sql

Récupérer tous les plans d'intervention avec leur profil et utilisateur associé créés entre le 1er décembre et le 1er janvier, triées en ordre chronologique selon la date de création.

## Ressources

- [Documentation MySQL Queries](https://dev.mysql.com/doc/refman/8.0/en/sql-statements.html)
- [MySQL JOIN Types](https://dev.mysql.com/doc/refman/8.0/en/join.html)

## Critères d'évaluation

| Critère           | Points | Description                                         |
| ----------------- | ------ | --------------------------------------------------- |
| **REQUEST_1.sql** | 1      | La requête retourne correctement ce qui est demandé |
| **REQUEST_2.sql** | 1      | La requête retourne correctement ce qui est demandé |
| **REQUEST_3.sql** | 1      | La requête retourne correctement ce qui est demandé |
| **REQUEST_4.sql** | 1      | La requête retourne correctement ce qui est demandé |
| **REQUEST_5.sql** | 1      | La requête retourne correctement ce qui est demandé |
| **Total**         | **5**  |                                                     |
