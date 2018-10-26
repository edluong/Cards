from pokerutil import PokerUtil
from hand import Hand
from cards import Card
from player import Player

pu = PokerUtil()

# is a pair
h = Hand(5)
h1 = Hand(5)

h.addCard(Card('Heart',13))
h.addCard(Card('Club',10))
h.addCard(Card('Diamond',11))
h.addCard(Card('Club',1))
h.addCard(Card('Heart',12))

#print(pu.handRanking(h))
print(pu.isStraight(h))

#is not a pair
h1.addCard(Card('Heart',13))
h1.addCard(Card('Club',13))
h1.addCard(Card('Diamond',13))
h1.addCard(Card('Club',7))
h1.addCard(Card('Heart',8))

#print(pu.handRanking(h1))


p = Player('Ed', hand = h)

#print(p.getHeldHand())





