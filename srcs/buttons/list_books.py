from data_store import dict_button, dict_books, dict_users, loans_list_dict
from text_entry import TextEntry

##########################################################################################

class ListBooks:
    def __init__(self):
        print("ListBooks class init")

    def on_start(self):
        print("")

    def update(self, text_entry: TextEntry):
        print("ListBooks Update")
        return "ListBooks Update"

##########################################################################################

# # List the most borrowed books
# def list_books(button: str):
#     print(f"{button} button Hit Action 4")
