 # Import for Raylib
from pyray import measure_text, text_subtext, draw_line_ex, begin_scissor_mode, end_scissor_mode, is_mouse_button_pressed
from pyray import Vector2 ,Color, draw_rectangle_rec, draw_rectangle_lines_ex, draw_text, check_collision_point_rec
from pyray import get_char_pressed, is_key_down, get_frame_time, text_subtext, fmaxf, Rectangle, get_mouse_position
from pyray import get_mouse_position, check_collision_point_rec, set_mouse_cursor, is_mouse_button_pressed
from pyray import MOUSE_CURSOR_IBEAM, MOUSE_LEFT_BUTTON, MOUSE_CURSOR_DEFAULT, KEY_BACKSPACE, KEY_REPEAT_DELAY, KEY_REPEAT_RATE
from pyray import LIGHTGRAY, LIGHTDARKGREEN, MAROON, DARKGRAY, BLACK
from pyray import KEY_DELETE, KEY_LEFT, KEY_RIGHT

class TextEntry:
	def __init__(self, x: float, y: float, width: float, height: float):
		rect: Rectangle = { x, y, width, height }
		text: str = ""
		text_size: int = 0
		cursorPosition: int = 0
		textOffset: int = 0
		is_active: bool = False
		font_size: int = 20
		spacing: int
		fontColor: Color = BLACK

		isBackspaceHeld: bool = False
		isDeleteHeld: bool = False
		isLeftArrowHeld: bool = False
		isRightArrowHeld: bool = False

	def draw_self(self):
		draw_rectangle_rec(self.rect, LIGHTGRAY)
		draw_rectangle_lines_ex(self.rect, 2, LIGHTDARKGREEN if self.is_active else DARKGRAY)

		pos: Vector2 = {self.rect.x + 5 - self.textOffset, self.rect.y + (self.rect.height - self.fontColor) / 2}
		
		# Draw the text with a clipping rectangle
		begin_scissor_mode(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
		if (self.text_size > 0):
			draw_text(self.text, self.rect.x, self.rect.y, self.font_size, self.fontColor)
		end_scissor_mode()
		
		# Draw the cursor
		if (self.is_active):
			cursor_x: float = pos.x + measure_text(text_subtext(self.text, 0, self.cursorPosition), self.font_size).x
			if (cursor_x >= self.rect.x and cursor_x <= self.rect.x + self.rect.width):
				draw_line_ex(Vector2(cursor_x, self.rect.y + 2), 
						Vector2(cursor_x, self.rect.y + self.rect.height - 2), 
						2, MAROON)

	def	update_textBox(self, adjust: Rectangle):

		mousePoint: Vector2 = get_mouse_position()
		adjustedRect: Rectangle = {
			self.rect.x + adjust.x,
			self.rect.y + adjust.y,
			self.rect.width,
			self.rect.height
		}

		if (check_collision_point_rec(mousePoint, adjustedRect)):
			set_mouse_cursor(MOUSE_CURSOR_IBEAM)
			if (is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):
				self.is_active = True
		else:
			set_mouse_cursor(MOUSE_CURSOR_DEFAULT)
			if (is_mouse_button_pressed(MOUSE_LEFT_BUTTON)):
				self.is_active = False

		if (self.is_active):
			key: int = get_char_pressed()
			while (key > 0):
				if ((key >= 32) and (key <= 125) and (self.text_size < self.maxLength)):
					self.text[self.cursorPosition] = chr(key)
					self.cursorPosition += 1
				
				key = get_char_pressed()

			# Backspace key handling
			if (is_key_down(KEY_BACKSPACE)):
				if (not self.isBackspaceHeld):
					if (self.cursorPosition > 0):
						self.text_size -= 1
						self.cursorPosition -= 1

					self.isBackspaceHeld = True
				else:
					self.backspaceTimer += get_frame_time()
					if (self.backspaceTimer > KEY_REPEAT_DELAY):
						if (self.cursorPosition > 0 and self.backspaceTimer - KEY_REPEAT_DELAY > KEY_REPEAT_RATE):
							self.text_size -= 1
							self.cursorPosition -= 1
			else:
				self.isBackspaceHeld = False

			# Delete key handling
			if (is_key_down(KEY_DELETE)):
				if (not self.isDeleteHeld):
					if (self.cursorPosition < self.text_size):
						self.text_size -= 1
					self.isDeleteHeld = True
				else:
					if (self.cursorPosition < self.text_size):
						self.text_size -= 1
			else:
				self.isDeleteHeld = False

			# Left arrow key handling
			if (is_key_down(KEY_LEFT)):
				if (not self.isLeftArrowHeld):
					if (self.cursorPosition > 0):
						self.cursorPosition -= 1
					self.isLeftArrowHeld = True
				else:
					if (self.cursorPosition > 0):
						self.cursorPosition -= 1
			else:
				self.isLeftArrowHeld = False

			# Right arrow key handling
			if (is_key_down(KEY_RIGHT)):
				if (not self.isRightArrowHeld):
					if (self.cursorPosition < self.text_size):
						self.cursorPosition += 1

					self.isRightArrowHeld = True
				else:
					if (self.cursorPosition < self.text_size):
						self.cursorPosition += 1
			else:
				self.isRightArrowHeld = False

			# Adjust the text offset
			visible_width: float = self.rect.width - 10;  # 10 pixels of margin
			textWidth: float = measure_text(self.text, self.font_size, self.spacing).x
			cursor_x: float = measure_text(text_subtext(self.text, 0, self.cursorPosition), self.font_size, self.spacing).x

			# Adjust the text offset so the cursor is always visible
			if (cursor_x - self.textOffset > visible_width):
				self.textOffset = cursor_x - visible_width + self.font_size
			elif (cursor_x - self.textOffset < 0):
				self.textOffset = cursor_x

			# Ensure the text doesn't go too far to the left
			if (textWidth - self.textOffset < visible_width and textWidth > visible_width):
				self.textOffset = textWidth - visible_width

			# Ensure the offset is never negative
			self.textOffset = fmaxf(0, self.textOffset)
