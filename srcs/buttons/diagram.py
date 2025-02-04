# from buttons.emprunt_retour_books import load_loans_csv
# from buttons.add_remove_books import load_books_csv
from init import dict_books, loans_list_dict

import matplotlib.pyplot as plt
import numpy as np

#--------------------------------------------------------------------#
# Visualization: Pie chart of borrowings by genre
def diagram(button: str):
    print(f"{button} button Hit Action 8")
    # load_loans_csv()
    # load_books_csv()
    for ele in loans_list_dict:
        print("Ele: ", ele)
    all_emprunt: list = find_by_type() # mount list by gender
    show_graph(all_emprunt)            # show graph with values


#--------------------------------------------------------------------#

def find_by_type() -> list:

    book_found: list = []

    # Collect all gender from loans_list_dict to find gender in dict_books
    for book in loans_list_dict:
        book_name = book["Livre"]
        print(f"book_name: {book_name}")
        for b in dict_books:
            print(f"book_name: {book_name} b: {b}")
            if (book_name == b):
                book_genre = dict_books[b]["Genre"]
                book_found.append(book_genre) 

    # Count the nomber of book by gender in a dict
    nbr_found: dict = {}
    for genre in book_found:
        if genre in nbr_found:
            nbr_found[genre] += 1
        else:
            nbr_found[genre] = 1

    # Mount a list to fit with matplotlib viewer ex:"nbr genre"
    cathegories: list = []
    for genre, count in nbr_found.items():
        cathegories.append(f"{count} {genre}")

    return cathegories # Return the list to affich in show_graph()

#--------------------------------------------------------------------#

def show_graph(cathegories: list):
    fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))

    data = [float(x.split()[0]) for x in cathegories]
    ingredients = [x.split()[-1] for x in cathegories]


    def func(pct, allvals):
        absolute = int(np.round(pct/100.*np.sum(allvals)))
        return f"{pct:.1f}%\n({absolute:d})"

    wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                    textprops=dict(color="w"))

    ax.legend(wedges, ingredients,
            title="Genre",
            loc="center left",
            bbox_to_anchor=(1, 0, 0.5, 1))

    plt.setp(autotexts, size=8, weight="bold")

    ax.set_title("Nombre d'emprunt de livre par Genre")

    sceen_whide: int = 10
    sceen_height: int = 7
    fig.set_size_inches(sceen_whide, sceen_height)

    plt.show()

#--------------------------------------------------------------------#
