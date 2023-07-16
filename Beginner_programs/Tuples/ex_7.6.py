# -*- coding: utf-8 -*-
"""
   File name: ex_7.6.py
   
   *-------------------------------------
   
   Ελέγξτε αν μια πλειάδα με αριθμούς είναι παλινδρομική.
"""

tup = (121,122,123)
pal = 0
for i in range(len(tup)):
 n = tup[i]
 temp = n
 rev = 0
 while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
 if(temp==rev):
    pal += 1
if (pal == len(tup)):
    print("Η πλειάδα είναι παλινδρομική.") 
else:
    print("Η πλειάδα δεν είναι παλινδρομική.")