import random
from random import choice
from turtle import Turtle, Screen

SCREEN = Screen()
SCREEN.setup(width=500, height=400)
USER_CHOICE = SCREEN.textinput(
    title = "Make your bet",
    prompt = "Which turtle will win the race? Enter color of choice"
).lower()

color_list = ["violet", "red", "blue", "green", "yellow", "indigo"]
POSITION_Y = 170
turtle_list = []
RACE_OVER = False
POSITION = 0


def set_color_set_position(turtle_obj: Turtle, y_coor: POSITION_Y, turtle_color: str):
    """Set turtle color and position"""
    turtle_obj.penup()
    turtle_obj.color(turtle_color)
    turtle_obj.goto(x=-245,y=y_coor)


def check_guess(turtle_color: str, user_choice):
    """Check if user wins"""
    if turtle_color.lower() == user_choice:
        print(f"You chose the {user_choice} turtle! "
              f"You win! The {turtle_color} turtle came first")
    else:
        print(f"You chose the {user_choice} turtle! "
              f"You lose! The {turtle_color} "
              f"turtle came first")

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    set_color_set_position(new_turtle, POSITION_Y, color_list[turtle_index])
    POSITION_Y -= 66
    turtle_list.append(new_turtle)

if USER_CHOICE:
    while not RACE_OVER:
        moving_turtle = choice(turtle_list)
        random_distance = random.randint(0,10)
        moving_turtle.forward(random_distance)
        POSITION = max(POSITION, moving_turtle.xcor())
        if POSITION > 230:
            winner_color = moving_turtle.fillcolor()
            check_guess(winner_color, USER_CHOICE)
            RACE_OVER = True

SCREEN.exitonclick()
