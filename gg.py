from turtle import Turtle


class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.write("Game Over", False, "center", ('Arial', 30, 'normal'))
