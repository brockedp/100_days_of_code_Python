from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITION = [(0,0),(0,-20),(0,-40)]

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in STARTING_POSITION:
            self.add_segment(i, 1)


    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)

    def add_segment(self, position, speed):
        new_snake_segment = Turtle(shape="square")
        new_snake_segment.speed(speed)
        new_snake_segment.penup()
        new_snake_segment.color("white")
        new_snake_segment.goto(position)
        self.segments.append(new_snake_segment)
        # new_snake_segment.goto(x=self.snake[len(self.snake) - 1].xcor() - 20, y=self.snake[len(self.snake) - 1].ycor())

    def extend(self):
        self.add_segment(self.segments[len(self.segments) - 1].position(),self.segments[len(self.segments) - 1].speed())

    def increase_speed(self):
        for segment in self.segments:
            speed = segment.speed()
            speed += 1
            segment.speed(speed)




