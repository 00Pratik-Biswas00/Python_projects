import hangman_database
import random

# Ascii art
import ascii_art_hangman
print(ascii_art_hangman.logo)

chosen_word = random.choice(hangman_database.word_list)
word_length = len(chosen_word)

lives = 8

display = []
print("\nYou have only 8 lives. Every wrong guess takes 1 life. You have to guess the word before your life is over. Let's start the game!\n")

for _ in range(word_length):
    display += "_"
print((f"The length of the word is: {word_length}"))
print(f"Here is your word: {display}\n")

end_of_game = False
while not end_of_game:
    guess = input("\nGuess a letter: ").lower()

    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    if guess in display:
        print(f"\nYou've guessed '{guess}'. It's the correct guess!\n")

    if guess not in chosen_word:
        print(f"\nYou chose a wrong letter, '{guess}' is not present in the word. You lose a life.\n")
        lives -= 1
        if lives == 0:
            print(f"You lose. The word is: {chosen_word}")
            end_of_game = True

    print(display)
    if "_" not in display:
        end_of_game = True
        print(f"You win! The word is: {chosen_word}")

    # Ascii art
    print(f"\nPresent condition of the Hangman: {ascii_art_hangman.stages[lives]}")
