import random
import os
# Starter file for students to create a Random Quote Generator

# Step 1: Import any necessary modules
# Step 2: Define a function to load quotes from a file when called
# Step 3: Define a function that returns a random quote when called
# Step 4: Define a main function that runs the program. Make sure to call the function.

# Functions takes in filename parameter and returns list of strings with lines from file
def load_quotes(filename):
    with open(filename, 'r') as file:
        quotes = file.readlines()
    return quotes

# Function takes in list of strings and randomly chooses one to return
def get_random_quote(quotes):
    random_num=random.randint(0,len(quotes)-1)
    return quotes[random_num].strip()

# Runs program. Main() is the only function called so that it calls the other functions appropriately and controls logic flow.
def main():
    print(get_random_quote(load_quotes("quotes.txt")))

main()





