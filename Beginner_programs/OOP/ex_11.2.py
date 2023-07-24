# -*- coding: utf-8 -*-
"""
   File name: ex_11_2.py
   
   *----------------------------------------------
   
   Δημιουργήστε κλάση vector που θα υλοποιεί βασικές πράξεις διανυσμάτων.
"""

import numpy 

class vector():
    
    def __init__(self,l):
        
        self.vctr = numpy.array(l)
        
    def addition(self,l02):
        vctr02 = numpy.array(l02)
        vctr_add = self.vctr + vctr02
        return vctr_add
    
        
    def substraction(self,l02):
        vctr02 = numpy.array(l02)
        vctr_sub = self.vctr - vctr02
        return vctr_sub
        
        
    def multiplication(self,l02):
        vctr02 = numpy.array(l02)
        vctr_mul = self.vctr - vctr02
        return vctr_mul
    
        
        
    def division(self,l02):
        vctr02 = numpy.array(l02)
        vctr_div = self.vctr / vctr02
        return vctr_div
        
        
    def dot_product(self,l02):
        vctr02 = numpy.array(l02)
        vctr_dot_product = self.vctr.dot(vctr02)
        return vctr_dot_product
        
        
        
l01 = [10,20,30,40,50]
l02 = [1,1,1,1,1]
vctr01 = vector(l01)
v_add = vctr01.addition(l02) 
print("Πρόσθεση διανυσμάτων:",v_add)
v_sub = vctr01.substraction(l02)
print("Αφαίρεση διανυσμάτων:",v_sub)
v_mul = vctr01.multiplication(l02)
print("Πολλαπλασιασμός διανυσμάτων:",v_mul)
v_d = vctr01.division(l02)
print("Διαίρεση διανυσμάτων:",v_d)
v_dot_pr = vctr01.dot_product(l02)
print("Εσωτερικό γινόμενο διανυσμάτων:",v_dot_pr)

