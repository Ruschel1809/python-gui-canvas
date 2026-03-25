# import time as t
# from tkinter import *
#
# fenster = Tk()
#
# def ausgabe_text():
#     stempel = t.asctime()
#     ausgabetext = "{} {}".format(opening.get(), name.get())
#     ausgabe.config(text=ausgabetext)
#     zeile = "{}: {}\n".format(stempel,ausgabetext)
#     log.insert(END, zeile)
#
#
# opening = StringVar()
# opening.set("Keine Begrüßung ausgewählt") # damit kein Radiobutton beim Öffnen ausgewählt ist
# ausgabe = Label(fenster, text="Ihre Begrüßung erscheint hier.", font=("Arial", 14),fg="blue", bg="red")
# morgen = Radiobutton(master=fenster, text="Guten Morgen!", value="Guten Morgen!", variable=opening)
# tag = Radiobutton(master=fenster, text="Guten Tag!", value="Guten Tag!", variable=opening)
# abend = Radiobutton(master=fenster, text="Guten Abend!", value="Guten Abend!", variable=opening)
# name = Entry(master=fenster)
# name.insert(0, 'Name')
# nachricht = Button(master=fenster, text='Nachricht', command=ausgabe_text)
# log = Text(master=fenster, font=("Terminal",10))
#
# ausgabe.grid(row=0, column=0, pady=10, columnspan=2)
# name.grid(row=1, column=0, pady=10, columnspan=2)
# morgen.grid(row=2, column=0, pady=10, sticky=W)
# tag.grid(row=3, column=0, pady=10, sticky=W)
# abend.grid(row=4, column=0, pady=10, sticky=W)
# nachricht.grid(row=5, column=0, pady=10, columnspan=2)
# log.grid(row=6, column=0, pady=10, columnspan=2)
# fenster.mainloop()

# Musterlösung
from tkinter import Tk, Label, Button, Entry, Radiobutton, Text, StringVar, END
from datetime import datetime


def aktuelle_zeit_als_string():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def begruessung():
    name = name_entry.get()
    zeit = zeit_var.get()
    begruessungstext = f"{zeit}, {name}!"
    begruessungslabel.config(text=begruessungstext)
    log.insert(END, f"{aktuelle_zeit_als_string()}: {begruessungstext}\n")


app = Tk()
app.title("Begrüßungs-App")


name_entry = Entry(app)
name_entry.grid(row=0, column=1, padx=10, pady=10)


begruessungslabel = Label(app, text="", font=('Arial', 16))
begruessungslabel.grid(row=1, column=0, columnspan=2, padx=10, pady=10)


begrussungsbutton = Button(app, text="Begrüßen", command=begruessung)
begrussungsbutton.grid(row=0, column=2, padx=10, pady=10)


zeit_var = StringVar()
zeit_var.set("Guten Tag")


Radiobutton(app, text="Guten Morgen", variable=zeit_var, value="Guten Morgen").grid(row=2, column=0)
Radiobutton(app, text="Guten Tag", variable=zeit_var, value="Guten Tag").grid(row=2, column=1)
Radiobutton(app, text="Guten Abend", variable=zeit_var, value="Guten Abend").grid(row=2, column=2)


log = Text(app, height=10, width=50)
log.grid(row=3, column=0, columnspan=3, padx=10, pady=10)


app.mainloop()
