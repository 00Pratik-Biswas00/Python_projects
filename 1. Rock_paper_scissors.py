import random
# Ascii arts
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice=''
while choice.lower() != 'no': # Taking multiple inputs
    com = random.randint(0, 2) # Randint function to take a random number between the given two integers
    a = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if a == com:
        print("You both choose the same. Match drawn")
    elif (a == 0) and (com == 1):
        print( "You:" + rock + "\n" + "Computer" + paper + "\n" + "Computer wins.")
    elif (a == 1) and (com == 0):
        print( "You:" + paper + "\n" + "Computer" + rock + "\n" + "You win.")
    elif (a == 0) and (com == 2):
        print( "You:" + rock + "\n" + "Computer" + scissors + "\n" + "You win.")
    elif (a == 2) and (com == 0):
        print( "You:" + scissors + "\n" + "Computer" + rock + "\n" + "Computer wins.")
    elif (a == 1) and (com == 2):
        print( "You:" + paper + "\n" + "Computer" + scissors + "\n" + "Computer wins.")
    elif (a == 2) and (com == 1):
        print( "You:" + scissors + "\n" + "Computer" + paper + "\n" + "You win.")
    else:
        print("invalid number")
    choice = input("Do you want to play again? Yes or No? -> ").lower()





