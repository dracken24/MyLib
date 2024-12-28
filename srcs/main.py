from pyray import * # Import for Raylib
from init import *
from buttons_functions import *
from button import draw_button

def main():

    init()

    # For Quit the main loop for exit programm
    quit_ct: bool = False
    affich_text: str = ""

    while (not quit_ct and not window_should_close()):    # Detect window close on x corner click or escape key
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
