import sys
import os
from init import dict_books, dict_users, loans_list_dict
from datetime import datetime, timedelta
from csv_control import save_loans_csv, save_books_csv, save_users_csv
from utility import our_input, EXIT_CODE, BASE_CHOICE_STR
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

# Affichage for DEBUG
def afficher_users():
	print("\n\033[1m\033[4m--List of Users--\033[0m")
	for user in dict_users.keys():
		print(f'\nID: {user}')
		print(f'Nom: {dict_users[user]["Nom"]}')
		print(f'Prénom: {dict_users[user]["Prénom"]}')
		print(f'Email: {dict_users[user]["Email"]}')
		print(f'Téléphone: {dict_users[user]["Téléphone"]}')
		print(f'Emprunts: {dict_users[user]["Emprunts"]}')
		print(f'Liste Livre Lu:')
		#print(f'ListeLivreLu: {dict_users[user]["ListeLivreLu"]}')
		for livre in dict_users[user]["ListeLivreLu"]:
			print(f' - {livre}')
def afficher_books():
	print("\n\033[1m\033[4m--List of Books--\033[0m")
	for book in dict_books.keys():
		print(f"\nLivre: {book}")
		print(f"Auteur: {dict_books[book]["Auteur"]}")
		print(f"Genre: {dict_books[book]["Genre"]}")
		print(f"Exemplaires: {dict_books[book]["Exemplaires"]}")
		print(f"Emprunts: {dict_books[book]["Emprunts"]}")
def afficher_loans():
	print("\n\033[1m\033[4m--List of Loans--\033[0m")
	for loan in loans_list_dict:
		print(f"\nUtilisateur_ID: {loan["Utilisateur_ID"]}")
		print(f"Livre: {loan["Livre"]}")
		print(f"Date_Emprunt: {loan["Date_Emprunt"]}")
		print(f"Date_Retour: {loan["Date_Retour"]}")

# Rechercher of dicts
def rechercher_user(id):
	for user in dict_users:
		if user == id:
			return user
	print(f"\033[91mAuncun utilisateur sous ce code d'identité {id} retrouvé.\033[0m")
	return None
def rechercher_livre(titre):
	for livre in dict_books:
		if livre == titre:
			return livre
	return f'\033[91mAuncun livre avec le titre "{titre}" retrouvé.\033[0m'

# Retour ou Emprunt
def retour_livre(id, titre):
	for loan in loans_list_dict:
		if id == loan["Utilisateur_ID"] and titre == loan["Livre"] and loan["Date_Retour"] is None:
			# Retourner l'exemplaire
			dict_books[titre]["Exemplaires"] += 1

			# Mettre a jour la date de retour
			loan["Date_Retour"] = datetime.now().strftime('%Y-%m-%d')

			# Calculer Pénalité
			text = (
				f'\nLivre "{titre}" \n'
				f'Emprunté par {dict_users[id]["Prénom"]} {dict_users[id]["Nom"].upper()} \n'
				f'à la date du {loan["Date_Emprunt"]}: \n'
				f'de retour le {loan["Date_Retour"]}.\n'
				f'\nCalculons la pénalité . . .\n'
			)
			our_input(text, 3)

			date = loan["Date_Emprunt"]
			date_conv = datetime.strptime(date, "%Y-%m-%d")
			date_limite = date_conv + timedelta(days=14)

			return_text = ""

			if datetime.now() > date_limite:
				jours_retard = (datetime.now() - date_limite).days
				penalite = jours_retard * 1.25
				return_text = f"\n{jours_retard} jour(s) en retard...\n"
				return_text += f"Pénalité: {penalite:.2f}$\n\n"
			else:
				return_text = "\nRetour à temps : pas de pénalité.\n\n"
			return return_text
	return "\nPas d'emprunt en cours retrouvé. ou livre inexistant\n\n"
def emprunter_livre(id, titre):
	# Verifier si User a deja le livre sous emprunt en cours
	for loan in loans_list_dict:
		if id == loan["Utilisateur_ID"] and titre == loan["Livre"] and loan["Date_Retour"] is None:
			return "\nVous avez déjà ce livre sous emprunt\n\n"
	
	# protection pour chercher un livre qui n'existe peut etre pas
	found = None
	for b in dict_books:
		if b == titre:
			found = dict_books[titre]

	# Verifier le nombre d'exemplaire disponibles
	if found != None:
		if dict_books[titre]["Exemplaires"] <= 0:
			return "\nIl n'y a plus d'exemplaires disponibles à ce moment.\n\n"
		our_input("--- Emprunt ou Retour de Livres ---\n\n" + "Ce livre est disponible à emprunter", 3)
		# sleep(1)

		# Enlever l'exemplaire
		dict_books[titre]["Exemplaires"] -= 1

		# Creer Date_Emprunt a jour
		date_emp = datetime.now().strftime('%Y-%m-%d')

		# Ajouter l'emprunt dans dict_books
		dict_books[titre]["Emprunts"] += 1

		# Ajouter livre dans listeLu si nouveau
		catch_return = ajouter_livreLu(id, titre)

		# Creer un emprunt pour ajouter a la list loans_list_dict
		loans_list_dict.append({"Utilisateur_ID": id, "Livre": titre, "Date_Emprunt": date_emp, "Date_Retour": None})

		date_exp = (datetime.strptime(date_emp, "%Y-%m-%d") + timedelta(days=14)).strftime('%Y-%m-%d')

		text = (
			f'\nLivre "{titre}" \n'
			f'Emprunté par {dict_users[id]["Prénom"]} {dict_users[id]["Nom"].upper()} \n'
			f'à la date du {loan["Date_Emprunt"]}: \n'
			f'à retourner avant le {date_exp}.\n'
		)
		# our_input(text, 3)

		# return catch_return + f'Livre "{titre}" emprunté avec succès.\n\n'
		# return text + catch_return + f'Livre "{titre}" emprunté avec succès.\n\n'
		return f'\nLivre "{titre}" emprunté avec succès.\n' + text + catch_return + '\n'
	else:
		return "\nLivre inexistant dans la bibliothèque\n\n"

