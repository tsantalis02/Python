# -*- coding: utf-8 -*-
"""
   File name: ex_6.7.py
   
   *------------------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται σειρά λέξεων από το πληκτρολόγιο και θα τις τοποθετεί σε λίστα. Στη συνέχεια, για 
   ένα δοσμένο κείμενο θα βρίσκει τη συχνότητα εμφάνισης των λέξεων της λίστας σε αυτό. 
"""

words = list()

for i in range(5):
    x = input("Δώσε μια λέξη: ")
    words.append(x)
keimeno = 'Το υλικό αυτής της σελίδας προσφέρεται μόνο σε φοιτητές του τμήματος Εφαρμοσμένης Πληροφορικής - ΠΑΜΑΚ.'
word_freq = [keimeno.count(i) for i in words]
for i in range(len(words)):
    print("'",words[i],"': ",word_freq[i],sep = "",end = " ")