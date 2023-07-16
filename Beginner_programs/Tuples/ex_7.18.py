# -*- coding: utf-8 -*-
"""
   File name: ex_7.18.py
   
   *---------------------------------------
   
   Να γράψετε πρόγραμμα που θα δημιουργεί πλειάδα με την ακολουθία αριθμών Fibonacci για δοσμένο ακέραιο αριθμό.
"""

listFib = list()
tupFib = tuple()
nth_term = int(input("Δώσε αριθμό για πλήθος όρων στην ακολουθία Fibonacci: "))
n1, n2 = 0, 1
listFib.append(n1) 
listFib.append(n2) 
for i in range(2,nth_term):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    listFib.append(n3)
tupFib = tuple(listFib)
print("Ακολουθία Fibonacci",nth_term,"όρων:")
print(tupFib)    