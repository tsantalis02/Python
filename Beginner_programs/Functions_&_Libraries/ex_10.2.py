# -*- coding: utf-8 -*-
"""
   File name: ex_10.2.py
   
   *-------------------------------------
   
   Να γράψετε συνάρτηση που θα δέχεται δύο αριθμούς και θα αντιμεταθέτει τις τιμές τους μόνο αν είναι διαφορετικοί μεταξύ
   τους.
"""

def antimetathesi(a,b):
    if a != b:
        x = a
        a = b
        b = x
    return(a,b)

x,y = antimetathesi(2,3)
print("x=",x,"y=",y)
    