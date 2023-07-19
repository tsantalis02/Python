# -*- coding: utf-8 -*-
"""
   File name: ex_10.13.py
   
   *-------------------------------------------------
   
   Να γράψετε συναρτήσεις που θα υλοποιούν τις λειτουργίες της ένωσης, της τομής και της διαφοράς δυο λιστών.
"""

def uni(s_01,s_02):
    return(s_01.union(s_02))

def inter(s_01,s_02):
    return(s_01.intersection(s_02))

def diff(s_01,s_02):
    return(s_01.difference(s_02))

s = {1,2,3}
k = {3,4,5}
set_uni = uni(s,k)
print("Union:",set_uni)
set_inter = inter(s,k)
print("Intersection:",set_inter)
set_diff_s = diff(s,k)
set_diff_k = diff(k,s)
print("Difference for s:",set_diff_s)
print("Difference for k:",set_diff_k)