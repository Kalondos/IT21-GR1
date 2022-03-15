##########
# Kiirold emcee himself kodar
# 15.03.2022
# UL %
#########
import tkinter as tk
from tkinter import *

#Aken
aken = tk.Tk()
aken.title('Käibemaks')
aken.geometry("300x200")


def summa():
    kokku = int(sisendamine.get())
    protsent = int(var.get())
    kaibemaks = (kokku/100*protsent)
    hind = (kokku+kaibemaks)
    valjund2.config(text=f"{kaibemaks}€")
    valjund3.config(text=f"{hind}€")
    
    
#Tekst
Tekst = Label(aken, text="Hind käibemaksuta:")
Tekst.grid(row=0,column=0)
valjund = Label(aken, text="   _______________________________________________________")
valjund.grid(row=6,columnspan=3)
valjund = Label(aken, text="Käibemaksumäär:")
valjund.grid(row=4,column=0)
valjund = Label(aken, text="Käibemaks:")
valjund.grid(row=7,column=0)
valjund2 = Label(aken, text="")
valjund2.grid(row=7,column=1)
valjund = Label(aken, text="Hind käibemaksuga:")
valjund.grid(row=8,column=0)
valjund3 = Label(aken, text="")
valjund3.grid(row=8,column=1)
sisendamine = Entry(aken)
sisendamine.grid(row=0,column=1)
#nupp
nupp1 = Button(aken, text="Vastus", width=10, command=summa)
nupp1.grid(row=9, column=1)
#valik
var = IntVar()
protsent2 = Radiobutton(aken,text="9%", variable=var, value=9)
protsent2.grid(row=4, column=1)
protsent2 = Radiobutton(aken,text="20%", variable=var, value=20)
protsent2.grid(row=5, column=1)



















aken.mainloop()