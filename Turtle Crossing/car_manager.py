from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.seth(180)
        self.speed(1)
        self.color(random.choice(COLORS))
        self.goto(280, random.randint(-200,220))
        self.turtlesize(stretch_wid=1, stretch_len=2)
        self.move_increment = MOVE_INCREMENT
        self.forward(STARTING_MOVE_DISTANCE)



    def move(self, car_speed):
        self.forward(car_speed)

    def increase_speed(self):
        self.move_increment += MOVE_INCREMENT
