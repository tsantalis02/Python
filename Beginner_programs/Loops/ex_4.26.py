# -*- coding: utf-8 -*-
"""
   File name: ex_4.26.py
   
   *------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται ως όρισμα έναν ακέραιο αριθμό Ν, όπου 0<=Ν<=10². Στη συνέχεια να υπολογίζει το
   ελάχιστο θετικό ακέραιο αριθμό Ρ, του οποίου το γινόμενο των ψηφίων ισούται με το Ν. Πχ. αν Ν=10, τότε Ρ=25. Το
   αποτέλεσμα να τυπώνεται στην οθόνη.
"""

n = int(input("Δώσε έναν ακέραιο αριθμό από το 0 έως το 100: "))
while(n < 0):
 n = int(input("Δώσε έναν ακέραιο αριθμό από το 0 έως το 100: "))
k = 0
arithmos = 0
synthiki = False
while(synthiki == False and k < 999):
    psifio_01 = k // 100
    psifio_02 = (k % 100) // 10
    psifio_03 = (k % 100) % 10
    if(psifio_01 == 0 and psifio_02 == 0):
        arithmos = psifio_03
    if(psifio_01 == 0):
        arithmos = psifio_02 * psifio_03
    else:
        arithmos = psifio_01 * psifio_02 * psifio_03
    if(arithmos == n):
        synthiki = True
    k += 1 
if(synthiki == True):    
 print("Ν =",n,",Ρ =",k-1)
else:
 print("Δεν βρέθηκε αριθμός.")        