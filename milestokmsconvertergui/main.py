from tkinter import *

window = Tk()
window.title("Miles to Kilometer Convertor")
window.config(padx=20, pady=20)

miles_input = Entry(width=7)
miles_input.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1, column=0)

kilometer_result_label = Label(text="0")
kilometer_result_label.grid(row=1, column=1)

kilometer_label = Label(text="Km")
kilometer_label.grid(row=1, column=2)


def calculate():
    kilometer_result = float(miles_input.get()) * 1.609344
    kilometer_result_label.config(text=f"{kilometer_result}")


calculate = Button(text="Calculate", command=calculate)
calculate.grid(row=2, column=1)

window.mainloop()
