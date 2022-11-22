#!/usr/bin/env python
# coding: utf-8

# # Classes
# 

# ## 1-Enseignants

# In[34]:


import os
import math
import glob
import re
import operator
import time
import datetime
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[69]:


class Enseignant:
    def __init__(self, nom, prenom, statut):
        self.nom = nom
        self.prenom=prenom
        self.telephone="nil"
        self.mail_ujm="nil"
        self.mail_perso="nil"
        self.adresse="nil"
        self.statut=statut
        self.cours=[]
        self.charge=[]
        self.service=0

class Niveau: 
    def __init__(self, niveau):
        self.niveau = niveau
        
class Enseignement:
    def __init__(self, niveau, semestre, code, titre, groupes):
        self.niveau = niveau
        self.semestre = semestre
        self.code = code
        self.titre = titre
        self.htd = 0
        self.hcm = 0
        self.groupes = groupes
        self.cours = []
                
class Charge_admin:
    def __init__(self, titre, htd):
        self.titre = titre
        self.htd = htd
        self.rqs = "nil"
        
class Cours:
    def __init__(self, enseignant, enseignement):
        self.enseignant = enseignant
        self.enseignement = enseignement
        self.duree = 0
        self.nseances = 0
        self.groupes = 0
        self.dates = []
        self.hdebut = 0
        self.jour = "nil"
        self.type = "TD"
        self.salle = "nil"
        self.groupe = "nil"
        self.rqs = "nil"
        self.plan = "nil"
        
class Salle:
    def __init__ (self, site, code, music):
        self.site = site
        self.code = code
        self.music = music
    def __lt__ (self, other):
        return self.site < other.site
    
SallesMusic = ["HR8","J02", "J11"]   

#print ("HR8" in SallesMusic)
    


# In[70]:


os.chdir("/Users/laurentpottier/Documents/LP/Recherches/Dir_Departement/Python_Planning/files/")


# In[71]:


X = pd.read_excel("Services_enseignants2021-22s.xlsx",sheet_name=0,header=0,index_col=0)


# In[72]:


#print(X.shape) # (18, 6)
#print (X.index[3])
#print (X.columns[2])
#print (X.nom[2])
#print (X.niveau[2])
#print (X.site[2])
#print (X.salle[2])
#print (X.duree[2])
#print (type(X.rqs[2]))
#heure1 = X.début[2]
#print (heure1)
#print (heure1.hour)
#print (heure1.minute)
#print (type (heure1))
#print (type (5))
#print (type (08:00:00))
#HOUR = timedelta(hours=1)
#print (dir(HOUR))
#print (type (HOUR))
#print (dir(heure1))
#print (heure1.minute)
#print ("heure1, datetime.time :" , isinstance (heure1, datetime.time))


# In[73]:


#print (Enseignants)
#print (Enseignants[0].nom)
#print (len(Enseignants))

def noms_enseignants(ListeEnseignants):
    res = []
    for i in range (len(ListeEnseignants)):
        res.append (ListeEnseignants[i].nom)
    return res

def prenoms_enseignants(ListeEnseignants):
    res = []
    for i in range (len(ListeEnseignants)):
        res.append (ListeEnseignants[i].prenom)
    return res


# In[74]:


