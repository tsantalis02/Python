# -*- coding: utf-8 -*-
"""
   File name: ex_2.17.py
   
   *------------------------------

   Να γράψετε πρόγραμμα που θα δέχεται μια τιμή για το x και θα εμφανίζει την αντίστοιχη τιμή του y σύμφωνα με τον παρακάτω
   τύπο:
       y = 2x ** 3 + 3x ** 2 + (1/3)x + 12 
"""

x = int(input("Δώσε μια τιμή: "))
y = (2*x) ** 3 + (3*x) ** 2 + (1 / 3) * x + 12
print("Η τιμή του y για x=",x,"είναι",y,".")
