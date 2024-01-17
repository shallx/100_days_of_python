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

data2 = data.to_dict()
states = data.state.to_list()
x = data.x.to_list()
y = data.y.to_list()
my_data = {}
for i in range(50):
    my_data[states[i].lower()] = (x[i], y[i])

matched_states = []


while len(my_data.keys()):

    # User Input
    answer_state = screen.textinput(title=f"{len(matched_states)}/50 Guess the state", prompt="What's another state name?").lower()
    # matched_data = data[data.state == answer_state]

    # print(matched_data)
    # print(matched_data.index[0])
    # print(matched_data.x[1])
    if answer_state in my_data.keys():
        pos = my_data.pop(answer_state)
        matched_states.append(answer_state)
        print(pos)
        print_board.write_state(pos, answer_state)

        
        # x = int(matched_data.x[1])
        # y = int(matched_data.y[1])
        # state = matched_data.state[1]
        # print(x)
        # print(y)
        # print(state)
        # print_board.write_state((x, y), state)
        # data.state.pop(matched_data.index[0])


turtle.mainloop()