class Card:
    '''
        Implementation of a playing card. Representing the information using a tuple
    '''

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def displaySuit(self):
        print(self.suit)

    def displayRank(self):
        print(self.rank)

    def __str__(self):

        rankName = {
            1: 'Ace',
            11: 'Jack',
            12: 'Queen',
            13: 'King'
        }

        return rankName.get(self.rank,'Invalid Rank') + ' of ' + self.suit + 's'
