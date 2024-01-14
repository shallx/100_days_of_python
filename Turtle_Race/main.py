from turtle import Turtle, Screen
from typing import List
import random

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]


turtles : List[Turtle] = []

for i in range(6):
    t = Turtle(shape="turtle")
    t.color(colors[i])
    t.penup()
    t.goto(x=-230, y=-100 + i*30)
    turtles.append(t)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You won the bet, {winner} was first")
            else:
                print(f"You lost the bet, The winner was {winner}")
        turtle.forward(random.randint(0,10))
screen.exitonclick()