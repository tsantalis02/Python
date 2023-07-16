# -*- coding: utf-8 -*-
"""
   File name: ex_7.25.py
   
   *-----------------------------------------------
   
   Να φτιάξετε μια λίστα πλειάδων που θα περιέχει α) το μήκος και το πλάτος ορθογωνίου (θα δίνονται από το πληκτρολόγιο), β)
   το εμβαδό και την περίμετρό του. 
"""

orthogonia = 5 # Έστω ότι έχουμε 5 ορθογώνια
l_orthogonia = list()

for i in range(orthogonia):
 # Ζητούμενο α)   
 mikos = eval(input("Δώσε το μήκος του ορθογωνίου: "))
 platos = eval(input("Δώσε το πλάτος του ορθωγωνίου: "))
 # Ζητούμενο β)
 emvado = mikos * platos
 perimetros = 2*mikos + 2*platos 
 orth = mikos,platos,emvado,perimetros
 l_orthogonia.append(orth)
print(l_orthogonia) 