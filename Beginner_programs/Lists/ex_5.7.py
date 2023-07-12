# -*- coding: utf-8 -*-
"""
   File name: ex_5.7.py
   
   *--------------------------------------
   
   Να γράψετε πρόγραμμα που θα δέχεται τον τύπο προϊόντος (τύπος 1,2 και 3) και τις πωλήσεις για καθένα από τα 10 προϊόντα 
   μιας επιχείρησης, εμφανίζοντας:
       - Πόσα προϊόντα κάθε τύπου διαθέτει.
       - Το σύνολο των πωλήσεων ανά τύπο προϊόντος.
       - Το λιγότερο επικερδές προϊόν.
       - Τις πωλήσεις ανά τύπο προϊόντος σε φθίνουσα διάταξη.
       - Τον τύπο προϊόντος με τις περισσότερες μηδενικές πωλήσεις.
"""

typos = list()
pwlhseis = list()
for i in range(10):
    t = int(input("Δώσε τον τύπο του προϊόντος (1,2 ή 3): "))
    typos.append(t)
    pwl = float(input("Δώσε τις πωλήσεις του προϊόντος: "))
    pwlhseis.append(pwl)

syn_pwl_01 = 0
syn_pwl_02 = 0
syn_pwl_03 = 0
pro_01 = 0
pro_02 = 0
pro_03 = 0
miden_pwl_01 = 0
miden_pwl_02 = 0
miden_pwl_03 = 0

for i in range(10):
    if(typos[i] == 1):
        syn_pwl_01 += pwlhseis[i]
        pro_01 += 1
        if(pwlhseis[i] == 0):
            miden_pwl_01 += 1
    elif(typos[i] == 2):
        syn_pwl_02 += pwlhseis[i]
        pro_02 += 1
        if(pwlhseis[i] == 0):
            miden_pwl_02 += 1
    else:
        syn_pwl_03 += pwlhseis[i]
        pro_03 += 1
        if(pwlhseis[i] == 0):
            miden_pwl_03 += 1
pwl_01 = [pwlhseis[i] for i in range(10) if typos[i] == 1]
pwl_02 = [pwlhseis[i] for i in range(10) if typos[i] == 2]
pwl_03 = [pwlhseis[i] for i in range(10) if typos[i] == 3]    
print("Τύπος 1: ",pro_01,"προϊόντα με",syn_pwl_01,"€ σε πωλήσεις.")
print("Τύπος 2: ",pro_02,"προϊόντα με",syn_pwl_02,"€ σε πωλήσεις.")
print("Τύπος 3: ",pro_03,"προϊόντα με",syn_pwl_01,"€ σε πωλήσεις.")           
print("Το λιγότερο επικερδές προϊόν είναι αυτό με πωλήσεις",min(pwlhseis),"€.")
print("Τύπος 1 πωλήσεις: ",end="")
pwl_01.sort(reverse = True)
print(pwl_01)
print("Τύπος 2 πωλήσεις: ",end = "")
pwl_02.sort(reverse = True)
print(pwl_02)
print("Τύπος 3 πωλήσεις: ",end = "" )
pwl_03.sort(reverse = True)
print(pwl_03)
print("Το προϊόν με τις περισσότερες μηδενικές πωλήσεις είναι ",end = "")
if(miden_pwl_01 > miden_pwl_02 and miden_pwl_01 > miden_pwl_03):
    print("τύπου 1.")
if(miden_pwl_02 > miden_pwl_01 and miden_pwl_02 > miden_pwl_03):
    print("τύπου 2.")
if(miden_pwl_03 > miden_pwl_01 and miden_pwl_03 > miden_pwl_02):
    print("τύπου 3.")    
if(miden_pwl_01 == 0 and miden_pwl_02 == 0 and miden_pwl_03 == 0):
    print("κανένα.")