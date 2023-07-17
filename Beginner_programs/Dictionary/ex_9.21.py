# -*- coding: utf-8 -*-
"""
   File name: ex_9.21.py
   
   *-------------------------------------------------------
   
   Δίνονται οι πληροφορίες φοιτητών με την μορφή: ΑΜ,Επίθετο,email. Να καταχωρηθούν σε λεξικό με κλειδί τον ΑΜ και τα 
   υπόλοιπα στοιχεία σε λίστα.
"""

l_am = list()
l = list()
foit = 'iis21125','Tsantalis','iis21125@uom.edu.gr','iis20033','Papadopoulos','iis20033@uom.edu.gr'
f = list(foit)
for i in range(len(f)):
    if(i == 0 or i % 3 == 0):
     l_am.append(f[i])
    elif(i == 1 or i - 3 == 1): 
     l.append([f[i],f[i+1]])   
d = dict(zip(l_am,l))
print(d)    