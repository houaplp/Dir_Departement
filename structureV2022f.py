#!/usr/bin/env python
# coding: utf-8

# # Classes
# 

# ## 1-Enseignants

# In[1]:


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


# In[2]:


class Enseignant:
    def __init__(self, nom, prenom, statut):
        self.nom = nom
        self.prenom=prenom
        self.telephone="nil"
        self.mail_ujm="nil"
        self.mail_perso="nil"
        self.adresse="nil"
        self.statut=statut
        self.Lcours=[]
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
        self.Lcours = []
                
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
        self.fac = "ALL"
        self.capacite = 0
    def __lt__ (self, other):
        return self.site < other.site
    
SallesMusic = ["HR8","J02", "J11"]   
#print ("HR8" in SallesMusic)
    


# In[3]:


os.chdir("/Users/laurentpottier/Documents/LP/Recherches/Dir_Departement/Python_Planning/files/")


# In[4]:


X = pd.read_excel("Services_enseignants2022-23o.xlsx",sheet_name=0,header=0,index_col=0)


# In[5]:


#print(X.shape) # (18, 6)
print (X.index[3])
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


# In[6]:


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


# In[7]:


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
    minutes = int(round ((timek - heures) * 60))
    return datetime.timedelta (days = jours, hours = heures, minutes = minutes)

print (maketimedelta (1.2))
print (maketimedelta (0))


# In[8]:



print("1-",[] == [])
print("2-", "1" == "1")
print("3-", [1, 2, 3] == [1, 2, 3])
print("4-", float("nan") == float("nan"))

coco = float("nan")
#coco = "nan"
print ("5-", coco)
print ("6-", coco == coco)
print ("7-", np.isnan (coco))
print ("8-", pd.isna(coco))


# In[9]:


def add_cours_enseignant(enseignants, base, j):
    """j est le numéro de la ligne dans la base"""
    nom_enseignant = base.nom[j]
    #si un enseignant est référencé dans la ligne considérée
    timej = datetime.timedelta (hours = 0, minutes = 0)
    #if not (isinstance(nom_enseignant, (int, float))): 
    #if not (np.isnan (nom_enseignant)):
    if nom_enseignant == nom_enseignant : 
        print (nom_enseignant)
        # si l'enseignant n'est pas dans la base on l'ajoute
        if nom_enseignant not in (noms_enseignants (enseignants)):
            enseignant = Enseignant(nom_enseignant, base.prenom[j], base.statut[j])   
            Enseignants.append(enseignant)

        liste_enseignants = noms_enseignants(Enseignants)
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = enseignants[nth]
        niveau = base.niveau[j]
        if niveau == niveau: 
            enseignement = Enseignement(niveau, base.semestre[j], base.code[j], base.titre[j],base.groupes[j]) 
            cours = Cours(enseignant, enseignement)
            timej = base.duree[j]
            hetd = base.HETD[j]
            if (isinstance(hetd, (int, float))): 
                enseignement.htd = maketimedelta(hetd / 24.)
            if timej == timej: 
                cours.duree = datetime.timedelta (hours = timej.hour, minutes = timej.minute)
            else : 
                cours.duree = datetime.timedelta (hours = 0, minutes = 0)
            #print (cours.duree)
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
            salle = base.salle[j]
            if salle != salle:
                salle = "inc2"
            site = base.site[j]
            if site != site:
                site = "inc0"
            cours.salle = Salle(site, salle, salle in SallesMusic)
            #print (cours.salle.site, cours.salle.code, cours.salle.music)
            enseignt = cours.enseignement
            #print (enseignt.niveau, enseignt.semestre, enseignt.code)
            cours.nseances = base.nseances[j]
            #print (liste_enseignants)
            enseignant.Lcours.append(cours)
        else:
            print ("+++++++++++charge : httd :++++++++++")
            hetd = base.HETD[j]
            #if (not (isinstance(hetd, (int, float)))): 
            #    hetd = datetime.timedelta (hours = hetd)   
            if (isinstance(hetd, (int, float))): 
                hetd = maketimedelta (hetd/24.)
            charge = Charge_admin(base.titre[j],hetd)
            charge.rqs = base.rqs[j]
            print (hetd)
            enseignant.charge.append(charge)


# In[10]:


enseignt = Enseignement("L1a", -2, "UE6", "coco" ,"jhejf")

enseignt.cours = []

print (enseignt.cours)


# In[11]:


# => X est la base issue d'Excel
# => Enseignants est la base créée à partir de X, liste d'enseignants (de la classe Enseignant)
Enseignants = []

