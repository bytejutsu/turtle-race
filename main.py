import random
from turtle import Turtle, Screen

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 400
TURTLE_COUNT = 6
Y_INTERVAL = SCREEN_HEIGHT / (TURTLE_COUNT + 1)
Y_INIT = (-1 * SCREEN_HEIGHT / 2) + Y_INTERVAL
X_INIT = (-1 * SCREEN_WIDTH / 2) + 20

tim = Turtle()
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []


def distribute_turtles():
    ycor = Y_INIT
    for color in colors:
        t = Turtle(shape="turtle")
        t.color(color)
        turtles.append(t)
        t.penup()
        t.goto(x=X_INIT, y=ycor)
        ycor += Y_INTERVAL


def race():
    while True:
        for turtle in turtles:
            if turtle.xcor() + 30 >= SCREEN_WIDTH / 2:
                return turtle.pencolor()
            turtle.forward(random.randint(0, 10))


def check_result(a_winner, a_user_bet):
    print(f"the winner is {a_winner}")
    if a_winner == a_user_bet:
        print("your bet is right")
    else:
        print("you lost the bet")


distribute_turtles()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
winner = race()
check_result(a_winner=winner, a_user_bet=user_bet)
screen.exitonclick()
