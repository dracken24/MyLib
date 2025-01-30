from text_entry import TextEntry

class Exit:
    def __init__(self):
        print("Exit class init")

    def on_start(self):
        print("")

    def update(self, text_entry: TextEntry):
        print("Exit Update")
        return "Exit Update"
    
    def on_quit(self):
        print("")