from pokerutil import PokerUtil
from hand import Hand
from cards import Card
from player import Player

pu = PokerUtil()

# is a pair
h = Hand(5)
h1 = Hand(5)

h.addCard(Card('Heart',13))
h.addCard(Card('Club',13))
h.addCard(Card('Diamond',2))
h.addCard(Card('Club',7))
h.addCard(Card('Heart',8))

# true
if pu.isPair(h):
    print('pass!')
else:
    print('fail...')

#is not a pair
h1.addCard(Card('Heart',13))
h1.addCard(Card('Club',4))
h1.addCard(Card('Diamond',2))
h1.addCard(Card('Club',7))
h1.addCard(Card('Heart',8))

# fail
if pu.isPair(h1):
    print('pass!')
else:
    print('fail...')

#print(h.getHeldCards())


p = Player('Ed', hand = h)

#print(p.getHeldHand())





