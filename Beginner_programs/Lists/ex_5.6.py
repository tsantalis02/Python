# -*- coding: utf-8 -*-
"""
   File name: ex_5.6.py
   
   *----------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται 10 βαθμούς από τον χρήστη και θα τους αποθηκεύει σε λίστα, εάν είναι έγκυροι. Επίσης,
   θα πρέπει να εμφανίζει τον μέσο όρο της βαθμολογίας, τον μεγαλύτερο και τον μικρότερο βαθμό, καθώς και το ποσοστό 
   επιτυχίας που σημειώθηκε. Στο τέλος, να εμφανιστούν οι βαθμοί κατά φθίνουσα διάταξη.
"""

v = list()

for i in range(10):
    vathmos = float(input("Δώσε βαθμό: "))
    if(vathmos >= 0 or vathmos <= 20):
      v.append(vathmos)
s = 0
epityxia = 0
for i in range(len(v)):
   s += v[i]
   if(v[i] >= 10):
       epityxia += 1
print("Ο μέσος όρος είναι",(s / len(v)))
print("Ο μεγαλύτερος βαθμός είναι",max(v))
print("Ο μικρότερος βαθμός είναι",min(v))
print("Το ποσοστό επιτυχίας είναι",(epityxia / len(v)) * 100, "%.")
v.sort(reverse = True)
print(v)    