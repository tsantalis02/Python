# -*- coding: utf-8 -*-
"""
   File name: ex_10.50.py
   
   *------------------------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται έναν αριθμό x και θα εμφανίζει τις x πρώτες γραμμές ενός τριγώνου Pascal.
"""

from math import factorial
 

def pascalTriangle(n):
 for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()
    
    
x = int(input("Δώσε αριθμό για την εμφάνιση τόσων γραμών το τριγώνου Pascal: ")) 
pascalTriangle(x)   