def readlines (base, LEnseignants):
    for j in range(base.shape[0]):
        #print (j)
        add_cours_enseignant(LEnseignants, base, 1+j)
        
# add_cours_enseignant(Enseignants, X, 150)

readlines (X, Enseignants)


# In[12]:



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
        res = str(days*24 + int(secondes /3600)%24)+ "h"+ str(int(round(secondes /60)%60))
    return res
        
print ("duree = " + timeToStr (dtm3))
print(dtm1+dtm3 )
print (dtm1*0.5)


# In[13]:


def serviceR(LEnseignants, nom_enseignant):    
    liste_enseignants = noms_enseignants(LEnseignants)
    nth = liste_enseignants.index(nom_enseignant)
    enseignant = LEnseignants[nth]
    Lcours = enseignant.Lcours
    charge = enseignant.charge
    service = datetime.timedelta (hours = 0, minutes = 0)
    print("service de ", enseignant.prenom,  nom_enseignant, ":")
    for j in range(len(Lcours)):
        duree = Lcours[j].duree
        nseances = Lcours[j].nseances
        groupes = Lcours[j].groupes
        enseignement = Lcours[j].enseignement
        niveau = enseignement.niveau
        htd = enseignement.htd
        semestre = int(enseignement.semestre)
        code = enseignement.code
        #if (isinstance(code, (int, float))):
        if code != code:
            code = "Gal"            
        titre = enseignement.titre
        #if (isinstance (Lcours[j].hdebut, datetime.time)):
        hetd = htd
        #ecriture d'un cours" 
        print ("hetd" , hetd)
        
serviceR(Enseignants, "Cailliez")


# In[14]:


def service(LEnseignants, nom_enseignant):    
    liste_enseignants = noms_enseignants(LEnseignants)
    nth = liste_enseignants.index(nom_enseignant)
    enseignant = LEnseignants[nth]
    Lcours = enseignant.Lcours
    charge = enseignant.charge
    service = datetime.timedelta (hours = 0, minutes = 0)
    print("service de ", enseignant.prenom,  nom_enseignant, ":")
    for j in range(len(Lcours)):
        duree = Lcours[j].duree
        nseances = Lcours[j].nseances
        groupes = Lcours[j].groupes
        enseignement = Lcours[j].enseignement
        niveau = enseignement.niveau
        htd = enseignement.htd
        semestre = int(enseignement.semestre)
        code = enseignement.code
        if (isinstance(code, (int, float))):
            code = "Gal"            
        titre = enseignement.titre
        #if (isinstance (Lcours[j].hdebut, datetime.time)):
        hetd = htd
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
                
service(Enseignants, "Cailliez")


# In[15]:


liste_enseignants = noms_enseignants(Enseignants)
#print (liste_enseignants)
#print (liste_enseignants.index('Pottier'))
#Lcours1 = (Enseignants[2].Lcours)
#print (len(Lcours1))
#print ("durée :" , Lcours1[1].duree)

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
        #if (not (isinstance(enseignant.statut, (int, float)))):
        if enseignant.statut == enseignant.statut:
            if ("Musique" in enseignant.statut):
                service(Enseignants, liste_enseignants_tri[i])
   # les autres enseignants
    for i in range (len(liste_enseignants)):
        nom_enseignant = liste_enseignants_tri[i]
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = LEnseignants[nth]
        #service(Enseignants, liste_enseignants_tri[i])
        if enseignant.statut == enseignant.statut:
            if (not "Musique" in enseignant.statut):
                service(Enseignants, liste_enseignants_tri[i])
        
#services(Enseignants)


# In[50]:


a = "UJM-MCF-Musique"

"Musique" in a

x = [1, -1, 2, 0]
for i in range (len(x)):
    print (str(x[i]))


# In[17]:


def printNiveau(enseignement):
    """ pour formater le titre de l'enseignement pour les services"""
    niveau = enseignement.niveau
    semestre = int(enseignement.semestre)
    code = enseignement.code
    titre = enseignement.titre
    ligne = ""
    if code != code:
        code = "Gal"  
    if (niveau == "L1a"):
        ligne = "L1A " + " - Semestre " + str(semestre) + " - " + code + " " + titre
    elif (niveau == "L"):
        ligne = "Licence " + str(int((semestre+1)/2)) + " - Semestre " + str(semestre) + " - " + code + " " + titre
    elif (niveau == "M"):
        ligne = "Master " + str(int((semestre+1)/2)) + " - Semestre " + str(semestre) + " - " + code + " " + titre
    else :
        ligne = str(niveau) + " " + str(semestre) + " " + str(code) + " " + str(titre)
    return ligne
        
