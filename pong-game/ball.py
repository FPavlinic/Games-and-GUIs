# used library
from turtle import Turtle

# constants
BALL_COLOR = "white"
STARTING_POSITION = (0, 0)


class Ball(Turtle):
    """Models a ball"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(BALL_COLOR)
        self.penup()
        self.goto(STARTING_POSITION)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Makes the ball move"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Makes the ball bounce of the wall"""
        self.y_move *= -1

    def bounce_x(self):
        """Makes the ball bounce of the paddle and speeds it up"""
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        """Resets the balls position to starting position after a score and speeds it up"""
        self.goto(STARTING_POSITION)
        self.move_speed = 0.1
        self.bounce_x()

