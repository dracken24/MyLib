from pyray import * # Import for Raylib

WINDOW_WIDTH: int = 700
WINDOW_HEIGHT: int = 600
WINDOW_TITLE: str = "MyLib"

# RL = raylib
FONT_COLOR = DARKGRAY
BUTTON_HEIGHT = int(30 + 5)

# Putt all buttons in a dictionary
dict_button = {
	"add_book": {  # Name for the button in dico (Key)
		"text": "Ajouter ou supprimer un livre dans la bibliotheque",	# Text visible on button
		"x": 10,                            # position x
		"y": BUTTON_HEIGHT + 10,            # position y
		"width": int(WINDOW_WIDTH - 20),    # Button width
		"height": int(BUTTON_HEIGHT - 5),   # Button height
		"measure_text": 0,                  # For center text in button
		"base_color": BLUE,                 # Base button color
		"hover_color": DARKBLUE,            # mouse hover button color
		"clicked_color": DARKGREEN,         # Clicked button color
		"text_color": WHITE,                # Color for text
		"is_clicked": False,                # For launch action once until mouse button release
		"action": 1                         # For launch good action in draw_button()
	},
	"add_user": {
		"text": "Ajouter ou supprimer un utilisateur",
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
		"text": "Enregistrer un emprunt ou un retour",
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
		"text": "Lister les livres les plus empruntes",
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
		"text": "Calculer la duree moyenne des emprunts par genre",
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
		"text": "Identifier les utilisateurs les plus actifs",
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
		"text": "Afficher le statut de la bibliotheque sous forme de statistiques",
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
		"text": "Visualisation: Diagramme circulaire des emprunts par genre",
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
		"text": "Visualisation: Evolution mensuelle des emprunt",
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
		"text": "Quitter",
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
		"action": 10
	}
}

# init principal variables for the program
def init():
    # Window init
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'))
    set_target_fps(60);  # FPS to 60

    # Init each text wide in pixel for center text in button
    for button in dict_button:
        dict_button[button]["measure_text"] = int(measure_text(dict_button[button]["text"].encode('utf-8'), 20) / 2)
