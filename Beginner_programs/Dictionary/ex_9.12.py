# -*- coding: utf-8 -*-
"""
   File name: ex_9.12.py
   
   *-----------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται έναν τριψήφιο αριθμό και θα δημιουργεί λεξικό το οποίο θα περιέχει ως κλειδιά μια 
   αρίθμηση και ως τιμές τις μονάδες, τις δεκάδες και τις εκατοντάδες του αριθμού.
"""

l = [1,2,3]
x = int(input("Δώσε τριψήφιο αριθμό: "))
ekat = x // 100
deka = (x % 100) // 10
mona = (x % 100) % 10
m = [mona,deka,ekat]
d = dict(zip(l,m))
print(d)