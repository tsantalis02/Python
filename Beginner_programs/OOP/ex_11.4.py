# -*- coding: utf-8 -*-
"""
   File name: ex_11.4.py
   
   *------------------------------------------------------
   
   Δημιουργήστε κλάση αντικειμένων λίστας που θα περιέχει τις λειτουργίες της ένωσης και της τομής συνόλων.
"""

class ListToSet():
    
    def __init__(self,l01,l02):
        self.set01 = set(l01)
        self.set02 = set(l02)
        
    def uni(self):
        s_union = self.set01.union(self.set02)
        return s_union
    
    def inter(self):
        s_inter = self.set01.intersection(self.set02)
        return s_inter
    
    
l01 = [1,2,3,4]
l02 = [3,4,5,6]
s_01 = ListToSet(l01,l02)
s_uni = s_01.uni()
print("Ένωση συνόλων:",s_uni)
s_inter = s_01.inter()
print("Τομή συνόλων:",s_inter)    