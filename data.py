import time
from tkinter import *
from tkinter import ttk
import pandas as pd

from inventory import *

# retrieve the user's credits from the .csv file
def get_user_credits():
    return int(get_value('credits'))

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