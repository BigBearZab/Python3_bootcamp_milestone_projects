# -*- coding: utf-8 -*-
"""
Card draw function. Generates a full deck with no suits (unecessary). Using a draw function will add a card to the hand requesting
Deck must be fed in every time to run down cards and change probability.
Standard randint used to seed time

@author: denis
"""
from random import randint

# generate deck
deck = 4*[2,3,4,5,6,7,8,9,10,'J','Q','K','A']


#draw a card from the deck and reduce value of deck
def card_draw(deck, hand):
    len_deck = len(deck)
    card_drawn = randint(0,len_deck-1)
    hand.append(deck[card_drawn])
    del(deck[card_drawn])
    return hand
    return deck
    
