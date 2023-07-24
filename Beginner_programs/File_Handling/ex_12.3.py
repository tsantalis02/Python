# -*- coding: utf-8 -*-
"""
   File name: ex_12.3.py
   
   *-----------------------------------------------
   
   Να γράψετε πρόγραμμα που θα ανοίγει ένα αρχείο κειμένου και θα εμφανίζει μόνο το κείμενο που είναι μέσα σε διπλά 
   εισαγωγικά ("").
"""
import re

input = open("file02.txt", 'r', encoding = "utf8")
quotes = re.findall(r'"[^"]*"', input.read(), re.U)
print(quotes)