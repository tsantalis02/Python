# -*- coding: utf-8 -*-
"""
   File name: ex_6.4.py
   
   *-----------------------------------
   
   Να εμφανιστεί η συχνότητα εμφάνισης κάθε λέξης ενός κειμένου.
"""

word_str = input("Γράψε ότι θες: ")
x = word_str.split()
word_freq = [word_str.count(i) for i in x]
for i in range(len(word_freq)):
    print("'",x[i],"': ",word_freq[i],sep = "",end = "   ")

