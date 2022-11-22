from tkinter import *
from datetime import datetime, date, time

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
    #zone_dessin.create_text (margeH+x, margeV+y, angle=orientation, text=text, anchor='nw', font=('TkMenuFont', size))
    zone_dessin.create_text (margeH+x, margeV+y, angle=orientation, text=text, anchor='nw', font=('Calibri', size))

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


img = PhotoImage(file = logofile, master = Fenetre)
logo1 = zone_dessin.create_image(80, 60, image = img)

trace_grille()

#************************** TEXTE *******************
spe = "L1 musicologie"
semestre = "1-2"
date = "Juin 2021"

def place_specialite(spe):
    place_txt (larg*0.5, -50, "SPECIALITE :", 21, 0)
    place_txt (larg*0.5 + 130, -50, spe, 21, 0)

place_specialite (spe)

def place_semestre(spe):
    place_txt (larg*0.8, -50, "SEMESTRE :", 21, 0)
    place_txt (larg*0.8 + 130, -50, semestre, 21, 0)

place_semestre (spe)

def place_date(date):
    place_txt (larg*0.8, haut+10, date, 21, 0)

place_date (date)

#****************** PLACER UN COURS ***************************
#EXEMPLE
intitule = "Solfège"
groupe = "gr.1"
enseignant = "V. Petiet"
salle = "J1.1"
autre = "sem impaires"
jour = "LUNDI"
heure = time(8, 30)
duree = time(2, 0)
semestre = 1

heure = time(8, 30)
duree = time(2, 0)
temps0 = time(8, 0)
temps1 = time(20, 0)
h0 = temps0.hour
minut0 = temps0.minute
h1 = temps1.hour
minut1 = temps1.minute

LTotal = h1*60+minut1 - h0*60+minut0 # en minutes

#print ("heure début:", temps0.hour)
#print ("heure fin:", temps1.hour)
#print ("duree de la journee:", LTotal/60.0)
#print ("position event (h) :",LEvent/60.0)
#print ("position rel (%) :",Position)
#print ("dur rel (%) :",DurRel)

def place_cours (intitule, groupe, enseignant, salle, autre, jour, heure, duree, semestre):
    heur = heure.hour
    minut = heure.minute
    durh = duree.hour
    durmin = duree.minute
    LEvent = heur*60+minut - h0*60+minut0
    Position = LEvent/LTotal
    DurEvent= durh*60+durmin
    DurRel = DurEvent/LTotal
    nthjour = jours.index(jour)
    x = larg * Position
    y = nthjour*(cell_haut)
    l = larg * DurRel
    zone_dessin.create_rectangle(x, y, x+l, x+cell_dim / 2)
    
        
place_cours(intitule, groupe, enseignant, salle, autre, jour, heure, duree, semestre)


#****************** ENREGISTRER EPS ***************************

def print_cnv():
    zone_dessin.postscript(file="grille2b.eps", colormode='color')

zone_dessin.after(1000, print_cnv)


#*********************************************


#zone_dessin.after(5000, print_cnv)

#place_specialite("L1 musicologie")
#place_semestre("1-2")
#place_date("Juin 2021")
#printPDF(zone_dessin)

Fenetre.mainloop()
