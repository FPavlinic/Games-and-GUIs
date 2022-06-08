# used library
from turtle import Turtle

# constants
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    """Models the turtle"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_to_start(self):
        """Moves the turtle to the starting position (bottom of the game window)"""
        self.goto(STARTING_POSITION)

    def go_up(self):
        """Moves the turtle upwards by the specified amount"""
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        """Checks if the turtle crossed the finish line"""
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
