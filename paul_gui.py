#Header-----------------------------------------------------

#Name: paul_GUI
#Programmer: Paul Muresan
#Date Finished:
#Description: Allows selections for one of 4 types of moth
#group, each group having 2 or 3 moth options for purchase.

#Imports----------------------------------------------------

import tkinter

#Define Functions-------------------------------------------

def show_moths():

    species = selected_species.get()

    if species == "1":

        #1 - Bombyx mori - $15
        #2 - Gunda javanica - $6
        #3 - Penicillifera apicalis - $10
        #4 - Colla umbrata - $9

        option_label.configure(text="Bombyx mori - $15\nGunda javanica - $6\nPenicillifera apicalis - $10\nColla umbrata - $9")
    
    elif species == "2":

        #1 - Lymantria dispar - $20
        #2 - Eulepidotis affinis - $4
        #3 - Lygephila pastinum - $5
        #4 - Catocala nupta - $10

        option_label.configure(text="Lymantria dispar - $20\nEulepidotis affinis - $4\nLygephila pastinum - $5\nCatocala nupta - $10")
    
    elif species == "3":

        #1 - Hepialus humuli - $6
        #2 - Pharmacis fusconebulosa - $7
        #3 - Korscheltellus lupulina - $2
        #4 - Gazoryctra ganna - $13

        option_label.configure(text="Hepialus humuli - $6\nPharmacis fusconebulosa - $7\nKorscheltellus lupulina - $2\nGazoryctra ganna - $13")

    elif species == "4":

        #1 - Pyralis farinalis - $10
        #2 - Galleria mellonella - $6
        #3 - Arcola malloi - $15
        #4 - Paralipsa gularis - $50

        option_label.configure(text="Pyralis farinalis - $10\nGalleria mellonella - $6\nArcola malloi - $15\nParalipsa gularis - $50")
    
def check_price(moth):

    if moth == "Bombyx mori":
        return "15"
    elif moth == "Gunda javanica":
        return "6"
    elif moth == "Penicillifera apicalis":
        return "10"
    elif moth == "Colla umbrata":
        return "9"
    elif moth == "Lymantria dispar":
        return "20"
    elif moth == "Eulepidotis affinis":
        return "4"
    elif moth == "Lygephila pastinum":
        return "5"
    elif moth == "Catocala nupta":
        return "10"
    elif moth == "Hepialus humuli":
        return "6"
    elif moth == "Pharmacis fusconebulosa":
        return "7"
    elif moth == "Korscheltellus lupulina":
        return "2"
    elif moth == "Gazoryctra ganna":
        return "13"
    elif moth == "Pyralis farinalis":
        return "10"
    elif moth == "Galleria mellonella":
        return "6"
    elif moth == "Arcola malloi":
        return "15"
    elif moth == "Paralipsa gularis":
        return "50"

def add_to_cart_m():

    #Taking values from entry field
    moth_quantity_m = moth_quantity_entry.get()
    moth_m = moth_enter.get()
    moth_family_m = moth_family_enter.get()

    #find moth price
    moth_price = check_price(moth_m)

    #create order list
    your_order = [moth_quantity_m,moth_m,moth_family_m,moth_price]

    #In-Console message
    print(your_order)

    #Adding to cart
    cart.append(your_order)

    #Append to total
    total_cost_list.append(moth_price)

