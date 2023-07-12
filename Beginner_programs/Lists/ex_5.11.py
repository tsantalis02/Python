# -*- coding: utf-8 -*-
"""
   File name: ex_5.11.py
   
   *------------------------------------
   
   Να γράψετε πρόγραμμα το οποίο θα δημιουργεί μια λίστα που θα περιλαμβάνει όλους τους τριψήφιους αριθμούς. Στη συνέχεια, 
   θα δημιουργεί μια 2η λίστα που θα περιλαμβάνει τους αριθμούς της 1ης, από τον μεγαλύτερο προς τον μικρότερο. Ως κριτήριο 
   ταξινόμησης να θεωρηθεί το άθροισμα των ψηφίων κάθε αριθμού.
"""

first_list = list()

for i in range(100,1000):
   first_list.append(i)
synolo = 0
second_list = list()
for i in range(len(first_list)):
    psifio_01 = first_list[i] // 100
    psifio_02 = (first_list[i] % 100) // 10
    psifio_03 = (first_list[i] % 100) % 100
    synolo = psifio_01 + psifio_02 + psifio_03
    second_list.append(synolo)
second_list.sort(reverse = True)
print("2η λίστα: ",second_list)    