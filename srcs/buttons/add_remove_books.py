from init import dict_books
from csv_control import save_books_csv
from utility import our_input, EXIT_CODE, BASE_CHOICE_STR

def add_remove_books(button: str):
	"""Gestion des livres quand le bouton est cliqué"""
	menu()
	return

def remove_book_button(button):
	print(f"{button} button Hit Action 1")

# Ajouter un livre à la bibliothèque
def add_book():
	"""Ajoute un nouveau livre à la bibliothèque"""
	print("\n--- Ajouter un nouveau livre ---")
	book_name = our_input("--- Ajouter un nouveau livre ---\nTitre du livre : ")
	if (book_name == EXIT_CODE):
		return EXIT_CODE

	author = our_input("--- Ajouter un nouveau livre ---\nAuteur : ")
	if (author == EXIT_CODE):
		return EXIT_CODE

	genre = our_input("--- Ajouter un nouveau livre ---\nGenre : ")
	if (genre == EXIT_CODE):
		return EXIT_CODE
	
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
	text_affich: str = "--- Gestion des livres ---\n\n"
	if dict_books:
		# print("\n--- Liste des livres dans la bibliothèque ---")
		text_affich += "--- Liste des livres dans la bibliothèque ---\n\n"
		for book_name, book in dict_books.items():
			text_affich += "-" * 30
			text_affich += f"\nTitre : {book_name}"
			text_affich += f"\nAuteur : {book['Auteur']}"
			text_affich += f"\nGenre : {book['Genre']}"
			text_affich += f"\nCopies disponibles : {book['Exemplaires']}"
			text_affich += f"\nNombre total d'emprunts : {book['Emprunts']}\n"
			text_affich += "-" * 30 + "\n"
	else:
		text_affich += "\nAucun livre dans la bibliothèque.\n"
	
	return text_affich + "\n" + BASE_CHOICE_STR

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
			return BASE_CHOICE_STR

		if choice == "1":
			# print("\n\033[94mVous avez choisi: Ajouter un livre\033[0m")
			add_book()
			return BASE_CHOICE_STR
		elif choice == "2":
			# print("\n\033[94mVous avez choisi: Supprimer un livre\033[0m")
			book_name = our_input("--- Gestion des livres ---\nVous avez choisi: Supprimer un livre\n\nTitre du livre à supprimer :")
			if (book_name == EXIT_CODE):
				return BASE_CHOICE_STR
			# book_name = input("Titre du livre à supprimer : ")
			return_remove = remove_book(book_name)
			our_input(f"--- Gestion des livres ---\n\n{return_remove}\n\nVeuillez cliquer sur un boutton pour faire un choix")
			return BASE_CHOICE_STR
		elif choice == "3":
			# print("\n\033[94mVous avez choisi: Afficher tous les livres\033[0m")
			return_text = display_books()
			our_input(return_text)
			return
		elif choice == "4":
			# print("\nMerci d'avoir utilisé le gestionnaire de livres.")
			our_input(f"--- Gestion des livres ---\n\nMerci d'avoir utilisé le gestionnaire de livres.\n\n" + BASE_CHOICE_STR)
			return
		else:
			# print("Option invalide. Veuillez réessayer.")
			invalid = "Option invalide. Veuillez réessayer.\n\n"


if __name__ == "__main__":
	# Charger les livres au démarrage
	# load_books_csv()
	
	# Lancer le menu principal
	menu()
