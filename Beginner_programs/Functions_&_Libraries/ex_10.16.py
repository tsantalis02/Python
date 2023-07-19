# -*- coding: utf-8 -*-
"""
   File name: ex_10.16.py
   
   *-----------------------------------------------
   
   Υλοποιήστε τον αλγόριθμο της σειριακής αναζήτησης σε συνάρτηση. Πως μπορεί να καλείται; Τι παραμέτρους θα χρειαστεί; Τι 
   θα μπορούσε να επιστρέφει;
"""

def search(List, n):
  
    for i in range(len(List)):
        if List[i] == n:
            return True
    return False

l = [1,2,'Stergios',4,5,'Tsantalis']
k = 5
if search(l,k):
    print("Found.")
else:
    print("Not Found.")    