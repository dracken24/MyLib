from data_store import dict_button, dict_books, dict_users, loans_list_dict
from text_entry import TextEntry

##########################################################################################

class MonthlyEvolution:
    def __init__(self):
        print("MonthlyEvolution class init")

    def on_start(self):
        print("")

    def update(self, text_entry: TextEntry):
        print("MonthlyEvolution Update")
        return "MonthlyEvolution Update"
        
##########################################################################################
    