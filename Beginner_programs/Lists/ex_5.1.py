# -*- coding: utf-8 -*-
"""
   File name: ex_5.1.py 
   
   *--------------------------------------
   
   Να γράψετε πρόγραμμα που θα βρίσκει το άθροισμα και το γινόμενο των στοιχείων μιας λίστας που βρίσκονται στις περιττές 
   και στις άρτιες θέσεις αντίστοιχα.
"""

x = list(range(1,7))
athroisma = 0
ginomeno = 1
for i in range(len(x)):
    print(x[i])
    if((i + 1) % 2 == 0):
        ginomeno *= x[i]
        print("γινόμενο:",ginomeno)
    else:
        athroisma += x[i]
        print("άθροισμα:",athroisma)
print("Το άθροισμα των στοιχείων που βρίσκονται στις περιττές θέσεις της λίστας είναι",athroisma,".")
print("Το γινόμενο των στοιχείων που βρίσκονται στις άρτιες θέσεις της λίστας είναι",ginomeno,".") 