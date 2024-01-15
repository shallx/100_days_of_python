from turtle import Screen, Turtle
from constants import SNAKE_COLOR, SCREEN_SIZE, SNAKE_SIZE
UP = 0
DOWN = 180
RIGHT = 90
LEFT = 270
SPEED = 6

class Snake:
    segments: list[Turtle]  = []
    def __init__(self):
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        '''Create Snake using turtle'''
        for i in range(3):
            t = Turtle("square")
            t.speed(SPEED)
            t.color(SNAKE_COLOR)
            t.penup()
            t.goto(0 - i*20,0)
            self.segments.append(t)

    def move(self):
        '''Move the snake forward each seg linked to other'''
        for i in range(len(self.segments)-1, 0, -1):
            x = self.segments[i-1].xcor()
            y = self.segments[i-1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(20)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def hitWall(self):
        boundary = SCREEN_SIZE//2 - SNAKE_SIZE
        if self.head.xcor() > boundary or self.head.xcor() < -boundary or self.head.ycor() > boundary or self.head.ycor() < -boundary:
            return True
        else:
            return False
        
    def eat(self, food: Turtle):
        if self.head.distance(food) < 18:
            return True
        else:
            False

    