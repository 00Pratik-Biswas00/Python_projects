from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    blank_password = password_letters + password_numbers + password_symbols

    random.shuffle(blank_password)

    new_password = "".join(blank_password)
    password_entry.delete(0, END)  # Deletes the prev password
    password_entry.insert(0, new_password)
    pyperclip.copy(new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Oops", message="Please don't left any field empty!")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"\nYou've entered Email: {username} and Password: {password}. Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {username} | {password}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=40)
password_img = PhotoImage(file="logo.png")

canvas = Canvas(width=200, height=200)
# canvas.create_image(100, 100, image=password_img)
canvas.grid(column=1, row=0)

# website
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=52)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

# Email/username
username_label = Label(text="Email/Username:")
username_label.grid(column=0, row=2)
username_entry = Entry(width=52)
username_entry.insert(0, "abc@gmail.com")
username_entry.grid(column=1, row=2, columnspan=2)

# password
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)
password_entry = Entry(width=34)
password_entry.grid(column=1, row=3, columnspan=1)

# generate button
generate_button = Button(text="Generate Password", highlightthickness=0, command=gen_password)
generate_button.grid(column=2, row=3)

# add button
add_button = Button(text="Add", width=45, highlightthickness=0, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
