# from buttons.emprunt_retour_books import load_loans_csv
from init import loans_list_dict
from utility import our_input, EXIT_CODE

import matplotlib.pyplot as plt

#--------------------------------------------------------------------#

# Visualization: Monthly evolution of borrowing
def monthly_evolution(button: str):
	# load_loans_csv()

	visible_text: str = "--- Evolution mensuelle des emprunts ---\n\nQuel an voulez vous voir ? (1900-2055)"
	
	year: str = our_input(visible_text)
	if (year == EXIT_CODE):
		return

	# Calcul emprunt from selected year if year is valid
	while (True):
		# Check if year is valid
		if (year == None and not year.isspace() or not year.isdigit()):
			year = our_input(visible_text + "\n\nEntree incorect")
			if (year == EXIT_CODE):
				return
			continue

		# check if year is in good range
		if (int(year) < 1900 or int(year) > 2055):
			year = our_input(visible_text + "\n\nEntree non comprise entre (1900-2055)")
			if (year == EXIT_CODE):
				return
		# calcul all books for this year
		emprunt_list: list[str] = calcul_emprunt(year)
		# Show a graph from those datas
		Show_graphic(emprunt_list, year)
		break

#--------------------------------------------------------------------#

def calcul_emprunt(year: str) -> list[str]:
	# Initialize month_count with 0 for all months
	month_count = {str(i): '0' for i in range(1, 13)}
	
	# Count loans by month
	for loan in loans_list_dict:
		if loan["Date_Emprunt"].split("-")[0] == year:
			month = loan["Date_Emprunt"].split("-")[1].lstrip('0')  # Remove leading zero if present
			month_count[month] = str(int(month_count[month]) + 1)
	
	# Return values in order of months (1 to 12)
	return_list = [month_count[str(i)] for i in range(1, 13)]
	print("return_list: ", return_list)
	return return_list

#--------------------------------------------------------------------#

def Show_graphic(emprunt_list: list[str], year: str):
	month_names = ["Janvier", "Fevrier", "Mars", "Avril", "Mai", "Juin", "Juillet",
					"Aout", "Septembre", "Octobre", "Novembre", "Decembre"]

	# Convert string list to int list for calculation
	emprunt_list_int: list[int] = [int(x) for x in emprunt_list]
	max_value = max(emprunt_list_int)

	fig, ax = plt.subplots()
	bar_container = ax.bar(month_names, emprunt_list_int)  # Use int list
	ax.set(ylabel = "Nombre d\'emprunt", title = f"Evolution des emprunts par mois pour l\'annee {year}", ylim = (0, max_value + 1))
	ax.bar_label(bar_container, fmt='{:,.0f}')

	sceen_whide: int = 14
	sceen_height: int = 7
	fig.set_size_inches(sceen_whide, sceen_height)

	plt.show()

#--------------------------------------------------------------------#
