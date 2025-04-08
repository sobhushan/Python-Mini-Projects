from tkinter import *
from tkinter import messagebox

y = 0
for i in range(1, 11):
  x = str(i)
  sen = "Stage " + x + " is passed?"
  if messagebox.askyesno("Question", sen):
    y += 1
    print(True)
  else:
    print(False)

if y >= 7:
  print("Project Passed with", y, "stages")
else:
  print("Project Failed. (only", y, "stages passed)")
