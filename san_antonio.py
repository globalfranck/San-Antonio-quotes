# Import random and json libraries
import random
import json

# Read values from a JSON external file
def read_values_from_json(path, key):
    values = []
    # open a json file with my objects
    with open(path) as f:
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

def main_loop():
# If user enters B => end the program, otherwise launch the program and show a random quote
    while True :
        print( message( get_random_character(), get_random_quote()) )
        message_to_user = "Enter to get another quote. \n To close the program, write 'B' ")

        user_choice = input(message_to_user).upper() # caps of user input will not matter
        if user_choice == "B":
            break
# stopping the loop

if __name__ == '__main__':
    main_loop()
