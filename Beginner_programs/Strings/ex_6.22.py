# -*- coding: utf-8 -*-
"""
   File name: ex_6.22.py
   
   *----------------------------------------

   Να γράψετε πρόγραμμα που θα δέχεται κείμενο πολλών γραμμών και θα το εμφανίζει βάζοντας αρίθμηση στις γραμμές του.
"""

count = 0
text = '''Στο πρώτο φιλικό επί ελληνικού εδάφους εν όψει του Παγκοσμίου Κυπέλλου, η Εθνική ομάδα μπάσκετ υποδέχεται τη 
Σλοβενία του Λούκα Ντόντσιτς στις 4 Αυγούστου στο ΟΑΚΑ. Το κοινό πέρα από τα αστέρια των δύο ομάδων θα απολαύσει και την 
βράβευση του μεγάλου Νίκου Γκάλη.
'''
text = text.splitlines()
for i in text:
    count += 1
    print("{}{}{}{}".format(count,"."," ",i))   
