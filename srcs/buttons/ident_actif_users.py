import sys
import os
import csv

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_users, loans_list_dict
from utility import our_input, BASE_CHOICE_STR
from csv_control import load_users_csv  # Add this import
# from buttons.add_remove_users import load_users_csv  # On supprime `User` qui n'est pas utilisé ici

USERS_FILE = "csv/users.csv"  # Nom du fichier contenant les utilisateurs et leurs emprunts
dict_users_tmp = {} # Pour calculer le nombre d'emprunt

def load_users_with_loans():
    """Charge les utilisateurs et leurs emprunts depuis `users.csv` et met à jour avec loans_list_dict."""
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            dict_users_tmp.clear()
            for row in reader:
                dict_users_tmp[row["ID"]] = {
                    "Prénom": row["Prénom"],
                    "Nom": row["Nom"],
                    "Emprunts": 0  # On initialise à 0
                }
        
        # Calculer le nombre d'emprunts à partir de loans_list_dict
        for loan in loans_list_dict:
            user_id = loan.get("Utilisateur_ID")
            if user_id in dict_users:
                dict_users_tmp[user_id]["Emprunts"] += 1
                
        return None
    else:
        return "\nAucun fichier `users.csv` trouvé. Création d'un nouveau fichier lors de la sauvegarde.\n\n"

# Identifier les utilisateurs les plus actifs
def ident_actif_users(button: str):
    afficher_utilisateurs_plus_actifs()

def afficher_utilisateurs_plus_actifs(nombre_top=3):
    """Affiche les utilisateurs ayant emprunté le plus de livres."""
    affich_text = "--- Identifier les users actifs ---\n"
    return_text = load_users_with_loans()  # 🔥 Recharger les données des utilisateurs depuis `users.csv`

    if return_text:
        our_input(affich_text + return_text + BASE_CHOICE_STR)
        return

    if not dict_users_tmp:
        affich_text += "\n" + ("-" * 30)
        affich_text += "\nAucun utilisateur enregistré.\n"
        affich_text += "-" * 30 + "\n\n"
        our_input(affich_text + BASE_CHOICE_STR)
        return

    # Trier les utilisateurs par nombre d'emprunts (total_books_rented depuis `users.csv`)
    utilisateurs_tries = sorted(
        dict_users_tmp.items(),
        key=lambda x: x[1]["Emprunts"],  # Utilisation des emprunts chargés depuis users.csv
        reverse=True
    )

    affich_text += "\n" + ("-" * 30)
    affich_text += f"\n* Les {nombre_top} utilisateurs les plus actifs :\n"
    affich_text += "-" * 30 + "\n\n"
    for i, (user_id, user) in enumerate(utilisateurs_tries[:nombre_top], start=1):
        affich_text += f"* #{i} {user['Prénom']} {user['Nom']} - Emprunts : {user['Emprunts']}\n"

    affich_text += "\n" + "-" * 30 + "\n\n"
    our_input(affich_text + BASE_CHOICE_STR)
