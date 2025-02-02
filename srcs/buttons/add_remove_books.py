import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_button, dict_books, dict_users, loans_list_dict
import csv

def add_remove_books(button: str):
    text: str = "--- Gestion des livres ---\n1 . Ajouter un livre\n2. Supprimer un livre\n3. Afficher tous les livres\n4. Quitter\n"
    dict_button[button]["text"] = text

def remove_book_button(button):
    print(f"{button} button Hit Action 1")




# Ajouter un livre à la bibliothèque
def add_book():
    """Ajoute un nouveau livre à la bibliothèque"""
    print("\n--- Ajouter un nouveau livre ---")
    book_name = input("Titre du livre : ")
    author = input("Auteur : ")
    genre = input("Genre : ")
    
    while True:
        try:
            copies = int(input("Nombre de copies disponibles : "))
            if copies > 0:
                break
            print("Le nombre de copies doit être positif.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

    # Créer le dictionnaire du livre avec tous les champs nécessaires
    dict_books[book_name] = {
        'Titre': book_name,
        'Auteur': author,
        'Genre': genre,
        'Copies': copies,
        'Emprunts': 0  # Initialiser le compteur d'emprunts à 0
    }

    print(f"\n\033[92mLe livre '{book_name}' a été ajouté à la bibliothèque.\033[0m")
    save_books_csv()


# Supprimer un livre de la bibliothèque
def remove_book(book_name):
    """Supprime complètement un livre de la bibliothèque."""
    if book_name in dict_books:
        del dict_books[book_name]
        print(f"\n\033[91mLe livre '{book_name}' a été supprimé de la bibliothèque.\033[0m")
        save_books_csv()
    else:
        print(f"\nLe livre '{book_name}' n'existe pas dans la bibliothèque.")


# Afficher tous les livres
def display_books():
    """Affiche les informations de tous les livres."""
    if dict_books:
        print("\n--- Liste des livres dans la bibliothèque ---")
        for book in dict_books.values():
            print("-" * 30)
            print(f"Titre : {book['Titre']}")
            print(f"Auteur : {book['Auteur']}")
            print(f"Genre : {book['Genre']}")
            print(f"Copies disponibles : {book['Copies']}")
            print(f"Nombre total d'emprunts : {book['Emprunts']}")
            print("-" * 30)
    else:
        print("\nAucun livre dans la bibliothèque.")


def display_total_number_of_books_in_library():
    """Affiche le nombre total d'exemplaires de livres dans la bibliothèque."""
    total_books = sum(book['Copies'] for book in dict_books.values())  # Compte les exemplaires
    print(f"\nNombre total d'exemplaires dans la bibliothèque : {total_books}")



# Sauvegarder les livres dans un fichier CSV
def save_books_csv(file="books.csv"):
    """Sauvegarde les informations des livres dans un fichier CSV."""
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["book_name", "author", "genre", "number_of_copies_available", "total_times_rented"])
        for book in dict_books.values():
            writer.writerow([
                book['Titre'],
                book['Auteur'],
                book['Genre'],
                book['Copies'],
                book['Emprunts']
            ])
    print("\nLes livres ont été sauvegardés avec succès.")


# Charger les livres depuis un fichier CSV
def load_books_csv(file="books.csv"):
    """Charge les informations des livres depuis un fichier CSV."""
    global dict_books
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)  # Skip header row
            dict_books.clear()
            for row in reader:
                if len(row) >= 5:  # Vérifier qu'on a assez de colonnes
                    titre, auteur, genre, copies, emprunts = row
                    dict_books[titre] = {
                        'Titre': titre,
                        'Auteur': auteur,
                        'Genre': genre,
                        'Copies': int(copies),
                        'Emprunts': int(emprunts)
                    }
        print("\nLes livres ont été chargés depuis le fichier CSV.")
    else:
        print("\nAucun fichier CSV trouvé. Création d'un nouveau fichier lors de la sauvegarde.")

# Menu principal pour gérer les livres
def menu():
    """Menu interactif pour ajouter, supprimer et afficher des livres."""
    while True:
        print("\n--- Gestion des livres ---")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Afficher tous les livres")
        print("4. Afficher le nombre total de livres dans la bibliothèque")
        print("5. Quitter")

        choice = input("Choisissez une option (1-4) : ")

        if choice == "1":
            print("\n\033[94mVous avez choisi: Ajouter un livre\033[0m")
            add_book()
        elif choice == "2":
            print("\n\033[94mVous avez choisi: Supprimer un livre\033[0m")
            book_name = input("Titre du livre à supprimer : ")
            remove_book(book_name)
        elif choice == "3":
            print("\n\033[94mVous avez choisi: Afficher tous les livres\033[0m")
            display_books()
        elif choice == "4":
            print("\n\033[94mVous avez choisi: Afficher le nombre total de livres dans la bibliothèque\033[0m")
            display_total_number_of_books_in_library()
        elif choice == "5":
            print("\nMerci d'avoir utilisé le gestionnaire de livres.")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    # Charger les livres au démarrage
    load_books_csv()
    
    # Lancer le menu principal
    menu()

