# Import for Raylib
from pyray import window_should_close, clear_background, draw_text, end_drawing, close_window
from pyray import get_mouse_wheel_move, is_mouse_button_released, begin_drawing, measure_text
from pyray import Rectangle, draw_rectangle_rec, get_screen_width
from pyray import LIGHTGRAY, DARKGRAY, WHITE, MOUSE_BUTTON_LEFT

from init import init, dict_button
from data_store import TEXT_OFFSET, WINDOW_TITLE, WINDOW_HEIGHT, WINDOW_WIDTH, text_entry, RESET_STRING
from utility import adjust_text_in_box_and_draw_result
from buttons.my_button import MyButton

""" Main function for run the programm """

def main():

	# comment
	init()

	quit_ct: bool = False               # Counter for the exit button to quit main loop
	from data_store import affich_text  # imprt affich_text as variable
	scroll_offset: int = 0              # The offset for scroll the text in the box
	mouse_wheel_ct = 0                  # Mouse wheel counter
	line_ct: int = 0                    # Line counter

	button_clicked: MyButton = None # For stock selected button to use update function link to classes

	text_box: Rectangle = Rectangle(10, int(WINDOW_HEIGHT / 4 * 3), int(WINDOW_WIDTH - 20), int(WINDOW_HEIGHT / 4 - 10)) # Make rectangle from values
	# Draw title text
	text_width = measure_text(WINDOW_TITLE.encode('utf-8'), 20) # For center the text in window
	x_position = int(get_screen_width() / 2 - text_width / 2)
	
	while (not quit_ct and not window_should_close()):    # Detect window close on x corner click, escape key or Quit button
# ------------------------------------ Scroll the text in the box text ------------------------------------ #		
		# Get the wheel movement
		wheel_move = get_mouse_wheel_move()
		mouse_wheel_ct += wheel_move

		scroll_offset += int(wheel_move * TEXT_OFFSET)  # Ajuste with TEXT_OFFSET in pixel
		# Prevents text from scrolling higher than the 1st line
		if (scroll_offset > 0):
			scroll_offset = 0

# ---------------------------------------------------- --------------------------------------------------- #

		# Drawing begin
		begin_drawing()

		# Clear screen with LIGHTGRAY color for reset UI at each frame (Use this color for backgroung)
		clear_background(LIGHTGRAY)     

		# Draw the title
		draw_text(WINDOW_TITLE.encode('utf-8'), x_position, 15, 20, DARKGRAY)

# ------------------------------------------- Draw all Buttons ------------------------------------------- #

		# Draw all buttons
		for button_key in dict_button:
			button = dict_button[button_key]			# Get the value from the key in the button dico
			button_clicked_nbr = button.draw_button()	# Get the return from the button
			
			# if text is not None and not 9(Exit), stock button to use update function from that button
			if button_clicked_nbr is not None and button_clicked_nbr != 9:
				button_clicked = button
				button_clicked.get_associate_class().on_start() # start function for each choice
			# For Quit withe the "Quitter" button
			if (button_clicked_nbr == 9):
				quit_ct = True

		# Launch the update function from class associate to button clicked
		if (button_clicked):
			affich_text = button_clicked.get_associate_class().update(text_entry)

# ---------------------------------------------------- --------------------------------------------------- #
# -------------------------------------- Check text from text_entry -------------------------------------- #
		text_entry.get_text()
		# if (entry_text):
		# 	affich_text = entry_text

		if (affich_text == RESET_STRING):
			# button_clicked.get_associate_class().on_quit() # Quit funct
			button_clicked = None
			affich_text = "Veuillez cliquer sur un bouton pour faire un choix"

		text_entry.update_textBox()
		text_entry.draw_self()

# ---------------------------------------------------- --------------------------------------------------- #
# ------------------------------- Cut and print the text in the text zone -------------------------------- #
		
		# Draw text zone
		draw_rectangle_rec(text_box, WHITE)
		
		# Cut the text to fit in Text vieuwer box
		if (quit_ct == False):
			line_ct = adjust_text_in_box_and_draw_result(text_box, affich_text, 0, scroll_offset)

		# For stop scrolling down text
		if (scroll_offset * -1 / TEXT_OFFSET > line_ct): # * -1 for compare scroll_offset (Is negative) with the number of line (ex: scroll_offset = -13 is = to line_ct = 13)
			scroll_offset = line_ct * -1 * TEXT_OFFSET

# ---------------------------------------------------- --------------------------------------------------- #

		end_drawing()

		# Reset color clicked when relese mouse button
		if (is_mouse_button_released(MOUSE_BUTTON_LEFT)):
			for button_key in dict_button:
				button = dict_button[button_key] 
				if (button.get_is_clicked() == True):
					button.set_is_clicked(False)

	# Close windows and openGL context properly at exit
	close_window()

main()
