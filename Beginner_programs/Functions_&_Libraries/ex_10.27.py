# -*- coding: utf-8 -*-
"""
   File name: ex_10.27.py
   
   *-----------------------------------------
   
   Δημιουργήστε αναδρομική συνάρτηση για την αντιστροφή ενός κειμένου.
"""

def reverse_text(s):
    if len(s) == 0:
        return s
    else:
        return reverse_text(s[1:]) + s[0]
    
    
text = input("Γράψε ότι θες: ")
r_text = reverse_text(text)
print("Το κείμενο αντίστροφα:",r_text)    