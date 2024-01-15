COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

import random
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color(random.choice(COLORS))
        # self.goto(STARTING_POSITION)
        self.shapesize(stretch_wid=1, stretch_len=3)
        # self.setheading(90)
        self.goto(300 - 30, random.randint(-250, 250))
        self.move_speed = STARTING_MOVE_DISTANCE
        
            
    def move(self):
        self.back(self.move_speed)
    
    def increase_speed(self):
        print("Increasing speed")
        self.move_speed += MOVE_INCREMENT
