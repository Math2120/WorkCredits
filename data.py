import time
from tkinter import *
from tkinter import ttk

# retrieve the user's credits from the txt file
def get_user_credits():
    file = open("user_credits.txt", "r")
    content = file.read()

    if content == '':
        user_credits = 0
    else:
        user_credits = int(content)

    file.close()
    return int(user_credits)

# save the user's credits in the txt file
def save_user_credits(credits, credits_label):
    # we add the credits to the txt file
    with open("user_credits.txt", "w") as file:
        file.write(str(credits))
        
    credits_label.config(text='Number of credits : ' + str(credits))
    root.update()

# update the user's credits on the interface
def update(label):
    user_credits = get_user_credits()
    label.config(text='Number of credits : ' + str(user_credits))

# the function works not with buttons
def add_widgets(type, root, text):
    widget = type(root, text=text)
    widget.pack()
    return widget

# so this function create only buttons
def add_button(root, text, command):
    button = Button(root, text=text, command=command)
    button.pack()

root = Tk()
root.minsize(400, 375)
notebook = ttk.Notebook()