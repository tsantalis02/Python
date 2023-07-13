# -*- coding: utf-8 -*-
"""
   File name: ex_6.25.py
   
   *----------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται κείμενο από το πληκτρολόγιο και θα ελέγχει αν μπορεί να χρησιμοποιηθεί ως κωδικός
   ασφαλείας (password). Για να είναι αρκετά ισχυρός ο κωδικός, θα πρέπει να πληροί τις παρακάτω προϋποθέσεις:
       - Να αποτελείται από τουλάχιστον 8 χαρακτήρες.
       - Να περιέχει τουλάχιστον έναν αριθμό, ένα σύμβολο και ένα κεφαλαίο γράμμα.
   Αν δεν πληροί τις προϋποθέσεις ασφαλείας, να εμφανίζει μήνυμα «Ο κωδικός σας δεν είναι αρκετά ισχυρός».   
"""

keimeno = input("Δώσε κωδικό ασφαλείας (password): ")
kefalaio = 0
arithmos = 0
symbolo = 0
if(len(keimeno) >= 8):
    for i in range(len(keimeno)):
        if(keimeno[i].isupper() == True):
            kefalaio += 1
        if(keimeno[i].isnumeric() == True):
            arithmos += 1
        if(keimeno[i].isalpha() == False and keimeno[i].isnumeric() == False):
            symbolo += 1
    if(kefalaio >= 1 and arithmos >= 1 and symbolo >= 1):
        print("Ο κωδικός σας «",keimeno,"» είναι ισχυρός.",sep = "")
    else:
        print("Ο κωδικός σας «",keimeno,"» δεν είναι ισχυρός.",sep = "")
else:
    print("Ο κωδικός σας «",keimeno,"» δεν είναι ισχυρός.",sep = "")     