#############
# Karlos fernando emiilio viies kotter
# 15.03.2022
# UL 3
#############

from tkinter import *

#aknena
aken = Tk()
aken.title("Tere tere, vanakere!")
aken.geometry("400x150")
#nimed
lorem = 'Nimi: Karlos Eriko'
lorem2 = 'Rühm: IT-21'
lorem3 = '2022'
#värvid
Label(aken, text=lorem, foreground="red", background="black", padx=30, font="Tahoma 26 bold italic").pack()
Label(aken, text=lorem2, foreground="red", background="black", padx=300, font="Tahoma 26 bold italic").pack()
Label(aken, text=lorem3, foreground="red", background="black",pady=10, padx=300, font="Tahoma 26 bold italic").pack()
aken.mainloop()