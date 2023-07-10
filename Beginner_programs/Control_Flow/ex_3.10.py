# -*- coding: utf-8 -*-
"""
   File name: ex_3.10.py
   
   *-------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται τρεις αριθμούς και θα τους εμφανίζει σε φθίνουσα διάταξη(ΣΗΜΕΙΩΣΗ: να μη 
   χρησιμοποιηθεί λίστα ή κάποια άλλη δομή, αλλά μόνο απλές αριθμητικές μεταβλητές).
"""
a = int(input("Δώσε έναν αριθμό: "))
b = int(input("Δώσε έναν αριθμό: "))
c = int(input("Δώσε έναν αριθμό: "))
megaliteros = a
mesaios = a
mikroteros = a
if(b > megaliteros):
    megaliteros = b
    if(c < mikroteros):
        mikroteros = c
    else:
        mesaios = c
if(c > megaliteros):
    megaliteros = c
    if(b < mikroteros):
      mikroteros = b
    else:
      mesaios = b
print("Οι αριθμοί σε φθίνουσα διάταξη:",megaliteros,mesaios,mikroteros)        