def add_cours_enseignant(enseignants, base, j):
    """dsflkjsldfkj"""
    nom_enseignant = base.nom[j]
    #si un enseignant est référencé dans la ligne considérée
    timej = datetime.timedelta (hours = 0, minutes = 0)
    if (not (isinstance(nom_enseignant, (int, float)))): 
        print (nom_enseignant)
        # si l'enseignant n'est pas dans la base on l'ajoute
        if nom_enseignant not in (noms_enseignants (enseignants)):
            enseignant = Enseignant(nom_enseignant, base.prenom[j], base.statut[j])   
            Enseignants.append(enseignant)

        liste_enseignants = noms_enseignants(Enseignants)
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = enseignants[nth]
        niveau = base.niveau[j]
        if (not (isinstance(niveau, (int, float)))): 
            enseignement = Enseignement(niveau, base.semestre[j], base.code[j], base.titre[j],base.groupes[j]) 
            cours = Cours(enseignant, enseignement)
            timej = base.duree[j]
            if (not (isinstance(timej, (int, float)))): 
                cours.duree = datetime.timedelta (hours = timej.hour, minutes = timej.minute)
            else : 
                cours.duree = datetime.timedelta (hours = 0, minutes = 0)
            print (cours.duree)
            if (isinstance (base.début[j], datetime.time)):
                cours.hdebut = base.début[j]
            cours.jour = base.jour[j]
            cours.groupe = base.etudts[j]
            cours.groupes = base.groupes[j]
            cours.rqs = base.rqs[j]
            cours.plan = base.plan[j]
            if(base.TD_CM[j]==1):
                cours.type = "TD" 
            elif(base.TD_CM[j]==1.5):
                cours.type = "CM" 
            else:
                cours.type = "nil"
            cours.salle = Salle(base.site[j], base.salle[j], base.salle[j] in SallesMusic)
            cours.nseances = base.nseances[j]
            #print (liste_enseignants)
            enseignant.cours.append(cours)
        else:
            timej = base.duree[j]
            print (type(timej))
            if (not (isinstance(timej, (int, float)))): 
                timej = datetime.timedelta (hours = duree.hour, minutes = duree.minute)   
            if (isinstance(timej, (int, float))): 
                timej = maketimedelta (timej)
            charge = Charge_admin(base.titre[j],timej)
            charge.rqs = base.rqs[j]
            enseignant.charge.append(charge)

    


# In[75]:


timej = 1.34
jours  = int(timej)
timek  = (timej - jours) * 24
heures = int (timek)
minutes = int((timek - heures) * 60)

print (jours, heures, minutes)

def maketimedelta (xfloat):
    jours  = int(xfloat)
    timek  = (xfloat - jours) * 24
    heures = int (timek)
    minutes = int((timek - heures) * 60)
    return datetime.timedelta (days = jours, hours = heures, minutes = minutes)

print (maketimedelta (1.34))
print (maketimedelta (0))


# In[76]:


# => X est la base issue d'Excel
# => Enseignants est la base créée à partir de X, liste d'enseignants (de la classe Enseignant)
Enseignants = []

def readlines (base, LEnseignants):
    for j in range(base.shape[0]):
        #print (j)
        add_cours_enseignant(LEnseignants, base, 1+j)
        
# add_cours_enseignant(Enseignants, X, 150)

readlines (X, Enseignants)


# In[77]:



dtm1 = datetime.timedelta (hours = 0, minutes = 20)
dtm2 = datetime.timedelta (hours = 10, minutes = 50)
dtm3 = datetime.timedelta (days = 0, hours = 0, minutes = 0)

#print (dir(dtm1 ))
print(str(dtm3.days*24 + int(dtm3.seconds /3600))+ "h"+ str(int(dtm3.seconds /60)%60))

def timeToStr (time):
    """time est un datetime.timedelta"""
    #print (time)
    days = time.days
    secondes = time.seconds
    res = ""
    if (secondes+days == 0):
        res = "0"
    else :
        res = str(days*24 + int(secondes /3600)%24)+ "h"+ str(int(secondes /60)%60)
    return res
        
print ("duree = " + timeToStr (dtm3))
print(dtm1+dtm3 )
print (dtm1*0.5)


# In[78]:


def service(LEnseignants, nom_enseignant):    
    liste_enseignants = noms_enseignants(LEnseignants)
    nth = liste_enseignants.index(nom_enseignant)
    enseignant = LEnseignants[nth]
    cours = enseignant.cours
    charge = enseignant.charge
    service = datetime.timedelta (hours = 0, minutes = 0)
    print("service de ", enseignant.prenom,  nom_enseignant, ":")
    for j in range(len(cours)):
        duree = cours[j].duree
        nseances = cours[j].nseances
        groupes = cours[j].groupes
        enseignement = cours[j].enseignement
        niveau = enseignement.niveau
        semestre = int(enseignement.semestre)
        code = enseignement.code
        if (isinstance(code, (int, float))):
            code = "Gal"            
        titre = enseignement.titre
        TD_CM = coefTDCM(cours[j].type)
        #if (isinstance (cours[j].hdebut, datetime.time)):
        if (math.isnan (groupes) or math.isnan (nseances)):
            hetd = datetime.timedelta (hours = 0, minutes = 0);
        else :
            hetd = duree * nseances * groupes * TD_CM
        #ecriture d'un cours" 
        print(niveau, "S"+str(semestre), code, titre, " : " , timeToStr(hetd), "hetd")
        service += hetd
    for j in range(len(charge)):
        hetd = charge[j].htd
        titre = charge[j].titre
        print(titre, " : " , timeToStr(hetd), "hetd")
        service += hetd
    print ("total :", timeToStr(service), "hetd")
    return service

