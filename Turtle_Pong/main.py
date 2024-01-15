# from canvas import Canvas
import time
from turtle import Screen, mode
from constant import CANVAS_HEIGHT, CANVAS_WIDTH, CANVAS_COLOR, TITLE
from paddle import Paddle
from ball import Ball

# Canvas
screen = Screen()
mode("logo")
screen.setup(height=CANVAS_HEIGHT, width=CANVAS_WIDTH)
screen.bgcolor(CANVAS_COLOR)
screen.title(TITLE)
screen.tracer(0)

# Turtle declare

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    ball.didCollide()
    ball.move()
    screen.update()

screen.exitonclick()