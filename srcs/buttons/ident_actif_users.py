from data_store import dict_button, dict_books, dict_users, loans_list_dict

class IdentActifUsers:
    def __init__(self):
        print("IdentActifUsers class init")

    def update(self):
        print("IdentActifUsers Update")

# Identify the most active users
def ident_actif_users(button: str):
    print(f"{button} button Hit Action 6")
