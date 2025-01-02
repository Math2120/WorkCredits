import time
from tkinter import *

from data import *

# we add the widgets of the timer's page
def timer_add_tkinter():
    frame = Frame()
    user_credits = get_user_credits()

    credits_label = add_widgets(Label, frame, "Numbe of credits : " + str(user_credits)) 
    # we global the timer label because he has to be accessed by the timer function
    global timer_label
    timer_label = add_widgets(Label, frame, "00:00:00")
    time_label = add_widgets(Label, frame, "Enter the time you want to work")
    time_entry = add_widgets(Entry, frame, "Enter the time you want to work")
    play_timer = add_button(frame, "Start timer", lambda: start_timer(time_entry.get(), credits_label))
    
    return frame

# the timer's function
def timer(seconds, root):
    credits = 0
    initial_seconds = seconds
    while seconds:
        # divmod attribute the first variable the quotient and the second the remainder
        hrs, secs = divmod(seconds, 3600)
        mins, secs = divmod(secs, 60)
        
        # formatting of the timer
        time_format = '{:02}:{:02}:{:02}'.format(hrs, mins, secs)
        timer_label.config(text=time_format)
        root.update()
        time.sleep(1)
        
        # every minute, the user earn a credit        
        seconds -= 1
        elapsed_seconds = initial_seconds - seconds
        if elapsed_seconds % 60 == 0:
            credits += 1
 
    timer_label.config(text='00:00:00')
    root.update()
    print(f'Total Credits Earned: {credits}')
    
    return credits

# start the timer and handle the follow-up, like save the user's credits
def start_timer(number_time, credits_label):
    if number_time == '' or int(number_time) == 0:
        print("Sorry, but you can't work 0 seconds or nothing.")
    else:
        user_credits = get_user_credits()
        user_credits += timer(int(number_time), root)
        save_user_credits(user_credits, credits_label)