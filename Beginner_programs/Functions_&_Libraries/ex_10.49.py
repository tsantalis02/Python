# -*- coding: utf-8 -*-
"""
   File name: ex_10.49.py
   
   *--------------------------------------------------
   
   ΝΑ γράψετε συνάρτηση που θα δέχεται έναν τριψήφιο αριθμό και θα εμφανίζει όλους τους πιθανούς συνδυασμούς των ψηφίων του.
"""

def combinations(n):
    ps_01 = n // 100
    ps_02 = n % 100 // 10
    ps_03 = n % 100 % 10
    l = list()
    l.append(ps_01)
    l.append(ps_02)
    l.append(ps_03)
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if (i!=j and j!=k and i!=k):
                    print(l[i], l[j], l[k])




n = int(input("Δώσε έναν τριψήφιο αριθμό: "))
combinations(n)