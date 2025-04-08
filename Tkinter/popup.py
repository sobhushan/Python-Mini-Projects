from tkinter import *
from tkinter import messagebox

root = Tk() 
root.geometry("200x200")

def yes():
  print(True)

def no():
  print(False)

def popup():
  if messagebox.askyesno("Question","Are you sure?"):
    print("TRUEE")

  else:
    print("FALSEE")

msg = Message(root, text = "Say yes or no?")
msg.pack(side="top")

b1 = Button(root, text = "Yes", command=yes).pack()
b2 = Button(root, text = "No", command=no).pack()
b3 = Button(root, text = "popup", command=popup).pack()
root.mainloop()