# -*- coding: utf-8 -*-
"""
   File name: ex_7.1.py
   
   *----------------------------------------
   
   Φτιάξτε λίστα με όλες τις κενές πλειάδες μιας άλλης λίστας.
"""

l = [(1,2),3,(4,5)]
new_l = list()

for i in range(len(l)):
    if( (type(l[i]) is tuple) and any(l[i]) == True):
        new_l.append(l[i])
print(new_l)        
