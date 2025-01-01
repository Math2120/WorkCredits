global user_credits
import time
from tkinter import *
from tkinter import ttk

from timer import *
from shop import *

frame_timer = timer_add_tkinter()
frame_shop = shop_add_tkinter()

notebook.add(frame_timer, text="Timer")
notebook.add(frame_shop, text="Shop")

notebook.pack()
root.mainloop()