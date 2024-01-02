import turtle
import pandas
from tkinter import messagebox
screen = turtle.Screen()
screen.title("Find States UTs and Capital of India in Map")
image = "blank_India_map.gif"
screen.addshape(image)
turtle.shape(image)

# def gg (x,y):
#     print(x,y)
# turtle.onscreenclick(gg)
# turtle.mainloop()

data = pandas.read_csv("India_states_uts_capital.csv")
all_states = data.state.to_list()
guessed_states = []
seen = set()
while len(guessed_states) < len(all_states):
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} entries are correct",
                                    prompt="What's another State's/UT's/Capital name?").title()
    if answer_state in seen:
        messagebox.showinfo("showinfo", "Already Entered")

    else:
        seen.add(answer_state)
        if answer_state == "Exit":
            missing_states = []
            for state in all_states:
                if state not in guessed_states:
                    missing_states.append(state)
            new_data = pandas.DataFrame(missing_states)
            new_data.to_csv("states_UTs_of_India_to_learn.csv")
            break
        if answer_state in all_states:
            guessed_states.append(answer_state)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            t.color("blue")
            t.font = ("Arial", 16, "bold")
            state_data = data[data.state == answer_state]
            t.goto(int(state_data.x), int(state_data.y))
            t.write(answer_state)
        else:
            messagebox.showinfo("showinfo", "Check spelling or enter right state/UT")
