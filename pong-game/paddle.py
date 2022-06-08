# used library
from turtle import Turtle

# constant
PADDLE_COLOR = "white"


class Paddle(Turtle):
    """Models a paddle"""

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color(PADDLE_COLOR)
        self.penup()
        self.goto(position)

    def go_up(self):
        """Moves it up the field"""
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """Moves it down the field"""
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
