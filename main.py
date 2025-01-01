global user_credits
import time
from tkinter import *
from tkinter import ttk

notebook = ttk.Notebook()
from timer import *
from shop import *

# we retrieve the user's credits from the txt file
file = open("user_credits.txt", "r")
content = file.read()

if content == '':
    user_credits = 0
else:
    user_credits = int(content)

file.close()

#####################
#                   #
#   Tkinter's part  #
#                   #
#####################

root = Tk()
root.minsize(400, 375)

shop_add_tkinter1(root)
shop_add_tkinter2(root)

timer_add_tkinter(user_credits, root)

root.mainloop()