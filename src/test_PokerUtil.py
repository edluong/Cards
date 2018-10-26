from pokerutil import PokerUtil
from hand import Hand
from cards import Card
from player import Player

pu = PokerUtil()

nothin = Hand(5)
pair = Hand(5)
trips = Hand(5)
straight = Hand(5)
flush = Hand (5)
fullhouse = Hand(5)
quads = Hand(5)
straightflush = Hand(5)

# load a nothing hand (Darn :/, time to fold)
nothin.addCard(Card('Club',6))
nothin.addCard(Card('Heart',10))
nothin.addCard(Card('Spade',11))
nothin.addCard(Card('Diamond',1))
nothin.addCard(Card('Club',12))

# load a pair hand (Aces, baby!)
pair.addCard(Card('Heart',1))
pair.addCard(Card('Club',1))
pair.addCard(Card('Diamond',12))
pair.addCard(Card('Club',7))
pair.addCard(Card('Heart',8))

# load a pair of trips (AKA three of a kind)
trips.addCard(Card('Heart',13))
trips.addCard(Card('Club',13))
trips.addCard(Card('Diamond',13))
trips.addCard(Card('Club',7))
trips.addCard(Card('Heart',8))

print(pu.handRanking(nothin))
print(pu.handRanking(pair))
print(pu.handRanking(trips))

