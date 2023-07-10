# -*- coding: utf-8 -*-
"""
   File name: ex_2.3.py
   
   *--------------------------------
   
   Τρεις φίλοι έχουν παίξει ένα δελτίο στοιχήματος. Καθένας έχει δ΄ωσει ένα ποσό. Να γράψετε πρόγραμμα που θα ζητάει το ποσό
   που έπαιξε κάθε παίκτης, καθώς και το ποσό που κέρδισε το δελτίο τους, και θα εμφανίζει τα κέρδη για τον καθένα από 
   αυτούς.
"""

poso_a = float(input("Δώσε το ποσό που έπαιξε ο παίκτης Α: "))
poso_b = float(input("Δώσε το ποσό που έπαιξε ο παίκτης Β: "))
poso_c = float(input("Δώσε το ποσό που έπαιξε ο παίκτης Γ: "))
synoliko = poso_a + poso_b + poso_c
kerdh = float(input("Δώσε το ποσό που κέρδισε το δελτίο τους: "))
pososto_a = poso_a / synoliko
pososto_b = poso_b / synoliko
pososto_c = poso_c / synoliko
print("Ο παίκτης Α κέρδισε ",kerdh * pososto_a,"€")
print("Ο παίκτης Β κέρδισε ",kerdh * pososto_b,"€")
print("Ο παίκτης Γ κέρδισε ",kerdh * pososto_c,"€")
