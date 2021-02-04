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

# function to obtain a random item from a list

def get_random_item(my_list):
    # get a random number from the random library
    rand_number = random.randint(0, len(my_list) - 1)   
    # choose a random item inside of the list (characters or quotes)
    item = my_list[rand_number]
    return item

# function to capitalize each words (characters are not capitalize)

def capitalize(words):
    for word in words:
        word.capitalize()

# function to create a message which is comprised of the characters name and its quote
        
def message(character, quote):
    """capitalize(character)
    capitalize(quote)"""
    return f"{character.capitalize()} a dit : {quote.capitalize()}"

# First interaction with the user : launching or not the loop

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

# If user enters B => end the program, otherwise launch the program and show a random quote

while user_answer != "B" :
    print( message( get_random_item(characters), get_random_item(quotes)) )
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")
