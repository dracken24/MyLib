from init import dict_button, dict_books, dict_users, loans_list_dict
from add_remove_users import User
dict_books = {}
dict_users = {}
import csv
import os

class Book:
    def __init__(self, book_name, author, genre, number_of_copies_available, total_times_rented=0):
        self.book_name = book_name
        self.author = author
        self.genre = genre
        self.number_of_copies_available = int(number_of_copies_available)
        self.total_times_rented = int(total_times_rented)

    def rent_book(self):
        if self.number_of_copies_available > 0:
            self.number_of_copies_available -= 1
            self.total_times_rented += 1
            print("-" * 30)
            print(f"Le livre '{self.book_name}' a été emprunté avec succès.")
            print("-" * 30)
        else:
            print(f"Désolé, aucune copie de '{self.book_name}' n'est disponible.")

    def return_book(self):
        self.number_of_copies_available += 1
        print("-" * 30)
        print(f"Le livre '{self.book_name}' a été retourné avec succès.")
        print("-" * 30)

    def display_info(self):
        print("-" * 30)
        print(f"Titre : {self.book_name}")
        print(f"Auteur : {self.author}")
        print(f"Genre : {self.genre}")
        print(f"Copies disponibles : {self.number_of_copies_available}")
        print(f"Nombre total d'emprunts : {self.total_times_rented}")
        print("-" * 30)

# Ajouter un livre à la bibliothèque
def add_book(book_name, author, genre, number_of_copies_available, total_times_rented):
    if book_name in dict_books:
        dict_books[book_name].number_of_copies_available += int(number_of_copies_available)
        print("-" * 30)
        print(f"Le livre '{book_name}' existait déjà. Les copies disponibles ont été mises à jour.")
        print("-" * 30)
    else:
        book = Book(book_name, author, genre, number_of_copies_available, total_times_rented)
        dict_books[book_name] = book
        print("-" * 30)
        print(f"Le livre '{book_name}' a été ajouté à la bibliothèque.")
        print("-" * 30)
    save_books_csv()

# Supprimer un livre de la bibliothèque
def remove_book(book_name):
    if book_name in dict_books:
        book = dict_books[book_name]
        print(f"\nLe livre '{book_name}' a actuellement {book.number_of_copies_available} copies disponibles.")
        print("-" * 30)
        # Demander à l'utilisateur combien de copies il souhaite retirer
        print("-" * 30)
        choice = input("Entrez le nombre de copies à supprimer ou tapez 'tous' pour tout supprimer : ")
        print("-" * 30)
        if choice.isdigit():
            # Supprimer un nombre spécifique de copies
            copies_to_remove = int(choice)
            if 0 < copies_to_remove <= book.number_of_copies_available:
                book.number_of_copies_available -= copies_to_remove
                print("-" * 30)
                print(f"{copies_to_remove} copie(s) de '{book_name}' ont été retirées. Copies restantes : {book.number_of_copies_available}.")
                print("-" * 30)
            else:
                print("-" * 30)
                print(f"Impossible de retirer {copies_to_remove} copie(s). Il n'y a que {book.number_of_copies_available} copie(s) disponibles.")
                print("-" * 30)
        elif choice.lower() == "tous":
            # Supprimer complètement le livre
            del dict_books[book_name]
            print("-" * 30)
            print(f"Toutes les copies de '{book_name}' ont été supprimées de la bibliothèque.")
            print("-" * 30)
        else:
            print("-" * 30)
            print("Choix invalide. Aucune action effectuée.")
            print("-" * 30)
    else:
        print("-" * 30)
        print(f"Le livre '{book_name}' n'est pas trouvé dans la bibliothèque.")
        print("-" * 30)
    save_books_csv()

# Emprunter un livre
def rent_book(book_name):
    if book_name in dict_books:
        dict_books[book_name].rent_book()
    else:
        print("-" * 30)
        print(f"Le livre '{book_name}' n'est pas trouvé dans la bibliothèque.")
        print("-" * 30)
    save_books_csv()

# Retourner un livre
def return_book(book_name):
    if book_name in dict_books:
        dict_books[book_name].return_book()
    else:
        print("-" * 30)
        print(f"Le livre '{book_name}' n'est pas trouvé dans la bibliothèque.")
        print("-" * 30)
    save_books_csv()

