import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
states = data.state.tolist()
answer_state = screen.textinput(title="Guess the state", prompt="What's another state's name?").title()
guessed_states = []
states_to_learn = []

while len(guessed_states) < 50:
    if answer_state == "Exit":
        # Version with List Comprehension
        # states_to_learn = [state for state in guessed_states if state not in guessed_states]
        for state in states:
            if state not in guessed_states:
                states_to_learn.append(state)

        missing_states = pandas.DataFrame(states_to_learn)
        missing_states.to_csv('states_to_learn.csv')
        break
    if answer_state in states:
        found_state = turtle.Turtle()
        found_state.penup()
        found_state.hideturtle()
        found_state.setpos(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y))
        found_state.write(data[data.state == answer_state].state.item())
        guessed_states.append(answer_state)
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()


