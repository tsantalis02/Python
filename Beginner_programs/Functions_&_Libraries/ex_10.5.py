# -*- coding: utf-8 -*-
"""
   File name: ex_10.5.py
   
   *--------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται μια λίστα αριθμών και θα επιστρέφει λίστα με τα προοδευτικά αθροίσματα των αριθμών 
   που δόθηκαν.
"""

def calc(l_01):
    l_02 = list()
    s = 0
    for i in range(len(l_01)):
      s += l_01[i]
      l_02.append(s)
    return(l_02)  


l = [1,2,3,4,5,6]
l_new = calc(l)
print(l_new)