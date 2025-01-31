# Pour empecher les dependances circulaires entre les classes et le init

from pyray import DARKGRAY

# from buttons.my_button import MyButton
from text_entry import TextEntry

WINDOW_WIDTH: int = 700
WINDOW_HEIGHT: int = 780
WINDOW_TITLE: str = "MyLib"

TEXT_OFFSET = 20

RESET_STRING = "reset button"

# RL = raylib
FONT_COLOR = DARKGRAY
BUTTON_HEIGHT = int(30 + 5)

############################### Text_entry init ###############################

text_entry: TextEntry = TextEntry(
	10,								# x
	int(BUTTON_HEIGHT * 12) + 20,	# y
	int(WINDOW_WIDTH - 20),			# width
	int(BUTTON_HEIGHT - 5)			# height
)
################################################################################

# lorem is to test the text box
lorem: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. EXIT."
# affich_text: str = lorem
affich_text: str = "Veuillez cliquer sur un bouton pour faire un choix"

# Putt all buttons in a dictionary
dict_button: dict = { }

dict_books: dict = {
    "Python Programming": {
        "Auteur": "John Doe",
        "Genre": "Programmation",
        "Exemplaires": 5,
        "Emprunts": 10
    },
    "The Great Gatsby": {
        "Auteur": "F. Scott Fitzgerald",
        "Genre": "Roman",
        "Exemplaires": 2,
        "Emprunts": 7
    },
    "Harry Potter 1": {
        "Auteur": "J.K. Rowling",
        "Genre": "Fantastique",
        "Exemplaires": 4,
        "Emprunts": 2,
    },
    "Harry Potter 3": {
        "Auteur": "J.K. Rowling",
        "Genre": "Fantastique",
        "Exemplaires": 5,
        "Emprunts": 1
    }
}

dict_users = {
    "1": {
        "Nom": "Smith",
        "Prénom": "Alice",
        "Email": "alice@gmail.com",
        "Téléphone": "514-888-9696",
        "Emprunts": 5,
        "ListeLivreLu":["Python Programming","The Great Gatsby","Marx's Inferno",
        "Atomic Habits"]
    },
    "2": {
        "Nom": "Brown",
        "Prénom": "Bob",
        "Email": "bob@gmail.com",
        "Téléphone": "430-568-8985",
        "Emprunts": 2,
        "ListeLivreLu":["Python Programming","The Great Gatsby"]
    }
}

loans_list_dict = [
    {
        "Utilisateur_ID": 1,
        "Livre": "Python Programming",
        "Date_Emprunt": "2024-12-01",
        "Date_Retour": "2024-12-10"
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "The Great Gatsby",
        "Date_Emprunt": "2024-11-25",
        "Date_Retour": None
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "Harry Potter 1",
        "Date_Emprunt": "2025-02-13",
        "Date_Retour": None
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "Harry Potter 3",
        "Date_Emprunt": "2025-03-18",
        "Date_Retour": None
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "Harry Potter 3",
        "Date_Emprunt": "2025-03-18",
        "Date_Retour": None
    },
    {
        "Utilisateur_ID": 1,
        "Livre": "Python Programming",
        "Date_Emprunt": "2024-09-01",
        "Date_Retour": "2025-04-10"
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "The Great Gatsby",
        "Date_Emprunt": "2024-11-25",
        "Date_Retour": None
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "Harry Potter 3",
        "Date_Emprunt": "2025-07-18",
        "Date_Retour": None
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "Harry Potter 3",
        "Date_Emprunt": "2025-03-18",
        "Date_Retour": None
    },
    {
        "Utilisateur_ID": 1,
        "Livre": "Python Programming",
        "Date_Emprunt": "2024-12-01",
        "Date_Retour": "2025-04-10"
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "The Great Gatsby",
        "Date_Emprunt": "2025-05-25",
        "Date_Retour": None
    }
]
