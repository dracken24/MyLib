from data_store import dict_button, dict_books, dict_users, loans_list_dict

class Diagram:
    def __init__(self):
        print("Diagram class init")
    
    def update(self):
        print("Diagram Update")

# Visualization: Pie chart of borrowings by genre
def diagram(button: str):
    print(f"{button} button Hit Action 8")
    