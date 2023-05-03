from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Adding a label inside GUI
my_label = Label(text="I'm a label", font=("Arial", 24, "bold"))
# my_label.pack()
# my_label.pack(side="bottom")  To orient the text to bottom of GUI

# Change the label text using one of these methods
my_label["text"] = "New Text"
# OR
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

# Button Component
def button_clicked():
    new_text = input.get()
    my_label.config(text=new_text)


button = Button(text="Click me", command=button_clicked)
button.grid(column=1, row=1)
# New Button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)
# Entry Component (input)
input = Entry(width=15)
input.grid(column=3, row=2)

print(input.get())
# Looping the GUI to remain in the screen
window.mainloop()