def add_to_cart_s():

    #Redefining moth
    moth_s_order = ""

    #Finding moth
    if selected_species.get() == "1":
            if selected_moth.get() == "1":
                moth_s_order = "Bombyx mori"
            elif selected_moth.get() == "2":
                moth_s_order = "Gunda javanica"
            elif selected_moth.get() == "3":
                moth_s_order = "Penicillifera apicalis"
            elif selected_moth.get() == "4":
                moth_s_order = "Colla umbrata"
    elif selected_species.get() == "2":
            if selected_moth.get() == "1":
                moth_s_order = "Lymantria dispar"
            elif selected_moth.get() == "2":
                moth_s_order = "Eulepidotis affinis"
            elif selected_moth.get() == "3":
                moth_s_order = "Lygephila pastinum"
            elif selected_moth.get() == "4":
                moth_s_order = "Catocala nupta"
    elif selected_species.get() == "3":
            if selected_moth.get() == "1":
                moth_s_order = "Hepialus humuli"
            elif selected_moth.get() == "2":
                moth_s_order = "Pharmacis fusconebulosa"
            elif selected_moth.get() == "3":
                moth_s_order = "Korscheltellus lupulina"
            elif selected_moth.get() == "4":
                moth_s_order = "Gazoryctra ganna"
    elif selected_species.get() == "4":
            if selected_moth.get() == "1":
                moth_s_order = "Pyralis farinalis"
            elif selected_moth.get() == "2":
                moth_s_order = "Galleria mellonella"
            elif selected_moth.get() == "3":
                moth_s_order = "Arcola malloi"
            elif selected_moth.get() == "4":
                moth_s_order = "Paralipsa gularis"

    #Defining moth family
    moth_family_s = ""

    if selected_species.get() == "1":
            moth_family_s = "Bombycidae"
    elif selected_species.get() == "2":
            moth_family_s = "Erebidae"
    elif selected_species.get() == "3":
            moth_family_s = "Hepialidae"
    elif selected_species.get() == "4":
            moth_family_s = "Pyralidae"

    #Defining moth_quantity_s
    moth_quantity_s = "1"

    #find moth price
    moth_price = check_price(moth_s_order)

    #create order list
    your_order = [moth_quantity_s,moth_s_order,moth_family_s,moth_price]

    #In-Console message
    print(your_order)

    #Adding to cart
    cart.append(your_order)

    #Append to total
    total_cost_list.append(moth_price)

def calculate_total():

    if len(total_cost_list) == 1:
        total = int(total_cost_list[0])
    elif len(total_cost_list) == 2:
        total = int(total_cost_list[0]) + int(total_cost_list[1])
    elif len(total_cost_list) == 3 or len(total_cost_list) > 3:
        total = int(total_cost_list[0]) + int(total_cost_list[1]) + int(total_cost_list[2])
    
    total_text = ("Total: ", total)    

    total_label = tkinter.Label(cart_frame,
                                text=total_text)
    total_label.grid(row=7,column=0)

def activate_checkout():

    #First Item
    if len(cart) == 2:

        first_item = tkinter.Label(cart_frame,
                                    text=cart[1])
        first_item.grid(row=3)

    #Second Item
    elif len(cart) == 3:

        second_item = tkinter.Label(cart_frame,
                                    text=cart[2])
        second_item.grid(row=4)

    #Third Item
    elif len(cart) == 4:

        third_item = tkinter.Label(cart_frame,
                                    text=cart[3])
        third_item.grid(row=5)

    #Maximum Items
    elif len(cart) > 3:

        max_items = tkinter.Label(cart_frame,
                                    text="MAXIMUM ITEMS REACHED!!!",
                                    font=("Times",20,"bold italic"),
                                    fg="red")
        max_items.grid(row=6)

    calculate_total()

#Main-------------------------------------------------------

