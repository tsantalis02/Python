# -*- coding: utf-8 -*-
"""
   File name: ex_4.4.py
   
   *--------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται ακέραιους αριθμούς και θα τους προσθέτει, υπολογίζοντας, στο τέλος, τον μέσο όρο τους.
   Η διαδικασία θα σταματά όταν δοθεί το 0. Να γίνεται έλεγχος αν οι αριθμοί δεν είναι ακέραιοι, εμφανίζοντας κατάλληλο μήνυμα,
   και να υπάρχει σχετική πρόβλεψη για την περίπτωση που δεν θα δοθεί μη μηδενικός ακέραιος.
"""

x = int(input("Δώσε ακέραιο αριθμό: "))
synolo = 0
count = 0
while(x % 1 == 0 and x != 0):
    synolo += x
    count += 1
    x = int(input("Δώσε ακέραιο αριθμό: "))
    if(x % 1 != 0):
        print("Δεν είναι ακέραιος.")
mo = synolo / count
print("Ο μέσος όρος είναι %.2f" %mo)        