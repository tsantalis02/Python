# -*- coding: utf-8 -*-
"""
   File name: ex_5.2.py
   
   *------------------------------------
   
   Να δημιουργήσετε μέσω σύνθεσης μια νέα λίστα με τα τετράγωνα των περιττών αριθμών μιας λίστας.
"""

x = list(range(1,7))
k = [n ** 2 for n in x  if n % 2 == 1]
print(k) 
