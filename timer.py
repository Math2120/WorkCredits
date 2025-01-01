import time
from tkinter import *

def timer_add_tkinter(credits, root):
    # we create the elements for the timer's part on the tkinter window
    credits_label = Label(root, text='Number of credits : ' + str(credits))
    credits_label.pack()    

    # we global the timer label because he has to be accessed by the timer function
    global timer_label
    timer_label = Label(root, text="00:00:00")
    timer_label.pack()

    time_label = Label(root, text="Enter the time you want to work.")
    time_label.pack()
    time_entry = Entry(root)
    time_entry.pack()
    
    play_timer = Button(root, text="Timer", command=lambda: start_timer(credits, time_entry.get(), root, credits_label))
    play_timer.pack()

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
        seconds -= 1
        elapsed_seconds = initial_seconds - seconds
        # every minute, the user earn a credit
        if elapsed_seconds % 60 == 0:
            credits += 1
 
    timer_label.config(text='00:00:00')
    root.update()
    print(f'Total Credits Earned: {credits}')
    return credits

def start_timer(credits, number_time, root, credits_label):
    if number_time == '' or int(number_time) == 0:
        print("Sorry, but you can't work 0 seconds or nothing.")
    else:
        credits += timer(int(number_time), root)
        
        # we add the credits to the txt file
        with open("user_credits.txt", "w") as file:
            file.write(str(credits))
            
        credits_label.config(text='Number of credits : ' + str(credits))
        root.update()