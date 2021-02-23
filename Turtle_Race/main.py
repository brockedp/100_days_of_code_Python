import turtle as t
from random import randint as rand

screen = t.Screen()
screen.setup(width=500, height=400)
screen.bgcolor("tan")

start_x = -225
top_y = 125
colors = ["green", "orange", "red", "blue", "purple", "yellow"]
all_turtles = []

user_bet = screen.textinput(title="Make you bet", prompt="Which turtle will win the race? Enter color:").lower()

#Turtle objects
for turtle in range(0,6):
    cool_turtle = t.Turtle(shape="turtle")
    cool_turtle.penup()
    cool_turtle.color(colors[turtle])
    cool_turtle.goto(x=start_x, y=top_y)
    all_turtles.append(cool_turtle)
    top_y -= 50


if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("Your turtle won!!")
            else:
                print(f"Your turtle lost!!\nThe {winning_color} turtle is the winner!")
            break
        rand_distance = rand(0, 10)
        turtle.forward(rand_distance)












screen.exitonclick()
