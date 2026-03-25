from tkinter import *

def geklickt():
    button.destroy()
    new_button=Button(master=fenster, text="Button wurde geklickt!")
    new_button.pack()
    label.config(text="Button wurde geklickt!", font=('Arial', 14), bg="yellow", fg="blue",justify="center")

fenster=Tk()
fenster.title("Mein GUI")
fenster.resizable(False, False)
label=Label(master=fenster, font=('Arial', 16),bg="yellow", fg="blue",justify="center",  text="Willkommen zu deinem GUI")
button = Button(master=fenster,text="Klick mich!", command=geklickt)
label.pack(pady=20)
button.pack(pady=10)
fenster.mainloop()

# Musterloesung
# from tkinter import Tk, Label, Button
#
#
# def button_klick():
#     # Ändere den Text des Labels
#
#     label.config(text='Button wurde geklickt!')
#
#
# # Initialisierung des Hauptfensters
#
# fenster = Tk()
# fenster.title('Mein erstes GUI')
#
#
# # Verhindere das Ändern der Fenstergröße
#
# fenster.resizable(False, False)
#
#
# # Erstellung und Konfiguration des Labels
#
# label = Label(fenster, text='Willkommen zu deinem ersten GUI!', font=('Arial', 16), fg='blue', bg='yellow')
# label.pack(pady=20)  # Vertikaler Abstand zum Fensterrand
#
#
# # Erstellung und Konfiguration der Schaltfläche
#
# button = Button(fenster, text='Klick mich!', command=button_klick)
# button.pack(pady=10)  # Vertikaler Abstand zum Label
#
#
# # Endlosschleife zur Anzeige des Fensters
#
# fenster.mainloop()