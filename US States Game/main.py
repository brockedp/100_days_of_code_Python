# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

import pandas
import turtle
image = "blank_states_img.gif"
screen = turtle.Screen()
screen.title("US States Game")
screen.addshape(image)
turtle.shape(image)

def printState(name, x, y):
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(x=x, y=y)
    t.write(font=("Times New Roman", 8, "bold"), align="center", arg=name)
data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states", prompt="What's another state").title()
    if answer_state == 'Exit':
        states_to_learn = []
        for state in all_states:
            if state not in guessed_states:
                states_to_learn.append(state)
        # print(states_to_learn)

        df = pandas.DataFrame(states_to_learn)
        df.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        state = data[data.state == answer_state]
        printState(name=state.state.item(), y=int(state.y), x=int(state.x))
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)

