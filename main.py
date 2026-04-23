import random

current_madlib = input('Which madlib would you like to do? ')
open_madlib = open(current_madlib)

questions = ['What is the name of your first pet? ', 'What is something that smells weird? ', 'Name your favorite food. ']

# Madlib txt file indication being _n, _v, _a or something of that nature. 
noun = ['What is the name of your first pet? ']
verb = []
adjective = [] 

replace = ''
updated_madlib = ''

# Iterates through each line of the madlib
for the_line in open_madlib:
    # Checks for blanks requiring a noun and prompts user. 
    while '_n' in the_line:
        replace = input(random.choice(noun))
        the_line = the_line.replace('_n', replace, 1)

    # Checks for blanks requiring a verb and prompts user. 
    while '_v' in the_line:
        replace = input(random.choice(verb))
        the_line = the_line.replace('_v', replace, 1)

    # Checks for blanks requiring an adjective and prompts user. 
    while '_a' in the_line:
        replace = input(random.choice(adjective))
        the_line = the_line.replace('_a', replace, 1)
    
    # Adds line to updated madlib with blanks filled.
    updated_madlib += the_line

print(updated_madlib)

open_madlib.close()


