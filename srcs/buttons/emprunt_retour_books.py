from data_store import dict_button, dict_books, dict_users, loans_list_dict
from text_entry import TextEntry

from time import sleep
from datetime import datetime, timedelta

WIP = "\n\033[93m\033[1mWIP\033[0m"

##########################################################################################

class EmpruntReturnBooks:
    def __init__(self):
        print("EmpruntReturnBooks class init")

    def on_start(self):
        pass

    def update(self, text_entry: TextEntry):
        print("EmpruntReturnBooks Update")
        return "EmpruntReturnBooks Update"

##########################################################################################

# Afficher of dicts
def afficher_users():
    print("\n\033[1m\033[4m--List of Users--\033[0m")
    for user in dict_users.keys():
        print(f'\nID: {user}')
        print(f'Nom: {dict_users[user]["Nom"]}')
        print(f'Prénom: {dict_users[user]["Prénom"]}')
        print(f'Email: {dict_users[user]["Email"]}')
        print(f'Téléphone: {dict_users[user]["Téléphone"]}')
        print(f'Emprunts: {dict_users[user]["Emprunts"]}')
        print(f'Liste Livre Lu:')
        #print(f'ListeLivreLu: {dict_users[user]["ListeLivreLu"]}')
        for livre in dict_users[user]["ListeLivreLu"]:
            print(f' - {livre}')
    #print("\n")
def afficher_books():
    print("\n\033[1m\033[4m--List of Books--\033[0m")
    for book in dict_books.keys():
        print(f"\nLivre: {book}")
        print(f"Auteur: {dict_books[book]["Auteur"]}")
        print(f"Genre: {dict_books[book]["Genre"]}")
        print(f"Exemplaires: {dict_books[book]["Exemplaires"]}")
        print(f"Emprunts: {dict_books[book]["Emprunts"]}")
def afficher_loans():
    print("\n\033[1m\033[4m--List of Loans--\033[0m")
    for loan in loans_list_dict:
        print(f"\nUtilisateur_ID: {loan["Utilisateur_ID"]}")
        print(f"Livre: {loan["Livre"]}")
        print(f"Date_Emprunt: {loan["Date_Emprunt"]}")
        print(f"Date_Retour: {loan["Date_Retour"]}")

def afficher_livres_simple():
    print("\n\033[1m\033[4m--List of Books--\033[0m")
    for book in dict_books.keys():
        print(f'- {book}')
#def afficher_loans_simple(id, titre): #WIP need to show only book input
    # # l = []
    # # for loan in loans_list_dict:
    # #     if int(id) == loan["Utilisateur_ID"] and titre == loan["Livre"]:
    # #         if loan["Date_Retour"] is None: #RETOUR
    # #             l.append(loan)
    # l = [loan for loan in loans_list_dict if int(id) == loan["Utilisateur_ID"] and titre == loan["Livre"] and loan["Date_Retour"] is None]
    # # l = [loan for loan in loans_list_dict if int(id) == loan["Utilisateur_ID"] and loan["Date_Retour"] is None]
    # if len(l) == 0:
    #     print(f"\033[91mPas d'emprunt en cours.\033[0m")
    #     return False
    # else:
    #     print("--Emprunt(s) trouvé(s)--")
    #     for i in range(1, len(l)+1):
    #         print(f'{i}. "{l[i-1]["Livre"]}" - Emprunté le {l[i-1]["Date_Emprunt"]}')
    #     #selection = int(input("Choisissez l'emprunt que vous souhaitez de retourner :"))
    #     #[l[selection]-1]

# Rechercher of dicts
def rechercher_user(id):
    for user in dict_users:
        if user == id:
            return user
    print(f"\033[91mAuncun utilisateur sous ce code d'identité {id} retrouvé.\033[0m")
    return None
def rechercher_livre(titre):
    for livre in dict_books:
        if livre == titre:
            return livre
    print(f'\033[91mAuncun livre avec le titre "{titre}" retrouvé.\033[0m')

def rechercher_loans(): #WIP - a determiner
    pass