#enst1 =  (Enseignants[0].Lcours[1].enseignement)
#printNiveau (enst1)


def writehtml_date (filename, filout):
    now = datetime.datetime.today() 
    nowstr = now.strftime("%d/%m/%y - %I:%M")
    filout.write("<p> fichier " + filename + " - " + nowstr + "</p>\n")
        


# In[18]:


print ("coco "+ str(2))


# In[19]:



def service_det_html(LEnseignants, nom_enseignant, filout):
        liste_enseignants = noms_enseignants(LEnseignants)
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = LEnseignants[nth]
        Lcours = enseignant.Lcours
        charge = enseignant.charge
        service = datetime.timedelta (hours = 0, minutes = 0)
        hdebut = 0
        salle = ""
        filout.write("<h1> Service " + str(enseignant.prenom) + " " + str(nom_enseignant) + "</h1>\n")
        for j in range(len(Lcours)):
            duree = Lcours[j].duree
            nseances = Lcours[j].nseances
            groupes = Lcours[j].groupes
            #print ("code0", Lcours[j].salle.code)
            if Lcours[j].salle.code == Lcours[j].salle.code: 
                #print ("code1", Lcours[j].salle.code)
                #print ("sirte11", Lcours[j].salle.site)
                salle = Lcours[j].salle.site + "-" + Lcours[j].salle.code
            jour = Lcours[j].jour
            duree = Lcours[j].duree
            groupe = Lcours[j].groupe
            rqs = Lcours[j].rqs
            enseignement = Lcours[j].enseignement
            htd = enseignement.htd
            #----- écriture d'un cours
            filout.write("<h2>" + printNiveau(enseignement) + "</h2>\n")
            filout.write("<p>Heures (eqtd) : " + timeToStr(htd) + " hetd</p>")
            service += htd
            if (isinstance (Lcours[j].hdebut, datetime.time)):
                hdebut = Lcours[j].hdebut
                filout.write("<p>salle "+str(salle) + " - le "+ str(jour) + " à " + str(hdebut.hour) + 
                             "h" + str(hdebut.minute) + " - " + "durée = " + timeToStr(duree))
            if groupe == groupe: 
                filout.write(" - groupes : "+ groupe )
            filout.write("</p>\n")
            if rqs == rqs: 
                #print (rqs)
                filout.write("<p>rqs : "+ rqs +"</p>\n")
          
        for j in range(len(charge)):
            hetd = charge[j].htd
            titre = charge[j].titre
            rqs = charge[j].rqs
            filout.write("<h2>" + titre + "</h2>\n")
            filout.write("<p>Heures (eqtd) : "  + timeToStr(hetd) + " hetd</p>\n")
            service += hetd
            if rqs == rqs: 
                #print (rqs)
                filout.write("<p>rqs : "+ rqs +"</p>\n")
        
        filout.write ("<h3>TOTAL : " + timeToStr(service) + " "+ " hetd" + "</h3>\n")


#with open("service_Pottier.txt", "w") as filout:
#    service_print(Enseignants, "Pottier", filout)


# In[20]:


#file to write in (html version)

def services_details_html(LEnseignants, filename):    
    with open(filename, "w") as filout:
        liste_enseignants = noms_enseignants(Enseignants)
        liste_enseignants_tri = sorted(noms_enseignants(Enseignants))
        # les enseignants Musique
        filout.write ("<!DOCTYPE html>\n")
        filout.write ("<html>\n")
        filout.write ("<head>\n")
        filout.write ("<title>Services 2022-23</title>\n")
        filout.write ("<meta charset=\"utf-8\" />\n")
        filout.write ("<link href=\"styles.css\" rel=\"stylesheet\" type=\"text/css\">\n")
        filout.write ("</head>\n")
        filout.write ("<body>\n")
        writehtml_date (filename, filout)

        for i in range (len(liste_enseignants)):
            nom_enseignant = liste_enseignants_tri[i]
            nth = liste_enseignants.index(nom_enseignant)
            enseignant = LEnseignants[nth]
            #print (enseignant.statut)
            #service(Enseignants, liste_enseignants_tri[i])
            if enseignant.statut == enseignant.statut:
                if ("Musique" in enseignant.statut):
                    service_det_html(Enseignants, liste_enseignants_tri[i], filout)
       # les autres enseignants
        for i in range (len(liste_enseignants)):
            nom_enseignant = liste_enseignants_tri[i]
            nth = liste_enseignants.index(nom_enseignant)
            enseignant = LEnseignants[nth]
            #service(Enseignants, liste_enseignants_tri[i])
            if enseignant.statut == enseignant.statut:
                if (not "Musique" in enseignant.statut):
                    service_det_html(Enseignants, liste_enseignants_tri[i], filout)
        filout.write ("</body>\n")
        filout.write ("</html>")
        
                
