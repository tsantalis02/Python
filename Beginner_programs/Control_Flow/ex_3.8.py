# -*- coding: utf-8 -*-
"""
   File name: ex_3.8.py
   
   *-------------------------------
   
   Μια εταιρεία παράγει και πουλάει δύο κατηγορίες υφασμάτων: τύπου Α, με 0.2, και τύπου Β, με 0.4€/μέτρο. Για παραγγελίες
   ποσότητας μέχρι 300 μέτρα ή αξίας μέχρι 100€, δίνει έκπτωση 5%, εν΄ω για μεγαλύτερες ποσότητες ή αξία δίνει έκπτωση 15%.
   Να γράψετε πρόγραμμα που θα δέχεται τις ποσότητες αγοράς από τα δύο είδη υφασμάτων και θα εμφανίζει το τελικό πληρωτέο 
   ποσό.
"""

pos_yf_a = float(input("Δώσε την ποσότητα αγοράς υφάσματος τύπου Α (σε μέτρα): "))
pos_yf_b = float(input("Δώσε την ποσότητα αγοράς υφάσματος τύπου Β (σε μέτρα): "))
kostos_a = pos_yf_a * 0.2
kostos_b = pos_yf_b * 0.4
synoliko = kostos_a + kostos_b
if((pos_yf_a + pos_yf_b) <= 300 or synoliko <= 100):
    ekptosi = synoliko * 5 / 100
else:
    ekptosi = synoliko * 15 / 100
synoliko -= ekptosi
print("Ο πελάτης θα πληρώσει ",synoliko,"€.",sep = "")    