# -*- coding: utf-8 -*-
"""
   File name: ex_11.5.py
   
   *----------------------------------------------------
   
   Σε ένα σχολείο υπάρχουν καθηγητές και μαθητές. Να δημιουργηθούν κλάσεις που θα διαχειρίζονται πληροφορίες κοινές και 
   ατομικές για κάθε αντικείμενο, καθώς και μέθοδοι εμφάνισης των στοιχείων αυτών.
"""

class human():
    
    population = 0
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
        human.population += 1
        
    def printInfo(self):
        print(self.name,end = ", ")
        print(self.age,"χρόνων",end = ", ")
        

class Teacher(human):

     def __init__(self,name,age,mathimata):
         
         super().__init__(name,age)
         self.mathimata = mathimata
         
     
     def printInfo(self):
         super().printInfo()
         print("Διδάσκει τα μαθήματα:",self.mathimata)
         

class Student(human):

     def __init__(self,name,age,taksi):
      
         super().__init__(name,age)
         self.taksi = taksi
         
         
     def printInfo(self):
         
         super().printInfo()
         print("Τάξη:",self.taksi)
         
         
t01 = Teacher('Tsantalis',34,['Physics','Chemistry'])
s01 = Student('Ioannidis',16,'B2')
s02 = Student('Statharakou',17,'G5')
t01.printInfo()
s01.printInfo()
s02.printInfo()
print("Συνολικά",human.population,"άνθρωποι.")         