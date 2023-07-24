# -*- coding: utf-8 -*-
"""
   File name: ex_11.15.py
   
   *------------------------------------------------
   
   Να δημιουργηθεί πρόγραμμα που θα διαχειρίζεται καταθέσεις πελατών. Θα αποθηκεύονται στοιχεία όπως: όνομα πελάτη, ποσό, 
   διάρκεια κατάθεσης, ενώ θα υπολογίζει τους τόκους και το τελικό κεφάλαιο.
"""
import random 

class Katathesi():
    
    population = 0
    epi = 0
    katatheseis = []
    
    def __init__(self,cname,amount,duration):
        
        self.cname = cname
        self.amount = amount
        self.duration = duration
        Katathesi.population += 1
        
     
    def calc(self):
        
        Katathesi.epi = random.uniform(0.01,0.2)
        self.amount = self.amount + self.amount * Katathesi.epi
        Katathesi.katatheseis.append(self.amount)
        
    def printInfo(self):
       for i in range(len(Katathesi.katatheseis)): 
        print("Όνομα πελάτη:",self.cname,end = ", ")
        print("Διάρκεια κατάθεσης:",self.duration,end = " μήνες, ")
        print("Επιτόκιο: %.2f" %Katathesi.epi,end = "%, ")
        print("Τελικό ποσό: %.2f" %Katathesi.katatheseis[i],"€.")
        


k01 = Katathesi('Tsantalis',5000,6)
k01.calc()
k02 = Katathesi('Ioannidis',6000,8)
k02.calc()
k02.printInfo()
print("Συνολικά",Katathesi.population,"καταθέσεις.")        