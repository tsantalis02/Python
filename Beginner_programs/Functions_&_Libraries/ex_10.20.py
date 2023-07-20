# -*- coding: utf-8 -*-
"""
   File name: ex_10.20.py
   
   *-------------------------------------------------
   
   Να γράψετε συνάρτηση που θα υπολογίζει με την μέθοδο του Ερατοσθένη αν ένας αριθμός είναι πρώτος.
"""

def MethodOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    p = 2
    while (p * p <= num):
        if (prime[p] == True):
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1
    for p in range(2, num+1):
        if prime[p]:
            print(p)
            
            
n = int(input("Δώσε μέχρι και ποιο αριθμό θες να εμφανιστούν οι πρώτοι αριθμοί: "))
print("Πρώτοι αριθμοί μέχρι και το",n,":")
print(MethodOfEratosthenes(n))            