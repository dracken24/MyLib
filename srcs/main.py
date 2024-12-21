import raylib
from pyray import Rectangle

WINDOW_WIDTH: int = 400
WINDOW_HEIGHT: int = 640
WINDOW_TITLE: str = "MyLib"

RL = raylib
FONT_COLOR = RL.DARKGRAY

dict_button = {
    "start": {
        "text": "Start",
        "x": 100,
        "y": 100,
        "width": 200,
        "height": 50,
        "measure_text": 0,
        "color": RL.BLUE,
        "text_color": RL.WHITE,
        "is_clicked": False,
        "action": 1
    },
    "stop": {
        "text": "Stop",
        "x": 100,
        "y": 200,
        "width": 200,
        "height": 50,
        "measure_text": 0,
        "color": RL.ORANGE,
        "text_color": RL.WHITE,
        "is_clicked": False,
        "action": 2
    }
}

# init principal variables for the program
def init():
    # Window init
    RL.InitWindow(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE.encode('utf-8'))
    RL.SetTargetFPS(60);  # FPS to 60

    # Init each text wide for center text in button
    for button in dict_button:
        dict_button[button]["measure_text"] = int(RL.MeasureText(dict_button[button]["text"].encode('utf-8'), 20) / 2)

def main():

    init()

    while (not RL.WindowShouldClose()):    # Detect window close on x corner click or escape key
        # Drawing begin
        RL.BeginDrawing()
        
        # Clear screen with LIGHTGRAY color for reset UI at each frame (Use this color for backgroung)
        RL.ClearBackground(RL.LIGHTGRAY)     

        # Draw title text
        text_width = RL.MeasureText(WINDOW_TITLE.encode('utf-8'), 20)
        x_position = int(RL.GetScreenWidth() / 2 - text_width / 2)

        # Draw all buttons
        for button in dict_button:
            draw_button(button)

        # Reset mouse left button pressed when button is released
        if RL.IsMouseButtonReleased(RL.MOUSE_BUTTON_LEFT):
            for butt in dict_button:
                # if button clicked set to True, Set it to False
                if dict_button[butt]["is_clicked"] == True:
                    dict_button[butt]["is_clicked"] = False

        RL.DrawText(WINDOW_TITLE.encode('utf-8'), x_position, 20, 20, RL.DARKGRAY)

        RL.EndDrawing()

    # Close windows and openGL context properly at exit
    RL.CloseWindow()


# Draw a button with a text and return if the mouse is over the button
def draw_button(button: str) -> bool:
    # if mouser is over the button, Check collision with mouse and button
    if (RL.CheckCollisionPointRec(RL.GetMousePosition(), Rectangle(dict_button[button]["x"], dict_button[button]["y"],
                                dict_button[button]["width"], dict_button[button]["height"]))):
        # If the mouse is over the button, check if the left mouse button is pressed and choose the good action
        if (RL.IsMouseButtonPressed(RL.MOUSE_BUTTON_LEFT)):
            dict_button[button]["is_clicked"] = True  # Set True for the button clicked

            # ***************************************Actions for Buttons*****************************************
            if dict_button[button]["action"] == 1:
                print(f"{button} button Hit Action 1")       # Action for the button start clicked
            elif dict_button[button]["action"] == 2:
                print(f"{button} button Hit Action 2")       # Action for the button stop clicked
            # *************************************************************************************************** 

        # If Mouse is over button but not clicked, Use this color of button (DARKBLUE by default)
        elif dict_button[button]["is_clicked"] == False:
            RL.DrawRectangle(dict_button[button]["x"], dict_button[button]["y"], dict_button[button]["width"], dict_button[button]["height"], RL.DARKBLUE)                      # Draw Button
            RL.DrawText(dict_button[button]["text"].encode('utf-8'), int(dict_button[button]["x"] + dict_button[button]["width"] / 2 - dict_button[button]["measure_text"]),    # Draw Text
                        int(dict_button[button]["y"] + dict_button[button]["height"] / 2 - 10), 20, dict_button[button]["text_color"])
            return True
        
        # If Mouse is over button and is clicked but mouse not release, Use this color of button (DARKGREEN by default)
        if dict_button[button]["is_clicked"] == True:
            RL.DrawRectangle(dict_button[button]["x"], dict_button[button]["y"], dict_button[button]["width"], dict_button[button]["height"], RL.DARKGREEN)                     # Draw Button
            RL.DrawText(dict_button[button]["text"].encode('utf-8'), int(dict_button[button]["x"] + dict_button[button]["width"] / 2 - dict_button[button]["measure_text"]),    # Draw Text
                        int(dict_button[button]["y"] + dict_button[button]["height"] / 2 - 10), 20, dict_button[button]["text_color"])
            return True
    # If Mouse is not over button and is not clicked, Use this color of button (Color enter by user at start)
    else:
        RL.DrawRectangle(dict_button[button]["x"], dict_button[button]["y"], dict_button[button]["width"], dict_button[button]["height"], dict_button[button]["color"])         # Draw Button
        RL.DrawText(dict_button[button]["text"].encode('utf-8'), int(dict_button[button]["x"] + dict_button[button]["width"] / 2 - dict_button[button]["measure_text"]),        # Draw Text
                    int(dict_button[button]["y"] + dict_button[button]["height"] / 2 - 10), 20, dict_button[button]["text_color"])
        return False

main()
