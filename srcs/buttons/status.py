import csv
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from init import dict_books, dict_users, loans_list_dict
from utility import our_input, BASE_CHOICE_STR, EXIT_CODE


def status(button: str):
    print(f"{button} button Hit Action 7")
    stats = Stats(button)
    text = stats.afficher_stats()  # Afficher les statistiques
    return_text = our_input(text + BASE_CHOICE_STR)
    if (return_text == EXIT_CODE):
        return


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
        text += "-" * 40 + "\n"
        text += "\U0001F4CA Statistiques de la bibliothèque\n"
        text += "-" * 40 + "\n"
        text += f"* Nombre total de titres (livres différents) : {self.nombre_total_livre}\n"
        text += f"* Nombre total d'exemplaires (tous livres confondus) : {self.nombre_total_exemplaires}\n"
        text += f"* Nombre total d'exemplaires empruntés : {self.nombre_total_exemplaire_emprunt}\n"
        text += f"* Nombre d'exemplaires disponibles : {self.nombre_livres_disponibles}\n"
        text += f"* Pourcentage de livres disponibles : {self.pourcentage_livre_disponible:.2f}%\n"
        text += f"* Nombre d'utilisateurs : {self.nombre_utilisateurs}\n"
        text += f"* Moyenne de livres empruntés par utilisateur : {self.nombre_de_livre_moyen_par_utilisateur:.2f}\n"
        text += "-" * 40 + "\n"
        
        return text