def ajouter_livreLu(id, livre):
	dict_users[id]["ListeLivreLu"]
	if livre in dict_users[id]["ListeLivreLu"]:
		return f"\n{dict_users[id]["Prénom"]} a déjà lu ce livre : Liste de livres lus non changée.\n"
		# return f"\nLivre Deja lu\n"
	else:
		dict_users[id]["ListeLivreLu"].append(livre)
		return f"\n{dict_users[id]["Prénom"]} n'a pas lu ce livre : Liste de livres lus mis à jour.\n"
		# return f"\nLivre no lu avant\n"

# Record a loan or return - MAIN FUNCTION HERE!
def emprunt_retour_books(button: str):
	# print(f"{button} button Hit Action 3")
	affich_text = "--- Gestion des emprunts ou retours ---\n"
	catch_return = ""

	text = (
		"\n1. Emprunter un livre\n"
		"2. Retourner un livre\n"
		"3. Quitter\n"
	)

	while True:
		choix = our_input(affich_text + text + "\nChoisissez une option (1-3) :")
		#choix = our_input(affich_text + text + catch_return)
		if (choix == EXIT_CODE):
			return

		if choix == "1":
			affich_text = "--- Emprunter un livre en cours ---\n"
			print("\033[94mVous avez choisi: Emprunt\033[0m")
			break
		if choix == "2":
			affich_text = "--- Retourner un livre en cours ---\n"
			print("\033[95mVous avez choisi: Retour\033[0m")
			break
		if choix == "3" or choix.lower() == "stop":
			return

		# DEBUG MODE
		if choix.lower() == "loans" or choix.lower() == "l":
			afficher_loans()
		if choix.lower() == "books" or choix.lower() == "b":
			afficher_books()
		if choix.lower() == "users" or choix.lower() == "u":
			afficher_users()

		else:
			catch_return = "\nChoix invalide, réessayez."

	# Trouver le client
	while True:
		text_u = "\n--Liste des utilisateurs--\n"	# Pour afficher une liste des utilisateurs
		for user in dict_users.keys():
			text_u += f'* {user} - {dict_users[user]["Prénom"]} {dict_users[user]["Nom"].upper()}\n'

		client = our_input(affich_text + "\nEntrez le code d'identité de l'utilisateur : \n" + text_u + catch_return)
		if (client == EXIT_CODE):
			return
		client_verifiee = rechercher_user(client)
		if not client_verifiee:
			catch_return = f"\nAuncun utilisateur sous ce code d'identité {client} retrouvé."
		elif client_verifiee:
			catch_return += f'\nUtilisateur {dict_users[client_verifiee]["Prénom"]} {dict_users[client_verifiee]["Nom"].upper()} trouvé.\n'
			break
		elif client.lower() == "stop": # To exit loop
			break
	# Trouver le livre
	if client_verifiee:
		while True:
			text_b = "\n\n--Liste des livres--\n"
			for book in dict_books.keys():
				text_b += f'* {book}\n'

			livre = our_input(affich_text + catch_return + "\nEntrez le titre du livre : " + text_b).title()
			catch_return = ""
			if (livre == EXIT_CODE):
				return
			livre_verifiee = rechercher_livre(livre)
			if livre_verifiee:
				catch_return = f'\033[92mLe livre "{livre_verifiee}" trouvé.\033[0m'
				break
			elif livre.lower() == "stop": # To exit loop
				break

	if client_verifiee and livre_verifiee:
		if choix == "1":
			#print("\033[94mIt's a boy! (Emprunt)\033[0m")  # This line is a joke, for debuging
			catch_return = emprunter_livre(client_verifiee, livre_verifiee)
		if choix == "2":
			#print("\033[95mIt's a girl! (Retour)\033[0m")  # This line is a joke, for debuging
			catch_return = retour_livre(client_verifiee, livre_verifiee)
		save_books_csv()
		save_users_csv()
		save_loans_csv()

	our_input(affich_text + catch_return + BASE_CHOICE_STR)
	# print(f"{button} button Hit Action 11 input text")