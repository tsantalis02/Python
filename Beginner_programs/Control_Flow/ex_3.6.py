# -*- coding: utf-8 -*-
"""
   File name: ex_3.6.py
   
   *---------------------------------------

   Σε μια επιχείρηση δίνεται στους υπαλλήλους επίδομα σύμφωνα με τα παρακάτω στοιχεία:
       
       ΕΠΙΠΕΔΟ ΕΚΠΑΙΔΕΥΣΗΣ                   ΕΤΗ ΥΠΗΡΕΣΙΑΣ                     ΕΠΙΔΟΜΑ
                                                 0-15                             -
         ΠΡΩΤΟΒΑΘΜΙΑ                      
                                                 16-...                          100
                                                 
                                                 0-15                             40
         ΔΕΥΤΕΡΟΒΑΘΜΙΑ
                                                 16-...                          140
                                                 
                                                 0-10                             80
         ΤΡΙΤΟΒΑΘΜΙΑ
                                                 11-...                          200
   Να γράψετε πρόγραμμα που θα διαβάζει τον τύπο εκπαίδευσης(ΠΕ,ΔΕ και ΤΕ) και τα έτη υπηρεσίας, εμφανίζοντας το ποσό του 
   επιδ΄΄οματος.                                             
"""

ekpaideusi = input("Δώσε τον επίπεδο εκπαίδευσης (ΠΕ,ΔΕ και ΤΕ / PE,DE και TE): ")
eti = int(input("Δώσε τα έτη υπηρεσίας: "))
epidoma = 0
if(ekpaideusi == 'ΠΕ' or ekpaideusi == 'πε' or ekpaideusi == 'PE' or ekpaideusi == 'pe'):
    if(eti <= 15):
        epidoma = 0
    else:
        epidoma = 100
elif(ekpaideusi == 'ΔΕ' or ekpaideusi == 'δε' or ekpaideusi == 'DE' or ekpaideusi == 'de'):
     if(eti <= 15):
         epidoma = 40
     else:
         epidoma = 140
else:
    if(ekpaideusi == 'ΤΕ' or ekpaideusi == 'τε' or ekpaideusi == 'TE' or ekpaideusi == 'te'):
     if(eti <= 10):
       epidoma = 80
     else:
       epidoma = 200
    else:
        print("Λάθος εισαγωγή επίπεδου εκπαίδευσης.")         
print("Το επίδομα είναι ",epidoma,"€.",sep = "")