# Create a Mad Libs program that reads in text files and lets the user
# add their own text anywhere the word ADJECTIVE, NOUN, ADVERB, or VERB
# appears in the text file.
# For example, a text file may look like this:
"""
The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.
The program would find these occurrences and prompt the user to replace
them:
"""

"""
Enter an adjective:
silly
Enter a noun:
chandelier
Enter a verb:
screamed
Enter a noun:
pickup truck
"""
# It would then create the following text file:
"""
The silly panda walked to the chandelier and then screamed. A nearby
pickup truck was unaffected by these events.
"""

from pathlib import Path

BASE_DIR = Path.home() / 'Desktop' / 'atbswp' / 'ch10'/ 'mad_libs'

def save_story(adj, noun1, verb, noun2, mode):
    story = f"The {adj} panda walked to the {noun1} and then {verb}. A nearby {noun2} was unaffected by these events."
    mad_libs_file = BASE_DIR / 'mad_libs_write.txt'
    with open(mad_libs_file, mode, encoding='utf-8') as file:
        file.write(story + '\n\n')

def main():

    current_mode = 'w' # sets the mode
    
    while True:
        adj = input("Enter an adjective:\n") #clumsy, invisible, grumpy
        noun1 = input("Enter a noun:\n") # set 1: trampoline, hot tub, vending machine
        verb = input("Enter a verb:\n") # backflipped, fainted, applauded
        noun2 = input("Enter a noun:\n") # set 2: lawnmower, subway train, potato

        save_story(adj, noun1, verb, noun2, current_mode)
        print("Story saved succesfully!")

        current_mode = 'a'

        choice = input("Would you like to make another story? (y/n): ")
        if choice.lower() != 'y':
            print("Session ended.")
            break

if __name__ == "__main__":
    main()
