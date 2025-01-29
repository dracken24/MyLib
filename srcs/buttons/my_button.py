from pyray import Rectangle, Vector2, DARKGRAY, GRAY, LIGHTGRAY, WHITE, BLACK
from pyray import check_collision_point_rec, get_mouse_position, is_mouse_button_down, MOUSE_BUTTON_LEFT
from pyray import draw_rectangle_rec, draw_text, draw_rectangle_lines_ex, is_mouse_button_released

BOARDER_THICK = 2
BORDER_COLOR = DARKGRAY

class MyButton: 
    # Constructor
    def __init__(self, associate_class, x: float, y: float, width: float, height: float,
                number: int, bgColor = GRAY, clickColor = WHITE, hoverColor = LIGHTGRAY,
                    font_color = BLACK, title: str = "", text: str = "", font_size: int = 20):
        self.__rect = Rectangle(x, y, width, height)
        self.bgColor = bgColor
        self.clickColor = clickColor
        self.hoverColor = hoverColor
        self.is_clicked = False
        self.title = title
        self.text = text
        self.text_color = font_color
        self.font_size = font_size
        self.measure_text: int = 0
        self.__associate_class = associate_class
        self.__number = number

    # Member Functions

    def draw_button(self, skip_update: bool = False) -> int:
        text_pos = Vector2(self.__rect.x + self.__rect.width / 2 - self.measure_text, 
                        self.__rect.y + self.__rect.height / 2 - self.font_size / 2)

        if check_collision_point_rec(get_mouse_position(), self.__rect) and not skip_update:
            if is_mouse_button_down(MOUSE_BUTTON_LEFT):
                draw_rectangle_rec(self.__rect, self.clickColor)
                draw_text(self.title.encode('utf-8'), int(text_pos.x), int(text_pos.y),
                          self.font_size, self.text_color)
                
                if not self.is_clicked:
                    print("Clicked on: ", self.text)
                    self.is_clicked = True
                    # self.associate_class.update() # Lunch function update in class link
                    return self.__number

                draw_rectangle_lines_ex(self.__rect, BOARDER_THICK, BORDER_COLOR)
                return None

            if is_mouse_button_released(MOUSE_BUTTON_LEFT):
                self.is_clicked = False

            draw_rectangle_rec(self.__rect, self.hoverColor)
            draw_text(self.title.encode('utf-8'), int(text_pos.x), int(text_pos.y),
                self.font_size, self.text_color)
            
        else:
            draw_rectangle_rec(self.__rect, self.bgColor)
            draw_text(self.title.encode('utf-8'), int(text_pos.x), int(text_pos.y),
                    self.font_size, self.text_color)

        draw_rectangle_lines_ex(self.__rect, BOARDER_THICK, BORDER_COLOR)
        return None
    
    def __str__(self):
        return f"Button name: {self.title}"

########################################################################
                                # GET
########################################################################

    def get_text(self):
        return self.text
    
    def get_title(self):
        return self.title
    
    def get_is_clicked(self):
        return self.is_clicked
    
    def get_number(self):
        return self.__number
    
    def get_associate_class(self):
        return self.__associate_class

########################################################################
                                # SET
########################################################################

    def set_bg_color(self, color):
        self.bgColor = color

    def set_text(self, text: str):
        self.text = text

    def set_mesure_text(self, len: int):
        self.measure_text = len

    def set_is_clicked(self, is_clicked: bool):
        self.is_clicked = is_clicked
