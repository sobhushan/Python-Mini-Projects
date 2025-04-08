from tkinter import *
from tkinter import messagebox

root = Tk(className="calculator")
root.geometry("290x300")

# Display question
display_label = Label(root,
                      text="",
                      width=26,
                      borderwidth=10,
                      bg="white",
                      anchor="w")
display_label.place(x=30, y=30)

inp = ""

# Function to update the display
def update_display(value):
    global inp
    inp += value
    display_label.config(text=inp)

def clear_display():
    global inp
    inp = ""
    display_label.config(text=inp)

def backspace():
    global inp
    inp = inp[:-1]
    display_label.config(text=inp)

def calculate():
    global inp
    try:
        res = eval(inp)
        if res % 1 == 0:
            res = int(res)
        display_label.config(text=str(res))
        inp = str(res)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Number and operator buttons
buttons = [
    ('7', 30, 120), ('8', 90, 120), ('9', 150, 120), ('+', 210, 120),
    ('4', 30, 160), ('5', 90, 160), ('6', 150, 160), ('-', 210, 160),
    ('1', 30, 200), ('2', 90, 200), ('3', 150, 200), ('*', 210, 200),
    ('0', 30, 240), ('.', 90, 240), ('=', 150, 240), ('/', 210, 240)
]

for (text, x, y) in buttons:
    Button(root, text=text, width=3, command=lambda t=text: update_display(t)).place(x=x, y=y)

# Special buttons
Button(root, text="Clear", width=5, command=clear_display, activebackground="white", activeforeground="blue").place(x=30, y=80)
Button(root, text="BKSP", width=5, command=backspace, activebackground="white", activeforeground="blue").place(x=193, y=80)

root.mainloop()
