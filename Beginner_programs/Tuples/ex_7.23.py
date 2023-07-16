# -*- coding: utf-8 -*-
"""
   File name: ex_7.23.py
   
   *--------------------------------------------------
   
   Δίνεται πρόταση από το πληκτρολόγιο. Να φτιάξετε λίστα πλειάδων με τα ζεύγη (λέξη,πλήθος) που θα εκφράζει το π΄΄οσες φορές
   εμφανίζεται κάθε λέξη μέσα στο κείμενο.
"""

word_str = input("Γράψε ότι θες: ")
l = list()
x = word_str.split()
word_freq = [word_str.count(i) for i in x]
for i in range(len(word_freq)):
    tup = x[i],word_freq[i] 
    l.append(tup)
print(l)    