# -*- coding: utf-8 -*-
"""
   File name: ex_10.24.py

   *---------------------------------------------------------

   Να γράψετε συνάρτηση που θα ελέγχει αν ένας αριθμός είναι παλίνδρομος.
"""

def checkPalindrome(n):
 temp = n
 rev = 0
 while(n > 0):
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
 if(temp == rev):
    print("Ο αριθμός",temp,"είναι παλίνδρομος!")
 else:
    print("Ο αριθμός",temp,"δεν είναι παλίνδρομος!")
    
    
    
x = int(input("Δώσε έναν ακέραιο αριθμό: "))
checkPalindrome(x)    