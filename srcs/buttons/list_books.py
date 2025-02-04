from init import dict_button, dict_books
from utility import our_input, BASE_CHOICE_STR
# from buttons.add_remove_books import load_books_csv
#from init import dict_button, dict_books, dict_users, loans_list_dict
#from sipbuild.generator import resolve

# List the most borrowed books - DONE
def list_books(button: str):
    print(f"{button} button Hit Action 4")
    # load_books_csv()
    count = 0
    affich_text = "--- Liste des 5 livres les plus empruntés ---\n\n"
    # print("\n\033[1m\033[4m--- Liste des 5 livres les plus empruntés ---\033[0m")
    # dict_button[button]["text"] = "- - Liste des 5 livres les plus empruntés - -"
    for s in sorted(dict_books.items(), key=lambda v: v[1]['Emprunts'], reverse=True)[:5]:
        count += 1
        affich_text += f'{count}. "{s[0]}": {s[1]["Emprunts"]} emprunt(s)\n'
        # print(f'{count}. "{s[0]}": {s[1]["Emprunts"]} emprunt(s)')
        # dict_button[button]["text"] += f'\n{count}. "{s[0]}": {s[1]["Emprunts"]} emprunt(s)'
    affich_text += '\n'
    our_input(affich_text +  BASE_CHOICE_STR)