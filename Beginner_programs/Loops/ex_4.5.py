# -*- coding: utf-8 -*-
"""
   File name: ex_4.5.py
   
   *--------------------------------
   
   Ένα φορτηγό πλοίο δέχεται κοντέινερ συνολικού βάρους 10,000 τόνων. Να γράψετε πρόγραμμα που θα δέχεται διαδοχικά 
   κοντέινερ και θα εμφανίζει πόσα κοντέινερ δέχθηκε τελικά, το συνολικό βάρος, το μέσο βάρος των κοντέινερ και πόσο βάρος
   έμεινε ανεκμετάλλευτο.
"""

xwros = 10000
count = 0
teliko_varos = 0

while xwros > 0:
    container = int(input("Δώσε βάρος κοντέινερ (σε τόνους): "))    
    if((xwros - container) >= 0):
        count += 1
        xwros = xwros - container
        teliko_varos = teliko_varos + container
    else:
        break

print("Το φορτηγό πλοίο δέχθηκε",count,"κοντέινερ.")
print("Το συνολικό βάρος των κοντέινερ είναι",teliko_varos,"τόνοι.")
print("Το μέσο βάρος των κοντέινερ είναι",(teliko_varos / count),"τόνοι.")
print("Το βάρος που έμεινε ανεκμετάλλευτο είναι",xwros,"τόνοι.")    