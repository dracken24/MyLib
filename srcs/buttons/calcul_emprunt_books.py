from init import dict_button, loans_list_dict, dict_books
from utility import our_input, BASE_CHOICE_STR
from buttons.add_remove_books import load_books_csv
from buttons.emprunt_retour_books import load_loans_csv
from datetime import datetime, timedelta

genre = []

# Calculate the average duration of loans by genre  - DONEE
def calcul_emprunt_books(button: str):
    # print(f"{button} button Hit Action 5")
    affich_text = "--- La durée moyenne des emprunts, par genre ---\n"
    load_books_csv()
    load_loans_csv()
    # print("\n\033[1m\033[4m--La durée moyenne des emprunts, par genre--\033[0m")
    dict_button[button]["text"] = "--- La durée moyenne des emprunts, par genre ---"
    trier_genre()
    affich_text += calculer_moyenne(button)

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
        # print("A")
        for book in dict_books.keys():
            # print("B")
            if dict_books[book]["Genre"] == gen:
                for loan in loans_list_dict:
                    if book == loan["Livre"]:
                        # print("C: ", loan["Date_Retour"])
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
                            print(f"\nEmpruntee pour {tempsEmprunt.days}")
        if len(days) == 0:
            continue
        else:
            # print(f"{sum(days)} / {len(days)} = {sum(days)/len(days)}")
            # print(f"{gen}: {sum(days)/len(days):.0f} jours")
            dict_button[button]["text"] += f"\n{gen}: {sum(days)/len(days):.0f} jours"
            return_text += f"\n{gen}: {sum(days)/len(days):.0f} jours"

    return return_text + "\n\n"