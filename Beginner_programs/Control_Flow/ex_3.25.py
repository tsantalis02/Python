# -*- coding: utf-8 -*-
"""
   File name: ex_3.25.py
   
   *------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται έναν αριθμό και θα εμφανίζει μήνυμα αν είναι πολλαπλάσιο του 3, του 5 ή του 7.
"""

num = int(input("Δώσε έναν αριθμό: "))
if(num % 3 == 0):
    print("Ο αριθμός",num,"είναι πολλαπλάσιο του 3.")
elif(num % 5 == 0):
    print("Ο αριθμός",num,"είναι πολλαπλάσιο του 5.")
elif(num % 7 == 0):
    print("Ο αριθμός",num,"είναι πολλαπλάσιο του 7.")    
else:
    print("Ο αριθμός",num,"δεν είναι πολλαπλάσιο του 3,του 5 ή του 7.")