# -*- coding: utf-8 -*-
"""
   File name: ex_12.7.py
   
   *---------------------------------------------------------
   
   Ένα αρχείο περιέχει τα ονόματα χρηστών ενός υπολογιστή. Να γράψετε πρόγραμμα που θα ζητάει το όνομα ενός χρήστη και θα 
   εμφανίζει αν αυτό αντιστοιχεί σε όνομα χρήστη που υπάρχει ήδη. Αν δεν υπάρχει, θα το προσθέτει στο τέλος του.
"""

import csv
import sys


l01 = list()

with open("usernames.txt","r") as f01:
    for line in f01:
        if line[-1] == '\n':
         l01.append(line[:-1])
        else:
         l01.append(line)   
user = input("Δώσε ένα όνομα χρήστη: ")
if user in l01:
 print("Αυτό το όνομα χρήστη υπάρχει ήδη.")
 sys.exit()
if user not in l01:
 l01.append(user)

with open("usernames.txt","w") as f02:
    writer = csv.writer(f02)
    writer.writerow(l01)        