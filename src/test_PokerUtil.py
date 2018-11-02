from pokerutil import PokerUtil
from hand import Hand
from cards import Card
from player import Player
import collections

pu = PokerUtil()

nothin = Hand(5)
pair = Hand(5)
two_pair = Hand(5)
trips = Hand(5)
straight = Hand(5)
flush = Hand (5)
fullhouse = Hand(5)
quads = Hand(5)
straight_flush = Hand(5)

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

# Top TWO
two_pair.addCard(Card('Heart',1))
two_pair.addCard(Card('Club',1))
two_pair.addCard(Card('Heart',13))
two_pair.addCard(Card('Club',13))
two_pair.addCard(Card('Heart',8))

# load a pair of trips (AKA three of a kind)
trips.addCard(Card('Heart',13))
trips.addCard(Card('Club',13))
trips.addCard(Card('Diamond',13))
trips.addCard(Card('Club',7))
trips.addCard(Card('Heart',8))

# Straight
straight.addCard(Card('Heart',1))
straight.addCard(Card('Club',10))
straight.addCard(Card('Diamond',11))
straight.addCard(Card('Club',12))
straight.addCard(Card('Heart',13))


# flush
flush.addCard(Card('Spade',6))
flush.addCard(Card('Spade',10))
flush.addCard(Card('Spade',11))
flush.addCard(Card('Spade',1))
flush.addCard(Card('Spade',12))

# fullhouse (AKA boat)
fullhouse.addCard(Card('Heart',13))
fullhouse.addCard(Card('Club',13))
fullhouse.addCard(Card('Diamond',13))
fullhouse.addCard(Card('Club',8))
fullhouse.addCard(Card('Heart',8))

# quads
quads.addCard(Card('Heart',13))
quads.addCard(Card('Club',13))
quads.addCard(Card('Diamond',13))
quads.addCard(Card('Spade',13))
quads.addCard(Card('Heart',8))

#straight flush
straight_flush.addCard(Card('Spade',1))
straight_flush.addCard(Card('Spade',10))
straight_flush.addCard(Card('Spade',11))
straight_flush.addCard(Card('Spade',12))
straight_flush.addCard(Card('Spade',13))

'''
base test to see if handRanking method is working correctly
useful for regression testing
'''
# print(pu.handRanking(nothin))
# print(pu.handRanking(pair))
# print(pu.handRanking(two_pair))
# print(pu.handRanking(trips))
# print(pu.handRanking(straight))
# print(pu.handRanking(flush))
# print(pu.handRanking(fullhouse))
# print(pu.handRanking(quads))
# print(pu.handRanking(straight_flush))

# print(pu.flushOrStraight(nothin))
# print(pu.handPairRank(pair))
# print(pu.handPairRank(two_pair))
# print(pu.handPairRank(trips))
# print(pu.flushOrStraight(straight))
# print(pu.flushOrStraight(flush))
# print(pu.handPairRank(fullhouse))
# print(pu.handPairRank(quads))
# print(pu.flushOrStraight(straight_flush))
# print(pu.handPairRank(nothin))


# testing getPairList() for 7 cards (board and hand)

# board_and_hand = Hand(7)

# board_and_hand.addCard(Card('Spade',12))
# board_and_hand.addCard(Card('Club',13))
# board_and_hand.addCard(Card('Heart',3))
# board_and_hand.addCard(Card('Heart',13))
# board_and_hand.addCard(Card('Spade',13))
# board_and_hand.addCard(Card('Club',3))
# board_and_hand.addCard(Card('Spade',3))

# # want all cards in the pair rank list
# sorted_hand = pu.getPairList(board_and_hand,1)

# # sort the list based on Pair count then Rank
# sorted_hand.sort(key=lambda tup:(tup[1],tup[0]), reverse = True)

# print(pu.handRanking(Hand(sorted_hand[:5])))

# sorted_hand[:5][0]: 
#     print(card)


#proof you can narrow down to 5 cards
print(pair.getHeldCards()[:5])
