# -*- coding: utf-8 -*-
"""
   File name: ex_10.57.py
   
   *---------------------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται ένα λεξικό και ένα κλειδί και θα επιστρέφει την πληροφορία αν στο λεξικό υπάρχει
   το συγκεκριμένο κλειδί ή όχι. 
"""

def isInDictionary(d,k):
    if k in d:
        return True
    else:
        return False
    
d = {'a': 1, 'b': 2}
key = eval(input("Δώσε κλειδί για έλεγχο: "))
if isInDictionary(d,key):
   print("Το κλειδί",key,"υπάρχει στο λεξικό.")
else:
   print("Το κλειδί",key,"δεν υπάρχει στο λεξικό.")    