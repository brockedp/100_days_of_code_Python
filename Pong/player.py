from turtle import Turtle
MOVEMENT = 20

class Player(Turtle):

    def __init__(self, location):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.turtlesize(stretch_wid=1, stretch_len=5)
        self.seth(90)
        self.goto(location)

    def move_up(self):
        if self.ycor() < 300:
            self.forward(MOVEMENT)

    def move_down(self):
        if self.ycor() > -300:
            self.forward(-MOVEMENT)