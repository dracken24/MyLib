import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_button, dict_books, dict_users, loans_list_dict
import csv
import re

def add_remove_users(button: str):
    """Gestion des utilisateurs quand le bouton est cliqué"""
    load_users_csv()
    text: str = "--- Gestion des utilisateurs ---\n1. Ajouter un utilisateur\n2. Supprimer un utilisateur\n3. Afficher tous les utilisateurs\n4. Quitter\n"
    dict_button[button]["text"] = text
    menu()

def add_user():
    """Ajoute un nouvel utilisateur"""
    print("\n--- Ajouter un nouvel utilisateur ---")
    prenom = input("Prénom : ")
    nom = input("Nom : ")
    
    while True:
        email = input("Email (format: exemple@gmail.com) : ")
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            break
        print("\u274C Email invalide")

    while True:
        telephone = input("Téléphone (format: xxx-xxx-xxxx) : ")
        if re.match(r"\d{3}-\d{3}-\d{4}", telephone):
            break
        print("\u274C Numéro de téléphone invalide")

    # Générer un nouvel ID
    if not dict_users:
        new_id = "1"
    else:
        last_id = max(int(user_id.replace('U', '')) for user_id in dict_users.keys())
        new_id = f"{last_id + 1}"


    dict_users[new_id] = {
        'Nom': nom,
        'Prénom': prenom,
        'Email': email,
        'Téléphone': telephone,
        'Emprunts': 0,
        'ListeLivreLu': []
    }
    
    print(f"\n\033[92mUtilisateur ajouté avec succès (ID: {new_id})\033[0m")
    save_users_csv()

def remove_user():
    """Supprime un utilisateur"""
    user_id = input("ID utilisateur à supprimer (ex: 1) : ").upper()
    
    if user_id in dict_users:
        user = dict_users[user_id]
        print(f"Utilisateur trouvé : {user['Prénom']} {user['Nom']}")
        confirmation = input("Confirmer la suppression ? (oui/non) : ").lower()
        if confirmation == "oui":
            del dict_users[user_id]
            print(f"\033[91mUtilisateur {user_id} supprimé.\033[0m")
            save_users_csv()
    else:
        print(f"\nUtilisateur {user_id} non trouvé.")


def display_users():
    """Affiche tous les utilisateurs"""
    if dict_users:
        print("\n--- Liste des utilisateurs ---")
        for user_id, user in dict_users.items():
            print("-" * 30)
            print(f"ID : {user_id}")
            print(f"Nom : {user['Nom']}")
            print(f"Prénom : {user['Prénom']}")
            print(f"Email : {user['Email']}")
            print(f"Téléphone : {user['Téléphone']}")
            print(f"Nombre d'emprunts : {user['Emprunts']}")
            if user['ListeLivreLu']:
                print("Livres lus :")
                for livre in user['ListeLivreLu']:
                    print(f"- {livre}")
            print("-" * 30)
    else:
        print("\nAucun utilisateur enregistré.")

def save_users_csv(file="users.csv"):
    """Sauvegarde les utilisateurs dans un fichier CSV"""
    with open(file, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Nom", "Prénom", "Email", "Téléphone", "Emprunts", "ListeLivreLu"])
        for user_id, user in dict_users.items():
            writer.writerow([
                user_id,
                user['Nom'],
                user['Prénom'],
                user['Email'],
                user['Téléphone'],
                user['Emprunts'],
                ";".join(user['ListeLivreLu']) if user['ListeLivreLu'] else ""
            ])

def load_users_csv(file="users.csv"):
    """Charge les utilisateurs depuis un fichier CSV"""
    if os.path.exists(file):
        with open(file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)  # Utiliser DictReader pour lire directement en dictionnaire
            dict_users.clear()
            for row in reader:
                user_id = row['ID']
                dict_users[user_id] = {
                    'Nom': row['Nom'],
                    'Prénom': row['Prénom'],
                    'Email': row['Email'],
                    'Téléphone': row['Téléphone'],
                    'Emprunts': int(row['Emprunts']),
                    'ListeLivreLu': row['ListeLivreLu'].split(";") if row['ListeLivreLu'] else []
                }

def mettre_a_jour_emprunts_utilisateurs():
    """Met à jour les emprunts des utilisateurs à partir de la liste des prêts"""
    for loan in loans_list_dict:
        user_id = loan.get("user_id")
        if user_id in dict_users:
            dict_users[user_id]['Emprunts'] = loan.get("Emprunts", 0)
            dict_users[user_id]['Livres'] = loan.get("Livres", [])

def menu():
    """Menu interactif pour la gestion des utilisateurs"""
    while True:
        print("\n--- Gestion des utilisateurs ---")
        print("1. Ajouter un utilisateur")
        print("2. Supprimer un utilisateur")
        print("3. Afficher tous les utilisateurs")
        print("4. Quitter")

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
            print("\n\033[94mVous avez choisi: Quitter\033[0m")
            print("Au revoir!")
            break
        else:
            print("Option invalide. Veuillez réessayer.")



