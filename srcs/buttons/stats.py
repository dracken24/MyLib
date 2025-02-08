import csv
import os
from init import dict_books, dict_users, loans_list_dict

BOOKS_FILE = "books.csv"  # Nom du fichier contenant les livres

def charger_nombre_total_exemplaires(fichier=BOOKS_FILE):
    """Charge le nombre total d'exemplaires disponibles depuis le fichier CSV (sans try/except)"""
    total_exemplaires = 0
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_exemplaires += int(row["number_of_copies_available"])  # Additionne les exemplaires disponibles
    return total_exemplaires

class Stats:
    def __init__(self):
        """Initialisation des statistiques"""

        self.nombre_total_livre = len(dict_books)  # Nombre total de livres (différents titres)
        
        # Charger le nombre total d'exemplaires de livres disponibles depuis books.csv
        self.nombre_total_exemplaires = charger_nombre_total_exemplaires()

        # Nombre total d'exemplaires empruntés
        self.nombre_total_exemplaire_emprunt = sum(loan.get("Emprunts", 0) for loan in loans_list_dict)


        # Nombre total d'exemplaires restants
        self.nombre_livres_disponibles = self.nombre_total_exemplaires - self.nombre_total_exemplaire_emprunt

        # Pourcentage de livres disponibles
        self.pourcentage_livre_disponible = (self.nombre_livres_disponibles / self.nombre_total_exemplaires * 100) if self.nombre_total_exemplaires > 0 else 0

        # Nombre moyen de livres empruntés par utilisateur
        self.nombre_utilisateurs = len(dict_users)
        self.nombre_de_livre_moyen_par_utilisateur = (self.nombre_total_exemplaire_emprunt / self.nombre_utilisateurs) if self.nombre_utilisateurs > 0 else 0

    # def afficher_stats(self):
    #     """Affiche les statistiques de la bibliothèque"""
    #     print("-" * 40)
    #     print("\U0001F4CA Statistiques de la bibliothèque")
    #     print("-" * 40)
    #     print(f"\U0001F4DA Nombre total de titres (livres différents) : {self.nombre_total_livre}")
    #     print(f"\U0001F4E6 Nombre total d'exemplaires (tous livres confondus) : {self.nombre_total_exemplaires}")
    #     print(f"\U0001F4D6 Nombre total d'exemplaires empruntés : {self.nombre_total_exemplaire_emprunt}")
    #     print(f"\u2705 Nombre d'exemplaires disponibles : {self.nombre_livres_disponibles}")
    #     print(f"\U0001F4CA Pourcentage de livres disponibles : {self.pourcentage_livre_disponible:.2f}%")
    #     print(f"\U0001F465 Nombre d'utilisateurs : {self.nombre_utilisateurs}")
    #     print(f"\U0001F4DA Moyenne de livres empruntés par utilisateur : {self.nombre_de_livre_moyen_par_utilisateur:.2f}")
    #     print("-" * 40)

# def menu_stats():
#     """Menu interactif pour afficher les statistiques"""
#     while True:
#         print("\n=== Menu des statistiques ===")
#         print("1. Afficher les statistiques\U0001F4CA")
#         print("2. Quitter\u274C")
        
#         choice = input("Choisissez une option (1-2) : ")
        
#         if choice == "1":
#             stats = Stats()  # Créer un objet Stats
#             stats.afficher_stats()  # Afficher les statistiques
#         elif choice == "2":
#             print("\n\U0001F6AA Au revoir !")
#             break
#         else:
#             print("\u274C Option invalide, veuillez choisir 1 ou 2.")

def stats(button: str):
    """Affiche les statistiques quand le bouton est cliqué"""
    
    text: str = "--- Statistiques de la bibliothèque ---\n"
    text += f"Nombre total de livres : {len(dict_books)}\n"
    text += f"Nombre total d'utilisateurs : {len(dict_users)}\n"
    
    # Calculer le nombre total d'emprunts
    total_emprunts = sum(user['Emprunts'] for user in dict_users.values())
    text += f"Nombre total d'emprunts : {total_emprunts}\n"
    
    # Moyenne d'emprunts par utilisateur
    if len(dict_users) > 0:
        moyenne_emprunts = total_emprunts / len(dict_users)
        text += f"Moyenne d'emprunts par utilisateur : {moyenne_emprunts:.2f}\n"
