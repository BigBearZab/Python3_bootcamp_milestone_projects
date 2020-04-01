# -*- coding: utf-8 -*-
"""
Takes a given hand at calculates the black jack value. Will correctly decide the value of aces depending on how many have been drawn.
Takes argument of cards in a hand as a list and returns a sum as an integer

@author: denis
"""

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
        handsum = 'bust'
        print('Bad luck, you have gone bust')
    else:
        print(f'Sum of hand: {handsum}')
    return handsum
   
    
