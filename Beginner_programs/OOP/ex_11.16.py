# -*- coding: utf-8 -*-
"""
   File name: ex_11.16.py
   
   *------------------------------------------------------------
   
   Να δημιουργηθεί πρόγραμμα για το παιχνίδι της τρίλιζας. Οι λειτουργίες θα αφορούν τις επιλογές των δύο παικτών, τον
   έλεγχο για νικητή και την εμφάνιση του πίνακα του παιχνιδιού στην οθόνη.
"""

class Player(object):
    def __init__(self, name, symbol, initial_score=0):
        self.name = name
        self.symbo = symbol
        self.score = initial_score

    def won_match(self):
        self.score += 100

    def lost_match(self):
        self.score -= 50

    def show_score(self):
        print('Παίκτη {}: {} νίκες'.format(self.name, self.score))

class PlayingField(object):
    def __init__(self):
        self.field = [
                     [None, None, None],
                     [None, None, None],
                     [None, None, None]
                    ]

    def show_field(self):
        for row in self.field:
            for player in row:
                print('_' if player is None else player.symbol,end = ' ')
            print()

    def set_player(self, x, y, player):
        if self.field[y][x] is not None:
            return False

        self.field[y][x] = player

        return True

    def full_board(self):
     for row in self.field:
        for col in row:
            if col is None:
                return False
        return True

    def check_won(self, x, y, player):
     if self.field[0][x] == player and self.field[1][x] == player and self.field[2][x] == player:
        return True
     elif self.field[y][0] == player and self.field[y][1] == player and self.field[y][2] == player:
        return True
     elif self.field[0][0] == player and  self.field[1][1] == player and self.field[2][2] == player:
        return True
     elif self.field[0][2] == player and  self.field[1][1] == player and  self.field[2][0] == player:
        return True
     else:
        return False



name_1 = input('Όνομα πρώτου παίκτη: ')
name_2 = input('Όνομα δεύτερου παίκτη: ')

players = [
              Player(name_1, 'X'),
              Player(name_2, 'O')
              ]

field= PlayingField()

while True:
        for player in players:
            field.show_field()

            x= int(input('Παίκτη {} διάλεξε στήλη: '.format(player.name))) - 1

            y= int(input('Παίκτη {} διάλεξε σειρά: '.format(player.name))) - 1

            if not field.set_player(x, y, player):
                print('Το κουτάκι είναι κατειλλημένο.')

            elif field.full_board():
             field.show_field()
             print('γεμάτη τρίλιζα')
             for player in players:
                print('{}: {}'.format(player.name, player.score))
             field= PlayingField()

            elif field.check_won(x,y,player):
                field.show_field()
                print('Ο παίκτης {} κέρδισε το παιχνίδι.'.format(player.name))
                print('Score')
                for player in players:
                    if field.check_won(player) == True:
                        player.won_match()
                    elif field.check_won(player) == False:
                        player.lost_match()
                    print('{}: {}'.format(player.name, player.score))
                field= PlayingField()