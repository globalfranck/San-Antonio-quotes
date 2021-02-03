quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes ! ",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre"
]

characters = [
    "alvin et les Chipmunks",
    "Babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "kirikou"
]

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

def show_random_quote(my_list):
    # get a random number from the random library
    quote = my_list[1]
    return quote

while user_answer != "B":
    print( show_random_quote(quotes) )
    user_answer = "B"
