# -*- coding: utf-8 -*-
"""
   File name: ex_3.26.py
   
   *---------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται έναν αριθμό, ένα σύμβολο από τα '+-*/' και έναν δεύτερο αριθμό και θα πραγματοποιεί
   την αντίστοιχη πράξη, εμφανίζοντας στο τέλος το αποτέλεσμα.
"""

num_01 = float(input("Δώσε έναν αριθμό: "))
symbol = input("Δώσε την πράξη: ")
num_02 = float(input("Δώσε έναν αριθμό: "))
apotelesma = 0
if(symbol == '+'):
    apotelesma = num_01 + num_02
elif(symbol == '-'):
    apotelesma = num_01 - num_02 
elif(symbol == '*'):
    apotelesma = num_01 * num_02
elif(symbol == '/'):
    apotelesma = num_01 / num_02
else:
    print("Λάθος εισαγωγή συμβόλου πράξης.")
print("Το αποτέλεσμα της πράξης",symbol,"είναι",apotelesma)    
