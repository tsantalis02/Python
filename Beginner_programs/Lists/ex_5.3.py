# -*- coding: utf-8 -*-
"""
   File name: ex_5.3.py
   
   *-----------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται λίστα και αριθμό και θα καταχωρεί, σε νέα λίστα, τις θέσεις όπου βρίσκεται αυτός ο 
   αριθμός.
"""

# l = list(range(1,11))
l = [1,2,3,4,4,5,3,4]
theseis = list()
counter = 0
x = int(input("Δώσε ακέραιο θετικό αριθμό: "))
for i in range(len(l)):
    if(x == l[i]):
        theseis.append(i+1)
        counter += 1
if(counter == 0):
    print("Ο αριθμός",x,"δεν βρέθηκε στην λίστα.")
else:
    print("Ο αριθμός",x,"βρέθηκε στις θέσεις ",end = "")
    print(theseis)
   
