#Header-------------------------------------------

#Name: Paul_Beans (The Moth Counter)
#Programmer: Paul Muresan
#Date Finished: 
#Description: This program will take input to count 
#the number of moths reported of 3 species.

#Imports-------------------------------------------

import tkinter
from tkinter.constants import CENTER
from tkinter.font import BOLD

#Variables-----------------------------------------

gold_swift = 0      #moth type 1
gold_swift_percentage = 0
gold = "#FFD600"
ghost_moth = 0      #moth type 2
ghost_moth_percentage = 0
ghost = "#706F69" #with white outline
iron_prominent = 0  #moth type 3
iron_prominent_percentage = 0
iron = "#474747"
domestic_silk_moth = 0 #moth type 4
domestic_silk_moth_percentage = 0
silk = "#E9E7E0"
peppered_moth = 0   #moth type 5
peppered_moth_percentage = 0
pepper = "#ED6F1C"
atlas_moth = 0      #moth type 6
atlas_moth_percentage = 0
atlas = "#ED4A1C"
white_ermine = 0    #moth type 7
white_ermine_percentage = 0
ermine = "#F4EBE8" #with yellow outline
giant_leopard_moth = 0 #moth type 8
giant_leopard_moth_percentage = 0
leopard = "#FFFFFF" #with black outline
chionarctia_nivea = 0  #moth type 9
chionarctia_nivea_percentage = 0
nivea = "#FFFFFF" #with red outline
moth_question = ""
moth_quantity = 0
total_moth = 0
stop_input = False

#Introduction Statement---------------------------

print("-------------------------------------------------------")
print("This is The Moth Counter and it will recieve your count \nof 3 different moth species and produce statistics")
print("-------------------------------------------------------")

#Program-------------------------------------------

#Input Loop
while (stop_input == False):
    moth_question = input("Select a moth species by number: \n1.Gold Swift\n2.Ghost Moth\n3.Iron Prominent\n4.Domestic Silk Moth\n5.Peppered Moth\n6.Atlas Moth\n7.White Ermine\n8.Giant Leopard Moth\n9.Chionarctia Nivea\nX to cancel\n") #Moth selection

    if (moth_question == "X"): #X input to stop loop
        stop_input = True
    else:
        moth_quantity = int(input("How many are you reporting: ")) #Find Quantity

    if (moth_question == "1"):
        gold_swift = gold_swift + moth_quantity
    elif (moth_question == "2"):
        ghost_moth = ghost_moth + moth_quantity
    elif (moth_question == "3"):
        iron_prominent = iron_prominent + moth_quantity
    elif (moth_question == "4"):
        domestic_silk_moth = domestic_silk_moth + moth_quantity
    elif (moth_question == "5"):
        peppered_moth = peppered_moth + moth_quantity
    elif (moth_question == "6"):
        atlas_moth = atlas_moth + moth_quantity
    elif (moth_question == "7"):
        white_ermine = white_ermine + moth_quantity
    elif (moth_question == "8"):
        giant_leopard_moth = giant_leopard_moth + moth_quantity
    elif (moth_question == "9"):
        chionarctia_nivea = chionarctia_nivea + moth_quantity
    elif (moth_question == "X"):
        print("\nGenerating Statistics . . .\n")
    else:
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print("!! ERROR !! Invalid moth entry !!")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#Console Output Statistics
if (stop_input == True):

    total_moth = gold_swift + ghost_moth + iron_prominent + domestic_silk_moth + peppered_moth + atlas_moth + white_ermine + giant_leopard_moth + chionarctia_nivea
    
    #Calculating percentage
    if (gold_swift != 0):
        gold_swift_percentage = round((gold_swift / total_moth) * 100)
    else:
        gold_swift_percentage = 0

    if (ghost_moth != 0):
        ghost_moth_percentage = round((ghost_moth / total_moth) * 100) 
    else:
        ghost_moth_percentage = 0 

    if (iron_prominent != 0):
        iron_prominent_percentage = round((iron_prominent / total_moth) * 100)  
    else:
        iron_prominent_percentage = 0 

    if (domestic_silk_moth != 0):
        domestic_silk_moth_percentage = round((domestic_silk_moth / total_moth) * 100)  
    else:
        domestic_silk_moth_percentage = 0

    if (peppered_moth != 0):
        peppered_moth_percentage = round((peppered_moth / total_moth) * 100)
    else:
        peppered_moth_percentage = 0  

    if (atlas_moth != 0):
        atlas_moth_percentage = round((atlas_moth / total_moth) * 100)
    else:
        atlas_moth_percentage = 0  

    if (white_ermine != 0):
        white_ermine_percentage = round((white_ermine / total_moth) * 100)
    else:
        white_ermine_percentage = 0

    if (giant_leopard_moth != 0):
        giant_leopard_moth_percentage = round((giant_leopard_moth / total_moth) * 100)
    else:
        giant_leopard_moth_percentage = 0

    if (chionarctia_nivea != 0):
        chionarctia_nivea_percentage = round((chionarctia_nivea / total_moth) * 100)
    else:
        chionarctia_nivea_percentage = 0

    #Statistic Output
    print("-----------------------------------")
    print("The statistics are as following: " + "\nGold Swifts = " + str(gold_swift) + " or " + str(gold_swift_percentage) + "%" + "\nGhost Moths = " + str(ghost_moth) + " or " + str(ghost_moth_percentage) + "%" + "\nIron Prominents = " + str(iron_prominent) + " or " + str(iron_prominent_percentage) + "%" + "\nDomestic Silk Moth " + str(domestic_silk_moth) + " or " + str(domestic_silk_moth_percentage) + "%" + "\nPeppered Moth = " + str(peppered_moth) + " or " + str(peppered_moth_percentage) + "%" + "\nAtlas Moth = " + str(atlas_moth) + " or " + str(atlas_moth_percentage) + "%" + "\nWhite Ermine = " + str(white_ermine) + " or " + str(white_ermine_percentage) + "%" + "\nGiant Leopard Moth = " + str(giant_leopard_moth) + " or " + str(giant_leopard_moth_percentage) + "%" + "\nChionarctia Nivea = " + str(chionarctia_nivea) + " or " + str(chionarctia_nivea_percentage) + "%" + "\nTotal = " + str(total_moth))
    print("-----------------------------------")

