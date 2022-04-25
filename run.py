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

WORDS = ["box", "cat","orange", "syndrome" ]

MAX_WRONG = len(HANGMANPICS) - 1

# Variables

# Word Randomisation

word = random.choice(WORDS)

# In words letters masking

current_guess = "-" * len(word)

# Wrong guesses tracker

wrong_guesses = 0

# Used letters tracker

used_letters = []

# Main loop creation

print("Welcome to Hangman")
print("Computer will generate a random word from a list")
print("Try guessing the word")

while wrong_guesses < MAX_WRONG and current_guess != word :

    #print(HANGMANPICS[wrong_guesses])


