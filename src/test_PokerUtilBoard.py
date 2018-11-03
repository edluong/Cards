from deck import Deck
from pokerutil import PokerUtil
from hand import Hand

deck = Deck()
board = []
hero_hand = Hand(7)
villans_hand = Hand(7)
pu = PokerUtil()

# shuffle the deck
deck.shuffleDeck()

#deal to the hero hand
hero_hand.addCard(deck.deal())
hero_hand.addCard(deck.deal())


#deal to the villans hand
# villans_hand.addCard(deck.deal())
# villans_hand.addCard(deck.deal())

#show hero hand
print("Hero's hand:")
for card in hero_hand.getHeldCards():
    print(card)

# print("---------------------------")

# #show villans hand
# print("Villan's hand:")
# for card in villans_hand.getHeldCards():
#     print(card)

print("---------------------------")

# deal to the flop
print('The Flop:')
board.append(deck.deal())
board.append(deck.deal())
board.append(deck.deal())

for card in board:
    print(card)

print("---------------------------")
print('Hero has on the flop:')

for card in board:
    hero_hand.addCard(card)

print(pu.handRanking(hero_hand))

print("---------------------------")

# print("---------------------------")
# print('Villan has on the flop:')

# for card in board:
#     villans_hand.addCard(card)

# print(pu.handRanking(villans_hand))

'''implement river card Ranking function '''
# deal the turn
turn = deck.deal()
board.append(turn)

for card in board:
    print(card)

hero_hand.addCard(turn)

print("---------------------------")
print('Hero has on the turn:')

# implement the more than 5 card ranking algorithm here

#board_and_hand = hero_hand.getHandRanks()

for card in pu.pair_count_sort(hero_hand):
    print(card)

# if there are pairs detected
#if(len(set(board_and_hand)) < len(board_and_hand)):
    # remove the lowest single cards
    # take highest pair and fill in all the other cards
    


# deal the river
# print("---------------------------")
# print('Hero has on the river:')