COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle

class CarManager:
    def __init__(self):
        self.all_cars : list[Turtle] = []

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            car = Turtle("square")
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.goto(300 - 30, random.randint(-250, 250))
            self.move_speed = STARTING_MOVE_DISTANCE
            self.all_cars.append(car)
        
            
    def move_cars(self):
        for car in self.all_cars:
            car.back(self.move_speed)
    
    def increase_speed(self):
        print("Increasing speed")
        self.move_speed += MOVE_INCREMENT
