from easygui import *

### MESSAGE BOX ####
text = "This is a Message Box"
title = "box title"
ok_btn_txt_1 = "ok"
output = msgbox(message, title, ok_btn_txt_1)
print("User pressed : ",output)

### INTEGER / ENTER BOX ####
text = "Enter Something"
title = "Window Title"
d_text = "Enter here..."
output = enterbox(text, title, d_text)
title = "Message Box"
message = "Entered Text : " + str(output)
msg = msgbox(message, title)

### INDEX BOX ####
message = "Choose a button"
title = "buttons"
buttons = ["button1", "button2", "button3"]
output = indexbox(message, title, buttons)

message = "You selected : " + str(output+1) + " button"
title = "message box"
msg = msgbox(message,title)

### TEXT BOX ####
message = "Below is the text to edit"
title = "Window Box"
text = ["random txt random txt hihi haha huhu"]
output = textbox(message, title, text)
print("Altered Text ")
print("=======================")
print(output)

### yn BOX ####
message = "yes or no?"
title = "Window Box"
choices = ["haan", "naa"]
output = ynbox(message, title, choices)
if output:
  print(True)
else:
  print(False)
