# -*- coding: utf-8 -*-
"""
   File name: ex_10.23.py
   
   *---------------------------------------------
   
   Να γράψετε συνάρτηση που θα ελέγχει αν ένας αριθμός είναι άρτιος ή περιττός.
"""

def checkNum(n):
    if n % 2 == 0:
        print("Ο αριθμός",n,"είναι άρτιος.")
    else:
        print("Ο αριθμός",n,"είναι περιττός.")
        
x = int(input("Δώσε έναν ακέραιο αριθμό: "))
checkNum(x)        