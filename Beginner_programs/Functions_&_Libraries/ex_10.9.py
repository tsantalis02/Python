# -*- coding: utf-8 -*-
"""
   
    File name: ex_10.9.py 

    *---------------------------------------------------

   Δημιουργήστε γεννήτρια που θα παράγει τυχαίους αριθμούς από το 1 μέχρι το 49, για ένα τυχερό παιχνίδι, φροντίζοντας να 
   μην επαναλαμβάνεται ο ίδιος αριθμός δύο φορές σε μια «κλήρωση».  
"""

import random


def gen():
   x = random.randint(1,49)
   yield x

l = list()
g = gen()
k = int(input("Δώσε πλήθος αριθμών: "))
for j in range(k):
 g = gen()
 for i in g:
    if i not in l:
        l.append(i)
print("Αριθμοί κλήρωσης:",l)        
        
