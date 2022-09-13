from turtle import Screen
import time
from player import Player
from level import Level
from cars import Cars
import random
from gg import GameOver

screen = Screen()
screen.setup(width=600, height=400)
screen.tracer(0)
screen.listen()

tur = Player()
level = Level()
cars = Cars()
cars.hideturtle()
cars.make_cars()

game_is_on = True
screen.onkeypress(tur.move, "Up")

speed = 0.1
while game_is_on:
    time.sleep(speed)
    screen.update()
    for car in cars.cars_list:
        car.car_move()
    if tur.crash_car(cars.cars_list):
        game_is_on = False
        game_over = GameOver()
    if tur.ycor() >= 170:
        speed = level.level_up(speed)
        tur.next_round()

screen.exitonclick()
