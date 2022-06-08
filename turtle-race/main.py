# used libraries
from turtle import Turtle, Screen
import random

# set up the screen
screen = Screen()
screen.setup(width=500, height=400)

# ask user to bet on a color of a turtle
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# starting position of the first turtle
x = -230
y = -120

# create six turtles, every next turtle is positioned above previous one
for turtle_index in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x, y)
    all_turtles.append(new_turtle)
    y += 50

# allow start of the race when bet is placed
is_race_on = False
if user_bet:
    is_race_on = True

# race is on
while is_race_on:
    # move turtles forward, each time by its own random distance and print the message when race is over
    for turtle in all_turtles:

        # check if a turtle crossed the finish line --> end race
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            # check if user won or lost and print the message
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        # move a turtle forward by a random distance
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

# keep the game window open until clicked on
screen.exitonclick()
