import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move, "w")

game_is_on = True
frame = 1
cars: list[CarManager] = []

while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    if frame % 6 == 0:
        car = CarManager()
        cars.append(car)
    frame += 1
    
    for car in cars:
        car.move()
