# used library
from turtle import Turtle


class TypeToMap(Turtle):
    """Models the state maper"""
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def map_state(self, state, x_cor, y_cor):
        """Writes the name of the state on the map"""
        self.penup()
        self.goto(x_cor, y_cor)
        self.write(f"{state}", align="center", font=("Courier", 7, "normal"))

    def congratulations(self):
        """Writes congratulations message on the screen"""
        self.penup()
        self.goto(0, 280)
        self.write("Congratulation! You've managed to guess all the states.",
                   align="center", font=("Courier", 14, "normal"))
