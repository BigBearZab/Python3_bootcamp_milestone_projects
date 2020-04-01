# -*- coding: utf-8 -*-
"""
Player object

@author: denis
"""
#from card_draw import card_draw

class Player():
    
    def __init__(self,hand=[],money=100,hand_tot=0,status='ok',cur_bet=0):
        self.hand = hand
        self.money = money
        self.hand_tot = hand_tot
        self.status = status
        self.cur_bet = cur_bet
        
    def __str__(self):
        return(f'Your hand: {self.hand}\nYou have: £{str(self.money)}\nYour running hand value: {self.hand_tot} \nYour status is: {self.status}\nCurrent bet is: £{self.cur_bet}')
        
    
    def hit(self):
        card_draw(deck,self.hand)
        self.hand_tot = cardsum(self.hand)
        print(f'Your hand is: {self.hand}')
        if self.hand_tot != 'bust':
            status = 'ok'
        else:
            self.status = 'bust'
            
    def bet(self,bet):
#        bet = input('Please enter how much you would like to bet: ')
        try:
            self.money = self.money - bet
            self.cur_bet = bet
        except:
            print('Please enter an integer value')
            
            

        