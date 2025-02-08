import sys
import os
import re

from init import dict_users, loans_list_dict
from csv_control import save_users_csv
from utility import our_input, EXIT_CODE, BASE_CHOICE_STR

def add_remove_users(button: str):
	"""Gestion des utilisateurs quand le bouton est cliqué"""
	menu()

def add_user():
	"""Ajoute un nouvel utilisateur"""
	prenom = our_input("Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nPrénom : ")
	if (prenom == EXIT_CODE):
		return

	nom = our_input("Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nNom : ")
	if (nom == EXIT_CODE):
		return EXIT_CODE
	
	invalid = ""
	while True:
		email = our_input(f"Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nEmail : {invalid}")
		if (email == EXIT_CODE):
			return EXIT_CODE
		if re.match(r"[^@]+@[^@]+\.[^@]+", email):
			break

		invalid = "Email invalide"

	invalid = ""

	while True:
		telephone = our_input(f"Vous avez choisi: Ajouter un utilisateur\n\n--- Ajouter un nouvel utilisateur ---\n\nTéléphone (format: xxx-xxx-xxxx) : {invalid}")
		if (telephone == EXIT_CODE):
			return EXIT_CODE
		if re.match(r"\d{3}-\d{3}-\d{4}", telephone):
			break

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
	
	if user_id in dict_users:
		user = dict_users[user_id]
		confirmation = our_input(base_str + (
			f"Utilisateur trouvé : {user['Prénom']} {user['Nom']}"
			"\n\nConfirmer la suppression ? (oui/non) : "
		))
		if (confirmation == EXIT_CODE):
			return EXIT_CODE
		if confirmation == "oui":
			del dict_users[user_id]
			save_users_csv()
			return f"Utilisateur {user_id} supprimé.\n\n"
		else:
			return f"Utilisateur {user_id} non supprimé.\n\n"
	else:
		return f"Utilisateur {user_id} non trouvé.\n\n"


def display_users():
	"""Affiche tous les utilisateurs"""
	return_text = "--- Gestion des utilisateurs ---\n\nVous avez choisi: Afficher tous les utilisateurs\n"
	if dict_users:
		return_text += "\n--- Liste des utilisateurs ---\n"
		for user_id, user in dict_users.items():
			return_text += "-" * 30 + "\n"
			return_text += f"ID : {user_id}"
			return_text += f"Nom : {user['Nom']}\n"
			return_text += f"Prénom : {user['Prénom']}\n"
			return_text += f"Email : {user['Email']}\n"
			return_text += f"Téléphone : {user['Téléphone']}\n"
			return_text += f"Nombre d'emprunts : {user['Emprunts']}\n"
			if user['ListeLivreLu']:
				return_text += "Livres lus :\n"
				for livre in user['ListeLivreLu']:
					return_text += f"- {livre}\n"
			return_text += "-" * 30 + "\n\n"
		return return_text
	else:
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
		choice = our_input(invalid + text + "\nChoisissez une option (1-4) :")
		if (choice == EXIT_CODE):
			return

		if choice == "1":
			if (add_user() == EXIT_CODE):
				return
			our_input(exit_str)
			break
		elif choice == "2":
			return_text = remove_user()
			if (return_text == EXIT_CODE):
				return
			our_input("--- Gestion des utilisateurs ---\n\n" + return_text + BASE_CHOICE_STR)
			break
		elif choice == "3":
			return_user = display_users()
			if (return_user == EXIT_CODE):
				return
			our_input(return_user + BASE_CHOICE_STR)
			break
		elif choice == "4":
			our_input((
				"--- Gestion des utilisateurs ---\n\n"
				"Vous avez choisi: Quitter\n\n"
				"Au revoir!\n\n"
			) + BASE_CHOICE_STR)
			break
		else:
			invalid = "Option invalide. Veuillez réessayer."
