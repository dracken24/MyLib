from init import dict_books, dict_users, loans_list_dict

import csv
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# ****************************************** book.csv ******************************************
def save_books_csv(file="books.csv"):
	"""Sauvegarde les livres dans un fichier CSV"""
	with open(file, "w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["Titre", "Auteur", "Genre", "Exemplaires", "Emprunts"])
		for titre, book in dict_books.items():
			writer.writerow([
				titre,
				book['Auteur'],
				book['Genre'],
				book['Exemplaires'],
				book['Emprunts']
			])
	print("\nLes livres ont été sauvegardés avec succès.")


# Charger les livres depuis un fichier CSV
def load_books_csv(file="books.csv"):
	"""Charge les livres depuis un fichier CSV"""
	if os.path.exists(file):
		with open(file, "r", encoding="utf-8") as f:
			# Vérifier si le fichier n'est pas vide
			if os.path.getsize(file) > 0:
				reader = csv.reader(f)
				headers = next(reader)  # Lire la première ligne pour les en-têtes
				dict_books.clear()
				for row in reader:
					if len(row) >= 5:  # Vérifier qu'on a assez de colonnes
						titre = row[0]
						dict_books[titre] = {
							'Auteur': row[1],
							'Genre': row[2],
							'Exemplaires': int(row[3]),
							'Emprunts': int(row[4])
						}
				return None
			else:
				print("\nLe fichier CSV est vide. Un nouveau fichier sera créé lors de la sauvegarde.")
				return None
	else:
		print("\nAucun fichier CSV trouvé. Un nouveau fichier sera créé lors de la sauvegarde.")
		return None
	
# ****************************************** users.csv *****************************************

def save_users_csv(file="users.csv"):
	"""Sauvegarde les utilisateurs dans un fichier CSV"""
	with open(file, "w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["ID", "Nom", "Prénom", "Email", "Téléphone", "Emprunts", "ListeLivreLu"])
		for user_id, user in dict_users.items():
			writer.writerow([
				user_id,
				user['Nom'],
				user['Prénom'],
				user['Email'],
				user['Téléphone'],
				user['Emprunts'],
				";".join(user['ListeLivreLu']) if user['ListeLivreLu'] else ""
			])

def load_users_csv(file="users.csv"):
	"""Charge les utilisateurs depuis un fichier CSV"""
	if os.path.exists(file):
		with open(file, "r", encoding="utf-8") as f:
			reader = csv.DictReader(f)  # Utiliser DictReader pour lire directement en dictionnaire
			dict_users.clear()
			for row in reader:
				user_id = row['ID']
				dict_users[user_id] = {
					'Nom': row['Nom'],
					'Prénom': row['Prénom'],
					'Email': row['Email'],
					'Téléphone': row['Téléphone'],
					'Emprunts': int(row['Emprunts']),
					'ListeLivreLu': row['ListeLivreLu'].split(";") if row['ListeLivreLu'] else []
				}
		return None
	else:
		# print("\nAucun fichier CSV trouvé. Création d'un nouveau fichier lors de la sauvegarde.")
		return "\nAucun fichier CSV trouvé. Création d'un nouveau fichier lors de la sauvegarde."

# ****************************************** loans.csv ******************************************

def save_loans_csv(file="loans.csv"):
	"""Sauvegarde les informations des emprunts dans un fichier CSV."""
	with open(file, "w", newline="", encoding="utf-8") as f:
		writer = csv.writer(f)
		writer.writerow(["Utilisateur_ID", "Livre", "Date_Emprunt", "Date_Retour"])
		for loan_data in loans_list_dict:
			writer.writerow([
				loan_data['Utilisateur_ID'],
				loan_data['Livre'],
				loan_data['Date_Emprunt'],
				loan_data['Date_Retour']
			])
	print("\nLes emprunts ont été sauvegardés avec succès.")


# Charger les emprunts depuis un fichier CSV
def load_loans_csv(file="loans.csv"):
	"""Charge les informations des emprunt depuis un fichier CSV."""
	if os.path.exists(file):
		with open(file, "r", encoding="utf-8") as f:
			reader = csv.reader(f)
			next(reader)  # Skip header row
			loans_list_dict.clear()
			for row in reader:
				if len(row) >= 4:  # Vérifier qu'on a assez de colonnes
					if row[3] == "":
						loans_list_dict.append({
						'Utilisateur_ID': row[0],
						'Livre': row[1],
						'Date_Emprunt': row[2],
						'Date_Retour': None})
					else:
						loans_list_dict.append({
						'Utilisateur_ID': row[0],
						'Livre': row[1],
						'Date_Emprunt': row[2],
						'Date_Retour': row[3]})
		print("\nLes emprunts ont été chargés depuis le fichier CSV.")
		return None
	else:
		# print("\nAucun fichier CSV trouvé. Création d'un nouveau fichier lors de la sauvegarde.")
		return "\nAucun fichier CSV trouvé. Création d'un nouveau fichier lors de la sauvegarde."
