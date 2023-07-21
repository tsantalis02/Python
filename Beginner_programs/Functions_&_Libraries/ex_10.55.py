# -*- coding: utf-8 -*-
"""
   File name: ex_10.55.py
   
   *---------------------------------------------------
    
   Να γράψετε συνάρτηση που θα υπολογίζει και θα επιστρέφει τη σταθερά e με τον τύπο:
       
       e = 1 + (1 / 1!) + (1 / 2!) + (1 / 3!) + ... + (1 / n!)
"""

from math import factorial

def calcE(n):
    e = 1
    for i in range(n):
        e += 1 / factorial(i)
    return e

n = int(input("Δώσε έναν αριθμό: "))
e = calcE(n)
print("e=",e)
    