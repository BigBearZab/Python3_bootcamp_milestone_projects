# -*- coding: utf-8 -*-
"""
A script allowing an individual to play a simple version of blackjack.

Please enjoy. Use play_blackjack() to continue the fun after round one

@author: denis
"""
from random import randint

deck = 4*[2,3,4,5,6,7,8,9,10,'J','Q','K','A']

#Allows for drawing of cards form the deck. The outcomes will reduce as deck is used up
def card_draw(deck, hand):
    len_deck = len(deck)
    card_drawn = randint(0,len_deck-1)
    hand.append(deck[card_drawn])
    del(deck[card_drawn])
    return hand
    return deck

#will sum the hand of player or dealer. Assumes Ace high unless total over 21. Will allow 1 ace high and others low if required
def cardsum(hand):
    num_list = []
    ace_count = 0
    for card in hand:
        try:
            card == int(card)
            num_list.append(card)
        except:
            if card == 'J' or card == 'Q' or card == 'K':
                num_list.append(10)
            elif card == 'A':
                ace_count += 1
    handsum = sum (num_list)
    if ace_count > 0:
        for i in range(ace_count):
            if handsum + 11 < 22:
                handsum = handsum + 11    
            else:
                handsum = handsum + 1
    if handsum > 21:
        
        print('Total over 21')
#    else:
#        print(f'Sum of hand: {handsum}')
    return handsum

#This generates the player as an object. Since dealer has no retained values between rounds dealer is embedded into player class
class Player():
    
    def __init__(self,hand=[],money=50,hand_tot=0,status='ok',cur_bet=0,play_stat='hit'):
        self.hand = hand
        self.money = money
        self.hand_tot = hand_tot
        self.status = status
        self.cur_bet = cur_bet
        self.play_stat = play_stat
        
    def __str__(self):
        return(f'You have: £{str(self.money)}\nYour running hand value: {self.hand_tot} \nYour status is: {self.status}\nCurrent bet is: £{self.cur_bet}')
        
    
    def hit(self):
        card_draw(deck,self.hand)
        self.hand_tot = cardsum(self.hand)
        print(f'Your hand is: {self.hand}')
        if self.hand_tot < 22:
            status = 'ok'
        else:
            self.status = 'bust'
            self.play_stat = 'bust'
            self.cur_bet = 0
            
    def bet(self,bet): # bet needs to be adjusted to not allow a bet larger than total
#        bet = input('Please enter how much you would like to bet: ')
        try:
            self.money = self.money - bet
            self.cur_bet = bet
            print(f'You are betting £{self.cur_bet} and you have £{self.money} remaining')
        except:
            print('Please enter an integer value')
            
    def stick(self,deal_hand=[],deal_tot=0): # this is where the whole dealer function occurs
        if self.status == 'bust':
            print('You have lost, please try again')
        else:
            self.play_stat = 'stick'
            print(f'Your total is: {self.hand_tot}. Now the dealer plays')
            while int(deal_tot) < 50:
                if deal_tot > self.hand_tot and deal_tot < 22:
                    print('Dealer wins')
                    self.cur_bet = 0
                    print(f'You now have {self.money}')
                    break
                elif deal_tot > 21:
                    print('Dealer loses')
                    self.money = self.money + 2*self.cur_bet 
                    self.cur_bet = 0
                    print(f'You now have £{self.money}')
                    break
                
                elif deal_tot < self.hand_tot + 1:
                    card_draw(deck,deal_hand)
                    deal_tot = cardsum(deal_hand)
                    print(f'Dealer hand is:{deal_hand}')
                    print(f'Dealer total is: {deal_tot}')



p1 = Player([])

#this function is all that needs to be re-run to play the game. It will retain player settings
def play_blackjack():
    p1.hit()
    p1.hit()
    print(p1)
    play_bet = input('Please enter how much you would like to bet? ')
    p1.bet(int(play_bet))
#    print(p1)

    while p1.play_stat == 'hit':
        play_dec = input(f'Your hand is: {p1.hand} Would you like to hit or stick? ')
        if play_dec == 'hit':
            p1.hit()
            if p1.status == 'bust':
                print(f"I'm afraid you lose, please try again. You have £{p1.money} remaining")
                p1.play_stat == 'bust'
    
        elif play_dec =='stick':
            p1.stick([])
            p1.play_stat == 'stick'
        else:
            print('Please enter either hit or stick')
            
        
    
    p1.play_stat = 'hit'
    p1.status = 'ok'
    p1.hand = []
    

    
play_blackjack()