#Window--------------------------------------------

window = tkinter.Tk()
window.geometry("1000x1000")
window.title("The Mᛟth Counter")

canvas = tkinter.Canvas(window, bg = "white", height = 1000, width = 1000)

#Bar Graph
gold_swift_nameplate = canvas.create_text(50, 60, text = "Gold Swift", anchor = CENTER, width = 75)
gold_swift_bar = canvas.create_rectangle(100, 50, (100 + gold_swift), 70, fill = gold)
gold_swift_amount = canvas.create_text(150, 60, text = str(gold_swift), anchor = CENTER, width = 75)

ghost_moth_nameplate = canvas.create_text(50, 90, text = "Ghost Moth", anchor = CENTER, width = 75)
ghost_moth_bar = canvas.create_rectangle(100, 80, (100 + ghost_moth), 100, fill = ghost, outline = "white")
ghost_moth_amount = canvas.create_text(150, 90, text = str(ghost_moth), anchor = CENTER, width = 75)

iron_prominent_nameplate = canvas.create_text(50, 120, text = "Iron Prominent", anchor = CENTER, width = 75)
iron_prominent_bar = canvas.create_rectangle(100, 110, (100 + iron_prominent), 130, fill = iron)
iron_prominent_amount = canvas.create_text(150, 120, text = str(iron_prominent), anchor = CENTER, width = 75)

domestic_silk_moth_nameplate = canvas.create_text(50, 150, text = "Silk Moth", anchor = CENTER, width = 75)
domestic_silk_moth_bar = canvas.create_rectangle(100, 140, (100 + domestic_silk_moth), 160, fill = silk)
domestic_silk_moth_amount = canvas.create_text(150, 150, text = str(iron_prominent), anchor = CENTER, width = 75)

peppered_moth_nameplate = canvas.create_text(50, 180, text = "Peppered Moth", anchor = CENTER, width = 75)
peppered_moth_bar = canvas.create_rectangle(100, 170, (100 + peppered_moth), 190, fill = pepper)
peppered_moth_amount = canvas.create_text(150, 180, text = str(peppered_moth), anchor = CENTER, width = 75)

atlas_moth_nameplate = canvas.create_text(50, 210, text = "Atlas Moth", anchor = CENTER, width = 75)
atlas_moth_bar = canvas.create_rectangle(100, 200, (100 + atlas_moth), 220, fill = atlas)
atlas_moth_amount = canvas.create_text(150, 210, text = str(atlas_moth), anchor = CENTER, width = 75)

white_ermine_nameplate = canvas.create_text(50, 240, text = "White Ermine", anchor = CENTER, width = 75)
white_ermine_bar = canvas.create_rectangle(100, 230, (100 + white_ermine), 250, fill = ermine, outline = "yellow")
white_ermine_amount = canvas.create_text(150, 240, text = str(white_ermine), anchor = CENTER, width = 75)

giant_leopard_moth_nameplate = canvas.create_text(50, 270, text = "Leopard Moth", anchor = CENTER, width = 75)
giant_leopard_moth_bar = canvas.create_rectangle(100, 260, (100 + giant_leopard_moth), 280, fill = leopard, outline = "black")
giant_leopard_moth = canvas.create_text(150, 270, text = str(giant_leopard_moth), anchor = CENTER, width = 75)

chionarctia_nivea_nameplate = canvas.create_text(50, 300, text = "Chionarctia", anchor = CENTER, width = 75)
chionarctia_nivea_bar = canvas.create_rectangle(100, 290, (100 + chionarctia_nivea), 310, fill = nivea, outline = "red")
chionarctia_nivea_amount = canvas.create_text(150, 300, text = str(chionarctia_nivea), anchor = CENTER, width = 75)

