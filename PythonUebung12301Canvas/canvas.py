from tkinter import *

def geklickt():
    label.config(text="Button wurde geklickt!",justify="center")

def farbe():
    wahl = c.get()
    if wahl == 'rot':
        label.config(bg='red')
    elif wahl == 'blau':
        label.config(bg='blue')

root = Tk()
root.title("Mein GUI-Programm")
label = Label(root, text = "Hallo Welt!")
btn = Button(root, text="Start!", command=geklickt)
c = StringVar(value="None")
Radiobutton(root, text="Hintergrund in rot Färben", variable=c, value='rot', command=farbe).pack()
Radiobutton(root, text="Hintergrund in blau Färben", variable=c, value='blau', command=farbe).pack()

canvas = Canvas(root, width=200, height=200, bg="white")
nr=canvas.create_oval(50,50,150,150,fill="blue", outline="")
canvas.create_line(0,50,100,150,fill="red", width=6)
label.pack()
btn.pack()
canvas.pack()
root.mainloop()
