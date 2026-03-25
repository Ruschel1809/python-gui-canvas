# from tkinter import *
#
#
# def loeschen():
#     entry.delete(0, END)
#
# def beenden():
#     fenster.destroy()
#
#
# fenster = Tk()
# fenster.title("Hallo Welt!")
# label = Label(master=fenster, text="Hallo Welt!", width=35, height=2,font=("Arial", 14))
# entry = Entry(master=fenster, width=25, font=("Arial", 14))
# button_l = Button(master=fenster, text="Löschen", command=loeschen)
# button_b = Button(master=fenster, text="Beenden", command=beenden)
# label.grid(row=0, column=0)
# entry.grid(row=1, column=0)
# button_l.grid(row=3, column=0)
# button_b.grid(row=3, column=1)
# fenster.mainloop()

#Musterlösung

from tkinter import Tk, Label, Entry, Button
def loesche_text():
    entry_widget.delete(0, 'end')
def schliesse_fenster():
    fenster.destroy()
fenster = Tk()
fenster.title('Mein Tkinter Programm')


#Erstellen des Label-Widgets

label_widget = Label(fenster, text="Hallo Welt!", font=('Arial', 14))
label_widget.pack()
#Erstellen des Entry-Widgets

entry_widget = Entry(fenster)
entry_widget.pack()
#Liste von Button-Texten und zugehörigen Funktionen

buttons = [("Text löschen", loesche_text), ("Fenster schließen", schliesse_fenster)]
#Erstellen und Einfügen der Buttons basierend auf der Liste

for text, funktion in buttons:
    button = Button(fenster, text=text, command=funktion)
    button.pack(side='bottom', pady=5)
fenster.mainloop()