# -*- coding: utf-8 -*-
"""
   File name: ex_9.4.py
   
   *----------------------------------
   
   Να γράψετε λεξικό με 5 κλειδιά τις ονομασίες λογ,δυν,ημ,συν,εφ και τιμές τις μαθηματικές συναρτήσεις για τον λογάριθμο,τη
   δύναμη, το ημίτονο, το συνημίτονο και την εφαπτομένη. Να γίνει η χρήση τους δοκιμαστικά με κάποιους αριθμούς.
"""

import math

pl = int(input("Δώσε το πλήθος των αριθμών: "))
l_01 = ['λογ','δυν','ημ','συν','εφ']
l_02 = list()
for i in range(pl):
    x = eval(input("Δώσε αριθμό: "))
    l_02.append(math.log10(x))
    l_02.append(math.pow(x, x))
    l_02.append(math.sin(x))
    l_02.append(math.cos(x))
    l_02.append(math.tan(x))
    d = dict(zip(l_01,l_02))
    print(d)