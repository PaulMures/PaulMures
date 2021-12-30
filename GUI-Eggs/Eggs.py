from tkinter import *
from tkinter import messagebox
import random



def create_window():
    new_window=Toplevel()
    new_window.geometry("200x200")
    new_window.title("Yolk?")
    new_window.config(background="yellow")

    def click():
        if messagebox.askokcancel(title='Yolk',message='Your yolk is ' + yourYolk):
            print("Been Yolked")
            new_window.destroy()
        else:
            print("You yolkn't")

    button=Button(new_window,
        text="yolk?",
        command=click,
        font=('Times New Roman',40),
        fg='black',
        bg='yellow')
    button.pack()

    yolk=('in need of love );','bad, leave.','truly beutiful (:','ugly','piss','Master Oogway Flavored','a warcrime','absolutely horiffic','missing ):','the size of a tree','sad',"Alex's nice hair",'yellow','moldy','PURPLE','watery','solid','gooey','nutricious','spherical','disgusting','fishy','ostrich','smooth','parked','loud','black','poggers','yolk')
    yourYolk=random.choice(yolk)


window = Tk()
window.geometry("400x400")
window.title("Egg")
window.config(background="white")

icon= PhotoImage(file='Egg.png')
window.iconphoto(True,icon)



label = Label(window,
                text="Egg",
                font=('Times New Roman',69),
                fg='purple',
                bg='white')
label.place(x=131,y=131)

button = Button(window,
                text="Crack Shell",
                command=create_window,
                font=("Times New Roman",30),
                fg="purple",
                bg="white",
                activeforeground="green",
                activebackground="white",
                )
button.pack()


window.mainloop()











