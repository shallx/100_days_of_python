import time
from turtle import Screen, Turtle, mode
from typing import List
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("My Snake Game")
mode("logo")

snake = Snake()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

    
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    
screen.exitonclick()