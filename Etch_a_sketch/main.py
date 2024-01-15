from turtle import Turtle, Screen, clearscreen

t = Turtle()

screen = Screen()

def move_forward():
    t.forward(10)

def move_backword():
    t.back(10)

def move_right():
    t.right(10)

def move_left():
    t.left(10)

screen.onkey(move_forward, "w")
screen.onkey(move_backword, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clearscreen, "c")
screen.listen()

t.screen.mainloop()
