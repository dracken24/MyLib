from init import loans_list_dict, dict_books
from utility import our_input, BASE_CHOICE_STR
from datetime import datetime

genre = []

# Calculate the average duration of loans by genre
def calcul_emprunt_books(button: str):
    affich_text = "--- Calculer la durée moyenne des emprunts par genre ---\n"

    if loans_list_dict == [] or verifier_emprunts_retour() == False:    # Au cas ou il n'a pas d'emprunt complet (sans retour)
        affich_text += "\n" + ("-" * 30)
        affich_text += "\nAucun emprunt enregistré.\n"
        affich_text += "-" * 30 + "\n\n"
        our_input(affich_text + BASE_CHOICE_STR)
        return

    else:
        affich_text += "\n" + ("-" * 30) + "\n"
        affich_text += f"* La durée moyenne des emprunts, par genre"
        affich_text += "\n" + ("-" * 30) + "\n"
        trier_genre()
        affich_text += calculer_moyenne(button)
        affich_text += "-" * 30 + "\n\n"
        our_input(affich_text + BASE_CHOICE_STR)
        return

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
        if len(days) == 0:
            continue
        else:
            return_text += f"\n* {gen}: {sum(days)/len(days):.0f} jours"

    return return_text + "\n\n"

def verifier_emprunts_retour():
    for loan in loans_list_dict:
        if loan["Date_Retour"] is not None:
            return True
        else:
            return False