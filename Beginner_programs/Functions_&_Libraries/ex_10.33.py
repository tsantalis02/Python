# -*- coding: utf-8 -*-
"""
   File name: ex_10.33.py
   
   *-------------------------------------
   
   Υπολογίστε τον μέγιστο κοινό διαιρέτη με αναδρομή.
"""

def gcd(a, b):
 if a == b:
  return a
 elif a < b:
  return gcd(b, a)
 else:
  return gcd(b, a - b)

x = int(input("Δώσε έναν αριθμό: "))
y = int(input("Δώσε έναν αριθμό: "))
mkd = gcd(x,y)
print("Ο μέγιστος κοινός διαιρέτης των αριθμών",x,",",y,"είναι ο αριθμός",mkd) 