from data_store import dict_button, dict_books, dict_users, loans_list_dict

class ListBooks:
    def __init__(self):
        print("ListBooks class init")

    def update(self):
        print("ListBooks Update")

# List the most borrowed books
def list_books(button: str):
    print(f"{button} button Hit Action 4")
