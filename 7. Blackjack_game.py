############### Blackjack Game Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have an equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


ascii_art = '''


  ____  _            _    _            _    
 |  _ \| |          | |  (_)          | |           .------.     .------.  
 | |_) | | __ _  ___| | ___  __ _  ___| | __        |K.--. |.-.  |A.--. |
 |  _ <| |/ _` |/ __| |/ / |/ _` |/ __| |/ /        | :/\: |     | (\/) |
 | |_) | | (_| | (__|   <| | (_| | (__|   <         | :\/: |'-.-.| :\/: |
 |____/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\        | '--'K|     | '--'A|
                        _/ |                        `------'  '-'`------'
                       |__/                 



'''

import random, os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Create a deal_card() function that uses the List below to return a random card.

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Create a function called calculate_score() that takes a List of cards as input and returns the score. 

def calculate_score(cards):
    # Inside calculate_score(), check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if sum(cards) == 21 and len(cards) == 2:  # sum() function to help you do this.
        return 0
    # Inside calculate_score(), check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Create a function called compare() and pass in the user_score and computer_score. If the computer and user have the same score, it's a draw. If the computer has a blackjack (0), then the user loses. If the user
# has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "computer wins!"
    elif user_score == 0:
        return "You win!"
    elif computer_score > 21:
        return "Computer went over. You win!"
    elif user_score > 21:
        return "You went over. Computer wins!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


def play_game():
    # Deal the user and computer 2 cards, each using deal_card() and append().
    user_cards = []
    computer_cards = []
    is_game = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())
    # The score will need to be rechecked with every new card drawn, and the checks in Hint 9 need to be repeated until the game ends.

    while not is_game:
        # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or the user's score is over 21, then the game ends.
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game = True
            # If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card( ) function to add another card to the user_cards List. If not, then the game has ended.
        else:
            user_should_play = input("Do you like to draw cards? Tap 'y' for yes and 'n' for no-> ").lower()
            if user_should_play == "y":
                user_cards.append(deal_cards())
            elif user_should_play == "n":
                is_game = True
            else:
                break

    # Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score of less than 17.

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand {user_cards}, and total score: {user_score} ")
    print(f"Computer's final hand {computer_cards}, and total score: {computer_score} ")
    print(compare(user_score, computer_score))


# Ask the user if they want to restart the game. If they answer yes, clear the console, start a new game of blackjack, and show the logo from art.py.
wanna_restart = True

while input("Do you like to play a Blackjack game? Tap 'y' for yes and any other key for no->  ") == 'y':
    os.system('cls')  # Clear the screen
    play_game()
