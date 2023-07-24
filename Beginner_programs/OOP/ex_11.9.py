# -*- coding: utf-8 -*-
"""
   File name: ex_11.9.py
   
   *-------------------------------------------------------
   
   Να δημιουργηθεί κλάση για την αναπαράσταση ενός ακέραιου αριθμού ως δυαδικού.
"""

class DecimalToBinary():
    
    def __init__(self,x):
        
        self.x = x
        
    def decimalToBinary(self):
        print(bin(self.x).replace("0b",""))
        
        
num = DecimalToBinary(5)
num.decimalToBinary()        