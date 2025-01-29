from data_store import dict_button, dict_books, dict_users, loans_list_dict

class CalculEmpruntBooks:
    def __init__(self):
        print("CalculEmpruntBooks class init")

    def update(self):
        print("CalculEmpruntBooks Update")

# Calculate the average duration of loans by type
def calcul_emprunt_books(button: str):
    print(f"{button} button Hit Action 5")
