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
