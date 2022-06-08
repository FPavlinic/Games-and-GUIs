# used library
from turtle import Turtle

# constants
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    """Models the snake"""
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake at the starting position by adding up segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Draws a segment of the snake"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """Resets the game, positions the snake at the starting position and reverts it to original size"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Makes snake longer by adding segments to its current body"""
        # add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Makes the snake move forward"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Redirects the snake upwards"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Redirects the snake downwards"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Redirects the snake to the left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Redirects the snake to the right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
