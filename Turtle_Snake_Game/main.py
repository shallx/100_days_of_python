import time
from turtle import Screen, Turtle
from typing import List

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")

segments: list[Turtle]  = []

for i in range(3):
    t = Turtle("square")
    t.color("white")
    t.penup()
    t.goto(0 - i*20,0)
    segments.append(t)
    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    for seg in segments:
        seg.forward(20)
    
    
screen.exitonclick()