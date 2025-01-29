import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_button, dict_books, dict_users, loans_list_dict
from buttons.add_remove_users import User, load_users_csv

# Identifier les utilisateurs les plus actifs
def ident_actif_users(button: str):
    print(f"{button} button Hit Action 6")
    afficher_utilisateurs_plus_actifs()

def afficher_utilisateurs_plus_actifs(nombre_top=3):
    if not dict_users:
        print("-" * 30)
        print("Aucun utilisateur enregistré.")
        print("-" * 30)
        return

    # Trier les utilisateurs par nombre d'emprunts
    utilisateurs_tries = sorted(
        dict_users.items(),
        key=lambda x: x[1]['Emprunts'],
        reverse=True
    )

    print("-" * 30)
    print(f"Les {nombre_top} utilisateurs les plus actifs :")
    print("-" * 30)
    for i, (user_id, user) in enumerate(utilisateurs_tries[:nombre_top], start=1):
        print(f"#{i} {user['Prénom']} {user['Nom']} - Emprunts : {user['Emprunts']}")
    print("-" * 30)

def obtenir_total_emprunts(user_id):
    if user_id not in loans_list_dict:
        return 0  # Aucun emprunt trouvé
    return loans_list_dict[user_id].get("Emprunts", 0)

def menu_users():
    while True:
        print("\n--- Menu des utilisateurs ---")
        print("1. Afficher les utilisateurs les plus actifs")
        print("2. Quitter")

        choice = input("Choisissez une option (1-2) : ")
        
        if choice == "1":
            print("\n\033[94mVous avez choisi: Afficher les utilisateurs les plus actifs\033[0m")       
            afficher_utilisateurs_plus_actifs()
        elif choice == "2":
            print("\n\033[94mVous avez choisi: Quitter\033[0m")
            break
        else:
            print("\u274C Option invalide, veuillez entrer 1 ou 2.")

# Lancer le menu pour tester
menu_users()
