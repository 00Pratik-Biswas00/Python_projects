from tkinter import  *

window = Tk()
window.title("Km to Mile Converter")
window.minsize(width=300, height=50)
window.config(pady=30, padx=30)

# label
label1 = Label(text="Your entry:", font=("Arial", 12))
label1.config(pady=5, padx=10)
label1.grid(column=0, row=0)

# entry
km_input = Entry(width=10)
km_input.grid(column=1, row=0)

# label
km_text = Label(text="Km", font=("Arial", 12))
km_text.config(padx=10)
km_text.grid(column=2, row=0)

# label
is_equal_label = Label(text="is equal to", font=("Arial", 12))
is_equal_label.config(padx=10)
is_equal_label.grid(column=0, row=1)

# label
result = Label(text=0, font=("Arial", 12))
result.grid(column=1, row=1)
result.config(pady=15)

# label
miles_label = Label(text="Miles", font=("Arial", 12))
miles_label.config(padx=10)
miles_label.grid(column=2, row=1)

def convert():
    km = float(km_input.get())
    miles = km * 0.621371
    result.config(text=f"{miles}")

# button
button = Button(text="Calculate", command=convert, font=("Arial", 12))
button.grid(column=1, row=2)

window.mainloop()
