from turtle import Turtle, Screen, shape, onscreenclick, mainloop
import csv

dict_states = dict()
answers = []

with open("50_states.csv") as file:
    data = list(file.readlines())
    print(data)
    for row in data:
        line = row.strip().split(",")
        if line[0] != "state":
            dict_states[line[0].lower()] = (int(line[1]), int(line[2]))
print(dict_states)

screen = Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"
screen.addshape(img)
shape(img)

def get_mouse_click_coor(x, y):
    print(x, y)

onscreenclick(get_mouse_click_coor)

game_play = True
lives = 3
score = 0
while lives > 0:
    ans = screen.textinput(f"What's another state's name?", f"{score}/50 States Correct\n{lives} lives remaining...").lower()
    if ans == "exit":
        break
    elif ans in dict_states:
        score += 1
        state_text = Turtle()
        state_text.hideturtle()
        state_text.penup()
        state_pos = dict_states.get(ans)
        state_text.goto(state_pos)
        state_text.write(ans, True)
        answers.append(ans)
        del dict_states[ans]
    else:
        lives -= 1

with open("states_to_learn.csv", mode="w") as file:
    for state in dict_states:
        file.write(state + ",'" + str(dict_states[state]) + "'\n")