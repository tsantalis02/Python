# -*- coding: utf-8 -*-
"""
   File name: ex_7.28.py
   
   *------------------------------------------
   
   Δίνονται οι συντεταγμένες δύο σημείων στο επίπεδο. Να εμφανίσετε αν αυτά τα σημεία είναι συμμετρικά, αν δηλαδή είναι 
   ίδια σημεία αλλά με αντίθετα πρόσημα.
"""

tup_01 = 2,3
tup_02 = -2,-3
count = 0
for i in range(2):
  if(tup_01[i] == -tup_02[i]):
    count += 1
if count == 2:
 print("Τα σημεία είναι συμμετρικά.")
else:
 print("Τα σημεία δεν είναι συμμετρικά.")    