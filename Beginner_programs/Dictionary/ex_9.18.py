# -*- coding: utf-8 -*-
"""
   File name: ex_9.18.py
   
   *-----------------------------------
   
   Να γράψετε πρόγραμμα που θα ελέγχει αν ένα λεξικό έχει τιμές None.
"""

d = {'a': 1, 'b': 2, 'c': None}
res = False
for _,val in d.items():
    if val is None:
        res = True
if res == True:
    print("Το λεξικό περιέχει None τιμές.")
else:
    print("Το λεξικό δεν περιέχει None τιμές.")