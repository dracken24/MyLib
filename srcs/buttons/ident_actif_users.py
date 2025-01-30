from data_store import dict_button, dict_books, dict_users, loans_list_dict
from text_entry import TextEntry

##########################################################################################

class IdentActifUsers:
    def __init__(self):
        print("IdentActifUsers class init")

    def on_start(self):
        print("")

    def update(self, text_entry: TextEntry):
        print("IdentActifUsers Update")
        return "IdentActifUsers Update"
    
    def on_quit(self):
        print("")

##########################################################################################

# # Identify the most active users
# def ident_actif_users(button: str):
#     print(f"{button} button Hit Action 6")
