from pyray import window_should_close, get_mouse_wheel_move, is_mouse_button_released, begin_drawing, clear_background, draw_text, measure_text, draw_rectangle_rec, end_drawing, close_window, LIGHTGRAY, get_screen_width,MOUSE_BUTTON_LEFT # Import for Raylib
from init import *
from utility import *
from buttons.button import draw_button

""" Main function for run the programm """
# lorem is to test the text box
lorem: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. EXIT."
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
        for button in dict_button:
            quit_ct, text, action = draw_button(button)
            if (action == True and text != "Exit"):
                affich_text = text
        
        # Draw text zone
        text_box: Rectangle = Rectangle(10, int(WINDOW_HEIGHT / 4 * 3), int(WINDOW_WIDTH - 20), int(WINDOW_HEIGHT / 4 - 10)) # Make rectangle from values
        draw_rectangle_rec(text_box, WHITE)
        
        # Passage explicite du scroll_offset
        line_ct = adjust_text_in_box_and_draw_result(text_box, affich_text, 0, scroll_offset)

        # For stop scrolling down text
        if (scroll_offset * -1 / TEXT_OFFSET > line_ct): # * -1 for compare scroll_offset (Is negative) with the number of line (ex: scroll_offset = -13 is = to line_ct = 13)
            scroll_offset = line_ct * -1 * TEXT_OFFSET

        # Draw the title
        draw_text(WINDOW_TITLE.encode('utf-8'), x_position, 15, 20, DARKGRAY)

        end_drawing()

        # Reset color clicked when relese mouse button
        if (is_mouse_button_released(MOUSE_BUTTON_LEFT)):
            for button_key in dict_button:
                button = dict_button[button_key]
                if (button["is_clicked"] == True):
                    button["is_clicked"] = False

    # Close windows and openGL context properly at exit
    close_window()

main()
