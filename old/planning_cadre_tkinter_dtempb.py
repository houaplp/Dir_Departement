from tkinter import *

Fenetre = Tk()
#Variables
margeH = 10
margeV = 120
margeV2 = 50
larg = 1000
haut = 500
cell_dim = 18
jours = ["LUNDI", "MARDI", "MERCREDI", "JEUDI", "VENDREDI", "SAMEDI"]
heures = ["8:0", "8:30", "9:0", "9:30", "10:0", "10:30", "11:0", "11:30", "12:0", "12:30", "13:0", "13:30", "14:0", "14:30", "15:0", "15:30", "16:0", "16:30", "17:0", "17:30", "18:0", "18:30", "19:0", "19:30"]
cell_larg = (larg - cell_dim) / len(heures)
cell_haut = (haut - cell_dim) / len(jours)
#logofile = "files/logoALL.png"
logofile = "logoALL2.png"

#création d'une zone de dessin
zone_dessin = Canvas(Fenetre, width=larg+2*margeH, height=haut+margeV+margeV2, bg="white", bd=5)
zone_dessin.pack() # adapte les dimensions

img = PhotoImage(file = logofile, master = Fenetre)
logo1 = zone_dessin.create_image(80, 60, image = img)

Fenetre.mainloop()
