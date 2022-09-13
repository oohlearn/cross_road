from turtle import Turtle


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(-270, 170)
        self.level = 0
        self.hideturtle()
        self.write(f"Level: {self.level}", False, "left", ('Arial', 8, 'normal'))

    def level_up(self, speed):
        speed -= 0.01
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", False, "left", ('Arial', 8, 'normal'))
        return speed
