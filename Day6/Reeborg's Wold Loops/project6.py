# One Code for all the hurdles & Maze

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while at_goal() == False:
    if front_is_clear():
        move()
        turn_right()
    elif wall_in_front():
        turn_left()
    else:
        at_goal() == True

