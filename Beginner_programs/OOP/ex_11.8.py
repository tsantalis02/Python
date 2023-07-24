# -*- coding: utf-8 -*-
"""
   File name: ex_11.8.py
   
   *-----------------------------------------------------
   
   Μια από τις πρώτες κατηγορίες παιχνιδιών για υπολογιστή ήταν εκείνη των text adventures και  role playing. 
   Δημιουργήστε ένα παιχνίδι που θα περιλαμβάνει τις κλάσεις: Ήρωας, Κακός και Χάρτης, με αντικείμενα, όπλα και τοποθεσίες
   που θα μπορεί να συλλέξει και να επισκεφθεί ο παίκτης. Να γίνει υλοποίηση των λειτουργιών: Μετακίνηση του παίκτη στον 
   χάρτη, Συλλογή αντικειμένων και Μάχη με τον εχθρό.
"""

class Hero():
    
    guns = []
    
    def __init__(self,name):
       
        self.name = name
     
    def fight(self,bad_guy):
        print(self.name,"fights with",bad_guy)
    
    def collectItem(self,gun):
        
        Hero.guns.append(gun)
      
    def visit(self,location):
        
        if location in Map.locations:
            print(self.name,"visits",location)
        else:
            print("There is no location named",location)
    
class Badguy():
    
    guns = []

    def __init__(self,name):
       
          self.name = name
        
    def collectItem(self,gun):
        
        Badguy.guns.append(gun)
        
    def visit(self,location):
        
        if location in Map.locations:
            print(self.name,"visits",location)
        else:
            print("There is no location named",location)
        
class Map():

  locations = []
    
  def __init__(self,name,location):
        
        self.name = name
        Map.locations.append(location)
        
        
        
l01 = Map('BattleLand','Castle')
l02 = Map('BattleLand','Beach')
print(Map.locations)
h = Hero('Batman')
bg = Badguy('Joker')
h.visit('Castle')
h.collectItem('BatBoomerang')
h.collectItem('Grenades')
print(h.name,"'s guns: ",h.guns,sep = "")
bg.visit('Castle')
bg.collectItem('Shotgun')
bg.collectItem('Knife')
print(bg.name,"'s guns: ",bg.guns,sep = "")
h.fight(bg.name)

        
        
        
        
        