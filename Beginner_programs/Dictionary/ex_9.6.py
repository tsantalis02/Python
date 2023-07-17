# -*- coding: utf-8 -*-
"""
   File name: ex_9.6.py
   
   *-----------------------------------
   
   Να γράψετε πρόγραμμα που θα ενώνει 3 λεξικά μεταξύ τους σε ένα νέο.
"""

d_all = {}
a = {'a': 1}
b = {'b': 2}
c = {'c': 3}
d_all.update(a)
d_all.update(b)
d_all.update(c)
print(d_all)