services_details_html(Enseignants, "services_details3.html")


# ## now = datetime.datetime.today()
# nowstr = now.strftime("%d/%m/%y-%I:%M")
# print ("date :" + str(nowstr))
# print ("date :" + str(now))

# In[21]:


## à faire : durée à mettre en format time


# ## 2-Planning (graphique)

# In[22]:



class Annee:
    def __init__ (self, annee, semestre1, semestre2, admin):
        self.annee = annee
        self.semestre1 = semestre1
        self.semestre2 = semestre2
        self.admin = admin
    
class Semestre:
    def __init__ (self, semestre, Lcours):
        self.semestre = semestre     
        self.Lcours = Lcours       
        
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
    


# In[23]:



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

for n in range(len(SallesDeCours)):
    print (SallesDeCours[n].site , "-" ,SallesDeCours[n].code) 


# In[24]:



SallesDeCours.sort(key=operator.attrgetter('code'))
SallesDeCours.sort(key=operator.attrgetter('site'), reverse=True)
SallesDeCours.sort(key=operator.attrgetter('music'), reverse=True)


#print (findSalle('A230' , SallesDeCours))
#print(SallesDeCours)    


# In[25]:


# faire un tableau html graphique
# on trie d'abord les enseignements pour les mettre chacun dans un semestre
# on trie ensuite les enseignements du semestre pour les mettre chacun dans un jour de la semaine
# on trie ensuite les enseigneemnts d'un jour pour les mettre chacun dans une salle
# on prend enfin une salle et un jour et on produit le <tr> correspondant en fonction de l'heure et de la durée


# In[26]:


Enseignants[1].Lcours[1].hdebut


# In[27]:


-1 % 2


# In[28]:


Lcours_Simpair = []
Lcours_Spair = []

for i in range (len(Enseignants)):
    for j in range (len(Enseignants[i].Lcours)):
        # 
        if (Enseignants[i].Lcours[j].enseignement.semestre % 2 == 1):
            if (isinstance (Enseignants[i].Lcours[j].hdebut, datetime.time)):
                Lcours_Simpair.append(Enseignants[i].Lcours[j])
                #print (Enseignants[i].Lcours[j].hdebut)
                x = len(Lcours_Simpair)
                #print ("b", Lcours_Simpair[x-1].Lcours[j].hdebut)
                #print ("b", Lcours_Simpair[x-1].hdebut)
       # elif (Enseignants[i].Lcours[j].enseignement.semestre % 2 == 0):
        #    Lcours_Spair.append(Enseignants[i].Lcours[j])
            
#print ("---------------")     

for i in range (len(Enseignants)):
    for j in range (len(Enseignants[i].Lcours)):
        if (Enseignants[i].Lcours[j].enseignement.semestre % 2 == 0):
            if (isinstance (Enseignants[i].Lcours[j].hdebut, datetime.time)):
                Lcours_Spair.append(Enseignants[i].Lcours[j])
                #print (Enseignants[i].cours[j].hdebut)
                x = len(Lcours_Spair)
                #print ("b", Lcours_Simpair[x-1].cours[j].hdebut)
                #print ("b", Lcours_Simpair[x-1].hdebut)
       # elif (Enseignants[i].Lcours[j].enseignement.semestre % 2 == 0):
        #    Lcours_Spair.append(Enseignants[i].cours[j])
            
#print ("Simpairs---------------")     
            
#for i in range (len(Lcours_Simpair)):
#    print ("S",(Lcours_Simpair[i].enseignement.semestre) , "-" , 
#           Lcours_Simpair[i].enseignant.nom , " ", (Lcours_Simpair[i].hdebut))
    
#print ("Spairs---------------")    
            
#for i in range (len(Lcours_Spair)):
#    print ("S",(Lcours_Spair[i].enseignement.semestre) , "-" , 
#           Lcours_Spair[i].enseignant.nom , " ", (Lcours_Spair[i].hdebut))


# In[29]:


#len(cours_Simpair)
Lcours_Spair[1].hdebut


# In[30]:


coco = Lcours_Simpair[0]
coco.plan in ["L", "L1a"]


# In[31]:


# remplissage des journées avec les différents cours qui composent la licence
SemestresImpairs= []

Lcours_lundi_Simpair = []
Lcours_mardi_Simpair = []
Lcours_mercredi_Simpair = []
Lcours_jeudi_Simpair = []
Lcours_vendredi_Simpair = []

