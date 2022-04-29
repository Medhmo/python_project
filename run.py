""" Imports"""

import random
import images

# Hangman Game
# The computer will generate a random WORD from a list
# Player tries to guess the full word
# Or one letter at the time

# User welcome and username selection

USERNAME = str(input("Please enter a Username : "))
print("Welcome to Hangman " + USERNAME + " Best of luck ! ")

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

# Word Randomisation

WORD = random.choice(WORDS)

# In words letters masking

CURRENT_GUESS = list(len(WORD)*"_")

# Sets the game progression Status

GAME_WON = False

# Wrong guesses and used letters tracker

WRONG_GUESSES = 0

USED_LETTERS = []

# Remaining lives tracker

LIVES = 6

# Variables

# Main loop creation

# Player greeting and the rules of the game
print("The computer will generate a random WORD from a list")
print("Try guessing the word")

# Generates a new scrambled version of the word


def updated_current_guess(letter, curent_word):
    """updates the current guess

    Args:
        letter (_str_): _guessed letter_
        WORD (_str_): _guess_word_

    Returns:
        bool:True if the letter is in the WORD
    """

    global CURRENT_GUESS
    for i, in enumerate(curent_word):
        letter = curent_word[i]
        if guess == letter:
            CURRENT_GUESS[i] = guess
    if "_" not in CURRENT_GUESS:
        return True
    else:
        return False


def status():
    """_summary_
    """
    print(images.HANGMANPICS[6-LIVES])
    print(CURRENT_GUESS)
    print("You have", LIVES, "lives remaining")


while not GAME_WON and LIVES > 0:
    # status()
    guess = input("Please enter your letter guess : ")
    guess = guess.upper()

    if guess == WORD:
        GAME_WON = True
        CURRENT_GUESS = WORD
    if len(guess) == 1 and guess in WORD:
        GAME_WON = updated_current_guess(guess, WORD)
    else:
        LIVES -= 1
        # Status()
        # Updated the used letters list
    status()
    if WRONG_GUESSES < MAX_WRONG and CURRENT_GUESS != WORD:
        print("You have used the following letters so far : ", USED_LETTERS)
        # Print(HANGMANPICS)
        USED_LETTERS.append(guess)
    # Checks if the letter has been previously used
    if guess in USED_LETTERS:
        print("Your last guessed letter is: ", guess)
    # Feedback on the guesses
    if guess in WORD:
        print("Great guess !")
    else:
        print("That was incorrect!")

    if LIVES == 0:
        print("You ran out of lives , the word is : ", WORD)

if GAME_WON:
    print("Congratulation ! You Won")
else:
    print("SORRY , you have lost ")
