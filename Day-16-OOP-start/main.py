# import another_module
# print(another_module.another_variable)
#
#
# from turtle import Turtle, Screen #import the Turtle class from turtle module
# my_turtle = Turtle()
# print(my_turtle)
# my_turtle.shape("turtle")
# my_turtle.color("blue")
# #my_turtle.right(100)
# my_turtle.forward(100)
# my_turtle.right(90)
# my_turtle.forward(50)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon",["Pikacku","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = 'l'
print(table)