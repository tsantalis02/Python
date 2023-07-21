# -*- coding: utf-8 -*-
"""
   File name:ex_10.59.py
   
   *------------------------------------------------
   
   Να γράψετε κώδικα σε συνάρτηση που να ελέγχει αν ο ΑΦΜ μιας επιχείρησης είναι έγκυρος ή όχι. Ο ΑΦΜ αποτελείται από 9 
   ψηφία. Στη γενική του μορφή ο ΑΦΜ έχει τα εξής ψηφία:
                                
                                  a1 a2 a3 a4 a5 a6 a7 a8 a9
   Ο αλγόριθμος για τον έλεγχο εγκυρότητας ενός ΑΦΜ είναι:
   Υπολόγισε το άθροισμα
            Σ = 256α1 + 128α2 + 64α3 + 32α4 + 16α5 + 8α6 + 4α7 + 2α8
   Υπολόγισε το υπόλοιπο (Υ) της διαίρεσης του Σ με τον αριθμό 11.
   Έλεγξε αν το τελευταίο ψηφίο του Υ ισούται με το τελευταίο ψηφίο (α9) του ΑΦΜ. Αν ναι, τότε ο ΑΦΜ είναι έγκυρος.
   Διαφορετικά, δεν είναι έγκυρος.

   Π.χ. Έστω ο ΑΦΜ 078251685. Έχουμε Σ = 1600, ενώ το υπόλοιπο της διαίρεσης 1600/11 είναι 5. Το υπόλοιπο ισούται με το
   τελευταίο ψηφίο του ΑΦΜ α9 = 5. Άρα, ο ΑΦΜ είναι έγκυρος.         
"""

def checkAFM(s):
    l_afm = list()
    athr = 0
    k = 256
    for i in range(len(s)):
        l_afm.append(s[i])
        if i < 8:
         athr +=  (k * int(s[i]))
         k /= 2    
    yp = athr % 11
    if (yp % 10) == int(l_afm[-1]):
        print("Ο ΑΦΜ είναι έγκυρος.")
    else:
        print("Ο ΑΦΜ δεν είναι έγκυρος.")
        
        
afm = input("Δώσε τον ΑΦΜ: ")
checkAFM(afm)        