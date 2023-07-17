# -*- coding: utf-8 -*-
"""
   File name: ex_9.20.py
   
   *-------------------------------------
   
   Δύο λεξικά έχουν ακριβώς τα ίδια κλειδιά και οι τιμές τους είναι αριθμοί. Να δημιουργηθεί νέο λεξικό που θα περιέχει τα 
   ίδια κλειδιά, αλλά οι τιμές του θα είναι το άθροισμα των αντίστοιχων τιμών των δύο πρώτων λεξικών.
"""

d_01 = {'a': 1, 'b': 2, 'c': 3}
d_02 = {'a': 4, 'b': 5, 'c': 6}
l_01 = list()
l_02 = list()
for key,val in d_01.items():
    l_01.append(key)
    l_02.append(d_01[key] + d_02[key])
d = dict(zip(l_01,l_02))
print(d)    