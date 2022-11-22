from datetime import datetime, date, time

heure = time(8, 30)
duree = time(2, 0)
temps0 = time(8, 0)
temps1 = time(20, 0)
≤h0 = temps0.hour
minut0 = temps0.minute
h1 = temps1.hour
minut1 = temps1.minute
heur = heure.hour
minut = heure.minute
durh = duree.hour
durmin = duree.minute

LTotal = h1*60+minut1 - h0*60+minut0 # en minutes
LEvent = heur*60+minut - h0*60+minut0
Position = LEvent/LTotal
DurEvent= durh*60+durmin
DurRel = DurEvent/LTotal

print ("heure début:", temps0.hour)
print ("heure fin:", temps1.hour)
print ("duree de la journee:", LTotal/60.0)
print ("position event (h) :",LEvent/60.0)
print ("position rel (%) :",Position)
print ("dur rel (%) :",DurRel)
