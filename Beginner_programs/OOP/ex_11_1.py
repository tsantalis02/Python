# -*- coding: utf-8 -*-
"""
   File name: ex_11_1.py
   
   *--------------------------------------------------------------
   
   Δημιουργήστε μια βασική κλάση για τον ορισμό των στοιχείων ενός σχήματος και δύο υποκλάσεις για έναν κύκλο και ένα 
   ορθογώνιο. Υλοποιήστε κατάλληλες μεθόδους για τον υπολογισμό του εμβαδού των δύο σχημάτων.
"""

class Sxima():
    
    population = 0
    
    def __init__(self):
        Sxima.population += 1



class Kyklos(Sxima):

    pi = 3.14159
    
    def __init__(self,aktina):
    
       super().__init__()
       self.aktina = aktina
       
    def emvado(self):
      emv = Kyklos.pi * (self.aktina ** 2)
      print("Το εμβαδόν του κύκλου ισούται με",emv)

class Orthogonio(Sxima):
    
    def __init__(self,pleyra_a,pleyra_b):
        
        super().__init__()
        self.pleyra_a = pleyra_a
        self.pleyra_b = pleyra_b
        
    def emvado(self):
        emv = self.pleyra_a * self.pleyra_b
        print("Το εμβαδόν του ορθογωνίου ισούται με",emv)
        
        
sxima01 = Kyklos(3)
print(sxima01.emvado())
sxima02 = Orthogonio(3,5)
print(sxima02.emvado())
print(Sxima.population,"σχήματα")        
           