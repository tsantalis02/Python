# -*- coding: utf-8 -*-
"""
   File name: ex_10.42.py

   *-----------------------------------------------------------

   Υπολογίστε ααδρομικά το άθροισμα των ψηφίων ενός αριθμού.
"""

def athroisma_psifiwn( n ):
    if n == 0:
        return 0
    return (n % 10 + athroisma_psifiwn(int(n / 10)))
 

num = int(input("Δώσε αριθμό: "))
result = athroisma_psifiwn(num)
print("Το άθροισμα των ψηφίων του αριθμού",num,"είναι", result)