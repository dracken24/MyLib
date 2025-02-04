import sys
import os

# Ajoutez le répertoire parent au sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from init import dict_button, loans_list_dict, dict_books
from utility import our_input, BASE_CHOICE_STR
from datetime import datetime, timedelta

genre = []

# Calculate the average duration of loans by genre
def calcul_emprunt_books(button: str):
    # print(f"{button} button Hit Action 5")
    affich_text = "--- La durée moyenne des emprunts, par genre ---\n"
    affich_text += "\n" + ("-" * 30)
    trier_genre()
    affich_text += calculer_moyenne(button)
    affich_text += "-" * 30 + "\n\n"
    our_input(affich_text + BASE_CHOICE_STR)
    return

def afficher_books():
    print("\n\033[1m\033[4m--List of Books--\033[0m")
    for book in dict_books.keys():
        print(f"\nLivre: {book}")
        print(f"Genre: {dict_books[book]["Genre"]}")
        print(f"Emprunts: {dict_books[book]["Emprunts"]}")

def trier_genre():
    for book in dict_books.keys():
        if dict_books[book]["Genre"] not in genre:
            genre.append(dict_books[book]["Genre"])

def calculer_moyenne(button: str):
    return_text = ""

    for gen in genre:
        days = []
        for book in dict_books.keys():
            if dict_books[book]["Genre"] == gen:
                for loan in loans_list_dict:
                    if book == loan["Livre"]:
                        if loan["Date_Retour"] == None:
                            continue
                        else:
                            # Date Math
                            date1 = loan["Date_Emprunt"]
                            date2 = loan["Date_Retour"]
                            date1 = datetime.strptime(date1, "%Y-%m-%d")
                            date2 = datetime.strptime(date2, "%Y-%m-%d")
                            tempsEmprunt = date2 - date1
                            days.append(tempsEmprunt.days)
                            #print(f"\nEmpruntee pour {tempsEmprunt.days}")
        if len(days) == 0:
            continue
        else:
            return_text += f"\n{gen}: {sum(days)/len(days):.0f} jours"

    return return_text + "\n\n"