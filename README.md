# cs32-final-project
My CS32 project with Tiyana and Anjali
# Project Overview
This project is a Mad Libs generator. Users are prompted to input words of specific types (nouns, verbs, adjectives, etc.), which are then inserted into pre-written story templates to create humorous and unexpected narratives.
# Motivation
Mad Libs are a classic word game that are simple to play but endlessly entertaining. We wanted to explore how a computer program can manage different text templates, handle player input, and produce creative outputs for entertainment.
# Features
* A library of story templates with labeled blanks (e.g., [NOUN], [VERB], [ADJECTIVE])
* A user-friendly interface that prompts players for words one at a time
* Support for multiple story templates so users can play again with different stories
# How main.py Works
1. The program selects a story template
2. It scans the template for blanks and identifies the part of speech needed for each
3. The user is prompted to enter a word for each blank, without seeing the story
4. Once all blanks are filled, the completed story is displayed
# Run it!
1. In terminal enter python3 main.py
2. User will be prompted to input the Madlib text number they would like to run.
3. User will be prompted to answer questions pertaining to nouns, adjectives, verbs corresponding to the amount for each in the specified Madlib text.
4. After user enters answers the code will output the finished Madlib.
#  How madlibmaker.py Works
1. The code uses while loops to enable the user to make as many noun, verb, and adjective questions as they'd like. 
2. The code prompts the user to create new lines with instruction on how to enter blanks/questions.
3. The code verifies that the line for the madlib is what the user intended with an if statement. 
# Run it!
1. In terminal enter python3 madlibmaker.py
2. The user is prompted to make their noun, verb, and adjective questions. 
3. The user is prompted to add lines to their madlib and verifies that it is the line that they want. 
4. The madlib the user created is printed out. 
# Team Members
* Tiyana Mattox
* Anjali
