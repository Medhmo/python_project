""" Imports"""

import random
import images

# Hangman Game
# Computer will generate a random WORD from a list
# Player tries to guess the full WORD
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

current_guess = list(len(WORD)*"_")

# Set the game progression Status

game_won = False

# Wrong guesses tracker

wrong_guesses = 0

used_letters = []

# Remaining lives tracker

lives = 6

# Variables

# Main loop creation

# Player greeting and the rules of the game
print("The computer will generate a random WORD from a list")
print("Try guessing the WORD")

# Generates a new scrambled version of the WORD


def updated_current_guess(letter, WORD):
    """updates the current guess

    Args:
        letter (_str_): _guessed letter_
        WORD (_str_): _guess_word_

    Returns:
        bool:True if the letter is in the WORD
    """

    global current_guess
    for i in range(0, len(WORD)):
        letter = WORD[i]
        if guess == letter:
            current_guess[i] = guess
    if "_" not in current_guess:
        return True
    else:
        return False


def status():
    """_summary_
    """
    print(images.HANGMANPICS[6-lives])
    print(current_guess)
    print("You have", lives, "lives remaining")


while not game_won and lives > 0:
    # status()
    guess = input("Please enter your letter guess : ")
    guess = guess.upper()

    if guess == WORD:
        game_won = True
        current_guess = WORD
    if len(guess) == 1 and guess in WORD:
        game_won = updated_current_guess(guess, WORD)
    else:
        lives -= 1
        # Status()
        # Updated the ussed letters list
    status()
    if wrong_guesses < MAX_WRONG and current_guess != WORD:
        print("You have used the following letters so far : ", used_letters)
        # print(HANGMANPICS)
        used_letters.append(guess)
    # Checks if the letter has been previously used
    if guess in used_letters:
        print("You have already guessed this letter: ", guess)
    # Feedback on the guesses
    if guess in WORD:
        print("Great guess !")
    else:
        print("That was incorrect!")

    if lives == 0:
        print("you ran out of lives , the WORD is : ", WORD)

if game_won:
    print("Congratulation ! You Won")
else:
    print("You have lost ")
