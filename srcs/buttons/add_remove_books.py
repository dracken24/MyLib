# import sys
# import os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# import csv
from init import dict_button, dict_books, dict_users, loans_list_dict
from csv_control import save_loans_csv, save_books_csv, save_users_csv
from utility import our_input, EXIT_CODE, BASE_CHOICE_STR



def add_remove_books(button: str):
	"""Gestion des livres quand le bouton est cliqué"""
	# text: str = load_books_csv()
	# if (text):  # Charger les livres au début
	# 	our_input(f"--- Gestion des livres ---\n\n{text}\n\n{BASE_CHOICE_STR}")
	# 	return BASE_CHOICE_STR
	
	menu()

	return BASE_CHOICE_STR

def remove_book_button(button):
	print(f"{button} button Hit Action 1")

# Ajouter un livre à la bibliothèque
def add_book():
	"""Ajoute un nouveau livre à la bibliothèque"""
	print("\n--- Ajouter un nouveau livre ---")
	book_name = our_input("--- Ajouter un nouveau livre ---\nTitre du livre : ")
	if (book_name == EXIT_CODE):
		return EXIT_CODE
	# book_name = input("Titre du livre : ")

	author = our_input("--- Ajouter un nouveau livre ---\nAuteur : ")
	if (author == EXIT_CODE):
		return EXIT_CODE
	# author = input("Auteur : ")

	genre = our_input("--- Ajouter un nouveau livre ---\nGenre : ")
	if (genre == EXIT_CODE):
		return EXIT_CODE
	# genre = input("Genre : ")
	
	text = "--- Ajouter un nouveau livre ---\nNombre de copies disponibles : "
	while True:
		try:
			copies = int(our_input(text))
			if (copies == EXIT_CODE):
				return EXIT_CODE
			# copies = int(input("Nombre de copies disponibles : "))
			if copies > 0:
				break
			print("Le nombre de copies doit être positif.")
			text = "--- Ajouter un nouveau livre ---\nLe nombre de copies doit être positif."
		except ValueError:
			print("Veuillez entrer un nombre valide.")
			text = "--- Ajouter un nouveau livre ---\nVeuillez entrer un nombre valide."

	# Créer le dictionnaire du livre avec tous les champs nécessaires
	dict_books[book_name] = {
		'Titre': book_name,
		'Auteur': author,
		'Genre': genre,
		'Exemplaires': copies,
		'Emprunts': 0  # Initialiser le compteur d'emprunts à 0
	}

	print(f"\n\033[92mLe livre '{book_name}' a été ajouté à la bibliothèque.\033[0m")
	save_books_csv()

# Supprimer un livre de la bibliothèque
def remove_book(book_name):
	"""Supprime complètement un livre de la bibliothèque."""
	if book_name in dict_books:
		del dict_books[book_name]
		# print(f"\n\033[91mLe livre '{book_name}' a été supprimé de la bibliothèque.\033[0m")
		save_books_csv()
		return f"Le livre '{book_name}' a été supprimé de la bibliothèque."
	else:
		# print(f"\nLe livre '{book_name}' n'existe pas dans la bibliothèque.")
		return f"Le livre '{book_name}' n'existe pas dans la bibliothèque."

# Afficher tous les livres
def display_books():
	"""Affiche les informations de tous les livres."""
	text_affich: str = "--- Gestion des livres ---\n"
	if dict_books:
		# print("\n--- Liste des livres dans la bibliothèque ---")
		text_affich += "--- Liste des livres dans la bibliothèque ---\n\n"
		for book_name, book in dict_books.items():
			# print("-" * 30)
			text_affich += "-" * 30
			# print(f"Titre : {book_name}")
			text_affich += f"\nTitre : {book_name}"
			# print(f"Auteur : {book['author']}")
			text_affich += f"\nAuteur : {book['Auteur']}"
			# print(f"Genre : {book['genre']}")
			text_affich += f"\nGenre : {book['Genre']}"
			# print(f"Copies disponibles : {book['number_of_copies_available']}")
			text_affich += f"\nCopies disponibles : {book['Exemplaires']}"
			# print(f"Nombre total d'emprunts : {book['total_times_rented']}")
			text_affich += f"\nNombre total d'emprunts : {book['Emprunts']}\n"
			# print("-" * 30)
			text_affich += "-" * 30 + "\n"
	else:
		# print("\nAucun livre dans la bibliothèque.")
		text_affich += "\nAucun livre dans la bibliothèque.\n"
	
	our_input(text_affich + "\n" + BASE_CHOICE_STR)


