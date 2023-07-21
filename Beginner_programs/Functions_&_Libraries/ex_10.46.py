# -*- coding: utf-8 -*-
"""
   File name: ex_10.46.py
   
   *-------------------------------------------------
   
   Να γράψετε συνάρτηση που θα υπολογίζει πόσα φωνήεντα υπάρχουν σε μια φράση.
"""

def countVowels(s):
    count = 0
    vowels = ['a','e','o','u','i']
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    return count        
    
    
    
example = "Count number of vowels in a string in Python"
vow = countVowels(example)
print("Vowels:",vow)   