# -*- coding: utf-8 -*-
"""
   File name: ex_9.10.py
   
   *-------------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται μια φράση (κείμενο) και θα δημιουργεί λεξικό με κλειδιά μια αρίθμηση και τιμές όλες 
   τις πιθανές αναδιατάξεις της φράσης. Για παράδειγμα, για τη φράση 'πχ' να γίνει το λεξικό {1: 'πχ', 2: 'χπ'}.
"""

l = list()
c = 1
phr_list = list()
phr = input("Γράψε μια φράση: ")
l.append(c)
phr_list.append(phr)
c += 1
phr_new = phr[1:] + phr[0]
while phr_new != phr:
    l.append(c)
    phr_list.append(phr_new)
    c += 1
    phr_new = phr_new[1:] + phr_new[0]
d = dict(zip(l,phr_list))
print(d)    
        