# -*- coding: utf-8 -*-
"""
   File name: ex_9.1.py
   
   *--------------------------------------
   
   Να γράψετε πρόγραμμα που θα δημιουργεί λεξικό με κλειδιά του τους αριθμούς από το 10 έως το 100, και τιμές τα τετράγωνα 
   των κλειδιών.
"""

l_01 = list()
l_02 = list()
for i in range(10,101):
    l_01.append(i)
    l_02.append(i * i)
d = dict(zip(l_01,l_02))
print(d)    