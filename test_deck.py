from deck import Deck

d = Deck()

# test to see if the deck was initiated correctly
# d.printDeck()

# test if shuffle method is working correctly
d.shuffle()
d.printDeck()

# test the deal function
print('\n')
print(d.deal())
print(d.deal())
print('\n')
d.printDeckSize()