from pyray import DARKGRAY, BLUE, DARKBLUE, DARKGREEN, WHITE, ORANGE, MAROON, RED
from pyray import init_window, set_target_fps, measure_text # Import for Raylib

from buttons.calcul_emprunt_books import CalculEmpruntBooks
from buttons.emprunt_retour_books import EmpruntReturnBooks
from buttons.monthly_evolution import MonthlyEvolution
from buttons.ident_actif_users import IdentActifUsers
from buttons.add_remove_books import AddRemBooks
from buttons.add_remove_users import AddRemUser
from buttons.list_books import ListBooks
from buttons.my_button import MyButton
from buttons.diagram import Diagram
from buttons.status import Status
from buttons.quit import Exit

from data_store import BUTTON_HEIGHT, WINDOW_WIDTH, WINDOW_TITLE, WINDOW_HEIGHT
from data_store import dict_books, dict_users, loans_list_dict, dict_button

# from text_entry import TextEntry

######################### Buttons liked to class init ##########################

calcul_emprunt: CalculEmpruntBooks = CalculEmpruntBooks()
emprunt_retour: EmpruntReturnBooks = EmpruntReturnBooks()
ident_actif_users: IdentActifUsers = IdentActifUsers()
add_rem_books: AddRemBooks = AddRemBooks()
add_rem_users: AddRemUser = AddRemUser()
monthly_evolution = MonthlyEvolution()
list_books: ListBooks = ListBooks()
diagram: Diagram = Diagram()
status: Status = Status()
my_exit: Exit = Exit()

################################################################################

################################# Buttons init #################################

add_book: MyButton = MyButton(add_rem_books,
							  10,
							  (BUTTON_HEIGHT + 10),
							  (WINDOW_WIDTH - 20),
							  (BUTTON_HEIGHT - 5),
							  0,
							  BLUE,
							  DARKGREEN,
							  DARKBLUE,
							  WHITE,
							  "Ajouter ou supprimer un livre dans la bibliotheque",
							#   "Text pour ajouter ou supprimer un livre dans la bibliotheque",
							  20)

add_user: MyButton = MyButton(add_rem_users,
							  10,
							  (BUTTON_HEIGHT * 2 + 10),
							  (WINDOW_WIDTH - 20),
							  (BUTTON_HEIGHT - 5),
							  1,
							  BLUE,
							  DARKGREEN,
							  DARKBLUE,
							  WHITE,
							  "Ajouter ou supprimer un utilisateur",
							#   "Text pour ajouter ou supprimer un utilisateur",
							  20)

emprunt: MyButton = MyButton(emprunt_retour,
							 10,
							 (BUTTON_HEIGHT * 3 + 10),
							 (WINDOW_WIDTH - 20),
							 (BUTTON_HEIGHT - 5),
							 2,
							 BLUE,
							 DARKGREEN,
							 DARKBLUE,
							 WHITE,
							 "Enregistrer un emprunt ou un retour",
							#  "Text pour enregistrer un emprunt ou un retour",
							 20)

lister: MyButton = MyButton(list_books,
							10,
							(BUTTON_HEIGHT * 4 + 10),
							(WINDOW_WIDTH - 20),
							(BUTTON_HEIGHT - 5),
							3,
							BLUE,
							DARKGREEN,
							DARKBLUE,
							WHITE,
							"Lister les livres les plus empruntes",
							# "Text pour lister les livres les plus empruntes",
							20)

calculer: MyButton = MyButton(calcul_emprunt,
							  10,
							  (BUTTON_HEIGHT * 5 + 10),
							  (WINDOW_WIDTH - 20),
							  (BUTTON_HEIGHT - 5),
							  4,
							  BLUE,
							  DARKGREEN,
							  DARKBLUE,
							  WHITE,
							  "Calculer la duree moyenne des emprunts par genre",
							#   "Text pour Calculer la duree moyenne des emprunts par genre",
							  20)

