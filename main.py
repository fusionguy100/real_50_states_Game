from turtle import Turtle

import pandas
import turtle

data = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

states = data["state"].tolist()
turtle.shape(image)



current_guesses = []
current_answers = 0



while True:
    answer_state = screen.textinput(title=f"{current_answers}/50", prompt="What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in states if state not in current_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in states and answer_state not in current_guesses:
        state_data = data[data.state == answer_state]
        x = int(state_data.x)
        y = int(state_data.y)
        writer = Turtle()
        writer.hideturtle()
        writer.penup()
        writer.goto(x,y)
        writer.write(answer_state, align = "Center", font = ("Arial",8,"normal"))
        current_guesses.append(answer_state)
        current_answers += 1

    if current_answers == 50:
        break