# def display_total_number_of_books_in_library():
# 	"""Affiche le nombre total d'exemplaires de livres dans la bibliothèque."""
# 	total_books = sum(book['Copies'] for book in dict_books.values())  # Compte les exemplaires
# 	print(f"\nNombre total d'exemplaires dans la bibliothèque : {total_books}")

# Sauvegarder les livres dans un fichier CSV
# def save_books_csv(file="books.csv"):
# 	"""Sauvegarde les livres dans un fichier CSV"""
# 	with open(file, "w", newline="", encoding="utf-8") as f:
# 		writer = csv.writer(f)
# 		writer.writerow(["Titre", "Auteur", "Genre", "Exemplaires", "Emprunts"])
# 		for titre, book in dict_books.items():
# 			writer.writerow([
# 				titre,
# 				book['Auteur'],
# 				book['Genre'],
# 				book['Exemplaires'],
# 				book['Emprunts']
# 			])
# 	print("\nLes livres ont été sauvegardés avec succès.")


# # Charger les livres depuis un fichier CSV
# def load_books_csv(file="books.csv"):
# 	"""Charge les livres depuis un fichier CSV"""
# 	if os.path.exists(file):
# 		with open(file, "r", encoding="utf-8") as f:
# 			# Vérifier si le fichier n'est pas vide
# 			if os.path.getsize(file) > 0:
# 				reader = csv.reader(f)
# 				headers = next(reader)  # Lire la première ligne pour les en-têtes
# 				dict_books.clear()
# 				for row in reader:
# 					if len(row) >= 5:  # Vérifier qu'on a assez de colonnes
# 						titre = row[0]
# 						dict_books[titre] = {
# 							'Auteur': row[1],
# 							'Genre': row[2],
# 							'Exemplaires': int(row[3]),
# 							'Emprunts': int(row[4])
# 						}
# 				return None
# 			else:
# 				print("\nLe fichier CSV est vide. Un nouveau fichier sera créé lors de la sauvegarde.")
# 				return None
# 	else:
# 		print("\nAucun fichier CSV trouvé. Un nouveau fichier sera créé lors de la sauvegarde.")
# 		return None

# Menu principal pour gérer les livres
def menu():
	"""Menu interactif pour ajouter, supprimer et afficher des livres."""
	text = (
		"--- Gestion des livres ---\n\n"
		"1. Ajouter un livre\n2. Supprimer un livre\n"
		"3. Afficher tous les livres\n"
		"4. Quitter\n"
	)
	invalid = ""

	while True:
		# choice = input("Choisissez une option (1-4) : ")
		choice = our_input(invalid + text + "\nChoisissez une option (1-4) :")
		if (choice == EXIT_CODE):
			return

		if choice == "1":
			# print("\n\033[94mVous avez choisi: Ajouter un livre\033[0m")
			add_book()
			return
		elif choice == "2":
			# print("\n\033[94mVous avez choisi: Supprimer un livre\033[0m")
			book_name = our_input("--- Gestion des livres ---\nVous avez choisi: Supprimer un livre\n\nTitre du livre à supprimer :")
			if (book_name == EXIT_CODE):
				return
			# book_name = input("Titre du livre à supprimer : ")
			return_remove = remove_book(book_name)
			our_input(f"--- Gestion des livres ---\n\n{return_remove}\n\nVeuillez cliquer sur un boutton pour faire un choix")
			return
		elif choice == "3":
			# print("\n\033[94mVous avez choisi: Afficher tous les livres\033[0m")
			display_books()
			return
		
		elif choice == "4":
			# print("\nMerci d'avoir utilisé le gestionnaire de livres.")
			our_input(f"--- Gestion des livres ---\n\nMerci d'avoir utilisé le gestionnaire de livres.\n\n" + BASE_CHOICE_STR)
			break
		else:
			# print("Option invalide. Veuillez réessayer.")
			invalid = "Option invalide. Veuillez réessayer.\n\n"


if __name__ == "__main__":
	# Charger les livres au démarrage
	# load_books_csv()
	
	# Lancer le menu principal
	menu()
