# -*- coding: utf-8 -*-
"""
   File name: ex_11.7.py
   
   *---------------------------------------------------
   
   Μια βιβλιοθήκη διαθέτει βιβλία και περιοδικά. Να δημιουργήσετε κατάλληλες κλάσεις για αυτά.
"""


class library():
    
    books = []
    magazines = []
    
    def __init__(self,title):
        
        self.title = title
        
        
class Book(library):

   def __init__(self,title,year):
       
        super().__init__(title)
        self.year = year
        library.books.append(self.title)

   def printBooks(self):
       for i in range(len(self.books)):
           print("Τίτλος Βιβλίου:",self.books[i],end = " , ")
           print("Έτος έκδοσης:",self.year)
           

class Magazine(library):
    
    def __init__(self,title,month,year):
        super().__init__(title)
        self.month = month
        self.year = year
        library.magazines.append(title)
     
    def printMagazines(self):
        for i in range(len(self.magazines)):
            print("Τίτλος περιοδικού:",self.magazines[i],end = " , ")
            if self.month < 10:
             print("Ημερομηνία έκδοσης: 0",self.month,sep = "",end = "/")
            else:
             print("Ημερομηνία έκδοσης:",self.month,end = "/")
            print(self.year)

           
b01 = Book('a',2021)
b02 = Book('b',2022)
b03 = Book('c',2023)
b03.printBooks()
m01 = Magazine('d',4,2021)
m02 = Magazine('e',5,2022)
m03 = Magazine('f',6,2023)
m03.printMagazines()
print("Η βιβλιοθήκη διαθέτει",len(library.books),"βιβλία και",len(library.magazines),"περιοδικά.")                