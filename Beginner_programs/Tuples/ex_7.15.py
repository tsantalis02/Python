# -*- coding: utf-8 -*-
"""
   File name: ex_7.15.py
   
   *---------------------------------------
   
   Υπολογίστε το άθροισμα των θετικών στοιχείων μιας πλειάδας.
"""

tup = 1,5,-3,0,6,9,-7
s = 0
for i in tup:
    if i > 0 :
        s += i
print("Το άθροισμα των θετικών στοιχείων της πλειάδας είναι",s)        