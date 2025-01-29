# Pour empecher les dependances circulaires entre les classes et le init

# Putt all buttons in a dictionary
dict_button: dict = { }

dict_books: dict = {
    "Python Programming": {
        "Auteur": "John Doe",
        "Genre": "Programmation",
        "Exemplaires": 5,
        "Emprunts": 10
    },
    "The Great Gatsby": {
        "Auteur": "F. Scott Fitzgerald",
        "Genre": "Roman",
        "Exemplaires": 2,
        "Emprunts": 7
    }
}

dict_users = {
    "1": {
        "Nom": "Smith",
        "Prénom": "Alice",
        "Email": "alice@gmail.com",
        "Téléphone": "514-888-9696",
        "Emprunts": 5,
        "ListeLivreLu":["Python Programming","The Great Gatsby","Marx's Inferno",
        "Atomic Habits"]
    },
    "2": {
        "Nom": "Brown",
        "Prénom": "Bob",
        "Email": "bob@gmail.com",
        "Téléphone": "430-568-8985",
        "Emprunts": 2,
        "ListeLivreLu":["Python Programming","The Great Gatsby"]
    }
}

loans_list_dict = [
    {
        "Utilisateur_ID": 1,
        "Livre": "Python Programming",
        "Date_Emprunt": "2024-12-01",
        "Date_Retour": "2024-12-10"
    },
    {
        "Utilisateur_ID": 2,
        "Livre": "The Great Gatsby",
        "Date_Emprunt": "2024-11-25",
        "Date_Retour": None
    }
]
