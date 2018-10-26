from hand import Hand
from cards import Card

h = Hand(5)
h.addCard(Card('Heart',13))
h.addCard(Card('Club',13))
h.addCard(Card('Diamond',2))
h.addCard(Card('Club',7))
h.addCard(Card('Heart',8))

for rank in h.getHandRanks():
    print(rank)