def coefTDCM(typ):
    if(typ=="TD"):
        coef = 1
    elif(typ=="CM"):
        coef = 1.5 
    else:
        coef = 0 
    return coef
                
service(Enseignants, "Fargeton")


# In[79]:


liste_enseignants = noms_enseignants(Enseignants)
#print (liste_enseignants)
#print (liste_enseignants.index('Pottier'))
#cours1 = (Enseignants[2].cours)
#print (len(cours1))
#print ("durée :" , cours1[1].duree)

def services(LEnseignants):
    liste_enseignants = noms_enseignants(Enseignants)
    liste_enseignants_tri = sorted(noms_enseignants(Enseignants))
    # les enseignants Musique
    for i in range (len(liste_enseignants)):
        nom_enseignant = liste_enseignants_tri[i]
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = LEnseignants[nth]
        #print (enseignant.statut)
        #service(Enseignants, liste_enseignants_tri[i])
        if (not (isinstance(enseignant.statut, (int, float)))):
            if ("Musique" in enseignant.statut):
                service(Enseignants, liste_enseignants_tri[i])
   # les autres enseignants
    for i in range (len(liste_enseignants)):
        nom_enseignant = liste_enseignants_tri[i]
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = LEnseignants[nth]
        #service(Enseignants, liste_enseignants_tri[i])
        if (not (isinstance(enseignant.statut, (int, float)))):
            if (not "Musique" in enseignant.statut):
                service(Enseignants, liste_enseignants_tri[i])
        
services(Enseignants)


# In[80]:


a = "UJM-MCF-Musique"

"Musique" in a


# In[81]:


def printNiveau(enseignement):
    niveau = enseignement.niveau
    semestre = int(enseignement.semestre)
    code = enseignement.code
    titre = enseignement.titre
    ligne = ""
    if (isinstance(code, (int, float))):
        code = "Gal"  
    if (niveau == "L"):
        ligne = "Licence " + str(int((semestre+1)/2)) + " - Semestre " + str(semestre) + " - " + code + " " + titre
    elif (niveau == "M"):
        ligne = "Master " + str(int((semestre+1)/2)) + " - Semestre " + str(semestre) + " - " + code + " " + titre
    else :
        ligne = str(niveau) + " " + str(semestre) + " " + str(code) + " " + str(titre)
    return ligne
        
#enst1 =  (Enseignants[0].cours[1].enseignement)
#printNiveau (enst1)


# In[82]:



def service_det_html(LEnseignants, nom_enseignant, filout):
        liste_enseignants = noms_enseignants(LEnseignants)
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = LEnseignants[nth]
        cours = enseignant.cours
        charge = enseignant.charge
        service = datetime.timedelta (hours = 0, minutes = 0)
        hdebut = 0
        salle = ""
        filout.write("<h1> Service " + enseignant.prenom + " " + nom_enseignant + "</h1>\n")
        for j in range(len(cours)):
            duree = cours[j].duree
            nseances = cours[j].nseances
            groupes = cours[j].groupes
            if (not (isinstance(cours[j].salle.code, (int, float)))): 
                #print ("site", cours[j].salle.site)
                salle = cours[j].salle.site + "-" + cours[j].salle.code
            jour = cours[j].jour
            duree = cours[j].duree
            groupe = cours[j].groupe
            rqs = cours[j].rqs
            enseignement = cours[j].enseignement
            TD_CM = coefTDCM(cours[j].type)
            #print ("duree : ", duree)
            if (math.isnan (groupes) or math.isnan (nseances)):
                hetd = datetime.timedelta (hours = 0, minutes = 0);
            else :
                hetd = duree * nseances * groupes * TD_CM
            #----- écriture d'un cours
            filout.write("<h2>" + printNiveau(enseignement) + "</h2>\n")
            filout.write("<p>Heures (eqtd) : " + timeToStr(hetd) + " hetd</p>")
            service += hetd
            if (isinstance (cours[j].hdebut, datetime.time)):
                hdebut = cours[j].hdebut
                filout.write("<p>salle "+str(salle) + " - le "+ str(jour) + " à " + str(hdebut.hour) + 
                             "h" + str(hdebut.minute) + " - " + "durée = " + timeToStr(duree))
            if (not (isinstance (groupe, (int, float)))): 
                filout.write(" - groupes : "+ groupe )
            filout.write("</p>\n")
            if (not (isinstance(rqs, (int, float)))): 
                filout.write("<p>rqs : "+ rqs +"</p>\n")
          
        for j in range(len(charge)):
            hetd = charge[j].htd
            titre = charge[j].titre
            rqs = charge[j].rqs
            filout.write("<h2>" + titre + "</h2>\n")
            filout.write("<p>Heures (eqtd) : "  + timeToStr(hetd) + " hetd</p>\n")
            service += hetd
            if (not (isinstance(rqs, (int, float)))): 
                filout.write("<p>rqs : "+ rqs +"</p>\n")
        
        filout.write ("<h3>TOTAL : " + timeToStr(service) + " "+ " hetd" + "</h3>\n")


