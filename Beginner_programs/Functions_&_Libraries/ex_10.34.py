# -*- coding: utf-8 -*-
"""
   File name: ex_10.34.py
   
   *---------------------------------------------------
   
   Να γράψετε μια συνάρτηση που θα δέχεται μια λίστα με αριθμούς και θα επιστρέφει το άθροισμα των περιττών και το γινόμενο
   των άρτιων.
"""

def calc(l):
    s = 0
    g = 1
    for i in l:
        if i % 2 == 0:
            g *= i
        else:
            s += i
    return s,g


l = [1,2,3,4,5,6]
s,g = calc(l)
print("Το άθροισμα των περιττών αριθμών της λίστας είναι",s)
print("Το γινόμενο των άρτιων αριθμών της λίστας είναι",g)         