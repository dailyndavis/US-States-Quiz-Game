# Challenge: 
# Read from the csv and get those x and y values. Ask for an answer 
# 1 - Convert the guess to Title case ✅
# 2 - Check if the guess is among the 50 states ✅
# 3 - Write correct guesses onto the map ✅
# 4 - Use a loop to allow the user to keep guessing ✅
# 5 - Record the correct guesses in a list ✅
# 6 - Keep track of the score. ✅
# 7 - Save the missing states to a csv - "states_to_learn.csv"
from turtle import Turtle, Screen, shape
import pandas  

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

state_data = pandas.read_csv("50_states.csv")

list_of_states = state_data["state"].to_list()
correct_guesses = [] 
user_points = 0 
missed_states = []

while user_points < 50:
    guess = Turtle()
    guess.hideturtle()
    guess.penup()
    answer_state = screen.textinput(\
    title=f"{user_points}/50 States Correct", \
    prompt="What's another state's name?"\
        ).title()
    if answer_state == "Exit":
        # i love you
        # for state in list_of_states:
        #     if state not in correct_guesses:
        #         missed_states.append(state)
        missed_states = [state for state in list_of_states if state not in correct_guesses]
        missed_states_list = pandas.DataFrame(missed_states)
        missed_states_list.to_csv("states_to_learn.csv")

        break
    if answer_state in list_of_states:
        row = state_data[state_data.state == answer_state]
        x = int(row.x)
        y = int(row.y)
        guess.goto(x,y)
        guess.write(answer_state, align="center", font=("Courier New", 12, "normal"))
        correct_guesses.append(answer_state)
        user_points += 1 