def main():

    #Global Variables
    global selected_species
    global selected_moth
    global option_label
    global selected_payment
    global payment_frame
    global cart
    global checkout
    global cart_frame
    global total_cost_list

    #Establish window variables
    window = tkinter.Tk()
    window.title("paul_gui")
    window.geometry("800x800")

    #First Frame
    menu_frame = tkinter.Frame(window)
    menu_frame.grid(row=0,column=0)

    #Second Frame
    options_frame = tkinter.Frame(window)
    options_frame.grid(row=0,column=1)

    #Third Frame
    selection_options_frame = tkinter.Frame(window)
    selection_options_frame.grid(row=0,column=2)

    #Fourth Frame
    payment_frame = tkinter.Frame(selection_options_frame,relief="solid",bd=2,bg="#b6c1d4")
    payment_frame.grid(row=1,column=0)

    #Fifth Frame
    cart_frame = tkinter.Frame(window)
    cart_frame.grid(row=2,column=1)

    #Menu
        #1 - Bombycidae
        #2 - Erebidae
        #3 - Hepialidae
        #4 - Pyralidae
    
    #selected_group defining
    selected_species = tkinter.StringVar()

    #selected_payment defining
    selected_payment = tkinter.StringVar()

    #Family Label
    family_label = tkinter.Label(menu_frame,
                                text="Moth Family",
                                font=("Comic",30,"bold italic"))
    family_label.grid(row=0,column=0)

    #Option Label
    option_display_label = tkinter.Label(options_frame,
                                        text="Moth & Price",
                                        font=("Comic",30,"bold italic"))
    option_display_label.grid(row=0,column=0)

    #Selection Method Label
    selection_method_label = tkinter.Label(selection_options_frame,
                                           text="Selection Methods",
                                           font=("Comic",30,"bold italic"))
    selection_method_label.grid(row=0,column=0)

    #Radiobuttons for each family
    bombycidae = tkinter.Radiobutton(menu_frame, 
                                    text="Bombycidae",
                                    variable=selected_species, 
                                    value="1",
                                    relief="raised",
                                    anchor="w",
                                    command=show_moths,
                                    font=("Gothic",20),
                                    bd=2)
    bombycidae.grid(row=1,column=0)

    erebidae = tkinter.Radiobutton(menu_frame,
                                    text="Erebidae",
                                    variable=selected_species,
                                    value="2",
                                    relief="raised",
                                    anchor="w",
                                    command=show_moths,
                                    font=("Gothic",20),
                                    bd=2)
    erebidae.grid(row=2,column=0)

    hepialidae = tkinter.Radiobutton(menu_frame,
                                    text="Hepialidae",
                                    variable=selected_species,
                                    value="3",
                                    relief="raised",
                                    anchor="w",
                                    command=show_moths,
                                    font=("Gothic",20),
                                    bd=2)
    hepialidae.grid(row=3,column=0)

    pyralidae = tkinter.Radiobutton(menu_frame,
                                    text="Pyralidae",
                                    variable=selected_species,
                                    value="4",
                                    relief="raised",
                                    anchor="w",
                                    command=show_moths,
                                    font=("Gothic",20),
                                    bd=2)
    pyralidae.grid(row=4,column=0)

    #Defining option_label
    option_label = tkinter.Label(options_frame, 
                                justify="left", 
                                bg="#eeeeee", 
                                text="",
                                font=("Times",20),
                                width=24,
                                height=5,
                                bd=5,
                                relief="raised")
    option_label.grid(row=1,column=0)

    #Manual Pay Area~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #Manual Pay Title
    manual_pay_title = tkinter.Label(payment_frame,
                                         text="Manual Pay",
                                         font=("Times",30),
                                         bg="#6b62c7")
    manual_pay_title.grid(row=0,column=0)

    #Moth Family Label
    moth_family_entry_label = tkinter.Label(payment_frame,
                                                text="Family",
                                                font=("Comic",20,"bold"),
                                                bg="#6b62c7")
    moth_family_entry_label.grid(row=1,column=0)

    #Defining global entry field global variables for add to cart button
    global moth_quantity_entry
    global moth_enter
    global moth_family_enter

    #Moth family entry field
    moth_family_enter = tkinter.Entry(payment_frame)
    moth_family_enter.grid(row=2,column=0)

    #Moth Label
    moth_entry_label = tkinter.Label(payment_frame,
                                         text="Moth & Quantity",
                                         font=("Comic",20,"bold"),
                                         bg="#6b62c7")
    moth_entry_label.grid(row=3,column=0)

    #Moth entry field
    moth_enter = tkinter.Entry(payment_frame)
    moth_enter.grid(row=4,column=0)

    #Moth quantity entry field
    moth_quantity_entry = tkinter.Entry(payment_frame,width=3)
    moth_quantity_entry.grid(row=4,column=1)

    #Creating globals for add to cart button
    global moth_quantity_m
    global moth_m
    global moth_family_m

    #Defining moth quantity, moth and moth family
    moth_quantity_m = moth_quantity_entry.get()
    moth_m = moth_enter.get()
    moth_family_m = moth_family_enter.get()

    #Add to cart button
    add_to_cart_button_m = tkinter.Button(payment_frame,
                                        command=add_to_cart_m,
                                        text="Add To Cart")
    add_to_cart_button_m.grid(row=6,column=0)

    #Smart Pay Area~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #Smart Pay Title
    smart_pay_title = tkinter.Label(payment_frame,
                                        text="  Smart Pay  ",
                                        font=("Times",30),
                                        bg="#F0FFFF")
    smart_pay_title.grid(row=8,column=0)

    #Creating global variable for add to cart button
    global ordered_family

    #Family selected variable (used in label)
    selected_family = ""

    #ordered_family defining
    ordered_family = ""

    #Defining species variable
    species = selected_species.get()

    #Defining text for family label
    if species == "1":
            selected_family = " Family selected: Bombycidae"
            ordered_family = "Bombycidae"
    elif species == "2":
            selected_family = " Family selected: Erebidae "
            ordered_family = "Erebidae"
    elif species == "3":
            selected_family = " Family selected: Hepialidae "
            ordered_family = "Hepialidae"
    elif species == "4":
            selected_family = " Family selected: Pyralidae "
            ordered_family = "Pyralidae"

    #Family selected label
    family_selected_label = tkinter.Label(payment_frame,
                                              text=selected_family,
                                              font=("Times",20,"bold"),
                                              bg="#F0FFFF")
    family_selected_label.grid(row=9,column=0)

    #Variable for moth selection
    selected_moth = tkinter.StringVar()

    #Radiotbuttons for moths
    moth_one = tkinter.Radiobutton(payment_frame,
                                    text="Moth 1",
                                    variable=selected_moth,
                                    value="1",
                                    relief="raised",
                                    anchor="w",
                                    font=("Times",10),
                                    bd=2,
                                    bg="#F0FFFF")   
    moth_one.grid(row=10,column=0)

    moth_two = tkinter.Radiobutton(payment_frame,
                                    text="Moth 2",
                                    variable=selected_moth,
                                    value="2",
                                    relief="raised",
                                    anchor="w",
                                    font=("Times",10),
                                    bd=2,
                                    bg="#F0FFFF")   
    moth_two.grid(row=11,column=0)

    moth_three = tkinter.Radiobutton(payment_frame,
                                    text="Moth 3",
                                    variable=selected_moth,
                                    value="3",
                                    relief="raised",
                                    anchor="w",
                                    font=("Times",10),
                                    bd=2,
                                    bg="#F0FFFF")   
    moth_three.grid(row=12,column=0)

    moth_four = tkinter.Radiobutton(payment_frame,
                                    text="Moth 4",
                                    variable=selected_moth,
                                    value="4",
                                    relief="raised",
                                    anchor="w",
                                    font=("Times",10),
                                    bd=2,
                                    bg="#F0FFFF")   
    moth_four.grid(row=13,column=0)

    #Defining global variables for add to cart button s
    global moth_s
    global moth_family_s
    global moth_quantity_s

    #Defining moth
    moth_s = ""

    #Determining moth
    if species == "1":
            if selected_moth == "1":
                moth_s = "Bombyx mori"
            elif selected_moth == "2":
                moth_s = "Gunda javanica"
            elif selected_moth == "3":
                moth_s = "Penicillifera apicalis"
            elif selected_moth == "4":
                moth_s = "Colla umbrata"
    elif species == "2":
            if selected_moth == "1":
                moth_s = "Lymantria dispar"
            elif selected_moth == "2":
                moth_s = "Eulepidotis affinis"
            elif selected_moth == "3":
                moth_s = "Lygephila pastinum"
            elif selected_moth == "4":
                moth_s = "Catocala nupta"
    elif species == "3":
            if selected_moth == "1":
                moth_s = "Hepialus humuli"
            elif selected_moth == "2":
                moth_s = "Pharmacis fusconebulosa"
            elif selected_moth == "3":
                moth_s = "Korscheltellus lupulina"
            elif selected_moth == "4":
                moth_s = "Gazoryctra ganna"
    elif species == "4":
            if selected_moth == "1":
                moth_s = "Pyralis farinalis"
            elif selected_moth == "2":
                moth_s = "Galleria mellonella"
            elif selected_moth == "3":
                moth_s = "Arcola malloi"
            elif selected_moth == "4":
                moth_s = "Paralipsa gularis"

    #Add to cart button
    add_to_cart_button = tkinter.Button(payment_frame,
                                        command=add_to_cart_s,
                                        text="Add To Cart")
    add_to_cart_button.grid(row=15,column=0)

    #Cart~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #Defining cart variable
    cart = [["Quantity, Moth, Family, Cost"]]

    #Total Cost List
    total_cost_list = []

    #Defining checkout variable
    checkout = False

    #Defining cart_title
    cart_title = tkinter.Label(cart_frame,
                                text="Your Cart",
                                font=("Comic",30,"bold italic"))
    cart_title.grid(row=0,column=0)

    #Cart Checkout button
    checkout_button = tkinter.Button(cart_frame,
                                     text="Checkout",
                                     command=activate_checkout)
    checkout_button.grid(row=1,column=0)

    #Cart place 1 (Description of placement)
    cart_one_text = (cart[0])
    cart_one = tkinter.Label(cart_frame,
                             text=cart_one_text,
                             )
    cart_one.grid(row=2,column=0)

    #Checkout Calculations


    #Invoking and mainloop~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    #Invoking Bombycidae
    bombycidae.invoke()

    #Set window to mainloop
    window.mainloop()

#Running Main-----------------------------------------------

main()