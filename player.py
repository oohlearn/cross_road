from turtle import Turtle
import random


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.shape("turtle")
        self.goto(0, -180)
        self.cars = []
        self.car_sum = random.randint(15, 20)

    def move(self):
        self.forward(10)

    def next_round(self):
        self.goto(0, -180)

    def crash_car(self, cars):
        for car in cars:
            if self.distance(car) < 10:
                return True
