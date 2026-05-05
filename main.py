##Main.py
import random

current_madlib = input('Which madlib would you like to do? ')
open_madlib = open(current_madlib)

# Madlib txt file indication being _n, _v, _a or something of that nature. 
noun = ['What is the name of your first pet? ', 'What was your favorite childhood toy? ', 'Name a place you have always wanted to vist. ', 'What is an object you use everyday? ', 'Name a funny looking animal ', 'What is a type of food you love? ', 'What is your dream job? ', 'Name your favorite Harry Potter character. ', 'What is a holiday you enjoy? ', 'Name something you would see in the sky. ',     'What is the weirdest animal you can think of? ',
    'What place would you absolutely not want to visit alone? ',
    'What is the most dramatic name you can imagine? ',
    'What food would you eat every day if it had zero calories? ',
    'What random object would make a terrible hat? ',
    'What job would be hilarious to have for one day? ',
    'What body part do you wish had its own personality? ',
    'What vehicle would you ride to look ridiculously cool? ',
    'What room in a house is secretly the most suspicious? ',
    'What clothing item would you wear backwards on purpose? ',
    'What type of weather feels personally offensive? ',
    'What liquid would you never drink even for $100? ',
    'What plant looks like it might be plotting something? ',
    'What building would you hide in during a zombie apocalypse? ',
    'What country would you go to just for the snacks? ',
    'What type of music would aliens probably enjoy? ',
    'What tool would you use to fix absolutely everything? ',
    'What piece of furniture would win in a fight? ',
    'What school subject deserves its own movie? ',
    'What holiday would be better if it lasted a month? ']
verb = ['Favorite way to get to classes. ', 'Something you do when you are bored. ', 'Favorite mode of travel. ','Something you do before a party. ','An action you would do on a summer day. ', 'A verb related to studying. ','Something that makes you laugh. ','A verb related to the kitchen. ',     'What is something you would do if no one was watching? ',
    'What is a weird way to start your morning? ',
    'What is something you should definitely not do in public? ',
    'What is something a superhero might do on a day off? ',
    'What is something you would do to impress a cat? ',
    'What is something you might do in zero gravity? ',
    'What is something you would do if you turned invisible? ',
    'What is something you would do in a haunted house? ',
    'What is something you would do if you won the lottery instantly? ',
    'What is something you would do during a boring class? ',
    'What is something you would do if you met an alien? ',
    'What is something you would do to survive on a deserted island? ',
    'What is something you would do with unlimited free time? ',
    'What is something you would do if gravity stopped working? ',
    'What is something you would do to annoy your best friend? ',
    'What is something you would do if you woke up as a giant? ',
    'What is something you would do if you could time travel? ',
    'What is something you would do if you found a treasure chest? ',
    'What is something you would do in the middle of a dance battle? ',
    'What is something you would do if you were the ruler of the world for a day? ']
adjective = ['Describe your spring semester. ','How do you feel today? ','Describe your favorite food. ','A word for the science center. ','Describe the state of your dorm room. ','A word describing your favorite song. ','Describe Harvard Square. ','A word for Annenberg. ',     'What is a word to describe how you feel on a Monday morning? ',
    'What is a word to describe your dream vacation? ',
    'What is a word to describe a suspicious-looking sandwich? ',
    'What is a word to describe a cat wearing sunglasses? ',
    'What is a word to describe your favorite snack? ',
    'What is a word to describe a haunted house at midnight? ',
    'What is a word to describe your best friend? ',
    'What is a word to describe a dance move gone wrong? ',
    'What is a word to describe a superhero outfit? ',
    'What is a word to describe a very bad haircut? ',
    'What is a word to describe a roller coaster ride? ',
    'What is a word to describe a mystery box? ',
    'What is a word to describe a rainy day? ',
    'What is a word to describe a really loud concert? ',
    'What is a word to describe a talking dog? ',
    'What is a word to describe a broken robot? ',
    'What is a word to describe a giant pizza? ',
    'What is a word to describe a science experiment gone wrong? ',
    'What is a word to describe a secret hideout? ',
    'What is a word to describe a movie that makes no sense? '] 

#Shuffle questions list
random.shuffle(noun)
random.shuffle(verb)
random.shuffle(adjective)
replace = ''
updated_madlib = ''

# Iterates through each line of the madlib
for the_line in open_madlib:
    # Checks for blanks requiring a noun and prompts user. 
    while '_n' in the_line:
        question = noun.pop() if noun else 'Enter a noun: ' #pop from question bank or tell them to put a noun
        replace = input(question) #change to input quesiton
        the_line = the_line.replace('_n', replace, 1)

    # Checks for blanks requiring a verb and prompts user. 
    while '_v' in the_line:
        question = verb.pop() if noun else 'Enter a verb: '
        replace = input(question)
        the_line = the_line.replace('_v', replace, 1)

    # Checks for blanks requiring an adjective and prompts user. 
    while '_a' in the_line:
        question = adjective.pop() if adjective else 'Enter a adjective: '
        replace = input(question)
        the_line = the_line.replace('_a', replace, 1)
    
    # Adds line to updated madlib with blanks filled.
    updated_madlib += the_line

print(updated_madlib)

open_madlib.close()


