import turtle as t

tim = t.Turtle()
# tim.penup()
tim.shape("turtle")
tim.color("green")
screen = t.Screen()

def move_forward():
    tim.forward(10)
def move_back():
    tim.forward(-10)
def turn_up():
    tim.seth(90)
def turn_down():
    tim.seth(270)

def turn_left():
    new_heading = tim.heading()+10
    tim.seth(new_heading)

def turn_right():
    new_heading = tim.heading()-10
    tim.seth(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()

screen.onkey(key="w", fun=move_forward)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear)

screen.exitonclick()