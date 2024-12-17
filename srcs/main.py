import raylib

WINDOW_WIDTH: int = 400;
WINDOW_HEIGHT: int = 640;
WINDOW_TITLE: str = "IntelliSerre";

RL = raylib
FONT_COLOR = RL.DARKGRAY;

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

        RL.ClearBackground(RL.LIGHTGRAY)     # Clear screen with white color

        # Draw text
        text = "Serre Intelligente"
        text_width = RL.MeasureText(text.encode('utf-8'), 20)
        x_position = int(RL.GetScreenWidth() / 2 - text_width / 2)
        
        RL.DrawText(text.encode('utf-8'), x_position, 20, 20, RL.DARKGRAY)
        
        RL.EndDrawing()

    RL.CloseWindow()

main()

# pip install raylib

