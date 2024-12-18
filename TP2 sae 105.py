import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Chemin vers le fichier CSV
file_path = 'C:\Users\akira\Desktop\BUT RT1 sauvegarde\SAE 105\TP2'  # Remplir avec le chemin du fichier CSV

# Initialisation des listes pour les données
# Déclarer ici les variables pour stocker les données extraites

# Lecture des données avec csv
renouvelable = []
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            eolien = float(row['Eolien'])
            solaire = float(row['Solaire']) # Extraction des données nécessaires
            hydraulique = float(row['Hydraulique']) # Extraire les colonnes pertinentes ici (par ex. Date, Consommation, etc.)
            pass
        except (ValueError, KeyError):
            # Gestion des erreurs (par ex. valeurs manquantes ou format incorrect)
            continue

# Tri des données
# Implémenter le tri des données selon les critères nécessaires

# Préparer les données pour la visualisation
# Transformer les données extraites en listes ou séries utilisables pour les graphiques

# Visualisation
plt.figure(figsize=(12, 6))
# Ajouter les courbes ou graphiques nécessaires ici

# Ajout des détails au graphique
plt.title("Titre du graphique")  # Remplir avec le titre approprié
plt.xlabel("Nom de l'axe X")  # Indiquer l'axe X
plt.ylabel("Nom de l'axe Y")  # Indiquer l'axe Y
plt.legend()  # Ajouter des légendes si nécessaire
plt.grid(True)
plt.tight_layout()
plt.show()
