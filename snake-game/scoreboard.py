# used library
from turtle import Turtle

# constants
TEXT_X = 0
TEXT_Y = 270
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class Scoreboard(Turtle):
    """Models the scoreboard"""
    def __init__(self):
        super().__init__()
        self.score = 0

        # opens the file with high score data
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(TEXT_X, TEXT_Y)

    def update_scoreboard(self):
        """Updates the score and the high score on the scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """Increases the score by one"""
        self.score += 1

    def reset_score(self):
        """Sets the new score as high score and resets the score"""
        if self.score > self.high_score:
            with open("data.txt", mode='w') as data:
                self.high_score = self.score
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

