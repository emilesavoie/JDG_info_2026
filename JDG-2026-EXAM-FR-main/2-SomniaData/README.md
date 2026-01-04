# Mandat 2 – Database - Somnia Data

## Contexte

Somnia Data est une entreprise spécialisée dans la gestion et l’analyse de données, avec pour slogan : « On garde vos rêves en mémoire ». Elle souhaite développer une plateforme web permettant aux utilisateurs de stocker leurs profils de sommeil, recevoir des recommandations personnalisées et suivre des plans d’intervention visant à améliorer la qualité de leur sommeil.

Chaque utilisateur doit avoir un compte sur la plateforme avant de pouvoir accéder aux services. Un utilisateur est caractérisé par un identifiant unique, un prénom, un nom, une adresse (rue, ville, code postal) et un courriel. Les utilisateurs peuvent enregistrer plusieurs profils de sommeil, chacun comprenant des préférences détaillées (type de matelas, fermeté, température, position de sommeil, habitudes nocturnes).

Pour chaque profil, la plateforme peut générer plusieurs plans d’intervention personnalisés, identifiés par un numéro unique et une date de création. Chaque plan d’intervention peut contenir plusieurs recommandations (exercices de relaxation, ajustements d’habitudes, horaires de sommeil), une description et un statut indiquant s’il est actif, terminé ou en attente.

Pour l’administration et l’optimisation des performances, la plateforme garde une trace des logs et statistiques sur les profils, plans d’intervention et recommandations. Chaque log est identifié par un identifiant unique et contient l’action réalisée, une description et la date. Les logs sont accédés très rarement et servent uniquement à des fins de débogage.

Vous êtes chargé de modéliser une base de données destinée à gérer le fonctionnement de la plateforme Somnia Data. Vous devrez identifier toutes les entités, leurs attributs, les associations entre elles, les cardinalités et les types d’associations (binaire 1:n, n:m, etc.).
