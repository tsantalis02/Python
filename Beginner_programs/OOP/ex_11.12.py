# -*- coding: utf-8 -*-
"""
   File name: ex_11.12.py
   
   *-------------------------------------
   
   Να δημιουργηθεί κλάση για την κρυπτογράφηση δοσμένου κειμένου. 
"""

from cryptography.fernet import Fernet



class Encrypt():

  def encrypt(self,input_string):  
   key = Fernet.generate_key()
   f = Fernet(key)
   encrypted_string = f.encrypt(input_string.encode()) 
   print("Original String:", input_string)
   print("Encrypted String:", encrypted_string)
   
   
input_string = input("Γράψε ότι θες: ")
string = Encrypt()
string.encrypt(input_string)   