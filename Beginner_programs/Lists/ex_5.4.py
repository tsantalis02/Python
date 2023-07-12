# -*- coding: utf-8 -*-
"""
   File name: ex_5.4.py
   
   *--------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται λίστα με βαθμολογίες από το 0 μέχρι το 10 και θα επιστρέφει μια νέα λίστα με τη 
   συχνότητα εμφάνισης όσων βαθμών υπάρχουν στη λίστα.
"""
vathmoi = [3,5,5,8,5,10]
syxnotita = list()
for i in range(len(vathmoi)):
    print("vathmos =",vathmoi[i])
    print("syxnotita =",vathmoi.count(vathmoi[i]))
    syxnotita.append([vathmoi.count(vathmoi[i]),vathmoi[i]])
print("[SYXNOTITA, VATHMOS]")
print(syxnotita)     