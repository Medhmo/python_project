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

print(word)