# Afficher tous les livres
def display_books():
    if dict_books:
        for book in dict_books.values():
            book.display_info()
    else:
        print("-" * 30)
        print("Aucun livre dans la bibliothèque.")
        print("-" * 30)

def display_rental_stats():
    if dict_books:
        print("\n--- Statistiques d'emprunts ---")
        print("-" * 30)
        for book in dict_books.values():
            print(f"'{book.book_name}' a été emprunté {book.total_times_rented} fois")
        print("-" * 30)
    else:
        print("-" * 30)
        print("Aucun livre dans la bibliothèque.")
        print("-" * 30)

def display_users():
    if dict_users:
        print("\n--- Liste des Utilisateurs ---")
        print("-" * 30)
        for user in dict_users.values():
            print(f"Nom: {user.first_name} {user.last_name}")
            print(f"Email: {user.email}")
            print(f"Livres lus: {', '.join(user.read_books)}")
            print(f"Total des emprunts: {user.total_books_rented}")
            print("-" * 30)
    else:
        print("-" * 30)
        print("Aucun utilisateur enregistré.")
        print("-" * 30)

# Déplacer user_rent_book en dehors de la classe Book et en faire une fonction globale
def user_rent_book():
    email = input("Entrez l'email de l'utilisateur : ")
    if email in dict_users:
        user = dict_users[email]
        print(f"Bonjour, {user.first_name} {user.last_name} !")
        display_books()  # Affiche les livres disponibles
        book_name = input("Entrez le nom du livre que vous voulez emprunter : ")
        if book_name in dict_books:
            book = dict_books[book_name]
            if book.number_of_copies_available > 0:
                book.rent_book()
                user.add_read_book(book_name)
                user.total_books_rented += 1
                save_users_csv()
                save_books_csv()
                print(f"Le livre '{book_name}' a été ajouté à la liste des livres lus de {user.first_name}.")
            else:
                print(f"Désolé, aucune copie de '{book_name}' n'est disponible.")
        else:
            print(f"Le livre '{book_name}' n'existe pas dans la bibliothèque.")
    else:
        print(f"Aucun utilisateur trouvé avec l'email {email}.")



def save_books_csv(file="books.csv"):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Écrire l'en-tête
        writer.writerow(["book_name", "author", "genre", "number_of_copies_available", "total_times_rented"])
        # Écrire les données des livres
        for book in dict_books.values():
            writer.writerow([
                book.book_name,
                book.author,
                book.genre,
                book.number_of_copies_available,
                book.total_times_rented
            ])
    print("-" * 30)
    print("Les livres ont été sauvegardés dans le fichier CSV avec succès.")
    print("-" * 30)

def load_books_csv(file="books.csv"):
    global dict_books
    if os.path.exists(file):  # Vérifier si le fichier existe
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            dict_books.clear()  # Vider le dictionnaire avant de charger les données
            for row in reader:
                dict_books[row["book_name"]] = Book(
                    book_name=row["book_name"],
                    author=row["author"],
                    genre=row["genre"],
                    number_of_copies_available=int(row["number_of_copies_available"]),
                    total_times_rented=int(row["total_times_rented"])
                )
        print("-" * 30)
        print("Les livres ont été chargés depuis le fichier CSV avec succès.")
        print("-" * 30)
    else:
        print("-" * 30)
        print("Aucun fichier CSV trouvé. Création d'un nouveau fichier.")
        print("-" * 30)

def save_users_csv(file="users.csv"):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["email", "first_name", "last_name", "read_books", "total_books_rented"])
        for user in dict_users.values():
            writer.writerow([
                user.email,
                user.first_name,
                user.last_name,
                ";".join(user.read_books),
                user.total_books_rented
            ])

def load_users_csv(file="users.csv"):
    global dict_users
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            dict_users.clear()
            for row in reader:
                read_books = row["read_books"].split(";") if row["read_books"] else []
                dict_users[row["email"]] = User(
                    email=row["email"],
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    read_books=read_books,
                    total_books_rented=int(row["total_books_rented"])
                )

