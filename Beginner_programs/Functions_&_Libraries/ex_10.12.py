# -*- coding: utf-8 -*-
"""
   File name: ex_10.12.py
   
   *----------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται μια συμβολοσειρά και θα επιστρέφει λεξικό με κλειδιά τους χαρακτήρες του κειμένου και
   τιμές το πλήθος εμφάνισης κάθε χαρακτήρα.
"""

def create_dict(s):
    l_ch = list()
    ch_freq = list()
    for i in s:
     l_ch.append(i)
     ch_freq.append(s.count(i))
     d = dict(zip(l_ch,ch_freq))
    return(d)
 
x = input("Δώσε μια συμβολοσειρά: ")
k = create_dict(x)
print(k)    