#with open("service_Pottier.txt", "w") as filout:
#    service_print(Enseignants, "Pottier", filout)


# In[83]:


#file to write in (html version)

def services_details_html(LEnseignants, filename):    
    with open(filename, "w") as filout:
        liste_enseignants = noms_enseignants(Enseignants)
        liste_enseignants_tri = sorted(noms_enseignants(Enseignants))
        # les enseignants Musique
        filout.write ("<!DOCTYPE html>\n")
        filout.write ("<html>\n")
        filout.write ("<head>\n")
        filout.write ("<title>Services 2021-22</title>\n")
        filout.write ("<meta charset=\"utf-8\" />\n")
        filout.write ("<link href=\"styles.css\" rel=\"stylesheet\" type=\"text/css\">\n")
        filout.write ("</head>\n")
        filout.write ("<body>\n")

        for i in range (len(liste_enseignants)):
            nom_enseignant = liste_enseignants_tri[i]
            nth = liste_enseignants.index(nom_enseignant)
            enseignant = LEnseignants[nth]
            #print (enseignant.statut)
            #service(Enseignants, liste_enseignants_tri[i])
            if (not (isinstance(enseignant.statut, (int, float)))):
                if ("Musique" in enseignant.statut):
                    service_det_html(Enseignants, liste_enseignants_tri[i], filout)
       # les autres enseignants
        for i in range (len(liste_enseignants)):
            nom_enseignant = liste_enseignants_tri[i]
            nth = liste_enseignants.index(nom_enseignant)
            enseignant = LEnseignants[nth]
            #service(Enseignants, liste_enseignants_tri[i])
            if (not (isinstance(enseignant.statut, (int, float)))):
                if (not "Musique" in enseignant.statut):
                    service_det_html(Enseignants, liste_enseignants_tri[i], filout)
            filout.write ("</body>\n")
            filout.write ("</html>")
        
                
services_details_html(Enseignants, "services_details2.html")


# In[84]:


## à faire : durée à mettre en format time


# ## 2-Planning (graphique)

# In[85]:



class Annee:
    def __init__ (self, annee, semestre1, semestre2, admin):
        self.annee = annee
        self.semestre1 = semestre1
        self.semestre2 = semestre2
        self.admin = admin
    
class Semestre:
    def __init__ (self, cours):
        self.cours = cours      
        
class Table:
    def __init__ (self):
        self.trs = []
        self.infos = ""
        
class Tr:
    def __init__ (self):
        self.tds = []
        self.salle = Salle()
        
class Td:
    def __init__ (self, cours):
        self.cours = cours
    


# In[86]:



def findSalle(code, Lsalles):
    res = 0
    for j in range (len(Lsalles)):
 if (code == Lsalles[j].code):
     res = 1
     break
    return res
    
def Lsalles(base):
    Lres = []
    salle = "nil"
    for j in range(base.shape[0]):
 site = base.site[1+j]
 code = base.salle[1+j]
 if not (isinstance(code, (int, float))):
     #print(site, code, code in SallesMusic)
     salle = Salle(site, code, code in SallesMusic)
     #print (findSalle(code , Lres))
     if not (findSalle(code , Lres))  :
         #print("kjkjkj")
         Lres.append (salle)
    return Lres

