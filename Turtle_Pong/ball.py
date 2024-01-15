from turtle import Turtle
from constant import OBJECT_COLOR, CANVAS_WIDTH, CANVAS_HEIGHT


class Ball(Turtle):
    moveX = 10
    moveY = 10

    def __init__(self):
        super().__init__("circle")
        self.color(OBJECT_COLOR)
        self.penup()

    def move(self):
        self.goto(self.xcor() + self.moveX, self.ycor() + self.moveY)
        
    def refresh(self):
        self.home()
        self.moveX *= -1
        self.moveY *= -1 
        
    def bounce_x(self):
        self.moveX *= -1
    
    def bounce_y(self):
        self.moveY *= -1

    def handleWallCollusion(self):
        # x_wall_bound = CANVAS_WIDTH//2 - 20
        y_wall_bound = CANVAS_HEIGHT//2 - 20
        # if self.xcor() > x_wall_bound or self.xcor() < -x_wall_bound:
        #     self.bounce_x()
        if self.ycor() > y_wall_bound or self.ycor() < -y_wall_bound:
            self.bounce_y()
            
    def handleCollusionWithPaddle(self, paddle: Turtle):
        # TODO: Don't make it hard coded,
        x_paddle_pos = 320 
        # x_paddle_pos = (CANVAS_WIDTH - 30)//2
        if self.distance(paddle) < 50:
            if self.xcor() > x_paddle_pos or self.xcor() < -x_paddle_pos:
                self.bounce_x()
                
    def handleHittingRightWall(self):
        x_wall_bound = CANVAS_WIDTH//2 - 20
        if self.xcor() > x_wall_bound:
            self.refresh()
            return True
        return False
    
    def handleHittingLeftWall(self):
        x_wall_bound = CANVAS_WIDTH//2 - 20
        if self.xcor() < -x_wall_bound:
            self.refresh()
            return True
        return False
