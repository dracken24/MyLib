from init import dict_button, dict_books, dict_users, loans_list_dict




dict_users = {}
import csv
import os
class User:
    def __init__(self, first_name, last_name, email, phone_number, total_books_rented=0, read_books=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.total_books_rented = int(total_books_rented)
        self.read_books = read_books if read_books is not None else []

    def to_dict(self):
        """Convertir un utilisateur en dictionnaire."""
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone_number": self.phone_number,
            "total_books_rented": self.total_books_rented,
        }

    @staticmethod
    def from_dict(data):
        """Créer un utilisateur à partir d'un dictionnaire."""
        return User(
            first_name=data["first_name"],
            last_name=data["last_name"],
            email=data["email"],
            phone_number=data["phone_number"],
            total_books_rented=data["total_books_rented"],
            read_books=data.get("read_books", [])
        )

    def add_read_book(self, book_name):
        """Ajouter un livre à la liste des livres lus s'il n'y est pas déjà."""
        if book_name not in self.read_books:
            self.read_books.append(book_name)

    def display_info(self):
        """Affiche les informations de l'utilisateur."""
        print("-" * 30)
        print(f"Prénom : {self.first_name}")
        print(f"Nom : {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Numéro de téléphone : {self.phone_number}")
        print(f"Nombre total d'emprunts : {self.total_books_rented}")
        print("-" * 30)


# Ajouter un utilisateur
def add_user():
    first_name = input("Entrez le prénom : ")
    last_name = input("Entrez le nom : ")
    email = input("Entrez l'email : ")
    phone_number = input("Entrez le numéro de téléphone : ")

    if email in dict_users:
        print(f"L'utilisateur avec l'email {email} existe déjà.")
    else:
        user = User(first_name, last_name, email, phone_number)
        dict_users[email] = user
        print("-" * 30)
        print(f"L'utilisateur {first_name} {last_name} a été ajouté avec succès.")
        print("-" * 30)
        save_users_csv()  # Sauvegarder après ajout


# Supprimer un utilisateur
def remove_user():
    email = input("Entrez l'email de l'utilisateur à supprimer : ")
    if email in dict_users:
        del dict_users[email]
        print("-" * 30)
        print(f"L'utilisateur avec l'email {email} a été supprimé.")
        print("-" * 30)
        save_users_csv()  # Sauvegarder après suppression
    else:
        print("-" * 30)
        print(f"Aucun utilisateur trouvé avec l'email {email}.")
        print("-" * 30)


# Afficher tous les utilisateurs
def display_users():
    if dict_users:
        for user in dict_users.values():
            user.display_info()
    else:
        print("-" * 30)
        print("Aucun utilisateur enregistré.")
        print("-" * 30)


def save_users_csv(file="users.csv"):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["first_name", "last_name", "email", "phone_number", "total_books_rented", "read_books"])
        for user in dict_users.values():
            writer.writerow([
                user.first_name,
                user.last_name,
                user.email,
                user.phone_number,
                user.total_books_rented,
                ";".join(user.read_books)  # Sauvegarder les livres lus comme une chaîne séparée par des points-virgules
            ])
    print("Les utilisateurs ont été sauvegardés dans le fichier CSV avec succès.")

def load_users_csv(file="users.csv"):
    global dict_users
    dict_users.clear()
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Handle the case where read_books column might not exist in older CSV files
                read_books_str = row.get("read_books", "")
                read_books = read_books_str.split(";") if read_books_str and read_books_str.strip() else []
                dict_users[row["email"]] = User(
                    first_name=row["first_name"],
                    last_name=row["last_name"],
                    email=row["email"],
                    phone_number=row["phone_number"],
                    total_books_rented=int(row["total_books_rented"]),
                    read_books=read_books
                )
        print("Les utilisateurs ont été chargés depuis le fichier CSV avec succès.")
    else:
        print("Aucun fichier CSV trouvé.")

