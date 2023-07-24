# -*- coding: utf-8 -*-
"""
   File name: ex_12.6.py
   
   *-----------------------------------------------------
   
   Ένα αρχείο περιέχει τις παραγγελίες προϊόντων μιας επιχείρησης. Έχει τη μορφή: όνομα προϊόντος, τεμάχια.
   Ένα προϊόν μπορεί να εμφανίζεται πολλές φορές. Να γράψετε πρόγραμμα που θα διαβάζει τις παραγγελίες, θα αθροίζει τον
   αριθμό τεμαχίων για κάθε προϊόν και θα σε νέο αρχείο τις πιο κάτω πληροφορίες.
        Όνομα προϊόντος, αριθμός παραγγελιών, συνολικά τεμάχια
"""



from collections import OrderedDict
import csv


f = open("products.txt", "rt", encoding = "utf8")
l_01 = list()
l_02 = list()
l_03 = list()
l_04 = list()
l_05 = list()
for line in f:
    l_01.append(line[0])
    l_02.append(int(line[3:5])) 
for i in range(len(l_01)):
    for j in range(len(l_01)):
        if i != j and l_01[i] == l_01[j]:
           x = int(l_02[i]) 
           y = int(l_02[j])
           l_03.append(l_01[i])
           l_04.append(x + y)
d_01 = dict(zip(l_03,l_04))
d_02 = dict(zip(l_01,l_02))      
print(d_01)
print(d_02)

output = {}
for d in (d_01, d_02):
    for k, v in d.items():
        output.setdefault(k, float('-inf'))
        output[k] = max(output[k], v)

dict1 = OrderedDict(sorted(output.items()))
output = dict(dict1)
print(output)

s_01 = set(l_01)
s_01 = sorted(s_01)
for i in s_01:
  l_05.append(l_01.count(i))
l_06 = list(s_01)
dict2 = dict(zip(l_06,l_05))      
final = {}
for d in (dict2,output):
    for k,v in d.items():
        final.setdefault(k,0)
        final[k] = dict2[k],v 

print(final)


headers = ['a','b','c','d']
        
with open("sales.txt","a",encoding="utf8") as f02:
    writer = csv.DictWriter(f02,fieldnames=headers)
    writer.writeheader()
    writer.writerow(final)



