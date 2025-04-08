#CALCULATOR#
from tkinter import *
from tkinter import messagebox  
root = Tk(className="calculator")
root.geometry("400x300") 

#title 
lb1 = Label(root, text="Enter 1st number").place(x = 30,y = 50)
lb2 = Label(root, text="Enter 2nd number").place(x = 30,y = 90)

in1 = Entry(root)
in1.place(x=150, y=50)
in2 = Entry(root)
in2.place(x=150, y=90)

# Defining functions
def add():
  num1 = float(in1.get())
  num2 = float(in2.get())
  res = num1 + num2
  if res % 1 == 0:
    res = int(res)
  msg = "Addition of two numbers is " + str(res)
  messagebox.showinfo("Result", msg)

def sub():
  num1 = float(in1.get())
  num2 = float(in2.get())
  res = abs(num1 - num2)
  if res % 1 == 0:
    res = int(res)
  msg = "Difference of two numbers is " + str(res)
  messagebox.showinfo("Result", msg)

def mul():
  num1 = float(in1.get())
  num2 = float(in2.get())
  res = num1 * num2
  if res % 1 == 0:
    res = int(res)
  msg = "Multiplication of two numbers is " + str(res)
  messagebox.showinfo("Result", msg)

def div():
  num1 = float(in1.get())
  num2 = float(in2.get())
  res = num1 / num2
  if res % 1 == 0:
    res = int(res)
  msg = "Division of two numbers is " + str(res)
  messagebox.showinfo("Result", msg)

#operator buttons
b1 = Button(root, text = "+", command=add).place(x = 30,y = 130)
b2 = Button(root, text = "-", command=sub).place(x = 90,y = 130)
b3 = Button(root, text = "*", command=mul).place(x = 150,y = 130)
b4 = Button(root, text = "/", command=div).place(x = 210,y = 130)
ans = Button(root, text = "Quit", command=root.quit).place(x = 270,y = 130)

root.mainloop()