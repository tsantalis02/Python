# -*- coding: utf-8 -*-
"""
Μονάδα κώδικα για την τυχαία πρόβλεψη του καιρού.
@author:Stergios Tsantalis
"""

import random

def weather():
    x = random.randint(0,3)
    if x == 0:
        yield 'Λιακάδα'
    if x == 1:
        yield 'Τοπικές καταιγίδες'
    if x == 2:
        yield 'Βροχή'
    if x == 3:
        yield 'Χιόνι'
        
# testing
if __name__ =='__ex.10.10py__':        
    k = int(input("Δώσε αριθμό προβλέψεων: "))
    for i in range(k):
        w = weather()
        for j in w:
         print("Πρόβλεψη: ",j)
