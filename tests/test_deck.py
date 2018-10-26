# from cards import Card

# testQueen = Card('Heart',12)
# testJack = Card('Club',11)
# testAce = Card('Diamond',1)
# testKing = Card('Spade',13) 
# testCard = Card('Club',2)
# testInvalid = Card('Hearts',32)

# print(testQueen)
# print(testJack)
# print(testAce)
# print(testKing)
# print(testCard)
# print(testInvalid)
import sys
sys.path.append('../testers')
from deck import Deck
from hand import Hand

max_hand_size = 2
h1 = Hand(max_hand_size)
h2 = Hand(max_hand_size)
board = []
deck = Deck()

x = 0 
while x < max_hand_size:
    h1.addCard(deck.deal())
    h2.addCard(deck.deal())
    x+=1

for card in h1.getHeldCards():
    print(card,end ='')



    



