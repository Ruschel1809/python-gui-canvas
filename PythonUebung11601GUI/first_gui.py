 from tkinter import *


 def loeschen():
     entry.delete(0, END)

 def beenden():
     fenster.destroy()


 fenster = Tk()
 fenster.title("Hallo Welt!")
 label = Label(master=fenster, text="Hallo Welt!", width=35, height=2,font=("Arial", 14))
 entry = Entry(master=fenster, width=25, font=("Arial", 14))
 button_l = Button(master=fenster, text="Löschen", command=loeschen)
 button_b = Button(master=fenster, text="Beenden", command=beenden)
 label.grid(row=0, column=0)
 entry.grid(row=1, column=0)
 button_l.grid(row=3, column=0)
 button_b.grid(row=3, column=1)
 fenster.mainloop()
