from tkinter import *


def geklickt():
    wahl = c.get()
    if wahl == 'rot':
        label.config(text="Rot",justify="center",bg='red')
        canvas.configure(background='red')
    elif wahl == 'blau':
        label.config(text="Blau",justify="center",bg='blue')
        canvas.configure(background='blue')
    elif wahl == 'grün':
        label.config(text="grün",justify="center", bg='green')
        canvas.configure(background='green')

root = Tk()
root.title("Mein GUI-Programm")

label = Label(root, text = "Wähle deine Lieblingsfarbe")
label.grid(row=0, column=1)

btn = Button(root, text="Bestätigen", command=geklickt)
btn.grid(row=1, column=1)

c = StringVar(value="None")
Radiobutton(root, text="Rot", variable=c, value='rot').grid(row=2, column=1)
Radiobutton(root, text="Grün", variable=c, value='grün').grid(row=3, column=1)
Radiobutton(root, text="Blau", variable=c, value='blau').grid(row=4, column=1)

canvas = Canvas(root, width=200, height=200, bg="white")
canvas.grid(row=5, column=1)
root.mainloop()

#Musterlösung
# from tkinter import *
#
# def farbe_anzeigen():
#     ausgewaehlte_farbe = farbwahl.get()
#     farbanzeige_label.config(text=f"Ausgewählte Farbe: {ausgewaehlte_farbe}")
#     canvas.config(bg=ausgewaehlte_farbe.lower())
#
# fenster = Tk()
# fenster.title("Farbwahl")
# farbwahl = StringVar()
# farbwahl.set("Rot")  # Standardauswahl
#
# # Widgets
# label = Label(fenster, text="Wähle deine Lieblingsfarbe:")
# label.grid(row=0, column=0, columnspan=2)
#
# rot_rb = Radiobutton(fenster, text="Rot", variable=farbwahl, value="Rot")
# rot_rb.grid(row=1, column=0)
#
# gruen_rb = Radiobutton(fenster, text="Grün", variable=farbwahl, value="Grün")
# gruen_rb.grid(row=1, column=1)
#
# blau_rb = Radiobutton(fenster, text="Blau", variable=farbwahl, value="Blau")
# blau_rb.grid(row=1, column=2)
#
# bestaetigen_button = Button(fenster, text="Bestätigen", command=farbe_anzeigen)
# bestaetigen_button.grid(row=2, column=0, columnspan=3)
#
# farbanzeige_label = Label(fenster, text="Ausgewählte Farbe: Rot")
# farbanzeige_label.grid(row=3, column=0, columnspan=3)
#
# canvas = Canvas(fenster, width=200, height=100, bg="red")
# canvas.grid(row=4, column=0, columnspan=3)
#
# fenster.mainloop()