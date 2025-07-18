# Projet SalesHouses

Ce projet vise à analyser les données de ventes d'appartements et de maisons, puis à construire un modèle de machine learning pour effectuer des prédictions sur le marché immobilier.

## Contenu du dossier

- **SalesHouses.ipynb**  
  Notebook principal du projet.  
  Il comprend :

  - L'exploration et l'analyse des données (EDA)
  - Le nettoyage et la préparation des données
  - La construction et l'entraînement d'un modèle de machine learning
  - L'évaluation des performances du modèle
  - La sauvegarde du modèle entraîné

- **appartements-data-db-6872f0ba853ec096170787.csv**  
  Jeu de données utilisé pour l'analyse et l'entraînement du modèle.

- **model.pkl**  
  Modèle de machine learning sauvegardé (format pickle), prêt à être utilisé pour des prédictions.

## Structure du dossier

```
Brief_2_SalesHouses/
├── appartements-data-db-6872f0ba853ec096170787.csv
├── model.pkl
├── README.md
└── SalesHouses.ipynb
```

## Prérequis

- Python 3.x
- Les bibliothèques suivantes :
  - pandas
  - numpy
  - scikit-learn
  - matplotlib
  - seaborn
  - jupyter

## Installation et utilisation

1. **Installer les dépendances**

   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn jupyter
   ```

2. **Ouvrir le notebook**

   ```bash
   jupyter notebook SalesHouses.ipynb
   ```

3. **Exécuter les cellules**  
   Suivre le notebook étape par étape pour reproduire l'analyse et la modélisation.

## Résultats

- Analyse détaillée des données immobilières
- Modèle de prédiction sauvegardé dans `model.pkl`
- Visualisations et interprétations des résultats

## Auteur

Projet réalisé dans le cadre de la formation Simplon.
