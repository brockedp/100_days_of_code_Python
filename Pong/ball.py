from turtle import Turtle
from random import randint

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.ball_start_speed = 0.1
        self.ball_speed = self.ball_start_speed


    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def hit_y(self):
        self.y_move *= -1

    def hit_x(self):
        self.x_move *= -1

    def reset_positon(self):
        self.goto(0, 0)
        self.hit_x()


