# -*- coding: utf-8 -*-
"""
   File name: ex_10.48.py
   
   *-----------------------------------------------
   
   Δημιουργήστε ανώνυμη συνάρτηση για τον υπολογισμό του αθροίσματος των άρτιων αριθμών μιας λίστας.
"""

l = [1,2,-3,4,5,-6,7,8]
s = sum(filter(lambda x: x%2 == 0,l))
print("Sum of even numbers:",s)