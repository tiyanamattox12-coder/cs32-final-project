##Madlibmaker.py
import random

noun = []
verb = []
adjective = [] 

new_madlib = ''

# Setting up user noun questions
n = 1
while n == 1: 
    noun_questions = input('What noun questions would you like to ask? ')
    noun.append(noun_questions)
    n = int(input('Would you like to continue? 1 for yes, 0 for no. '))

# Setting up user verb questions
v = 1
while v == 1: 
    verb_questions = input('What verb questions would you like to ask? ')
    verb.append(verb_questions)
    v = int(input('Would you like to continue? 1 for yes, 0 for no. '))

# Setting up user adjective questions 
a = 1
while a == 1: 
    adjective_questions = input('What adjective questions would you like to ask? ')
    adjective.append(adjective_questions)
    a = int(input('Would you like to continue? 1 for yes, 0 for no. '))

# Checking that the inputs are actually being added to the list will remove later
print(noun)
print(verb)
print(adjective)

adding_lines = '1'
while adding_lines == '1':
    madlib_add = input('Do you want to add a new line to your madlib? 1 for yes, 0 for no. ')
    if madlib_add == '1':
        new_line = input('Please add your new line. To add a noun blank insert "_n", "_v" for a verb, and "_a" for an adjective. ')
        checking = input("Is this the correct line? 1 for yes, 0 for no. ")
        if checking == '1':
            new_madlib += new_line

    else:
        adding_lines = 0 


print(new_madlib)


# Generative AI was used to help write these lines of code
save = input('Would you like to save your madlib? 1 for yes, 0 for no. ')

if save == '1':
    filename = input('Enter a file name (without .txt): ')
    
    with open(filename + '.txt', 'w') as file:
        file.write(new_madlib)
    
    print('Your madlib has been saved!')
