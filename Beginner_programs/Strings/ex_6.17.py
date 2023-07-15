# -*- coding: utf-8 -*-
"""
   File name: ex_6.17.py
   
   *-------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται έναν αριθμό έως 3 ψηφία και θα εμφανίζει κ΄σθε στοιχείο με τη μορφή λέξης. Π.χ. για 
   τον αριθμό 12 να εμφανίζει «Ένα» και «Δύο». 
"""

x = int(input("Δώσε αριθμό έως 3 ψηφία: "))
psifia = list()
psifio_01 = x // 100
psifio_02 = (x % 100) // 10
psifio_03 = (x % 100) % 10
psifia.append(psifio_01)
psifia.append(psifio_02)
psifia.append(psifio_03)
s = ''
for i in range(3):
    if(psifia[i] == 1):
        s = s + ' «Ένα»'
    elif(psifia[i] == 2):
        s = s + ' «Δύο»'
    elif(psifia[i] == 3):
        s = s + ' «Τρία»'
    elif(psifia[i] == 4):
        s = s + ' «Τέσσερα»'
    elif(psifia[i] == 5):
        s = s + ' «Πέντε»'
    elif(psifia[i] == 6):
        s = s + ' «Έξι»'
    elif(psifia[i] == 7):
        s = s + ' «Εφτά»'
    elif(psifia[i] == 8):
        s = s + ' «Οκτώ»'
    elif(psifia[i] == 9):    
        s = s + ' «Εννιά»'
print(x,"=",s)        
