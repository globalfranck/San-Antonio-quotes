# Import random module in order to use the randint method to get a random integer
import random

quotes = [
    "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes ! ",
    "On doit pouvoir choisir entre s'écouter parler et se faire entendre"
]

characters = [
    "alvin et les chipmunks",
    "babar",
    "betty boop",
    "calimero",
    "casper",
    "le chat potté",
    "kirikou"
]

def get_random_item(my_list):
    # get a random number from the random library
    rand_number = random.randint(0, len(my_list) - 1)    
    quote = my_list[rand_number]
    return quote

def capitalize(words):
    for word in words:
        word.capitalize()

def message(character, quote):
    """capitalize(character)
    capitalize(quote)"""
    return f"{character.capitalize()} a dit : {quote.capitalize()}"

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

while user_answer != "B" :
    print( message( get_random_item(characters), get_random_item(quotes)) )
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")
