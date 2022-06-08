# used library
from turtle import Turtle

# constant
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    """Models the scoreboard"""
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-250, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        """Updates the scoreboard"""
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def increase_level(self):
        """Increases the game level"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """Shows 'GAME OVER' at the center of the screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