SallesDeCours = Lsalles (X) 

SallesDeCours.sort(key=operator.attrgetter('code'))
SallesDeCours.sort(key=operator.attrgetter('site'), reverse=True)
SallesDeCours.sort(key=operator.attrgetter('music'), reverse=True)

for n in range(len(SallesDeCours)):
    print (SallesDeCours[n].site + "-" +SallesDeCours[n].code) 

#print (findSalle('A230' , SallesDeCours))
#print(SallesDeCours)    


# In[87]:


# faire un tableau html graphique
# on trie d'abord les enseignements pour les mettre chacun dans un semestre
# on trie ensuite les enseignements du semestre pour les mettre chacun dans un jour de la semaine
# on trie ensuite les enseigneemnts d'un jour pour les mettre chacun dans une salle
# on prend enfin une salle et un jour et on produit le <tr> correspondant en fonction de l'heure et de la durée


# In[88]:


Enseignants[1].cours[1].hdebut


# In[89]:


cours_Simpair = []
cours_Spair = []

for i in range (len(Enseignants)):
    for j in range (len(Enseignants[i].cours)):
        if (Enseignants[i].cours[j].enseignement.semestre % 2 == 1):
            if (isinstance (Enseignants[i].cours[j].hdebut, datetime.time)):
                cours_Simpair.append(Enseignants[i].cours[j])
                #print (Enseignants[i].cours[j].hdebut)
                x = len(cours_Simpair)
                #print ("b", cours_Simpair[x-1].cours[j].hdebut)
                #print ("b", cours_Simpair[x-1].hdebut)
       # elif (Enseignants[i].cours[j].enseignement.semestre % 2 == 0):
        #    cours_Spair.append(Enseignants[i].cours[j])
            
print ("---------------")            
            
#for i in range (len(cours_Simpair)):
#    print ("S",(cours_Simpair[i].enseignement.semestre) , "-" , 
#           cours_Simpair[i].enseignant.nom , " ", (cours_Simpair[i].hdebut))


# In[90]:


#len(cours_Simpair)
cours_Simpair[1].hdebut


# In[91]:


# remplissage des journées avec les différents cours qui la composent
Semestre1= []

cours_lundi_Simpair = []
cours_mardi_Simpair = []
cours_mercredi_Simpair = []
cours_jeudi_Simpair = []
cours_vendredi_Simpair = []

for j in range (len(cours_Simpair )):
    if (cours_Simpair[j].jour == "lundi" and cours_Simpair[j].plan == "L"):
        cours_lundi_Simpair.append(cours_Simpair[j])
    elif (cours_Simpair[j].jour == "mardi" and cours_Simpair[j].plan == "L"):
        cours_mardi_Simpair.append(cours_Simpair[j])
    elif (cours_Simpair[j].jour == "mercredi" and cours_Simpair[j].plan == "L"):
        cours_mercredi_Simpair.append(cours_Simpair[j])
    elif (cours_Simpair[j].jour == "jeudi" and cours_Simpair[j].plan == "L"):
        cours_jeudi_Simpair.append(cours_Simpair[j])
    elif (cours_Simpair[j].jour == "vendredi" and cours_Simpair[j].plan == "L"):
        cours_vendredi_Simpair.append(cours_Simpair[j])
        
Semestre1.append(cours_lundi_Simpair)  
Semestre1.append(cours_mardi_Simpair)  
Semestre1.append(cours_mercredi_Simpair)  
Semestre1.append(cours_jeudi_Simpair)  
Semestre1.append(cours_vendredi_Simpair)     

for jourcours in Semestre1:
    jourcours.sort(key=operator.attrgetter('hdebut'))
    jourcours.sort(key=operator.attrgetter('salle.code'))
    jourcours.sort(key=operator.attrgetter('salle.site'),  reverse=True)
    jourcours.sort(key=operator.attrgetter('salle.music'), reverse=True)

    
print ("cours_mardi_Simpair")
for i in range (len(cours_mardi_Simpair)):
   print (str(cours_mardi_Simpair[i].salle.code) + "-" + cours_mardi_Simpair[i].enseignant.nom+ "-" + cours_mardi_Simpair[i].enseignement.titre)
