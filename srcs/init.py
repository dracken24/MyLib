from pyray import init_window, set_target_fps, measure_text, Rectangle # Import for Raylib
from pyray import DARKGRAY, BLUE, DARKBLUE, DARKGREEN, WHITE, ORANGE, MAROON, RED

from text_entry import TextEntry

WINDOW_WIDTH: int = 700
WINDOW_HEIGHT: int = 760
WINDOW_TITLE: str = "MyLib"

TEXT_OFFSET = 20

# RL = raylib
FONT_COLOR = DARKGRAY
BUTTON_HEIGHT = int(30 + 5)

TEXT_BOX: Rectangle = Rectangle(
	10,
	int(WINDOW_HEIGHT / 4 * 3) - 90,
	int(WINDOW_WIDTH - 20),
	int(WINDOW_HEIGHT / 4 - 10) + 89
) # Make rectangle from values

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
	},
	"quitter": {
		"title": "Quitter",
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
	}
}

dict_books: dict = {}

dict_users: dict = {}

loans_list_dict: list = []

# init principal variables for the program
def init():
	# Window init
	init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'))
	set_target_fps(12)  # FPS to 12 frame sec
	
	for b in loans_list_dict:
		print(b)

	# Init each text wide in pixel for center text in button
	for button in dict_button:
		dict_button[button]["measure_text"] = int(measure_text(dict_button[button]["title"].encode('utf-8'), 20) / 2)
