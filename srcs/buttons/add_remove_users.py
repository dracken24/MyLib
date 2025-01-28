from init import dict_button, dict_books, dict_users, loans_list_dict
dict_users = {}
import json

class User:
    def __init__(self, first_name, last_name, email, phone_number, total_books_rented=0):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.total_books_rented = int(total_books_rented)

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
        )

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
        save_users()  # Sauvegarder après ajout


# Supprimer un utilisateur
def remove_user():
    email = input("Entrez l'email de l'utilisateur à supprimer : ")
    if email in dict_users:
        del dict_users[email]
        print("-" * 30)
        print(f"L'utilisateur avec l'email {email} a été supprimé.")
        print("-" * 30)
        save_users()  # Sauvegarder après suppression
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


# Sauvegarder les utilisateurs dans un fichier JSON
def save_users(file="users.json"):
    with open(file, "w") as f:
        users_to_save = {email: user.to_dict() for email, user in dict_users.items()}
        json.dump(users_to_save, f, indent=4)
    print("Les utilisateurs ont été sauvegardés avec succès.")


# Charger les utilisateurs depuis un fichier JSON
def load_users(file="users.json"):
    global dict_users
    try:
        with open(file, "r") as f:
            users_data = json.load(f)
            dict_users = {
                email: User.from_dict(data) for email, data in users_data.items()
            }
        print("Les utilisateurs ont été chargés avec succès.")
    except FileNotFoundError:
        print("Aucun fichier de sauvegarde trouvé. Création d'un nouveau fichier.")


# Menu principal
def menu():
    load_users()  # Charger les utilisateurs au démarrage
    while True:
        print("\n--- Menu de Gestion des Utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Afficher tous les utilisateurs")
        print("4. Quitter")
        print("-" * 30)
        choice = input("Choisissez une option : ")
        
        if choice == "1":
            add_user()
        elif choice == "2":
            remove_user()
        elif choice == "3":
            display_users()
        elif choice == "4":
            print("-" * 30)
            print("Merci d'avoir utilisé le système de gestion des utilisateurs. À bientôt !")
            print("-" * 30)
            break
        else:
            print("-" * 30)
            print("Choix invalide. Veuillez réessayer.")
            print("-" * 30)


# Lancer le menu principal
menu()
