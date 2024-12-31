from pyray import * # Import for Raylib
from init import *
from buttons_functions import *
from my_button import *

def adjust_text_in_box_and_draw_result(box: Rectangle, text: str, line_position: int = 0):
    text_width = measure_text(text.encode('utf-8'), 20)
    line_height = 22
    writable_length = int(box.width - 20)

    if text_width > writable_length:
        line = text[:int(writable_length / 10.2)]
        text = text[int(writable_length / 10.2):]

        adjust_text_in_box_and_draw_result(box, text, line_height + line_position)
        draw_text(line, int(box.x + 10), int(box.y + line_position), 20, BLACK)
    else:
        draw_text(text, int(box.x + 10), int(box.y + line_position), 20, BLACK)

def main():

    init()

    # For Quit the main loop for exit programm
    quit_ct: bool = False
    affich_text: str = lorem

    while (not quit_ct and not window_should_close()):    # Detect window close on x corner click or escape key
        # Drawing begin
        begin_drawing()
        
        # Clear screen with LIGHTGRAY color for reset UI at each frame (Use this color for backgroung)
        clear_background(LIGHTGRAY)     

        # Draw title text
        text_width = measure_text(WINDOW_TITLE.encode('utf-8'), 20)
        x_position = int(get_screen_width() / 2 - text_width / 2)

        # Draw all buttons
        for button_key in dict_button:
            button = dict_button[button_key]
            if isinstance(button, MyButton):
                text = button.draw_button()
                if text is not None and text != "Quitter":
                    affich_text = text
                if (text == "Quitter"):
                    quit_ct = True
        
        # Draw text zone
        draw_rectangle(10, int(WINDOW_HEIGHT / 4 * 3), int(WINDOW_WIDTH - 20), int(WINDOW_HEIGHT / 4 - 10), WHITE)
        # draw_text(affich_text, 20, int(WINDOW_HEIGHT / 4 * 3) + 10, 20, BLACK)
        adjust_text_in_box_and_draw_result(Rectangle(10, int(WINDOW_HEIGHT / 4 * 3), int(WINDOW_WIDTH - 20), int(WINDOW_HEIGHT / 4 - 10)), affich_text)

        draw_text(WINDOW_TITLE.encode('utf-8'), x_position, 15, 20, DARKGRAY)

        end_drawing()

    # Close windows and openGL context properly at exit
    close_window()

main()
