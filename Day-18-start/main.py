import turtle as t
from random import choice, randint

henry = t.Turtle()
henry.shape("arrow")
henry.color("red")
henry.setposition(-10, 0)
t.colormode(255)


# for i in range(4):
#     timmy_the_turtle.forward(210)
#     timmy_the_turtle.left(90)
# for i in range(100):
#     if i % 2 == 0:
#         timmy_the_turtle.penup()
#     else:
#         timmy_the_turtle.pendown()
#     timmy_the_turtle.forward(2)
def shapes_shapes_shapes(num_of_sides):
    for i in range(4, (num_of_sides + 1)):
        degrees = 360 / i
        #colors = ["red", "yellow", "green", "blue", "purple", "orange", "black", "teal"]
        colors = (randint(1,255),randint(1,255),randint(1,255))
        this_color = choice(colors)
        for j in range(i):
            henry.color(this_color)
            henry.forward(100)
            henry.right(degrees)



def random_walk(pen_size):
    #colors = ["red", "yellow", "green", "blue", "purple", "orange", "black", "teal"]
    color = (randint(1, 255), randint(1, 255), randint(1, 255))
    #this_color = choice(color)
    directions = [0, 90, 180, 270]
    direction = choice(directions)
    henry.seth(direction)
    henry.color(color)
    henry.pensize(pen_size)
    henry.speed(10)
    henry.forward(25)


henry.speed(0)

def draw_spirograph():
    for i in range(1,361):
        henry.setheading(i)
        color = (randint(1, 255), randint(1, 255), randint(1, 255))
        henry.color(color)
        henry.circle(180)


#shapes_shapes_shapes(8)
# pen_size = 1
# for i in range(100):
#     if i % 3 == 0:
#         pen_size += 1
#     random_walk(pen_size)

draw_spirograph()


screen = t.Screen()
screen.exitonclick()
