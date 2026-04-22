import random

current_madlib = input('Which madlib would you like to do? ')
open_madlib = open(current_madlib)

questions = ['What is the name of your first pet? ', 'What is something that smells weird? ', 'Name your favorite food. ']

# Madlib indication being _n, _v, _a or something of that nature. 
noun = ['What is the name of your first pet? ']
verb = []
adjective = [] 

replace = ''
updated_madlib = ''

for the_line in open_madlib:
    while '_n' in the_line:
        replace = input(random.choice(noun))
        the_line = the_line.replace('_n', replace, 1)
        
    updated_madlib += the_line

print(updated_madlib)

open_madlib.close()