#print (cours_lundi_Simpair[1].hdebut)
#semestre1 = Semestre(coursS1)


# In[92]:


def SallesJour(coursDuJour):
    codes = []
    salles = []
    for i in range (len (coursDuJour)):
        salle = coursDuJour[i].salle
        code = salle.code
        if not (isinstance(code, (int, float))):
            if (not code in codes):
                codes.append(code)
                salles.append(salle)
    return salles
            
len(SallesJour(Semestre1[0]))


# In[93]:



def printNiveauR(enseignement):
    niveau = enseignement.niveau
    semestre = int(enseignement.semestre)
    if (niveau == "L"):
        ligne = "L" + str(int((semestre+1)/2))
    elif (niveau == "M"):
        ligne = "M" + str(int((semestre+1)/2)) 
    return ligne
        
printNiveauR(Semestre1[0][1].enseignement)


# In[94]:


# créer la cellule d'un cours
print(Semestre1[0][1].jour)


# In[95]:


print(Semestre1[1])


# In[96]:


# il suffit de trier les cours d'une journée par salle puis par horaires
# puis tester les conflits horaires dans une salle !!!!!!!!!!!!
# créer les cellules vides qui précédent

def printjour(coursDuJour):
    createTR(1)
    jour = coursDuJour[1].jour
    premierjour = True
    sallesJour = SallesJour(coursDuJour)
    nsalles = len(sallesJour)
    createTDjour(jour, nsalles)
    for salle in sallesJour:
        hdebut = datetime.timedelta (hours = 8, minutes = 0)
        if not premierjour :
            createTR(1)
            premierjour = False
        code = salle.code
        createTDsalle (code)
        for i in range (len (coursDuJour)):
        #"voir quoi faire avec les salles nan"
            if (coursDuJour[i].salle.code == code):
                hdebut = createTD (hdebut, coursDuJour[i])  
        createTR(0)  

def createTR(flag):
    if flag  == 1: print("<tr>")
    else: print("</tr>")
    
def createTDjour(jour, nsalles):
    print("<td class=celljour rowspan="+str(nsalles)+">"+ jour + "</td>")
    
def createTDsalle(code):
    print("<td class=cellsalle>" + code +"</td>")
         
def createTD(heureref, cours):
    heure = cours.hdebut
    duree = cours.duree
    hdebut = datetime.timedelta(hours = heure.hour, minutes = heure.minute)  
    dureeLibre = hdebut - heureref
    ncellvides = int(dureeLibre.seconds / (15*60))
    ncellpleines = int(duree.seconds / (15*60))
    rqs = cours.rqs
    if (isinstance(rqs, (int, float))): rqs = ""
    #print ("coursdebut = " , cours.hdebut, " -  duree : " , dureeLibre,)
    if not ncellvides == 0:
        print("<td colspan=", ncellvides,  "class=cellvide>&nbsp;</td>")
    print("<td colspan=", ncellpleines, "class=cell"+printNiveauR(cours.enseignement)+">" , printNiveauR(cours.enseignement), 
          "-" , cours.enseignement.titre,
           "-" ,  cours.enseignant.nom,  rqs, "</td>")
    return hdebut + duree
            
printjour  (Semestre1[1])


# In[102]:


# il suffit de trier les cours d'une journée par salle puis par horaires
# puis tester les conflits horaires dans une salle !!!!!!!!!!!!
# créer les cellules vides qui précédent

def printhtmljour(coursDuJour, flag, filout):
    createhtmlTR(1, filout)
    jour = coursDuJour[1].jour
    premierjour = True
    sallesJour = SallesJour(coursDuJour)
    nsalles = len(sallesJour)
    createhtmlTDjour(jour, nsalles, flag, filout)
    for salle in sallesJour:
        hdebut = datetime.timedelta (hours = 8, minutes = 0)
        hfin = datetime.timedelta (hours = 19, minutes = 0)
        if not premierjour :
            createhtmlTR(1, filout)
            premierjour = False
        code = salle.code
        createhtmlTDsalle (code, filout)
        for i in range (len (coursDuJour)):
        #"voir quoi faire avec les salles nan"
            if (coursDuJour[i].salle.code == code):
                hdebut = createhtmlTD (hdebut, coursDuJour[i], filout)
                
        dureeLibre = hfin - hdebut
        ncellvides = int(dureeLibre.seconds / (15*60))
        if not ncellvides == 0:
            filout.write("<td colspan=" + str( ncellvides) + " " +  "class=cellvide>&nbsp;</td>")
   
        createhtmlTR(0, filout)  

