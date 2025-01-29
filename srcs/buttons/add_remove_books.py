import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from data_store import dict_button, dict_books, dict_users, loans_list_dict
import csv

class AddRemBooks:
    def __init__(self):
        print("AddRemBooks class init")

    def update(self):
        print("AddRemBooks Update")
        return self.print_prompt()
        
    def print_prompt(self):
        text: str = "--- Gestion des livres ---\n1 . Ajouter un livre\n2. Supprimer un livre\n3. Afficher tous les livres\n4. Quitter\n\nChoisissez une option (1-4) :\n"
        return text

# Ajouter un livre à la bibliothèque
def add_book(book_name, author, genre, number_of_copies_available, total_times_rented=0):
    """Ajoute un livre ou met à jour les copies disponibles s'il existe déjà."""
    if book_name in dict_books:
        dict_books[book_name].number_of_copies_available += int(number_of_copies_available)
        print(f"\nLe livre '{book_name}' existe déjà. Copies disponibles mises à jour.")
    else:
        dict_books[book_name] = Book(book_name, author, genre, number_of_copies_available, total_times_rented)
        print(f"\nLe livre '{book_name}' a été ajouté à la bibliothèque.")
    save_books_csv()


# Supprimer un livre de la bibliothèque
def remove_book(book_name):
    """Supprime complètement un livre de la bibliothèque."""
    if book_name in dict_books:
        del dict_books[book_name]
        print(f"\nLe livre '{book_name}' a été supprimé de la bibliothèque.")
        save_books_csv()
    else:
        print(f"\nLe livre '{book_name}' n'existe pas dans la bibliothèque.")


# Afficher tous les livres
def display_books():
    """Affiche les informations de tous les livres."""
    if dict_books:
        print("\n--- Liste des livres dans la bibliothèque ---")
        for book in dict_books.values():
            book.display_info()
    else:
        print("\nAucun livre dans la bibliothèque.")


# Sauvegarder les livres dans un fichier CSV
def save_books_csv(file="books.csv"):
    """Sauvegarde les informations des livres dans un fichier CSV."""
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["book_name", "author", "genre", "number_of_copies_available", "total_times_rented"])
        for book in dict_books.values():
            writer.writerow([
                book.book_name,
                book.author,
                book.genre,
                book.number_of_copies_available,
                book.total_times_rented
            ])
    print("\nLes livres ont été sauvegardés avec succès.")


# Charger les livres depuis un fichier CSV
def load_books_csv(file="books.csv"):
    """Charge les informations des livres depuis un fichier CSV."""
    global dict_books
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            dict_books.clear()
            for row in reader:
                dict_books[row["book_name"]] = Book(
                    book_name=row["book_name"],
                    author=row["author"],
                    genre=row["genre"],
                    number_of_copies_available=int(row["number_of_copies_available"]),
                    total_times_rented=int(row["total_times_rented"])
                )
        print("\nLes livres ont été chargés depuis le fichier CSV.")
    else:
        print("\nAucun fichier CSV trouvé. Création d'un nouveau fichier lors de la sauvegarde.")


# Menu principal pour gérer les livres
def menu():
    """Menu interactif pour ajouter, supprimer et afficher des livres."""
    # while True:
    #     print("\n--- Gestion des livres ---")
    #     print("1. Ajouter un livre")
    #     print("2. Supprimer un livre")
    #     print("3. Afficher tous les livres")
    #     print("4. Quitter")

    choice = input("Choisissez une option (1-4) : ")

    if choice == "1":
        print("\n\033[94mVous avez choisi: Ajouter un livre\033[0m")
        book_name = input("\nTitre du livre : ")
        author = input("Auteur : ")
        genre = input("Genre : ")
        number_of_copies = input("Nombre de copies disponibles : ")

        # Validation de l'entrée
        if not number_of_copies.isdigit():
            print("Le nombre de copies doit être un nombre entier.")
            # continue

        add_book(book_name, author, genre, int(number_of_copies))
    elif choice == "2":
        print("\n\033[94mVous avez choisi: Supprimer un livre\033[0m")
        book_name = input("Titre du livre à supprimer : ")
        remove_book(book_name)
    elif choice == "3":
        print("\n\033[94mVous avez choisi: Afficher tous les livres\033[0m")
        display_books()
    elif choice == "4":            
        print("\nMerci d'avoir utilisé le gestionnaire de livres.")
        # break
    else:
        print("Option invalide. Veuillez réessayer.")

class Book:
    """Classe représentant un livre dans la bibliothèque."""
    def __init__(self, book_name, author, genre, number_of_copies_available, total_times_rented=0):
        self.book_name = book_name
        self.author = author
        self.genre = genre
        self.number_of_copies_available = int(number_of_copies_available)
        self.total_times_rented = int(total_times_rented)

    def display_info(self):
        """Afficher les informations du livre."""
        # text_to_affich: str = "-" * 30 + f"\nTitre : {self.book_name}\nAuteur : {self.author}\nGenre : {self.genre}\nCopies disponibles : {self.number_of_copies_available}\nNombre total d'emprunts : {self.total_times_rented}\n" + "-" * 30
        print("-" * 30)
        print(f"Titre : {self.book_name}")
        print(f"Auteur : {self.author}")
        print(f"Genre : {self.genre}")
        print(f"Copies disponibles : {self.number_of_copies_available}")
        print(f"Nombre total d'emprunts : {self.total_times_rented}")
        print("-" * 30)

if __name__ == "__main__":
    # Charger les livres au démarrage
    load_books_csv()
    
    # Lancer le menu principal
    menu()
