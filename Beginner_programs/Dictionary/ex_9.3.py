# -*- coding: utf-8 -*-
"""
   File name: ex_9.3.py
   
   *-----------------------------------------------
   
   Να γράψετε πρόγραμμα που θα δημιουργεί λεξικό με κλειδιά κάποιους αριθμούς και τιμές τους μέγιστους κοινούς διαιρέτες.
   (Οι αριθμοί εισάγονται με αύξουσα διάταξη)
"""

import math

pl = int(input("Δώσε πλήθος αριθμών: "))
l = list()
for i in range(pl):
    x = int(input("Δώσε αριθμό: "))
    l.append(x)
mkd = list()
mk = 0
for i in range(pl):
    if(i+1 < pl):  
     if(i > 0 and mk >= l[i-1]):
         break
     else:
      mk = math.gcd(l[i])
      mkd.append(mk)
if(len(mkd) < pl):
       for i in range(i,pl):
           mkd.append(mk)    
d = dict(zip(l,mkd))
print("{Αριθμός: ΜΚΔ}")
print(d)
