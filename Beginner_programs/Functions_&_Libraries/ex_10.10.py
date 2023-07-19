# -*- coding: utf-8 -*-
"""
   File name: ex_10.10.py
   
   *-----------------------------------------------
   
   Δημιουργήστε μια λειτουργική μονάδα που θα εμφανίζει «προβλέψεις» για τον καιρό (τυχαία). Χρησιμοποείται το module weather.py
"""

import weather

k = int(input("Δώσε αριθμό προβλέψεων: "))
for i in range(k):
    w = weather.weather()
    for j in w:
     print("Πρόβλεψη: ",j)
