# -*- coding: utf-8 -*-
"""
   File name: ex_6.9.py 
   
   *------------------------------------------
   
   Για δοσμένο κείμενο να γράψετε πρόγραμμα που θα αφαιρεί τον χαρακτήρα '\n' και θα προσθέτει την ετικέτα (tag) <br>.
"""

s = '''«Στο πρώτο φιλικό επί ελληνικού εδάφους εν όψει του Παγκοσμίου Κυπέλλου, η Εθνική ομάδα μπάσκετ υποδέχεται τη 
Σλοβενία του Λούκα Ντόντσιτς στις 4 Αυγούστου στο ΟΑΚΑ. Το κοινό πέρα από τα αστέρια των δύο ομάδων θα απολαύσει και την 
βράβευση του μεγάλου Νίκου Γκάλη».
'''

s_01 = s.replace('\n', '<br>')
s_01 = s_01.split('<br>')
for i in range(len(s_01)):
    print(s_01[i])