graph_x_line = canvas.create_line(100, 50, 100, 310, fill = "black", width = 3) #Bar Graph x line
graph_y_line = canvas.create_line(100, 50, 900, 50, fill = "black", width = 3) #Bar Graph y line

#Screen Split
screen_split = canvas.create_line(0, 400, 1000, 400, fill = "black") #Center Screen Splitting Line

#Pie Chart Degree Calculations
gold_swift_degree = (gold_swift_percentage * 360) / 100 
ghost_moth_degree = (ghost_moth_percentage * 360) / 100
iron_prominent_degree = (iron_prominent_percentage * 360) / 100
domestic_silk_moth_degree = (domestic_silk_moth_percentage * 360) / 100
peppered_moth_degree = (peppered_moth_percentage * 360) / 100
atlas_moth_degree = (atlas_moth_percentage * 360) / 100
white_ermine_degree = (white_ermine_percentage * 360) / 100
giant_leopard_moth_degree = (giant_leopard_moth_percentage * 360) / 100
chionarctia_nivea_degree = (chionarctia_nivea_percentage * 360) / 100

#Proportion Pie Graph

#Pies
gold_swift_pie = canvas.create_arc(400, 600, 500, 700, start = 0, extent = gold_swift_degree, fill = gold)
ghost_moth_pie = canvas.create_arc(400, 600, 500, 700, start = 0 + gold_swift_degree, extent = ghost_moth_degree, fill = ghost, outline = "white")
iron_prominent_pie = canvas.create_arc(400, 600, 500, 700, start = 0 + (gold_swift_degree + ghost_moth_degree), extent = iron_prominent_degree, fill = iron)
domestic_silk_moth_pie = canvas.create_arc(400, 600, 500, 700, start = 0 + (gold_swift_degree + ghost_moth_degree + iron_prominent_degree), extent = domestic_silk_moth_degree, fill = silk)
peppered_moth_pie = canvas.create_arc(400, 600, 500, 700, start = 0 +  (gold_swift_degree + ghost_moth_degree + iron_prominent_degree + domestic_silk_moth_degree), extent = peppered_moth_degree, fill = pepper)
atlas_moth_pie = canvas.create_arc(400, 600, 500, 700, start = 0 + (gold_swift_degree + ghost_moth_degree + iron_prominent_degree + domestic_silk_moth_degree + peppered_moth_degree), extent = atlas_moth_degree, fill = atlas)
white_ermine_pie = canvas.create_arc(400, 600, 500, 700, start = 0 + (gold_swift_degree + ghost_moth_degree + iron_prominent_degree + domestic_silk_moth_degree + peppered_moth_degree + atlas_moth_degree), extent = white_ermine_degree, fill = ermine, outline = "yellow")
giant_leopard_moth_pie = canvas.create_arc(400, 600, 500, 700, start = 0 + (gold_swift_degree + ghost_moth_degree + iron_prominent_degree + domestic_silk_moth_degree + peppered_moth_degree + atlas_moth_degree + white_ermine_degree), extent = giant_leopard_moth_degree, fill = leopard)
chionarctia_nivea_pie = canvas.create_arc(400, 600, 500, 700, start = 0 + (gold_swift_degree + ghost_moth_degree + iron_prominent_degree + domestic_silk_moth_degree + peppered_moth_degree + atlas_moth_degree + white_ermine_degree + giant_leopard_moth_degree), extent = chionarctia_nivea_degree, fill = nivea, outline = "red")

#Proportion Graph Key

#Box
key_box = canvas.create_rectangle(220, 530, 375, 750, fill = "black", outline = "purple", width = 5)

#Keys
gold_swift_key = canvas.create_text(300, 550, text = "Gold Swift", anchor = CENTER, width = 100, fill = gold)
ghost_moth_key = canvas.create_text(300, 570, text = "Ghost Moth", anchor = CENTER, width = 100, fill = ghost)
iron_prominent_key = canvas.create_text(300, 590, text = "Iron Prominent", anchor = CENTER, width = 100, fill = iron)
domestic_silk_moth_key = canvas.create_text(300, 610, text = "Domestic Silk Moth", anchor = CENTER, width = 150, fill = silk)
peppered_moth_key = canvas.create_text(300, 630, text = "Peppered Moth", anchor = CENTER, width = 100, fill = pepper)
atlas_moth_key = canvas.create_text(300, 650, text = "Atlas Moth", anchor = CENTER, width = 100, fill = atlas)
white_ermine_key = canvas.create_text(300, 670, text = "White Ermine", anchor = CENTER, width = 100, fill = ermine)
giant_leopard_moth = canvas.create_text(300, 690, text = "Giant Leopard Moth", anchor = CENTER, width = 150, fill = leopard)
chionarctia_nivea_key = canvas.create_text(300, 710, text = "Chionarctia Nivea", anchor = CENTER, width = 150, fill = nivea)


canvas.pack()
window.mainloop()