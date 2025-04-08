from tkinter import *
from tkinter import messagebox

root = Tk(className="calculator")
root.geometry("290x300")

#display question
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
  inp = inp + value
  display_label.config(text=inp)


def zero():
  update_display("0")


def one():
  update_display("1")


def two():
  update_display("2")


def three():
  update_display("3")


def four():
  update_display("4")


def five():
  update_display("5")


def six():
  update_display("6")


def seven():
  update_display("7")


def eight():
  update_display("8")


def nine():
  update_display("9")


def dot():
  update_display(".")


# Defining functions
def add():
  update_display(" + ")


def sub():
  update_display(" - ")


def mul():
  update_display(" * ")


def div():
  update_display(" / ")


def brc1():
  update_display(" ( ")


def brc2():
  update_display(" ) ")


def equal():
  # global inp
  # num = inp.split()
  # print(num)
  # try:
  #   if num[1] == "+":
  #     res = float(num[0]) + float(num[2])

  #   elif num[1] == "-":
  #     res = float(num[0]) - float(num[2])

  #   elif num[1] == "*":
  #     res = float(num[0]) * float(num[2])

  #   elif num[1] == "/":
  #     res = float(num[0]) / float(num[2])
  global inp
  try:
    res = eval(inp)

    if res % 1 == 0:
      res = int(res)

    display_label.config(text=res)
    inp = str(res)
  except Exception as e:
    messagebox.showerror("Error", str(e))


def clear():
  global inp
  inp = ""
  display_label.config(text="")


def bksp():
  global inp
  inp = inp[:-1]
  display_label.config(text=inp)


#operator buttons
b1 = Button(root, text="+", command=add, width=3,
            activebackground="#E3E4A5").place(x=210, y=120)
b2 = Button(root, text="-", command=sub, width=3,
            activebackground="#E3E4A5").place(x=210, y=160)
b3 = Button(root, text="*", command=mul, width=3,
            activebackground="#E3E4A5").place(x=210, y=200)
b4 = Button(root, text="/", command=div, width=3,
            activebackground="#E3E4A5").place(x=210, y=240)

#number buttons
n0 = Button(root, text="0", command=zero).place(x=90, y=240)
n1 = Button(root, text="1", command=one).place(x=30, y=200)
n2 = Button(root, text="2", command=two).place(x=90, y=200)
n3 = Button(root, text="3", command=three).place(x=150, y=200)
n4 = Button(root, text="4", command=four).place(x=30, y=160)
n5 = Button(root, text="5", command=five).place(x=90, y=160)
n6 = Button(root, text="6", command=six).place(x=150, y=160)
n7 = Button(root, text="7", command=seven).place(x=30, y=120)
n8 = Button(root, text="8", command=eight).place(x=90, y=120)
n9 = Button(root, text="9", command=nine).place(x=150, y=120)
n10 = Button(root,
             text="=",
             command=equal,
             bg="#cfcfcf",
             activebackground="#E4A5A5").place(x=150, y=240)
n11 = Button(root, text=".", command=dot).place(x=30, y=240)

cl = Button(root,
            text="AC",
            command=clear,
            activebackground="white",
            activeforeground="blue").place(x=30, y=80)
q = Button(root,
           text="BKSP",
           command=bksp,
           width=3,
           activebackground="white",
           activeforeground="blue").place(x=210, y=80)

b5 = Button(root, text="(", command=brc1, width=1,
            activebackground="#E3E4A5").place(x=90, y=80)
b6 = Button(root, text=")", command=brc2, width=1,
            activebackground="#E3E4A5").place(x=150, y=80)

root.mainloop()
