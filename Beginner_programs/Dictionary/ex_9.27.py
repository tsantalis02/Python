# -*- coding: utf-8 -*-
"""
   File name: ex_9.27.py
   
   *----------------------------------
   
   Σε συνέχεια του ex_9.26.py να γράψετε πρόγραμμα που θα ζητάει έναν αριθμό και θα εμφανίζει τα προϊόντα με τιμή μεγαλύτερη
   από τον αριθμό αυτό.
"""

l_proion = list()
l_timi = list()
proion = input("Δώσε τον κωδικό του προϊόντος: ")
timi = eval(input("Δώσε την τιμή του προϊόντος: "))
while(timi >= 0):
    l_proion.append(proion)
    l_timi.append(timi)
    proion = input("Δώσε τον κωδικό του προϊόντος: ")
    timi = eval(input("Δώσε την τιμή του προϊόντος: "))
d = dict(zip(l_proion,l_timi))
l_meg = list()
x = eval(input("Δώσε μια τιμή: "))
for key,val in d.items():
    if val > x:
        l_meg.append(key)
print("Κωδικοί προϊόντων με μεγαλύτερη τιμή από",x,":",l_meg)        