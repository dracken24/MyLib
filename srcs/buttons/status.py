import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_button, dict_books, dict_users, loans_list_dict
# from buttons.add_remove_books import load_books_csv
# from buttons.emprunt_retour_books import load_loans_csv


def status(button: str):
    print(f"{button} button Hit Action 7")
    stats = Stats(button)
    stats.afficher_stats()


BOOKS_FILE = "books.csv"  # Nom du fichier contenant les livres

def charger_nombre_total_exemplaires(fichier=BOOKS_FILE):
    """Charge le nombre total d'exemplaires disponibles depuis le fichier CSV (sans try/except)"""
    total_exemplaires = 0
    if os.path.exists(fichier):
        with open(fichier, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_exemplaires += int(row["Exemplaires"])  # Additionne les exemplaires disponibles
    return total_exemplaires


class Stats:
    def __init__(self, button=None):
        """Initialisation des statistiques"""
        self.button = button
        
        # load_books_csv()
        # load_loans_csv()

        self.nombre_total_livre = len(dict_books)  # Nombre total de livres (différents titres)
        
        # Charger le nombre total d'exemplaires de livres disponibles depuis books.csv
        self.nombre_total_exemplaires = sum(book['Exemplaires'] for book in dict_books.values())

        # Nombre total d'exemplaires empruntés
        self.nombre_total_exemplaire_emprunt = len(loans_list_dict)

        # Nombre total d'exemplaires restants
        self.nombre_livres_disponibles = self.nombre_total_exemplaires - self.nombre_total_exemplaire_emprunt

        # Pourcentage de livres disponibles
        self.pourcentage_livre_disponible = (self.nombre_livres_disponibles / self.nombre_total_exemplaires * 100) if self.nombre_total_exemplaires > 0 else 0

        # Nombre total d'utilisateurs
        self.nombre_utilisateurs = len(dict_users)

        # Nombre moyen de livres empruntés par utilisateur
        self.nombre_de_livre_moyen_par_utilisateur = (self.nombre_total_exemplaire_emprunt / self.nombre_utilisateurs) if self.nombre_utilisateurs > 0 else 0

    def afficher_stats(self):
        """Affiche les statistiques de la bibliothèque"""
        text =""
        print("-" * 40)
        text += "-" * 40 + "\n"
        print("\U0001F4CA Statistiques de la bibliothèque")
        text += "\U0001F4CA Statistiques de la bibliothèque\n"
        print("-" * 40)
        text += "-" * 40 + "\n"
        print(f"* Nombre total de titres (livres différents) : {self.nombre_total_livre}")
        text += f"* Nombre total de titres (livres différents) : {self.nombre_total_livre}\n"
        print(f"* Nombre total d'exemplaires (tous livres confondus) : {self.nombre_total_exemplaires}")
        text += f"* Nombre total d'exemplaires (tous livres confondus) : {self.nombre_total_exemplaires}\n"
        print(f"* Nombre total d'exemplaires empruntés : {self.nombre_total_exemplaire_emprunt}")
        text += f"* Nombre total d'exemplaires empruntés : {self.nombre_total_exemplaire_emprunt}\n"
        print(f"* Nombre d'exemplaires disponibles : {self.nombre_livres_disponibles}")
        text += f"* Nombre d'exemplaires disponibles : {self.nombre_livres_disponibles}\n"
        print(f"* Pourcentage de livres disponibles : {self.pourcentage_livre_disponible:.2f}%")
        text += f"* Pourcentage de livres disponibles : {self.pourcentage_livre_disponible:.2f}%\n"
        print(f"* Nombre d'utilisateurs : {self.nombre_utilisateurs}")
        text += f"* Nombre d'utilisateurs : {self.nombre_utilisateurs}\n"
        print(f"* Moyenne de livres empruntés par utilisateur : {self.nombre_de_livre_moyen_par_utilisateur:.2f}")
        text += f"* Moyenne de livres empruntés par utilisateur : {self.nombre_de_livre_moyen_par_utilisateur:.2f}\n"
        print("-" * 40)
        text += "-" * 40 + "\n"
        if self.button:
            dict_button[self.button]["text"] = text



def menu_stats():
    """Menu interactif pour afficher les statistiques"""
    while True:
        print("\n=== Menu des statistiques ===")
        print("1. Afficher les statistiques\U0001F4CA")
        print("2. Quitter\u274C")
        
        choice = input("Choisissez une option (1-2) : ")
        
        if choice == "1":
            stats = Stats()  # Créer un objet Stats
            stats.afficher_stats()  # Afficher les statistiques
        elif choice == "2":
            print("\n\U0001F6AA Au revoir !")
            break
        else:
            print("\u274C Option invalide, veuillez choisir 1 ou 2.")

# Exécuter le menu
if __name__ == "__main__":
    menu_stats()
