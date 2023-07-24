# -*- coding: utf-8 -*-
"""
   File name: ex_12.4.py
   
   *---------------------------------------------------------
   
   Να γράψετε πρόγραμμα που θα διαβάζει ένα κείμενο, θα το κρυπτογραφεί με την κρυπτογράφηση του Καίσαρα και θα το 
   αποθηκεύει σε νέο δυαδικό αρχείο. Να γράψετε και την αντίστροφη εργασία ανάγνωσης του κρυπτογραφημένου κειμένου και την 
   αποθήκευση σε νέο αρχείο.
"""


with open("file.txt", encoding = "utf8") as f:
  text = f.read() 
s = 4
#encryption
result = ""
for i in range(len(text)):
      char = text[i]
      if (char.isupper()):
         result += chr((ord(char) + s-65) % 26 + 65)
      else:
         result += chr((ord(char) + s - 97) % 26 + 97)
#save in binary file         
with open("new.txt","wb") as f02:
    newFileByteArray = bytearray(result,encoding="utf8")
    f02.write(newFileByteArray)
#read binary file     
with open("new.txt","rb") as f03:
    text = f03.read()
#save in new binary file    
with open("new_02.txt","wb") as f04:
    ByteArray = bytearray(text)
    f04.write(ByteArray)    