def createhtmlTR(flag, filout):
    if flag  == 1: filout.write("<tr>\n")
    else: filout.write("</tr>\n")
    
def createhtmlTDjour(jour, nsalles, flag, filout):
    if flag == 1:
        filout.write("<td class=celljour rowspan="+str(nsalles)+">"+ jour + "</td>\n")
    else:
        filout.write("<td class=celljour2 rowspan="+str(nsalles)+">"+ jour + "</td>\n")
    
def createhtmlTDsalle(code, filout):
    filout.write("<td class=cellsalle>" + code +"</td>\n")
    
        
def createhtmlTD(heureref, cours, filout):
    heure = cours.hdebut
    duree = cours.duree
    hdebut = datetime.timedelta(hours = heure.hour, minutes = heure.minute)  
    dureeLibre = hdebut - heureref
    ncellvides = int(dureeLibre.seconds / (15*60))
    ncellpleines = int(duree.seconds / (15*60))
    rqs = cours.rqs
    if (isinstance(rqs, (int, float))): rqs = ""
    else: rqs = "-"+rqs
    #print ("coursdebut = " , cours.hdebut, " -  duree : " , dureeLibre,)
    if not ncellvides == 0:
        filout.write("<td colspan=" + str( ncellvides) + " " +  "class=cellvide>&nbsp;</td>")
    filout.write("<td colspan=" + str(ncellpleines) + " "  "class=cell"+printNiveauR(cours.enseignement)+">"+
                 printNiveauR(cours.enseignement)+"-"+cours.enseignement.titre+
                 "-"+cours.enseignant.nom+rqs+"</td>\n")
    return hdebut + duree
            


# In[103]:


def printHtmlHeures(filout):
    heure = datetime.timedelta (hours = 8)  
    heurefin = datetime.timedelta (hours = 19)  
    filout.write("<tr>\n")
    filout.write("<td colspan=2 class=cellhor>&nbsp;</td>\n") 
    while heure <= heurefin :
        filout.write("<td class=cellhorb>" + str(int(heure.seconds/3600))+"h" + str(int((heure.seconds/60)%60)) + "</td>\n")
        heure += datetime.timedelta (minutes = 15)  
        
#printHtmlHeures("lll")


# In[104]:


def planning_html(LEnseignants, filename):    
    with open(filename, "w") as filout:
        liste_enseignants = noms_enseignants(Enseignants)
        liste_enseignants_tri = sorted(noms_enseignants(Enseignants))
        # les enseignants Musique
        filout.write ("<!DOCTYPE html>\n")
        filout.write ("<html>\n")
        filout.write ("<head>\n")
        filout.write ("<title>Services 2021-22</title>\n")
        filout.write ("<meta charset=\"utf-8\" />\n")
        filout.write ("<link href=\"styleP.css\" rel=\"stylesheet\" type=\"text/css\">\n")
        filout.write ("</head>\n")
        filout.write ("<body>\n")
        filout.write ("<table border=0 cellpadding=0 cellspacing=0>\n")
        filout.write ("<tr>\n<td class=titre colspan=8>SEMESTRES impairs</td>\n")
        filout.write ("<td class=colorL1>L1</td>\n")
        filout.write ("<td class=colorL2>L2</td>\n")
        filout.write ("<td class=colorL3>L3</td>\n")
        filout.write ("<td class=colorM1>M1</td>\n")
        filout.write ("<td class=bluecell colspan=35>&nbsp;</td>\n")
        filout.write ("</tr>\n")
        flag = 1

        for jour in Semestre1:
            printHtmlHeures(filout)
            printhtmljour  (jour, flag, filout)
            flag = (flag + 1) %2 
        filout.write ("</table>\n")
        filout.write ("</body>\n")
        filout.write ("</html>\n")
        
planning_html(Enseignants, "planning_2021-22auto.html")


# In[33]:


flag = 1

for x in range (4):
    print(flag)
    flag = (flag + 1 )%2 

