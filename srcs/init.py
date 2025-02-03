from pyray import init_window, set_target_fps, measure_text, Rectangle # Import for Raylib
from pyray import DARKGRAY, BLUE, DARKBLUE, DARKGREEN, WHITE, ORANGE, MAROON, RED

from text_entry import TextEntry

WINDOW_WIDTH: int = 700
WINDOW_HEIGHT: int = 660
WINDOW_TITLE: str = "MyLib"

TEXT_OFFSET = 20

# RL = raylib
FONT_COLOR = DARKGRAY
BUTTON_HEIGHT = int(30 + 5)

TEXT_BOX: Rectangle = Rectangle(10, int(WINDOW_HEIGHT / 4 * 3), int(WINDOW_WIDTH - 20), int(WINDOW_HEIGHT / 4 - 10)) # Make rectangle from values

# Text_entry init

text_entry: TextEntry = TextEntry(
	10,								# x
	int(BUTTON_HEIGHT * 12) + 20,	# y
	int(WINDOW_WIDTH - 20),			# width
	int(BUTTON_HEIGHT - 5)			# height
)

# Putt all buttons in a dictionary
dict_button = {
	"add_book": {  # Name for the button in dico (Key)
		"title": "Ajouter ou supprimer un livre dans la bibliotheque",	# Text visible on button
		"text": "Text pour ajouter ou supprimer un livre dans la bibliotheque",	# Text for write on textBox
		"x": 10,                            	# position x
		"y": BUTTON_HEIGHT + 10,            	# position y
		"width": int(WINDOW_WIDTH - 20),    	# Button width
		"height": int(BUTTON_HEIGHT - 5),  		# Button height
		"measure_text": 0,                  	# For center text in button
		"base_color": BLUE,                 	# Base button color
		"hover_color": DARKBLUE,            	# mouse hover button color
		"clicked_color": DARKGREEN,         	# Clicked button color
		"text_color": WHITE,                	# Color for text
		"is_clicked": False,                	# For launch action once until mouse button release
		"action": 1                         	# For launch good action in draw_button()
	},
	"add_user": {
		"title": "Ajouter ou supprimer un utilisateur",
		"text": "Text pour ajouter ou supprimer un utilisateur",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 2) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 2
	},
	"emprunt": {
		"title": "Enregistrer un emprunt ou un retour",
		"text": "Text pour enregistrer un emprunt ou un retour",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 3) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 3
	},
	"lister": {
		"title": "Lister les livres les plus empruntes",
		"text": "Text pour lister les livres les plus empruntes",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 4) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 4
	},
	"calculer": {
		"title": "Calculer la duree moyenne des emprunts par genre",
		"text": "Text pour Calculer la duree moyenne des emprunts par genre",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 5) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 5
	},
	"identifier": {
		"title": "Identifier les utilisateurs les plus actifs",
		"text": "Text pour identifier les utilisateurs les plus actifs",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 6) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 6
	},
	"status": {
		"title": "Afficher le statut de la bibliotheque sous forme de statistiques",
		"text": "Text pour afficher le status de la bibliotheque",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 7) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 7
	},
	"diagramme": {
		"title": "Visualisation: Diagramme circulaire des emprunts par genre",
		"text": "Faire apparaitre une box avec un diagramme circulaire detaille",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 8) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 8
	},
	"evolution": {
		"title": "Visualisation: Evolution mensuelle des emprunt",
		"text": "Text pour voir l'evolution mensuelle des emprunts",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 9) + 10,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": BLUE,
		"hover_color": DARKBLUE,
		"clicked_color": DARKGREEN,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 9
	# },
	# "input": {
	# 	"title": "Input Utilisateur",
	# 	"text": "Text pour Input",
	# 	"x": 10,
	# 	"y": int(BUTTON_HEIGHT * 12) + 20,
	# 	"width": int(WINDOW_WIDTH - 20),
	# 	"height": int(BUTTON_HEIGHT - 5),
	# 	"measure_text": 0,
	# 	"base_color": BLUE,
	# 	"hover_color": DARKBLUE,
	# 	"clicked_color": DARKGREEN,
	# 	"text_color": WHITE,
	# 	"is_clicked": False,
	# 	"action": 10
	},
	"quitter": {
		"title": "Quitter",
		"text": "Text pour quitter le programme",
		"x": 10,
		"y": int(BUTTON_HEIGHT * 10) + 20,
		"width": int(WINDOW_WIDTH - 20),
		"height": int(BUTTON_HEIGHT - 5),
		"measure_text": 0,
		"base_color": ORANGE,
		"hover_color": MAROON,
		"clicked_color": RED,
		"text_color": WHITE,
		"is_clicked": False,
		"action": 11
	},
}

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
	"1": {
		"Auteur": "A",
		"Genre": "Roman",
		"Exemplaires": 5,
		"Emprunts": 10
	},
	"2": {
		"Auteur": "B",
		"Genre": "Programmation",
		"Exemplaires": 11,
		"Emprunts": 20
	},
	"3": {
		"Auteur": "C",
		"Genre": "Programmation",
		"Exemplaires": 1,
		"Emprunts": 5
	},
	"4": {
		"Auteur": "D",
		"Genre": "Test",
		"Exemplaires": 2,
		"Emprunts": 8
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
		
	},
	"3": {
		"Nom": "Johnson",
		"Prénom": "Charlie",
		"Email": "charlie@gmail.com",
		"Téléphone": "514-888-9696",
		"Emprunts": 22,
		"ListeLivreLu":["Python Programming","The Great Gatsby","Marx's Inferno"]
	},
	"4": {
		"Nom": "Williams",
		"Prénom": "David",
		"Email": "david@gmail.com",
		"Téléphone": "514-888-9696",
		"Emprunts": 1000000,
		"ListeLivreLu":["Python Programming","The Great Gatsby","Marx's Inferno","Atomic Habits et +"]
	}
}

loans_list_dict = [
	{
		"Utilisateur_ID": "1",
		"Livre": "Python Programming",
		"Date_Emprunt": "2024-12-01",
		"Date_Retour": "2024-12-10"
	},
	{
		"Utilisateur_ID": "2",
		"Livre": "The Great Gatsby",
		"Date_Emprunt": "2024-11-25",
		"Date_Retour": "2024-12-10"
	},
	{
		"Utilisateur_ID": "1",
		"Livre": "1",
		"Date_Emprunt": "2024-11-25",
		"Date_Retour": "2024-11-30"
	},
	{
		"Utilisateur_ID": "2",
		"Livre": "2",
		"Date_Emprunt": "2024-02-05",
		"Date_Retour": "2024-03-15"
	},
	{
		"Utilisateur_ID": "1",
		"Livre": "3",
		"Date_Emprunt": "2024-02-05",
		"Date_Retour": None
	}
]

# init principal variables for the program
def init():
	# Window init
	init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'))
	set_target_fps(10)  # FPS to 10 frame sec
	
	for b in loans_list_dict:
		print(b)

	# Init each text wide in pixel for center text in button
	for button in dict_button:
		dict_button[button]["measure_text"] = int(measure_text(dict_button[button]["title"].encode('utf-8'), 20) / 2)
