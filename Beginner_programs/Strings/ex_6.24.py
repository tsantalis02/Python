# -*- coding: utf-8 -*-
"""
   File name: ex_6.24.py
   
   *---------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται κείμενο και θα εμφανίζει πόσοι χαρακτήρες δεν είναι γράμματα.
"""

txt = '''Στο πρώτο φιλικό επί ελληνικού εδάφους εν όψει του Παγκοσμίου Κυπέλλου, η Εθνική ομάδα μπάσκετ υποδέχεται τη 
Σλοβενία του Λούκα Ντόντσιτς στις 4 Αυγούστου στο ΟΑΚΑ. Το κοινό πέρα από τα αστέρια των δύο ομάδων θα απολαύσει και την 
βράβευση του μεγάλου Νίκου Γκάλη.
'''
s = 0
for i in range(len(txt)):
    if(txt[i].isalpha() == False): # and txt[i] != ' '): σε περίπτωση που δεν θέλουμε να μετράει τα κενά 
        s += 1
print(s,"χαρακτήρες δεν είναι γράμματα.")        