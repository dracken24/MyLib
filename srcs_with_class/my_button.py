from pyray import * # Import for Raylib
from pyray import  Rectangle, Vector2, Color, Font

BOARDER_THICK = 2
BORDER_COLOR = DARKGRAY

class MyButton: 
#{
    # Constructor
    def __init__(self, x: float, y: float, width: float, height: float,
                bgColor = GRAY, clickColor = WHITE, hoverColor = LIGHTGRAY,
                    font_color = BLACK, text: str = "", font_size: int = 20) -> str:
    #{
        self.rect = Rectangle(x, y, width, height)
        self.bgColor = bgColor
        self.clickColor = clickColor
        self.hoverColor = hoverColor
        self.is_clicked = False
        self.text = text
        self.text_color = font_color
            
        self.font_size = font_size
        
        self.measure_text: int = 0
    #}

    # Member Functions

    def draw_button(self, skip_update: bool = False) -> str:
    #{
        text_pos = Vector2(self.rect.x + self.rect.width / 2 - self.measure_text, 
                        self.rect.y + self.rect.height / 2 - self.font_size / 2)

        if check_collision_point_rec(get_mouse_position(), self.rect) and not skip_update:
        #{
            if is_mouse_button_down(MOUSE_BUTTON_LEFT):
            #{
                draw_rectangle_rec(self.rect, self.clickColor)
                draw_text(self.text.encode('utf-8'), int(text_pos.x), int(text_pos.y),
                          self.font_size, self.text_color)
                if not self.is_clicked:
                #{
                    print("Clicked on: ", self.text)
                    self.is_clicked = True
                    return self.text
                #}

                draw_rectangle_lines_ex(self.rect, BOARDER_THICK, BORDER_COLOR)
                return None
            #}

            if is_mouse_button_released(MOUSE_BUTTON_LEFT):
            #{
                self.is_clicked = False
            #}

            draw_rectangle_rec(self.rect, self.hoverColor)
            draw_text(self.text.encode('utf-8'), int(text_pos.x), int(text_pos.y),
                self.font_size, self.text_color)
        #}
        else:
        #{
            draw_rectangle_rec(self.rect, self.bgColor)
            draw_text(self.text.encode('utf-8'), int(text_pos.x), int(text_pos.y),
                    self.font_size, self.text_color)
        #}

        draw_rectangle_lines_ex(self.rect, BOARDER_THICK, BORDER_COLOR)
        return None
    #}

########################################################################
                                # GET
########################################################################

    def get_text(self):
    #{
        return self.text
    #}

########################################################################
                                # SET
########################################################################

    def set_bg_color(self, color):
    #{
        self.bgColor = color
    #}

    def set_text(self, text: str):
    #{
        self.text = text
    #}

    def set_mesure_text(self, len: int):
    #{
        self.measure_text = len
    #}
#}
