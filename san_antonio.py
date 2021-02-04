# Import random module in order to use the randint method to get a random integer
import random
# Import the json library to work with json external files
import json

# reading values from an external file
def read_values_from_json(file, key):
    # create an empty list
    values = []

    # open a json file with my objects
    with open(file) as f:
    # load all the data contained in this file
        data = json.load(f)
    # add each entry into my created list
    for entry in data : 
        values.append(entry[key])

    # return my completed list
    return values

# function to obtain a random item from a list
def get_random_item(my_list):
    # get a random number from the random library
    rand_number = random.randint(0, len(my_list) - 1) 
    # choose a random item inside of the list (characters or quotes)   
    quote = my_list[rand_number]
    return quote

# function to capitalize each words (characters are not capitalize)
def capitalize(words):
    for word in words:
        word.capitalize()

# function to create a message which is comprised of the characters name and its quote
def message(character, quote):
    return f"{character.capitalize()} a dit : {quote.capitalize()}"

def get_random_quote():
    all_values = read_values_from_json('quotes.json', 'quote')
    return get_random_item(all_values)

def get_random_character():
    all_values = read_values_from_json('characters.json', 'character')
    return get_random_item(all_values)

user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")

# If user enters B => end the program, otherwise launch the program and show a random quote
while user_answer != "B" :
    print( message( get_random_character(), get_random_quote()) )
    user_answer = input("Tapez entrée pour connaître une autre citation ou B pour quitter le programme.")