for j in range (len(Lcours_Simpair )):
    if (Lcours_Simpair[j].jour == "lundi" and Lcours_Simpair[j].plan in ["L", "L1a", "M"]):
        Lcours_lundi_Simpair.append(Lcours_Simpair[j])
    elif (Lcours_Simpair[j].jour == "mardi" and Lcours_Simpair[j].plan  in ["L", "L1a", "M"]):
        Lcours_mardi_Simpair.append(Lcours_Simpair[j])
    elif (Lcours_Simpair[j].jour == "mercredi" and Lcours_Simpair[j].plan  in ["L", "L1a", "M"]):
        Lcours_mercredi_Simpair.append(Lcours_Simpair[j])
    elif (Lcours_Simpair[j].jour == "jeudi" and Lcours_Simpair[j].plan  in ["L", "L1a", "M"]):
        Lcours_jeudi_Simpair.append(Lcours_Simpair[j])
    elif (Lcours_Simpair[j].jour == "vendredi" and Lcours_Simpair[j].plan  in ["L", "L1a", "M"]):
        Lcours_vendredi_Simpair.append(Lcours_Simpair[j])
        
SemestresImpairs.append(Lcours_lundi_Simpair)  
SemestresImpairs.append(Lcours_mardi_Simpair)  
SemestresImpairs.append(Lcours_mercredi_Simpair)  
SemestresImpairs.append(Lcours_jeudi_Simpair)  
SemestresImpairs.append(Lcours_vendredi_Simpair)     

for jourcours in SemestresImpairs:
    jourcours.sort(key=operator.attrgetter('hdebut'))
    jourcours.sort(key=operator.attrgetter('salle.code'))
    jourcours.sort(key=operator.attrgetter('salle.site'),  reverse=True)
    jourcours.sort(key=operator.attrgetter('salle.music'), reverse=True)

    
#print ("Lcours_mercredi_Simpair")
for i in range (len(Lcours_mercredi_Simpair)):
    Lcours = Lcours_mercredi_Simpair[i]
    #print (str(Lcours.salle.code) + "-" + Lcours.enseignant.nom+ "-" + Lcours.enseignement.titre)
    #print (str(Lcours.enseignement.niveau)+ "-" + str(int (Lcours.enseignement.semestre)))
#print (Lcours_lundi_Simpair[1].hdebut)
#semestre1 = Semestre(coursS1)

SemestrImpairs = Semestre("Semestres impairs", SemestresImpairs)


# In[32]:


#for jourcours in SemestresImpairs:
   # for coursx in jourcours:
        #print (coursx.salle.code)
    #print (jourcours)


# In[33]:


# remplissage des journées avec les différents cours qui la composent
SemestresPairs= []

Lcours_lundi_Spair = []
Lcours_mardi_Spair = []
Lcours_mercredi_Spair = []
Lcours_jeudi_Spair = []
Lcours_vendredi_Spair = []

for j in range (len(Lcours_Spair )):
    if (Lcours_Spair[j].jour == "lundi" and Lcours_Spair[j].plan in ["L", "L1a", "M"]):
        Lcours_lundi_Spair.append(Lcours_Spair[j])
    elif (Lcours_Spair[j].jour == "mardi" and Lcours_Spair[j].plan in ["L", "L1a", "M"]):
        Lcours_mardi_Spair.append(Lcours_Spair[j])
    elif (Lcours_Spair[j].jour == "mercredi" and Lcours_Spair[j].plan in ["L", "L1a", "M"]):
        Lcours_mercredi_Spair.append(Lcours_Spair[j])
    elif (Lcours_Spair[j].jour == "jeudi" and Lcours_Spair[j].plan in ["L", "L1a", "M"]):
        Lcours_jeudi_Spair.append(Lcours_Spair[j])
    elif (Lcours_Spair[j].jour == "vendredi" and Lcours_Spair[j].plan in ["L", "L1a", "M"]):
        Lcours_vendredi_Spair.append(Lcours_Spair[j])
        
SemestresPairs.append(Lcours_lundi_Spair)  
SemestresPairs.append(Lcours_mardi_Spair)  
SemestresPairs.append(Lcours_mercredi_Spair)  
SemestresPairs.append(Lcours_jeudi_Spair)  
SemestresPairs.append(Lcours_vendredi_Spair)     

for jourcours in SemestresPairs:
    jourcours.sort(key=operator.attrgetter('hdebut'))
    jourcours.sort(key=operator.attrgetter('salle.code'))
    jourcours.sort(key=operator.attrgetter('salle.site'),  reverse=True)
    jourcours.sort(key=operator.attrgetter('salle.music'), reverse=True)

    
