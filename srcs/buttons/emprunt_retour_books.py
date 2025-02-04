from init import dict_button, dict_books, dict_users, loans_list_dict
import csv
import os
from time import sleep
from datetime import datetime, timedelta
from buttons.add_remove_users import load_users_csv, save_users_csv
from buttons.add_remove_books import load_books_csv, save_books_csv
from utility import our_input, EXIT_CODE, BASE_CHOICE_STR

WIP = "\n\033[93m\033[1mWIP\033[0m"

# Afficher of dicts
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
	#print("\n")

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

def afficher_livres_simple():
	print("\n\033[1m\033[4m--List of Books--\033[0m")
	for book in dict_books.keys():
		print(f'- {book}')

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
	# print(f'\033[91mAuncun livre avec le titre "{titre}" retrouvé.\033[0m')
	return f'\033[91mAuncun livre avec le titre "{titre}" retrouvé.\033[0m'

def retour_livre(id, titre):
	for loan in loans_list_dict:
		if id == loan["Utilisateur_ID"] and titre == loan["Livre"] and loan["Date_Retour"] is None:
			# Retourner l'exemplaire
			dict_books[titre]["Exemplaires"] += 1

			# Mettre a jour la date de retour
			loan["Date_Retour"] = datetime.now().strftime('%Y-%m-%d')

			# Calculer Pénalité
			text = (
				f'Livre "{titre}" \n'
				f'Emprunté par {dict_users[id]["Nom"]} \n'
				f'à la date du {loan["Date_Emprunt"]}: \n'
				f'de retour le {loan["Date_Retour"]}.\n'
			)
			our_input(text, 1)
			# print(f'Livre "{titre}" \nEmprunté par {dict_users[id]["Nom"]} \nà la date du {loan["Date_Emprunt"]}: \nde retour le {loan["Date_Retour"]}.')
			# print("\033[93mCalculons la pénalité . . . \033[0m")
			# sleep(1)

			date = loan["Date_Emprunt"]
			date_conv = datetime.strptime(date, "%Y-%m-%d")
			date_limite = date_conv + timedelta(days=14)

			return_text = ""

			if datetime.now() > date_limite:
				jours_retard = (datetime.now() - date_limite).days
				penalite = jours_retard * 1.25
				return_text = f"\n{jours_retard} jour(s) en retard...\n"
				return_text += f"Pénalité: {penalite:.2f}$\n\n"
				# print(f"\033[91m{jours_retard} jour(s) en retard...")
				# print(f"Pénalité: {penalite:.2f}$\033[0m")
			else:
				return_text = "\nRetour a temps! :)\n\n"
				# print(f"\033[92mRetour a temps! :)\033[0m")
			return return_text
	# print(f"\033[91mPas d'emprunt en cours retrouvé.\033[0m")
	return "\nPas d'emprunt en cours retrouvé. ou livre inexistant\n\n"

def emprunter_livre(id, titre):
	# Verifier si User a deja le livre sous emprunt en cours
	for loan in loans_list_dict:
		if id == loan["Utilisateur_ID"] and titre == loan["Livre"] and loan["Date_Retour"] is None:
			# print("Vous avez deja ce livre sous emprunt")
			return "\nVous avez deja ce livre sous emprunt\n"
	
	# protection pour chercher un livre qui n'existe peut etre pas
	found = None
	for b in dict_books:
		if b == titre:
			found = dict_books[titre]

	# Verifier le nombre d'exemplaire disponibles
	if  found != None:
		if dict_books[titre]["Exemplaires"] <= 0:
			return "\nIl n'y a plus d'exemplaires disponibles à ce moment.\n\n"
		our_input("--- Emprunt ou Retour de Livres ---\n\n" + "\nCe livre est disponible à emprunter.", 1)
		# print("Ce livre est disponible à emprunter.")
		# sleep(1)

		# Enlever l'exemplaire
		dict_books[titre]["Exemplaires"] -= 1
		#print(f"Exemplaires mise a jour {dict_books[titre]["Exemplaires"]}")

		# Creer Date_Emprunt a jour
		date_emp = datetime.now().strftime('%Y-%m-%d')
		#print(f"Date d'emprunt a jour {date_emp}")

		# Ajouter l'emprunt dans dict_books
		dict_books[titre]["Emprunts"] += 1
		#print(f"Ajouter Emprunts pour livre {dict_books[titre]["Emprunts"]}")

		# Ajouter livre dans listeLu si nouveau
		catch_return = ajouter_livreLu(id, titre)
		#print(f"Ajouter nouveau dans liste (si nouveau)")
		#print(f"{dict_users[id]["ListeLivreLu"]}")

		# Creer un emprunt pour ajouter a la list loans_list_dict
		loans_list_dict.append({"Utilisateur_ID": id, "Livre": titre, "Date_Emprunt": date_emp, "Date_Retour": None})
		# print(f'Livre "{titre}" emprunté avec succès.')
		return catch_return + f'Livre "{titre}" emprunté avec succès.\n\n'
	else:
		# print("Il n'y a plus d'exemplaires disponibles à ce moment.")
		return "\nLivre inexistant dans la bibliotheque\n\n"

