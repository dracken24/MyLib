from pyray import * # Import for Raylib
from init import *
from buttons_functions import *
from my_button import *

"""Recursive function for draw and scroll text inside a box (rectangle)
    Args:
        box (Rectangle): Rectangle for draw text
        text (str): Text to draw
        line_position (int): Position of the line in the box
        scroll_offset (int): Scroll offset for base on mouse wheel
        line_ct (int): Text is cut in x line_ct to fix in box whide
    
    Returns:
        int: Line count
"""
def adjust_text_in_box_and_draw_result(box: Rectangle, text: str, line_position: int = 0,
                                       scroll_offset: int = 0, line_ct: int = 0) -> int:
    # Function for draw in a specific zone. (like writing text inside a box) 
    begin_scissor_mode(int(box.x), int(box.y), int(box.width), int(box.height))
    
    text_width: int = measure_text(text.encode('utf-8'), 20)    # Check if text is more whide than the box
    line_height: int = 22                                       # Space for offset each line in pixel
    writable_length: int = int(box.width - 20)                  # Writable whide space in the box (20 pixels offset)

    adjusted_y = int(box.y + line_position + scroll_offset)     # Adjust each line position in y

    # if the text is to whide for the box
    if text_width > writable_length:
        line = text[:int(writable_length / 10.2)]   # Take a line in the text base on writable_length
        text = text[int(writable_length / 10.2):]   # Erase that line from the text
        
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
    
""" Main function for run the programm """
TEXT_OFFSET = 20
def main():

    init()

    # For Quit the main loop for exit programm
    quit_ct: bool = False       # Couinter for the exit button
    affich_text: str = lorem    # Text visible on the textBox
    scroll_offset: int = 0      # The offset for the text in the box
    mouse_wheel_ct = 0          # Mouse wheel counter
    line_ct: int = 0            # Line counter

    while (not quit_ct and not window_should_close()):    # Detect window close on x corner click, escape key or Quit button
        
        # Get the wheel movement
        wheel_move = get_mouse_wheel_move()
        mouse_wheel_ct += wheel_move

        scroll_offset += int(wheel_move * TEXT_OFFSET)  # Ajuste with TEXT_OFFSET in pixel
        # Prevents text from scrolling higher than the 1st line
        if (scroll_offset > 0):
            scroll_offset = 0

        # Drawing begin
        begin_drawing()
        
        # Clear screen with LIGHTGRAY color for reset UI at each frame (Use this color for backgroung)
        clear_background(LIGHTGRAY)     

        # Draw title text
        text_width = measure_text(WINDOW_TITLE.encode('utf-8'), 20) # For center the text in window
        x_position = int(get_screen_width() / 2 - text_width / 2)

        # Draw all buttons
        for button_key in dict_button:
            button = dict_button[button_key] # Get the value from the key in the button dico
            text = button.draw_button()      # Get the return from the button
            # Get the text from the return of a button and affich it on the textBox if text is not None
            if (text is not None and text != "Quitter"): 
                affich_text = text
            # For Quit withe the "Quitter" button
            if (text == "Quitter"):
                quit_ct = True
        
        # Draw text zone
        text_box: Rectangle = Rectangle(10, int(WINDOW_HEIGHT / 4 * 3), int(WINDOW_WIDTH - 20), int(WINDOW_HEIGHT / 4 - 10)) # Make rectangle from values
        draw_rectangle_rec(text_box, WHITE)
        
        # Passage explicite du scroll_offset
        line_ct = adjust_text_in_box_and_draw_result(text_box, affich_text, 0, scroll_offset, line_ct)

        # For stop scrolling down text
        if (scroll_offset * -1 / TEXT_OFFSET > line_ct): # * -1 for compare scroll_offset (Is negative) with the number of line (ex: scroll_offset = -13 is = to line_ct = 13)
            scroll_offset = line_ct * -1 * TEXT_OFFSET

        # Draw the title
        draw_text(WINDOW_TITLE.encode('utf-8'), x_position, 15, 20, DARKGRAY)

        end_drawing()

        line_ct = 0

    # Close windows and openGL context properly at exit
    close_window()

main()
