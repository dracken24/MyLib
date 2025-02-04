from pyray import draw_rectangle_rec, draw_rectangle_lines_ex, draw_text, check_collision_point_rec, is_mouse_button_pressed, get_mouse_position, MOUSE_BUTTON_LEFT, Rectangle, DARKGRAY # Import for Raylib
from init import dict_button

from buttons.add_remove_books import add_remove_books
from buttons.add_remove_users import add_remove_users
from buttons.emprunt_retour_books import emprunt_retour_books
from buttons.list_books import list_books
from buttons.calcul_emprunt_books import calcul_emprunt_books
from buttons.ident_actif_users import ident_actif_users
from buttons.status import status
from buttons.diagram import diagram
from buttons.monthly_evolution import monthly_evolution

BOARDER_THICK = 2
BORDER_COLOR = DARKGRAY
BASE_CHOICE_STR = "Veuillez cliquer sur un boutton pour faire un choix\n"

def draw_clicked_button(button: str, rect: Rectangle):
    draw_rectangle_rec(rect, dict_button[button]["clicked_color"])                     # Draw Button
    draw_text(dict_button[button]["title"].encode('utf-8'), int(rect.x + rect.width / 2 - dict_button[button]["measure_text"]),    # Draw Text
                int(rect.y + rect.height / 2 - 10), 20, dict_button[button]["text_color"])
    
    # Draw a button border
    draw_rectangle_lines_ex(rect, BOARDER_THICK, BORDER_COLOR)

# Draw a button with a text and return if the mouse is over the button (Return True for close program)
def draw_button(button: str) -> tuple:
    # Mount position and size button in a rectangle for easy use
    rect = Rectangle(dict_button[button]["x"], dict_button[button]["y"], dict_button[button]["width"], dict_button[button]["height"])

    # if mouser is over the button, Check collision with mouse and button
    if (check_collision_point_rec(get_mouse_position(), (rect.x, rect.y, rect.width, rect.height))):
        # If the mouse is over the button, check if the left mouse button is pressed and choose the good action
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            dict_button[button]["is_clicked"] = True  # Set True for the button clicked

            # ***************************************Actions for Buttons*****************************************
            if dict_button[button]["action"] == 1:
                text = add_remove_books(button)            # Action for the button add_remove_books clicked
                draw_clicked_button(button, rect)
                return False, text, True
            elif dict_button[button]["action"] == 2:
                add_remove_users(button)            # Action for the button add_remove_users clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 3:
                emprunt_retour_books(button)        # Action for the button emprunt_retour_books clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 4:
                list_books(button)                  # Action for the button list_books clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 5:
                calcul_emprunt_books(button)        # Action for the button calcul_emprunt_books clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 6:
                ident_actif_users(button)           # Action for the button ident_actif_users clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 7:
                status(button)                      # Action for the button status clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 8:
                diagram(button)                     # Action for the button diagram clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 9:
                monthly_evolution(button)           # Action for the button monthly_evolution clicked
                draw_clicked_button(button, rect)
                return False, BASE_CHOICE_STR, True
            elif dict_button[button]["action"] == 11:
                print(f"{button} button Hit Action 10") # EXIT
                return True, "Exit", True
            # *************************************************************************************************** 

        # If Mouse is over button but not clicked, Use this color of button (dict_button[button]["hover_color"])
        elif dict_button[button]["is_clicked"] == False:
            draw_rectangle_rec(rect, dict_button[button]["hover_color"])                      # Draw Button
            draw_text(dict_button[button]["title"].encode('utf-8'), int(rect.x + rect.width / 2 - dict_button[button]["measure_text"]),    # Draw Text
                        int(rect.y + rect.height / 2 - 10), 20, dict_button[button]["text_color"])
        
        # If Mouse is over button and is clicked but mouse not release, Use this color of button (dict_button[button]["clicked_color"])
        if dict_button[button]["is_clicked"] == True:
            draw_clicked_button(button, rect)
    # If Mouse is not over button and is not clicked, Use this color of button (dict_button[button]["base_color"])
    else:
        draw_rectangle_rec(rect, dict_button[button]["base_color"])         # Draw Button
        draw_text(dict_button[button]["title"].encode('utf-8'), int(rect.x + rect.width / 2 - dict_button[button]["measure_text"]),        # Draw Text
                    int(rect.y + rect.height / 2 - 10), 20, dict_button[button]["text_color"])
        
    # Draw a button border
    draw_rectangle_lines_ex(rect, BOARDER_THICK, BORDER_COLOR)
    return False, "", False
