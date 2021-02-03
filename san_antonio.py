quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes ! ",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre"
]

characters = [
    "Alvin et les Chipmunks",
    "Babar",
    "Betty Boop",
    "Calimero",
    "Casper",
    "Le chat potté",
    "Kirikou"
]

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

# Show random quote

if user_answer == "B":
    pass
# - leave the program

else: 
    pass
# - show another quote

def show_random_quote(my_list):
    # get a random number from the random library
    quote = my_list[1]
    print(quote)

show_random_quote(quotes)
