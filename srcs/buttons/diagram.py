from data_store import dict_button, dict_books, dict_users, loans_list_dict
from text_entry import TextEntry

class Diagram:
    def __init__(self):
        print("Diagram class init")

    def on_start(self):
        print("")
    
    def update(self, text_entry: TextEntry):
        print("Diagram Update")
        return "Diagram Update"
    
    def on_quit(self):
        print("")

# # Visualization: Pie chart of borrowings by genre
# def diagram(button: str):
#     print(f"{button} button Hit Action 8")
    