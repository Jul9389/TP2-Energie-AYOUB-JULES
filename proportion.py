import csv
import matplotlib.pyplot as plt
from collections import defaultdict
from datetime import datetime

# Fonction pour parser la date sans l'heure
def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except ValueError:
        return None

# Chemin vers le fichier CSV
file_path = '/Users/jules9389/Documents/cours/RT/projet_code_énergie/RTE_2022.csv'  # Remplir avec le chemin du fichier

# Initialisation des variables pour stocker les données extraites
renouvelable_mois = defaultdict(float)
non_renouvelable_mois = defaultdict(float)

# Lecture des données avec csv
with open(file_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        try:
            # Extraction des valeurs d'énergie
            eolien = float(row['Eolien'])  
            solaire = float(row['Solaire'])  
            hydraulique = float(row['Hydraulique'])  
            fioul = float(row['Fioul'])  
            charbon = float(row['Charbon'])  
            gaz = float(row['Gaz'])  
            nucleaire = float(row['Nucleaire'])  
            pompage = float(row['Pompage'])  
            
            # Calcul de la production renouvelable et non-renouvelable
            renouvelable = eolien + solaire + hydraulique
            non_renouvelable = fioul + charbon + gaz + nucleaire + pompage

            # Extraction de la date et du mois
            date_str = row['Date']
            date = parse_date(date_str)
            if date:
                mois = date.strftime("%Y-%m")  # Format du mois (année-mois)

                # Ajout des valeurs pour chaque mois
                renouvelable_mois[mois] += renouvelable
                non_renouvelable_mois[mois] += non_renouvelable

        except (ValueError, KeyError) as e:
            # Gestion des erreurs (par ex. valeurs manquantes ou format incorrect)
            print(f"Erreur dans la ligne: {row}. Erreur: {e}")
            continue

# Calcul des proportions pour chaque mois
mois = list(renouvelable_mois.keys())
proportions_renouvelable = []
proportions_non_renouvelable = []

for m in mois:
    total = renouvelable_mois[m] + non_renouvelable_mois[m]
    proportions_renouvelable.append(renouvelable_mois[m] / total * 100)  
    proportions_non_renouvelable.append(non_renouvelable_mois[m] / total * 100)

# Affichage des proportions par mois
plt.figure(figsize=(10, 6))
plt.plot(mois, proportions_renouvelable, label='Renouvelables', color='b')
plt.plot(mois, proportions_non_renouvelable, label='Non-renouvelables', color='r')
plt.xlabel('Mois')
plt.ylabel('Proportion (%)')
plt.title('Proportions d\'énergies renouvelables et non-renouvelables par mois en 2022')
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Création d'un graphique en camembert pour les totaux annuels
total_renouvelable = sum(renouvelable_mois.values())
total_non_renouvelable = sum(non_renouvelable_mois.values())

labels = ['Renouvelables', 'Non-renouvelables']
sizes = [total_renouvelable, total_non_renouvelable]
colors = ['#66b3ff', '#ff6666']

plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Part des énergies renouvelables et non-renouvelables en 2022')
plt.axis('equal')  # Pour que le graphique soit un cercle
plt.show()