def ajouter_livreLu(id, livre):
	dict_users[id]["ListeLivreLu"]
	if livre in dict_users[id]["ListeLivreLu"]:
		# print("Livre Deja lu")
		return "\nLivre Deja lu\n"
	else:
		dict_users[id]["ListeLivreLu"].append(livre)
		# print("Livre no lu avant")
		return "\nLivre no lu avant\n"

# Record a loan or return - MAIN FUNCTION!
def emprunt_retour_books(button: str):
	# print(f"{button} button Hit Action 3")
	affich_text = "--- Emprunt ou Retour de Livres ---\n"
	catch_return = ""

	load_books_csv()
	load_users_csv()
	load_loans_csv()

	text = (
		"\nCeci est pour un emprunt ou un retour?"
		"\n1. Emprunt\n"
		"2. Retour\n"
		"3. Quitter\n"
	)

	# dict_button[button]["text"] = "WIP\nCeci est pour un emprunt ou un retour?"
	# dict_button[button]["text"] += "\n1. Emprunt\n2. Retour\n3. Quitter"
	while True:
		# print("\033[1mCeci est pour un emprunt ou un retour?\033[0m")
		# print("1. Emprunt")
		# print("2. Retour")
		# print("3. Quitter")
		choix = our_input(affich_text + text + catch_return)
		if (choix == EXIT_CODE):
			return
		# choix = input("\nChoisissez une option : ") # Come back later

		if choix == "1":
			print("\033[94mVous avez choisi: Emprunt\033[0m")
			break
		if choix == "2":
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
			# print("\033[91mChoix invalide, réessayez.\033[0m\n")
	# Trouver le client
	while True:
		client = our_input(affich_text + "\nEntrez le code d'identité de l'utilisateur : \n" + catch_return)
		if (client == EXIT_CODE):
			return
		# client = input("\nEntrez le code d'identité de l'utilisateur : ")
		client_verifiee = rechercher_user(client)
		if not client_verifiee:
			catch_return = f"\nAuncun utilisateur sous ce code d'identité {client} retrouvé."
		elif client_verifiee:
			# print(f'\033[92mUtilisateur {dict_users[client_verifiee]["Prénom"]} {dict_users[client_verifiee]["Nom"].upper()} trouvé.\033[0m')
			catch_return += f'\nUtilisateur {dict_users[client_verifiee]["Prénom"]} {dict_users[client_verifiee]["Nom"].upper()} trouvé.\n'
			break
		elif client.lower() == "stop": # To exit loop
			break
	# Trouver le livre
	if client_verifiee: # Next Step:
		while True: # Trouver le livre
			livre = our_input(affich_text + catch_return + "\nEntrez le titre du livre : ")
			catch_return = ""
			if (livre == EXIT_CODE):
				return
			# livre = input("\nEntrez le titre du livre : ").title()
			livre_verifiee = rechercher_livre(livre)
			if livre_verifiee:
				catch_return = f'\033[92mLe livre "{livre_verifiee}" trouvé.\033[0m'
				# print(f'\033[92mLe livre "{livre_verifiee}" trouvé.\033[0m')
				break
			elif livre.lower() == "stop": # To exit loop
				break

	if client_verifiee and livre_verifiee: # Need to make fucntions for both options
		if choix == "1":
			#print("\033[94mIt's a boy! (Emprunt)\033[0m")  # This line is a joke, should delete later
			catch_return = emprunter_livre(client_verifiee, livre_verifiee)
		if choix == "2":
			#print("\033[95mIt's a girl! (Retour)\033[0m")  # This line is a joke, should delete later
			catch_return = retour_livre(client_verifiee, livre_verifiee)
		save_books_csv()
		save_users_csv()
		save_loans_csv()

	our_input(affich_text + catch_return + BASE_CHOICE_STR)
	# print(f"{button} button Hit Action 11 input text")

#_________________________________________________________________________________
# Sauvegarder les emprunts dans un fichier CSV
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