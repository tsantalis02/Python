# -*- coding: utf-8 -*-
"""
   File name: ex_7.2.py
   
   *-------------------------------------------
   
   Μια λίστα περιέχει πλειάδες δύο στοιχείων. Το ένα στοιχείο είναι κείμενο και το άλλο αριθμός. Ταξινομήστε τη λίστα με 
   βάση τους αριθμούς των πλειάδων.
"""

l = [('Στέργιος',20),('Χρήστος',16),('Απόστολος',39)]
l.sort(key=lambda a: a[1])
print(l)