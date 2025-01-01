import time
from tkinter import *

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