# -*- coding: utf-8 -*-
"""
   File name: ex_7.14.py
   
   *----------------------------------
   
   ΝΑ γράψετε πρόγραμμα που θα ελέγχει αν υπάρχουν διπλά στοιχεία σε μια πλειάδα.
"""

tup = 0,1,2,3,4,5,2,6,4,8
for i in range(len(tup)):
    count = 1
    for j in range(len(tup)):
        if(j != i):
            if tup[j] == tup[i] :
                count += 1
    if(count == 2):
       print("Το στοιχείο",tup[i],"είναι διπλό.")
    else:
        print("Το στοιχείο",tup[i],"δεν είναι διπλό.")