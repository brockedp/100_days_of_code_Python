###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##

import colorgram
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     if r < 210 and g < 210 and b < 210:
#         rgb_colors.append(new_color)
#
# print(rgb_colors)

from random import choice
import turtle as t

color_list = [(202, 164, 110), (149, 75, 50), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184),
              (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (160, 142, 158), (54, 45, 50),
              (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102),
              (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim = t.Turtle()
tim.shape("square")
t.colormode(255)
screen = t.Screen()
screen.screensize(500, 500)


def move_turtle():
    tim.pendown()
    tim.dot(25, choice(color_list))
    tim.penup()
    tim.forward(50)


x_position = -250
y_position = -200
tim.penup()
tim.setpos(x_position, y_position)
for j in range(10):
    for i in range(10):
        move_turtle()
    y_position += 50
    tim.setpos(x_position, y_position)

screen.exitonclick()
