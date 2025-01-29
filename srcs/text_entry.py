# Import for Raylib
from pyray import get_mouse_position, check_collision_point_rec, set_mouse_cursor, is_mouse_button_pressed
from pyray import draw_line_ex, begin_scissor_mode, end_scissor_mode, is_mouse_button_pressed
from pyray import get_char_pressed, is_key_down, text_subtext, Rectangle, get_mouse_position
from pyray import Vector2 ,Color, draw_rectangle_rec, draw_rectangle_lines_ex, draw_text
from pyray import measure_text, text_subtext, check_collision_point_rec, is_key_pressed
from pyray import MOUSE_CURSOR_IBEAM, MOUSE_LEFT_BUTTON, MOUSE_CURSOR_DEFAULT, KEY_BACKSPACE
from pyray import KEY_DELETE, KEY_LEFT, KEY_RIGHT, KEY_ENTER
from pyray import MAROON, BLACK, DARKBLUE, WHITE

LIGHTDARKGREEN = ( 0, 166, 69, 255 )

class TextEntry:
	def __init__(self, x: float, y: float, width: float, height: float):
		self.rect: Rectangle = Rectangle(x, y, width, height)
		self.text: str = ""					# visible text
		self.text_size: int = 0				# nbr of char
		self.cursor_position: int = 0		# position of the cursor
		self.text_offset: int = 1			# For adjust cursor with text
		self.is_active: bool = False		# Textbox is active by clicking on it and inactive if clicking outside it
		self.font_size: int = 20			# Fontsize for the text
		self.font_color: Color = BLACK		# color for the text

	# Draw the textbox
	def draw_self(self):
		draw_text("Entrez votre texte ici:", int(self.rect.x), int(self.rect.y) - 20, 18, BLACK) # Text above textbox entry

		draw_rectangle_rec(self.rect, WHITE) # Background box color
		draw_rectangle_lines_ex(self.rect, 2, LIGHTDARKGREEN if self.is_active else DARKBLUE) # exterior line color

		# CAdjust text with offset to add margin and center text in textBox
		text_pos_x = self.rect.x + 5 - self.text_offset
		text_pos_y = self.rect.y + (self.rect.height - self.font_size) / 2
		
		# Draw the text in a specific rectangle and cut the rest
		begin_scissor_mode(int(self.rect.x), int(self.rect.y), int(self.rect.width), int(self.rect.height))
		if (self.text_size > 0):
			draw_text(self.text, int(text_pos_x), int(text_pos_y), self.font_size, self.font_color)
		end_scissor_mode()
		
		# Draw the cursor if textBox is active by clicking on it
		if (self.is_active):
			cursor_x = text_pos_x + measure_text(text_subtext(self.text, 0, self.cursor_position), self.font_size)
			draw_line_ex(
				Vector2(cursor_x, self.rect.y + 4), 					# Starting point of the line
				Vector2(cursor_x, self.rect.y + self.rect.height - 4),	# End point of the line
				2, 														# thick
				MAROON													# Color
			)

	# update the textBox
	def	update_textBox(self):
		mouse_point: Vector2 = get_mouse_position() # Get the mouse position

		# Check collision between textBox and mouse position
		if (check_collision_point_rec(mouse_point, self.rect)):
			set_mouse_cursor(MOUSE_CURSOR_IBEAM)				# Change cursor type if mouse is over the textBox
			if (is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):	# Active textBox if mouse is clicked over the textBox
				self.is_active = True
		# Reset the cursor to default value		
		else: 
			set_mouse_cursor(MOUSE_CURSOR_DEFAULT)
			if (is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):
				self.is_active = False

		# if the textBox is active
		if (self.is_active):
			key: int = get_char_pressed() # get the key pressed on keyboard
			while (key > 0):
				# if key is printable (between 32 and 125 in ascii table)
				if ((key >= 32) and (key <= 125)): 
					# Insert char in the str, convert key int to char
					self.text = self.text[:self.cursor_position] + chr(key) + self.text[self.cursor_position:]
					self.text_size += 1			# Text_size increase by 1
					self.cursor_position += 1	# cursor_position increase by 1

				key: int = get_char_pressed()	# if pressed more than once in a frame

			# Backspace key handling
			if (is_key_down(KEY_BACKSPACE)):
				if (self.cursor_position > 0):
					# Delete character before cursor while key is held
					self.text = self.text[:self.cursor_position - 1] + self.text[self.cursor_position:]
					self.text_size -= 1
					self.cursor_position -= 1

			# Delete key handling
			if (is_key_down(KEY_DELETE)):
				if (self.cursor_position < self.text_size):
					# Delete character after cursor while key is held
					self.text = self.text[:self.cursor_position] + self.text[self.cursor_position + 1:]
					self.text_size -= 1

			# Left arrow key handling
			if (is_key_down(KEY_LEFT)):
				if (self.cursor_position > 0):
					self.cursor_position -= 1

			# Right arrow key handling
			if (is_key_down(KEY_RIGHT)):
				if (self.cursor_position < self.text_size):
					self.cursor_position += 1

			# Adjust the text offset
			visible_width = self.rect.width - 10  # Margin 10 pixels (5 to right and 5 to left of the text)
			text_width = measure_text(self.text, self.font_size)
			cursor_x = measure_text(text_subtext(self.text, 0, self.cursor_position), self.font_size)

			# if cursor is to far right, adjust offset
			if cursor_x - self.text_offset > visible_width:
				self.text_offset = cursor_x - visible_width + 10

			# if cursor is to far left, adjust offset
			elif cursor_x - self.text_offset < 0:
				self.text_offset = cursor_x - 10

			# if text is more short than the writing space, reset to 0
			if text_width <= visible_width:
				self.text_offset = 0
			# Block cursor to go to far to left
			elif text_width - self.text_offset < visible_width:
				self.text_offset = text_width - visible_width + 10

	# Reset all value and clear text
	def reset_text_entry(self):
		self.text: str = ""
		self.text_size: int = 0
		self.cursor_position: int = 0
		self.text_offset: int = 1
		self.is_active: bool = False

########################################################################
                                # GET
########################################################################

	# Get text if enter key is pressed
	def get_text(self) -> str:
		if (is_key_pressed(KEY_ENTER)):
			text_temp: str = self.text
			self.reset_text_entry()
			return text_temp
		
		return None
		
