# It is a Reedborg robot hurdle game with many inbuilt functions, like turn_left(), right_is_clear(), etc. The details of the 
# inbuilt functions are present in Reedborg's keywords section. The Reedborg website link is attached in the Readme file under number 4.

def right():   # Function to turn right
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():   # Function to check if front is clear (This function needed before at_goal to solve certain infinite path problems
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
