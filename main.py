from tkinter import *
import random
import re


# Functioning part
def msgToCode():
    message = msgTextarea.get(1.0, END)
    symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "<", ">", "?", "{", "}", "[", "]", ":"]
    two_layer_code = ""
    four_layer_code = ""
    for a in message:
        two_layer_code += (str(ord(a)) + random.choice(symbols))
    for a in two_layer_code:
        four_layer_code += (str(ord(a)) + random.choice(symbols))
    codeTextarea.delete(1.0, END)
    codeTextarea.insert(END, four_layer_code)


def clear():
    msgTextarea.delete(1.0, END)
    codeTextarea.delete(1.0, END)


def codeToMsg():
    code = codeTextarea.get(1.0, END)
    subcode_one = re.findall(r"[\w']+", code)
    sub_message = ""
    for a in subcode_one:
        sub_message += chr(int(a))
    subcode_two = re.findall(r"[\w']+", sub_message)
    final_message = ""
    for a in subcode_two:
        final_message += chr(int(a))
    msgTextarea.delete(1.0, END)
    msgTextarea.insert(END, final_message)


# GUI part
root = Tk()
root.title("Message converter basic model")
root.geometry("1200x650+30+15")
root.resizable(False, False)
root.iconbitmap("icon.ico")

# =============================== main heading ==================================
# headingLabel = Label(root, text="MESSAGE CONVERTER", font=("arial", 35, "bold"), background="yellow", foreground="blue")
headingLabel = Label(root, text="MESSAGE CONVERTER", font=("arial", 35, "bold"), background="aquamarine2",
                     foreground="blue")
headingLabel.pack(fill=X, pady=8)

# =============================== message frame ==================================
# messageLabelFrame = LabelFrame(root, bg="hot pink")
messageLabelFrame = LabelFrame(root, bg="cadetBlue1")
messageLabelFrame.pack(fill=X)

msgbox = Label(messageLabelFrame)
msgbox.grid(row=0, column=0, padx=45, pady=20)

msgLabel = Label(msgbox, text="Your message", font=("arial roman", 25, "bold"), background="aqua", foreground="green4")
msgLabel.pack(fill=X)
msgScrollbar = Scrollbar(msgbox, orient=VERTICAL)
msgScrollbar.pack(side=RIGHT, fill=Y)
msgTextarea = Text(msgbox, font=("arial", 18), height=14, width=37, yscrollcommand=msgScrollbar.set,
                   foreground="green2", background="Light Cyan2")
msgTextarea.pack()
msgScrollbar.config(command=msgTextarea.yview)

codebox = Label(messageLabelFrame)
codebox.grid(row=0, column=1, pady=20, padx=45)

codeLabel = Label(codebox, text="Your code", font=("arial roman", 25, "bold"), background="aqua",
                  foreground="orange red")
codeLabel.pack(fill=X)
codeScrollbar = Scrollbar(codebox, orient=VERTICAL)
codeScrollbar.pack(side=RIGHT, fill=Y)
codeTextarea = Text(codebox, font=("arial", 18), height=14, width=37, yscrollcommand=codeScrollbar.set,
                    foreground="orange red", background="Light Cyan2")
codeTextarea.pack()
codeScrollbar.config(command=codeTextarea.yview)

# ================================== button section ==============================
# buttonLabel = LabelFrame(root, bg="blue")
buttonLabel = LabelFrame(root, bg="aquamarine2")
buttonLabel.pack(fill=X, pady=5)

msgtocodeButton = Button(buttonLabel, text="Message to Code", font=("arial", 20, "bold"), bg="green2",
                         activebackground="orange red", command=msgToCode)
# msgtocodeButton.grid(row=0,column=0,pady=14)
msgtocodeButton.place(x=165, y=14)

clearButton = Button(buttonLabel, text="Clear", font=("arial", 20, "bold"), bg="red", activebackground="black",
                     activeforeground="red", command=clear)
# clearButton.grid(row=0,column=1,pady=14)
clearButton.place(x=550, y=14)

codetomsgButton = Button(buttonLabel, text="Code to Message", font=("arial", 20, "bold"), bg="orange red",
                         activebackground="green2", command=codeToMsg)
codetomsgButton.grid(row=0, column=2, pady=14, padx=790)
# codetomsgButton.place(x=800,y=14)

root.mainloop()
