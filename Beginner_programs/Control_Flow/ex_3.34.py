# -*- coding: utf-8 -*-
"""
   File name: ex_3.34.py
   
   *--------------------------------------
   
   Να γράψετε πρόγραμμα που θα υπολογίζει τη συνάρτηση f(x,y) για διάφορες τιμές των x και y που δίνονται από τον χρήστη. Η
   συνάρτηση f(x,y) είναι:
                        
                         x-y, x>=0, y>=0
                         x-y³, x>=0, y<0
               f(x,y)=   x³-y, x<0, y>=0
                         x³-y³, x<0, y<0
""" 

x = float(input("Δώσε την τιμή του x: "))
y = float(input("Δώσε την τιμή του y: "))
apotelesma = 0
if(x >= 0 and y >= 0):
    apotelesma = x - y
elif(x >= 0 and y < 0):
    apotelesma = x - y ** 3
elif(x < 0 and y >= 0):
    apotelesma = x ** 3 - y
elif(x < 0 and y < 0):
    apotelesma = x ** 3 - y ** 3
else:
    print("Λάθος εισαγωγή κάποιας τιμής.")
print("Για x=",x,"και y=",y,"έχουμε f(x,y) =",apotelesma)    