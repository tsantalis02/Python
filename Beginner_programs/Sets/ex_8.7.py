# -*- coding: utf-8 -*-
"""
   File name: ex_8.7.py
   
   *--------------------------------------------------
   
   Να γράψετε πρόγραμμα που θα διαβάζει κείμενο και θα εμφανίζει όλους τους διαφορετικούς χαρακτήρες που υπάρχουν μέσα σ΄΄  αυτό.
"""

keimeno = input("Γράψε κείμενο: ")
s = set(keimeno)
print(s)