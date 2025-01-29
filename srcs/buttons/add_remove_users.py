import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_button, dict_books, dict_users, loans_list_dict
import csv
import re  # Pour les validations d'email et de numéro de téléphone

def add_remove_users(button):
    main_menu()

def remove_user_button(button):
    print(f"{button} button Hit Action 2")

# Classe représentant un utilisateur
class User:
    def __init__(self, user_id, first_name, last_name, email, phone_number, total_books_rented=0):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.total_books_rented = int(total_books_rented)
        self.rented_books = []  # Ajout d'une liste pour suivre les livres empruntés

    def rent_book(self, book_name):
        """Ajouter un livre à la liste des emprunts"""
        self.rented_books.append(book_name)
        self.total_books_rented += 1

    def display_info(self):
        """Afficher les informations d'un utilisateur."""
        print("-" * 30)
        print(f"ID : {self.user_id}")
        print(f"Nom : {self.first_name} {self.last_name}")
        print(f"Email : {self.email}")
        print(f"Téléphone : {self.phone_number}")
        print(f"Nombre total d'emprunts : {self.total_books_rented}")
        if self.rented_books:
            print("Livres empruntés :")
            for book in self.rented_books:
                print(f"- {book}")
        print("-" * 30)


# Mettre à jour `total_books_rented` et `rented_books` à partir de loans_list_dict
def mettre_a_jour_emprunts_utilisateurs():
    """Met à jour les emprunts des utilisateurs à partir de la liste des prêts"""
    for loan in loans_list_dict:  # Itérer directement sur la liste
        user_id = loan.get("user_id")  # Supposant que chaque prêt est un dictionnaire avec une clé "user_id"
        if user_id in dict_users:
            dict_users[user_id].total_books_rented = loan.get("Emprunts", 0)
            dict_users[user_id].rented_books = loan.get("Livres", [])


# Ajouter un utilisateur avec validation
def add_user():
    # Générer un nouvel ID utilisateur
    if not dict_users:
        new_id = "U001"  # Premier utilisateur
    else:
        # Trouver le plus grand ID et l'incrémenter
        last_id = max(int(user_id.replace('U', '')) for user_id in dict_users.keys())
        new_id = f"U{(last_id + 1):03d}"  # Format U001, U002, etc.

    first_name = input("Entrez le prénom : ")
    last_name = input("Entrez le nom : ")
    while True:
        email = input("Entrez l'email (format obligatoire: exemple@gmail.com) : ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            break
        print("\u274C L'email n'est pas valide. Veuillez entrer un email valide.")

    # Validation du numéro de téléphone
    while True:
        phone_number = input("Entrez le numéro de téléphone (format obligatoire: xxx-xxx-xxxx) : ")
        if re.match(r"\d{3}-\d{3}-\d{4}", phone_number):
            break
        print("\u274C Le numéro de téléphone n'est pas valide. Veuillez entrer un numéro valide.")

    # Créer le nouvel utilisateur avec l'ID généré
    dict_users[new_id] = User(new_id, first_name, last_name, email, phone_number)
    print("\n" + "-" * 30)
    print(f"\033[92mL'utilisateur {first_name} {last_name} a été ajouté avec succès (ID: {new_id}).\033[0m")
    print("-" * 30)
    save_users_csv()


# Supprimer un utilisateur
def remove_user():
    user_id = input("Entrez l'ID utilisateur à supprimer (ex: U001) : ").upper()
    
    # Vérification de l'ID utilisateur
    if user_id == "":
        print("L'ID utilisateur ne peut pas être vide.")
        return
    
    if user_id in dict_users:
        user = dict_users[user_id]
        print(f"Utilisateur trouvé : {user.first_name} {user.last_name}")
        confirmation = input(f"Êtes-vous sûr de vouloir supprimer cet utilisateur? (oui/non) : ").lower()
        if confirmation == "oui":
            del dict_users[user_id]
            print(f"L'utilisateur avec l'ID {user_id} a été supprimé avec succès.")
            save_users_csv()
        else:
            print("Suppression annulée.")
    else:
        print(f"Aucun utilisateur trouvé avec l'ID {user_id}.")


# Afficher tous les utilisateurs
def display_users():
    if dict_users:
        print("\n--- Liste des utilisateurs ---")
        for user in dict_users.values():
            user.display_info()
    else:
        print("Aucun utilisateur enregistré.")


# Sauvegarder les utilisateurs dans un fichier CSV
def save_users_csv(file="users.csv"):
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["user_id", "first_name", "last_name", "email", "phone_number", 
                        "total_books_rented", "rented_books"])
        for user in dict_users.values():
            writer.writerow([
                user.user_id,
                user.first_name,
                user.last_name,
                user.email,
                user.phone_number,
                user.total_books_rented,
                ";".join(user.rented_books) if user.rented_books else ""
            ])
    print("Les utilisateurs ont été sauvegardés avec succès.")


# Charger les utilisateurs depuis un fichier CSV
def load_users_csv(file="users.csv"):
    global dict_users
    if os.path.exists(file):
        try:
            with open(file, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                dict_users.clear()
                for row in reader:
                    # Vérifier si les livres empruntés existent dans le fichier
                    rented_books = row.get("rented_books", "").split(";") if row.get("rented_books") else []
                    dict_users[row["user_id"]] = User(
                        user_id=row["user_id"],
                        first_name=row["first_name"],
                        last_name=row["last_name"],
                        email=row["email"],
                        phone_number=row["phone_number"],
                        total_books_rented=int(row.get("total_books_rented", 0))
                    )
                    dict_users[row["user_id"]].rented_books = rented_books
            print("Les utilisateurs ont été chargés depuis le fichier CSV.")
        except Exception as e:
            print(f"Erreur lors du chargement du fichier CSV : {e}")
            dict_users = {}  # Réinitialiser le dictionnaire en cas d'erreur
    else:
        print("Aucun fichier CSV trouvé. Création d'un nouveau fichier.")


# Menu principal pour gérer les utilisateurs
def manage_users():
    while True:
        print("\n--- Gestion des utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Afficher tous les utilisateurs")
        print("4. Retour au menu principal")

        choice = input("Choisissez une option (1-4) : ")

        if choice == "1":
            print("\n\033[94mVous avez choisi: Ajouter un utilisateur\033[0m")
            add_user()
        elif choice == "2":
            print("\n\033[94mVous avez choisi: Supprimer un utilisateur\033[0m")
            remove_user()
        elif choice == "3":
            print("\n\033[94mVous avez choisi: Afficher tous les utilisateurs\033[0m")
            display_users()
        elif choice == "4":
            break
        else:
            print("Option invalide. Veuillez réessayer.")


def main_menu():
    while True:
        print("\n=== Menu Principal ===")
        print("1. Gestion des utilisateurs")
        print("2. Quitter")
        
        choice = input("Choisissez une option (1-2) : ")
        
        if choice == "1":
            print("\n\033[94mVous avez choisi: Gestion des utilisateurs\033[0m")
            manage_users()
        elif choice == "2":
            print("\n\033[94mVous avez choisi: Quitter\033[0m")
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


def main():
    load_users_csv()  # Charger les utilisateurs depuis CSV
    mettre_a_jour_emprunts_utilisateurs()  # Mise à jour des emprunts depuis loans_list_dict
    main_menu()
    save_users_csv()  # Sauvegarder les utilisateurs avant de quitter

if __name__ == "__main__":
    main()

