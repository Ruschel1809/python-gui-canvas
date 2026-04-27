 import time as t
 from tkinter import *

 fenster = Tk()

 def ausgabe_text():
     stempel = t.asctime()
     ausgabetext = "{} {}".format(opening.get(), name.get())
     ausgabe.config(text=ausgabetext)
     zeile = "{}: {}\n".format(stempel,ausgabetext)
     log.insert(END, zeile)


 opening = StringVar()
 opening.set("Keine Begrüßung ausgewählt") # damit kein Radiobutton beim Öffnen ausgewählt ist
 ausgabe = Label(fenster, text="Ihre Begrüßung erscheint hier.", font=("Arial", 14),fg="blue", bg="red")
 morgen = Radiobutton(master=fenster, text="Guten Morgen!", value="Guten Morgen!", variable=opening)
 tag = Radiobutton(master=fenster, text="Guten Tag!", value="Guten Tag!", variable=opening)
 abend = Radiobutton(master=fenster, text="Guten Abend!", value="Guten Abend!", variable=opening)
 name = Entry(master=fenster)
 name.insert(0, 'Name')
 nachricht = Button(master=fenster, text='Nachricht', command=ausgabe_text)
 log = Text(master=fenster, font=("Terminal",10))

 ausgabe.grid(row=0, column=0, pady=10, columnspan=2)
 name.grid(row=1, column=0, pady=10, columnspan=2)
 morgen.grid(row=2, column=0, pady=10, sticky=W)
 tag.grid(row=3, column=0, pady=10, sticky=W)
 abend.grid(row=4, column=0, pady=10, sticky=W)
 nachricht.grid(row=5, column=0, pady=10, columnspan=2)
 log.grid(row=6, column=0, pady=10, columnspan=2)
 fenster.mainloop()



app.mainloop()