identifier: MyButton = MyButton(ident_actif_users,
								10,
								(BUTTON_HEIGHT * 6 + 10),
								(WINDOW_WIDTH - 20),
								(BUTTON_HEIGHT - 5),
								5,
								BLUE,
								DARKGREEN,
								DARKBLUE,
								WHITE,
								"Identifier les utilisateurs les plus actifs",
								# "Text pour identifier les utilisateurs les plus actifs",
								20)

status: MyButton = MyButton(status,
							10,
							(BUTTON_HEIGHT * 7 + 10),
							(WINDOW_WIDTH - 20),
							(BUTTON_HEIGHT - 5),
							6,
							BLUE,
							DARKGREEN,
							DARKBLUE,
							WHITE,
							"Afficher le statut de la bibliotheque sous forme de statistiques",
							# "Text pour afficher le status de la bibliotheque",
							20)

diagramme: MyButton = MyButton(diagram,
							   10,
							   (BUTTON_HEIGHT * 8 + 10),
							   (WINDOW_WIDTH - 20),
							   (BUTTON_HEIGHT - 5),
							   7,
							   BLUE,
							   DARKGREEN,
							   DARKBLUE,
							   WHITE,
							   "Visualisation: Diagramme circulaire des emprunts par genre",
							#    "Faire apparaitre une box avec un diagramme circulaire detaille",
							   20)

evolution: MyButton = MyButton(monthly_evolution,
							   10,
							   (BUTTON_HEIGHT * 9 + 10),
							   (WINDOW_WIDTH - 20),
							   (BUTTON_HEIGHT - 5),
							   8,
							   BLUE,
							   DARKGREEN,
							   DARKBLUE,
							   WHITE,
							   "Visualisation: Evolution mensuelle des emprunt",
							#    "Text pour voir l'evolution mensuelle des emprunts",
							   20)

quitter: MyButton = MyButton(my_exit,
							 10,
							 (BUTTON_HEIGHT * 10 + 25),
							 (WINDOW_WIDTH - 20),
							 (BUTTON_HEIGHT - 5),
							 9,
							 ORANGE,
							 RED,
							 MAROON,
							 WHITE,
							 "Quitter",
							#  "Quitter",
							 20)


# init principal variables for the program
def init():
	# Window init
	init_window(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'))
	set_target_fps(12)  # FPS to 12 frame sec
	
	for b in loans_list_dict:
		print(b)

	# Init each text wide in pixel for center text in button
	identifier.set_mesure_text(int(measure_text(identifier.get_title().encode('utf-8'), 20) / 2))
	evolution.set_mesure_text(int(measure_text(evolution.get_title().encode('utf-8'), 20) / 2))
	diagramme.set_mesure_text(int(measure_text(diagramme.get_title().encode('utf-8'), 20) / 2))
	add_book.set_mesure_text(int(measure_text(add_book.get_title().encode('utf-8'), 20) / 2))
	add_user.set_mesure_text(int(measure_text(add_user.get_title().encode('utf-8'), 20) / 2))
	calculer.set_mesure_text(int(measure_text(calculer.get_title().encode('utf-8'), 20) / 2))
	emprunt.set_mesure_text(int(measure_text(emprunt.get_title().encode('utf-8'), 20) / 2))
	quitter.set_mesure_text(int(measure_text(quitter.get_title().encode('utf-8'), 20) / 2))
	lister.set_mesure_text(int(measure_text(lister.get_title().encode('utf-8'), 20) / 2))
	status.set_mesure_text(int(measure_text(status.get_title().encode('utf-8'), 20) / 2))

	# Putt all buttons in a dictionary
	dict_button[identifier.get_title()] = identifier
	dict_button[diagramme.get_title()] = diagramme
	dict_button[evolution.get_title()] = evolution
	dict_button[add_book.get_title()] = add_book
	dict_button[add_user.get_title()] = add_user
	dict_button[calculer.get_title()] = calculer
	dict_button[emprunt.get_title()] = emprunt
	dict_button[quitter.get_title()] = quitter
	dict_button[lister.get_title()] = lister
	dict_button[status.get_title()] = status
