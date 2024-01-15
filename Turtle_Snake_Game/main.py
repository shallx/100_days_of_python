import time
from turtle import Screen, Turtle, mode
from typing import List
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from constants import SCREEN_SIZE, BACKGROUND_COLOR

screen = Screen()
screen.setup(width=SCREEN_SIZE, height=SCREEN_SIZE)
screen.tracer(0)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("My Snake Game")
mode("logo")

snake = Snake()
food = Food()
score = Scoreboard()

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

    if snake.head.distance(food) < 18:
        print("nom nom nom")
        food.refresh()
        score.increase_score()
    
screen.exitonclick()