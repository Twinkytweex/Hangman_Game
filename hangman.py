#Hangman Game

#skins

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

#importing random module

import random
from re import A
word_list = ["apple", "banana", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(display)

#creating Health system
live = 6

#Check guessed letter
while live != 0:
      #winning condition
      if "_" not in display:
          print("Congrats you won the game!")
      guess = input("Guess a letter: ").lower()
      #checking if its correct
      for position in range(word_length):            
            letter = chosen_word[position]
            if guess in letter:                  
                  display[position] = letter
                  
                  print(display)
      #cheking if its incorrect and -1 if not
      if guess not in chosen_word:
            print("you are wrong")
            live -= 1
            print(f"you're life left: {live}")
            print(stages[live]) 
# loseing the game
if live == 0:
      print("you lose the game!!!")

