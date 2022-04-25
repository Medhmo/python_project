""" Imports"""

import random

# Hangman Game
# Computer will generate a random word from a list
# Player tries to guess the full word
# Or one letter at the time

# User welcome and username selection

USERNAME = str(input("Please enter a Username : "))
print("Welcome " + USERNAME + " Best of luck ! ")

# Constants

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
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
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

WORDS = ["BOX", "CAT", "ORANGES", "SYNDROME"]

MAX_WRONG = len(HANGMANPICS) - 1

# Variables

# Word Randomisation

word = random.choice(WORDS)

# In words letters masking

current_guess = "-" * len(word)

# Wrong guesses tracker

WRONG_GUESSES = 0

# Used letters tracker

used_letters = []

# Main loop creation

print("Welcome to Hangman")
print("Computer will generate a random word from a list")
print("Try guessing the word")

while WRONG_GUESSES < MAX_WRONG and current_guess != word:

    print(HANGMANPICS[WRONG_GUESSES])
    print("You have used the following letters so far : ", used_letters)
    print("So far the word is : ")

    guess = input("Please enter your letter guess : ")
    guess = guess.upper()

# Checks if the letter has been previously used

    while guess in used_letters:
        print("You have already guessed this letter: ", guess)
        guess = input("Enter your letter guess: ")
        guess = guess.upper()

         # Updated the ussed letters list

        used_letters.append(guess)

         # Updates the guesses

        if guess in word:
            print("Great guess !")