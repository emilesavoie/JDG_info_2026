# Q2 - Sloganology (7 points)

**Objectif :** Développer un outil de génération de slogans intelligent pour Nocturna Solutions.

## Contexte

En pair avec son nouveau logo, Nocturna veut se doter d'un outil de génération de slogans intelligent. Cet outil devra produire des slogans créatifs, pertinents et grammaticalement corrects qui reflètent l'identité de l'entreprise de consulting spécialisée dans les solutions nocturnes.

## Instructions

Développez un programme qui **reçoit en entrée une liste de mots** et **génère un slogan grammaticalement correct** en utilisant ces mots.

### Format d'entrée

Votre programme recevra une liste de mots de différentes catégories grammaticales dans une ordre aléatoire :

- Noms propres (ex: Nocturna)
- Noms communs (ex: consultation, solutions, nuit)
- Adjectifs (ex: intelligent, logique, innovant)
- Verbes (ex: briller, éclairer, accompagner)

Un exemple de format d'entrée se trouve dans le **fichier `input.txt`** situé dans le même dossier que votre exécutable/script. **Chaque ligne contient un mot**.

**Exemple de fichier `input.txt` :**

```
Nocturna
consultation
logique
intelligent
nuit
```

### Format de sortie

Votre programme doit produire un slogan qui :

- Utilise **tous les mots fournis** en entrée
- Respecte les **règles grammaticales** (accords, conjugaisons, syntaxe)
- Forme une **phrase cohérente et percutante**
- Reflète l'identité de Nocturna Solutions

**Exemple de sortie :**

```
"Nocturna, de la consultation logique et intelligente, même la nuit"
```

## Contraintes techniques

- **Tous les mots** de la liste d'entrée doivent être utilisés dans le slogan
- Le slogan doit être **grammaticalement correct** (accords en genre/nombre, structure syntaxique valide)
- Les mots peuvent être **modifiés** selon les règles grammaticales (ex: "intelligent" → "intelligente" pour l'accord)
- L'**ordre des mots** peut être modifié pour créer une phrase cohérente
- Il est aussi permis d'ajouter **d'autres mots** (noms, adjectifs, verbes, etc.) supplémentaires pour vous aider à former une phrase naturelle et correcte
- Le slogan ne doit pas dépasser **100 caractères**
- La méthodologie est à votre guise, tant qu'elle n'utilise pas d'API LLM externes. Vous pouvez utiliser des bibliothèques de traitement du langage naturel (NLP) open-source par exemple.

## Exemples supplémentaires

**Entrée :** `[Nocturna, solutions, briller, obscurité]`  
**Sortie possible :** `"Nocturna : des solutions qui brillent dans l'obscurité"`

**Entrée :** `[consultation, nuit, succès, jour]`  
**Sortie possible :** `"consultation de nuit, succès de jour"`

**Entrée :** `[Nocturna, défis, éclairer, expertise]`  
**Sortie possible :** `"Nocturna : notre expertise éclaire vos défis"`

## Ressources

- [Notions de NLP et génération de texte](https://en.wikipedia.org/wiki/Natural_language_processing)
- [Traitement automatique du langage naturel](https://fr.wikipedia.org/wiki/Traitement_automatique_du_langage_naturel)
- Aucun code de base n'est fourni, à vous de choisir votre approche

## Exemple d'approches valides pour vous aider

- **Approche par templates** : Créer des modèles de phrases et y insérer les mots
- **Approche grammaticale** : Analyser la catégorie grammaticale des mots et construire des phrases valides
- **Approche combinatoire** : Tester différentes combinaisons et valider la grammaire
- **Approche par règles** : Définir des règles de construction de phrases en français

## Critères d'évaluation


| Critère                            | Points | Description                                                                                                                       |
| ---------------------------------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- |
| **Utilisation complète des mots**  | 2      | Tous les mots de l'entrée sont présents dans le slogan généré, aucun mot n'est oublié                                             |
| **Correction grammaticale**        | 2      | Respect des règles grammaticales (accords en genre/nombre, conjugaisons correctes, syntaxe valide), structure de phrase cohérente |
| **Qualité et cohérence du slogan** | 2      | Le slogan a du sens, est percutant, reflète l'identité de Nocturna Solutions, est mémorable                                       |
| **Créativité et agencement**       | 1      | Capacité à agencer les mots de manière originale, utilisation créative des mots de liaison, qualité de la formulation             |
| **Total**                          | **7**  |                                                                                                                                   |

\* _Note : L'évaluation se fera avec plusieurs séries de mots différentes de celles fournies dans `input.txt`. Une solution hardcodée ne fonctionnera pas._