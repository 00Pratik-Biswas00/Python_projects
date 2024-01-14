from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("data/french_words.csv")
    to_learn = org_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# Next Card

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(theTitle, text="French", fill="black")
    canvas.itemconfig(theAnswer, text=current_card["French"], fill="black")
    canvas.itemconfig(card_bg, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)


# Flip Card

def flip_card():
    canvas.itemconfig(theTitle, text="English", fill="white")
    canvas.itemconfig(theAnswer, text=current_card["English"], fill="white")
    canvas.itemconfig(card_bg, image=card_back_img)


# Right Guess

def right_card():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# UI Setup

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)

card_front_img = PhotoImage(file="images/card_front.png")
card_bg = canvas.create_image(400, 263, image=card_front_img)

card_back_img = PhotoImage(file="images/card_back.png")

theTitle = canvas.create_text(400, 150, text="Title", font=('Arial', 40, 'italic'))
theAnswer = canvas.create_text(400, 263, text="answer", font=('Arial', 40, 'bold'))

canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

my_wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=my_wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

my_right_image = PhotoImage(file="images/right.png")
right_button = Button(image=my_right_image, highlightthickness=0, command=right_card)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
