from data_store import dict_button, dict_books, dict_users, loans_list_dict, RESET_STRING
from text_entry import TextEntry

import matplotlib.pyplot as plt
import numpy as np

##########################################################################################

class Diagram:
#--------------------------------------------------------------------#

	def __init__(self):
		print("Diagram class init")

#--------------------------------------------------------------------#

	def on_start(self):
		print("")

#--------------------------------------------------------------------#
	
	def update(self, text_entry: TextEntry):
		# print("Diagram Update")
		all_emprunt: list = self.find_by_type() # mount list by gender
		self.show_graph(all_emprunt)            # show graph with values

		return RESET_STRING # Return that string to reset button selected

#--------------------------------------------------------------------#

	def find_by_type(self) -> list:

		book_found: list = []

		# Collect all gender from loans_list_dict to find gender in dict_books
		for book in loans_list_dict:
			book_name = book["Livre"]
			for b in dict_books:
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

	def show_graph(self, cathegories: list):
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

##########################################################################################

# # Visualization: Pie chart of borrowings by genre
# def diagram(button: str):
#     print(f"{button} button Hit Action 8")
	