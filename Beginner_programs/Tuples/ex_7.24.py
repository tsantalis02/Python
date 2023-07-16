# -*- coding: utf-8 -*-
"""
   File name: ex_7.24.py
   
   *---------------------------------------------------
   
   Για δοσμένη πλειάδα εμφανίστε το 1ο μισό σε φθίνουσα και το 2ο μισό της σε αύξουσα διάταξη.
"""

tup = 1,3,6,2,4,7,8,9,0
l_01 = list()
l_02 = list()
for i in range(len(tup) // 2):
    l_01.append(tup[i])
l_01.sort(reverse=True)
print("1ο μισό:",l_01)
for i in range(len(tup)//2,len(tup)):
    l_02.append(tup[i])    
l_02.sort()
print("2ο μισό:",l_02)    