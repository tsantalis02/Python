# -*- coding: utf-8 -*-
"""
    File name: ex_10.40.py 

   *------------------------------------------

   Να γράψετε συνάρτηση που θα υπολογίζει τον μεγαλύτερο άρτιο και τον μικρότερο περιττό αριθμό σε δοσμένο διάστημα τιμών. 
"""

def createLists(k,n):
 even = list()
 odd = list()   
 for i in range(k,n):
  if i % 2 == 0:
    even.append(i)
  else:
    odd.append(i)
 return even,odd


a = int(input("Δώσε αριθμό: "))
b = int(input("Δώσε αριθμό: "))
e,o = createLists(a,b)
print("Ο μεγαλύτερος άρτιος στο δοσμένο διάστημα τιμών είναι ο αριθμός",max(e))
print("Ο μικρότερος περιττός στο δοσμένο διάστημα τιμών είναι ο αριθμός",min(o))        