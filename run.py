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

wrong_guesses = 0

# Used letters tracker

used_letters = []

# Main loop creation

print("Welcome to Hangman")
print("Computer will generate a random word from a list")
print("Try guessing the word")

while wrong_guesses < MAX_WRONG and current_guess != word:

    print(HANGMANPICS[wrong_guesses])
    print("You have used the following letters so far : ", used_letters)
    print("So far the word is : ",  )
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
    else:
        print("That was incorrect!")

    # Generates a new scrambled version of the word

    updated_current_guess = ""
    for letter in range(len(word)):
        if guess == word[letter]:
            updated_current_guess += guess
        else:
            updated_current_guess += current_guess[letter]
            current_guess == updated_current_guess


    # Updates the number of incorrect guesses

wrong_guesses += 1

# Game Ends

if wrong_guesses == MAX_WRONG:
    print(HANGMANPICS[wrong_guesses])
    print("You have lost")
    print("The correct word is", word)
else:
    print("Congratulation ! You Won")
