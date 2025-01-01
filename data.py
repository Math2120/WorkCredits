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
    return int(user_credits)

def save_user_credits(credits, credits_label):
    # we add the credits to the txt file
    with open("user_credits.txt", "w") as file:
        file.write(str(credits))
        
    credits_label.config(text='Number of credits : ' + str(credits) + ' (5 credits = 1min)')
    root.update()

def update(label):
    user_credits = get_user_credits()
    label.config(text='Number of credits : ' + str(user_credits) + ' (5 credits = 1min)')
    
def add_button_update(window, label):
    button_update = Button(window, text="Update the page", command=lambda: update(label))
    button_update.pack()

root = Tk()
root.minsize(400, 375)
notebook = ttk.Notebook()