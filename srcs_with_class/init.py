from pyray import * # Import for Raylib
from my_button import *

WINDOW_WIDTH: int = 700
WINDOW_HEIGHT: int = 600
WINDOW_TITLE: str = "MyLib"

# RL = raylib
FONT_COLOR = DARKGRAY
BUTTON_HEIGHT = int(30 + 5)

# Dictionary for all buttons
dict_button = { }

add_book: MyButton = MyButton(10,
                              (BUTTON_HEIGHT + 10),
                              (WINDOW_WIDTH - 20),
                              (BUTTON_HEIGHT - 5),
                              BLUE,
                              DARKGREEN,
                              DARKBLUE,
                              WHITE,
                              "Ajouter ou supprimer un livre dans la bibliotheque",
                              20)

add_user: MyButton = MyButton(10,
                              (BUTTON_HEIGHT * 2 + 10),
                              (WINDOW_WIDTH - 20),
							  (BUTTON_HEIGHT - 5),
							  BLUE,
							  DARKGREEN,
							  DARKBLUE,
                              WHITE,
							  "Ajouter ou supprimer un utilisateur",
                              20)

emprunt: MyButton = MyButton(10,
							 (BUTTON_HEIGHT * 3 + 10),
							 (WINDOW_WIDTH - 20),
							 (BUTTON_HEIGHT - 5),
							 BLUE,
							 DARKGREEN,
							 DARKBLUE,
                             WHITE,
							 "Enregistrer un emprunt ou un retour",
                             20)

lister: MyButton = MyButton(10,
							(BUTTON_HEIGHT * 4 + 10),
							(WINDOW_WIDTH - 20),
							(BUTTON_HEIGHT - 5),
							BLUE,
							DARKGREEN,
							DARKBLUE,
                            WHITE,
							"Lister les livres les plus empruntes",
                            20)

calculer: MyButton = MyButton(10, (BUTTON_HEIGHT * 5 + 10),
							  (WINDOW_WIDTH - 20),
							  (BUTTON_HEIGHT - 5),
							  BLUE,
							  DARKGREEN,
							  DARKBLUE,
                              WHITE,
							  "Calculer la duree moyenne des emprunts par genre",
                              20)

identifier: MyButton = MyButton(10,
								(BUTTON_HEIGHT * 6 + 10),
								(WINDOW_WIDTH - 20),
								(BUTTON_HEIGHT - 5),
								BLUE,
								DARKGREEN,
								DARKBLUE,
								WHITE,
								"Identifier les utilisateurs les plus actifs",
								20)

status: MyButton = MyButton(10,
							(BUTTON_HEIGHT * 7 + 10),
							(WINDOW_WIDTH - 20),
							(BUTTON_HEIGHT - 5),
							BLUE,
							DARKGREEN,
							DARKBLUE,
							WHITE,
							"Afficher le statut de la bibliotheque sous forme de statistiques",
							20)

diagramme: MyButton = MyButton(10,
							   (BUTTON_HEIGHT * 8 + 10),
							   (WINDOW_WIDTH - 20),
							   (BUTTON_HEIGHT - 5),
							   BLUE,
							   DARKGREEN,
							   DARKBLUE,
                               WHITE,
							   "Visualisation: Diagramme circulaire des emprunts par genre",
                               20)

evolution: MyButton = MyButton(10,
							   (BUTTON_HEIGHT * 9 + 10),
							   (WINDOW_WIDTH - 20),
							   (BUTTON_HEIGHT - 5),
							   BLUE,
							   DARKGREEN,
							   DARKBLUE,
                               WHITE,
							   "Visualisation: Evolution mensuelle des emprunt",
                               20)

quitter: MyButton = MyButton(10,
							 (BUTTON_HEIGHT * 10 + 25),
							 (WINDOW_WIDTH - 20),
							 (BUTTON_HEIGHT - 5),
							 BLUE,
							 DARKGREEN,
							 DARKBLUE,
							 WHITE,
                             "Quitter",
							 20)

# init principal variables for the program
def init():
    # Window init
    init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'))
    set_target_fps(60);  # FPS to 60

    # Init each text wide in pixel for center text in button
    add_book.set_mesure_text(int(measure_text(add_book.get_text().encode('utf-8'), 20) / 2))
    add_user.set_mesure_text(int(measure_text(add_user.get_text().encode('utf-8'), 20) / 2))
    emprunt.set_mesure_text(int(measure_text(emprunt.get_text().encode('utf-8'), 20) / 2))
    lister.set_mesure_text(int(measure_text(lister.get_text().encode('utf-8'), 20) / 2))
    calculer.set_mesure_text(int(measure_text(calculer.get_text().encode('utf-8'), 20) / 2))
    identifier.set_mesure_text(int(measure_text(identifier.get_text().encode('utf-8'), 20) / 2))
    status.set_mesure_text(int(measure_text(status.get_text().encode('utf-8'), 20) / 2))
    diagramme.set_mesure_text(int(measure_text(diagramme.get_text().encode('utf-8'), 20) / 2))
    evolution.set_mesure_text(int(measure_text(evolution.get_text().encode('utf-8'), 20) / 2))
    quitter.set_mesure_text(int(measure_text(quitter.get_text().encode('utf-8'), 20) / 2))

    # Putt all buttons in a dictionary
    dict_button[add_book.get_text()] = add_book
    dict_button[add_user.get_text()] = add_user
    dict_button[emprunt.get_text()] = emprunt
    dict_button[lister.get_text()] = lister
    dict_button[calculer.get_text()] = calculer
    dict_button[identifier.get_text()] = identifier
    dict_button[status.get_text()] = status
    dict_button[diagramme.get_text()] = diagramme
    dict_button[evolution.get_text()] = evolution
    dict_button[quitter.get_text()] = quitter

