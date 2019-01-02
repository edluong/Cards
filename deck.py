from random import shuffle

class Deck():
    def __init__(self):

        SUITS = ['Heart','Diamond','Spade','Club']
        LOW_CARD_VAL = 2
        HIGH_CARD_VAL = 14 # represented for Aces
        # initialized a deck of cards
        # 14 will stand for Aces; Most cases Aces in which Aces are high card. Will hardcode in when evaluating in straight
        self.cards = [(suit,value) for suit in SUITS for value in range(LOW_CARD_VAL,HIGH_CARD_VAL + 1)]
      
    def deal(self):
        # deals the top card from the deck
        return self.cards.pop(0)
    
    # shuffle the deck
    def shuffle(self):
        shuffle(self.cards) # method from random module

    # print the deck. Mainly used for testing
    def printDeck(self):
        for card in self.cards:
            print(card)

    def printDeckSize(self):
        print(len(self.cards))        