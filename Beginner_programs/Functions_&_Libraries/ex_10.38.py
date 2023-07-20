# -*- coding: utf-8 -*-
""" 
   File name: ex_10.38.py
   
   *-----------------------------------------------
   
   Δημιουργήστε συνάρτηση που θα δέχεται κείμενο και θα επιστρέφει μόνο τους χαρακτήρες που υπάρχουν μια φορά σε αυτό.
"""

def oneFreqChar(ch_str):
 l_ch = list()
 for i in ch_str:
    if ch_str.count(i) == 1:
     l_ch.append(i)
 return(l_ch) 


ch_str = input("Γράψε ότι θες: ")
ch = oneFreqChar(ch_str)
print(ch)    