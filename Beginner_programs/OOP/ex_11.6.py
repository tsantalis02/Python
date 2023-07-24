# -*- coding: utf-8 -*-
"""
   File name: ex_11.6.py
   
   *--------------------------------------
   
   Μια επιχείρηση απασχολεί εργαζόμενους σε διάφορα τμήματα. Να γράψετε σύστημα κλάσεων για κάθε εργαζόμενο, όπου θα 
   αποτυπώνονται τα χαρακτηριστικά τους και θα υλοποιούνται δύο βασικές λειτουργίες για την εμφάνιση των στοιχείων τους και
   την αλλαγή του μισθού τους. Η αλλαγή του μισθού θα πρέπει να γίνεται με ασφάλεια και κατάλληλους ελέγχους. Αυξήσεις 
   δίνονται σ΄ αυτούς που έχουν χρόνια υπηρεσίας από 5 μέχρι 10 έτη (10%) και σ΄΄ αυτούς με περισσότερα από 10 έτη (20%).
"""

class employee():
    
    population = 0
    
    def __init__(self,name,age,eidikotita,misthos,xronia_yphresias):
        
        self.name = name
        self.age = age
        self.eidikotita = eidikotita
        self.misthos = misthos
        self.xronia_yphresias = xronia_yphresias
        employee.population += 1
        
    
    def changeMisthos(self):
        if self.xronia_yphresias >= 5 and self.xronia_yphresias <= 10:
            self.misthos = self.misthos + (self.misthos * 10 / 100)
        elif self.xronia_yphresias > 10:
            self.misthos = self.misthos + (self.misthos * 20 / 100)
            
            
    def printInfo(self):
       print(self.name,end = ", ")
       print(self.age,"χρόνων",end = ", ")
       print(self.eidikotita,end = ", ")
       print(self.misthos,"€",end = ", ")
       print(self.xronia_yphresias,"χρόνια υπηρεσίας")


e01 = employee('Stergios',35,'Mechanic',1800,7)
e01.changeMisthos()
e02 = employee('Petros',43,'Mechanic',2200,13)
e02.changeMisthos()
e01.printInfo()
e02.printInfo()
print("Συνολικά",employee.population,"εργαζόμενοι.")        