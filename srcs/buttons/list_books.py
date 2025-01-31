from init import dict_button, dict_books
#from init import dict_button, dict_books, dict_users, loans_list_dict
#from sipbuild.generator import resolve

# List the most borrowed books - DONE
def list_books(button: str):
    print(f"{button} button Hit Action 4")
    count = 0
    print("\n\033[1m\033[4m--Liste des 5 livres les plus empruntés--\033[0m")
    dict_button[button]["text"] = "- - Liste des 5 livres les plus empruntés - -"
    for s in sorted(dict_books.items(), key=lambda v: v[1]['Emprunts'], reverse=True)[:5]:
        count += 1
        print(f'{count}. "{s[0]}": {s[1]["Emprunts"]} emprunt(s)')
        dict_button[button]["text"] += f'\n{count}. "{s[0]}": {s[1]["Emprunts"]} emprunt(s)'