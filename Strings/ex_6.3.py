# -*- coding: utf-8 -*-
"""
   File name: ex_6.3.py
   
   *-----------------------------------
   
   Να εμφανιστεί η συχνότητα εμφάνισης κάθε χαρακτήρα ενός κειμένου.
"""

ch_str = input("Γράψε ότι θες: ")
ch_freq = [ch_str.count(i) for i in ch_str] 
print("Frequency")
for i in range(len(ch_str)):
    print("'",ch_str[i],"':",ch_freq[i],sep = "",end = ",")



