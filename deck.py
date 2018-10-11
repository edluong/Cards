from cards import Card
from random import shuffle

class Deck:
    '''
        creates a standard deck of playing cards
        requirements:
        - Holds all of the cards
        - Shuffle the deck
    '''
    suit = ['Club','Diamond','Heart','Spade']
    rank = []
    for i in range(1,14):
        rank.append(i)
    deck = []

    def __init__(self):
        #creates the deck when an object is initialized
        for suit in self.suit:
            for rank in self.rank:
                self.deck.append(Card(suit,rank))
    
    # print the content of the deck out
    def displayDeck(self):
        for card in self.deck:
            print(card,end="\n")
   
    # shuffle the deck
    def shuffleDeck(self):
        shuffle(self.deck)
    