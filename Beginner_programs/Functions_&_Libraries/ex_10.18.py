# -*- coding: utf-8 -*-
"""
   File name: ex_10.18.py
   
   *----------------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται έναν ακέραιο αριθμό και θα επιστρέφει τον αντίστοιχό του στο δυαδικό σύστημα. 
   Δημιουργήστε άλλη μια συνάρτηση που να κάνει το αντίθετο.
"""

def decimalToBinary(n):
    return bin(n).replace("0b","")

def binaryToDecimal(n):
 decimal, i = 0, 0
 while(n != 0):
    dec = n % 10
    decimal = decimal + dec * pow(2, i)
    n = n//10
    i += 1
 return(decimal) 


print(decimalToBinary(5))
print(binaryToDecimal(100))      
