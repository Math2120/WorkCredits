from tkinter import *

from data import *

# buy products based on the user's credits
def buy_product(selected_item, number):
    user_credits = get_user_credits()
    
    if number == '' or int(number) == 0:
        print("You cannot purchase 0 or nothing.")
    elif selected_item == None or selected_item == '':
        print("Please select an item to purchase.")
    else:
        amount_credits_needed = int(number)*5        
        if user_credits < amount_credits_needed:
            print("Sorry, but you don't have enough credits to buy that!")
        else:
           print(f'Purchased product: {selected_item}, {number} time(s)')
           user_credits -= amount_credits_needed
           save_user_credits(user_credits, credits_label)

# we add the first part of the widgets for the shop's page
def shop_add_tkinter1(root):
    # we retrieve the selected item of the listbox
    def on_select(event):
        global selected_item
        selected_item = listbox.get(listbox.curselection())    

    title1 = add_widgets(Label, root, "Welcome to the shop!")
    title2 = add_widgets(Label, root, "Here you can buy time to play games, watch videos and more!")

    global credits_label
    credits_label = Label(root, text='Number of credits : ' + str(get_user_credits()))
    credits_label.pack()

    title3 = add_widgets(Label, root, "List of products : (5 credits = 1min)")

    listbox = Listbox(root)
    listbox.pack()

    # here we can change the products by changing this array
    items = ['Minecraft', 'Valorant', 'Rocket League', 'Multigaming', 'Youtube videos']
    for item in items:
        listbox.insert('end', item)
        
    listbox.bind('<<ListboxSelect>>', on_select)   

# we add the second part of the widgets for the shop's page
def shop_add_tkinter2(root):
    # if one product is selected, we try to buy it with the buy_product function
    def attempt_purchase():
        try:
            selected_item
        except NameError:
            print("Please select a product before purchasing.")
        else:
            buy_product(selected_item, number.get()) 

    number_label = add_widgets(Label, root, "Amount of minute you want to spend")
    number = add_widgets(Entry, root, "Enter the number of times you want the product.")

    buy = add_button(root, "Buy", attempt_purchase)

# we finally combine all the widgets of the shop's page together
def shop_add_tkinter():
    frame = Frame()
    shop_add_tkinter1(frame)
    shop_add_tkinter2(frame)
    button_update = add_button(frame, "Update the page", lambda: update(credits_label))
    
    return frame