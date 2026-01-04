# Q5 - Prompt Engineering (3 points)

**Objectif :** Concevoir des prompts robustes (système + utilisateur) pour une IA générative afin qu'elle produise des plans de sommeil personnalisés.

## Contexte

SchleepShop souhaite automatiser la génération de plans de sommeil personnalisés. Les prompts doivent être conçus pour guider une IA afin qu'elle retourne un plan structuré, clair et adapté aux données utilisateur.

**Contrainte importante :** L'IA est restreinte dans le cadre de l'examen, donc vous n'avez pas le droit de tester vos prompts. Basez-vous uniquement sur la théorie de prompt engineering.

## Instructions

- Écrivez les prompts en français.

## Description des prompts à compléter

- **Prompt système** : Ensemble d'instructions destinées à l’IA pour définir son rôle, fixer les limites de ses réponses, préciser le ton à adopter et structurer le format de sortie attendu. Dans le cadre de ce mandat, le rôle de l'IA est celui d'un expert en sommeil capable de fournir des recommandations basées sur les meilleures pratiques cliniques et scientifiques.

- **Prompt utilisateur** : Modèle de questions ou de champs à renseigner par l’utilisateur, permettant de collecter les informations nécessaires à la personnalisation du plan de sommeil. Dans le cadre de ce mandat, le prompt utilisateur doit permettre de recueillir des données telles que l'âge, les habitudes de sommeil, les problèmes rencontrés et les objectifs spécifiques de l'utilisateur.

## Livrables attendus

- `prompt_system.txt`
- `prompt_user.txt`

## Ressources

- [Prompt Engineering Techniques (Prompting Guide)](https://www.promptingguide.ai/techniques)
- [Best Practices for Prompt Engineering (OpenAI Help)](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)
- [Guide de Prompt Design (Anthropic)](https://docs.anthropic.com/claude/docs/introduction-to-prompt-design)

## Critères d'évaluation

| Critère                             | Points | Description                                                                            |
| ----------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| **Prompt système**                  | 1      | Rôle clair, contraintes de sécurité, format de sortie défini (schéma JSON/Markdown)    |
| **Prompt utilisateur**              | 1      | Variables complètes, template clair, instructions sur le format et le niveau de détail |
| **Application des principes de PE** | 0.75   | Spécificité, utilisation de patterns explicites                                        |
| **Gestion des cas limites**         | 0.25   | Identification des situations à risque et instructions de repli                        |
| **Total**                           | **3**  |                                                                                        |
