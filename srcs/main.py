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

# Add or remove a book from the library
def add_remove_books(button: str):
    print(f"{button} button Hit Action 1")

# Add or delete a user
def add_remove_users(button: str):
    print(f"{button} button Hit Action 2")

# Record a loan or return
def emprunt_retour_books(button: str):
    print(f"{button} button Hit Action 3")

# List the most borrowed books
def list_books(button: str):
    print(f"{button} button Hit Action 4")

# Calculate the average duration of loans by type
def calcul_emprunt_books(button: str):
    print(f"{button} button Hit Action 5")

# Identify the most active users
def ident_actif_users(button: str):
    print(f"{button} button Hit Action 6")

# Show library status as statistics
def status(button: str):
    print(f"{button} button Hit Action 7")

# Visualization: Pie chart of borrowings by genre
def diagram(button: str):
    print(f"{button} button Hit Action 8")

# Visualization: Monthly evolution of borrowing
def monthly_evolution(button: str):
    print(f"{button} button Hit Action 9")

# Draw a button with a text and return if the mouse is over the button (Return True for close program)
def draw_button(button: str) -> tuple:
    # if mouser is over the button, Check collision with mouse and button
    if (check_collision_point_rec(get_mouse_position(), (dict_button[button]["x"], dict_button[button]["y"],
                                dict_button[button]["width"], dict_button[button]["height"]))):
        # If the mouse is over the button, check if the left mouse button is pressed and choose the good action
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            dict_button[button]["is_clicked"] = True  # Set True for the button clicked

            # ***************************************Actions for Buttons*****************************************
            if dict_button[button]["action"] == 1:
                add_remove_books(button)            # Action for the button add_remove_books clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 2:
                add_remove_users(button)            # Action for the button add_remove_users clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 3:
                emprunt_retour_books(button)        # Action for the button emprunt_retour_books clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 4:
                list_books(button)                  # Action for the button list_books clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 5:
                calcul_emprunt_books(button)        # Action for the button calcul_emprunt_books clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 6:
                ident_actif_users(button)           # Action for the button ident_actif_users clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 7:
                status(button)                      # Action for the button status clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 8:
                diagram(button)                     # Action for the button diagram clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 9:
                monthly_evolution(button)           # Action for the button monthly_evolution clicked
                return False, dict_button[button]["text"], True
            elif dict_button[button]["action"] == 10:
                print(f"{button} button Hit Action 10") # EXIT
                return True, dict_button[button]["text"], True
            # *************************************************************************************************** 

        # If Mouse is over button but not clicked, Use this color of button (dict_button[button]["hover_color"])
        elif dict_button[button]["is_clicked"] == False:
            draw_rectangle(dict_button[button]["x"], dict_button[button]["y"], dict_button[button]["width"], dict_button[button]["height"], dict_button[button]["hover_color"])                      # Draw Button
            draw_text(dict_button[button]["text"].encode('utf-8'), int(dict_button[button]["x"] + dict_button[button]["width"] / 2 - dict_button[button]["measure_text"]),    # Draw Text
                        int(dict_button[button]["y"] + dict_button[button]["height"] / 2 - 10), 20, dict_button[button]["text_color"])
        
        # If Mouse is over button and is clicked but mouse not release, Use this color of button (dict_button[button]["clicked_color"])
        if dict_button[button]["is_clicked"] == True:
            draw_rectangle(dict_button[button]["x"], dict_button[button]["y"], dict_button[button]["width"], dict_button[button]["height"], dict_button[button]["clicked_color"])                     # Draw Button
            draw_text(dict_button[button]["text"].encode('utf-8'), int(dict_button[button]["x"] + dict_button[button]["width"] / 2 - dict_button[button]["measure_text"]),    # Draw Text
                        int(dict_button[button]["y"] + dict_button[button]["height"] / 2 - 10), 20, dict_button[button]["text_color"])
    # If Mouse is not over button and is not clicked, Use this color of button (dict_button[button]["base_color"])
    else:
        draw_rectangle(dict_button[button]["x"], dict_button[button]["y"], dict_button[button]["width"], dict_button[button]["height"], dict_button[button]["base_color"])         # Draw Button
        draw_text(dict_button[button]["text"].encode('utf-8'), int(dict_button[button]["x"] + dict_button[button]["width"] / 2 - dict_button[button]["measure_text"]),        # Draw Text
                    int(dict_button[button]["y"] + dict_button[button]["height"] / 2 - 10), 20, dict_button[button]["text_color"])
    
    return False, "", False

def main():

    init()

    # For Quit the main loop for exit programm
    quit_ct: bool = False
    affich_text: str = ""

    while (not quit_ct):    # Detect window close on x corner click or escape key
        # Drawing begin
        begin_drawing()
        
        # Clear screen with LIGHTGRAY color for reset UI at each frame (Use this color for backgroung)
        clear_background(LIGHTGRAY)     

        # Draw title text
        text_width = measure_text(WINDOW_TITLE.encode('utf-8'), 20)
        x_position = int(get_screen_width() / 2 - text_width / 2)

        # Draw all buttons
        for button in dict_button:
            quit_ct, text, action = draw_button(button)
            if (action == True):
                affich_text = text
                break
        
        # Draw text zone
        draw_rectangle(10, int(WINDOW_HEIGHT / 4 * 3), int(WINDOW_WIDTH - 20), int(WINDOW_HEIGHT / 4 - 10), WHITE)
        draw_text(affich_text, 20, int(WINDOW_HEIGHT / 4 * 3) + 10, 20, BLACK)

        # Reset mouse left button pressed when button is released
        if is_mouse_button_released(MOUSE_BUTTON_LEFT):
            for butt in dict_button:
                # if button clicked set to True, Set it to False
                if dict_button[butt]["is_clicked"] == True:
                    dict_button[butt]["is_clicked"] = False

        draw_text(WINDOW_TITLE.encode('utf-8'), x_position, 20, 20, DARKGRAY)

        end_drawing()

    # Close windows and openGL context properly at exit
    close_window()

main()
