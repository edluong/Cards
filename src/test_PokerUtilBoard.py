from deck import Deck
from pokerutil import PokerUtil
from hand import Hand

deck = Deck()
board = []
hero_hand = Hand(5)
villans_hand = Hand(5)
pu = PokerUtil()

# shuffle the deck
deck.shuffleDeck()

#deal to the hero hand
hero_hand.addCard(deck.deal())
hero_hand.addCard(deck.deal())


#deal to the villans hand
villans_hand.addCard(deck.deal())
villans_hand.addCard(deck.deal())

#show hero hand
print("Hero's hand:")
for card in hero_hand.getHeldCards():
    print(card)

print("---------------------------")

#show villans hand
print("Villan's hand:")
for card in villans_hand.getHeldCards():
    print(card)

print("---------------------------")

# deal to the flop
board.append(deck.deal())
board.append(deck.deal())
board.append(deck.deal())

for card in board:
    print(card)

print("---------------------------")
print('Hero has on the flop:')

for card in board:
    hero_hand.addCard(card)

# print(pu.flushOrStraight(hero_hand))
# print(pu.handPairRank(hero_hand))
print(pu.handRanking(hero_hand))

print("---------------------------")
print('Villan has on the flop:')

for card in board:
    villans_hand.addCard(card)

# print(pu.flushOrStraight(villans_hand))
# print(pu.handPairRank(villans_hand))
print(pu.handRanking(villans_hand))