# -*- coding: utf-8 -*-
"""
   File name: ex_10.3.py
   
   *---------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται τρεις αριθμούς και θα επιστρέφει τον μεγαλύτερο και τον μικρότερο από αυτούς.
"""

def num(a,b,c):
    if(a < b and b > c):
        maxi = b
    elif(a < c and c > b):
        maxi = c
    elif(a > c and a > b):
        maxi = a
    if(a > b and b < c):
        mini = b
    elif(a > c and c < b):
        mini = c
    elif(a < c and a < b):
        mini = a   
    return maxi,mini  
maximum,minimum = num(2,4,6)   
print("Max=",maximum)
print("Min=",minimum)   