print (">>> Lcours_jeudi_Spair")
for i in range (len(Lcours_jeudi_Spair)):
   print (str(Lcours_jeudi_Spair[i].salle.code) + "-" + Lcours_jeudi_Spair[i].enseignant.nom+ "-" + Lcours_jeudi_Spair[i].enseignement.titre)
#print (cours_lundi_Spair[1].hdebut)

SemestrPairs = Semestre("Semestres pairs", SemestresPairs)


# In[34]:


coco = 5
coco in [1, 2, 5]


# In[35]:


def SallesJour(LcoursDuJour):
    codes = []
    salles = []
    for i in range (len (LcoursDuJour)):
        salle = LcoursDuJour[i].salle
        code = salle.code
        if (code == code) :
            if (not code in codes):
                codes.append(code)
                salles.append(salle)
    return salles
            
len(SallesJour(SemestresImpairs[0]))

def SallesJour_annee(LcoursDuJour, semest, niveau):
    codes = []
    salles = []
    for i in range (len (LcoursDuJour)):
        salle = LcoursDuJour[i].salle
        code = salle.code
        sem = LcoursDuJour[i].enseignement.semestre
        niv = LcoursDuJour[i].enseignement.niveau
        #print ("niveau : ", niv, niveau)
        if (code == code) and (sem in semest) and (niv in niveau):
            if (not code in codes):
                    codes.append(code)
                    salles.append(salle)
    return salles
            
len(SallesJour(SemestresImpairs[0]))
len(SallesJour_annee(SemestresImpairs[0], [1, 5], ["L", "M"]))


# In[36]:


#print ("i = " , (len(SemestresImpairs)))
for i in range (len(SemestresImpairs)):
    print ("jour", 1+i, "nbre de cours  : " , (len(SemestresImpairs[i])))
    #for j in range (len(SemestresImpairs[i])):
        #print (SemestresImpairs[i][j].enseignement.titre)
        #print (SemestresImpairs[i][j].enseignement.semestre)
        #print (SemestresImpairs[i][j].enseignement.niveau)


# In[37]:


def printNiveauR(enseignement):
    niveau = enseignement.niveau
    semestre = int(enseignement.semestre)
    if (niveau == "L1a"):
        ligne = niveau + str(int((semestre+1)/2))
    elif (niveau == "L"):
        ligne = niveau + str(int((semestre+1)/2))
    elif (niveau == "M"):
        ligne = "M" + str(int((semestre+1)/2)) 
    return ligne
        
print (printNiveauR(SemestresImpairs[0][1].enseignement))
print (printNiveauR(SemestresImpairs[0][0].enseignement))
print (printNiveauR(SemestresImpairs[0][7].enseignement))


# In[38]:


# créer la cellule d'un cours
print(SemestresImpairs[0][1].jour)


# In[39]:


#print(SemestresImpairs[1])


# In[40]:


# il suffit de trier les cours d'une journée par salle puis par horaires
# puis tester les conflits horaires dans une salle !!!!!!!!!!!!
# créer les cellules vides qui précédent

def printhtmljour(LcoursDuJour, flag, filout):
    """flag = numéro du semestre (L0 => -2 et -1)"""
    jour = LcoursDuJour[1].jour
    premierjour = True
    sallesJour = SallesJour(LcoursDuJour)
    nsalles = len(sallesJour)
    createhtmlTDjour(jour, nsalles, flag, filout)
    for salle in sallesJour:
        hdebut = datetime.timedelta (hours = 8, minutes = 0)
        hfin = datetime.timedelta (hours = 19, minutes = 0)
        if not premierjour :
            createhtmlTR(1, filout)
            premierjour = False
        site = salle.site
        code = salle.code
        createhtmlTDsalle (site, code, filout)
        for i in range (len (LcoursDuJour)):
        #"voir quoi faire avec les salles nan"
            if (LcoursDuJour[i].salle.code == code):
                hdebut = createhtmlTD (hdebut, LcoursDuJour[i], filout)                
        dureeLibre = hfin - hdebut
        ncellvides = int(dureeLibre.seconds / (15*60))
        if not ncellvides == 0:
            filout.write("<td colspan=" + str( ncellvides) + " " +  "class=cellvide>&nbsp;</td>")
        createhtmlTR(0, filout)  


# In[41]:



