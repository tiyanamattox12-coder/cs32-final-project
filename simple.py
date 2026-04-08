import random

current_madlib = input('Which madlib would you like to do? ')
open_madlib = open(current_madlib)

questions = ['What is the name of your first pet? ', 'What is something that smells weird? ', 'Name your favorite food. ']

replace = ''
updated_madlib = ''

for the_line in open_madlib:
    i = 0
    while i < len(the_line):
        if the_line[i] == '_':
            replace = input(random.choice(questions))
            the_line = the_line.split('_', 1)
            the_line[0] += replace
            the_line = the_line[0] + the_line[1]
            updated_madlib += the_line

        i += 1

print(updated_madlib)
