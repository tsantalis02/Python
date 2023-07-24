# -*- coding: utf-8 -*-
"""
   File name: ex_12.2.py
   
   *------------------------------------------------
   
   Να γράψετε πρόγραμμα που θα ανοίγει ένα αρχείο κειμένου και θα μετράει το πλήθος των χαρακτήρων που περιέχει.
"""

file = open("file.txt", "r", encoding = "utf8")
data = file.read()
number_of_characters = len(data)
print('Πλήθος χαρακτήρων του αρχείου:', number_of_characters)