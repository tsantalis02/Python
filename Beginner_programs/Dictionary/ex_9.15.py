# -*- coding: utf-8 -*-
"""
   File name: ex_9.15.py
   
   *--------------------------------------
   
   Ένα λεξικό περιέχει ως κλειδιά τους αριθμούς έως και το 9 με τη μορφή χαρακτήρων. Οι τιμές τους είναι ημερομηνίες 
   κατάθεσης της φορολογικής δήλωσης. Να γράψετε πρόγραμμα που θα δέχεται έναν ΑΦΜ και, με βάση το τελευταίο ψηφίο του, θα 
   εμφανίζει την ημερομηνία που πρέπει να γίνει η δήλωση.
"""

d = {'0': '19/08','1': '19/08', '2': '24/08', '3': '24/08','4': '19/08','5': '16/08','6': '16/08','7': '24/08','8': '16/08','9': '24/08'}
afm = input("Δώσε ΑΦΜ: ")
tel = afm[-1]
print(tel)
for key,val in d.items():
    if (key == '0' or key == '1' or key == '4') and key == tel:
        print("Η φορολογική δήλωση πρέπει να κατατεθεί μέχρι τις",d[key])
    elif (key == '2' or key == '3' or key == '7' or key == '9') and key == tel:
        print("Η φορολογική δήλωση πρέπει να κατατεθεί μέχρι τις",d[key])
    elif (key == '5' or key == '6' or key == '8') and key == tel: 
        print("Η φορολογική δήλωση πρέπει να κατατεθεί μέχρι τις",d[key])    