from init import dict_button, dict_books
from utility import our_input, BASE_CHOICE_STR

# List the most borrowed books - DONE
def list_books(button: str):
    print(f"{button} button Hit Action 4")
    count = 0
    affich_text = "--- Lister les livres les plus empruntés  ---\n"

    print(verifier_livre_emprunt())

    if dict_books == {} or verifier_livre_emprunt() == False:
        affich_text += "\n" + ("-" * 30)
        affich_text += "\nAucun livre enregistré.\n"
        affich_text += "-" * 30 + "\n\n"
        our_input(affich_text + BASE_CHOICE_STR)
        return

    else:
        affich_text += "\n" + ("-" * 30) + "\n"
        affich_text += "* Les 5 livres les plus empruntés :\n"
        affich_text += ("-" * 30) + "\n\n"

        for s in sorted(dict_books.items(), key=lambda v: v[1]['Emprunts'], reverse=True)[:5]:
            count += 1
            #affich_text += f'{count}. "{s[0]}": {s[1]["Emprunts"]} emprunt(s)\n'
            affich_text += f'* #{count}. "{s[0]}" - Emprunts : {s[1]["Emprunts"]}\n'
        affich_text += "\n" + "-" * 30 + "\n"
        affich_text += '\n'
        our_input(affich_text +  BASE_CHOICE_STR)

def verifier_livre_emprunt():
    for book in dict_books:
        if dict_books[book]["Emprunts"] != 0:
            return True
    return False