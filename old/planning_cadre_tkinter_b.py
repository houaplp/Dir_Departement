from tkinter import *

Fenetre = Tk()

margeH = 10
margeV = 100
larg = 1000
haut = 500

zone_dessin = Canvas(Fenetre, width=larg+2*margeH, height=haut+2*margeV, bg="white", bd=5)
zone_dessin.pack() # adapte les dimensions

#def cadre(larg, haut, margeH, margeV):
#    zone_dessin.create_line(margeH, margeV, margeH+larg, margeV, fill="black", width=1)
#    zone_dessin.create_line(margeH, margeV+18, margeH+larg, margeV+18, fill="black", width=1)
#    zone_dessin.create_line(margeH, margeV, margeH, margeV+haut, fill="black", width=1)
#    zone_dessin.create_line(margeH+larg, margeV+haut, margeH, margeV+haut, fill="black", width=1)
#    zone_dessin.create_line(margeH+larg, margeV+haut, margeH+larg, margeV, fill="black", width=1)

def ligneH (x, larg):
    zone_dessin.create_line(margeH, margeV+x, margeH+larg, margeV+x, fill="black", width=1)
    
def block_temp(x, larg):
    ligneH(0+x, larg)
    ligneH(18+x, larg)
    
def cadre(larg, haut, margeH, margeV):
    block_temp(0, larg)
    zone_dessin.create_line(margeH, margeV+18, margeH+larg, margeV+18, fill="black", width=1)
    zone_dessin.create_line(margeH, margeV, margeH, margeV+haut, fill="black", width=1)
    zone_dessin.create_line(margeH+larg, margeV+haut, margeH, margeV+haut, fill="black", width=1)
    zone_dessin.create_line(margeH+larg, margeV+haut, margeH+larg, margeV, fill="black", width=1)

cadre(larg, haut, margeH, margeV)
    

#zone_dessin.create_line(0, 500, 500, 0, fill="red", width=3)
#zone_dessin.create_line(0, 0, 500, 500, fill="red", width=3)
#zone_dessin.create_rectangle(150, 150, 350, 350)
#zone_dessin.create_oval(150, 150, 350, 350, fill="orange", width=5)

Fenetre.mainloop()
