from data_store import dict_button, dict_books, dict_users, loans_list_dict

class Status:
    def __init__(self):
        print("MonthlyEvolution class init")
    
    def update(self):
        print("Status Update")

# Show library status as statistics
def status(button: str):
    print(f"{button} button Hit Action 7")
    