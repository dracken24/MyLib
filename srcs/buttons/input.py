from init import dict_button

# Entry point for text
def input_text(button: str):
    dict_button["input"]["text"] = input("Que voulez-vous faire?")
    print(f"{button} button Hit Action 11 input text")
