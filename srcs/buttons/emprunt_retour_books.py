from init import dict_button, dict_books, dict_users, loans_list_dict

# Record a loan or return
def emprunt_retour_books(button: str):
    print(f"{button} button Hit Action 3")

    # Confirm user
    while True:
        user_id = input("Entrez l'ID d'utilisateur : ")
        if user_id in dict_users.keys():
            print("User found!")
            break
        else:
            print("User not found!")
    print(f"still here?: {user_id}")

    # Confirm livre
    dict_button["input"]["text"] = input("Entrez un livre : ")
    book_title = dict_button["input"]["text"].title()

    if book_title in dict_books.keys():
        print("Book found!")
        for loan in loans_list_dict:
            if int(user_id) == loan["Utilisateur_ID"] and book_title == loan["Livre"]:
                print(True)
                if loan["Date_Retour"] == None:
                    print("This is a return!")
                    return
        print("This is a loan, in theory?")
        return
    else:
        print("Book not found!")
    return

    #print(f"{button} button Hit Action 11 input text")