def printhtmljour_annee(LcoursDuJour, flag, semest, niveau, filout):
    """OK pour licence et pour Master"""
    #print ("kmlkmlkmlkmlkmlkl")
    createhtmlTR(1, filout)
    jour = LcoursDuJour[1].jour
    #print (jour)
    premierjour = True
    sallesJour = SallesJour_annee(LcoursDuJour, semest, niveau)
    nsalles = len(sallesJour)
    #print ("nsalles" , nsalles )
    createhtmlTDjour(jour, nsalles, flag, filout)
    if nsalles == 0: #pas de cours ce jour là
        filout.write("<td colspan=" + str(46) + " " +  "class=cellvide>&nbsp;</td>")
        
    for salle in sallesJour:
        hdebut = datetime.timedelta (hours = 8, minutes = 0)
        hfin = datetime.timedelta (hours = 19, minutes = 0)
        if not premierjour :
            createhtmlTR(1, filout)
            premierjour = False
        site = salle.site
        code = salle.code
        createhtmlTDsalle (site, code, filout)
        for i in range (len (LcoursDuJour)):
        #"voir quoi faire avec les salles nan"
            if (LcoursDuJour[i].enseignement.semestre in semest) and (LcoursDuJour[i].enseignement.niveau in niveau) and (LcoursDuJour[i].salle.code == code):
                hdebut = createhtmlTD (hdebut, LcoursDuJour[i], filout)                
        dureeLibre = hfin - hdebut
        ncellvides = int(dureeLibre.seconds / (15*60))
        if not ncellvides == 0:
            filout.write("<td colspan=" + str( ncellvides) + " " +  "class=cellvide>&nbsp;</td>")
        createhtmlTR(0, filout)  


# In[42]:


def createhtmlTR(flag, filout):
    if flag  == 1: filout.write("<tr>\n")
    else: filout.write("</tr>\n")
    
def createhtmlTDjour(jour, nsalles, flag, filout):
    nsalles = max(nsalles, 1)
    if flag == 1:
        filout.write("<td class=celljour rowspan="+str(nsalles)+">"+ jour + "</td>\n")
    else:
        filout.write("<td class=celljour2 rowspan="+str(nsalles)+">"+ jour + "</td>\n")
    
def createhtmlTDsalle(site, code, filout):
    filout.write("<td class=cellsalle>" + site +"</td>\n")
    filout.write("<td class=cellsalle>" + code +"</td>\n")
    
        
def createhtmlTD(heureref, cours, filout):
    heure = cours.hdebut
    duree = cours.duree
    hdebut = datetime.timedelta(hours = heure.hour, minutes = heure.minute)  
    dureeLibre = hdebut - heureref
    ncellvides = int(dureeLibre.seconds / (15*60))
    ncellpleines = int(duree.seconds / (15*60))
    rqs = cours.rqs
    grp = cours.groupe
    if rqs!=rqs: rqs = ""
    else: rqs = "-"+rqs
    if grp!=grp: grp = ""
    else: grp = "-"+grp
    rqs =  rqs+grp   
    #print ("coursdebut = " , cours.hdebut, " -  duree : " , dureeLibre,)
    if not ncellvides == 0:
        filout.write("<td colspan=" + str( ncellvides) + " " +  "class=cellvide>&nbsp;</td>")
    filout.write("<td colspan=" + str(ncellpleines) + " "  "class=cell"+printNiveauR(cours.enseignement)+">"+
                 printNiveauR(cours.enseignement)+"-"+cours.enseignement.titre+
                 "-"+cours.enseignant.prenom[0]+"."+cours.enseignant.nom+rqs+"</td>\n")
    return hdebut + duree
            


# In[43]:


def printHtmlHeures(filout):
    "pour afficher le bandeau horaire"
    heure = datetime.timedelta (hours = 8)  
    heurefin = datetime.timedelta (hours = 19)  
    filout.write("<tr>\n")
    filout.write("<td colspan=3 class=cellhor>&nbsp;</td>\n")
    i = 0
    "modifications horaires"
    while heure < heurefin :
        if (i==0) :
            filout.write("<td class=cellhorb>" + str(int(heure.seconds/3600)) + "h</td>\n")
            heure += datetime.timedelta (minutes = 15)
            i = (i+1)%4
        else :
            filout.write("<td class=cellhor>" + str(int(heure.seconds/3600)) + "h" + str(int((heure.seconds/60)%60)) + "</td>\n")
            heure += datetime.timedelta (minutes = 15)
            i = (i+1)%4
        
    filout.write("</tr>\n")
        
#printHtmlHeures("lll")


# In[44]:


