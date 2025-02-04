import sys
import os
import csv

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_button, dict_books, dict_users
from utility import our_input, BASE_CHOICE_STR
from buttons.add_remove_users import load_users_csv  # On supprime `User` qui n'est pas utilisé ici

USERS_FILE = "users.csv"  # Nom du fichier contenant les utilisateurs et leurs emprunts

def load_users_with_loans():
    """Charge les utilisateurs et leurs emprunts depuis `users.csv`."""
    global dict_users
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            dict_users.clear()
            for row in reader:
                dict_users[row["ID"]] = {
                    "Prénom": row["Prénom"],
                    "Nom": row["Nom"],
                    "Emprunts": int(row["Emprunts"])  # Nombre total d'emprunts
                }
        return None
    else:
        # print("\nAucun fichier `users.csv` trouvé. Création d'un nouveau fichier lors de la sauvegarde.")
        return "\nAucun fichier `users.csv` trouvé. Création d'un nouveau fichier lors de la sauvegarde.\n\n"

# Identifier les utilisateurs les plus actifs
def ident_actif_users(button: str):
    # print(f"{button} button Hit Action 6")
    afficher_utilisateurs_plus_actifs()

def afficher_utilisateurs_plus_actifs(nombre_top=3):
    """Affiche les utilisateurs ayant emprunté le plus de livres."""
    affich_text = "--- Identifier les users actifs ---\n"
    return_text = load_users_with_loans()  # 🔥 Recharger les données des utilisateurs depuis `users.csv`

    if return_text:
        our_input(affich_text + return_text + BASE_CHOICE_STR)
        return

    if not dict_users:
        affich_text += "\n" + ("-" * 30)
        # print("-" * 30)
        affich_text += "\nAucun utilisateur enregistré.\n"
        # print("Aucun utilisateur enregistré.")
        affich_text += "-" * 30 + "\n\n"
        # print("-" * 30)
        our_input(affich_text + BASE_CHOICE_STR)
        return

    # Trier les utilisateurs par nombre d'emprunts (total_books_rented depuis `users.csv`)
    utilisateurs_tries = sorted(
        dict_users.items(),
        key=lambda x: x[1]["Emprunts"],  # ✅ Utilisation des emprunts chargés depuis users.csv
        reverse=True
    )

    affich_text += "\n" + ("-" * 30)
    # print("-" * 30)
    affich_text += f"\n* Les {nombre_top} utilisateurs les plus actifs :\n"
    # print(f"🔥 Les {nombre_top} utilisateurs les plus actifs :")
    affich_text += "-" * 30 + "\n\n"
    # print("-" * 30 + "\n")
    for i, (user_id, user) in enumerate(utilisateurs_tries[:nombre_top], start=1):
        affich_text += f"* #{i} {user['Prénom']} {user['Nom']} - Emprunts : {user['Emprunts']}\n"
        # print(f"\U0001F525 #{i} {user['Prénom']} {user['Nom']} - Emprunts : {user['Emprunts']}")

    affich_text += "\n" + "-" * 30 + "\n\n"
    our_input(affich_text + BASE_CHOICE_STR)
    # print("-" * 30)

def menu_users():
    """Menu interactif pour afficher les utilisateurs actifs."""
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
if __name__ == "__main__":
    menu_users()
