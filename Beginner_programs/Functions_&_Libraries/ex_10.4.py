# -*- coding: utf-8 -*-
"""
   File name: ex_10.4.py
   
   *--------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται έναν αριθμό και θα επιστρέφει τον αντίθετο και τον αντίστροφό του.
"""

def invert(n):
    if n != 0:
        antithetos = - n
        antistrofos = 1 / n
    return(antithetos,antistrofos)
a = int(input("Δώσε έναν ακέραιο αριθμό: "))
x,y = invert(a)
print("Αντίθετος:",x)
print("Αντίστροφος:",y)
