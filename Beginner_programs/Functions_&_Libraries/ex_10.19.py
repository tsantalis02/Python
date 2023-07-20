# -*- coding: utf-8 -*-
"""
   File name: ex_10.19.py
   
   *---------------------------------------------------
   
   Να δημιουργήσετε μια λειτουργική μονάδα που θα περιέχει συναρτήσεις για τη μετατροπή ενός αριθμού στο δυαδικό, οκταδικό 
   και δεκαεξαδικό σύστημα αρίθμησης.
"""

import conversion

n = 344

print(conversion.decimalToBinary(n))
print(conversion.decimalToOctal(n))
print(conversion.decimalToHex(n))