from pyray import is_mouse_button_pressed, get_mouse_position, MOUSE_BUTTON_LEFT, Rectangle, DARKGRAY # Import for Raylib
from pyray import begin_scissor_mode, end_scissor_mode, draw_text, measure_text, Rectangle, BLACK
from pyray import draw_rectangle_rec, draw_rectangle_lines_ex, draw_text, check_collision_point_rec
from pyray import begin_drawing, end_drawing, clear_background, get_screen_width, draw_text
from pyray import LIGHTGRAY, GRAY, DARKGRAY, WHITE, measure_text, draw_rectangle_rec, get_mouse_wheel_move
from pyray import BLUE, DARKBLUE, DARKGREEN

from init import WINDOW_TITLE, TEXT_BOX, text_entry, TEXT_OFFSET, WINDOW_WIDTH

from time import sleep

EXIT_CODE = "!B@A#B$Y%S^H&A*R&K^Y%O$L#O@O!"
BORDER_COLOR = DARKGRAY
BOARDER_THICK = 2

BASE_CHOICE_STR = "Veuillez cliquer sur un boutton pour faire un choix\n"

button_return = {
    "title": "Retour Au Menu Principal",
    "text": "",
    "x": 10,
    "y": 175,
    "width": int(WINDOW_WIDTH - 20),
    "height": 80,
    "measure_text": 0,
    "base_color": BLUE,
    "hover_color": DARKBLUE,
    "clicked_color": DARKGREEN,
    "text_color": WHITE,
    "is_clicked": False,
    "action": 11
}


"""Recursive function for draw and scroll text inside a box (rectangle)
    Args:
        box (Rectangle): Rectangle for draw text
        text (str): Text to draw
        line_position (int): Position in x of the line in the box
        scroll_offset (int): Scroll offset for base on mouse wheel
        line_ct (int): Text is cut in x line_ct to fix in box whide
    
    Returns:
        int: Line count (Number of time text was cut)
"""
def adjust_text_in_box_and_draw_result(box: Rectangle, text: str, line_position: int = 0,
                                       scroll_offset: int = 0, line_ct: int = 0) -> int:
    begin_scissor_mode(int(box.x), int(box.y), int(box.width), int(box.height))
    
    text_width: int = measure_text(text.encode('utf-8'), 20)    # Check if text is more whide than the box
    line_height: int = 20                                       # Space for offset each line in pixel
    writable_length: int = int(box.width - 20)                  # Writable whide space in the box (20 pixels offset)

    adjusted_y = int(box.y + line_position + scroll_offset)     # Adjust each line position in y

    line = text[:int(writable_length / 10.2)]   # Take a line in the text base on writable_length

    # for check each char in the str for check for \n to do a new line
    ct: int = 0
    find: bool = False
    for c in line: # if \n is find, give new value to line from start to \n and break
        if (c == '\n'):
            line = text[:ct]
            find = True
            break
        ct += 1

    # if the text is to whide for the box or \n find in line
    if text_width > writable_length or find == True:

        # Erase that line from the text at max length or at the \n(ct + 1 for skip \n)
        if (find == True):
            text = text[ct + 1:]
        else:
            text = text[int(writable_length / 10.2):]

        draw_text(line, int(box.x + 10), adjusted_y, 20, BLACK) # Draw the line in the box
        line_ct += 1 # Add one to the line counter

        # Call recursive function with the text less the cut line
        line_ct = adjust_text_in_box_and_draw_result(box, text, line_height + line_position, scroll_offset, line_ct)
    # If text fit in the box, just write it
    else:
        draw_text(text, int(box.x + 10), adjusted_y, 20, BLACK)

    # End scissor mode
    end_scissor_mode()

    # Return the number of line
    return line_ct

# *************************************************************************************************** 
# Function neded for our Input
# *************************************************************************************************** 

def draw_clicked_button(rect: Rectangle):
    msur_text = measure_text(button_return["title"].encode('utf-8'), 20) / 2

    draw_rectangle_rec(rect, button_return["clicked_color"])                     # Draw Button
    draw_text(button_return["title"].encode('utf-8'), int(rect.x + rect.width / 2 - msur_text),    # Draw Text
                int(rect.y + rect.height / 2 - 10), 20, button_return["text_color"])
    
    # Draw a button border
    draw_rectangle_lines_ex(rect, BOARDER_THICK, BORDER_COLOR)

