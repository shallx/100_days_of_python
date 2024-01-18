import turtle
import pandas

from print_board import PrintBoard

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S States Game")
image = "blank_States_img.gif"
screen.addshape(image)
turtle.shape(image)
print_board = PrintBoard()

# Read from CSV
data = pandas.read_csv("50_states.csv")

states = [state.lower() for state in data.state.to_list()]
matched_states = []


while len(matched_states) < 50:

    # User Input
    answer_state = screen.textinput(title=f"{len(matched_states)}/50 Guess the state", prompt="What's another state name?").lower()

    if answer_state == "exit":
        break
    if answer_state in states:
        matched_data = data[data.state.str.lower() == answer_state]
        print(matched_data)
        print(matched_data.x.item())
        print(matched_data.y.item())
        print_board.write_state((int(matched_data.x.item()), int(matched_data.y.item())), matched_data.state.item())
        matched_states.append(answer_state)
        states.pop(states.index(answer_state))


missed_states = {
    "states": states
}

pandas.DataFrame(missed_states).to_csv("missed_states.csv")

turtle.mainloop()