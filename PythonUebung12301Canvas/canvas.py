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

# Musterlösung
# from tkinter import *
#
# def aendere_label_text():
#     label.config(text="Button wurde geklickt!")
#
# def aendere_label_farbe(farbe):
#     label.config(bg=farbe)
#
# def zeichne_canvas():
#     canvas.create_line(10, 10, 200, 50)
#     canvas.create_oval(50, 50, 150, 100, fill="yellow")
#
# fenster = Tk()
# fenster.title("Mein GUI-Programm")
#
# label = Label(fenster, text="Hallo Welt!")
# label.pack()
#
# button = Button(fenster, text="Klick mich", command=aendere_label_text)
# button.pack()
#
# radiobutton_var = StringVar()
# radiobutton_var.set("rot")  # Setzt die Standardfarbe auf Rot
#
# radiobutton_rot = Radiobutton(fenster, text="Rot", variable=radiobutton_var, value="red", command=lambda: aendere_label_farbe("red"))
# radiobutton_rot.pack()
#
# radiobutton_blau = Radiobutton(fenster, text="Blau", variable=radiobutton_var, value="blue", command=lambda: aendere_label_farbe("blue"))
# radiobutton_blau.pack()
#
# canvas = Canvas(fenster, width=200, height=150)
# canvas.pack()
# zeichne_canvas()
#
# fenster.mainloop()
