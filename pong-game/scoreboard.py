# used library
from turtle import Turtle


class Scoreboard(Turtle):
    """Models scoreboard"""

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates score"""
        self.clear()
        self.goto(-100, 220)
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))

    def l_point(self):
        """Adds point to player on the left"""
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        """Adds point to the player on the right"""
        self.r_score += 1
        self.update_scoreboard()
