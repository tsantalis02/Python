# -*- coding: utf-8 -*-
"""
   File name: ex_10.30.py
   
   *------------------------------------------------
   
   Να γράψετε συνάρτηση που θα ελέγχει αν ένα κείμενο είναι αναγραμματισμός άλλου.
"""

def check(s1, s2):
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
         
s1 = input("Γράψε ένα κείμενο:")
s2 = input("Γράψε ένα κείμενο:")
check(s1, s2)