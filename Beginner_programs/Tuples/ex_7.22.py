# -*- coding: utf-8 -*-
"""
   File name: ex_7.22.py
   
   *---------------------------------
   
   Δίνεται λίστα με πλειάδες από στοιχεία μαθητών: όνομα,βαθμός,τάξη. Ταξινομήστε τη με βάση τον βαθμό και, μετά, κατά όνομα.
"""

l = [('Στέργιος',17,'Γ5'),('Χρήστος',18,'Γ4'),('Ακύλας',19,'Γ3')]
l.sort(key=lambda a: a[1])
l.sort(key=lambda a: a[0])
print(l)