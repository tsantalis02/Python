# -*- coding: utf-8 -*-
"""
   File name: ex_10.25.py
   
   *-----------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται δύο αριθμούς x και y και θα ελέγχει αν η διαίρεσή τους είναι τέλεια.
"""

def checkDivide(x,y):
    if x % y == 0:
        print("Η διαίρεση των αριθμών",x,"και",y,"είναι τέλεια.")
    else:
        print("Η διαίρεση των αριθμών",x,"και",y,"δεν είναι τέλεια.")
        

n = int(input("Δώσε έναν ακέραιο αριθμό(διαιρετέος): "))
k = int(input("Δώσε έναν ακέραιο αριθμό(διαιρέτης): "))
checkDivide(n,k)        