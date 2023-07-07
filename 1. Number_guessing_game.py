import random
ascii_art = '''


  _   _                 _                                           
 | \ | |               | |                                          
 |  \| |_   _ _ __ ___ | |__   ___ _ __    __ _ _   _  ___  ___ ___ 
 | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|  / _` | | | |/ _ \/ __/ __|
 | |\  | |_| | | | | | | |_) |  __/ |    | (_| | |_| |  __/\__ \__ /
 |_| \_|\__,_|_| |_| |_|_.__/ \___|_|     \__, |\__,_|\___||___/___/
                                           __/ |                    
                                          |___/                     

'''

print(ascii_art)
print("\n\nI am thinking of a number between 1 and 100.\n")
answer = random.randint(1, 101)
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    elif level == "hard":
        return HARD_LEVEL_TURNS
    else:
        print("\nChoose correct difficulty.")
        return


turns = set_difficulty()

loop_continue = False
while not loop_continue:
    number = int(input(f"\nYou have {turns} attempts  remaining to guess the number.\nMake a guess: "))
    if number == answer:
        print(f"\nYou got it! The answer was {number}")
        loop_continue = True
    if number != answer:
        turns -= 1
        if number < answer:
            print("Too low!")
        elif number > answer:
            print("Too high!")
        if turns != 0:
            print("Guess again.")
        if turns == 0:
            print(f"\nYou lose. The number is: {answer}")
            loop_continue = True

"""
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


# Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
# checks answer against guess. Returns the number of turns remaining.
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The answer was {answer}.")


# Make function to set difficulty.
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def game():

    # Choosing a random number between 1 and 100.
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        # Let the user guess a number.
        guess = int(input("Make a guess: "))

        # Track the number of turns and reduce by 1 if they get it wrong.
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

game()
"""
