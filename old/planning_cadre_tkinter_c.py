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
logofile = "files/logoALL.png"

#création d'une zone de dessin
zone_dessin = Canvas(Fenetre, width=larg+2*margeH, height=haut+margeV+margeV2, bg="white", bd=5)
zone_dessin.pack() # adapte les dimensions

#graphismes
def ligneH (y, larg):
    zone_dessin.create_line(margeH, margeV+y, margeH+larg, margeV+y, fill="black", width=1)
    
def ligneV (x, y, haut):
    zone_dessin.create_line(margeH+x, margeV+y, margeH+x, margeV+y+haut, fill="black", width=1)

def place_txt(x, y, text, size, orientation):
    zone_dessin.create_text (margeH+x, margeV+y, angle=orientation, text=text, anchor='nw', font=('TkMenuFont', size))

def trace_grille ():
    font_size = 10
    ligneV (0, 0, haut)
    ligneV (cell_dim, 0, haut)
    ligneV (larg, 0, haut)
    
    ligneH (0, larg)
    ligneH (cell_dim, larg)
    for j in range (len(heures)):
        ligneV (cell_dim + (j*(cell_larg)), 0, cell_dim)
        place_txt (2+cell_dim + (j*(cell_larg)) ,2, heures[j], font_size, 0)

    for i in range (len(jours)):
        ligneH (((1+i)*(cell_haut)), larg)
        ligneH (((1+i)*(cell_haut))+cell_dim, larg)
        place_txt (1, -5+((1+i)*(cell_haut)), jours[i], font_size, 90)
        
        for j in range (len(heures)):
            ligneV (cell_dim + (j*(cell_larg)), (1+i)*(cell_haut), cell_dim)
            place_txt (2+cell_dim + (j*(cell_larg)),2+ (i+1)*(cell_haut), heures[j], font_size, 0)

def place_logo(logofile):
    img = PhotoImage(file = logofile, master = Fenetre)
    logo1 = zone_dessin.create_image(80, 60, image = img)

#def print_cnv():
#    zone_dessin.postscript(file="grille.eps", colormode='color')



#def place_specialite("L1 musicologie")
#def place_semestre("1-2")
#def place_date("Juin 2021")

#def printPDF(canvas)

#****** MAIN *******
trace_grille()
place_logo(logofile)

#zone_dessin.after(5000, print_cnv)

#place_specialite("L1 musicologie")
#place_semestre("1-2")
#place_date("Juin 2021")
#printPDF(zone_dessin)

Fenetre.mainloop()
