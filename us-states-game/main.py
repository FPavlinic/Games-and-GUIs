# used libraries
import turtle
import pandas
from type_to_map import TypeToMap

# set up the game screen
screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# create object to be able to show progress of the game
type_to_map = TypeToMap()

# read names of the states and save from txt and save them to the list
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

# empty list for correctly guessed states
guessed_states = []

# play game
game_is_on = True
while game_is_on:

    # check the number of guessed states and set the title accordingly
    if len(guessed_states) == 0:
        title = "Guess the State"
    else:
        title = f"{len(guessed_states)}/{len(data.state)} States Correct"

    # window for the answer
    answer_state = screen.textinput(title=title, prompt="What's another state's name?").title()

    # type 'Exit' to leave the game and save at current state
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    # check if the answer is duplicated
    if answer_state not in guessed_states:
        # check if the answer is correct
        if answer_state in all_states:
            guessed_states.append(answer_state)
            state_data = data[data.state == answer_state]
            type_to_map.map_state(answer_state, int(state_data.x), int(state_data.y))

        # check if all states are guessed correctly and end the game
        if len(guessed_states) == len(data.state):
            type_to_map.congratulations()
            game_is_on = False


# use to find out x and y of points in the window and where to put state names
# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
