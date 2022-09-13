from turtle import Turtle
import random


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.cars_list = []
        self.shape("square")
        self.shapesize(stretch_wid=0.75, stretch_len=1.5)
        self.penup()
        self.setheading(180)
        self.cars_sum = random.randint(15, 20)

    def car_move(self):
        self.forward(10)
        if self.xcor() <= -300:
            new_y = random.randint(-120, 140)
            new_x = random.randint(300, 350)
            self.goto(new_x, new_y)

    def make_cars(self):
        for _ in range(self.cars_sum):
            car = Cars()
            car_y = random.randint(-120, 140)
            car_x = random.randint(300, 1000)
            car.sety(car_y)
            car.setx(car_x)
            self.cars_list.append(car)
