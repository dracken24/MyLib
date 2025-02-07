import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# import csv
import re

from init import dict_users, loans_list_dict
from csv_control import save_users_csv
from utility import our_input, EXIT_CODE, BASE_CHOICE_STR

def add_remove_users(button: str):
	"""Gestion des utilisateurs quand le bouton est cliqué"""
	menu()

def add_user():
	"""Ajoute un nouvel utilisateur"""
	# print("\n--- Ajouter un nouvel utilisateur ---")
	prenom = our_input("Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nPrénom : ")
	if (prenom == EXIT_CODE):
		return
	# prenom = input("Prénom : ")
	nom = our_input("Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nNom : ")
	if (nom == EXIT_CODE):
		return EXIT_CODE
	# nom = input("Nom : ")
	
	invalid = ""
	while True:
		email = our_input(f"Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nEmail : {invalid}")
		if (email == EXIT_CODE):
			return EXIT_CODE
		# email = input("Email (format: exemple@gmail.com) : ")
		if re.match(r"[^@]+@[^@]+\.[^@]+", email):
			break
		# print("\u274C Email invalide")
		invalid = "Email invalide"

	invalid = ""
	while True:
		telephone = our_input(f"Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nTéléphone (format: xxx-xxx-xxxx) : {invalid}")
		if (telephone == EXIT_CODE):
			return EXIT_CODE
		# telephone = input("Téléphone (format: xxx-xxx-xxxx) : ")
		if re.match(r"\d{3}-\d{3}-\d{4}", telephone):
			break
		# print("\u274C Numéro de téléphone invalide")
		invalid = "Numéro de téléphone invalide"

	# Générer un nouvel ID
	if not dict_users:
		new_id = "1"
	else:
		last_id = max(int(user_id.replace('U', '')) for user_id in dict_users.keys())
		new_id = f"{last_id + 1}"


	dict_users[new_id] = {
		'Nom': nom,
		'Prénom': prenom,
		'Email': email,
		'Téléphone': telephone,
		'Emprunts': 0,
		'ListeLivreLu': []
	}
	
	print(f"\n\033[92mUtilisateur ajouté avec succès (ID: {new_id})\033[0m")
	save_users_csv()

def remove_user():
	"""Supprime un utilisateur"""
	base_str = (
		"--- Gestion des utilisateurs ---\n"
		"Vous avez choisi: Supprimer un utilisateur\n\n"
	)
	user_id = our_input(base_str + "ID utilisateur à supprimer (ex: 1) : ")
	if (user_id == EXIT_CODE):
		return EXIT_CODE
	# user_id = input("ID utilisateur à supprimer (ex: 1) : ").upper()
	
	if user_id in dict_users:
		user = dict_users[user_id]
		confirmation = our_input(base_str + (
			f"Utilisateur trouvé : {user['Prénom']} {user['Nom']}"
			"\n\nConfirmer la suppression ? (oui/non) : "
		))
		if (confirmation == EXIT_CODE):
			return EXIT_CODE
		# print(f"Utilisateur trouvé : {user['Prénom']} {user['Nom']}")
		# confirmation = our_input(base_str + "Confirmer la suppression ? (oui/non) : ")
		# if (confirmation == EXIT_CODE):
		# 	return EXIT_CODE
		# confirmation = input("Confirmer la suppression ? (oui/non) : ").lower()
		if confirmation == "oui":
			del dict_users[user_id]
			# print(f"\nUtilisateur {user_id} supprimé.")
			save_users_csv()
			return f"Utilisateur {user_id} supprimé.\n\n"
		else:
			return f"Utilisateur {user_id} non supprimé.\n\n"
	else:
		# print(f"\nUtilisateur {user_id} non trouvé.")
		return f"Utilisateur {user_id} non trouvé.\n\n"


