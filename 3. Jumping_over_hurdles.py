# It is a Reedborg robot hurdle game with many inbuilt functions, like turn_left(), right_is_clear(), etc. The details of the 
# inbuilt functions are present in Reedborg's keywords section. The Reedborg website link is attached in the Readme file under number 3.

def right():    # Function to turn right
    turn_left()
    turn_left()
    turn_left()

def height():    # Function to measure the height of a wall
    if right_is_clear():
        move()
    else:
        turn_left()

while not at_goal():    
    if right_is_clear():
        right()
        move()
    elif wall_in_front():
        height()
    else:
        move()
