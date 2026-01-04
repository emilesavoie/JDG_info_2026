# Q4 - Emojiology (7 points)

**Objectif :** Analyser les tendances de sommeil des employés de Nocturna Solutions en utilisant Emojicode.

## Contexte

Nocturna Solutions veut analyser les tendances de sommeil de ses employés pour optimiser leur bien-être et leur productivité. L'entreprise possède des données sur l'heure de début de sommeil et l'état de sommeil à chaque heure subséquente de ses employés. L'objectif sera donc d'analyser ces données pour en arriver à des conclusions.

**La twist spéciale :** Les entrées de données sont en emojis, le code doit être rédigé en **Emojicode** et la sortie doit être fournie en emojis également !

## Instructions

- Consultez le code à compléter dans le fichier `solution.emojic` (méthodes 🅰️, 🅱️ et ©️).
- Implémentez la solution en langage **Emojicode**.
- Les données d'entrées à traiter proviennent du fichier `input.txt`, le parsing des données d'entrées à déjà été fait pour vous.
- Générez la sortie en **console** dans le format spécifié (exemple dans output_example.txt).

## Format des données

### Données d'entrée

- ⭐⭐⭐ : Niveaux de satisfaction du sommeil (1 étoile = très insatisfait, 5 étoiles = très satisfait)
- 🕐XX : Heure de coucher
- 🛏️😴💭💤 : États de sommeil à chaque heure incluant l'heure de coucher (au lit🛏️, someil léger😴, REM💭, sommeil profond💤)

### Analyse statistique à effectuer

Vous devez produire **3 statistiques** à partir des lignes d’entrée. Voir le format de sorties dans le fichier `output_example.txt`.

#### 🏆 Classement de satisfaction moyenne par heure de coucher (Méthode 🅰️)

```
Pour chaque heure de coucher 🕐XX, calculer la satisfaction moyenne (en étoiles entières) et produire un classement (Arrondissez à la valeur entière la plus proche).
```

#### 🕰️ État de sommeil le plus fréquent par heure absolue (Méthode 🅱️)

```
Pour chaque heure entre 20h et 12h fournissez l’état de sommeil le plus fréquent à cette heure avec son emoji correspondant.

* En cas d’égalité, utiliser la priorité suivante :
💤 > 💭 > 😴 > 🛏️

** Si aucune donnée n’existe pour une heure, afficher aucun emoji (vide).
```

#### 📊 Efficacité moyenne du sommeil (Méthode ©️)

```
Pour chaque employé, calculez l’efficacité de son sommeil comme le ratio entre les heures passées endormi (😴, 💭, 💤) et le total des heures enregistrées (incluant 🛏️).

heures_endormi = #(😴) + #(💭) + #(💤)
heures_totales = #(🛏️) + #(😴) + #(💭) + #(💤)
efficacite = heures_endormi / heures_totales

Sortie attendue sous format emoji, arrondi à la hausse (74% = 8/10 carrés verts) :
🟩🟩🟩🟩🟩🟩🟩🟩⬜⬜
```

## Exemple de flux

```
Input
⭐⭐⭐ 🕐22 😴💤💤😴💤💤💤🛏️
⭐⭐ 🕐23 💤💤😴💤💭💤🛏️
⭐⭐⭐ 🕐21 😴😴💤💭💤😴🛏️
...

Output (exemple de structure, valeurs fictives) :

🏆
🥇 🕐22 ⭐⭐⭐⭐
🥈 🕐21 ⭐⭐⭐
🥉 🕐23 ⭐⭐

🕰️
🕐20 😴
🕐21 😴
🕐22 💤
🕐23 💭
🕐00 💭
...

📊
🟩🟩🟩🟩🟩🟩🟩⬜⬜⬜
```

## Exécution avec Docker

Pour compiler et exécuter votre code Emojicode, utilisez le container Docker fourni :

1. **Construire le container (première fois seulement) :**

   ```powershell
   cd emojicode-container
   docker-compose build
   ```

2. **Compiler et exécuter votre fichier .emojic :**

   **Option A - Avec le script (recommandé si sur windows) :**

   ```powershell
   .\run-emojicode.ps1 .\solution.emojic
   ```

   **Option B - Manuellement avec Docker :**

   ```powershell
   cd emojicode-container
   docker-compose run --rm emojicode bash -c "emojicodec solution.emojic && ./solution"
   ```

## Ressources

- [Documentation Emojicode](https://www.emojicode.org/docs/reference/)
- [Documentation Emojicode - Package Standard](https://www.emojicode.org/docs/packages/s/)

## Critères d'évaluation

Une solution qui n'utilise pas Emojicode ne sera pas évaluée. Vous pouvez cependant obtenir des points partiels selon les critères suivants :

| Critère                                     | Points | Description                                                                                                                                    |
| ------------------------------------------- | ------ | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| **Classement satisfaction moyenne**         | 2      | Calcul correct de la satisfaction moyenne par heure de coucher, classement approprié avec médailles, arrondi à l'entier le plus proche         |
| **État le plus fréquent par heure absolue** | 2      | Détermination correcte de l'état dominant pour chaque heure (20h-12h), gestion des égalités selon la priorité, affichage vide si aucune donnée |
| **Efficacité moyenne du sommeil**           | 2      | Calcul précis du ratio heures_endormi/heures_totales, représentation visuelle correcte avec carrés verts/blancs, arrondi à la hausse           |
| **Compilation et exécution**                | 1      | Le code compile sans erreur en Emojicode, peut être exécuté et affiche une sortie en console du format attendu.                                |
| **Total**                                   | **7**  |                                                                                                                                                |

\* _Note : L'évaluation se fera avec une série de données différente de celle fournie dans `input.txt`. Une solution hardcodée ne fonctionnera pas._