### tous les cours tous les niveaux
def planning_html_Sems(LEnseignants, Semestres, filename):    
    with open(filename, "w") as filout:
        filout.write ("<!DOCTYPE html>\n")
        filout.write ("<html>\n")
        filout.write ("<head>\n")
        filout.write ("<title>"+filename+"</title>\n")
        filout.write ("<meta charset=\"utf-8\" />\n")
        filout.write ("<link href=\"styleP.css\" rel=\"stylesheet\" type=\"text/css\">\n")
        filout.write ("</head>\n")
        filout.write ("<body>\n")
        filout.write ("<table border=0 cellpadding=0 cellspacing=0>\n")
        filout.write ("<tr>\n<td class=titre colspan=8>"+Semestres.semestre+"</td>\n")
        filout.write ("<td class=colorL0>L0</td>\n")
        filout.write ("<td class=colorL1a>L1a</td>\n")
        filout.write ("<td class=colorL1>L1b</td>\n")
        filout.write ("<td class=colorL2>L2</td>\n")
        filout.write ("<td class=colorL3>L3</td>\n")
        filout.write ("<td class=colorM1>M1</td>\n")
        filout.write ("<td class=bluecell colspan=33>&nbsp;</td>\n")
        filout.write ("</tr>\n")
        
        flag = 1

        for cours in Semestres.Lcours:
            printHtmlHeures(filout)
            printhtmljour  (cours, flag, filout)
            flag = (flag + 1) %2 
        filout.write ("</table>\n")
        writehtml_date (filename, filout)
        filout.write ("</body>\n")
        filout.write ("</html>\n")
        
planning_html_Sems(Enseignants, SemestrImpairs, "planningS1_2022-23auto.html")
planning_html_Sems(Enseignants, SemestrPairs, "planningS2_2022-23auto.html")


# In[45]:


### tous les cours pour un niveau donné un semestre donné
def planning_html_Sem(LEnseignants, Semestres, semest, niveau, filename):    
    with open(filename, "w") as filout:
        filout.write ("<!DOCTYPE html>\n")
        filout.write ("<html>\n")
        filout.write ("<head>\n")
        filout.write ("<title>"+filename+"</title>\n")
        filout.write ("<meta charset=\"utf-8\" />\n")
        filout.write ("<link href=\"styleP.css\" rel=\"stylesheet\" type=\"text/css\">\n")
        filout.write ("</head>\n")
        filout.write ("<body>\n")
        filout.write ("<table border=0 cellpadding=0 cellspacing=0>\n")
        filout.write ("<tr>\n<td class=titre colspan=8>"+Semestres.semestre+"</td>\n")
        filout.write ("<td class=colorL0>L0</td>\n")
        filout.write ("<td class=colorL1a>L1a</td>\n")
        filout.write ("<td class=colorL1>L1b</td>\n")
        filout.write ("<td class=colorL2>L2</td>\n")
        filout.write ("<td class=colorL3>L3</td>\n")
        filout.write ("<td class=colorM1>M1</td>\n")
        filout.write ("<td class=bluecell colspan=35>&nbsp;</td>\n")
        filout.write ("</tr>\n")
        flag = 1

        for cours in Semestres.Lcours:
            #print (len(cours))
            printHtmlHeures(filout)
            printhtmljour_annee  (cours, flag, semest, niveau, filout)
            flag = (flag + 1) %2 
        filout.write ("</table>\n")
        writehtml_date (filename, filout)
        filout.write ("</body>\n")
        filout.write ("</html>\n")
        


# In[47]:


jeudi = (SemestrPairs.Lcours[3])
for i in range(len(jeudi)):
    cours = jeudi [i]
    print (cours.enseignant.nom, cours.enseignement.titre, cours.enseignement.niveau)


# In[48]:


planning_html_Sem(Enseignants, SemestrImpairs, [-1, 1], ["L1a"], "planningS1L0_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrImpairs, [1], ["L1a", "L"], "planningS1L1_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrImpairs, [3], ["L"], "planningS1L2_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrImpairs, [5], ["L"], "planningS1L3_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrPairs, [0, 2], ["L1a"], "planningS2L0_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrPairs, [2], ["L1a", "L"], "planningS2L1_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrPairs, [4], ["L"], "planningS2L2_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrPairs, [6], ["L"], "planningS2L3_2022-23auto.html")

planning_html_Sem(Enseignants, SemestrImpairs, [1], ["M"],  "planningS1M1_2022-23auto.html")
planning_html_Sem(Enseignants, SemestrPairs, [2], ["M"], "planningS2M1_2022-23auto.html")


# In[49]:


flag = 1

for x in range (4):
    print(flag)
    flag = (flag + 1 )%2 

