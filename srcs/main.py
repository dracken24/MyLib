# Import for Raylib
from pyray import window_should_close, clear_background, draw_text, end_drawing, close_window
from pyray import get_mouse_wheel_move, is_mouse_button_released, begin_drawing, measure_text
from pyray import Rectangle, draw_rectangle_rec, get_screen_width
from pyray import LIGHTGRAY, DARKGRAY, WHITE, MOUSE_BUTTON_LEFT

from init import init, text_entry, TEXT_OFFSET, WINDOW_TITLE, WINDOW_HEIGHT, WINDOW_WIDTH, dict_button, TEXT_BOX
from utility import adjust_text_in_box_and_draw_result
from buttons.button import draw_button
# from text_entry import TextEntry

""" Main function for run the programm """
# lorem is to test the text box
lorem: str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. EXIT."
def main():

    # comment
    init()

    quit_ct: bool = False       # Counter for the exit button to quit main loop
    affich_text: str = lorem    # Text visible on the textBox
    affich_text: str = "Veuillez cliquer sur un boutton pour faire un choix"    # Text visible on the textBox
    scroll_offset: int = 0      # The offset for the text in the box
    mouse_wheel_ct = 0          # Mouse wheel counter
    line_ct: int = 0            # Line counter

    
    # Draw title text
    text_width = measure_text(WINDOW_TITLE.encode('utf-8'), 20) # For center the text in window
    x_position = int(get_screen_width() / 2 - text_width / 2)
    
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

        # Draw the title
        draw_text(WINDOW_TITLE.encode('utf-8'), x_position, 15, 20, DARKGRAY)

        # Draw all buttons
        for button in dict_button:
            quit_ct, text, action = draw_button(button)
            # if (action == True and text != "Exit" and text != "skip"):
            if (action == True and text != "Exit"):
                affich_text = text

        entry_text: str = text_entry.get_text()
        if (entry_text):
            affich_text = entry_text

        text_entry.update_textBox()
        text_entry.draw_self()
        
        # Draw text zone
        draw_rectangle_rec(TEXT_BOX, WHITE)
        
        # Passage explicite du scroll_offset
        line_ct = adjust_text_in_box_and_draw_result(TEXT_BOX, affich_text, 0, scroll_offset)

        # For stop scrolling down text
        if (scroll_offset * -1 / TEXT_OFFSET > line_ct): # * -1 for compare scroll_offset (Is negative) with the number of line (ex: scroll_offset = -13 is = to line_ct = 13)
            scroll_offset = line_ct * -1 * TEXT_OFFSET

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
