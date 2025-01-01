import time
from tkinter import *
from tkinter import ttk

def get_user_credits():
    # we retrieve the user's credits from the txt file
    file = open("user_credits.txt", "r")
    content = file.read()

    if content == '':
        user_credits = 0
    else:
        user_credits = int(content)

    file.close()
    return user_credits

def update(label):
    user_credits = get_user_credits()
    label.config(text='Number of credits : ' + str(user_credits))
    
def add_button_update(window, label):
    button_update = Button(window, text="Update the page", command=lambda: update(label))
    button_update.pack()

root = Tk()
root.minsize(400, 375)
notebook = ttk.Notebook()