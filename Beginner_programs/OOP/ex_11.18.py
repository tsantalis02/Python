# -*- coding: utf-8 -*-
"""
   File name: ex_11.18.py
   
   *----------------------------------------------------------------

   Να γράψετε πρόγραμμα για το παιχνίδι της κρεμάλας. Ο υπολογιστής θα επιλέγει τυχαία μια λέξη (από μια έτοιμη για αυτόν 
   τον σκοπό λίστα) και ο παίκτης θα επιλέγει γράμματα. Θα πρέπει να υπάρχουν μέθοδοι για την εύρεση γραμμάτων ή όχι μέσα 
   στη λέξη, εμφάνιση της κρεμάλας στην οθόνη και έλεγχο τερματισμού του παιχνιδιού.
"""

import random

            
class Hangman():

      def __init__(self,word):

           self.word = word            
       
           
      def guess(self):
           
            self.turns = 5
            self.guesses = ''
            while self.turns > 0:         
                self.failed = 0
                Hangman.printHangman(self)
                if self.failed == 0 :        
                    print()
                    print ("Κέρδισες :)")
                    break
                guess = input(" μάντεψε έναν χαρακτήρα:") 
                self.guesses += guess
               
                
                if guess not in self.word:  
                 self.turns -= 1
                 print ("Λάθος μαντεψιά")
                 print ("Έχεις", self.turns, 'ακόμα μαντεψιές.' )
                if self.turns == 0:
                   print ("Έχασες :(")
            print(Hangman.display_hangman(self))        
             
      def display_hangman(self):
       stages = [  
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                #
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
            
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
         ]
       return stages[self.turns]     
            
      def printHangman(self):
          
            for char in self.word:      
                if char in self.guesses:    
                    print (char,end = "")
                else:
                    print ("_",end="")
                    self.failed += 1  
            
l = ['secret','hangman','mechanic']            
H01 = Hangman(random.choice(l))
H01.guess()
            
            
            