# NOT DONE - PASSES
def retour_livre(id, titre):
    print(WIP)
    for loan in loans_list_dict:
        if int(id) == loan["Utilisateur_ID"] and titre == loan["Livre"] and loan["Date_Retour"] is None:
            # Retourner l'exemplaire
            dict_books[titre]["Exemplaires"] += 1
            #print(f"Exemplaire de retour {dict_books[titre]["Exemplaires"]}")

            # Mettre a jour la date de retour
            loan["Date_Retour"] = datetime.now().strftime('%Y-%m-%d')

            # Calculer Pénalité
            print(f'Livre "{titre}" \nEmprunté par {dict_users[id]["Nom"]} \nà la date du {loan["Date_Emprunt"]}: \nde retour le {loan["Date_Retour"]}.')
            print("\033[93mCalculons la pénalité . . . \033[0m")
            sleep(1)

            date = loan["Date_Emprunt"]
            date_conv = datetime.strptime(date, "%Y-%m-%d")
            date_limite = date_conv + timedelta(days=14)

            if datetime.now() > date_limite:
                jours_retard = (datetime.now() - date_limite).days
                penalite = jours_retard * 1.25
                print(f"\033[91m{jours_retard} jour(s) en retard...")
                print(f"Pénalité: {penalite}$\033[0m")
            else:
                print(f"\033[92mRetour a temps! :)\033[0m")
            return
    else:
        print(f"\033[91mPas d'emprunt en cours retrouvé.\033[0m")
def emprunter_livre(id, titre):
    print(WIP)
    print(f"{id} - {titre}")
    # Verifier le nombre d'exemplaire disponibles
    if dict_books[titre]["Exemplaires"] > 0:
        print("Ce livre est disponible à emprunter.")
        sleep(1)

        # Enlever l'exemplaire
        dict_books[titre]["Exemplaires"] -= 1
        date_emp = datetime.now().strftime('%Y-%m-%d')

        # Ajouter l'emprunt
        dict_books[titre]["Emprunts"] += 1

        # Creer un emprunt pour ajouter a la list loans_list_dict
        creer_emprunt(id,livre,date_emp)
        print(f'Livre "{livre}" emprunté avec succès par {id} à la date du {date_emp}')
    else:
        print("Il n'y a plus d'exemplaires disponibles à ce moment.")

def creer_emprunt(id, livre, date_emp, date_ret=None):
    loans_list_dict.append({"Utilisateur_ID": id, "Livre": livre, "Date_Emprunt": date_emp, "Date_Retour": date_ret})
    return

# Record a loan or return - MAIN FUNCTION!
def emprunt_retour_books(button: str):
    print(f"{button} button Hit Action 3")
    print(WIP)

    while True:
        print("\033[1mCeci est pour un emprunt ou un retour?\033[0m")
        print("1. Emprunt")
        print("2. Retour")
        choix = input("\nChoisissez une option : ") # Come back later

        if choix == "1":
            print("\033[94mVous avez choisi: Emprunt\033[0m")
            break
        if choix == "2":
            print("\033[95mVous avez choisi: Retour\033[0m")
            break
        # DEBUG MODE
        if choix == "3" or choix.lower() == "loans":
            afficher_loans()
        if choix == "4" or choix.lower() == "books":
            afficher_books()
        if choix == "5" or choix.lower() == "users":
            afficher_users()
        if choix == "0" or choix.lower() == "stop":
            return
        else:
            print("\033[91mChoix invalide, réessayez.\033[0m\n")

    while True: # Trouver le client
        client = input("\nEntrez le code d'identité de l'utilisateur : ")
        client_verifiee = rechercher_user(client)
        if client_verifiee:
            print(f'\033[92mUtilisateur {dict_users[client_verifiee]["Prénom"]} {dict_users[client_verifiee]["Nom"].upper()} trouvé.\033[0m')
            break
        elif client.lower() == "stop": # To exit loop
            break

    if client_verifiee: # Next Step:
        afficher_livres_simple()
        while True: # Trouver le livre
            livre = input("\nEntrez le titre du livre : ").title()
            livre_verifiee = rechercher_livre(livre)
            if livre_verifiee:
                print(f'\033[92mLe livre "{livre_verifiee}" trouvé.\033[0m')
                break
            elif livre.lower() == "stop": # To exit loop
                break

    if client_verifiee and livre_verifiee: # Need to make fucntions for both options
        if choix == "1":
            print("\033[94mIt's a boy! (Emprunt)\033[0m")
            emprunter_livre(client_verifiee, livre_verifiee)
        if choix == "2":
            print("\033[95mIt's a girl! (Retour)\033[0m")
            retour_livre(client_verifiee, livre_verifiee)

    print(f"{button} button Hit Action 11 input text")