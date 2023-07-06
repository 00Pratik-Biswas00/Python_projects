# It is a Reedborg robot hurdle game, where many inbuilt functions are present like turn_left(), right_is_clear() etc. The details of the 
# inbuilt functions are present in the Reedborg' keywords section. The Reedborg website link is attached in the Readme file under number 3.

def right():
    turn_left()
    turn_left()
    turn_left()

def height():
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
