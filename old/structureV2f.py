#!/usr/bin/env python
# coding: utf-8

# # Classes
# 

# ## Enseignant

# In[1]:


import os
import math
import glob
import re
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
                
class Charge_admin:
    def __init__(self, titre, htd):
        self.titre = titre
        self.htd = htd
        
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


# In[3]:


os.chdir("/Users/laurentpottier/Documents/LP/Recherches/Dir_Departement/Python_Planning/files/")


# In[9]:


X = pd.read_excel("Services_enseignants2021-22p.xlsx",sheet_name=0,header=0,index_col=0)


# In[10]:


print(X.shape) # (18, 6)
print (X.index[3])
print (X.columns[2])
print (X.nom[2])
print (X.niveau[2])


# In[11]:


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


# In[12]:


def add_cours_enseignant(enseignants, base, j):
    """dsflkjsldfkj"""
    nom_enseignant = base.nom[j]
    #si un enseignant est référencé dans la ligne considérée
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
            cours.duree = base.duree[j]
            cours.jour = base.jour[j]
            cours.groupes = base.groupes[j]
            if(base.TD_CM[j]==1):
                cours.type = "TD" 
            elif(base.TD_CM[j]==1.5):
                cours.type = "CM" 
            else:
                cours.type = "nil"
            cours.salle = base.salle[j]
            cours.nseances = base.nseances[j]
            #print (liste_enseignants)
            enseignant.cours.append(cours)
        else:
            charge = Charge_admin(base.titre[j],base.duree[j])
            enseignant.charge.append(charge)

    
#add_cours_enseignant(Enseignants, X, 144)


# In[13]:


# => X est la base issue d'Excel
# => Enseignants est la base créée à partir de X, liste d'enseignants (de la classe Enseignant)
Enseignants = []

def readlines (base, LEnseignants):
    for j in range(base.shape[0]):
        #print (j)
        add_cours_enseignant(LEnseignants, base, 1+j)
        
readlines (X, Enseignants)


# In[55]:


def service(LEnseignants, nom_enseignant):    
    liste_enseignants = noms_enseignants(LEnseignants)
    nth = liste_enseignants.index(nom_enseignant)
    enseignant = LEnseignants[nth]
    cours = enseignant.cours
    charge = enseignant.charge
    service = 0
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
        hetd = duree * nseances * groupes * TD_CM
        print(niveau, "S"+str(semestre), code, titre, " : " ,hetd, "hetd")
        service += hetd
    for j in range(len(charge)):
        hetd = charge[j].htd
        titre = charge[j].titre
        print(titre, " : " ,hetd, "hetd")
        service += hetd
    print ("total :", service, "hetd")
    return service

def coefTDCM(typ):
    if(typ=="TD"):
        coef = 1
    elif(typ=="CM"):
        coef = 1.5 
    else:
        coef = 0 
    return coef
                
service(Enseignants, "Damon-Guillot")


# In[13]:


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


# In[ ]:


#file to write in

def services_detaille(LEnseignants):
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


# In[15]:


a = "UJM-MCF-Musique"

"Musique" in a


# In[58]:


def service_print(LEnseignants, nom_enseignant, filout):
        liste_enseignants = noms_enseignants(LEnseignants)
        nth = liste_enseignants.index(nom_enseignant)
        enseignant = LEnseignants[nth]
        cours = enseignant.cours
        charge = enseignant.charge
        service = 0
        filout.write("service de " + enseignant.prenom + " " + nom_enseignant + " :" + "\n")
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
            hetd = duree * nseances * groupes * TD_CM
            filout.write(niveau + " "+ "S"+str(semestre) + " "+ code + " "+ titre + " : "  + str(hetd) + " "+ "hetd" + "\n")
            #filout.write(niveau + " "+ "S"+str(semestre) +  " "+ titre + " : "  + str(hetd) + " "+ "hetd" + "\n")
            service += hetd
        for j in range(len(charge)):
            hetd = charge[j].htd
            titre = charge[j].titre
            filout.write(titre + " : "  + hetd + "hetd")
            service += hetd
        filout.write ("total : " + str(service) + " "+ "hetd" + "\n" + "\n")

def coefTDCM(typ):
    if(typ=="TD"):
        coef = 1
    elif(typ=="CM"):
        coef = 1.5 
    else:
        coef = 0 
    return coef
                

with open("service_Pottier.txt", "w") as filout:
    service_print(Enseignants, "Pottier", filout)


# In[39]:


with open("coco", "w") as filout:
    s = "service de " +  "lp" +  "\n" + "nom_enseignant" + ": " + str(5.2)
    filout.write(s)


# In[59]:


def services_print (LEnseignants, filename):
    with open(filename, "w") as filout:
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
                    service_print(Enseignants, liste_enseignants_tri[i], filout)
       # les autres enseignants
        for i in range (len(liste_enseignants)):
            nom_enseignant = liste_enseignants_tri[i]
            nth = liste_enseignants.index(nom_enseignant)
            enseignant = LEnseignants[nth]
            #service(Enseignants, liste_enseignants_tri[i])
            if (not (isinstance(enseignant.statut, (int, float)))):
                if (not "Musique" in enseignant.statut):
                    service_print(Enseignants, liste_enseignants_tri[i], filout)
                
services_print(Enseignants, "services.txt")


# ## Planning (graphique)

# In[ ]:




