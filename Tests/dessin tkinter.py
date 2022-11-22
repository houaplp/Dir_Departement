from tkinter import *

Fenetre = Tk()

zone_dessin = Canvas(Fenetre, width=500, height=500, bg="white", bd=5)
zone_dessin.pack() # adapte les dimensions

zone_dessin.create_line(0, 500, 500, 0, fill="red", width=3)
zone_dessin.create_line(0, 0, 500, 500, fill="red", width=3)
zone_dessin.create_rectangle(150, 150, 350, 350)
zone_dessin.create_oval(150, 150, 350, 350, fill="orange", width=5)

Fenetre.mainloop()
