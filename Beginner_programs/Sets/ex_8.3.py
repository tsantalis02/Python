# -*- coding: utf-8 -*-
"""
   File name: ex_8.3.py
   
   *----------------------------------
   
   Να γράψετε πρόγραμμα που θα δημιουργεί σύνολο με δέκα μοναδικά στοιχεία. Μπορούν να τυπωθούν με αντίστροφη σειρά;(Ναι μπορούν)
"""

s = set()
while len(s) != 10:
  x = eval(input("Δώσε στοιχείο: "))
  if x not in s:
      s.add(x)
print(s)  
# Εκτύπωση με αντίστροφη σειρά
print(sorted(s,reverse=True))    