def display_users():
	"""Affiche tous les utilisateurs"""
	return_text = "--- Gestion des utilisateurs ---\n\nVous avez choisi: Afficher tous les utilisateurs\n"
	if dict_users:
		# print("\n--- Liste des utilisateurs ---")
		return_text += "\n--- Liste des utilisateurs ---\n"
		for user_id, user in dict_users.items():
			# print("-" * 30)
			return_text += "-" * 30 + "\n"
			# print(f"ID : {user_id}")
			return_text += f"ID : {user_id}"
			# print(f"Nom : {user['Nom']}")
			return_text += f"Nom : {user['Nom']}\n"
			# print(f"Prénom : {user['Prénom']}")
			return_text += f"Prénom : {user['Prénom']}\n"
			# print(f"Email : {user['Email']}")
			return_text += f"Email : {user['Email']}\n"
			# print(f"Téléphone : {user['Téléphone']}")
			return_text += f"Téléphone : {user['Téléphone']}\n"
			# print(f"Nombre d'emprunts : {user['Emprunts']}")
			return_text += f"Nombre d'emprunts : {user['Emprunts']}\n"
			if user['ListeLivreLu']:
				# print("Livres lus :")
				return_text += "Livres lus :\n"
				for livre in user['ListeLivreLu']:
					# print(f"- {livre}")
					return_text += f"- {livre}\n"
			# print("-" * 30)
			return_text += "-" * 30 + "\n\n"
		return return_text
	else:
		# print("\nAucun utilisateur enregistré.")
		return_text += "Aucun utilisateur enregistré.\n\n"
		return return_text

def mettre_a_jour_emprunts_utilisateurs():
	"""Met à jour les emprunts des utilisateurs à partir de la liste des prêts"""
	for loan in loans_list_dict:
		user_id = loan.get("user_id")
		if user_id in dict_users:
			dict_users[user_id]['Emprunts'] = loan.get("Emprunts", 0)
			dict_users[user_id]['Livres'] = loan.get("Livres", [])

def menu():
	"""Menu interactif pour la gestion des utilisateurs"""
	exit_str = f"--- Gestion des utilisateurs ---\n\nAu revoir!\n\n" + BASE_CHOICE_STR
	invalid = ""
	
	text: str = (
		"--- Gestion des utilisateurs ---\n\n"
		"1. Ajouter un utilisateur\n"
		"2. Supprimer un utilisateur\n"
		"3. Afficher tous les utilisateurs\n"
		"4. Quitter\n"
	)

	while True:
		# print("\n--- Gestion des utilisateurs ---")
		# print("1. Ajouter un utilisateur")
		# print("2. Supprimer un utilisateur")
		# print("3. Afficher tous les utilisateurs")
		# print("4. Quitter")

		choice = our_input(invalid + text + "\nChoisissez une option (1-4) :")
		if (choice == EXIT_CODE):
			return
		# choice = input("Choisissez une option (1-4) : ")

		if choice == "1":
			# print("\n\033[94mVous avez choisi: Ajouter un utilisateur\033[0m")
			if (add_user() == EXIT_CODE):
				return
			our_input(exit_str)
			break
		elif choice == "2":
			# print("\n\033[94mVous avez choisi: Supprimer un utilisateur\033[0m")
			return_text = remove_user()
			if (return_text == EXIT_CODE):
				return
			our_input("--- Gestion des utilisateurs ---\n\n" + return_text + BASE_CHOICE_STR)
			break
		elif choice == "3":
			# print("\n\033[94mVous avez choisi: Afficher tous les utilisateurs\033[0m")
			return_user = display_users()
			if (return_user == EXIT_CODE):
				return
			our_input(return_user + BASE_CHOICE_STR)
			break
		elif choice == "4":
			# print("\n\033[94mVous avez choisi: Quitter\033[0m")
			# print("Au revoir!")
			our_input((
				"--- Gestion des utilisateurs ---\n\n"
				"Vous avez choisi: Quitter\n\n"
				"Au revoir!\n\n"
			) + BASE_CHOICE_STR)
			break
		else:
			# print("Option invalide. Veuillez réessayer.")
			invalid = "Option invalide. Veuillez réessayer."



