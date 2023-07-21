# -*- coding: utf-8 -*-
"""
   File name: ex_10.54.py
   
   *--------------------------------------------------
   
   Να γράψετε συνάρτηση που θα υπολογίζει το πλήθος των ψηφίων ενός αριθμού.
"""


def countDigits(n): 
 count=0
 while(n>0):
    count=count+1
    n=n//10
 return(count)   

 
n=int(input("Δώσε έναν αριθμό:"))
c = countDigits(n)
print("Το πλήθος των ψηφίων του αριθμού",n,"είναι:",c) 