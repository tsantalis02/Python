# -*- coding: utf-8 -*-
"""
Μονάδα κώδικα για την μετατροπή αριθμού από το δεκαδικό στο δυικό, το οκταδικό και το δεκαεξαδικό σύστημα αρίθμησης.
@author:Stergios Tsantalis
"""
def decimalToBinary(n):
    return bin(n).replace("0b","")

def decimalToOctal(n):
    return oct(n)

def decimalToHex(n):
    return hex(n)
