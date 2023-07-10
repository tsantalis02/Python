# -*- coding: utf-8 -*-
"""
   File name: ex_3.11.py
   
   *---------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται τρεις αριθμούς, εμφανίζοντας τον μεγαλύτερο και τον μικρότερο, χωρίς τη χρήση 
   έτοιμων συναρτήσεων της Python.
"""

a = int(input("Δώσε έναν αριθμό: "))
b = int(input("Δώσε έναν αριθμό: "))
c = int(input("Δώσε έναν αριθμό: "))
megaliteros = a
mikroteros = a
if(b > megaliteros and b > c):
    megaliteros = b
elif(b > megaliteros and b < c):
    megaliteros = c
elif(b < megaliteros and b > c):
    megaliteros = a 
else:
    if(c > megaliteros):
      megaliteros = c
if(b < mikroteros and b < c):
  mikroteros = b
elif(b < mikroteros and b > c):
  mikroteros = c
elif(b > mikroteros and b < c):
  mikroteros = a
else:
  if(c < mikroteros):
      mikroteros = c
print("Ο μεγαλύτερος είναι:",megaliteros)
print("Ο μικρότερος είναι:",mikroteros)      
       