# *************************************************************************************************** 
# Draw buttons without function association
# *************************************************************************************************** 

# Draw a button with a text and return if the mouse is over the button (Return True for close program)
def draw_return_button() -> bool:
    # Mount position and size button in a rectangle for easy use
    rect = Rectangle(button_return["x"], button_return["y"], button_return["width"], button_return["height"])

    msur_text = measure_text(button_return["title"].encode('utf-8'), 20) / 2

    # if mouser is over the button, Check collision with mouse and button
    if (check_collision_point_rec(get_mouse_position(), (rect.x, rect.y, rect.width, rect.height))):
        # If the mouse is over the button, check if the left mouse button is pressed and choose the good action
        if (is_mouse_button_pressed(MOUSE_BUTTON_LEFT)):
            button_return["is_clicked"] = True  # Set True for the button clicked

            draw_clicked_button(rect)
            # print("AAA")
            return True

        # If Mouse is over button but not clicked, Use this color of button (dict_button[button]["hover_color"])
        elif button_return["is_clicked"] == False:
            draw_rectangle_rec(rect, button_return["hover_color"])                      # Draw Button
            draw_text(button_return["title"].encode('utf-8'), int(rect.x + rect.width / 2 - msur_text),    # Draw Text
                        int(rect.y + rect.height / 2 - 10), 20, button_return["text_color"])
        
        # If Mouse is over button and is clicked but mouse not release, Use this color of button (dict_button[button]["clicked_color"])
        if button_return["is_clicked"] == True:
            draw_clicked_button(rect)
    # If Mouse is not over button and is not clicked, Use this color of button (dict_button[button]["base_color"])
    else:
        draw_rectangle_rec(rect, button_return["base_color"])         # Draw Button
        draw_text(button_return["title"].encode('utf-8'), int(rect.x + rect.width / 2 - msur_text),        # Draw Text
                    int(rect.y + rect.height / 2 - 10), 20, button_return["text_color"])
        
    # Draw a button border
    draw_rectangle_lines_ex(rect, BOARDER_THICK, BORDER_COLOR)
    return False

 # *************************************************************************************************** 

def our_input(text_affichable: str, delay: int = 0) -> str:
    first_pass: bool = True
    scroll_offset: int = 0      # The offset for the text in the box
    mouse_wheel_ct = 0          # Mouse wheel counter

    while True:
        # Get the wheel movement
        wheel_move = get_mouse_wheel_move()
        mouse_wheel_ct += wheel_move

        scroll_offset += int(wheel_move * TEXT_OFFSET)  # Ajuste with TEXT_OFFSET in pixel
        # Prevents text from scrolling higher than the 1st line
        if (scroll_offset > 0):
            scroll_offset = 0

        # Drawing begin
        begin_drawing()

        text_width = measure_text(WINDOW_TITLE.encode('utf-8'), 20)
        x_position = int(get_screen_width() / 2 - text_width / 2)
        # Clear screen with LIGHTGRAY color for reset UI at each frame (Use this color for backgroung)
        clear_background(GRAY)
        draw_text(WINDOW_TITLE.encode('utf-8'), x_position, 15, 20, DARKGRAY)
        # Draw all buttons
        action = draw_return_button()
        if (action == True and first_pass == False):
            return EXIT_CODE
        first_pass = False
    
        text_entry.update_textBox()
        entry_text = text_entry.get_text()
        text_entry.draw_self()

        # Draw text zone
        draw_rectangle_rec(TEXT_BOX, WHITE)
        # if (text_affichable):
        line_ct = adjust_text_in_box_and_draw_result(TEXT_BOX, text_affichable, 0, scroll_offset)

        # For stop scrolling down text
        if (scroll_offset * -1 / TEXT_OFFSET > line_ct): # * -1 for compare scroll_offset (Is negative) with the number of line (ex: scroll_offset = -13 is = to line_ct = 13)
            scroll_offset = line_ct * -1 * TEXT_OFFSET

        end_drawing()

        if (entry_text):
            return entry_text
        # To use our_input like a sleep with a print()
        if (delay):
            sleep(delay)
            return None