import raylib
from pyray import Rectangle

WINDOW_WIDTH: int = 400
WINDOW_HEIGHT: int = 640
WINDOW_TITLE: str = "IntelliSerre"

RL = raylib
FONT_COLOR = RL.DARKGRAY

# init principal variables for the program
def init():
    # Window init
    RL.InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'))

    # Set window resizable
    RL.SetWindowState(RL.FLAG_WINDOW_RESIZABLE)
    RL.SetWindowMinSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    RL.SetWindowMaxSize(1920, 1080)

    RL.SetTargetFPS(60);  # FPS to 60

def main():

    init()

    while (not RL.WindowShouldClose()):    # Detect window close
        # Drawing begin
        RL.BeginDrawing()
        
        # Clear screen with LIGHTGRAY color
        RL.ClearBackground(RL.LIGHTGRAY)     

        # Draw text
        text = "Serre Intelligente"
        text_width = RL.MeasureText(text.encode('utf-8'), 20)
        x_position = int(RL.GetScreenWidth() / 2 - text_width / 2)

        # Draw button
        if (draw_button("Start", int(RL.GetScreenWidth() / 2 - 100), int(RL.GetScreenHeight() / 2 - 25), 200, 50, RL.BLUE)):
            # If the mouse is over the button, check if the left mouse button is pressed
            if (RL.IsMouseButtonPressed(RL.MOUSE_BUTTON_LEFT)):
                print("Start button Hit")
            else:
                print("Start button Hovered")

        RL.DrawText(text.encode('utf-8'), x_position, 20, 20, RL.DARKGRAY)

        RL.EndDrawing()

    RL.CloseWindow()

# Draw a button with a text and return if the mouse is over the button
def draw_button(text: str, x: int, y: int, width: int, height: int, color: RL.BLUE) -> bool:
    RL.DrawRectangle(x, y, width, height, color)
    RL.DrawText(text.encode('utf-8'), int(x + width / 2 - RL.MeasureText(text.encode('utf-8'), 20) / 2), int(y + height / 2 - 10), 20, RL.WHITE)

    if (RL.CheckCollisionPointRec(RL.GetMousePosition(), Rectangle(x, y, width, height))):
        return True
    return False

main()
