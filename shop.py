from tkinter import *

# we retrieve the user's credits from the txt file
file = open("user_credits.txt", "r")
content = file.read()

if content == '':
    user_credits = 0
else:
    user_credits = int(content)

file.close()

root = Tk()
root.minsize(400, 375)

title1 = Label(root, text='Welcome to the shop!')
title1.pack()

title2 = Label(root, text='Here you can buy time to play games, watch videos and more!')
title2.pack()

credits = Label(root, text='Number of credits : ' + str(user_credits))
credits.pack()

title3 = Label(root, text='List of products :')
title3.pack()

listbox = Listbox(root)
listbox.pack()

items = ['Minecraft', 'Valorant', 'Rocket League', 'Multigaming', 'Youtube videos']
for item in items:
    listbox.insert('end', item)
    
def on_select(event):
    global selected_item
    selected_item = listbox.get(listbox.curselection())
    
def buy_product(selected_item, number):
    if number == '' or int(number) == 0:
        print("You cannot purchase 0 or nothing.")
    elif selected_item == None or selected_item == '':
        print("Please select an item to purchase.")
    else:
        print(f'Purchased product: {selected_item}, {number} time(s)')
    
def attempt_purchase():
    try:
        selected_item
    except NameError:
        print("Warning : Please select a product before purchasing.")
    else:
        buy_product(selected_item, number.get())     

listbox.bind('<<ListboxSelect>>', on_select)

number_label = Label(root, text='Number of the product wanted')
number_label.pack()

number = Entry(root, text='Enter the number of times you want the product.')
number.pack()

buy = Button(root, text='Buy', command=attempt_purchase)
buy.pack()

root.mainloop()